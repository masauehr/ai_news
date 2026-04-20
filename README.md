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

- [4/14〜4/20](./articles/weekly/2026-W17.md)
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

# 生成AI週次ダイジェスト（4/14〜4/20）

> 自動生成: 2026-04-21 | 対象期間: 2026-04-14 〜 2026-04-20

## 今週のハイライト

1. **Anthropic が Claude Opus 4.7 を正式リリース（4/16）** — SWE-bench Pro 64.3% と業界最高スコアを記録。GPT-5.4 をコーディング・エージェント系ベンチマークで上回り、Anthropic が一般公開済みモデルのトップを奪還。
2. **OpenAI 次期フラッグシップ「Spud」（GPT-5.5/GPT-6 相当）の事前学習完了** — 3 月 24 日に事前学習終了が確認され、4 月内リリースの確率が Polymarket で 78% に達した。
3. **デジタル庁「源内」全府省庁展開が目前に** — 5 月から約 18 万人の政府職員を対象とした国産 LLM 7 モデルの大規模実証が開始予定。日本の行政 AI 活用が量的拡大フェーズへ。

---

## 🤖 モデル・技術リリース

### Claude Opus 4.7 — SWE-bench Pro 64.3%・エージェント系でGPT-5.4を超える（4/16）

- **発表元**: Anthropic
- **公開日**: 2026 年 4 月 16 日
- **概要**: Anthropic の最上位モデルが Opus 4.6 から Opus 4.7 に更新。SWE-bench Pro で **64.3%** を記録し、業界最高スコアを更新した。GPT-5.4（57.7%）を 6.6 ポイント上回る。
- **ポイント**: MCP-Atlas ツール呼び出しベンチマークで GPT-5.4 を **9.2 ポイント**リード。GPQA（科学的推論）94.2%、ビジョン性能も 57.7% → **79.5%** に大幅向上。価格は Opus 4.6 と同一（入力 $5 / 出力 $25 per M tokens）。
- 参照: [Introducing Claude Opus 4.7（Claude Opus 4.7 の発表）](https://www.anthropic.com/news/claude-opus-4-7) / [Anthropic releases Claude Opus 4.7, narrowly retaking lead（Anthropic が Claude Opus 4.7 をリリース、わずかな差で首位奪還）](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)

### Google Gemma 4 ファミリー — 31B Dense が 20 倍大のモデルを超える（4/2 リリース・今週も話題続く）

- **発表元**: Google DeepMind
- **概要**: 2B・4B・26B MoE・31B Dense の 4 バリアント。Apache 2.0 で公開。AIME 2026 にて 31B が **89.2%**（Gemma 3 の 20.8% から大幅向上）。Codeforces ELO が 110 → **2150** と史上最大の単世代ジャンプ。Android AICore Developer Preview で端末上動作も対応。
- 参照: [Welcome Gemma 4: Frontier multimodal intelligence on device（Gemma 4 の発表：オンデバイスで最先端マルチモーダル性能）](https://huggingface.co/blog/gemma4)

### Alibaba Qwen3.6-Plus — 100 万トークンコンテキスト・エージェントコーディング特化（4/2）

- **発表元**: Alibaba Cloud
- **概要**: エンタープライズ向けに最適化。**100 万トークン**コンテキストをデフォルト提供。オープンソース版 `Qwen3.6-35B-A3B`（Apache 2.0）も同時公開。
- 参照: [Alibaba Unveils Qwen3.6-Plus to Accelerate Agentic AI Deployment（Alibaba、エージェント AI 展開加速のため Qwen3.6-Plus を発表）](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603000)

### OpenAI 「Spud」— GPT-5.5/GPT-6 相当モデルの事前学習完了（リリース間近）

- **概要**: 内部コードネーム「Spud」が 3 月 24 日頃に事前学習完了。Polymarket では 4 月 30 日までのリリース確率を **78%** と評価。コンテキスト 256K〜512K 拡張・マルチステップツールチェーン強化が期待される。
- 参照: [OpenAI Spud: GPT-5.5 Pretraining Done, April Release Likely（OpenAI Spud：GPT-5.5 の事前学習完了、4 月リリース有力）](https://www.abhs.in/blog/openai-spud-gpt-5-5-release-date-polymarket-april-2026)

---

## 📄 注目論文

### Think Longer to Explore Deeper — 強化学習で未知問題への自律探索を強化

- **著者/機関**: arXiv cs.LG（2026年2月投稿・4月話題化）
- **概要**: 「長さインセンティブ型強化学習（Length-Incentivized RL）」により、AI が未知の問題に対して自律的に試行錯誤し正解に辿り着く能力を向上。単純な CoT 延長と異なり、モデル自身が「どこまで考えるべきか」を学習する。
- arXiv: [arXiv:2602.11748](https://arxiv.org/abs/2602.11748)

---

## 🏢 ビジネス・業界動向

- **Anthropic** — Opus 4.7 リリースと同時に Project Glasswing（Claude Mythos 限定評価プログラム）参加の約 50 社向けにも追加機能評価を開始。参照: [New AI Models April 2026（4 月の新 AI モデル動向）](https://whatllm.org/blog/new-ai-models-april-2026)
- **Google** — Gemma 4 を Android AICore の Developer Preview として統合。Pixel・Samsung 等の端末でオンデバイス推論を公式サポート。参照: [Android Developers Blog: Announcing Gemma 4 in the AICore Developer Preview（AICore Developer Preview に Gemma 4 を発表）](https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html)
- **AIエージェント市場** — 2025 年 52 億ドルから 2030 年 **526 億ドル**（CAGR 46.3%）成長予測。Fortune 500 の 80% が導入中も、63% がガバナンス課題に直面。

---

## 🛠️ ツール・OSS

- **MCP（Model Context Protocol）実装数 9,700 超** — ChatGPT・Cursor・Gemini・VS Code・Microsoft Copilot が標準対応済み。エンタープライズアプリベンダーの 30% が 2026 年内に独自 MCP サーバーを立ち上げる見込み。参照: [MCPは終わったのか？その議論が間違っている理由](https://www.workato.com/the-connector/ja/is-mcp-dead/)
- **TRON × deBridge MCP 統合（4/17）** — AI エージェントによるクロスチェーン決済の自律実行を可能に。参照: [TRON が deBridge MCP を統合（Bitcoin News）](https://news.bitcoin.com/ja/tron-debridge-mcp-tougou-ai-agent-muke-seamless-crosschain-jikkou-jitsugen/)

---

## 🇯🇵 国内動向

### 国内AI企業・研究

- **日本のAI産業 2026 — LLM-jp と「富岳 NEXT」が導く国産AIの逆襲（4/14 分析）** — NII の LLM-jp-4 公開と富岳 NEXT 稼働計画を踏まえ、日本が「フルスクラッチ国産基盤モデル」競争に再参入しつつある。参照: [日本のAI産業2026の展望（月影ブログ）](https://www.namuamidabu.com/entry/2026/04/14/193405)
- **Sakana AI・ELYZA・SB Intuitions など国内 AI スタートアップ** — 源内向け国産 LLM 選定を受け、各社が行政向けファインチューニングを本格化。5 月の大規模実証後に「品質競争フェーズ」へ。

### 政府・行政

- **デジタル庁「源内」— 5 月より全府省庁 39 機関・約 18 万人へ展開開始** — 国産 LLM 7 モデル（NEC・PFN PLaMo 等）の実証が 2026 年 5 月開始。2027 年 1 月に評価公表後、有償調達へ移行。参照: [デジタル庁が国産AI「7人の侍」選定（SBビジネス）](https://www.sbbit.jp/article/cont1/182108) / [今後のガバメントAI 源内の展開（デジタル庁資料）](https://www.digital.go.jp/assets/contents/node/information/field_ref_resources/2d69c287-2897-46d8-a28f-ea5a1fc9bce9/86f43a74/20260306_policies_ai_gennai_mass_deployment.pdf)

---

## 📜 規制・政策

- **EU AI 法 GPAI 規制、8 月 2 日施行が維持の見込み** — 汎用目的 AI プロバイダーへの透明性・著作権遵守要件は 8 月 2 日施行予定を維持。参照: [Where AI Regulation is Heading in 2026（2026 年 AI 規制の世界動向）](https://www.onetrust.com/blog/where-ai-regulation-is-heading-in-2026-a-global-outlook/)
- **内閣府「人工知能基本計画骨子案」— 関係府省庁の取り組みをとりまとめ** — 研究開発から社会実装・安全確保まで横断的な政策連携が明確化。参照: [人工知能基本計画骨子案に係る関係府省庁の取組（内閣府）](https://www8.cao.go.jp/cstp/ai/ai_expert_panel/2kai/shiryo1_2.pdf)

---

## 編集後記

今週最大のニュースは Claude Opus 4.7 のリリースだ。SWE-bench Pro 64.3% という数字は、AI がソフトウェアエンジニアリングの実務でどこまで使えるかを測る業界の「ものさし」として重みを増している。Anthropic・OpenAI・Google のフラッグシップ競争は、コーディング性能とエージェント能力の二軸で急速に激化しており、来週にも OpenAI 「Spud」のリリース発表があれば再び順位が入れ替わる可能性がある。

国内では 5 月に始まる「源内」18 万人展開が注目点。LLM-jp-4 や PLaMo といった国産モデルが実際の行政業務でどう評価されるかが、日本のAI政策の今後を左右する試金石になりそうだ。
