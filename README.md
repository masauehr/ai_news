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

- [4/13〜4/19](./articles/weekly/2026-W16.md)
- [4/6〜4/12](./articles/weekly/2026-W15.md)
- [3/30〜4/5](./articles/weekly/2026-W14.md)
- [3/23〜3/29](./articles/weekly/2026-W13.md)

<!-- articles/weekly/ のファイルへのリンクがここに追加される -->

### 月次まとめ

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

# 生成AI週次ダイジェスト（4/13〜4/19）

> 自動生成: 2026-04-13 | 対象期間: 2026-04-13 〜 2026-04-19

## 今週のハイライト

1. **OpenAI・Anthropic・Google が中国モデル複製問題で初の共同対抗（4/6）** — 三社が Frontier Model Forum 経由で情報共有を開始。Anthropic 単独で 1,600 万件の不正クエリを検出し、DeepSeek・Moonshot AI・MiniMax を名指し。
2. **Anthropic 年収ランレート 300 億ドル突破、OpenAI を初めて超える（4/6）** — 2025 年末の 90 億ドルから 4 ヶ月で 3 倍超に急拡大。Claude Mythos Preview の公開も重なり、エンタープライズ需要が爆発。
3. **国立情報学研究所「LLM-jp-4」公開、日本語性能で GPT-4o を一部上回る（4/3）** — 約 12 兆トークンで学習したフルスクラッチ国産 LLM が Apache 2.0 でオープンソース公開。

---

## 🤖 モデル・技術リリース

### Anthropic Claude Mythos（Capybara）Preview 公開（4/8）

- **発表元**: Anthropic
- **公開日**: 2026 年 4 月 8 日（Preview）
- **概要**: 3 月末に CMS 設定ミスで内部文書が流出し存在が判明していた次世代モデル「Claude Mythos」（内部コード名: Capybara）の Preview を限定公開。従来の Haiku・Sonnet・Opus の 3 階層を超える「第 4 のティア」として位置づける。
- **ポイント**: Claude Opus 4.6 比でコーディング・学術的推論・サイバーセキュリティ分野のテストスコアが「劇的に向上」と説明。一方、サイバー攻撃への応用リスクから「前例のないサイバーセキュリティ上のリスクを持つ」との懸念もリーク文書に記載されており、デュアルユース問題として業界の注目を集めている。現在は約 50 社のパートナー組織限定での試用段階。
- 参照: [Exclusive: Anthropic 'Mythos' AI model representing 'step change'（Anthropic「Mythos」モデル、「段階的変化」を代表するAI）](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) / [Anthropic leak reveals new model "Claude Mythos"（Anthropic が「Claude Mythos」を漏洩）](https://the-decoder.com/anthropic-leak-reveals-new-model-claude-mythos-with-dramatically-higher-scores-on-tests-than-any-previous-model/)

### Bonsai 8B — 1ビット重みで 1.15 GB・65 tok/sec のローカル LLM（PrismML）

- **発表元**: PrismML
- **概要**: 8B（80 億）パラメータの LLM を最初から 1 ビット重みで学習した超軽量モデル「Bonsai 8B」。通常の 8B モデル（16 GB 前後）の約 14 分の 1 にあたる **1.15 GB** で動作し、Apple Silicon 上で 65 tok/sec の推論速度を実現。
- **ポイント**: 従来の「後から量子化」アプローチとは異なり、重みを -1/+1 の 2 値のみで事前学習。乗算演算が不要になり CPU での高速推論が実現される。
- 参照: [1.15 GB で 8B モデルが動く「1-bit Bonsai」を Mac で試した](https://note.com/kazu_t/n/n00eedbb798e0) / [Bonsai-8B 考察 — 1-bit LLM は使い物になるのか](https://qiita.com/y0kud4/items/3f7faeea52d7eec01b0f)

---

## 🏢 ビジネス・業界動向

- **Anthropic** — 年収ランレートが **300 億ドル（約 4.5 兆円）** を突破し、OpenAI（約 250 億ドル）を初めて上回った（4/6）。法人顧客数は 2 ヶ月以内に倍増。Broadcom・Google との大規模コンピュート協定も拡大。参照: [Anthropic Tops $30 Billion Run Rate（Anthropic が 300 億ドルランレート突破）](https://www.bloomberg.com/news/articles/2026-04-06/broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic)

- **OpenAI・Anthropic・Google — 中国モデル複製防止で協力（4/6）** — Frontier Model Forum 経由で情報共有を開始。Anthropic 単独で DeepSeek・Moonshot AI・MiniMax の約 24,000 の不正アカウントから 1,600 万件超の無許可クエリを検出したと公表。3 社が競合関係を越えて協力する初のオペレーション。参照: [OpenAI, Anthropic, Google Unite to Combat Model Copying in China（中国モデル複製対策で連携）](https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china)

---

## 🛠️ ツール・OSS

- **MCP（Model Context Protocol）サーバー 1 万件超に到達** — 2026 年 4 月時点で登録サーバー数が 10,000 件を超え、ChatGPT・Cursor・Gemini・VS Code・Microsoft Copilot など主要ツールが標準対応済み。参照: [MCP とは？AIエージェントのツール連携を変えるオープン標準【2026年版】](https://renue.co.jp/posts/mcp-model-context-protocol-ai-agent-guide-2026)

---

## 🇯🇵 国内動向

### 国内AI企業・研究

- **国立情報学研究所（NII）「LLM-jp-4」オープンソース公開（4/3）** — 約 **12 兆トークン**で学習した国産 LLM を Apache 2.0 で公開。8B モデルと 32B-A3B MoE モデルの 2 種。日本語ベンチマークで GPT-4o・Qwen3-8B を一部上回る性能を達成。参照: [NII 公式リリース — LLM-jp-4 公開](https://www.nii.ac.jp/news/release/2026/0403.html)

### 政府・行政

- **ガバメントAI「源内」5 月より全省庁 39 機関・約 18 万人へ展開** — デジタル庁が 3 月に選定した国産 LLM 7 件を用いた実証が 2026 年 5 月から本格開始。2027 年 1 月に評価結果を公表し有償調達へ移行予定。参照: [今後のガバメントAI 源内の展開（デジタル庁・2026年3月6日）](https://www.digital.go.jp/assets/contents/node/information/field_ref_resources/2d69c287-2897-46d8-a28f-ea5a1fc9bce9/86f43a74/20260306_policies_ai_gennai_mass_deployment.pdf)

---

## 📜 規制・政策

- **EU AI 法 — GPAI 規制の 8 月 2 日施行が迫る** — 高リスク AI の適用は 2027 年 12 月に延期されたが、汎用目的 AI（GPAI）モデルプロバイダーへの規制は 8 月 2 日施行が維持される見込み。参照: [Where AI Regulation is Heading in 2026（2026 年 AI 規制の世界動向）](https://www.onetrust.com/blog/where-ai-regulation-is-heading-in-2026-a-global-outlook/)

---

## 編集後記

今週の最大のニュースは、競合関係にあった OpenAI・Anthropic・Google が中国勢による「アドバーサリアル・ディスティレーション」という共通の脅威に対して初めて協力体制を敷いたことだろう。AI の地政学的競争が技術革新の競い合いにとどまらず、知的財産保護の次元でも顕在化してきた。

国内では NII の「LLM-jp-4」が GPT-4o を一部上回る性能をオープンソースで達成したことが注目に値する。5 月からいよいよ始まるガバメントAI「源内」の全省庁展開と合わせ、日本の生成 AI 実装が量から質へと転換する局面を迎えようとしている。
