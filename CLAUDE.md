# CLAUDE.md — ai_news プロジェクト専用指示

## このプロジェクトについて

生成AI（LLM・画像生成・マルチモーダル等）に関する最新情報を週次・月次でまとめ、
GitHubで公開するプロジェクト。毎週月曜日に自動実行される。

---

## 自動実行時の動作フロー

### Step 1: 日付判定

今日が「月の第1月曜日」かどうかを判定する。

```bash
DAY=$(TZ=Asia/Tokyo date +%d)
if [ "$DAY" -le 7 ]; then
  # 月次モード（月次まとめ + 週次まとめ）
else
  # 週次モードのみ
fi
```

### Step 2: 情報収集（WebSearch / WebFetch）

以下のサイト・キーワードで最新情報を収集する（直近7日間を対象）:

**収集キーワード（WebSearch）**:
- `生成AI 最新ニュース 今週`
- `LLM release 今週`
- `OpenAI Anthropic Google AI news`
- `AI 規制 法律 日本`
- `arXiv LLM 注目論文`

**優先収集キーワード（SPEC.md の注目トピック — 必ず検索すること）**:
- `ローカルLLM Ollama 新モデル` / `小型LLM 量子化 最新`
- `AIエージェント MCP AutoGen 最新動向`
- `AI PC NPU VRAM ローカルAI スペック`
- `デジタル庁 生成AI` / `行政 AI活用 自治体`

**日本国内AI動向（必ず個別に検索すること）**:
- `Sakana AI 最新` — さくらインターネット・SB Intuitions等の国産LLM開発動向も含む
- `日本 AI スタートアップ 資金調達 最新`
- `PFN preferred networks AI`
- `国産LLM 新モデル リリース`
- `日本 生成AI 企業導入 事例 最新`
- `NEDO JST AI 研究開発 採択`

**参照サイト（WebFetch）**:
- OpenAI Blog
- Anthropic News
- Google DeepMind Blog
- Hugging Face Blog
- ITmedia AI+
- Sakana AI Blog（https://sakana.ai/blog/）
- AINOW（https://ainow.ai/）
- 窓の杜 AI関連（https://forest.watch.impress.co.jp/）

### Step 3: 週次記事の生成

ファイル名: `articles/weekly/YYYY-WXX.md`（例: `2026-W14.md`）

SPEC.md の週次フォーマットに従い記事を生成する。
- 最低5トピック以上を収録（日本国内動向を必ず1件以上含める）
- 各情報源のURLを必ず記載
- 日本語で記述（技術用語・モデル名は原語のまま）
- **英語記事・英語タイトルのリンクには、必ず日本語訳タイトルを併記する**
  - 例: `[Introducing GPT-5.4（GPT-5.4の発表）](https://...)`
  - 例: `参照: [OpenAI Blog — Introducing o3（o3の紹介）](https://...)`
- 記事タイトルは `# 生成AI週次ダイジェスト（MM/DD〜MM/DD）` の形式で月日表記を使うこと
  （スクリプトから渡される `WEEK_LABEL` の値を使う）

### Step 4: 月次記事の生成（第1月曜のみ）

ファイル名: `articles/monthly/YYYY-MM.md`（例: `2026-03.md`）

SPEC.md の月次フォーマットに従い記事を生成する。
- 前月の週次まとめ記事を参照してサマリーを作成
- 主要トピックを3件以上深掘り

### Step 5: README.md の更新

`README.md` の「最新記事」セクションに、生成した記事へのリンクを追記する。

週次まとめのリンク形式:
```markdown
- [MM/DD〜MM/DD](./articles/weekly/YYYY-WXX.md)
```
（例: `- [3/23〜3/29](./articles/weekly/2026-W13.md)`）

月次まとめのリンク形式:
```markdown
- [YYYY年MM月](./articles/monthly/YYYY-MM.md)
```

### Step 6: git commit & push

```bash
git add articles/ README.md
git commit -m "YYYY-WXX 週次まとめを追加

- トピック数: X件
- 主な内容: 〜

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

git push origin main
```

---

## 記事生成の注意事項

- 情報ソースのURLは必ず記載する
- 推測・憶測は「〜とみられる」「〜の可能性がある」と明示する
- 個人情報・機密情報は含めない
- 著作権に配慮し、要約・引用にとどめる（原文の大量コピーは避ける）
- 既存の記事ファイルは上書きしない（同名ファイルが存在する場合はスキップ）

---

## ファイルパス一覧

| 目的 | パス |
|---|---|
| 週次記事 | `/Users/masahiro/projects/ai_news/articles/weekly/YYYY-WXX.md` |
| 月次記事 | `/Users/masahiro/projects/ai_news/articles/monthly/YYYY-MM.md` |
| README | `/Users/masahiro/projects/ai_news/README.md` |
| 実行ログ | `/Users/masahiro/projects/ai_news/ai_news.log` |
