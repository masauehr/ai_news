# ai_news — 生成AI最新情報ダイジェスト

**🌐 公開サイト: https://masauehr.github.io/ai_news/**

> 詳しい運用マニュアルは [ai-news.md](./ai-news.md) を参照。

## クイックリンク

| | リンク |
|---|---|
| 🌐 公開サイト | https://masauehr.github.io/ai_news/ |
| 📰 Ollama週次まとめ | https://masauehr.github.io/ai_news/articles/weekly/ |
| ⚡ Haiku週次まとめ | https://masauehr.github.io/ai_news/articles/haiku_weekly/ |
| 🔬 モデル比較 | https://masauehr.github.io/ai_news/articles/compare/ |
| 📅 月次まとめ一覧 | https://masauehr.github.io/ai_news/articles/monthly/ |
| ⚙️ 収集・生成仕様 | [SPEC.md](./SPEC.md) |

---

## 概要

生成AI（LLM・画像生成・マルチモーダル等）に関する最新情報を、
週次・月次で自動収集・要約してGitHubで公開するプロジェクト。

## プロジェクト構成

```
ai_news/
├── README.md                         # このファイル（最新記事一覧）
├── SPEC.md                           # 情報収集・記事生成の仕様
├── articles/
│   ├── weekly/YYYY-MMDD.md          # Ollama 週次記事（土曜 09:00 自動生成）
│   ├── haiku_weekly/YYYY-MMDD.md    # Haiku 週次記事（土曜 13:00 自動生成）
│   ├── compare/YYYY-MMDD.md         # モデル比較ページ（13:00 以降 自動生成）
│   └── monthly/YYYY-MM.md           # 月次まとめ（第1土曜 自動生成）
└── scripts/
    ├── local_agent.py               # Ollama エージェント（09:00 実行）
    ├── haiku_agent.py               # Claude Haiku エージェント（13:00 実行）
    ├── generate_compare.py          # 比較ページ生成スクリプト
    ├── fetch_news.py                # BeautifulSoup 事前スクレイピング
    ├── run_ai_news.sh               # Ollama 実行スクリプト（launchd）
    ├── run_ai_news_haiku.sh         # Haiku 実行スクリプト（launchd）
    ├── com.user.ai_news.plist       # launchd 設定（09:00）
    └── com.user.ai_news_haiku.plist # launchd 設定（13:00）
```

### ファイル役割と更新方法

| ファイル | 役割 | 更新方法 | 更新頻度 |
|---|---|---|---|
| `articles/weekly/YYYY-MMDD.md` | Ollama 週次まとめ | **自動生成**（09:00） | 毎週土曜 |
| `articles/haiku_weekly/YYYY-MMDD.md` | Haiku 週次まとめ | **自動生成**（13:00） | 毎週土曜 |
| `articles/compare/YYYY-MMDD.md` | モデル比較ページ | **自動生成**（13:00以降） | 毎週土曜 |
| `articles/monthly/YYYY-MM.md` | 月次まとめ | **自動生成** | 毎月第1土曜 |
| `README.md` | 記事一覧・プロジェクト概要 | 手動 or 自動更新 | 記事追加時 |

---

## 最新記事

<!-- 自動更新される記事一覧 -->

### 週次まとめ（Ollama / qwen3.6:35b-mlx）

- [5/30〜6/6](./articles/weekly/2026-0606.md)
- [5/23〜5/30](./articles/weekly/2026-0530.md)
- [5/25〜5/31](./articles/weekly/2026-0525.md)
- [5/18〜5/24](./articles/weekly/2026-0518.md)
- [5/11〜5/17](./articles/weekly/2026-0511.md)
- [5/4〜5/10](./articles/weekly/2026-0504.md)
- [4/27〜5/3](./articles/weekly/2026-0427.md)
- [4/21〜4/27](./articles/weekly/2026-0421.md)
- [4/14〜4/20](./articles/weekly/2026-0420.md)
- [4/13〜4/19](./articles/weekly/2026-0413.md)
- [4/6〜4/12](./articles/weekly/2026-0406.md)
- [3/30〜4/5](./articles/weekly/2026-0330.md)
- [3/23〜3/29](./articles/weekly/2026-0323.md)

<!-- articles/weekly/ のファイルへのリンクがここに追加される -->

### Haiku週次まとめ（Claude Haiku）

- [5/30〜6/6](./articles/haiku_weekly/2026-0606.md)
- [5/23〜5/30](./articles/haiku_weekly/2026-0530.md)
- [5/25〜5/31](./articles/haiku_weekly/2026-0525.md)
<!-- articles/haiku_weekly/ のファイルへのリンクがここに追加される -->

### Haiku月次まとめ（Claude Haiku）

- [2026年6月](./articles/haiku_monthly/2026-06.md)
<!-- articles/haiku_monthly/ のファイルへのリンクがここに追加される -->

### モデル比較（Ollama vs Haiku）

- [5/30〜6/6](./articles/compare/2026-0606.md)（Claude Sonnet 評価付き）
- [5/23〜5/30](./articles/compare/2026-0530.md)
- [5/25〜5/31](./articles/compare/2026-0525.md)

<!-- articles/compare/ のファイルへのリンクがここに追加される -->

### 月次まとめ（Ollama）

- [2026年6月](./articles/monthly/2026-06.md)
- [2026年5月](./articles/monthly/2026-05.md)
- [2026年4月](./articles/monthly/2026-04.md)

### 月次比較（Ollama vs Haiku）

- [2026年6月](./articles/compare/monthly-2026-06.md)（Claude Sonnet 評価付き）

<!-- articles/monthly/ のファイルへのリンクがここに追加される -->

### トピックス（臨時・深掘りレポート）

週次・月次とは別に、特定テーマを深掘りする単発レポート。

- [1ビットLLM — メモリ14分の1・8倍速推論の衝撃](./articles/topics/2026-04-06_1bit-llm.md)（2026-04-06）
- [MCP（Model Context Protocol） — AIエージェントの「配管工事」が業界標準へ](./articles/topics/2026-04-06_mcp.md)（2026-04-06）

<!-- articles/topics/ のファイルへのリンクがここに追加される -->

---

## 自動実行システム

macOS の launchd が `scripts/run_ai_news.sh` を呼び出し、
**Ollama のローカルLLM（tool calling）** が情報収集から記事生成・git push までを自動実行する。

### スケジュール

| タイミング | 内容 |
|---|---|
| 毎週土曜 09:00 JST | Ollama（qwen3.6:35b-mlx）が週次記事を自動生成・git push |
| 毎月第1土曜 09:00 JST | 上記に加えて月次まとめも生成 |
| 毎週土曜 13:00 JST | Claude Haiku が同じ週の記事を別ファイルに生成 → 比較ページを自動作成 |

### 使用モデル

| 実行 | モデル | 種別 |
|---|---|---|
| 09:00 | `qwen3.6:35b-mlx` | Ollama ローカルLLM（デフォルト） |
| 13:00 | `claude-haiku-4-5-20251001` | Anthropic API（Claude Haiku） |

```bash
# 一時的にモデルを変更して実行
AI_NEWS_MODEL=qwen3.6:27b-mlx bash ~/projects/ai_news/scripts/run_ai_news.sh

# 常用モデルを変更する場合は com.user.ai_news.plist の EnvironmentVariables に追記:
# <key>AI_NEWS_MODEL</key>
# <string>qwen3.6:27b-mlx</string>
```

| モデル | サイズ | 特徴 |
|---|---|---|
| `qwen3.6:35b-mlx` | 21GB | **デフォルト**。品質優先 |
| `qwen3.6:27b-mlx` | 19GB | 速度優先（品質も十分） |
| `gemma4:31b-mlx` | 20GB | 代替候補 |

### 手動実行

```bash
# Ollama 版（09:00 相当）を今すぐ実行
bash ~/projects/ai_news/scripts/run_ai_news.sh

# Haiku 版（13:00 相当）を今すぐ実行
bash ~/projects/ai_news/scripts/run_ai_news_haiku.sh

# 比較ページのみ手動生成（両記事が揃っている場合）
python3 ~/projects/ai_news/scripts/generate_compare.py \
  --week-file 0525 --week-label "5/25〜5/31" --year 2026

# launchd 手動起動
launchctl start com.user.ai_news        # Ollama 版
launchctl start com.user.ai_news_haiku  # Haiku 版

# ログ確認
tail -f ~/projects/ai_news/ai_news.log        # Ollama ログ
tail -f ~/projects/ai_news/ai_news_haiku.log  # Haiku ログ
```

---

## 収集対象トピック

| カテゴリ | 内容 | 最新トピック |
|---|---|---|
| 🤖 モデルリリース | OpenAI / Anthropic / Google / Meta / Mistral 等の新モデル情報 | [GPT-5.4（OpenAI）](https://llm-stats.com/llm-updates) |
| 📄 注目論文 | arXiv等で話題になった研究（LLM・画像生成・エージェント等） | MoEアーキテクチャの実用化加速 |
| 🏢 ビジネス動向 | AI関連企業の動向・資金調達・提携・製品リリース | [Anthropic vs 国防総省（DOD）](https://techcrunch.com/2026/03/09/openai-and-google-employees-rush-to-anthropics-defense-in-dod-lawsuit/) |
| 📜 規制・政策 | 各国のAI規制・ガイドライン・法整備の動き | [米ホワイトハウス AI立法フレームワーク公開](https://www.whitehouse.gov/articles/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/) |
| 🛠️ ツール・OSS | 注目のAIツール・ライブラリ・OSSのリリース | [freee-mcp（freee）](https://corp.freee.co.jp/news/20260302freee_mcp.html) |
| 🇯🇵 国内動向 | 日本のAI関連ニュース・省庁・企業の取り組み | [楽天「Rakuten AI 3.0」正式公開](https://www.itmedia.co.jp/aiplus/articles/2603/17/news085.html) |

---

## 最新レポート全文

<!-- 最新の週次まとめ記事をここに表示 -->

# 生成AI週次ダイジェスト（5/30〜6/6）

> 自動生成: 2026-06-06 | 対象期間: 2026-05-30 〜 2026-06-06

## 今週のハイライト

1. **Anthropic: Claude Opus 4.8** — Super-Agentベンチマークでのトップ性能、Legal Agent Benchmark最高スコア、Online-Mind2Web 84%など大幅強化。Fast Modeはコスト3分の1で2.5倍速。
2. **Google DeepMind: Gemini 3.5 Flash + Gemini Omni** — エージェント特化モデル（Terminal-Bench 76.2%、MCP Atlas 83.6%）と動画生成マルチモーダルモデルの2本立て発表。
3. **OpenAI: ChatGPT Dreaming V3** — メモリ機能を刷新。計算コスト5分の1で無料ユーザーへも展開。
4. **デジタル庁: 源内OSSとして公開** — 全府省庁18万人を対象に大規模実証を開始。国産LLM7モデルを試用。

[→ Ollama版 全文を読む](./articles/weekly/2026-0606.md) | [→ Haiku版 全文を読む](./articles/haiku_weekly/2026-0606.md) | [→ Sonnet評価付き比較](./articles/compare/2026-0606.md)
