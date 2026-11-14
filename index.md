---
layout: compare
title: 生成AI週次ダイジェスト
---

<div class="compare-header">
  <h1>🔬 モデル比較（11/7〜11/14）</h1>
  <div class="compare-meta">
    <span class="badge ollama">🖥️ qwen3.6</span> <span style="font-family:monospace;font-size:0.82rem;color:#666">qwen3.6:35b-mlx（土曜 09:00 生成）</span>
    <span style="margin: 0 0.5rem;">vs</span>
    <span class="badge haiku">⚡ Claude</span> <span style="font-family:monospace;font-size:0.82rem;color:#666">claude-haiku-4-5（土曜 13:00 生成）</span>
    <span class="badge ornith">🦉 ornith</span> <span style="font-family:monospace;font-size:0.82rem;color:#666">ornith-1.5:35b（土曜 10:00 生成）</span>
    <span class="badge nemotron">🌩️ nemotron</span> <span style="font-family:monospace;font-size:0.82rem;color:#666">nemotron-3.5-lightning:30b-mlx（土曜 11:00 生成）</span>
    <span class="badge qwen38">💠 qwen3.8</span> <span style="font-family:monospace;font-size:0.82rem;color:#666">qwen3.8:27b-mlx（土曜 12:00 生成）</span>
  </div>
</div>

<div class="compare-wrapper">

<div class="compare-panel ollama-panel">
<div class="panel-header-bar">
  <span class="model-badge">🖥️ qwen3.6</span>
  <span class="model-name">qwen3.6:35b-mlx</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（11/7〜11/14）

今週はGoogleのGemini 4シリーズ新モデル発表、NVIDIA創業者CEO辞任という業界最大ニュース、Microsoft 365大規模障害、Cohereの日本国内推論基盤提供など、見どころが多数あった週となりました。

---

## 1. Google: Gemini 4 Carbon・Hydrogen 連続リリース、Gemini Robotics 2.5公開

Google DeepMindは今週、Gemini 4シリーズの新モデルを相次いで発表しました。

- **[Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)** — 11月12日公開。「Flash」ブランドを廃止した初のモデルで、1Mトークンコンテキストウィンドウを持つ推論モデル。コーディングベンチマーク57%達成。
- **[Gemini 4 Carbon is now available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)** — サイバー防御と長時間自律作業向け最上位モデル。AI Ultra加入者へ提供開始。
- **[Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)** — ロボティクス分野でも新モデルを発表、実世界での物理知能を加速。

[Google DeepMind Blog](https://deepmind.google/blog/) によると、AlphaGenome 2（DNA解読）、AlphaProof Code（複雑なソフトウェア検証）、Gemini Omni 1.2 Flash（高速・低コスト）など、AIモデルのラインナップが大幅に拡大しています。

> Gemini 4 Hydrogen Benchmarks, Cost and Capabilities（未確認の出典のためリンク省略） (Vals AI)
> Google's Gemini 4 Hydrogen Is INSANE — AI Agents Just...（未確認の出典のためリンク省略） (YouTube)

---

## 2. NVIDIA: ジェンスン・フアンCEOが辞任、創業者以来の体制に幕

11月12日、NVIDIAは創業者ジェンスン・フアン氏のCEO辞任を発表しました。

- **[NVIDIA Announces CEO Transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)** — CFOのColette Kress氏が暫定CEOに就任。
- **Jensen Huang resigns as Nvidia CEO after alleged extramarital affairs（未確認の出典のためリンク省略）** (The Guardian) — 不倫報道が辞任の背景に。
- **[Huang agrees to appear before Congress](https://www.bbc.com/news/live/c6zjry11v8w1t)** (BBC News) — 米議会証言にも応じる意向。

[Techno Edge](https://www.techno-edge.net/article/2026/11/13/5711.html) の報道によると、「スパイの標的」や「部下と不倫」の報道が相次ぎ、急遽辞任が決定しました。NVIDIA株は下落し、AI業界全体にも影響が及んでいます。

---

## 3. Microsoft 365大規模障害: Outlook・Teams・Copilotが数日間利用不能

11月12日から13日にかけて、Microsoft 365の世界的な障害が発生しました。

- **Microsoft 365 OUTAGE: Outlook DOWN for Thousands!（未確認の出典のためリンク省略）** (YouTube)
- **Microsoft scrambles to fix global outage affecting Outlook, Teams, Word, Excel（未確認の出典のためリンク省略）** (The Guardian)
- **Microsoft 365 Outage Nov 2026: Impact on Business & AI（未確認の出典のためリンク省略）** (DopeStudio)

障害はOutlook、Exchange Online、Teams、Copilotなど広範囲に影響。ChatGPTのMicrosoft 365コネクタも巻き込まれました。復旧したサーバーが再び止まる事態で長期化し、政府共通基盤「GSS」にも波及しました。

[Techno Edge](https://www.techno-edge.net/article/2026/11/13/5714.html) および [Microsoft 365障害、政府共通基盤「GSS」も巻き込む](https://www.techno-edge.net/article/2026/11/13/5723.html) によると、デジタル庁も対応に追われました。

---

## 4. Cohere: Model Vaultを日本で提供開始、国内完結の推論基盤

Cohereは今週、日本法人設立と合わせて推論基盤「Model Vault」を日本国内で提供開始すると発表しました。

- **[生成AIへの質問も回答も国内で、Cohereが推論基盤「Model Vault」を日本で提供へ](https://www.techno-edge.net/article/2026/11/13/5720.html)** (Techno Edge)
- **[Leading Open AI Models Now Available in Model Vault](https://cohere.com/blog/open-source-model-vault)** (Cohere Blog, Nov 3)

Model Vaultは、AIモデルを日本国内の計算クラスターのみで動かす推論基盤。入力プロンプトと出力応答を国内に留めるため、データ主権（sovereign inference）が保証されます。ゼロデータ保持（zero data retention）デフォルト対応。富士通とのTakane開発も推進しています。

---

## 5. Anthropic: Claude Meetings・Mythos/Fable新モデル、Agent Skills寄付

Anthropicは今週、複数の新機能・新モデルを発表しました。

- **[Anthropic launches Claude Meetings to turn workplace discussions into plans and tasks](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/)** (TechCrunch) — ビデオ会議中にClaudeが参加し、タスクを自動生成。
- **[Anthropic releases new Mythos and Fable models amid RSI concerns](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/)** (TechCrunch) — コーディング・推論・ビジョン性能を改善した新モデル。
- **[Donating Agent Skills To The Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)** (Anthropic News) — エージェントスキルをオープンソース基盤に寄付。

[Anthropic Newsroom](https://www.anthropic.com/news/) によると、AI for Science分野の拡張やGSAとのパートナーシップ拡大も進んでいます。

---

## 6. AWS: Kiro Androidアプリ公開、QuickのSmartApprovals導入

AWSは今週、AIコーディングツールKiroのモバイルアプリと、エージェント承認機能のアップデートを発表しました。

- **[AWSのKiroがAndroidアプリ公開、クラウドで動くAIコーディングの作業をスマホで引き継ぐ](https://www.techno-edge.net/article/2026/11/13/5718.html)** (Techno Edge) — クラウド上のAIコーディング作業をスマートフォンで引き継ぎ可能。Grok 4.7も選択可能。
- **[AWSの動きを手元のPCで再現、コーディングAIがデプロイを待たずに試せる公式エミュレーター](https://www.techno-edge.net/article/2026/11/13/5719.html)** (Techno Edge) — PC上でAWS環境をローカル再現する無料エミュレーター。
- **[AIエージェントからの「確認疲れ」を減らす仕組み、別のAIが承認か差し戻しかを決定](https://www.techno-edge.net/article/2026/11/13/5717.html)** (Techno Edge) — AWS QuickのSmartApprovalsは別AIが事前判定し危険操作のみ人間承認。

---

## 7. ローカルLLM: Hugging Face Blogで複数の新モデル・技術を紹介

Hugging Face Blogは今週、ローカルLLM関連の複数の記事を公開しました。

- **[Nemotron-Personas-Finance-Japan: 日本の人口分布と金融コンテキストを捉える合成ペルソナデータセット](https://huggingface.co/blog/nvidia/nemotron-personas-finance-japan-ja)** — NVIDIAが日本の金融コンテキスト向け合成データを公開。
- **[Uncensor any LLM with abliteration](https://huggingface.co/blog/mlabonne/abliteration)** — LLMのフィルターを解除するabliteration技術を紹介。
- **[Bring Your Own Expert! Extending MoE Models with New Domain Expertise](https://huggingface.co/blog/tngtech/bring-your-own-expert-extending-moe-models-with-ne)** — MoEモデルに新ドメイン専門知識を追加する方法。

[1-bit LLM BitNet](https://github.com/microsoft/BitNet) 関連では、Microsoftが公式推論フレームワークを公開。CPU上で100Bパラメータモデルを6倍高速化、エネルギー82%削減を実現しています。

---

## 8. デジタル庁: Microsoft障害対応・ガバメントAI「源内」推進

デジタル庁は今週、Microsoft 365障害への対応とガバメントAI「源内」の推進に関する情報を更新しました。

- **[マイクロソフト社の障害を受け、本日（2026年11月13日）技術提案書等提出期限の調達案件の対応について掲載](https://www.digital.go.jp/news/)** — 調達案件の対応方針を公開。
- **[マイクロソフト社の障害によりメール不着等となる事象について](https://www.digital.go.jp/news/)** — メール不着への対処情報を提供。

[ガバメントAI「源内」](https://www.digital.go.jp/policies/genai) は、政府職員が安全にAIを活用できる基盤として各府省庁に展開中。国産LLM（tsuzumi 2・Sarashina・PLaMo・Takane・cotomi・CC Gov-LLM・ELYZA）を採用し、データ主権を確保しています。

---

## 9. その他注目ニュース

- **[元Anker CMOが挑む「AIのための記憶補完デバイス」、11グラムのAIウェアラブル「Memoket Gem」](https://www.techno-edge.net/article/2026/11/13/5713.html)** (Techno Edge) — 会話を録音・要約し、長期記憶エンジンで文脈を結ぶ11gのウェアラブルデバイス。
- **[NVIDIAフアンCEOが辞任、創業以来の体制に幕](https://www.techno-edge.net/article/2026/11/13/5711.html)** (Techno Edge) — 詳細は前述の通り。
- **OpenAI, Anthropic and Google to create an AI standards body（未確認の出典のためリンク省略）** (TechXplore) — 3社がAI安全基準機関を設立する方向で調整中。

---

## まとめ

今週はGoogleのGemini 4シリーズ連続リリース、NVIDIA創業者CEO辞任、Microsoft 365大規模障害という業界最大級ニュースが続出しました。Cohereの日本国内推論基盤提供は、データ主権への関心の高さを示す動きです。AWSのエージェント承認機能アップデートも、実務導入が進むAIエージェントの実態を反映しています。

来週もGemini 4 Hydrogenのパフォーマンス詳細や、NVIDIAの後継体制動向に注目です。

---

*この週次ダイジェストは、[Techno Edge](https://www.techno-edge.net/)、[AINOW](https://ainow.ai/)、[Hugging Face Blog](https://huggingface.co/blog/)、[Google DeepMind Blog](https://deepmind.google/blog/)、[Anthropic News](https://www.anthropic.com/news/)、[OpenAI News](https://openai.com/news/)、[デジタル庁ニュース](https://www.digital.go.jp/news/)などの情報を基に生成しています。*

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（11/7〜11/14）

## 国産AIプラットフォーム「源内」の大規模展開が進行

デジタル庁が開発した国産生成AI基盤「源内」の大規模実証事業が本格化し、政府職員約18万人を対象に導入が進むことになりました。源内は内製化されたシステムで、一定の機密性がある情報も扱え、文章作成・翻訳・国会答弁の草案作成などに対応。2027年度からの本格利用を目指しており、デジタル庁が国産7つの大規模言語モデルの試用を進めています。この取り組みは日本のAI自律性確保と民間投資喚起が狙いです。

参照: [デジタル庁 — 生成AI関連政策](https://www.digital.go.jp/news/)

## 国産LLM新モデルの相次ぐリリース

**Preferred Networks「PLaMo 3.0 Fin」**: 11月9日、PFNが金融特化型のLLM「PLaMo 3.0 Fin」をオープンウェイトで公開。非商用利用は無償、売上10億円未満の企業は商用利用も無償で利用可能。金融分野の高度な推論と日本語対応が特徴です。

**ソフトバンク「Sarashina mini」**: 11月5日発表、11月28日から提供開始。700億パラメータ級の軽量モデルで、日本語特化・高速処理・日本特有の文化・法制度への対応が強み。

## Anthropic、IPOに向けた大規模調達とモデル発表

Anthropicが大規模な資金調達とIPO準備を進めており、Googleから200億ドル以上の投資を獲得。同時に新モデルClause Fable 5.2・Mythos 5.2を公開し、Opus 5.5をほぼ全評価で上回るパフォーマンスを発揮。東京にアジア太平洋初のオフィスを開設し、日本市場への事業展開も強化しています。

## OpenAI、企業向けの大型アップデートと新サービス

OpenAIが2026年第3四半期に約10億ドルの収益を上げ、同期比50%増を達成。新たにサイバーセキュリティ特化型の「GPT-6 Cyber」をDaybreak Red（防衛機関向け）経由でリリース。一方、Advanced/Standard Voice は12月11日で廃止となり、全ユーザーがLive Voiceへ移行予定。企業向けインフラとしてControl Room（研究推論ジョブ追跡・制御サービス）もリリースされました。

## Google、数学証明生成で600万行のコード生成

Googleが生成AIを用いて600万行以上の数学的証明コードを生成し、プライベートメッセージの暗号化を検証。Gemini Omni 1.2 Flashも話題で、マルチモーダル・画像処理能力で注目を集めています。

参照: [OpenAI News](https://openai.com/news/)

## ローカルLLM「Ollama」v0.40.16がリリース、新モデル「Ripple Preview」に対応

11月9日、Ollama v0.40.16がGitHubでリリース。Recursive Intelligence製の65Bパラメータ denseモデル「Ripple Preview」を追加し、エージェント型コーディングに最適化。Qwen3.8 Flash NextではApple Silicon向けのメモリ効率化により、MacBook Pro等での利用性が大幅向上し、メモリ使用量が約27GB削減されました。

参照: AIpicks.jp — Ollama新モデル情報（未確認の出典のためリンク省略）

## AIエージェント・MCP基盤の標準化が加速

MicrosoftはAutoGenをAG2アクターモデルに再構築し、Microsoft Agent Framework 1.0（2026年4月GA）がSemantic Kernelと統合。MCPはLinux Foundation傘下のAAIFで正式化され、OpenAI・Google・Anthropicなどが対応を進めています。2026年7月の仕様改訂でステートレス化し、HTTPインフラでの水平スケーリングが容易に。SDKダウンロードは月5億回超、TypeScript/Python累計10億回超えの実績を達成。

参照: [atmarkit「MCP・Microsoft Agent Framework」](https://atmarkit.itmedia.co.jp/ait/)

## 1-bit LLM「BitNet b1.58 2B4T」の実用化が進展

MicrosoftがBitNet b1.58 2B4Tを公開。20億パラメータ・4兆トークンで学習した初のオープンソース1-bit LLMで、メモリ・エネルギー・レイテンシが大幅削減。MITライセンスでHugging Faceで公開され、言語理解・数学・コーディング・会話で従来型フルプレシジョンLLMと同等パフォーマンスを実現。

参照: [arXiv「BitNet b1.58 2B4T Technical Report」](https://arxiv.org/html/2504.12285v1)

## 日本企業の生成AI実装で定量成果が本格化

NEC（部品調達交渉を約80秒で自動化）、パナソニック（18.6万時間削減）、イオンリテール（工数90%削減）など大手企業での活用実績が報告。制度・法制度への対応やビジネス実装が進むなか、AI導入による業務効率化の効果が数字で示されるようになってきました。

---

**記事生成**: Claude Haiku 4.5 | **出力日**: 2026-11-14

</div>
</div>

</div>

<div class="compare-extra-header">
  <h2>🧩 追加ローカルモデル（比較用）</h2>
  <p>メイン比較と同じ週・同じ収集条件で、別のローカルLLMが生成した週次まとめです。</p>
</div>

<div class="compare-extra">

<div class="compare-panel ornith-panel">
<div class="panel-header-bar">
  <span class="model-badge">🦉 ornith</span>
  <span class="model-name">ornith-1.5:35b</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（11/7〜11/14）

今週は米Googleが最 frontier モデル「Gemini 4 Carbon」を公開し、Anthropicが職場向け新機能を続々投入。一方でNVIDIAのジェンスン・フアンCEOの辞任、Microsoft 365の大規模障害など、業界の地盤を揺さぶる出来事も相次いだ。日本ではCohereが国内完結の推論基盤を提供開始するなど、データローカライゼーションの動きも活発だった。

## Gemini 4 Carbon が提供開始 — コーディング・エージェント特化の最上位モデル

Googleは11月10日、最上位AIモデル「Gemini 4 Carbon」の提供を開始した。サイバー防御や長時間の自律作業（エージェント）向けに設計され、API は Google AI Studio と Gemini for business プラットフォーム経由で利用可能だ。提供開始に伴い、11月30日までプロモーション価格（入力100万トークンあたり2ドル、出力100万トークンあたり10ドル）が適用される。

Gemini 4 Carbon は、コーディング・エージェント・複雑な推論作業に最適化されており、Google の最高峰モデルとしての位置づけを持つ。

- [Gemini 4 Carbon is now available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- [Gemini 4 Carbon: Our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

## Gemini 4 Hydrogen が発表 — 「Flash」ブランドを終了し日常利用モデルとして登場

Googleは11月12日、新モデル「Gemini 4 Hydrogen」を発表した。既存の「Gemini 3.8 Flash」の後継にあたり、本シリーズで初めて「Flash」の名称が外された。高速・低コストで信頼性の高いエージェントワークフローと日常タスク向けに構築され、ネイティブの100万トークンコンテキスト窗口をサポート。速度と知能の両面で「大きな飛躍」があるとされている。

- [Introducing Gemini 4 Hydrogen for Agentic Workflows](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
- [Google announces Gemini 4 Hydrogen with 'significant leaps'](https://9to5google.com/2026/11/12/gemini-4-hydrogen-launch/)

## Anthropic、職場向け新機能「Claude Meetings」などを発表 — IPO 前の攻勢

Anthropicは11月10日、職場向けの新機能を複数発表した。中でも注目なのが「Claude Meetings」だ。ビデオ通話にClaudeを組み込み、参加者が話しながらタスクを進められる。初期設定としてトラッカーや予算表の準備をClaudeが行い、参加者は同じスプレッドシートを継続して編集できる。デフォルトではClaudeは書面回答を採用し、許可を得た接続ツールを利用できる。当初は Google Meet 経由で利用可能。

あわせて「Claude Whiteboards」「Claude Sheets」「Claude Data」も発表され、Google や Microsoft のオフィス製品に食い込む攻勢を示した。

- [Introducing Claude Meetings, now in beta](https://claude.com/resources/articles/claude-meetings)
- [Anthropic launches Claude Meetings to turn workplace discussions into plans and tasks](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/)

## Anthropic、Agent Skills を Agentic AI Foundation に寄付 — エージェント標準の共通基盤化

Anthropicは、エージェントにタスクを習得させるオープンスタンダード「Agent Skills」を、Linux Foundation 傘下の Agentic AI Foundation（AAIF）に寄付したと発表した。AAIF は MCP プロトコルをホストする組織で、今や10件のプロジェクトが収められる。OpenAI も Responses API を由来とする「Open Responses」を寄付しており、エージェント生態系の標準化が進んでいる。

- [Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
- Anthropic donates Agent Skills standard to Agentic AI Foundation（未確認の出典のためリンク省略）

## Salesforce、オープンウェイトの音声文字起こしモデル「SOV-Transcribe-1」を Hugging Face に公開

Salesforce のソヴレインテリジェンス部門は11月12日、オープンウェイトの音声→テキストモデル「SOV-Transcribe-1」を Hugging Face に公開した。Apache 2.0 ライセンスで配布され、非ストリーミングの音声文字起こしでオープンウェイトモデルトップ（Artificial Analysis で #1、総合 #7）、VoiceCodeBench で 23 系統 among #2 を記録。Word Error Rate は 2.28% と、オープンモデルとして最高の精度を誇る。

- [Introducing Salesforce SOV-Transcribe-1: #1 Open-Weight Model Built for Real-World Speech](https://huggingface.co/blog/salesforce-sovereign-intelligence/sov-transcribe-1)

## NVIDIA のジェンスン・フアンCEOが辞任 — 創業以来の体制に幕

NVIDIAは11月12日（米国時間）、創業者のジェンスン・フアン氏が社長兼CEO・取締役を即日辞任すると発表した。後任は暫定的にコレット・レスCFOが就く。辞任の背景には、中国スパイとの不倫を疑われる報道や、部下との不倫報道が相次いだことにある。フアン氏は辞任後、米議会への出頭に同意している。NVIDIA は創業以来、フアン氏を軸に成長してきた。

- [NVIDIA Announces CEO Transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)
- Jensen Huang resigns as Nvidia CEO after alleged...（未確認の出典のためリンク省略）

## Microsoft 365 で大規模障害 — Outlook・Teams・Copilot が数日間利用不可

11月12〜13日、Microsoft 365 の大規模障害が発生し、Outlook・Teams・Microsoft 365 Copilot が世界中で利用不能になった。Exchange Online との連携部分に問題が発生源とみられ、修正のための設定変更が「期待どおりに機能しない」事態も生じた。日本では政府共通基盤「GSS」も巻き込まれ、デジタル相が「なんで使えないんだろうと」不満を表明。代替手段で業務継続を図った。

- [Microsoft 365で大規模障害、Outlook・Teams・Copilotにつながらず](https://www.techno-edge.net/article/2026/11/13/5714.html)
- [Microsoft 365障害、政府共通基盤「GSS」も巻き込む](https://www.techno-edge.net/article/2026/11/13/5723.html)

## 【国内】Cohere、推論基盤「Model Vault」を日本で提供開始 — 質問も回答も国内完結

Cohere は、日本法人設立とあわせて国内完結の推論基盤「Model Vault」を日本で提供開始すると発表した。Model Vault は AI モデルを特定の地域内だけで稼働させる Cohere 独自の推論基盤で、日本国内の計算クラスターを利用することで、プロンプトと応答を国内にとどめたまま推論を実行できる。また、Takane（タカネ）の開発では富士通と推進。生成AIのデータローカライゼーション需要に応える。

- [生成AIへの質問も回答も国内で、Cohereが推論基盤「Model Vault」を日本で提供へ](https://www.techno-edge.net/article/2026/11/13/5720.html)

## 【国内】デジタル庁、Microsoft 障害を受け調達対応について掲載 — 体制整備を促進

デジタル庁は、Microsoft 社の障害を受け、11月13日に技術提案書等提出期限の調達案件への対応について掲載した。あわせて、マイクロソフト社の障害によりメール不着等となる事象についても公表。JP PINT（民間事業者の取組・政府調達編）も更新している。国内の行政・企業のAI導入基盤の堅牢性向上が求められる中、万が一に備えた対応を示した形だ。

- [デジタル庁ニュース](https://www.digital.go.jp/news/)

## ローカルLLM — Hugging Face で新モデル・新ライブラリが続々公開

Hugging Face では今週も多数の新公開が行われた。特に注目なのが、NVIDIA が公開した「NVIDIA Cosmos 3」オープンモデル。インタラクティブな世界シミュレーション向けで、ロボット学習・動画生成の基盤として期待される。また、Salesforce の SOV-Transcribe-1（上記参照）や、AllenAI のロボット学習用制御世界「ToyBlocks」なども公開された。

加えて、機械学習ライブラリ llama.cpp と ggml が v1.0.0 をリリース。Hugging Face 公式ブログで発表され、開発者の責任を強調する重要なマイルストーンとなった。

- [New NVIDIA Cosmos 3 Open Models for Interactive World Simulation](https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation)
- [A Blog post by ggml-org on Hugging Face](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

## AIエージェント — MCP と AutoGen の連携が拡大

Microsoft の AutoGen では、MCP 対応ツールを標準入出力で通信するアダプター `autogen_ext.tools.mcp` が提供されている。コマンドラインツールやローカルサービスをラップし、AutoGen エージェントに統合できる。エージェント生態系では、Anthropic が寄付した Agent Skills と MCP が AAIF 下で統合され、標準化が進んでいる。

- autogen_ext.tools.mcp — AutoGen（未確認の出典のためリンク省略）

## 1-bit LLM — BitNet の進化が注目

1-bit LLM の分野では、Microsoft Research が手がける BitNet の進化が続いている。BitNet b1.58 は、重みを1.58bitで学習する新アプローチで、1bitでも高性能を達成。CPU 推論に特化した bitnet.cpp なども登場し、極限軽量化の最前線として注目されている。

- [BitNetとは？ 1.58bitでLLMを軽く速くする1-bit](https://abeam.tech/media/ai-papers/2026-06-07-bitnet-1bit-pretraining/)

---

*本ダイジェストは ornith-1.5:35b（比較用サブモデル）が生成しました。*

</div>
</div>

<div class="compare-panel nemotron-panel">
<div class="panel-header-bar">
  <span class="model-badge">🌩️ nemotron</span>
  <span class="model-name">nemotron-3.5-lightning:30b-mlx</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（11/7〜11/14）

## 1. OpenAIが推論モデル「o3」と「o4-mini」を発表
OpenAIは推論能力を大幅に強化した新世代モデル「o3」と、軽量版の「o4-mini」を発表しました。o3は複雑な数学的・プログラミングタスクでGPT-4oを上回る性能を示し、o4-miniは低コストで高速な推論を実現します。両モデルはChatGPT Plus/Proユーザー向けに順次展開されています。

- OpenAI, Anthropic and Google to create an AI standards body（未確認の出典のためリンク省略）
- [OpenAI、推論能力を大幅に強化した新AIモデル「o3」を発表](https://wired.jp/article/openai-o3-reasoning-model-google-gemini/)

## 2. Google、最上位AIモデル「Gemini 4 Carbon」提供開始
Googleは最高峰AIモデル「Gemini 4 Carbon」の提供を開始しました。サイバー防御と長時間自律作業向けに最適化され、AI Ultra加入者向けに提供されています。従来のGemini 3.5から推論効率が大幅に向上し、複雑なタスク処理能力が強化されています。

- [Google、最上位AIモデル「Gemini 4 Carbon」提供開始](https://www.techno-edge.net/article/2026/11/11/5703.html)

## 3. NVIDIAの創業者ジェンスン・フアンがCEO職を辞任
NVIDIAの創業者で長年CEOを務めてきたジェンスン・フアン氏が、2026年11月12日(米国時間)に社長兼CEOと取締役を即日辞任することが発表されました。同社は「スパイの標的」や「部下と不倫」といった報道が相続したため、後任として同社幹部が昇格すると表明しています。AIハードウェア分野のリーダーシップ交代に注目が集まっています。

- [NVIDIAフアンCEOが辞任、創業以来の体制に幕](https://www.techno-edge.net/article/2026/11/13/5711.html)

## 4. Cohereが日本で推論基盤「Model Vault」を提供開始
Cohereは日本法人設立と国内完結の推論基盤Model Vaultを拡大し、Takane開発を富士通と推進すると発表しました。日本語処理に特化したこのサービスは、国内データの管理下でLLMを利用したい企業にとって大きな選択肢となります。1-bit LLMのBitNetと組み合わせた軽量推論にも対応しています。

- [生成AIへの質問も回答も国内で、Cohereが推論基盤「Model Vault」を日本で提供へ](https://www.techno-edge.net/article/2026/11/13/5720.html)

## 5. デジタル庁が国産LLM7モデルを政府共通プラットフォーム「源内」に選定
デジタル庁は政府共通AIプラットフォーム「源内」で使用する国産LLMとして7モデルの選定を正式に公表しました。PLaMo 3.1 Prime、Sarashina、tsuzumi 2、cotomi、CC Gov-LLM、ELYZA、Takaneの7モデルが選定され、政府主導での国産AI活用が本格化しています。特にSarashinaとPLaMo 3.1 Primeは無償β版が提供されています。

- 【2026年版】国産LLM7選｜デジタル庁「源内」が選んだAIモデルを完全比較（未確認の出典のためリンク省略）

## 6. BitNet b1.58の1-bit LLM推論が注目される
Microsoft Researchによる1-bit LLM「BitNet b1.58」が注目を集めています。1.58ビットという極限の圧縮率ながら、FP16モデルと同等以上の性能を発揮し、CPU上での推論が可能です。Ollama上でも動作が確認されており、ローカル環境での軽量AI利用の新しい選択肢となっています。

- [1-bit LLMとBonsai：極限軽量化の最前線を論文ベースで整理する](https://zenn.dev/amasashi/articles/e75ffebff53bb7)

---
*週次ダイジェストは2026-11-14現在の情報に基づいています。*

</div>
</div>

<div class="compare-panel qwen38-panel">
<div class="panel-header-bar">
  <span class="model-badge">💠 qwen3.8</span>
  <span class="model-name">qwen3.8:27b-mlx</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（11/7〜11/14）

> 生成モデル: qwen3.8:27b-mlx（Ollama 経由・ローカル実行）／ 集計日: 2026-11-14
> 本記事は複数ローカルLLMによる週次要約比較企画の、qwen3.8 担当分です。

今週（11/7〜11/14）は、Google が最上位モデル「Gemini 4 Carbon」の一般提供を開始したほか、Microsoft 365 の大規模障害が政府の共通基盤 GSS まで波及する出来事、Cohere の日本法人設立と国内完結推論基盤「Model Vault」の拡大、デジタル庁の生成AI活用に関する対応など、国内外で幅広い動きがありました。以下、主要トピックを整理します。

---

## 1. Google、最上位AIモデル「Gemini 4 Carbon」を一般提供開始

Google は 11 月 10 日、同社 AI モデルの中で最も高性能と位置づける「Gemini 4 Carbon」の一般提供を開始しました。サイバーセキュリティと、長時間にわたって自律的に作業を進めるエージェント型ワークフローに強みを持つとされています。先行提供は 2 週間前からサイバー防御担当者を対象とする「Fairwind Program」を通じて行われており、今回は有料の開発者・企業、個人向け最上位プラン「Google AI Ultra」の加入者へ対象が広がりました。

- 性能面では、Argon の上位にあたり、複雑で多段階のコーディング・デバッグや答えの定まらない科学研究を担う位置づけ。100 万トークンあたりの API 料金は当初 Argon と同額（入力 2 ドル・出力 10 ドル）で、12 月 1 日以降は 2 倍（入力 4 ドル・出力 20 ドル）に。
- 開発環境「Google Antigravity」には、1 つのプロンプトから協調して動く複数エージェントのチームを立ち上げる新機能「/swarm」がプレビュー追加。
- 安全性は Argon と比較し、適応型レッドチーミングでの試行あたり突破率 0.8%（Argon 3.1%）、誠実性ベンチマークの合格率 92%（Argon 70%）など、悪用耐性と誠実性の両面で改善を報告。

出典:
- [Gemini 4 Carbon is now available（Gemini 4 Carbon の提供開始）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- [Introducing Gemini 4 Carbon（Gemini 4 Carbon の紹介）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- [Google、最上位AIモデル「Gemini 4 Carbon」提供開始（Techno Edge）](https://www.techno-edge.net/article/2026/11/11/5703.html)

---

## 2. Microsoft 365 の大規模障害が政府共通基盤 GSS まで波及

11 月 13 日、Microsoft 365 で Outlook・Teams・Copilot につながらない大規模障害が発生し、復旧したサーバーが再び停止する事態で長期化しました。この障害は政府の共通基盤「GSS（政府共通システム）」にも波及し、メール不着などの事象が確認されました。デジタル相は「なんで使えないんだろうと」と述べ、政府は代替手段で業務継続を図っています。

- デジタル庁は 11 月 13 日、マイクロソフト社の障害を受け、技術提案書等の提出期限が迫る調達案件の対応について掲載。
- 障害によりメール不着となる事象について、庁内で周知・対応を呼びかけ。

出典:
- [Microsoft 365で大規模障害、Outlook・Teams・Copilotにつながらず（Techno Edge）](https://www.techno-edge.net/article/2026/11/13/5714.html)
- [Microsoft 365障害、政府共通基盤「GSS」も巻き込む（Techno Edge）](https://www.techno-edge.net/article/2026/11/13/5723.html)
- [デジタル庁 新着・更新（マイクロソフト社障害への対応）](https://www.digital.go.jp/news/)

---

## 3. Cohere、日本法人設立と国内完結推論基盤「Model Vault」の拡大

企業・政府機関向けの生成AIを手がけるカナダの Cohere は、日本法人の設立計画を明らかにしました。あわせて、AI の推論処理を日本国内だけで完結させる「Model Vault」の国内提供を広げます。機密データを扱う企業や官公庁が、データを国外に出さずに生成AIを使えるようにするのが狙いです。

- Model Vault は AI モデルを特定の地域の中だけで動かす Cohere 独自の推論基盤。パブリッククラウド、プライベートクラウド、オンプレミス、エアギャップ環境まで導入形態を選べます。
- 日本向けには富士通と組んで日本市場に合わせた LLM「Takane」の開発・導入を支援。Takane はデジタル庁の生成AI利用環境「GENAI」で評価対象に選ばれた国産 LLM の一つ。
- 最大 70 億カナダドル（約 7,900 億円）のシリーズ E 資金調達を進め、企業価値は 357 億カナダドル（約 3.99 兆円）。セキュリティ企業 AISLE を買収し「Cohere Cyber」も設立。

出典:
- [生成AIへの質問も回答も国内で、Cohereが推論基盤「Model Vault」を日本で提供へ（Techno Edge）](https://www.techno-edge.net/article/2026/11/13/5720.html)

---

## 4. 国産 LLM の動向：PLaMo・Sarashina・LLM-jp-4 など日本語性能の競争

国産 LLM 分野では、日本語性能を軸にした競争が継続しています。

- **PFN「PLaMo 3.0 Prime」**: フルスクラッチ開発の国産 LLM フラッグシップ。Reasoning / Non-reasoning の 2 モデル構成で、標準プランは入力 60 円・出力 250 円（1M トークン）と、同価格帯の Claude Haiku 4.5・GPT-5.4 Mini との比較が話題に。
- **SB Intuitions「Sarashina3」**: 国産 LLM の 5 モデル構成と性能・料金が整理され、NTT の「tsuzumi 2」との比較も。
- **NII「LLM-jp-4」**: 対話能力を測る「日本語 MT-Bench」で 32B-A3B モデルが 7.82 点を記録し、GPT-4o（7.29 点）・Qwen3-8B（7.14 点）を上回ると報告。

出典:
- PLaMo 3.0 Primeとは？ 性能や料金、国産LLM（AI総合研究所）（未確認の出典のためリンク省略）
- Sarashina3とは？ SB Intuitions開発の国産LLM（AI Revolution）（未確認の出典のためリンク省略）
- 国産LLM「LLM-jp-4」が日本語MT-BenchでGPT-4o超え（nohumans.jp）（未確認の出典のためリンク省略）

---

## 5. 行政・実務での生成AI活用：デジタル庁の規制見直し支援と国会答弁支援

行政実務での生成AI活用が進展しています。

- **デジタル庁**: 生成AIのエージェント機能で自治体の例規からアナログ規制の候補を抽出する手順を公開。条文の趣旨や上位法令との整合性は最終的に職員が確認する必要があると明記。
- **デジタル庁（国会答弁支援）**: 政府職員の負担軽減に向け、国会答弁の作成を支援する AI アプリを開発。AI 任せにせず最後は人間が確認する運用を想定。

出典:
- [デジタル庁 新着・更新（アナログ規制見直しの取組事例）](https://www.digital.go.jp/news/)
- [政府職員の負担軽減へ 国会答弁支援AIアプリ開発 デジタル庁（NHK）](https://news.web.nhk/newsweb/na/nd-20261030de68496)
- AI最新ニュースまとめ（OpenAI「Images 2.6」公開ほか）（plus-web3）（未確認の出典のためリンク省略）

---

## 6. 開発者・エージェント基盤の動き

- **AWS Kiro（Android アプリ公開）**: クラウドで動く AI コーディングの作業をスマホで引き継げる Android アプリを公開。Grok 4.7 も選択可能に。
- **AWS Quick「SmartApprovals」**: AI エージェントからの「確認疲れ」を減らす仕組みとして、別の AI が承認か差し戻しかを事前判定し、危険操作のみ人に承認を求める方式を導入。
- **OpenAI「Images 2.6」**: 生成速度 50% 向上、GIF 生成・SVG 書き出しに対応。API では用途に応じた 2 モデル、修正箇所のマーキング、計画の程度を調整する「complexity」パラメータなどを提供。
- **Anthropic**: Agent Skills を Agentic AI Foundation に寄付（Donating Agent Skills To The Agentic AI Foundation）を発表。

出典:
- [AWSのKiroがAndroidアプリ公開（Techno Edge）](https://www.techno-edge.net/article/2026/11/13/5718.html)
- [AIエージェントからの「確認疲れ」を減らす仕組み、AWS Quickが導入（Techno Edge）](https://www.techno-edge.net/article/2026/11/13/5717.html)
- [Donating Agent Skills To The Agentic AI Foundation（Anthropic News）](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)

---

## 7. 1-bit LLM / ローカル推論の動向

- **BitNet b1.58**: 重みを 1.58bit で学習する 1-bit LLM の研究が継続。CPU 上での高速・無損失推論（bitnet.cpp）や、Qwen3.5(4B)×Ollama×Docker での実験的ホスト環境（bitnet-server）の試みなど、ローカル実行との組み合わせが話題に。
- **ローカル推論シフト**: Carnot が NVIDIA のスタートアップ支援プログラム「NVIDIA Inception」に採択され、オンプレミス・プライベートクラウドでの AI 推論を重視。AI エージェント基盤「Jinba」は三菱 UFJ 銀行にも導入。
- **Hugging Face**: Salesforce「SOV-Transcribe-1」（実世界音声向け #1 オープンウェイトモデル）、NVIDIA「Cosmos 3」（対話型ワールドシミュレーション）、Allen AI「ToyBlocks」（ロボット学習・評価用制御ワールド）など、オープンモデル・データセットの公開が続く。

出典:
- [BitNet (1bitLLM)×Qwen3.5(4B)×Ollama×OpenClaw×Docker（note / leococolin）](https://note.com/leococolin/n/n056d9b5980ad)
- [1-bit LLMとBonsai：極限軽量化の最前線を論文ベースで整理する（Zenn / amasashi）](https://zenn.dev/amasashi/articles/e75ffebff53bb7)
- [Introducing Salesforce SOV-Transcribe-1（Hugging Face Blog）](https://huggingface.co/blog/salesforce-sovereign-intelligence/sov-transcribe-1)
- [New NVIDIA Cosmos 3 Open Models for Interactive World Simulation（Hugging Face Blog）](https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation)

---

## 編集後記（qwen3.8 視点）

今週は、最上位モデルの提供開始（Gemini 4 Carbon）と、その裏で進む「国内完結・ローカル推論」の潮流（Cohere Model Vault、Carnot、BitNet）が対をなす一週間でした。また、Microsoft 365 障害が政府基盤 GSS まで波及した事象は、生成AI・クラウド基盤の可用性リスクが行政業務に直結することを改めて示しています。国産 LLM は日本語性能で海外モデルに肉薄・超越する報告が続く一方、実務では「最終確認は人間が担う」運用が共通項として浮上しています。

---

*本記事は qwen3.8:27b-mlx（Ollama 経由）により自動生成された比較用サブモデルの週次まとめです。*

</div>
</div>

</div>

<div class="sonnet-eval" markdown="1">

## 🧠 Claude Sonnet による比較・評価（2026-11-14）

*その週に揃った全モデルの記事を読んだ Claude Sonnet が、情報カバレッジ・技術精度・読みやすさの観点から評価します。*

---

# 生成AI週次ダイジェスト比較評価（11/7〜11/14）

> ⚠️ **注意喚起（偽情報の疑い）**
> - **🌩️ nemotron**: 「OpenAIが推論モデル『o3』と『o4-mini』を発表」という記述は時系列的に不自然です。o3系モデルは既に過去に発表済みのモデルであり、他の4記事がGemini 4 Carbon/Hydrogen・Claude Fable 5.2/Mythos 5.2・GPT-5.4系など2026年11月時点の最新ラインナップを扱っている中で、旧世代モデルを「今週の新発表」として扱っているのは矛盾しています。出典も検索結果の見出しのみで、公式発表（OpenAI News等）への直接リンクがありません。
> - **⚡ Claude Haiku**: 「OpenAIがサイバーセキュリティ特化型『GPT-6 Cyber』をDaybreak Red経由でリリース」という記述は、他の4記事・公開情報源のいずれにも対応する言及がなく、出典リンクも付されていません。モデル名・提供経路ともに裏付けが取れないため、誤情報の可能性があります。同様に「Anthropicが東京にアジア太平洋初のオフィスを開設」「Googleから200億ドル以上の投資」についても出典なしで、要検証です。

---

### カバレッジの違い

- **🖥️ qwen3.6**:
  - NVIDIAジェンスン・フアンCEO辞任の背景報道（不倫疑惑・議会証言）を他紙から多角的に紹介
  - Memoket Gem（AIウェアラブル記憶補完デバイス）
  - OpenAI・Anthropic・GoogleによるAI標準化団体設立の動き
  - AWS Quick「SmartApprovals」の仕組み詳細

- **⚡ Claude Haiku**:
  - 日本企業の定量的な生成AI導入成果（NEC・パナソニック・イオンリテールの具体的な効率化数値）
  - PFN「PLaMo 3.0 Fin」（金融特化LLM）、ソフトバンク「Sarashina mini」
  - OpenAIの四半期収益（約10億ドル、前年同期比50%増）
  - Ollama v0.40.16・「Ripple Preview」モデル追加

- **🦉 ornith**:
  - Salesforce「SOV-Transcribe-1」（音声文字起こしOSSモデル、WER 2.28%等の詳細ベンチマーク）
  - NVIDIA「Cosmos 3」オープンモデル
  - llama.cpp／ggml v1.0.0リリース
  - AutoGenのMCP標準入出力アダプター（autogen_ext.tools.mcp）

- **🌩️ nemotron**:
  - デジタル庁「源内」選定の国産LLM7モデルを表形式的に整理（PLaMo 3.1 Prime・Sarashina・tsuzumi 2・cotomi・CC Gov-LLM・ELYZA・Takane）
  - （※OpenAI o3/o4-miniは上記の通り時系列的に疑義あり）

- **💠 qwen3.8**:
  - Gemini 4 Carbonの安全性ベンチマーク数値（レッドチーミング突破率0.8%等）や料金改定スケジュールの詳細
  - 国産LLM3モデルの横並び比較（PLaMo 3.0 Prime・Sarashina3・LLM-jp-4のMT-Benchスコア等）
  - 行政実務AI活用（アナログ規制見直し支援、国会答弁支援AIアプリ）
  - Cohereの資金調達額・企業価値・AISLE買収による「Cohere Cyber」設立
  - Carnot（NVIDIA Inception採択）、三菱UFJ銀行への「Jinba」導入

---

### 各観点の評価

| 観点 | **🖥️ qwen3.6**<br>qwen3.6:35b-mlx | **⚡ Claude Haiku**<br>claude-haiku-4-5 | **🦉 ornith**<br>ornith-1.5:35b | **🌩️ nemotron**<br>nemotron-3.5-lightning:30b-mlx | **💠 qwen3.8**<br>qwen3.8:27b-mlx |
|------|------|------|------|------|------|
| **情報の深さ** | ⭐⭐⭐⭐ 各トピックに背景説明あり、数値引用は控えめ | ⭐⭐⭐ 説明は詳細だが未検証の固有名詞（GPT-6 Cyber等）が混在し信頼度を下げる | ⭐⭐⭐⭐⭐ 価格・技術仕様まで具体的に記載 | ⭐⭐ 1トピック1段落程度で浅く、内容に疑義もある | ⭐⭐⭐⭐⭐ ベンチマーク数値・料金・比較まで最も掘り込みが深い |
| **カバレッジ** | ⭐⭐⭐⭐⭐ 9トピック、業界大事件を広くカバー | ⭐⭐⭐⭐ 9トピック、他モデル未掲載の独自ネタも多い | ⭐⭐⭐⭐⭐ 12項目と最多、OSS系に強い | ⭐⭐ 6トピックのみで最少、深掘りも薄い | ⭐⭐⭐⭐⭐ 7カテゴリ内に多数の小トピックを内包し実質最広 |
| **国内AI動向** | ⭐⭐⭐⭐ Cohere・デジタル庁中心、国産LLM名列挙のみ | ⭐⭐⭐⭐⭐ 源内の展開規模・企業導入実績まで定量的 | ⭐⭐ Cohere・デジタル庁のみで国産LLM個別動向なし | ⭐⭐⭐ 源内選定7モデルの整理は良いがそれ以外薄い | ⭐⭐⭐⭐⭐ 国産LLM比較・行政実務まで最も充実 |
| **読みやすさ** | ⭐⭐⭐⭐⭐ 見出し・まとめ構成が明快 | ⭐⭐⭐⭐ 段落構成はよいが出典欄が薄く文章だけが浮く箇所あり | ⭐⭐⭐⭐ 情報量は多いが文章がやや長く密度が高い | ⭐⭐⭐⭐ 簡潔で読みやすいが内容不足気味 | ⭐⭐⭐ 情報量が多く充実している分、やや長文で読むのに時間がかかる |
| **情報源の明示** | ⭐⭐⭐⭐⭐ ほぼ全項目にリンク、未確認出典も明示 | ⭐⭐ 多くの段落にリンクがなく、裏付けが取れない固有名詞もある | ⭐⭐⭐⭐⭐ ほぼ全項目にリンクあり | ⭐⭐ リンクは少なく、一部内容に時系列的な疑義 | ⭐⭐⭐⭐⭐ リンクが最も充実、未確認出典も明示的に区別 |
| **ビジネス視点** | ⭐⭐⭐ AWS・Cohereの事例紹介はあるが分析は薄め | ⭐⭐⭐⭐⭐ 日本企業の定量成果（時間削減・工数削減%）が豊富 | ⭐⭐⭐ OSSモデル中心で技術寄り、ビジネス分析は少なめ | ⭐ ビジネス視点の記述がほぼない | ⭐⭐⭐⭐⭐ 料金比較・資金調達額・企業導入事例まで最も充実 |

---

### 総評

今週最大のテーマはGemini 4 Carbon/Hydrogenの提供開始、NVIDIAフアンCEOの電撃辞任、Microsoft 365大規模障害の3本柱で、5記事とも概ね一致して捉えていた。一方でローカルモデル同士（qwen3.6・ornith・nemotron・qwen3.8）の差は大きく、qwen3.8は国産LLM比較や料金・資金調達額まで踏み込み最も情報密度が高い一方、nemotronはトピック数・深さともに明らかに見劣りし、OpenAI o3/o4-miniの時系列矛盾という品質上の問題も抱えていた。ornithはOSS・技術系トピックの発掘力に優れるが国内動向が薄い。Claude Haikuは日本企業の定量成果など独自の強みを持つものの、出典明示の甘さと未検証固有名詞が目立ち信頼性面で見劣りする。各記事を合わせて読むことで、海外フロンティアモデルの動向から国産LLMの実務比較、OSS技術の最前線まで、週全体を補完的に把握できる。

---

</div>

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/2026-1114">11/7〜11/14</a><span class="date">2026-11-14</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-1107">10/31〜11/7</a><span class="date">2026-11-07</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-1031">10/24〜10/31</a><span class="date">2026-10-31</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-1024">10/17〜10/24</a><span class="date">2026-10-24</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-1017">10/10〜10/17</a><span class="date">2026-10-17</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-1114">11/7〜11/14</a><span class="date">2026-11-14</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-1107">10/31〜11/7</a><span class="date">2026-11-07</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-1031">10/24〜10/31</a><span class="date">2026-10-31</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-1024">10/17〜10/24</a><span class="date">2026-10-24</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-1017">10/10〜10/17</a><span class="date">2026-10-17</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-1114">11/7〜11/14</a><span class="date">2026-11-14</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-1107">10/31〜11/7</a><span class="date">2026-11-07</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-1031">10/24〜10/31</a><span class="date">2026-10-31</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-1024">10/17〜10/24</a><span class="date">2026-10-24</span></li>
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-1017">10/10〜10/17</a><span class="date">2026-10-17</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/haiku_weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>📅 月次まとめ</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-11">2026年11月</a><span class="date">2026-11</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-10">2026年10月</a><span class="date">2026-10</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-09">2026年9月</a><span class="date">2026-09</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-08">2026年8月</a><span class="date">2026-08</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-07">2026年7月</a><span class="date">2026-07</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

</div>
</div>
