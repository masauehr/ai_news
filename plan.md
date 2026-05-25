# ai_news 作業予定

## 未完了タスク

### [ ] GitHub Pages を有効化する（手動・1回のみ）

https://github.com/masauehr/ai_news/settings/pages を開き、
Branch: `main` / folder: `/ (root)` → Save

有効化後のサイト: https://masauehr.github.io/ai_news/

---

### [ ] 2026-05-30（土）自動実行後のログ確認

次回自動実行で `update_index` が正しく呼ばれるか確認する。

```bash
tail -50 ~/projects/ai_news/ai_news.log
```

確認ポイント:
- `update_index` のログ行が存在するか
- `articles/weekly/index.md` と `index.md` が git に含まれているか

スキップされていた場合 → `write_article` と同様の強制促進ロジックを追加する。

---

## 完了済み

- [x] Jekyll サイト構築（`_config.yml` / `_layouts/default.html` / `index.md`）
- [x] 全記事に Jekyll front matter を追加（`---\nlayout: default\n---`）
- [x] `articles/weekly/index.md` 週次一覧ページを作成
- [x] `articles/monthly/index.md` 月次一覧ページを作成
- [x] `local_agent.py`: 新記事に front matter を自動付与
- [x] `local_agent.py`: `update_index` ツールを追加（3ファイル同時更新）
- [x] `README.md` にサイトリンクを追加
