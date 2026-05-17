# ai_news — 生成AI最新情報ダイジェスト

## クイックリンク

| | リンク |
|---|---|
| 📰 最新週次まとめ | [articles/weekly/](./articles/weekly/) |
| 📅 月次まとめ | [articles/monthly/](./articles/monthly/) |
| ⚙️ 収集・生成仕様 | [SPEC.md](./SPEC.md) |

---

## 概要

生成AI（LLM・画像生成・マルチモーダル等）に関する最新情報を、
週次・月次で自動収集・要約してGitHubで公開するプロジェクト。

## プロジェクト構成

```
ai_news/
├── README.md                    # このファイル（最新記事一覧）
├── SPEC.md                      # 情報収集・記事生成の仕様
├── CLAUDE.md                    # Claude向け自動生成指示
├── articles/
│   ├── weekly/YYYY-WXX.md      # 週次まとめ記事（毎週月曜 自動生成）
│   └── monthly/YYYY-MM.md      # 月次まとめ記事（毎月第1月曜 自動生成）
└── scripts/
    ├── run_ai_news.sh           # 実行スクリプト（launchdから呼ばれる）
    └── com.user.ai_news.plist   # launchd設定ファイル（参考用）
```

### ファイル役割と更新方法

| ファイル | 役割 | 更新方法 | 更新頻度 |
|---|---|---|---|
| `articles/weekly/YYYY-WXX.md` | 週次まとめ記事 | **自動生成** | 毎週月曜 |
| `articles/monthly/YYYY-MM.md` | 月次まとめ記事 | **自動生成** | 毎月第1月曜 |
| `README.md` | 記事一覧・プロジェクト概要 | 手動 or 自動更新 | 記事追加時 |

---

## 最新記事

<!-- 自動更新される記事一覧 -->

### 週次まとめ

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

### 月次まとめ

- [2026年5月](./articles/monthly/2026-05.md)
- [2026年4月](./articles/monthly/2026-04.md)

<!-- articles/monthly/ のファイルへのリンクがここに追加される -->

### トピックス（臨時・深掘りレポート）

週次・月次とは別に、特定テーマを深掘りする単発レポート。

- [1ビットLLM — メモリ14分の1・8倍速推論の衝撃](./articles/topics/2026-04-06_1bit-llm.md)（2026-04-06）
- [MCP（Model Context Protocol） — AIエージェントの「配管工事」が業界標準へ](./articles/topics/2026-04-06_mcp.md)（2026-04-06）

<!-- articles/topics/ のファイルへのリンクがここに追加される -->

---

## 自動実行システム

Claude Code CLI（`claude`コマンド）を `scripts/run_ai_news.sh` 経由で呼び出し、
macOS の launchd によって定期実行する。

### スケジュール

| タイミング | 内容 |
|---|---|
| 毎週月曜 09:00 JST（第2〜5週） | 週次まとめ記事を自動生成・git push |
| 毎月第1月曜 09:00 JST | 月次まとめ記事を自動生成・git push |

### 手動実行

```bash
# 週次まとめを今すぐ生成
bash /path/to/ai_news/scripts/run_ai_news.sh

# launchd登録
launchctl load ~/Library/LaunchAgents/com.user.ai_news.plist

# launchd手動起動
launchctl start com.user.ai_news

# ログ確認
tail -f /path/to/ai_news/ai_news.log
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

# 生成AI週次ダイジェスト（5/18〜5/24）

> 自動生成: 2026-05-18 | 対象期間: 2026-05-12 〜 2026-05-18

## 今週のハイライト

1. **Google、Gemini IntelligenceをAndroid全体に展開** — GeminiがAndroid全機種でアプリをまたいで自律操作。Googlebook（Gemini専用ノートPC）も予告。
2. **OpenAI、GPT-5.5-Cyber を審査済みセキュリティ研究者に限定公開** — サイバー攻撃発見能力でAnthropicのMythosと性能が伯仲、政府アクセス交渉も進行。
3. **Anthropicがサブスクリプション体系を刷新（6月15日施行）** — エージェント用途を別課金プールに分離。実質値上げとなり開発者コミュニティで議論。

[→ 全文を読む](./articles/weekly/2026-0518.md)
