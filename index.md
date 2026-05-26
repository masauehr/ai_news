---
layout: compare
title: 生成AI週次ダイジェスト
---

<div class="compare-header">
  <h1>🔬 モデル比較（5/25〜5/31）</h1>
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

# 生成AI週次ダイジェスト（5/25〜5/31）

今週は、OpenAIによる80年の歴史を持つ数学の未解決問題の解明、Google I/O 2026でのGeminiシリーズ大刷新、AnthropicによるClaude Opus 4.7のリリースとStainless買収など、生成AI界隈で非常に重要なニュースが相次ぎました。日本国内ではデジタル庁「源内」への国産LLM展開や、OpenAI Codexのオンプレミス展開など、実務レベルでのAI導入が加速しています。

---

## 1. OpenAI: GPT-5.5が80年の歴史を持つ数学の未解決問題を解明

**[An OpenAI model has disproved a central conjecture in discrete geometry](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)** (OpenAI, 2026-05-20)

OpenAIは、内部推論モデル「GPT-5.5」が80年以上にわたり未解決だった組合せ幾何学における有名な予想（Erdősのunit distance problem）を解明し、反例を示したと発表しました。フィールズ賞受賞者Tim Gowers氏らは「画期的な成果」「AI数学におけるマイルストーン」と評価しています。

- **背景**: 1946年にPaul Erdősが提示した平面単位距離問題。正方形格子構成が本質的に最適であるという長期の予想が、GPT-5.5によって反証されました。
- **手法**: 代数体理論（algebraic number theory）から予想外のアイデアを抽出し、幾何学的質問に適用する手法を採用。
- **意義**: AIが自律的に主要な未解決問題を解決したのは初めて。数学界だけでなくAIコミュニティにも大きな衝撃を与えています。

---

## 2. Google I/O 2026: Gemini 3.5 Flash, Gemini Omni, Gemini Sparkを発表

**[Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)** (Google DeepMind, 2026-05-19)
**[Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)** (Google DeepMind, 2026-05-19)

Google I/O 2026では、Geminiシリーズの大幅な刷新が発表されました。

### Gemini 3.5 Flash
- 長時間のagenticタスクに最適化されたモデル。開発者や監査担当者が数日〜数週間を要していた作業を短縮可能。
- 「frontier intelligence with action」を標榜し、推論と行動の両立を実現。

### Gemini Omni
- マルチモーダル（テキスト・画像・動画・音声）を統合した最新モデル。
- 動画生成や複雑な視覚的理解において飛躍的な性能向上。

### Gemini Spark
- 新しいパーソナルAIアシスタントとして発表。日常のタスク管理や創造的作業をサポート。

**[100 things we announced at I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)** (Google Blog, 2026-05-19)
- Google Antigravity 2.0の発表（AI-powered開発プラットフォーム）
- Co-Scientist: マルチエージェントAIパートナーによる研究加速
- Gemini for Science: AI実験ツールの新登場

---

## 3. Anthropic: Claude Opus 4.7リリース、Stainless買収、KPMG/PwC/Gates Foundationとの連携

### Claude Opus 4.7
**[Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)** (Anthropic, 2026-05-19)

AnthropicはClaude Opus 4.7を一般公開しました。Opus 4.6からの主な改善点：
- **ソフトウェアエンジニアリング**: 最も困難なタスクで顕著な向上。複雑で長時間のコーディング作業も自律的に処理可能。
- **ビジョン性能**: より高解像度の画像認識に対応。プロフェッショナルなインターフェースやスライド生成の品質が向上。
- **セキュリティ**: Cyber Verification Program（脆弱性調査、ペネトレーションテスト）向けにサイバー防御機能を強化。Claude Mythos Previewよりもサイバー能力を抑制し、安全対策を講じてリリース。
- **価格**: Opus 4.6と同様、入力$5/百万トークン、出力$25/百万トークン。

**[Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs)** (Anthropic, 2026-04-17)
- Anthropic Labs製品として「Claude Design」をリリース。自然言語でデザイン、プロトタイプ、スライド、マーケティング資料を生成可能。Figmaへの挑戦とも見なされている。

### Stainless買収
**[Anthropic Acquires Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)** (Anthropic, 2026-05-19)
- MCP（Model Context Protocol）サーバーツールリングやSDKを専門とするStainlessを買収。エージェント接続性の拡張が目的。

### KPMGとのグローバルアライアンス
**[Anthropic KPMG](https://www.anthropic.com/news/anthropic-kpmg)** (Anthropic, 2026-05-19)
- KPMGのデジタルプラットフォーム「Digital Gateway」にClaudeを統合。全世界27万6千人の従業員が利用可能に。

### PwCとのパートナーシップ拡大
**[Pwc Expanded Partnership](https://www.anthropic.com/news/pwc-expanded-partnership)** (Anthropic, 2026-05-14)
- PwCがClaudeを技術構築、デール実行、エンタープライズ変革に深く統合。

### ザ・ガッツ財団との$2億ドルパートナーシップ
**[Gates Foundation Partnership](https://www.anthropic.com/news/gates-foundation-partnership)** (Anthropic, 2026-05-14)
- Bill & Melinda Gates Foundationと4年間で$2億ドルのパートナーシップ。AIツールを医療・教育分野で展開。

---

## 4. OpenAI: CodexのDellとのオンプレミス展開、GPT-5.5のCybersecurity活用

**[OpenAI and Dell Technologies partner to bring Codex to hybrid and on-premises enterprise environments](https://www.marketingscoop.com/tech/openai-and-dells-codex-partnership-moves-enterprise-ai-out-of-browser-tabs/)** (Marketing Scoop, 2026-05-18)

OpenAIとDell Technologiesは、Codex（コーディングエージェント）をハイブリッドおよびオンプレミスの企業環境に展開するパートナーシップを発表。
- Dell AI Data Platformとの統合により、データローカライゼーションを維持しながらCodexを活用可能。
- 企業のセキュリティ要件を満たしつつ、AIコーディング支援を導入する道を開く。

**[OpenAI named a Leader in enterprise coding agents by Gartner](https://openai.com/news/)** (OpenAI, 2026-05-22)
- GartnerがOpenAIをエンタープライズコーディングエージェント分野でリーダーと評価。

---

## 5. Google DeepMind: シンガポールとのNational AI Partnership、Co-Scientist発表

**[Strengthening Singapore’s AI Future: A New National Partnership](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/)** (Google DeepMind, 2026-05-19)
- Google DeepMindはシンガポール政府とNational AI Partnershipを強化。医療・ライフサイエンス、教育、気候変動対策などでAIを活用。
- AlphaFoldやGemina for Educationの展開、SG Enable（障害者支援）との連携など、社会課題解決に焦点。

**[Co-Scientist: A multi-agent AI partner to accelerate research](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/)** (Google DeepMind, 2026-05-19)
- マルチエージェントAIによる研究加速ツール「Co-Scientist」を発表。科学的研究の仮説生成や実験設計を支援。

---

## 6. MCP（Model Context Protocol）: GoogleがOpenAIに続き採用表明

**[Google joins OpenAI in adopting Anthropic's protocol for connecting AI agents](https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)** (ZDNET, 2026-05-21)
- GoogleがAnthropicのMCP（Model Context Protocol）をサポートすると表明。OpenAIに続き、主要AI企業がMCPを採用することで、エージェント間の相互運用性が向上。

---

## 7. 日本国内動向: デジタル庁「源内」への国産LLM展開、OpenAI Codexの日本展開

### デジタル庁「源内」へ国産LLM7モデル展開
**[デジタル庁がガバメントAI「源内」で国産LLM7件を選定──全府省庁18万人で実証](https://www.sbbit.jp/article/cont1/182108)** (SB Bit, 2026-03-06)
**[【2026年最新】デジタル庁が選んだ「国産LLM」7選！政府の生成AI「源...](https://wa2.ai/ai-news/kokusan-llm-genai-platform-genai-digitalcho-ai-strategy-dx-security-guide)** (WA2, 2026-03-24)

デジタル庁は、政府共用生成AI基盤「源内（げんない）」へ7つの国産LLMを展開。
- **選定モデル**: NTTデータ・PLaMo・Sarashina2・tsuzumi 2・ELYZAなど
- **実証期間**: 2026年5月〜2027年3月、全府省庁約18万人が試用
- **目的**: 国産AIの育成・強化、民間投資の喚起、AIにおける日本の自律性確保

### LLM-jp-4の注目
**[国産LLM「LLM-jp-4」が日本語MT-BenchでGPT-4oを上回った](https://qiita.com/nogataka/items/6821e5d530938d269e58)** (Qiita, 2026-04-08)
**[約12兆トークンの良質なコーパスで学習した新たな国産LLM「LLM-jp-4 8...](https://www.nii.ac.jp/news/release/2026/0403.html)** (NII, 2026-04-03)

国立情報学研究所（NII）が公開した国産LLM「LLM-jp-4 32B-A3B」は、日本語MT-BenchでGPT-4oのスコアを上回る性能を示し、国内外で注目されています。長文要約、推論、文化・制度関連の質問で特に強みを持つとされています。

### OpenAI Codexの日本展開
**[OpenAI named a Leader in enterprise coding agents by Gartner](https://openai.com/news/)** (OpenAI, 2026-05-22)
- OpenAI Codexがエンタープライズコーディングエージェント分野でリーダーと評価され、日本企業への展開も期待される。

---

## 8. ローカルLLM・Ollama: 新モデル動向

**[【2026年最新】OllamaおすすめAIモデル徹底比較！目的・スペック別の選び方（ローカルLLM）](https://lifework-blog.com/ollama-recommended-models/)** (LIFEWORK Blog, 2026-03-19)
- Ollamaで使えるモデルの最新比較。gemma3など主要モデルが対応。

**[ローカルLLMのOllamaが画像生成に対応](https://pc.watch.impress.co.jp/docs/news/2079796.html)** (PC Watch, 2026-01-22)
- Ollamaが試験的に画像生成をサポート。macOS対応後、Windows/Linuxへ拡げる予定。

---

## 9. AIエージェント・MCP: 最新動向

**[Anthropic Acquires Stainless To Expand Agent Connectivity](https://pulse2.com/anthropic-acquires-stainless-to-expand-agent-connectivity/)** (Pulse2, 2026-05-19)
- AnthropicがStainlessを買収し、MCPサーバーツールリングを強化。エージェント間の接続性向上を目指す。

**[Google joins OpenAI in adopting Anthropic's protocol for connecting AI agents](https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)** (ZDNET, 2026-05-21)
- GoogleがMCPをサポート表明。OpenAI、Anthropic、Googleの3社がMCPを採用することで、エージェントエコシステムが拡大。

---

## 10. Note記事: 生成AI使ってみた

**[日々の壁打ち：ComfyUI...](https://note.com/nyaa_toraneko/n/n0522322b97c6)** (note / nyaa_toraneko)
- ComfyUIを用いた画像生成AIの実践的な使い方。SD UI Forgeとの組み合わせなど。

**[アニメ動画作りにおすすめの動画生成AI...](https://note.com/ai_freak/n/na6f3419fa9e2)** (note / ai_freak)
- Midjourneyや動画生成AIの比較検証。アニメーション制作への活用事例。

---

## まとめ

今週は、OpenAIによる数学問題の解明という画期的な成果を皮切りに、Google I/O 2026でのGeminiシリーズ刷新、AnthropicのClaude Opus 4.7リリースと買収・連携発表など、生成AI界隈で非常に重要なニュースが相次ぎました。

特に注目すべきは：
1. **OpenAI GPT-5.5**による数学問題解明 — AIの推論能力が新たな段階へ
2. **Google I/O 2026** — Gemini 3.5 Flash, Omni, Sparkの発表とCo-Scientist
3. **Anthropic Claude Opus 4.7** — コーディング性能の大幅向上とセキュリティ強化
4. **MCPエコシステムの拡大** — GoogleがOpenAIに続きMCPを採用
5. **日本国内ではデジタル庁「源内」への国産LLM展開** — 18万人規模の実証が開始

今週も生成AIの進化スピードは衰えることを知りません。次週も注目です。

---

*本記事は以下の情報源に基づいて作成されています:*
- [OpenAI Blog](https://openai.com/news/)
- [Anthropic News](https://www.anthropic.com/news/)
- [Google DeepMind Blog](https://deepmind.google/blog/)
- [Google Blog](https://blog.google/)
- [ZDNET](https://www.zdnet.com/)
- [SB Bit](https://www.sbbit.jp/)
- [WA2](https://wa2.ai/)
- [NII](https://www.nii.ac.jp/)
- [Qiita](https://qiita.com/)
- [LIFEWORK Blog](https://lifework-blog.com/)
- [PC Watch](https://pc.watch.impress.co.jp/)
- [note記事](https://note.com/)

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（5/25〜5/31）

今週の生成AI業界では、Google I/O 2026での大型発表から国産モデルの進化、そして新たな翻訳AIの登場まで、様々なトピックがありました。以下、主要なニュースを5つのカテゴリーに分けてまとめます。

## 1. 大手AI企業の最新動向

### Google I/O 2026：AIメガネとGemini 3.5の発表
Googleは開発者向けイベント「Google I/O 2026」で、複数の重大発表を行いました。特に注目されたのは以下の3点です：

- **Gemini Omnuモデルの発表**：マルチモーダル能力を強化した最新版Geminiの登場
- **AIメガネ「インテリジェント・アイウェア」の秋冬発売予定**：サムスン協業により、Geminiのエージェント機能を音声で指示・確認できるスマートグラス
- **Gemini 3.5**：フロンティアレベルの知能を備えたアクション機能付きモデル

参考：[Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)、[Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

### OpenAIの企業向け展開
OpenAIは複数の重要なパートナーシップを発表：

- **Gartnerでエンタープライズコーディングエージェントのリーダーに選定**（5月22日）
- **DellとのパートナーシップでCodexのハイブリッド・オンプレミス展開**（5月18日）：企業環境での安全なCodex利用を実現
- **ChatGPTに個人金融機能を追加**（5月15日）：ユーザーのファイナンシャル情報管理機能
- **敏感な会話でのコンテキスト認識向上**（5月14日）：プライバシーを配慮した対話品質の改善

参考：[OpenAI News](https://openai.com/news/)

### Anthropicの動向
Anthropicの最新情報：

- **Claude Opus 4.7の発表**：最新世代の高性能モデル
- **Claude Designサービスの展開**（Anthropic Labs）：デザイン分野への応用
- **KPMG・PwCとの拡大パートナーシップ**：エンタープライズAI導入支援の強化
- **Bill & Melinda Gates Foundationとの新規パートナーシップ**：グローバルな社会課題解決への取り組み

参考：[Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)、[Anthropic KPMG](https://www.anthropic.com/news/anthropic-kpmg)

## 2. 国産AI・ローカルLLMの進展

### 国産LLM「LLM-jp-4」が国際競争力を達成
国立情報学研究所（NII）は2026年4月3日、新たな国産LLM「LLM-jp-4」をオープンソースで公開しました：

- **2つのモデル構成**：
  - LLM-jp-4 8Bモデル：軽量でローカル実行に最適
  - LLM-jp-4 32B-A3B（Mixture of Experts）：高い表現力を実現
- **12兆トークンの大規模日本語コーパスで学習**
- **日本語MT-BenchでGPT-4oを上回るスコアを達成**：日本語能力で国際ベンチマーク最高水準を実現
- **オープンソース化**：学術・産業界での研究開発に資する公開戦略

この成功は、日本語特化型モデルの有効性を実証し、国産AI開発の国際競争力を示す重要なマイルストーンとなっています。

参考：[LLM-jp-4公開発表](https://www.nii.ac.jp/news/release/2026/0403.html)、[note / 編集部](https://note.com/humble_bobcat51/n/nd9a3cf59b264)

### NTTの国産LLM「tsuzumi 2」も企業向けに提供開始
NTTが10月20日に発表した「tsuzumi 2」は、以下の特徴を備えています：

- **純国産フルスクラッチ開発**：セキュリティ面でのメリット
- **軽量設計**：1GPUで動作可能で、コストパフォーマンスに優れている
- **日本語性能と専門知識の強化**：RAGユースケースでも高性能を実現
- **低コスト・高セキュアの維持**：企業DXを支える選択肢

参考：[NTT tsuzumi 2提供開始](https://group.ntt/jp/newsrelease/2025/10/20/251020a.html)

### Ollamaエコシステムの成熟
ローカルLLM実行ツール「Ollama」は、5月24日の情報でも以下の進展が確認されます：

- **OpenAI Codex CLI連携**（v0.24以降）：API課金やレート制限なしでのローカル実行
- **多数の最新モデル対応**：Llama 4、DeepSeek-R1、GPT-OSS、Gemma 4など
- **GUI対応版の実装**（v0.10.0以降）：Windows環境でもChatGPTのような使い勝手を実現

参考：[Ollama完全ガイド](https://warokai.com/2026/04/26/ollama-complete-guide-2026/)

## 3. 新興AI技術と軽量モデルの実用化

### GPT-5.5匹敵のローカル翻訳AI「Hy-MT2-30B」が無料公開
テンセント開発の革新的翻訳モデルが5月25日に注目を集めました（テクノエッジ報道）：

- **GPT-5.5レベルの翻訳性能**：高精度な自然言語翻訳を実現
- **軽量版「Hy-MT2-1.8B」も公開**：重量級の有料翻訳API（Microsoft有料翻訳サービスなど）を凌駕
- **完全ローカルで実行可能**：プライバシー面でも優位性を持つ
- **無料提供**：アカデミアと産業界での利用を促進

参考：[テクノエッジ「GPT-5.5匹敵のローカル翻訳AI」](https://www.techno-edge.net/article/2026/05/25/5098.html)

### 日本語TTSモデル「Supertonic 3」とAI3D生成「Pixal3D」
5月24日のテクノエッジまとめで複数の日本の生成AI技術が紹介されました：

- **Supertonic 3**：
  - CPU完全動作の日本語対応TTS（Text-to-Speech）
  - ローカル環境での低レイテンシー音声生成を実現
  
- **Pixal3D**：
  - 元の写真に忠実な3Dモデル生成AI
  - 画像から高精度な3D表現への変換を可能に

参考：[テクノエッジ「生成AI技術5つを解説」](https://www.techno-edge.net/article/2026/05/24/5094.html)

## 4. AIエージェント・ロボティクス分野の進展

### LeRobot：オープンソースの低コスト人型ロボット学習プラットフォーム
Hugging Faceは新たなロボティクスプロジェクト「LeRobot Humanoid」を発表：

- **3Dプリント可能な設計**：アクセス可能な価格でのロボット学習を実現
- **オープンなロボット学習フレームワーク**：研究開発の民主化を推進

参考：[LeRobot Humanoid: An Open, Low-Cost, 3D-Printed Humanoid for Robot Learning](https://huggingface.co/blog/VirgileBatto/lerobot-humanoid)

### NVIDIAコスモスによるロボットビデオ生成
NVIDIAの「Cosmos」モデルがロボット動作予測に活用される動き：

- **LoRA/DoRA微調整対応**：ロボット固有の動作学習に最適化
- **ビデオ予測によるシミュレーション**：ロボット制御の高度化を支援

参考：[Fine-Tuning NVIDIA Cosmos](https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation)

### 推論効率化技術の進化
AIエージェント・ロボット実装に必須の技術進展：

- **KV Caching技術**：トランスフォーマー推論効率を大幅向上
- **Agent Traces as Memory**：エージェントの記憶機構を改善
- **Mixture of Experts（MoE）**：効率的な大規模モデルの実装

参考：[KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)、[Software Forgets: Agent Traces Are the Memory](https://huggingface.co/blog/huggingface/agent-traces-as-memory)

## 5. AI応用事例と企業のDX推進

### 生成AIで効率化できる業務と実装事例
AINOWの最新レポート（5月）では、生成AI導入による業務効率化の具体像が明らかに：

- **業務8選の効率化ユースケース**：
  - コンテンツ生成（文案作成・レポート自動化）
  - データ分析・インサイト抽出
  - カスタマーサービス自動化
  - コード生成・ソフトウェア開発支援
  
- **導入時の注意点**：セキュリティ、品質管理、コスト管理

参考：[AINOW「生成AIで効率化できる業務8選」](https://ainow.ai/2026/05/16/278083/)

### DXを加速する生成AIの全体像
同じくAINOWの記事では、生成AIによるDX加速戦略が12社の成功事例とともに紹介：

- **成功事例12社の共通パターン**：小規模パイロットから段階的な組織展開
- **推進ステップ**：導入計画 → パイロット実装 → 評価・改善 → 全社展開
- **注意点**：変化管理、スキル育成、倫理ガイドラインの整備

参考：[AINOW「生成AIでDXを加速する全体像」](https://ainow.ai/2026/05/19/278090/)

### Googleの日本国内支援策「Google Play Accelerator Japan」
Google I/O 2026に合わせた日本市場重視戦略：

- **アプリ・ゲーム開発者向け海外展開支援**：国内スタートアップの国際展開を支援
- **Android XR開発者サポート**：新型ウェアラブル環境での開発機会

参考：[テクノエッジ「Google Play Accelerator Japan」](https://www.techno-edge.net/article/2026/05/25/5100.html)

## 今週の総括

**国産AI技術の確立**がこの週を特徴付ける最大のテーマです。LLM-jp-4が日本語ベンチマークで国際水準を達成し、NTTのtsuzumi 2が企業向けに本格展開されるなど、日本独自のAI基盤が確実に構築されています。

一方、Googleのメガネ型AIやOpenAIの企業向けCodex展開など、大手企業の**AIエージェント化・実装化**も加速しており、単なる会話AIから実行可能なタスク処理へのシフトが明確になりました。

ローカルLLMの成熟（Ollama、LLM-jp-4のオープンソース化）と軽量モデル（Hy-MT2-1.8B、Supertonic 3）の普及により、**プライバシー・セキュリティ・コスト効率**を両立させたAI利用が現実化しつつあります。企業のDX推進局面では、これらの国産・オープン選択肢が重要な役割を担う見込みです。

---

**情報源**
- Techno Edge（テクノエッジ）
- AINOW
- Google Blog・Google DeepMind Blog
- OpenAI News
- Anthropic News
- Hugging Face Blog
- 国立情報学研究所（NII）
- NTTグループ
- 日本経済新聞・朝日新聞などのニュースメディア

</div>
</div>

</div>

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0518">5/18〜5/24</a><span class="date">2026-05-18</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0511">5/11〜5/17</a><span class="date">2026-05-11</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0504">5/4〜5/10</a><span class="date">2026-05-04</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0427">4/27〜5/3</a><span class="date">2026-04-27</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/haiku_weekly/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/haiku_weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>📅 月次まとめ</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-05">2026年5月</a><span class="date">2026-05</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-04">2026年4月</a><span class="date">2026-04</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

</div>
</div>
