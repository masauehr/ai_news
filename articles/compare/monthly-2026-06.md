---
layout: compare
title: 月次比較（2026年6月）
---

<div class="compare-header">
  <h1>🔬 月次比較（2026年6月）</h1>
  <div class="compare-meta">
    <span class="badge ollama">🖥️ Ollama</span>
    <span style="font-family:monospace;font-size:0.82rem;color:#666">qwen3.6:35b-mlx（第1土曜 09:00 生成）</span>
    <span style="margin: 0 0.5rem;">vs</span>
    <span class="badge haiku">⚡ Claude</span>
    <span style="font-family:monospace;font-size:0.82rem;color:#666">claude-haiku-4-5（第1土曜 13:00 生成）</span>
  </div>
</div>

<div class="compare-wrapper">

<div class="compare-panel ollama-panel">
<div class="panel-header-bar">
  <span class="model-badge">🖥️ Ollama</span>
  <span class="model-name">qwen3.6:35b-mlx</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI月次ダイジェスト（2026年6月）

2026年6月は、主要AIプレイヤーが相次いで大規模アップデートを発表した月です。AnthropicはClaude Opus 4.8のリリースとProject Glasswingの大幅拡大、Google DeepMindはGemini 3.5 Flash/Omniの発表、OpenAIはChatGPT Dreaming V3の刷新、MicrosoftはMAI-Image-2.5の登場など、モデル性能・エージェント機能・マルチモーダル生成の各領域で重要な進展がありました。また、デジタル庁はガバメントAI「源内」をOSSとして公開し、全府省庁への展開を開始するなど、日本国内のAI動向も活発でした。

---

## 1. モデル性能・エージェント機能

### Anthropic: Claude Opus 4.8
AnthropicはClaude Opus 4.8を発表しました。Super-AgentベンチマークでGPT-5.5を凌駕し、全ケースをエンドツーエンドで完了した唯一のモデルとなりました。Legal Agent Benchmarkで過去最高スコア、Online-Mind2Webで84%というComputer Useモデルとして最高のスコアを記録しました。Fast Modeが従来比3倍の速度で、コストは1/3に削減されました。

### Google DeepMind: Gemini 3.5 Flash
エージェントおよびコーディング性能に特化したGemini 3.5 Flashを発表。Terminal-Bench 2.1で76.2%、GDPval-AAで1656 Elo、MCP Atlasで83.6%など、エージェントベンチマークで先行モデルを凌駕しました。出力トークン/秒において他のフロンティアモデル比4倍高速です。

### OpenAI: ChatGPT Dreaming V3
OpenAIは6月4日、ChatGPTのメモリ（記憶）機能を大幅に刷新した「Dreaming V3」を導入。Saved Memoriesを完全置換し、計算コストが従来比5分の1に削減。無料ユーザーへの展開が可能になりました。

---

## 2. マルチモーダル・画像生成

### Google DeepMind: Gemini Omni
「推論」と「創造」を融合した新モデルファミリー。画像・音声・動画・テキストを入力として受け取り、高品質な動画を生成することができます。Conversation-based Video Editingにより自然言語による動画編集が可能になり、キャラクターの一貫性、物理法則の保持、シーン記憶を実現しています。

### Microsoft: MAI-Image-2.5
テキストから画像生成（text-to-image）および画像編集（image-edit）の両Arenaリーダーボードでトップクラスのパフォーマンスを達成。Fine-grained Edit Controlにより物体の置換、テキスト更新、モーションブラー除去など精密なローカライズ編集に対応しています。

### Google DeepMind: Gemma 4 12B
ノートPCでの利用を想定したマルチモーダルAIモデル。エンコーダーフリーユニファイドアーキテクチャを採用し、16GB VRAM/統合メモリのノートPCで動作します。推論性能は26B MoEに迫る水準を達成しています。

---

## 3. Physical AI・ローカルLLM

### NVIDIA: Cosmos 3
「世界生成」「物理推論」「行動生成」を1つのモデルで実現するPhysical AI向けオムニモデル。MoT（Mixture-of-Transformers）アーキテクチャにより、全モダリティを単一の統一アーキテクチャで処理します。Cosmos 3 Nano（16B）はワークステーションクラス向けに最適化。

### Anthropic: Project Glasswing 拡大
Claude Mythos Previewモデルを使用して主要なソフトウェアの脆弱性をスキャンするProject Glasswingを約150の新たな組織に拡大。15カ国以上で展開され、電力、水道、医療、通信、ハードウェアなど重要インフラ業界をカバー。初期50組織から10,000以上の高・重大度脆弱性を発見しました。

---

## 4. AIガバナンス・倫理

### Anthropic: Chris Olah氏、教皇レオ14世のAI回勅で講演
Anthropic創設者のChris Olah氏は、教皇レオ14世が発表したAIに関する回勅「Magnifica humanitas」の発表式典で講演。AI開発は単なる技術問題ではなく、人文科学、宗教、哲学、社会全体の問題であると強調しました。

---

## 5. 日本国内動向

### デジタル庁: ガバメントAI「源内」OSS公開 & 全府省展開
デジタル庁は「源内（げんない）」をオープンソースソフトウェア（OSS）として公開し、全府省庁約18万人の政府職員を対象とした大規模実証を開始しました。2026年度中に全府省庁約18万人の政府職員が生成AIを利用可能とする予定。

---

## 今月のまとめ

2026年6月はAIモデル性能・エージェント機能・マルチモーダル生成の各領域で重要な進展があった月です。特にAnthropicの$965Bバリュエーション達成と、Claude Opus 4.8・Gemini 3.5 Flash・Gemini Omniなど各社のエージェント機能強化が顕著でした。国内では源内OSS公開が日本のAIガバナンス・実装の進展を示しています。

**参考文献**
- [Introducing Claude Opus 4.8 - Anthropic](https://www.anthropic.com/news/claude-opus-4-8)
- [Gemini 3.5: frontier intelligence with action - Google DeepMind Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [ChatGPTのメモリ機能が刷新「Dreaming V3」 - Techno Edge](https://www.techno-edge.net/article/2026/06/05/5150.html)
- [Introducing Gemini Omni - Google DeepMind Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)
- [Introducing MAI-Image-2.5 - Microsoft AI](https://microsoft.ai/news/introducing-mai-image-2-5/)
- [Welcome NVIDIA Cosmos 3 - Hugging Face Blog](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)
- [Expanding Project Glasswing - Anthropic](https://www.anthropic.com/news/expanding-project-glasswing)
- [ガバメントAI「源内」 - デジタル庁](https://www.digital.go.jp/policies/genai)

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI月次ダイジェスト（2026年6月）

2026年6月は、主要AIプレイヤーが資金調達・新モデル・エージェント機能において相次いで大型発表を行った月です。Anthropicは史上最大規模の調達でOpenAIのバリュエーションを超え、GoogleはGemini 3.5 Flash/Omniで動画生成とエージェントの融合を実現、OpenAIはメモリ機能を刷新した「Dreaming V3」を全ユーザーに展開しました。国内では、デジタル庁「源内」OSSの公開と8社共同「日本AI基盤モデル開発会社」の設立が、日本のAI主権確立に向けた重要な一歩となりました。

---

## 1. 主要モデル・プラットフォームの動向

### Anthropic: $65B調達・Claude Opus 4.8・Stainless買収

**資金調達**: Series HでAlitimeter Capital、Dragoneer、Sequoia Capitalから$65Bを調達。ポストマネーバリュエーションは$965Bに達し、OpenAI（$730B）を超え生成AI企業として世界最高の評価額となりました。

- 出所: [Anthropic Series H](https://www.anthropic.com/news/series-h)

**Claude Opus 4.8**: Super-Agentベンチマークで全ケースを完遂した唯一のモデル。Claude DesignとClaude Is A Space To Think機能が統合。Fast Modeはコスト3分の1で2.5倍速。

**Stainless買収**: APIおよびSDK開発ツール企業Stainlessを買収し、MCPエコシステムを強化しました。

---

### Google DeepMind: Gemini 3.5 Flash + Gemini Omni

**Gemini 3.5 Flash**: エージェントとコーディングに特化したモデル。他フロンティアモデル比4倍の高速推論を実現し、24時間稼働の個人用AIエージェント「Gemini Spark」のベースとなっています。

- Terminal-Bench 2.1: 76.2%、MCP Atlas: 83.6%
- 出所: [Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

**Gemini Omni**: 動画生成マルチモーダルモデル。自然言語による動画編集（Conversation-based Video Editing）が可能で、Geminiアプリ・Google Flow・YouTube Shortsに展開中。

---

### OpenAI: Dreaming V3・Codex Windows対応

**ChatGPT Dreaming V3**: メモリ機能を全面刷新。計算コストを5分の1に削減し、無料ユーザーへの展開を実現。Memory Summaryページで好み・プロジェクト情報を可視化。

**Codex Windows対応**: macOSに続きWindows 11でもComputer Useが利用可能に。モバイルからの遠隔操作機能も追加。

---

### Microsoft: MAI-Image-2.5・BitNet a4.8

**MAI-Image-2.5**: Arena Image Edit No.2、Arena Text-to-Image No.3を達成。精密な画像編集とFace Identity Consistencyを実現。

**BitNet a4.8**: 1-bit LLMのさらなる進化。16倍のメモリ削減により、CPUでの実用的な推論が可能に。

---

### NVIDIA: Cosmos 3・Google: Gemma 4 12B

**NVIDIA Cosmos 3**: Physical AI向けオムニモデル。全モダリティを単一アーキテクチャで処理するCosmos 3 Nano（16B）/ Super（64B）の2サイズをHugging Faceで公開。

**Gemma 4 12B**: ノートPC向け（16GB VRAM）マルチモーダルエージェントモデル。Apache 2.0ライセンスで商用利用も自由。Gemmaシリーズ累計1億5000万ダウンロードを突破。

---

## 2. 日本国内AI動向（特集）

### デジタル庁「源内」OSSとして公開・全府省展開

政府共用生成AI基盤「源内（げんない）」をOSS（商用利用可能ライセンス）として公開。全府省庁約18万人への展開を2026年度中に完了する計画。国産LLM7モデル（tsuzumi 2・Sarashina2 miniなど）の大規模実証（2026年5月〜2027年3月）を実施中。

- 出所: [ガバメントAI「源内」（デジタル庁）](https://www.digital.go.jp/policies/genai)

### 日本AI基盤モデル開発会社の設立（8社共同）

ソフトバンク・NEC・ホンダ・ソニーグループなど8社が共同出資し「日本AI基盤モデル開発」が正式設立。デジタル庁の2026年度予算では生成AI関連に約5,198億円を計上。官民一体での日本AI主権確立が急ピッチで進んでいます。

- 出所: [note / 孤独なプログラマー](https://note.com/ken_1101/n/ndb64ea9832c9)

### NII: 国産LLM「LLM-jp-4」公開

国立情報学研究所が約12兆トークンの良質なコーパスで学習した「LLM-jp-4」（8B・32B-A3B）を公開。一部ベンチマークではGPT-4oやQwen3-8Bを上回る日本語性能を達成。

### 生成AIのビジネス活用が「インフラ化」段階へ

医療・保険・マーケティングなどの業界で生成AIが業務インフラとして定着。チャットツール活用からAIエージェントへの転換が本格化しています。

---

## 今月のトレンドまとめ

| テーマ | 主な動き |
|---|---|
| **AI企業の資本集中** | Anthropicが$965Bバリュエーション達成。投資競争が最高潮 |
| **エージェントAIの実用化** | Claude Opus 4.8・Gemini 3.5 Flash・Codex Windowsがエージェント機能を強化 |
| **マルチモーダル動画生成** | Gemini Omniが自然言語×物理シミュレーションによる動画生成を実現 |
| **日本のAI主権確立** | 源内OSS公開・8社共同会社設立・LLM-jp-4公開と官民の動きが加速 |
| **ローカル・軽量LLMの進化** | BitNet a4.8（16倍メモリ削減）・Gemma 4 12B（ノートPC動作）が実用段階に |

**生成**: Claude Haiku（claude-haiku-4-5）| 2026年6月6日

</div>
</div>

</div>

---

<div class="sonnet-eval" markdown="1">

## 🧠 Claude Sonnet による比較・評価（月次・2026年6月）

*両記事を読んだ Claude Sonnet 4.6 が、情報カバレッジ・構成・特徴の観点から月次記事を評価します。*

---

### カバレッジの違い

**Ollama 記事が独自にカバーしたトピック**（Haiku には未掲載）:
- Project Glasswing 拡大の詳細（150組織、15カ国以上、10,000件以上の脆弱性発見）
- Chris Olah 氏の教皇レオ14世 AI 回勅講演（AIと宗教・哲学の交差点）
- Gemma 4 12B の技術詳細（エンコーダーフリーアーキテクチャ、Multi-Token Prediction）
- Trimming技術・Token-In Token-Out（TITO）などHugging Face技術トレンド

**Haiku 記事が独自にカバーしたトピック**（Ollama には未掲載）:
- Stainless 買収の文脈説明（MCP エコシステム強化との関連）
- BitNet a4.8 の詳細（ハイブリッド量子化、16倍メモリ削減の実用的意義）
- 日本AI基盤モデル開発会社設立の詳細（8社の具体名、政府予算5,198億円）
- NII LLM-jp-4（GPT-4o・Qwen3-8Bを超える日本語性能）
- 生成AIのビジネス活用「インフラ化」という視座
- Codex Computer Use Windows対応・Rosalind Biodefense

---

### 各観点の評価

| 観点 | Ollama (qwen3.6:35b-mlx) | Haiku (claude-haiku-4-5) |
|------|--------------------------|--------------------------|
| **情報の深さ** | ⭐⭐⭐⭐⭐ ベンチマーク数値・技術仕様が詳細 | ⭐⭐⭐⭐ 重要トピックを十分な深さでカバー |
| **構成の明快さ** | ⭐⭐⭐⭐ テーマ別に整理 | ⭐⭐⭐⭐⭐ 表形式のまとめ・出所明示で読みやすい |
| **国内AI動向** | ⭐⭐⭐ 源内のみ1件 | ⭐⭐⭐⭐⭐ 源内・8社共同会社・LLM-jp-4・ビジネス活用を網羅 |
| **ビジネス視点** | ⭐⭐⭐ 技術・研究寄り | ⭐⭐⭐⭐⭐ 産業への影響・トレンドの整理が優れる |
| **情報源の明示** | ⭐⭐⭐⭐⭐ 参考文献を脚注形式で網羅 | ⭐⭐⭐⭐ 各節に出所を明記 |
| **月次としての総合性** | ⭐⭐⭐⭐ 技術トレンドの縦断的把握 | ⭐⭐⭐⭐⭐ 国内外バランス良く月次を総括 |

---

### 総評

月次記事という性質上、週次よりも俯瞰的な視点が重要になります。

**Ollama 記事**は、Project Glasswing の150組織拡大やChris Olah氏の教皇回勅講演講演など**技術者・研究者が見落としがちな深掘りトピック**を含む点で価値があります。Hugging Face系の技術トレンド（Trimming・TITO）も独自にカバーしており、技術動向の横断的理解に適しています。

**Haiku 記事**は、日本AI基盤モデル開発会社（8社共同、政府予算5,198億円）やLLM-jp-4の詳細など**日本国内動向の深さ**で大きく上回ります。「生成AIのビジネス活用インフラ化」というトレンド分析も独自で、産業界・ビジネスパーソン向けの月次サマリーとして優れた構成です。月次まとめをトレンド表で締めくくる構成も月次記事らしい俯瞰感があります。

**月次レポートとして**は、Haiku 記事の方が「国内外バランス・ビジネス視点・読みやすい構成」の点で総合的に優れています。ただし、エンジニア・研究者向けには Ollama 記事の技術詳細も不可欠です。

</div>

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較（週次）</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama月次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-06">2026年6月</a><span class="date">2026-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-05">2026年5月</a><span class="date">2026-05</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku月次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/haiku_monthly/2026-06">2026年6月</a><span class="date">2026-06</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/haiku_monthly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>📅 月次比較</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/monthly-2026-06">2026年6月</a><span class="date">2026-06</span></li>
</ul>
</div>

</div>
</div>
