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

- [3/23〜3/29](./articles/weekly/2026-W13.md)

<!-- articles/weekly/ のファイルへのリンクがここに追加される -->

### 月次まとめ

<!-- articles/monthly/ のファイルへのリンクがここに追加される -->

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

# 生成AI週次ダイジェスト（3/23〜3/29）

> 自動生成: 2026-03-26 | 対象期間: 2026-03-23 〜 2026-03-29

## 今週のハイライト

1. **ホワイトハウスがAI立法フレームワークを公開（3/20）** — 6つの指針をもとに連邦AI規制の方向性を議会に提示。州法の上書きを含む包括的な方針。
2. **楽天「Rakuten AI 3.0」正式公開（3/17）** — 約7,000億パラメータのMoEモデルをApache 2.0で無償公開。国産最大規模のLLMがオープンソースに。
3. **MCP 2026年ロードマップ公開（3/9）** — Anthropic主導のModel Context Protocolがエージェント連携インフラへ進化。9,700以上の実装が稼働中。

---

## 🤖 モデル・技術リリース

### GPT-5.4（OpenAI）

- **発表元**: OpenAI
- **概要**: 2026年3月5日リリース。最大105万トークンのコンテキストウィンドウを持つOpenAI最新フロンティアモデル。Standard・Thinking・Proの3バリアント。
- **ポイント**: GPT-5.2比でファクト誤りを33%削減。動的なツール呼び出しを行う新アーキテクチャ「Tool Search」を搭載。
- 参照: [AI Updates Today (March 2026) — Latest AI Model Releases（最新AIモデルリリース）](https://llm-stats.com/llm-updates)

### Qwen 3.5 Small（Alibaba）

- **発表元**: Alibaba / Qwen Team
- **概要**: 2026年3月1日リリース。0.8B・2B・4B・9Bの4サイズ展開。テキスト・画像・動画をネイティブにサポートするマルチモーダルオープンモデル。
- **ポイント**: 別途ビジョンアダプタ不要で同一ウェイトからマルチモーダル推論が可能。ローカル動作にも対応。
- 参照: [AI Updates Today (March 2026) — Latest AI Model Releases（最新AIモデルリリース）](https://llm-stats.com/llm-updates)

### DeepSeek-V3.2（DeepSeek）

- **発表元**: DeepSeek
- **概要**: オープンソースの高性能LLM最新版。DeepSeek Sparse Attention（DSA）による長文脈処理、8万5,000件以上のエージェントタスクで強化学習。
- **ポイント**: オープンウェイトモデルとして現時点でトップクラスの実力とされ、企業・研究者に広く活用されている。
- 参照: [Breaking: Open Source LLM Updates & AI Releases (March 2026)（オープンソースLLMアップデート）](https://www.clawpod.co/blog/llm-news-open-source-ai-models-march-2026)

### Ollama v0.18.0

- **発表元**: Ollama
- **概要**: 2026年3月時点の最新安定版。`ollama launch` コマンドが追加され、Claude Code・Codex等の外部ツールとワンコマンド連携が可能に。
- **ポイント**: Gemma3:27b、Qwen3.5、DeepSeek-R1など最新モデルをワンコマンドでローカル実行できる。VRAM 8GBからも動作可能なモデルを多数収録。
- 参照: [【2026年最新版】ローカルLLM（Ollama）で完全オフラインAI開発環境を作る](https://qiita.com/miruky/items/026aeee6b59f78df5e9d)

---

## 📄 注目論文・技術動向

### MoEアーキテクチャの実用化加速

- **概要**: Rakuten AI 3.0・DeepSeek-V3.2・Qwen3.5いずれもMixture of Experts（MoE）を採用。総パラメータは大きくとも推論時の有効パラメータを絞ることで、ローカル機器でも動作しうる設計が主流化しつつある。
- **意義**: クラウドAPI依存からオンプレ・エッジ推論への移行を加速させるアーキテクチャトレンドとして注目。

---

## 🏢 ビジネス・業界動向

- **Anthropic vs 国防総省（DOD）**: AnthropicがDODから「サプライチェーンリスク」指定を受けた問題をめぐり、OpenAI・Google DeepMindの従業員30名以上がAnthropicを支持する声明に署名。Anthropicは大量監視・自律兵器への技術利用を拒否したことが発端。AnthropicCEOのDario Amodei氏はOpenAIの対応を「安全性のポーズ」と批判。参照: [OpenAI and Google employees rush to Anthropic's defense in DOD lawsuit（Anthropicの訴訟でOpenAI・Google従業員が支持）](https://techcrunch.com/2026/03/09/openai-and-google-employees-rush-to-anthropics-defense-in-dod-lawsuit/)

- **Google Gemini 成長**: Gemini有料契約者が前年比258%増。Claude（同200%増）を上回るペースで拡大。GoogleはDODの300万人職員向けAIエージェントの提供も計画中。参照: [Google's AI grew 258% while OpenAI and Anthropic fought in court（Googleのシェア拡大）](https://ucstrategies.com/news/googles-ai-grew-258-while-openai-and-anthropic-fought-in-court/)

- **Microsoft Copilot Cowork**: 企業向けAIエージェント「Copilot Cowork」をローンチ。PC上のファイルを読み込み・分析・操作するオンデバイスエージェント機能を提供。

- **Google Stitch「Vibe Design」**: Google AIデザインツール「Stitch」を大幅更新。テキスト・音声指示からUIを自動生成する「Vibe Design」を発表。Figma株価が一時8.8%下落するほどのインパクトを与えた。

---

## 🛠️ ツール・OSS

- **freee-mcp（freee）**: 2026年3月3日にOSSとして公開。AIエージェントがfreeeの経理・請求・人事機能をMCP経由で操作可能に。参照: [freee、AIエージェントからfreeeの基幹業務を操作可能にするMCPサーバー「freee-mcp」をOSSとして公開](https://corp.freee.co.jp/news/20260302freee_mcp.html)

- **MCP（Model Context Protocol）v2026ロードマップ**: Anthropic主導で「サーバー機能の自動発見」「非同期タスク処理の強化」「通信方式の進化」の3点を重点課題に設定。AIエージェントが複数サービスを自律連携するインフラ規格として事実上の標準化が進行中。参照: [MCPは死んでない？ MCPの2026年ロードマップ公開](https://atmarkit.itmedia.co.jp/ait/articles/2603/16/news011.html)

---

## 🇯🇵 国内動向

### 国内AI企業・研究

- **楽天**: 2026年3月17日、「Rakuten AI 3.0」を正式公開。MoEアーキテクチャで総671Bパラメータ（推論時有効37〜40B）。Apache 2.0ライセンスで商用利用可能。経産省・NEDOのGENIACプロジェクト支援を受けて開発。参照: [楽天、日本語LLM「Rakuten AI 3.0」公開 商用利用も可能](https://www.itmedia.co.jp/aiplus/articles/2603/17/news085.html)

- **KDDI / ELYZA**: Llama-3.1-ELYZA-JP-70Bがデジタル庁のガバメントAI「源内」用国産LLMとして選定。MetaのLlama-3.1-70BベースにELYZAが日本語追加学習を施したモデル。参照: [KDDIとELYZA、デジタル庁の「ガバメントAIで試用する国内大規模言語モデル」に選定](https://biz.kddi.com/topics/2026/news/004/)

- **NTTデータ**: 2026年度中にITシステム開発の大半を生成AIで自動化する方針を発表。開発工程の効率化とコスト削減を目指す。

### 政府・行政

- **デジタル庁**: 2026年3月6日、全府省庁約18万人を対象とした生成AI基盤「ガバメントAI（源内）」に活用する国産LLM 7件を選定。選定モデル: NTTデータ「tsuzumi 2」、KDDI/ELYZA「Llama-3.1-ELYZA-JP-70B」、SoftBank「Sarashina2 mini」、NEC「cotomi v3」、富士通「Takane 32B」、PFN「PLaMo 2.0 Prime」、カスタマークラウド「CC Gov-LLM」。2026年5月より実証開始、2027年1月に評価結果公表予定。参照: [デジタル庁が国産AI「7人の侍」選定、行政AI「源内」全府省庁18万人で実証](https://www.sbbit.jp/article/cont1/182108)

---

## 📜 規制・政策

- **米国ホワイトハウス（3/20）**: トランプ政権がAI立法フレームワーク「National Policy Framework for Artificial Intelligence」を公開。6つの指針として「子どもの安全」「知的財産保護」「検閲防止・表現の自由」「イノベーション促進」「AI人材育成」「コミュニティ保護」を掲げる。新たな連邦AI規制機関は設けず、既存省庁の業種別規制を維持する方針。参照: [President Donald J. Trump Unveils National AI Legislative Framework（トランプ大統領、AI立法フレームワークを公表）](https://www.whitehouse.gov/articles/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/)

- **EU AI Act（3/13）**: EU理事会がAI規制の一部簡素化案に合意。デジタル立法の調和を図る規制整理の方向性を示した。参照: [Council agrees position to streamline rules on Artificial Intelligence（EU、AI規制の簡素化案に合意）](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/)

- **日本国内**: デジタル庁による国産LLM選定（上記「国内動向」参照）のほか、NTT・富士通・SBCなどが国内AIスパコン能力（ソブリン・コンピューティング）の整備を加速させている。

---

## 編集後記

今週は「日本の生成AI実装」が大きな一歩を踏み出した週といえる。デジタル庁によるガバメントAI「源内」向け国産LLM 7件の選定は、行政デジタル化の核にLLMを据えるという明確な意思表示だ。楽天のRakuten AI 3.0公開と合わせ、国産LLMエコシステムが着実に育ちつつある。

一方、海外では米国のAI立法フレームワーク発表・Anthropic対DODの法廷闘争など、AI利用の「ガバナンス競争」が加速。技術的には GPT-5.4・Qwen3.5・DeepSeek-V3.2と高性能モデルが相次ぎリリースされ、ローカルLLMの選択肢もさらに広がった。MCPの2026年ロードマップ公開も含め、来週以降はエージェント実用化の動きに注目が集まる。
