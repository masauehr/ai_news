# ai_news — 生成AI情報まとめ自動生成システム

生成AI（LLM・画像生成・エージェント等）の最新情報を週次・月次で自動収集し、
Markdown記事としてGitHubに公開する自動化の記録。

---

## 概要

macOS の launchd からローカルLLMエージェント（Ollama + tool calling）を呼び出し、
情報収集 → 記事生成 → git push までを自動化する。

| タイミング | エンジン | モード | 処理内容 |
|---|---|---|---|
| 毎週土曜 09:00 | Ollama（qwen3.6:35b-mlx） | 週次 | 直近7日間の生成AIニュースを収集 → 週次記事を生成・push |
| 月の第1土曜 09:00 | Ollama | 月次 | 週次記事に加えて月次まとめ記事も生成・push |
| 毎週土曜 10:00 | Ollama（ornith-1.5:35b／比較用サブモデル） | 週次 | 同じ週の記事を `articles/weekly_ornith/` に生成・push（README/index更新なし） |
| 毎週土曜 11:00 | Ollama（nemotron-3.5-lightning:30b-mlx／比較用サブモデル） | 週次 | 同じ週の記事を `articles/weekly_nemotron/` に生成・push（README/index更新なし） |
| 毎週土曜 13:00 | Claude Haiku（Anthropic API） | 週次 | 同じ週の記事を別ファイルに生成・push → その週に揃った全モデルの比較ページを自動生成 |
| 月の第1土曜 13:00 | Claude Haiku（Anthropic API） | 月次 | Haiku版月次まとめを生成・push → 月次比較ページも自動生成 |

> 比較用サブモデル（ornith / nemotron）は `run_ai_news.sh` を `AI_NEWS_VARIANT=<key>` 付きで起動する軽量モード。
> 記事生成と push のみを行い、README.md / index.md / 一覧ページの更新・月次生成はしない。
> モデルは https://masauehr.github.io/local_agent/ の比較で選定したローカルモデル。

> **変更履歴**
> - 2026-05-17: 「毎日 09:00 チェック」→「毎週土曜 09:00」に変更
> - 2026-05-24: 記事生成エンジンを Claude CLI → **Ollama ローカルLLM** に変更
> - 2026-05-25: **Claude Haiku（Anthropic API）による並行実行 + モデル比較ページ自動生成を追加**
> - 2026-05-31: **ファイル名・期間ラベルの基準を「実行日」ベースに変更**（実行日7日前〜実行日を対象期間とする）
> - 2026-06-07: **Haiku月次記事・月次比較ページを追加**。Sonnet評価セクション（`.sonnet-eval`）をcompare layoutに追加。ホームページをSonnet評価付き最新比較に変更。フッター表記を修正。
> - 2026-08-28: **比較用ローカルモデル2種（ornith-1.5:35b／土曜10:00、nemotron-3.5-lightning:30b-mlx／土曜11:00）を追加**。`run_ai_news.sh` に `AI_NEWS_VARIANT` モードを実装（`articles/weekly_<key>/` に保存・後処理なし）。`generate_compare.py` をその週に揃った全モデル対応に拡張（メイン2カラム＋追加モデル縦積み、Sonnet評価も全モデル対象）。`compare.html` に ornith/nemotron 用CSSを追加。

---

## 成果物

| ファイル | 内容 | 生成エンジン | 更新頻度 |
|---|---|---|---|
| `articles/weekly/YYYY-MMDD.md` | Ollama 週次記事（8〜12トピック） | Ollama（qwen3.6:35b-mlx） | 毎週土曜 09:00 |
| `articles/weekly_ornith/YYYY-MMDD.md` | 比較用サブモデル週次記事 | Ollama（ornith-1.5:35b） | 毎週土曜 10:00 |
| `articles/weekly_nemotron/YYYY-MMDD.md` | 比較用サブモデル週次記事 | Ollama（nemotron-3.5-lightning:30b-mlx） | 毎週土曜 11:00 |
| `articles/haiku_weekly/YYYY-MMDD.md` | Haiku 週次記事（同じ週を別視点で生成） | Claude Haiku | 毎週土曜 13:00 |
| `articles/compare/YYYY-MMDD.md` | その週に揃った全モデルの週次記事を並べた比較ページ（メイン2カラム＝qwen3.6 vs Haiku＋追加モデル縦積み、Sonnet評価付き） | generate_compare.py | 毎週土曜 13:00以降 |
| `articles/monthly/YYYY-MM.md` | Ollama 月次まとめ記事 | Ollama | 毎月第1土曜 |
| `articles/haiku_monthly/YYYY-MM.md` | Haiku 月次まとめ記事 | Claude Haiku | 毎月第1土曜 13:00 |
| `articles/compare/monthly-YYYY-MM.md` | Ollama と Haiku の月次記事を2カラムで並べた比較ページ（Sonnet評価付き） | generate_compare.py | 毎月第1土曜 13:00以降 |
| `README.md` | 最新記事一覧（自動更新） | — | 記事生成時 |

GitHub URL: https://github.com/masauehr/ai_news  
公開サイト: https://masauehr.github.io/ai_news/

---

## 仕組み（現行: 2エンジン並行 + 比較ページ自動生成）

### Ollama 実行フロー（09:00）

```
launchd（毎週土曜 09:00）
  ↓
run_ai_news.sh が起動
  ↓
実行日分のファイル（articles/weekly/YYYY-MMDD.md、MMDD=実行日）が存在する？
  ├─ Yes → スキップ（数秒で終了）
  └─ No  → fetch_news.py でニュースサイトを事前スクレイピング
              ↓
            local_agent.py を起動（Ollama tool-calling エージェント）
              ↓
            ┌─ search_web()        DuckDuckGo で直近ニュースを検索
            ├─ fetch_url()         trafilatura / requests でページ取得
            ├─ write_article()     articles/weekly/ に記事を保存
            ├─ append_to_readme()  README.md にリンクを追加
            ├─ update_index()      index.md（GitHub Pages）を更新
            └─ git_commit_push()   git add / commit / push
```

### Haiku 実行フロー（13:00）

```
launchd（毎週土曜 13:00）
  ↓
run_ai_news_haiku.sh が起動
  ↓
今日が月の第1土曜日か？（DAY_OF_MONTH <= 7）
  ├─ Yes → MODE="monthly"
  └─ No  → MODE="weekly"
  ↓
実行日分の週次ファイル（articles/haiku_weekly/YYYY-MMDD.md）が存在する？
  ├─ Yes → 比較ページが未生成なら generate_compare.py のみ実行して終了
  └─ No  → ~/.anthropic_env から ANTHROPIC_API_KEY を読み込む
              ↓
            fetch_news.py でニュースサイトを事前スクレイピング（Ollama版と共通）
              ↓
            【週次】haiku_agent.py を起動（--mode weekly）
              ↓
            ┌─ search_web()        DuckDuckGo で直近ニュースを検索
            ├─ fetch_url()         trafilatura / requests でページ取得
            ├─ write_article()     articles/haiku_weekly/ に記事を保存
            ├─ append_to_readme()  README.md の「Haiku週次まとめ」セクションにリンクを追加
            ├─ update_index()      articles/haiku_weekly/index.md を更新
            └─ git_commit_push()   git add / commit / push
              ↓
            MODE == "monthly" かつ月次ファイル（articles/haiku_monthly/YYYY-MM.md）が未生成？
              ├─ Yes → 【月次】haiku_agent.py を起動（--mode monthly）
              │          ↓
              │        ┌─ read_file()        Ollama版月次記事を参照
              │        ├─ search_web()       月次補足情報を収集
              │        ├─ write_article()    articles/haiku_monthly/ に月次記事を保存
              │        ├─ append_to_readme() README.md の「Haiku月次まとめ」セクションに追加
              │        ├─ update_index()     articles/haiku_monthly/index.md を更新
              │        └─ git_commit_push()  git add / commit / push
              └─ No  → 月次生成スキップ
              ↓
            Ollama 版週次記事（articles/weekly/YYYY-MMDD.md）が存在する？
              ├─ Yes → generate_compare.py を実行（週次比較ページ生成）
              │          ↓
              │        両記事を読み込んで 2カラム比較ページ + Sonnet評価を生成
              │        articles/compare/YYYY-MMDD.md を保存
              │        articles/compare/index.md を更新
              │        git commit / push
              └─ No  → 比較ページ生成をスキップ（警告ログを記録）
              ↓
            MODE == "monthly" かつ月次比較ファイルが未生成？
              ├─ Yes → generate_compare.py を実行（月次比較ページ生成）
              │          ↓
              │        articles/compare/monthly-YYYY-MM.md を保存
              │        git commit / push
              └─ No  → 月次比較スキップ
```

### エージェントの動作詳細

#### Ollama エージェント（`local_agent.py`）

Ollama の `/api/chat` API（tool calling 対応）を使う。

1. システムプロンプトに「収集すべきキーワード・手順・フォーマット」を渡す
2. LLMが `search_web` / `fetch_url` を自律的に呼び出して情報収集する
3. 十分な情報が集まったら `write_article` で記事を生成する
4. `append_to_readme` → `update_index` → `git_commit_push` の順で後処理を実行する
5. 最大40ターンでループを打ち切る

**デフォルトモデル:** `qwen3.6:35b-mlx`（環境変数 `AI_NEWS_MODEL` で変更可能）

**比較用サブモデルモード（`AI_NEWS_VARIANT`）:**
`run_ai_news.sh` を `AI_NEWS_VARIANT=ornith`（または `nemotron`）付きで起動すると:
- ログ: `ai_news_<variant>.log`／実行済み判定ファイル: `articles/weekly_<variant>/YYYY-MMDD.md`
- 常に週次モード（月次判定はスキップ）
- `local_agent.py --variant <variant>` が `VARIANT_SYSTEM_PROMPT_TMPL`（簡略版）を使う
  → 情報収集 → `write_article`（`articles/weekly_<variant>/` へ）→ `git_commit_push`（その1ファイルのみ）
  → `append_to_readme` / `update_index` は呼ばない
- launchd 登録は `com.user.ai_news_ornith.plist`（土曜10:00）/ `com.user.ai_news_nemotron.plist`（土曜11:00）。
  モデル名・variant は各 plist の `EnvironmentVariables`（`AI_NEWS_MODEL` / `AI_NEWS_VARIANT`）で指定。

#### Haiku エージェント（`haiku_agent.py`）

Anthropic SDK の tool use（`client.messages.create`）を使う。

**週次モード（`--mode weekly`）:**
1. `SYSTEM_PROMPT_WEEKLY_TMPL` を使用。収集キーワード・フォーマット指定はOllama版と同じ構造
2. `write_article` の保存先は `articles/haiku_weekly/`（Ollama版と分離）
3. `append_to_readme` は README.md の「### Haiku週次まとめ」セクションに追加
4. `update_index` は `articles/haiku_weekly/index.md` を更新

**月次モード（`--mode monthly`）:**
1. `SYSTEM_PROMPT_MONTHLY_TMPL` を使用。前月の Ollama月次記事を `read_file` で参照してサマリー生成
2. `write_article` の保存先は `articles/haiku_monthly/`
3. `append_to_readme` は README.md の「### Haiku月次まとめ」セクションに追加
4. `update_index` は `articles/haiku_monthly/index.md` を更新

**共通:**
- 最大40ターン・ループ検出・URLキャッシュ機構はOllama版と同一
- 再試行は最大2回（Ollama版は3回）

**デフォルトモデル:** `claude-haiku-4-5-20251001`（環境変数 `HAIKU_MODEL` で変更可能）

#### 比較ページ生成（`generate_compare.py`）

`run_ai_news_haiku.sh` から Haiku 記事生成の完了後に呼ばれる。

1. `collect_models()` がその週に揃っているモデル記事を検出する
   - 必須: `articles/weekly/YYYY-MMDD.md`（qwen3.6）と `articles/haiku_weekly/YYYY-MMDD.md`（Haiku）。どちらか欠けたら比較不成立でスキップ
   - 任意: `articles/weekly_ornith/YYYY-MMDD.md` / `articles/weekly_nemotron/YYYY-MMDD.md`（`VARIANT_MODELS` で定義）。あれば追加
2. Jekyll front matter を除去して本文だけを抽出する
3. `_layouts/compare.html` を使った Markdown を生成する
   - `build_compare_block()`: 比較ヘッダー（全モデルのバッジ）＋メイン2カラム（`.compare-wrapper` = qwen3.6 vs Haiku）＋追加モデル縦積み（`.compare-extra` = ornith / nemotron）
4. `generate_sonnet_eval()`: Claude Code CLI（`--model sonnet`）にその週の全モデル記事を渡し、モデル数ぶんの列を持つ評価表と総評を生成
5. `articles/compare/index.md` と `index.md` の比較セクションを更新する
6. git commit / push する（追加モデルの記事ファイルも存在すればコミット対象に含める）

> 追加モデル（ornith 10:00 / nemotron 11:00）は比較生成（13:00〜）より前に走るため通常は間に合う。
> 万一 13:00 時点で未生成なら、そのモデルはその週の比較ページから欠落する（比較ページは1回だけ生成し再生成しない）。

---

## データ収集方法

情報収集は **DuckDuckGo検索（エージェント主導）** と **BeautifulSoupによる事前スクレイピング（固定URL）** の
ハイブリッド方式を採用している。

### 方式1: DuckDuckGo検索 — エージェントが自律的に実行

LLMがシステムプロンプトの指示に従い、以下のキーワードを順番に検索する。

**一般ニュース検索:**
```
生成AI 最新ニュース 今週
LLM release 今週
OpenAI Anthropic Google AI news
AI 規制 法律 日本
arXiv LLM 注目論文
```

**注目トピック（SPEC.md 参照）:**
```
ローカルLLM Ollama 新モデル
小型LLM 量子化 最新
AIエージェント MCP AutoGen 最新動向
1-bit LLM BitNet Bonsai 最新
```

**日本政府・行政:**
```
デジタル庁 生成AI 国産AI 選定
国産LLM 新モデル リリース
```

**日本国内AI企業:**
```
日本 生成AI 企業 最新ニュース 今週
```

**Note（note.com）記事:**
```
site:note.com 生成AI 使ってみた 今週
```

### 方式2: BeautifulSoupによる事前スクレイピング — 固定URLの取得

スクリプト: `scripts/fetch_news.py`

エージェントを呼び出す **前** に Python スクリプトが各サイトの HTML を直接取得し、
記事タイトル＋URL の一覧を抽出してシステムプロンプトに含める。

| サイト | 取得方式 | 理由 |
|---|---|---|
| ITmedia AI+ | BeautifulSoup（h2/h3タグ、Shift-JIS） | 構造が安定・高速取得可 |
| Techno Edge | BeautifulSoup（URLパターン `/article/YYYY/MM/DD/`） | 過去30日分をフィルタ |
| AINOW | BeautifulSoup（URLパターン `/202X/MM/DD/`） | 2025〜2026年記事のみ |
| Anthropic News | BeautifulSoup（URLスラグから生成） | JS描画前のリンクが取得可能 |
| Hugging Face Blog | BeautifulSoup（articleタグ） | 構造が安定 |
| Google DeepMind Blog | BeautifulSoup（articleタグ＋日付除去） | 構造が安定 |
| デジタル庁ニュース | `fetch_url`（エージェントが取得） | SPA構造でBeautifulSoup不可 |
| OpenAI Blog | `fetch_url`（エージェントが取得） | 403エラーが発生するため |

### 方式3: fetch_url — エージェントが必要に応じて取得

LLMが `fetch_url` ツールを呼び出し、trafilatura でメインコンテンツを抽出する。
BeautifulSoup で取得できない JS 描画ページや特定 URL の詳細取得に使用。

---

## ファイル構成

```
~/projects/ai_news/
├── README.md                              # 概要・最新記事一覧（GitHub公開）
├── SPEC.md                                # 収集対象・記事フォーマット仕様（GitHub公開）
├── CLAUDE.md                              # Claude向け自動生成指示（ローカル専用・非公開）
├── index.md                               # ホームページ（GitHub Pages）最新比較 + Sonnet評価
├── _layouts/
│   ├── default.html                       # 通常記事レイアウト（GitHub Pages）
│   └── compare.html                       # 2カラム比較レイアウト（.sonnet-eval CSS含む）
├── articles/
│   ├── weekly/YYYY-MMDD.md               # Ollama 週次記事（qwen3.6、土曜 09:00）
│   ├── weekly_ornith/YYYY-MMDD.md        # 比較用サブモデル週次記事（ornith-1.5:35b、土曜 10:00）
│   ├── weekly_nemotron/YYYY-MMDD.md      # 比較用サブモデル週次記事（nemotron-3.5-lightning:30b-mlx、土曜 11:00）
│   ├── haiku_weekly/YYYY-MMDD.md         # Haiku 週次記事（土曜 13:00）
│   ├── monthly/YYYY-MM.md                # Ollama 月次まとめ記事（第1土曜）
│   ├── haiku_monthly/YYYY-MM.md          # Haiku 月次まとめ記事（第1土曜 13:00）
│   └── compare/
│       ├── YYYY-MMDD.md                  # 週次比較ページ（Sonnet評価付き）
│       └── monthly-YYYY-MM.md            # 月次比較ページ（Sonnet評価付き）
├── scripts/
│   ├── local_agent.py                     # Ollama エージェント（公開）
│   ├── haiku_agent.py                     # Haiku エージェント（公開、月次モード対応）
│   ├── generate_compare.py               # 比較ページ生成（公開）
│   ├── fetch_news.py                      # 事前スクレイピング（公開）
│   ├── run_ai_news.sh                     # Ollama launchd スクリプト（AI_NEWS_VARIANT対応、非公開）
│   ├── run_ai_news_haiku.sh              # Haiku launchd スクリプト（月次対応、非公開）
│   ├── com.user.ai_news.plist            # launchd 設定 土曜09:00 qwen3.6（非公開）
│   ├── com.user.ai_news_ornith.plist    # launchd 設定 土曜10:00 ornith（非公開）
│   ├── com.user.ai_news_nemotron.plist  # launchd 設定 土曜11:00 nemotron（非公開）
│   └── com.user.ai_news_haiku.plist     # launchd 設定 土曜13:00 Haiku（非公開）
├── ai_news.log                            # Ollama（qwen3.6）実行ログ（非公開）
├── ai_news_ornith.log                     # ornith 実行ログ（非公開）
├── ai_news_nemotron.log                   # nemotron 実行ログ（非公開）
└── ai_news_haiku.log                      # Haiku 実行ログ（非公開）
```

### GitHub公開範囲

| ファイル | GitHub公開 | 理由 |
|---|---|---|
| `README.md` / `SPEC.md` / `articles/` / `_layouts/` | ✅ 公開 | 記事本体・仕様・Jekyll テーマは公開コンテンツ |
| `scripts/local_agent.py` / `haiku_agent.py` / `generate_compare.py` / `fetch_news.py` | ✅ 公開 | 絶対パスを含まない汎用スクリプト |
| `CLAUDE.md` | ❌ 非公開 | 絶対パス等の個人情報を含む |
| `scripts/run_ai_news*.sh` / `scripts/com.user.ai_news*.plist` | ❌ 非公開 | 絶対パス等の個人情報を含む（`.gitignore` に4種の plist を明記） |
| `*.log` | ❌ 非公開 | 実行ログはローカル専用 |

---

## 収集対象トピック

SPEC.md に定義。以下の5項目を優先収集する。

| # | トピック | 主なキーワード |
|---|---|---|
| 1 | ローカル動作する小型LLM | Ollama / llama.cpp / MLX / 量子化 |
| 2 | AIエージェントの動向 | MCP / LangGraph / AutoGen / CrewAI |
| 3 | 生成AIを動かせるPC・ハードウェア | AI PC / NPU / RTX / Apple Silicon |
| 4 | 日本政府・行政機関の生成AI活用 | デジタル庁 / 国産AI選定 / 令和8年度試行 |
| 5 | 日本のAI企業・研究動向 | RakutenAI / ELYZA / SB Intuitions / PFN 等（特定企業偏重なし） |

---

## セットアップ手順（初回・再構築時）

### 1. リポジトリをクローン

```bash
git clone https://github.com/masauehr/ai_news.git ~/projects/ai_news
```

### 2. 依存ライブラリのインストール

```bash
# Ollama版・Haiku版 共通
/opt/anaconda3/bin/pip install requests beautifulsoup4 ddgs trafilatura

# Haiku版に必要（Anthropic SDK）
/opt/anaconda3/bin/pip install anthropic
```

### 3. Ollama のセットアップ

```bash
# Ollama がインストール済みであること（https://ollama.com）
ollama pull qwen3.6:35b-mlx   # デフォルトモデル（19〜21GB）
# 軽量版を使う場合
ollama pull qwen3.6:27b-mlx
```

### 4. Anthropic API キーの設定（Haiku版のみ）※2026-07-13時点で移行中・下記メモ参照

> ⚠️ **暫定情報**: 2026-07-13 に Haiku/Sonnet の実行方式を Anthropic API から
> Claude Code CLI（Pro/Maxサブスクリプション）方式に変更する作業を進めている。
> 詳細・検証状況は下記「設計判断メモ」の `2026-07-13` エントリを参照。
> 本番反映が完了したらこのセクション自体を書き換える予定（現時点では旧手順を残してある）。

```bash
# 旧方式（Anthropic API課金）: ~/.anthropic_env に API キーを記載（パーミッション 600 必須）
echo 'ANTHROPIC_API_KEY=sk-ant-...' > ~/.anthropic_env
chmod 600 ~/.anthropic_env
```

`run_ai_news_haiku.sh` が起動時に `source ~/.anthropic_env` で自動読み込みする。
`ANTHROPIC_API_KEY` 環境変数が既にシェルに設定されている場合はこのファイルは不要。

### 5. CLAUDE.md を作成（非公開・手動作成が必要）

gitに含まれていないため、手動で作成するか Claude Code で再生成する。
内容の雛形は SPEC.md の「自動実行フロー」を参照。

### 6. run_ai_news.sh を作成（非公開・手動作成が必要）

以下が現在の構成（絶対パスは環境に合わせて変更すること）：

```bash
#!/bin/bash
PROJECT_DIR="$HOME/projects/ai_news"
LOG_FILE="${PROJECT_DIR}/ai_news.log"
PYTHON_BIN="/opt/anaconda3/bin/python3"
AI_NEWS_MODEL="${AI_NEWS_MODEL:-qwen3.6:35b-mlx}"  # 環境変数で上書き可能
TODAY=$(TZ=Asia/Tokyo date +%Y-%m-%d)
DAY_OF_MONTH=$(TZ=Asia/Tokyo date +%d)
YEAR=$(TZ=Asia/Tokyo date +%Y)

# ファイル名: 実行日（MMDD）/ ラベル: 実行日の7日前〜実行日
WEEK_FILE_MMDD=$(TZ=Asia/Tokyo date +%m%d)
WEEK_END=$(TZ=Asia/Tokyo date +%-m/%-d)
WEEK_START=$(TZ=Asia/Tokyo date -v-7d +%-m/%-d)
WEEK_LABEL="${WEEK_START}〜${WEEK_END}"
WEEKLY_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-${WEEK_FILE_MMDD}.md"

log() { echo "[$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"; }

log "=== 起動チェック: ${TODAY} / ${YEAR}-${WEEK_FILE_MMDD} / 対象期間: ${WEEK_LABEL} ==="
[ -f "${WEEKLY_FILE}" ] && log "実行日分（${YEAR}-${WEEK_FILE_MMDD}）は実行済み。スキップ。" && exit 0

[ "${DAY_OF_MONTH}" -le 7 ] && MODE="monthly" || MODE="weekly"
log "=== 実行開始: ${MODE} ==="

SCRAPED=$("${PYTHON_BIN}" "${PROJECT_DIR}/scripts/fetch_news.py" 2>>"${LOG_FILE}" || true)

MAX_RETRY=3; RETRY=0; SUCCESS=false
while [ ${RETRY} -lt ${MAX_RETRY} ]; do
  RETRY=$((RETRY + 1))
  log "ローカルエージェント起動 model=${AI_NEWS_MODEL} (試行 ${RETRY}/${MAX_RETRY})"
  if "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/local_agent.py" \
      --mode "${MODE}" \
      --week-file "${WEEK_FILE_MMDD}" \
      --week-label "${WEEK_LABEL}" \
      --year "${YEAR}" \
      --month "$(TZ=Asia/Tokyo date +%m)" \
      --model "${AI_NEWS_MODEL}" \
      --prefetch "${SCRAPED}" \
      2>&1 | tee -a "${LOG_FILE}"; then
    SUCCESS=true; break
  else
    log "失敗。60秒後にリトライします..."
    [ ${RETRY} -lt ${MAX_RETRY} ] && sleep 60
  fi
done
[ "${SUCCESS}" = false ] && log "ERROR: ${MAX_RETRY}回すべて失敗。手動確認が必要です。" && exit 1
log "=== 完了 ==="
```

### 7. run_ai_news_haiku.sh を作成（非公開・手動作成が必要）

`scripts/run_ai_news_haiku.sh` はリポジトリに含まれている（絶対パスは固定済み）。
新環境に移行する場合は `PROJECT_DIR` 等を書き換えること。

### 8. launchd に登録

```bash
# Ollama 版（09:00）
cp ~/projects/ai_news/scripts/com.user.ai_news.plist \
   ~/Library/LaunchAgents/com.user.ai_news.plist
launchctl load ~/Library/LaunchAgents/com.user.ai_news.plist

# 比較用サブモデル ornith（土曜 10:00）
cp ~/projects/ai_news/scripts/com.user.ai_news_ornith.plist \
   ~/Library/LaunchAgents/com.user.ai_news_ornith.plist
launchctl load ~/Library/LaunchAgents/com.user.ai_news_ornith.plist

# 比較用サブモデル nemotron（土曜 11:00）
cp ~/projects/ai_news/scripts/com.user.ai_news_nemotron.plist \
   ~/Library/LaunchAgents/com.user.ai_news_nemotron.plist
launchctl load ~/Library/LaunchAgents/com.user.ai_news_nemotron.plist

# Haiku 版（13:00）
cp ~/projects/ai_news/scripts/com.user.ai_news_haiku.plist \
   ~/Library/LaunchAgents/com.user.ai_news_haiku.plist
launchctl load ~/Library/LaunchAgents/com.user.ai_news_haiku.plist

# 登録確認
launchctl list | grep ai_news
# → com.user.ai_news / com.user.ai_news_ornith / com.user.ai_news_nemotron / com.user.ai_news_haiku
#   の4つが表示されれば OK
```

#### launchd設定（com.user.ai_news.plist）の最小構成

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.user.ai_news</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>/PATH/TO/ai_news/scripts/run_ai_news.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key><integer>6</integer>
    <key>Hour</key><integer>9</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/opt/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key><string>/PATH/TO/HOME</string>
    <key>LANG</key><string>ja_JP.UTF-8</string>
  </dict>
  <key>StandardOutPath</key>
  <string>/PATH/TO/ai_news/ai_news.log</string>
  <key>StandardErrorPath</key>
  <string>/PATH/TO/ai_news/ai_news.log</string>
  <key>RunAtLoad</key><false/>
  <key>WorkingDirectory</key>
  <string>/PATH/TO/ai_news</string>
</dict>
</plist>
```

### 9. テスト実行（初回）

```bash
# Ollama 版（今週分のファイルが無い状態で実行）
bash ~/projects/ai_news/scripts/run_ai_news.sh
tail -f ~/projects/ai_news/ai_news.log

# Haiku 版（Ollama版完了後に実行すると比較ページも生成される）
bash ~/projects/ai_news/scripts/run_ai_news_haiku.sh
tail -f ~/projects/ai_news/ai_news_haiku.log

# 比較ページだけ手動で生成したい場合（両記事が揃っている前提）
python3 ~/projects/ai_news/scripts/generate_compare.py \
  --week-file 0530 --week-label "5/23〜5/30" --year 2026
```

---

## 使用モデルの変更

デフォルトは `qwen3.6:35b-mlx`。`AI_NEWS_MODEL` 環境変数で変更できる。

### 一時的に変更（1回だけ）

```bash
AI_NEWS_MODEL=qwen3.6:27b-mlx bash ~/projects/ai_news/scripts/run_ai_news.sh
```

### launchd で常用モデルを変更

`com.user.ai_news.plist` の `EnvironmentVariables` に追加する:

```xml
<key>AI_NEWS_MODEL</key>
<string>qwen3.6:27b-mlx</string>
```

変更後は reload:

```bash
launchctl unload ~/Library/LaunchAgents/com.user.ai_news.plist
launchctl load  ~/Library/LaunchAgents/com.user.ai_news.plist
```

### Ollama で使用可能なモデル一覧（2026-05-24 時点）

| モデル | サイズ | 日本語 | tool calling | 推奨用途 |
|---|---|---|---|---|
| `qwen3.6:35b-mlx` | 21GB | ◎ | ○ | **デフォルト。品質優先** |
| `qwen3.6:27b-mlx` | 19GB | ◎ | ○ | 速度優先（品質も十分） |
| `gemma4:31b-mlx` | 20GB | ○ | ○ | 代替候補 |
| `hf.co/mmnga/RakutenAI-2.0-8x7B-instruct-gguf:Q4_K_M` | 28GB | ◎ | △ | 日本語特化（tool calling弱め） |
| `devstral-small-2:24b` | 15GB | △ | ○ | コード特化のため不向き |

---

## 実行確認方法

| 確認内容 | 方法 |
|---|---|
| Ollama 実行ログ | `tail ~/projects/ai_news/ai_news.log` |
| Haiku 実行ログ | `tail ~/projects/ai_news/ai_news_haiku.log` |
| 記事内容（Ollama） | `articles/weekly/` または GitHub Pages |
| 記事内容（Haiku） | `articles/haiku_weekly/` または GitHub Pages |
| 比較ページ | `articles/compare/` または GitHub Pages |
| launchd 登録状態 | `launchctl list \| grep ai_news` |
| Ollama 稼働状態 | `curl http://localhost:11434/api/tags` |
| API キー設定 | `source ~/.anthropic_env && echo $ANTHROPIC_API_KEY` |

**正常時のログ例：**
```
[2026-06-07 09:00:05] === ai_news 起動チェック ===
[2026-06-07 09:00:05] 今日: 2026-06-07 / 実行日ファイル: 2026-0607 / 対象期間: 5/31〜6/7
[2026-06-07 09:00:05] === ai_news 自動実行開始 ===
[2026-06-07 09:00:05] モード: 週次
[2026-06-07 09:00:06] BeautifulSoup で記事一覧を事前取得中...
[2026-06-07 09:00:16] スクレイピング完了（79 行取得）
[2026-06-07 09:00:16] ローカルエージェントを起動します... model=qwen3.6:35b-mlx (試行 1/3)
[2026-06-07 09:00:16] エージェント開始: model=qwen3.6:35b-mlx, mode=weekly, week=0607
[2026-06-07 09:00:16] --- ターン 1/40 ---
[2026-06-07 09:00:35] ツール呼び出し: search_web({"query": "生成AI 最新ニュース 今週"})
...
[2026-06-07 09:15:22] ツール呼び出し: git_commit_push(...)
[2026-06-07 09:15:28] === ai_news 自動実行完了 ===
```

**スキップ時のログ例：**
```
[2026-06-07 09:00:01] === ai_news 起動チェック ===
[2026-06-07 09:00:01] 今日: 2026-06-07 / 実行日ファイル: 2026-0607 / 対象期間: 5/31〜6/7
[2026-06-07 09:00:01] 実行日分（2026-0607）は実行済み。スキップします。
```

---

## 手動実行

```bash
# Ollama 版（今週分のファイルが無い場合のみ実行される）
bash ~/projects/ai_news/scripts/run_ai_news.sh

# モデルを指定して実行
AI_NEWS_MODEL=qwen3.6:27b-mlx bash ~/projects/ai_news/scripts/run_ai_news.sh

# 比較用サブモデルを手動実行（articles/weekly_<variant>/ に生成）
AI_NEWS_VARIANT=ornith   AI_NEWS_MODEL=ornith-1.5:35b                bash ~/projects/ai_news/scripts/run_ai_news.sh
AI_NEWS_VARIANT=nemotron AI_NEWS_MODEL=nemotron-3.5-lightning:30b-mlx bash ~/projects/ai_news/scripts/run_ai_news.sh
tail -f ~/projects/ai_news/ai_news_ornith.log

# Haiku 版
bash ~/projects/ai_news/scripts/run_ai_news_haiku.sh

# Haiku モデルを変更して実行
HAIKU_MODEL=claude-sonnet-4-6 bash ~/projects/ai_news/scripts/run_ai_news_haiku.sh

# 比較ページのみ手動生成
python3 ~/projects/ai_news/scripts/generate_compare.py \
  --week-file MMDD --week-label "M/D〜M/D" --year YYYY

# launchd 経由で即時起動
launchctl start com.user.ai_news           # Ollama 版（qwen3.6）
launchctl start com.user.ai_news_ornith    # 比較用 ornith
launchctl start com.user.ai_news_nemotron  # 比較用 nemotron
launchctl start com.user.ai_news_haiku     # Haiku 版

# ログ確認
tail -f ~/projects/ai_news/ai_news.log           # Ollama（qwen3.6）ログ
tail -f ~/projects/ai_news/ai_news_ornith.log    # ornith ログ
tail -f ~/projects/ai_news/ai_news_nemotron.log  # nemotron ログ
tail -f ~/projects/ai_news/ai_news_haiku.log     # Haiku ログ
```

---

## 管理・設定変更

### 収集トピックの追加・変更

`~/projects/ai_news/SPEC.md` の「特に注目しているトピック」セクションを編集する。
あわせて `~/projects/ai_news/CLAUDE.md` の「優先収集キーワード」と
`~/projects/ai_news/scripts/local_agent.py` のシステムプロンプト内キーワードも更新する。

### スクレイピング対象サイトの追加・変更

`~/projects/ai_news/scripts/fetch_news.py` の `SITES` リストを編集する。
各サイトの HTML 構造に合わせて `extractor` 関数を実装する。

### スケジュール変更

`~/projects/ai_news/scripts/com.user.ai_news.plist` の `StartCalendarInterval` を編集。

```bash
# 変更後は reload が必要
launchctl unload ~/Library/LaunchAgents/com.user.ai_news.plist
cp ~/projects/ai_news/scripts/com.user.ai_news.plist \
   ~/Library/LaunchAgents/com.user.ai_news.plist
launchctl load ~/Library/LaunchAgents/com.user.ai_news.plist
```

### launchd の停止・削除

```bash
# 一時停止
launchctl unload ~/Library/LaunchAgents/com.user.ai_news.plist

# 完全削除
launchctl unload ~/Library/LaunchAgents/com.user.ai_news.plist
rm ~/Library/LaunchAgents/com.user.ai_news.plist
```

---

## 設計判断メモ

### 2026-08-28: 比較用ローカルモデル2種（ornith / nemotron）を追加

**背景:**
`local_agent`（https://masauehr.github.io/local_agent/）でローカルモデルを横断比較したところ、
`ornith-1.5:35b` と `nemotron-3.5-lightning` が qwen3.6 の対抗馬として有力だった。
ai_news の週次比較にこの2モデルを定点観測として組み込む。

**アーキテクチャの選択:**

| 選択肢 | 説明 | 採否 |
|---|---|---|
| モデルごとに run スクリプト・エージェントを複製 | `run_ai_news_ornith.sh` 等を新規作成 | ✗ 重複が多くメンテ負荷が高い |
| **`run_ai_news.sh` に `AI_NEWS_VARIANT` モードを追加**（採用） | 同一スクリプト・同一エージェントを環境変数で分岐。保存先ディレクトリと後処理有無だけ変える | ○ 差分が小さい。plist の `EnvironmentVariables` でモデルを切り替えるだけ |

**比較ページの構成（ユーザー選択）:**
- メインの2カラム（qwen3.6 vs Haiku）は現状維持。その下に ornith / nemotron を**1カラム縦積み**で追加（`.compare-extra`）。
- 4カラム横並びも検討したが、記事全文を横に4つ並べると各カラムが狭くなりすぎるため却下。
- Sonnet 評価はその週に揃った**全モデル**を対象（評価表はモデル数ぶんの列を動的生成）。

**実行時刻をずらす理由:**
- Ollama は同時に複数モデルを走らせると VRAM を食い合う。qwen3.6(09:00) → ornith(10:00) → nemotron(11:00) と1時間ずつずらし、
  Haiku・比較生成(13:00) までに全ローカルモデルが完了しているようにした（2026-05-25 の Ollama/Haiku 分離と同じ考え方）。

**サブモデルが README/index を更新しない理由:**
- 「今週の記事」としての正典は qwen3.6 版1本に保ちたい（一覧が3倍に増えると読みづらい）。
- サブモデルの記事は比較ページ経由でのみ露出させる。`local_agent.py` の `VARIANT_SYSTEM_PROMPT_TMPL` で
  `append_to_readme` / `update_index` を手順から外し、`git_commit_push` は生成した1ファイルのみ対象にした。

**モデル名の補足:**
- `nemotron-3.5-lightning` はタグ無しでは `ollama` に存在せず、`:30b` と `:30b-mlx` がある。
  qwen3.6 と同じく MLX 版（`nemotron-3.5-lightning:30b-mlx`）を採用。変更する場合は
  `com.user.ai_news_nemotron.plist` の `AI_NEWS_MODEL` を書き換えて reload する。

---

### 2026-07-13: Haiku/Sonnet実行を Anthropic API → Claude Code CLI（サブスク）方式に変更【一時メモ・要清書】

**背景（障害）:**
- 2026-07-04・2026-07-11 の Haiku自動実行が `anthropic.Anthropic()` 経由のAPI呼び出しで
  `Your credit balance is too low to access the Anthropic API` により失敗
- 2026-07-05・2026-07-12 の weather_digest（同一方式）でも同時多発
- 原因は Claude Pro/Max **サブスクリプション**とは別勘定の **Anthropic API プリペイドクレジット**残高切れ。
  Claude Code / claude.ai チャットはサブスク課金で無関係だが、`haiku_agent.py` と `generate_compare.py`
  の Sonnet評価は `anthropic` Python SDK で生API を直叩きしていたため影響を受けた
- 同時期、`stock_analysis` / `rakuten_margin` は `~/.local/bin/claude`（Claude Code CLI）を
  `--model haiku --dangerously-skip-permissions` で subprocess 呼び出しする方式のため無傷と判明
  （ANTHROPIC_API_KEY を環境にセットしていないため、CLIはOAuthログイン＝サブスク認証にフォールバックする）

**変更内容（ai_newsのみ。weather_digestは未着手）:**
- `haiku_agent.py`: `anthropic.Anthropic()` の tool-use ループ（`TOOLS`定義・`search_web`/`fetch_url`/
  `write_article`/`read_file`）を全廃。代わりに以下のハイブリッド構成にした
  - **取材・記事執筆**: `claude --print --dangerously-skip-permissions --model haiku
    --allowedTools "WebSearch,WebFetch,Write,Read" --max-budget-usd <N>` を subprocess 呼び出し
    （プロンプトは stdin 経由）。実行前に `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` を
    環境変数から明示的に `pop()` し、API課金経路に落ちないようにしている
  - **README.md / index.md 更新・git commit/push**: 引き続き Python の決定論的な関数
    （`append_to_readme` / `update_index` / `git_commit_push`。ロジックは旧版から変更なし）で実行。
    Claude Code CLI 側には Bash/Edit を許可しておらず、記事ファイル1つ以外は書けない
  - 安全策として、CLI呼び出し前後で `git status --porcelain` を比較し、想定外のファイルが
    変更されていた場合は README更新・commit/push を中断するガードを追加
- `generate_compare.py`: `generate_sonnet_eval()` 内の `client.messages.create(model="claude-sonnet-4-6")`
  を `claude --print --model sonnet --allowedTools ""`（ツールなし単発呼び出し）に置き換え
- `run_ai_news_haiku.sh`: `~/.anthropic_env` の読み込み・`ANTHROPIC_API_KEY` 必須チェックを削除。
  代わりに `~/.local/bin/claude` の存在確認と `unset ANTHROPIC_API_KEY` に変更。
  `HAIKU_MODEL` のデフォルト値も `claude-haiku-4-5-20251001`（フルモデルID）→ `haiku`（CLIエイリアス）に変更。
  ついでに既存のタイプミス（`WEEK_MON_MMDD` → `WEEK_FILE_MMDD`、実行済みスキップ時の比較ページ生成が
  常に失敗していた）も修正
- 依存ライブラリ: `haiku_agent.py`・`generate_compare.py` は `anthropic` SDK が不要になった
  （`local_agent.py`＝Ollama版は引き続き `requests`/`ddgs`/`trafilatura` を使用するため変更なし）

**検証状況（2026-07-13時点）:**
- `claude --model haiku` / `--model sonnet` とも ANTHROPIC_API_KEY なしでクレジットエラーが出ないことを確認
- scratchpad（本番リポジトリ外）で実際のプロンプト全文（WebSearch 10クエリ + WebFetch 2件 + Write）を
  流し、実記事1本の生成に成功。指示通り記事ファイル以外には書き込んでいないことを確認
- **本番リポジトリでのエンドツーエンド実行（README/index更新・git push含む）は未実施。**
  stock_analysis 等、他の自動化と Pro/Max サブスクリプションの利用枠を共有するため、
  利用量に余裕がある時間帯にユーザー確認の上で実行する方針（2026-07-13時点で保留中）

**未対応:**
- weather_digest への同様の移行は未着手（ai_newsでの安定稼働確認後に着手する想定）
- 上記「本番実行」が完了したら、この節を正式な手順（実行フロー図・エージェント動作詳細・
  セットアップ手順の書き換え）に反映して整理すること

---

### 2026-06-07: Haiku月次記事・月次比較ページ・Sonnet評価セクションを追加

#### Haiku月次記事の追加（`haiku_monthly/`）

**変更内容:**
- `haiku_agent.py` に `SYSTEM_PROMPT_MONTHLY_TMPL` を追加（月次専用システムプロンプト）
- `build_system_prompt()` が `--mode` 引数で週次/月次プロンプトを切り替え
- `tool_append_to_readme()` と `tool_update_index()` でパスに "haiku_monthly" が含まれるかを検出し、
  該当する README セクション（`### Haiku月次まとめ`）と index ファイル（`haiku_monthly/index.md`）を更新

**月次実行タイミング:**
- `run_ai_news_haiku.sh` が `DAY_OF_MONTH <= 7`（月の第1土曜）を検出して `MODE="monthly"` に設定
- 既に月次ファイルが存在する場合はスキップ

#### 月次比較ページの追加（`compare/monthly-YYYY-MM.md`）

- `generate_compare.py` を月次モードで呼び出し（`--mode monthly` など）、
  `articles/monthly/YYYY-MM.md` と `articles/haiku_monthly/YYYY-MM.md` を2カラムで並べる
- ファイル名規則: `compare/monthly-YYYY-MM.md`（週次は `compare/YYYY-MMDD.md`）
- `articles/compare/index.md` に「## 月次比較」セクションを追加

#### Sonnet評価セクション（`.sonnet-eval` CSS クラス）

**変更内容:**
- `_layouts/compare.html` に `.sonnet-eval` CSS クラスブロックを追加（紫系カラー）
- compare ページの Markdown で `<div class="sonnet-eval" markdown="1">` を使用

**`markdown="1"` が必須な理由 (→ 後述の「GitHub Pages技術解説」参照):**
- Kramdown は `<div>` ブロック内の Markdown をデフォルトでは HTML として扱い、
  `# 見出し` や `| テーブル |` を変換しない
- `markdown="1"` を付与することで Kramdown が div 内も Markdown として処理する
- インラインスタイル（`style="..."` 属性）では Kramdown の Markdown 変換が働かないため、
  CSS クラスに分離した上で `markdown="1"` を組み合わせる必要があった

#### ホームページ（`index.md`）をSonnet評価付き最新比較に変更

- `layout: compare` を使用し、最新週の Ollama と Haiku の全文 + Sonnet評価を掲載
- 旧: `layout: default` で単純に Ollama 記事の概要のみ掲載

#### フッター修正

- `_layouts/default.html`: `Powered by Ollama ローカルLLM` → `Ollama ローカルLLM & Claude Haiku による自動生成`
- Haiku版記事も default.html を使うため、サイト全体のフッターが誤表示されていた

---

### 2026-05-31: ファイル名・期間ラベルを実行日ベースに変更

**変更前:** ファイル名 = 今週月曜日（例: 5/30 実行 → `2026-0525.md`、ラベル `5/25〜5/31`）  
**変更後:** ファイル名 = 実行日（例: 5/30 実行 → `2026-0530.md`、ラベル `5/23〜5/30`）

**変更理由:**
- 旧方式では「5/30 実行なのに 5/31 まで」のラベルになり、実際にカバーしていない未来の日付を含んでいた
- 実行日ベースにすることで「実行した日までの7日間」という直感的な期間になる
- ファイル名も実行日一致になるため「いつ実行した記事か」が一目でわかる

**スクリプトの変更:**  
`run_ai_news.sh` / `run_ai_news_haiku.sh` の週計算部分:
```bash
# 旧: 今週月曜日を基準
WEEK_MON_MMDD=$(TZ=Asia/Tokyo date -v-$((DOW-1))d +%m%d)

# 新: 実行日を基準
WEEK_FILE_MMDD=$(TZ=Asia/Tokyo date +%m%d)
WEEK_END=$(TZ=Asia/Tokyo date +%-m/%-d)
WEEK_START=$(TZ=Asia/Tokyo date -v-7d +%-m/%-d)
WEEK_LABEL="${WEEK_START}〜${WEEK_END}"
```

---

### 2026-05-25: Claude Haiku 並行実行 + モデル比較ページを追加

**追加理由:**
ローカルLLM（Ollama）とクラウドモデル（Haiku）が同じ週の同じトピックをどう要約するか
週次で定点比較することで、モデル特性の違いを継続的に観察できるようにした。

**アーキテクチャの選択:**

| 選択肢 | 説明 | 採用理由 |
|---|---|---|
| 単一スクリプトで両モデルを実行 | run_ai_news.sh 内で Ollama → Haiku を順次実行 | ✗ 処理時間が長くなり、片方が失敗すると両方失敗する |
| **別スクリプトで時刻をずらして実行**（採用） | Ollama=09:00、Haiku=13:00 で独立実行 | ○ 障害が独立・Ollamaが終わった後にHaikuが実行されて比較成立 |

**ANTHROPIC_API_KEY の管理:**
- plist に直接書くとファイルを git 管理できなくなる
- `~/.anthropic_env` に分離してシェルスクリプト内で `source` する方式を採用
- これにより plist 自体はリポジトリに入れても秘密情報が漏れない

**比較ページの生成方式:**
- Jekyll の `_layouts/compare.html` で2カラムレイアウトを実現
- `generate_compare.py` が両記事の front matter を除去して `<div class="panel-body" markdown="1">` に埋め込む
- `markdown="1"` 属性により、Kramdown が div 内の Markdown を HTML に変換する

**Haiku エージェントの実装:**
- `haiku_agent.py` は Anthropic SDK の `client.messages.create()` + tool use を使う
- `local_agent.py`（Ollama）と同じツール名・引数を定義することで、
  両エージェントのシステムプロンプトを統一しやすくした
- 保存先ディレクトリのみ異なる（`haiku_weekly/` vs `weekly/`）

---

### 2026-05-24: Claude CLI → Ollama ローカルLLMエージェントに変更

**変更理由:**
Sonnet 等の API を使った記事生成は世の中にありふれている。
**ローカルLLMで動かすこと自体に意味がある**という判断から、
Claude CLI を Ollama の tool-calling エージェントに置き換えた。

**検討したアーキテクチャ案:**

| 案 | 概要 | 長所 | 短所 |
|---|---|---|---|
| **案A（シンプル収集）** | Python が全検索・スクレイピングをこなし、LLM は記事生成のみ | 実装が単純・品質安定 | 検索クエリをハードコードするため柔軟性ゼロ |
| **案B（Tool calling）** | LLM が search_web / fetch_url を自律呼び出しで情報収集 | Claude ワークフローに近い・LLM が検索内容を判断できる | 実装コスト高め・モデル品質に依存 |

→ **案Bを採用**。Qwen3 の tool calling 品質が高く、エージェント的な動作との相性が良いため。

**技術的課題と解決策:**

| 課題 | Claude CLIでの解決 | ローカルLLMでの解決 |
|---|---|---|
| WebSearch | 組み込みツール | `ddgs`（DuckDuckGo）ライブラリ |
| WebFetch（静的ページ） | 組み込みツール | `trafilatura` + `requests` |
| WebFetch（JS描画ページ） | 組み込みツール | `trafilatura`でベストエフォート（完全取得は困難） |
| ファイル書き込み | Write ツール | `write_article()` 関数（上書き禁止チェック付き） |
| README 更新 | Edit ツール | `append_to_readme()` 関数（専用ツールで安全に更新） |
| git 操作 | Bash ツール | `git_commit_push()` 関数 |

**モデル選定:**

候補モデルを以下の観点で評価した。

| モデル | サイズ | 日本語 | tool calling | 評価 |
|---|---|---|---|---|
| `qwen3.6:35b-mlx` | 21GB | ◎ | ○ | ◎ **採用**（品質・速度バランス最良） |
| `qwen3.6:27b-mlx` | 19GB | ◎ | ○ | ○ 速度優先なら有力 |
| `RakutenAI-2.0 Q4` | 28GB | ◎（日本語特化） | △ | △ tool calling が弱い |
| `gemma4:31b-mlx` | 20GB | ○ | ○ | △ 代替候補 |
| `devstral-small-2` | 15GB | △ | ○ | ✗ コード特化で不向き |

選定理由: Qwen3 は 128K context・多言語・tool calling の実績があり、
MLX 最適化版で Apple Silicon 上の推論速度が良好。

**品質上の留意点:**
- Claude Sonnet と比べて英語記事の要約精度・複数トピック整理力で差が出る可能性がある
- 記事品質を優先する場合は `qwen3.6:35b-mlx` を使用すること

**ライブラリ:**
```bash
/opt/anaconda3/bin/pip install ddgs trafilatura
```
- `ddgs`: DuckDuckGo 検索（`duckduckgo_search` の後継パッケージ）
- `trafilatura`: Web ページからメインコンテンツを抽出（boilerplate 除去）

---

### 2026-05-17: 毎日チェック方式 → 毎週土曜 09:00 に変更

**変更前:** 毎日 09:00 に起動し、スクリプト内で「今週分の記事ファイルが存在するか」を確認。
存在しない場合のみ実行（実質は週1回）。

**変更理由:**
- 毎日09:00に起動しても「スキップして終了」するだけの無駄な起動が週6回発生していた
- `StartCalendarInterval` に `Weekday: 6`（土曜）を指定することで、土曜のみ起動するよう変更
- **MacスリープによるMiss対応**: 土曜にスリープで実行できなかった場合は、次の土曜（1週後）に自動実行される

**土曜実行を選んだ理由（月曜でなく）:**
- 月曜実行の場合、記事は月曜時点の情報しか含まれない（週末の大きなニュースが記事に入らない）
- 土曜実行なら月〜金の主要ニュースを含む、より完成度の高い週次まとめになる

**注意点:** plist 変更後は `launchctl unload` → `load` が必要。
unload/load をせずに plist のみ書き換えると、launchd がメモリ上の古い設定で動き続ける。

---

### 2026-05-17: BeautifulSoup による事前スクレイピングを導入

**変更前:** LLMの WebFetch ツールで各サイトのHTMLを直接取得し、LLMがトピックを抽出。

**変更理由（コンテキスト削減）:**
- WebFetch は生のHTML（数十〜数百KB）をそのままLLMのコンテキストに流す
- BeautifulSoupで事前に記事タイトル＋URLだけを抽出すると1〜3KB程度になる
- 1サイトあたり **10〜50倍のコンテキスト削減** が期待できる
- ローカルLLMは context length が有限（65536 token に設定）なので特に重要

**サイト構造の違いへの対応:**
- ITmedia: Shift-JIS エンコーディング、h2/h3タグでリンク取得
- Techno Edge: `/article/YYYY/MM/DD/` URLパターン + 過去30日フィルタ
- Anthropic: URLスラグからタイトルを生成（テキストに日付・カテゴリが混入するため）
- DeepMind: articleタグ内の日付・カテゴリをregexで除去

---

### なぜ「毎日チェック」方式にしたか（2026-04当時）

当初は月曜 09:00 のみ実行する設定だったが、**Macがスリープ中だと実行されない**問題があった。
`StartCalendarInterval` はスリープ中にスキップし、起動後は「次の月曜まで待つ」動作になるため、
月曜が丸ごと実行されないケースが発生していた。

**解決策（当時）:** 毎日 09:00 に起動し、スクリプト内で「今週分の記事ファイルが存在するか」を確認。
→ 2026-05-17 に「土曜のみ起動」方式に変更。

---

### CLAUDE.md・scripts/ を非公開にした理由

絶対パスにユーザー名等の個人情報が含まれるため `.gitignore` で除外。
記事本体（`articles/`）・仕様（`SPEC.md`）・概要（`README.md`）のみ公開する。
`local_agent.py` と `fetch_news.py` は絶対パスを含まないため公開対象。

---

### 日本国内情報の収集設計判断

当初は Sakana AI ブログを直接参照先として設定していたが、以下の問題があった：
- 特定企業への偏重 → 楽天AI（RakutenAI）等が漏れる
- 企業ブログは毎週更新があるとは限らず空振りしやすい

**修正方針:**
- 政府情報はデジタル庁ニュースページを `fetch_url` で直接取得
- 企業動向は `日本 生成AI 企業 最新ニュース 今週` 等の横断的な検索で収集
- SPEC.md の注目企業リストは「例示」であり、その週に動きのあった企業を優先する

---

---

## GitHub Pages 技術解説

### .md ファイルの公開と通常の HTML 公開の違い

GitHub Pages では、リポジトリに置いたファイルをそのままブラウザに配信する。
ファイルの拡張子によって処理方法が異なる。

| ファイル形式 | ブラウザでの動作 | 変換エンジン |
|---|---|---|
| `.html` | そのまま HTML として表示 | なし（変換不要） |
| `.md`（Jekyll有効時） | HTML に自動変換されてから配信 | **Kramdown**（Jekyllのデフォルト） |
| `.md`（Jekyll無効時） | テキストとして表示（Markdownがそのまま見える） | なし |

このリポジトリでは Jekyll が有効なため、`.md` ファイルはビルド時に HTML に変換される。
ブラウザのアドレスバーでは `/articles/weekly/2026-0606` のように拡張子なしで表示される
（実際には `/articles/weekly/2026-0606.html` として配信）。

### Jekyll / Kramdown の処理フロー

```
GitHubへ push
  ↓
GitHub Pages が Jekyll ビルドを自動実行
  ↓
各 .md ファイルを処理:
  1. front matter（---〜---）を読み取り、layout を決定
  2. Markdown 本文を Kramdown で HTML に変換
  3. _layouts/{layout}.html のテンプレートに埋め込む（{{ content }} の位置）
  4. 完成した HTML を .html ファイルとして配信
  ↓
ブラウザからは https://masauehr.github.io/ai_news/articles/weekly/2026-0606 でアクセス可能
```

### front matter（フロントマター）

各 Markdown ファイルの冒頭に YAML 形式で記述するメタデータ。Jekyll が読み取る。

```yaml
---
layout: compare    # 使用するレイアウトテンプレート（_layouts/ 内のファイル名）
title: "週次比較ページ"  # ページタイトル
---
```

| フィールド | 説明 |
|---|---|
| `layout` | 使用するレイアウト（`default` または `compare`） |
| `title` | `<title>` タグに使われるページタイトル |

front matter がない .md ファイルは、Jekyll がデフォルトレイアウトで処理するか、
設定によってはそのままテキストとして扱われる。

### `_layouts/` の役割

```
_layouts/
├── default.html    # 週次・月次・通常記事のレイアウト
└── compare.html    # 2カラム比較ページのレイアウト（カスタムCSS内蔵）
```

- レイアウトは HTML で書かれた「テンプレート」
- `{{ content }}` という Liquid タグの位置に .md の変換結果が挿入される
- CSS はレイアウトファイルの `<style>` タグ内に直接記述（外部CSS不使用）
- ナビゲーション・ヘッダー・フッターはレイアウト側で管理

### `markdown="1"` 属性の意味

**問題:** Kramdown は `<div>` や `<section>` などの HTML ブロック要素の**中**にある
Markdown 記法（見出し・テーブル・箇条書き等）をデフォルトでは変換しない。

```markdown
<!-- これはダメ: <div>内のMarkdownが変換されない -->
<div class="sonnet-eval">
## 見出し
| A | B |
|---|---|
| 1 | 2 |
</div>

<!-- これが正しい: markdown="1"を付けると変換される -->
<div class="sonnet-eval" markdown="1">
## 見出し
| A | B |
|---|---|
| 1 | 2 |
</div>
```

**注意点:**
- `markdown="1"` は Kramdown 固有の拡張機能。他の Markdown エンジンでは動作しない
- GitHub Pages の標準 Kramdown では動作する
- インライン style 属性（`<div style="...">`）を使う場合も同様に `markdown="1"` が必要

### ブラウザでの表示確認方法

```bash
# ローカルで Jekyll ビルドして確認（要 Ruby + Jekyll）
cd ~/projects/ai_news
bundle exec jekyll serve

# ブラウザで http://localhost:4000/ai_news/ を開く
```

または、GitHub へ push 後に https://masauehr.github.io/ai_news/ で確認する。
ビルドには通常 30〜90 秒かかる。

### よくある表示崩れの原因

| 症状 | 原因 | 対処 |
|---|---|---|
| `<div>` 内の見出し・テーブルが表示されない | `markdown="1"` が抜けている | 対象 `<div>` に `markdown="1"` を追加 |
| CSS クラスのスタイルが効かない | `compare.html` に .sonnet-eval 等のCSS定義がない | `_layouts/compare.html` の `<style>` に追加 |
| 特定ページだけレイアウトが違う | front matter の `layout:` が間違っている | ファイル冒頭の front matter を確認 |
| アドレスバーに .md のまま表示 | Jekyll が無効 / front matter がない | `_config.yml` と front matter を確認 |
| 画像が表示されない | URL が絶対パスでなく相対パス | `{{ site.baseurl }}/images/...` の形式で記述 |
| リンクが 404 になる | `site.baseurl` が設定されていない | `_config.yml` に `baseurl: /ai_news` を確認 |

### `_config.yml` の設定

```yaml
title: 生成AI週次ダイジェスト
description: 生成AIの最新情報を週次・月次で自動収集・要約
baseurl: /ai_news          # GitHub Pages のサブパス（リポジトリ名）
url: https://masauehr.github.io
markdown: kramdown         # デフォルト（明示的に設定することも可）
```

---

## トラブルシューティング

**Ollama 版（共通）**

| 症状 | 原因 | 対処 |
|---|---|---|
| 毎週記事が生成されない | launchd が未登録 | `launchctl list \| grep ai_news` で確認・再登録 |
| スキップされ続ける | 実行日分のファイルが既に存在する | `ls articles/weekly/` で確認・不要なら削除 |
| `Ollama に接続できません` | Ollama が起動していない | `ollama serve` または Ollama.app を起動 |
| ターン数上限（40回）に達する | エージェントがループ | ログを確認して原因を特定・システムプロンプトを調整 |
| 記事が生成されたが内容が薄い | モデルの品質限界 | `qwen3.6:35b-mlx` を使用しているか確認 |
| DuckDuckGo でレート制限エラー | 検索回数が多すぎる | ターン間に `sleep 2` が入っているが、再試行で解消することが多い |
| git push が失敗 | SSH鍵 or HTTPS認証の問題 | `git push` を手動実行してエラーを確認 |
| スクレイピングが全失敗する | ネットワーク障害・サイト構造変更 | ログに `WARN: スクレイピング失敗` が出て、エージェントが直接 fetch_url で補完する |
| 特定サイトの記事が取れない | サイトのHTML構造が変わった | `scripts/fetch_news.py` の該当 `extractor` 関数を修正する |

**Haiku 版**

| 症状 | 原因 | 対処 |
|---|---|---|
| `ANTHROPIC_API_KEY が設定されていません` | APIキー未設定 | `~/.anthropic_env` に `ANTHROPIC_API_KEY=sk-ant-...` を記載して `chmod 600` |
| Haiku 記事が生成されない | launchd 未登録または APIキーエラー | `ai_news_haiku.log` でエラーを確認 |
| Haiku 月次記事が生成されない | 第1土曜でない、またはファイルが既に存在する | `DAY_OF_MONTH` と `haiku_monthly/` を確認 |
| 比較ページが生成されない | Ollama 版記事が未生成（13:00時点） | Ollama 版完了後に `generate_compare.py` を手動実行 |
| 月次比較ページが生成されない | Haiku月次ファイルか Ollama月次ファイルが未生成 | 両ファイルを確認後 `generate_compare.py --mode monthly` で手動実行 |
| Haiku 記事の内容が薄い | Haiku の文章生成能力の限界 | `HAIKU_MODEL=claude-sonnet-4-6` で上位モデルに変更 |
| 比較ページのレイアウトが崩れる | `_layouts/compare.html` の問題 | Jekyll の `markdown="1"` が有効か確認（→ GitHub Pages技術解説参照） |
| Sonnet評価のテーブルや見出しが表示されない | `markdown="1"` が抜けている | compare ページの `<div class="sonnet-eval">` に `markdown="1"` を追加 |
