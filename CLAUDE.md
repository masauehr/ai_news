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

**参照サイト（WebFetch）**:
- OpenAI Blog
- Anthropic News
- Google DeepMind Blog
- Hugging Face Blog
- ITmedia AI+

### Step 3: 週次記事の生成

ファイル名: `articles/weekly/YYYY-WXX.md`（例: `2026-W14.md`）

SPEC.md の週次フォーマットに従い記事を生成する。
- 最低5トピック以上を収録
- 各情報源のURLを必ず記載
- 日本語で記述（技術用語・モデル名は原語のまま）

### Step 4: 月次記事の生成（第1月曜のみ）

ファイル名: `articles/monthly/YYYY-MM.md`（例: `2026-03.md`）

SPEC.md の月次フォーマットに従い記事を生成する。
- 前月の週次まとめ記事を参照してサマリーを作成
- 主要トピックを3件以上深掘り

### Step 5: README.md の更新

`README.md` の「最新記事」セクションに、生成した記事へのリンクを追記する。

週次まとめのリンク形式:
```markdown
- [YYYY年WXX週（MM/DD〜MM/DD）](./articles/weekly/YYYY-WXX.md)
```

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
