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

- [4/6〜4/12](./articles/weekly/2026-W15.md)
- [3/30〜4/5](./articles/weekly/2026-W14.md)
- [3/23〜3/29](./articles/weekly/2026-W13.md)

<!-- articles/weekly/ のファイルへのリンクがここに追加される -->

### 月次まとめ

- [2026年4月](./articles/monthly/2026-04.md)

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

# 生成AI週次ダイジェスト（4/6〜4/12）

> 自動生成: 2026-04-06 | 対象期間: 2026-04-06 〜 2026-04-12

## 今週のハイライト

1. **Google「Gemma 4」Apache 2.0 で公開（4/2）** — フロンティア級の性能をシングルGPUで実現するオープンモデル最新世代。ライセンスをApache 2.0に刷新し、企業導入の障壁を大幅に引き下げた。
2. **Anthropic Claude Code ソースコード約50万行が誤公開（3/31）** — npmレジストリへのデバッグファイル混入により約1,900ファイル・50万行が一時公開状態に。安全性最優先を掲げる同社のオペレーション上の課題として注目される。
3. **AWS がオープンソースMCPサーバー54種を一括公開（4/1）** — AWSの主要サービスをカバーするMCPサーバーをすべてOSSとして公開。MCPエコシステムのクラウド統合が加速。

---

## 🤖 モデル・技術リリース

### Google Gemma 4（Google DeepMind）

- **発表元**: Google DeepMind
- **公開日**: 2026年4月2日
- **概要**: Gemini 3 の研究成果をベースに構築した最新世代オープンモデルファミリー。4サイズ展開（5B dense・8B dense・26B MoE 4Bアクティブ・31B dense）。
- **ポイント**: Gemma 3 まで採用されていたカスタムライセンスを **Apache 2.0 に変更**し、企業での商用利用を大幅に容易化。31Bモデルは総合ベンチマークランキングで3位を記録し、シングルGPUで動作するモデルとしてはフロンティア級の性能。AMD の全GPU/CPUラインナップでもサポートされ、NVIDIA RTX AI Garage にも対応。開発者コミュニティからは過去世代の4億ダウンロードを背景に「Gemmaverse」が100,000バリアントを超えた。
- 参照: [Gemma 4: Byte for byte, the most capable open models（Gemma 4：パラメータあたり最高性能のオープンモデル）](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) / [Gemma 4: Expanding the Gemmaverse with Apache 2.0（Gemma 4とApache 2.0への移行）](https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html)

### rvLLM — Rust 製 vLLM 互換推論エンジン（OSS）

- **発表元**: コミュニティ（m0at / GitHub）
- **公開日**: 2026年4月4〜5日
- **概要**: Rust で実装した高性能 LLM 推論エンジン。vLLM のドロップイン代替として設計され、OpenAI 互換 API を提供。
- **ポイント**: Rust の低レイテンシ・省メモリ特性を活かし、vLLM より低いリソース消費での推論を目指す。コミュニティ実装ながら注目を集め、ローカル LLM 推論の代替選択肢が拡がりつつある。
- 参照: [GitHub — m0at/rvllm](https://github.com/m0at/rvllm)

---

## 📄 注目論文・技術動向

### GLM-4.5 — MoE 構成で商用フロンティアモデルに迫るオープンモデル

- **著者/機関**: Tsinghua University / Zhipu AI
- **概要**: MoE アーキテクチャを採用したオープンソース LLM。355B-A32B（3550億パラメータ・アクティブ32B）構成が最大。
- **意義**: SWE-bench Verified で 77.8% と高スコアを記録し、Claude Opus 4.6（80.8%）・MiniMax M2.5（80.2%）に肉薄。o3・Grok 4・Claude Opus 4.6 といったフロンティアモデルと競合しうるオープンモデルとして注目を集めている。

### PRCO — マルチモーダル LLM の知覚・推論同時強化

- **概要**: RLVR（報酬付き強化学習）を用いてマルチモーダル LLM の視覚的知覚能力と推論能力を同時に向上させる手法 PRCO（Perception-Reasoning Co-optimization）が arXiv で公開。
- **意義**: 8つの高難度ベンチマークで平均7ポイント以上の精度向上を達成。「見る力と考える力を同時に伸ばす」アプローチとして、マルチモーダルエージェント研究の先端的な手法として注目される。

---

## 🏢 ビジネス・業界動向

- **Anthropic**: 2026年3月31日、Claude Code の npm パッケージにデバッグファイルが誤って含まれ、内部ソースコード約1,900ファイル・50万行が一時的に公開状態になったと報じられた。「次世代モデル Mythos/Capybara」に関する未公開ドキュメント流出（3/28-29）に続くオペレーションミスとして業界の注目を集めた。参照: [Anthropic's 500K-Line Code Leak, Google Gemma 4 Goes Apache, and Q1 Funding Hits $297B（Anthropic 50万行漏洩・Gemma 4 Apache 化・Q1資金調達2970億ドル）](https://agenticaihype.substack.com/p/anthropics-500k-line-code-leak-google)

- **Q1 2026 AI資金調達 2,970億ドル（約44兆円）**: 2026年Q1の AI 関連資金調達額が 2,970億ドルに達したと報告。前年同期比で大幅増加。参照: [Anthropic's 500K-Line Code Leak, Google Gemma 4 Goes Apache, and Q1 Funding Hits $297B](https://agenticaihype.substack.com/p/anthropics-500k-line-code-leak-google)

- **Sakana AI — 三菱電機から出資（3/25）**: 東京発AI スタートアップ Sakana AI が三菱電機から出資を受けたことを発表。産業・組み込み領域でのAI活用に向けた提携として注目される。参照: [Sakana AI Receives Investment From Mitsubishi Electric Corporation（Sakana AI が三菱電機から出資を受ける）](https://www.finsmes.com/2026/03/sakana-ai-receives-investment-from-mitsubishi-electric-corporation.html)

- **TEAMZ Summit 2026（4/7〜8・東京）**: 日本最大級の Web3・AI カンファレンス「TEAMZ Summit 2026」が2026年4月7〜8日に東京・八芳園で開催。テーマは「Tradition Meets Tomorrow」。日本のAI・Web3エコシステムの最新動向が集まる場として注目される。

---

## 🛠️ ツール・OSS

- **AWS オープンソース MCPサーバー 54種公開（4/1）**: AWS が S3・Lambda・EC2 等の主要サービスを操作するMCPサーバー54種を一括でオープンソース公開。AIエージェントからクラウドインフラを自然言語で操作するユースケースが格段に広がった。参照: [【2026年4月最新】AWSが公開するオープンソースMCPサーバー カテゴリ別早見表](https://blog.supica.work/entry/aws-mcp-server-list-2026-04-01)

- **GMOペパボ「ムームードメイン」MCPサーバー提供開始（3/31）**: 国内ドメイン取得サービスとして初のリモートMCPサーバーを提供開始。AIエージェントとの自然言語対話でドメイン取得・管理が可能になった。参照: [AIとの会話でドメイン管理が可能に！ ムームードメイン byGMOペパボが国内初のリモートMCPサーバーを提供開始](https://pepabo.com/news/information/202603311100/)

---

## 🇯🇵 国内動向

### 国内AI企業・研究

- **Sakana AI**: 三菱電機からの出資を受け入れ（3/25）、産業・製造分野でのAI深化を図る。また先週公開した日本仕様LLM「Namazu」+「Sakana Chat」の反響が続いており、国内スタートアップとしての存在感を高めている。参照: [Sakana AI Receives Investment From Mitsubishi Electric Corporation（三菱電機がSakana AIに出資）](https://www.finsmes.com/2026/03/sakana-ai-receives-investment-from-mitsubishi-electric-corporation.html)

- **みずほFG × SB Intuitions**: みずほフィナンシャルグループと SB Intuitions が金融特化LLMの共同開発を進めていることが確認された。ベースモデルには SB Intuitions の「Sarashina」シリーズを使用。金融規制対応・専門用語への強さを重視した設計とみられる。

- **TEAMZ Summit 2026（4/7〜8）**: 東京・八芳園で日本最大級のWeb3・AIカンファレンスが開催。国内AI企業・スタートアップの最新動向が集まる場として注目。

### 政府・行政

- **デジタル庁「ガバメントAI（源内）」5月より全省庁展開へ**: 2026年3月6日に選定された国産LLM7件（NTTデータ tsuzumi 2・KDDI/ELYZA Llama-3.1-ELYZA-JP-70B・ソフトバンク Sarashina2 mini・NEC cotomi v3・富士通 Takane 32B・PFN PLaMo 2.0 Prime・カスタマークラウド CC Gov-LLM）を用いた実証が2026年5月から外局含む全39機関・約18万人を対象に開始される予定。2027年1月に評価結果を公表し、優れたモデルを有償調達する方針。参照: [（参考資料）今後のガバメントAI 源内の展開（デジタル庁・2026年3月6日）](https://www.digital.go.jp/assets/contents/node/information/field_ref_resources/2d69c287-2897-46d8-a28f-ea5a1fc9bce9/86f43a74/20260306_policies_ai_gennai_mass_deployment.pdf)

---

## 🖥️ ハードウェア・ローカルAI

- **NVIDIA RTX 50シリーズでVRAM 16GB が標準化**: RTX 5070 Ti 以上では 16GB VRAM が標準搭載となり、従来は RTX 4080 以上でないと確保できなかった 16GB 環境が普及価格帯に降りてきた。ローカルLLM（7B〜13B クラス）を快適に動かす閾値として VRAM 16GB が事実上の「新スタンダード」になりつつある。ローカルLLM 向け最適構成として「RTX 5060 Ti (16GB) + RAM 32GB」が推奨されるケースが増えている。参照: [生成AI向けPC22選！用途別のおすすめパソコン・選び方を徹底解説【2026年最新版】](https://www.ai-souken.com/article/ai-generation-pc-introduction)

- **AMD、Gemma 4 を全GPU/CPUラインナップでサポート**: AMD が Gemma 4 モデルファミリーを ROCm 経由で全製品ラインナップでサポートすることを発表。NVIDIA 一強だったローカルLLM 実行環境に AMD が本格参入。参照: [AMD Rolls Out Gemma 4 Model Support Across Full Range of GPUs & CPUs（AMD が全GPU/CPUで Gemma 4 サポート）](https://wccftech.com/amd-rolls-out-gemma-4-model-support-across-full-range-of-gpus-cpus/)

---

## 📜 規制・政策

- **EU AI Act**: 高リスクAIシステムの全面適用が2026年8月に迫る中、業界の対応準備が加速。欧州議会は3月に高リスクシステムの遵守期限を2027年12月に延期する改正案を可決済み。ただし GPAI（汎用目的AI）モデルプロバイダーへの規制は8月2日施行が維持される見込み。参照: [【2026年最新】EU・米国・日本・シンガポール。各国AI法の特徴と進捗を完全整理。](https://www.fidx.co.jp/%E3%80%902026%E5%B9%B4%E6%9C%80%E6%96%B0%E3%80%91eu%E3%83%BB%E7%B1%B3%E5%9B%BD%E3%83%BB%E6%97%A5%E6%9C%AC%E3%83%BB%E3%82%B7%E3%83%B3%E3%82%AC%E3%83%9D%E3%83%BC%E3%83%AB%E3%80%82%E5%90%84%E5%9B%BDai/)

- **日本AI法（AI事業者ガイドライン更新）**: IPA が2026年3月に令和7年度版 AI 事業者ガイドラインの更新内容を審議。2025年12月閣議決定の AI 基本計画を反映した改訂が進む。罰則を伴わない枠組みを維持しつつ、イノベーション促進と生成AIの悪用防止を両立させる方針。

---

## 編集後記

今週は「オープンAIの民主化」が一歩進んだ週と言える。Google Gemma 4 の Apache 2.0 ライセンス変更は単なるライセンス更新以上の意味を持ち、企業が安心してオープンモデルを商用製品に組み込める環境が整いつつある。AWS の MCP サーバー一括公開・GMO ペパボの国内初MCPサービス開始も、AIエージェントと既存インフラをつなぐ「配管工事」が着々と進んでいることを示している。

一方、Anthropic の連続したオペレーションミス（情報漏洩）は、AI 技術の信頼性が「モデルの性能」だけでなく「開発組織のセキュリティ成熟度」でも問われる時代であることを改めて示した。国内では5月から始まるガバメントAI「源内」の全省庁実証が、日本の行政デジタル化における正念場を迎える。
