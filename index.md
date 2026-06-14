---
layout: compare
title: 生成AI週次ダイジェスト
---

<div class="compare-header">
  <h1>🔬 モデル比較（6/6〜6/13）</h1>
  <div class="compare-meta">
    <span class="badge ollama">🖥️ Ollama</span>
    <span style="font-family:monospace;font-size:0.82rem;color:#666">qwen3.6:35b-mlx（土曜 09:00 生成）</span>
    <span style="margin: 0 0.5rem;">vs</span>
    <span class="badge haiku">⚡ Claude</span>
    <span style="font-family:monospace;font-size:0.82rem;color:#666">claude-haiku-4-5（土曜 13:00 生成）</span>
  </div>
</div>

<div class="compare-wrapper">

<div class="compare-panel ollama-panel">
<div class="panel-header-bar">
  <span class="model-badge">🖥️ Ollama</span>
  <span class="model-name">qwen3.6:35b-mlx</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（6/6〜6/13）

今週は、Anthropicの最上位モデル「Claude Fable 5」の一般公開や、Apple WWDC2026での「Siri AI」発表など、主要テック企業の大きな動きが目立つ週となりました。また、GoogleのAI価格戦略の変更やOpenAIの新機能導入など、実用面での進化も加速しています。

## 1. Anthropic: Claude Fable 5 & Mythos 5 の公開、Claude Corps 発足

Anthropicは今週、複数の重要な発表を行いました。まず、6月9日に**Claude Fable 5**を一般公開しました。これは同社の最上位モデル「Mythos」クラスの能力を備えた最初のモデルで、コーディングやエージェントタスクにおいて従来のClaudeを上回る性能を発揮します。ただし、サイバーセキュリティなどの高リスク領域では安全フィルターが適用され、完全なMythos 5の能力は制限されています [Anthropic News](https://www.anthropic.com/news/claude-fable-5-mythos-5)。

また、Claude Mythos 5は「Project Glasswing」を通じて限られたサイバー防御組織に提供されており、今週その参加組織を約150機関に拡大したことが報告されています [Anthropic News](https://www.anthropic.com/news/expanding-project-glasswing)。

さらに6月11日、Anthropicは**Claude Corps**という新たなフェローシッププログラムを発表しました。これは1億5,000万ドルを投じて、米国の非営利団体や地域社会にAIスキルを持つ若手専門家を派遣するプログラムで、最初の100人のフェローが2026年10月から活動を開始します [Anthropic News](https://www.anthropic.com/news/claude-corps)。

## 2. Apple WWDC2026: Siri AI と第3世代 Foundation Models の発表

AppleはWWDC2026（6月8日〜12日）で、**Siri AI**の大幅な刷新を発表しました。iOS 27、iPadOS 27、macOS 27「Golden Gate」などで実装されるSiri AIは、GoogleのGeminiモデルを活用し、画面の文脈を理解するなどの高度な機能を提供します [Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/)。

また、第3世代**Apple Foundation Models (AFM)**の詳細も公開されました。特に注目すべきは、200億パラメータの「AFM 3 Core Advanced」モデルで、これは「Flash Architecture」と呼ばれる新アーキテクチャを採用し、iPhone Airなどのデバイス上でフラッシュメモリから直接動作可能となっています [Techno Edge](https://www.techno-edge.net/article/2026/06/09/5162.html)。

## 3. OpenAI: Codex の Banked Reset 機能導入

OpenAIは、コーディングエージェント「Codex」に対して**Banked Reset**機能を導入しました。これはPlusやProプランのユーザーがレート制限のリセットを「貯めて」後から使用できる機能で、友達を招待すると双方にリセットがプレゼントされるなどのキャンペーンも行われています [Techno Edge](https://www.techno-edge.net/article/2026/06/12/5176.html)。

## 4. Google: AI Plus の価格改定と DiffusionGemma 公開

Googleは、サブスクリプションサービス「Google AI Plus」の月額料金を7.99ドルから**4.99ドル**に値下げし、ストレージ容量を200GBから**400GB**に倍増させると発表しました [Techno Edge](https://www.techno-edge.net/article/2026/06/10/5166.html)。

また、Google DeepMindは拡散言語モデル**DiffusionGemma**を公開しました。これはGemma 4アーキテクチャに基づき、テキスト生成を並列で行うことで最大4倍高速な生成を実現するオープンモデルです [Hugging Face Blog](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)。

## 5. デジタル庁: 政府AI「源内」の新指針公表と実証拡大

デジタル庁は、6月12日に**「行政の進化と革新のための生成AIの調達・利活用に係るガイドライン（第2.0版）」**を公表しました。これは政府機関における生成AIの安全な導入ルールを定めた重要な指針です [Digital.go.jp](https://www.digital.go.jp/news/)。

また、ガバメントAI「源内」については、約18万人規模での実証が継続されており、一部モデルがオープンソースとして公開される動きもあります [Digital.go.jp](https://digital-gov.note.jp/n/n84aeba282e60)。

## 6. ローカルLLM & MCP/AIエージェント動向

ローカルLLM界隈では、Ollamaを中心にQwen3.5やLlama 4などの最新モデルが活発に利用されています。また、MCP（Model Context Protocol）を活用したAIエージェントの開発が進んでおり、AutoGenやLangGraphとの連携事例も増加しています [LinkedIn](https://www.linkedin.com/posts/heinrich-krupp-a94a205_github-doobidoomcp-memory-service-open-source-activity-7448114623100149760-pnyq)。

## 7. 1-bit LLM BitNet の最新動向

Microsoftの**BitNet**は、1-bit LLMの推論フレームワークとして注目されています。BitNet b1.58シリーズは、メモリ使用量を大幅に削減しながらも高性能な推論を実現し、CPU上での大規模モデル運用を可能にしています [GitHub](https://github.com/microsoft/BitNet)。

## 8. 日本国内の生成AI企業ニュース

日本国内では、デジタル庁による「源内」への国産LLM7モデルの展開が注目されています。また、NII（国立情報学研究所）が公開した**LLM-jp-4**シリーズも、日本語性能において海外モデルに匹敵する成果を示しています [NII News](https://www.nii.ac.jp/news/release/2026/0403.html)。

今週は特に、AnthropicのClaude Fable 5やAppleのSiri AIなど、主要テック企業の戦略的な動きが日本のAI実装にも影響を与えそうです。デジタル庁のガイドライン改定も、今後の政府調達や企業導入において重要な指針となるでしょう。

---
*出典: Anthropic, OpenAI, Google DeepMind, Apple, Digital.go.jp, Techno Edge, Hugging Face Blog, GitHub, NII など*

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（6/6〜6/13）

## 概要

6月6日から13日にかけて、生成AI領域では国内外で大きな進展が相次ぎました。Anthropicの最新モデルClaude Fable 5の公開、Appleのローカル動作Foundation Modelの発表、Google AI Plusの値下げ、そしてデジタル庁による国産AI政策の推進など、AIエコシステムの急速な進化が見られます。

---

## 📰 主要トピック

### 1. **Anthropic、Claude Fable 5を一般公開 — Mythosはサイバー防衛に限定提供**

Anthropicが最上位モデル「Claude Fable 5」を一般公開しました。同社はより高度なモデル「Mythos 5」も開発していますが、こちらはサイバー防衛領域に限定提供される方針です。Claude Fable 5はレート制限の拡張やスレスパの能力が従来比3倍と大幅に強化されており、AIエージェント開発の新標準になると期待されています。

**出典**: [Techno Edge - Anthropic Claude Fable 5公開](https://www.techno-edge.net/article/2026/06/10/5167.html)

---

### 2. **Apple、オンデバイスAI対応の第3世代Foundation Model発表 — iPhone Airでも動作**

Apple WWDC26での発表により、ローカル動作する20Bモデルが発表されました。新アーキテクチャ採用により「フラッシュに置く」方式でメモリ効率を実現し、iPhone Air での実行を可能にしています。M2 Mac は対象外となる一方、スマートフォンでのオンデバイスAI処理が実用化段階に入りました。

**出典**: [Techno Edge - Apple Foundation Model 20B](https://www.techno-edge.net/article/2026/06/09/5162.html)

---

### 3. **Google AI Plus大幅値下げ — 月額725円で400GB＆Gemini Pro追加機能**

Googleが「Google AI Plus」の月額料金を大幅に値下げしました。月額725円で400GBのストレージ拡張とGemini Proの追加機能が利用可能になり、消費者向けAIサービスの価格競争が加速しています。同時にGemini 3.5やDiffusionGemmaなど複数の新モデルも展開されています。

**出典**: [Techno Edge - Google AI Plus値下げ](https://www.techno-edge.net/article/2026/06/10/5166.html)

---

### 4. **デジタル庁、生成AI利用ガイドライン第2.0版を策定 — 全府省庁で源内実証開始**

デジタル庁が「行政の進化と革新のための生成AIの調達・利活用に係るガイドライン（第2.0版）」を策定し、公表しました。政府開発の生成AI「源内」に対して国産LLM 7モデルが選定され、全府省庁約18万人の公務員を対象にした大規模実証が実施されています。

選定された国産LLMは以下の通り：
- NTTデータ「Tsuzumi」
- NEC「Cotomi」
- ソフトバンク「Sarashina mini」
- その他4モデル

これにより、日本政府が主導する「ソブリンAI」戦略が本格化しています。

**出典**: [デジタル庁ニュース](https://www.digital.go.jp/news/), [AIフレンズ - ガバメントAI源内](https://aifriends.jp/digital-agency-government-ai-gennai-180k-deployment-2026/)

---

### 5. **OpenAI、Codexのレート制限リセット権を実装 — Banked Reset機能が利用可能に**

OpenAIがAIコーディングエージェント「Codex」に新機能「Banked Reset」を追加しました。レート制限の使用権をリセットして後から利用できる仕組みで、企業向けのコーディング自動化ツールの利便性が向上しています。友達紹介によるリセット権のプレゼントも開始されています。

**出典**: [Techno Edge - OpenAI Codex Banked Reset](https://www.techno-edge.net/article/2026/06/12/5176.html)

---

### 6. **NVIDIA Cosmos 3：物理AI推論用オムニモデルが登場**

NVIDIAが「NVIDIA Cosmos 3」を発表しました。物理AI推論と行動決定を統合した初のオープンオムニモデルで、ロボティクスや現実世界のシミュレーション領域での応用が期待されています。

**出典**: [Hugging Face Blog - Welcome NVIDIA Cosmos 3](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)

---

### 7. **Google、Gemini Omniおよび関連モデル群をリリース**

GoogleはGemini Omnimapにおいて、マルチモーダル対応を強化した新世代モデルを展開。Gemini 3.5では音声翻訳機能「Live Translate」も実装され、境界のないAI利用環境が実現されつつあります。

**出典**: [Google DeepMind Blog - Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/), [Google - Gemini Live 3.5 Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)

---

### 8. **国立情報学研究所、LLM-jp-4シリーズを公開 — 日本語特化の国産LLM**

国立情報学研究所（NII）が国産LLM「LLM-jp-4」シリーズを新たにリリースしました。日本語MT-Benchでスコア7.82を記録した32B-A3Bモデルが、日本語理解力の新標準を確立しています。

**出典**: [電波タイムス - 国産LLM新モデル](https://www.dempa-times.co.jp/administration/48600/)

---

### 9. **AI時代のスマートフォン冷却技術が進化 — COMPUTEX 2026で空冷ファン導入が加速**

COMPUTEX 2026では、オンデバイスAI処理に対応するため、スマートフォンに空冷ファンを搭載する動きが加速していることが報告されました。AI推論による発熱対策が、スマートフォン設計の新常識になりつつあります。

**出典**: [Techno Edge - AI時代のスマホ冷却最前線](https://www.techno-edge.net/article/2026/06/12/5177.html)

---

### 10. **Claude Fable 5が創作した小説「止まり木」シリーズ — AI作家と人間編集者の協働が新段階へ**

Anthropicの Claude Fable 5の実力を示すケーススタディとして、AI作家「黒戸寓五」による新シリーズ「止まり木」の構想過程が公開されました。AI とプロ編集者の全やり取りを記録した報告は、生成AIの創作支援における可能性を示唆しています。

**出典**: [Techno Edge - Claude Fable 5で産まれた小説](https://www.techno-edge.net/article/2026/06/12/5174.html)

---

## 🔬 技術トレンド

- **マルチモーダル統合**: Gemini Omniなど、複数モダリティの統合実装が標準化
- **オンデバイスAI**: Apple、Googleなど大手がローカル実行モデルに注力
- **コスト競争激化**: Google AI Plusの値下げに代表される価格競争の本格化
- **国内AI戦略の本格化**: デジタル庁による源内実証と国産LLM7モデル選定
- **ロボティクスとAI統合**: Cosmos 3など物理AI推論の進展

---

## 📊 市場動向

- **業界連携**: OpenAI、Anthropic、Googleの3大企業がG7サミットに参加予定
- **価格戦争**: トークン価格の削減競争が進行中
- **オープンソース化**: Hugging Faceを中心にオープン系モデルの拡充が継続
- **日本国内**: ガバメントAI源内の全府省庁実証により、官民の国産AI活用が加速

---

## 🔗 関連リンク

- [Google AI Plus公式](https://support.google.com/one/answer/14637637)
- [デジタル庁 生成AIガイドライン](https://www.digital.go.jp/policies/genai)
- [Anthropic Claude モデル](https://www.anthropic.com/)
- [国立情報学研 LLM-jp](https://llm-jp.nii.ac.jp/)

---

**記事作成日**: 2026年6月13日  
**情報収集期間**: 6月6日〜6月13日  
**情報源**: Techno Edge、Google DeepMind、Hugging Face、デジタル庁、国立情報学研究所ほか

</div>
</div>

</div>

<div class="sonnet-eval" markdown="1">

## 🧠 Claude Sonnet による比較・評価（2026-06-14）

*両記事を読んだ Claude Sonnet 4.6 が、情報カバレッジ・技術精度・読みやすさの観点から評価します。*

---

### カバレッジの違い

**Ollama 記事が独自にカバーしたトピック**（Haikuには未掲載）:
- Claude Corps フェローシッププログラム（1.5億ドル投資・100人フェロー派遣）
- Project Glasswing の参加組織拡大（約150機関）
- ローカルLLM界隈の動向（Qwen3.5、Llama 4、MCP/AIエージェント、AutoGen/LangGraph連携）
- Microsoft BitNet（1-bit LLM）の最新動向

**Haiku 記事が独自にカバーしたトピック**（Ollamaには未掲載）:
- NVIDIA Cosmos 3（物理AI推論用オープンオムニモデル）
- Google Gemini Omni および Live Translate 機能
- スマートフォン空冷ファン技術（COMPUTEX 2026）
- Claude Fable 5による小説「止まり木」シリーズ（AI創作事例）
- G7サミットへのOpenAI・Anthropic・Google参加予定
- 源内に選定された国産LLM7モデルの具体的な社名列挙（Tsuzumi、Cotomi、Sarashina miniなど）

---

### 各観点の評価

| 観点 | Ollama (qwen3.6:35b-mlx) | Haiku (claude-haiku-4-5) |
|------|--------------------------|--------------------------|
| **情報の深さ** | ⭐⭐⭐⭐ 各トピックに背景説明や制約条件（例：安全フィルター、高リスク領域）まで言及しており、単なる事実紹介を超えた文脈が得られる | ⭐⭐⭐ 項目数は多いが、各トピックの説明が短く、表面的な情報にとどまるものもある（例：Gemini Omni、Cosmos 3） |
| **カバレッジ** | ⭐⭐⭐ 主要8トピックをカバー。ローカルLLMやBitNetなど技術寄りの話題は拾っているが、NVIDIA・Gemini Omniなど見落としがある | ⭐⭐⭐⭐⭐ 10トピックを幅広くカバー。AI創作事例やスマホ冷却技術など周辺領域まで網羅しており、今週の全体像をつかみやすい |
| **国内AI動向** | ⭐⭐⭐ デジタル庁ガイドラインとLLM-jp-4に触れているが、源内の国産LLM選定モデル名など具体情報が薄い | ⭐⭐⭐⭐⭐ 選定国産LLM7モデルの社名を列挙し、「ソブリンAI」という戦略的文脈も提示。官民動向の解像度が高い |
| **読みやすさ** | ⭐⭐⭐⭐ 流れるような文章で段落構成が自然。ただし絵文字や視覚的区切りがなく、長文で疲労感が出やすい | ⭐⭐⭐⭐⭐ 絵文字アイコン・太字・トレンドまとめセクションなど視覚的メリハリが豊富で、斜め読みにも対応しやすい |
| **情報源の明示** | ⭐⭐⭐ 出典URLを文中にインライン記法で埋め込んでいるが、記事末尾のリストが簡略的で検証しにくい箇所もある | ⭐⭐⭐⭐ 各トピック末尾に「出典」ブロックを統一フォーマットで配置しており、追跡しやすい。末尾の関連リンクも整理されている |
| **ビジネス視点** | ⭐⭐⭐ Claude Corpsの社会実装投資など一部に戦略的示唆があるが、市場・競争構造の分析は限定的 | ⭐⭐⭐⭐ 「価格戦争」「業界連携（G7）」「オープンソース化」など市場動向セクションを独立設置し、業界構造の変化を俯瞰できる |

---

### 総評

今週は「既存モデルの高度化・普及」と「国産AI政策の具体化」が同時進行した週であり、両記事ともその核心を押さえている。Ollama記事は各トピックの背景・制約・技術的意義を丁寧に掘り下げており、特にAnthropicの多角的な動きや開発者向け情報（MCP、BitNet）に強みがある。一方、Haiku記事は項目数の多さと構造化された読みやすさに優れ、国産LLM選定の具体名やビジネス・市場視点のまとめなど、意思決定層にも刺さる情報整理が光る。深みを求めるならOllama記事、全体像の速習にはHaiku記事が向いており、両記事を合わせて読むことで技術的詳細から市場トレンド・国内政策まで、今週のAI動向を立体的に把握することができる。

</div>

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0613">6/6〜6/13</a><span class="date">2026-06-13</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/monthly-2026-06">2026年6月</a><span class="date">2026-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0613">6/6〜6/13</a><span class="date">2026-06-13</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0518">5/18〜5/24</a><span class="date">2026-05-18</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-0613">6/6〜6/13</a><span class="date">2026-06-13</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/haiku_weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>📅 月次まとめ</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-06">2026年6月</a><span class="date">2026-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-06">2026年6月</a><span class="date">2026-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-05">2026年5月</a><span class="date">2026-05</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-04">2026年4月</a><span class="date">2026-04</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

</div>
</div>
