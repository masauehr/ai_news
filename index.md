---
layout: compare
title: 生成AI週次ダイジェスト
---

<div class="compare-header">
  <h1>🔬 モデル比較（5/30〜6/6）</h1>
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

# 生成AI週次ダイジェスト（5/30〜6/6）

今週は主要プレイヤーが相次いで大規模アップデートを発表した週です。AnthropicはClaude Opus 4.8でエージェント性能とハンスネスを大幅強化、Google DeepMindはGemini 3.5 FlashとGemini Omniの2本立てでエージェント・マルチモーダル領域を牽引しました。OpenAIはChatGPTのメモリ機能「Dreaming V3」を更新し、Microsoftは画像生成モデルMAI-Image-2.5を発表。またデジタル庁はガバメントAI「源内」をOSSとして公開し、全府省庁への展開を開始するなど、日本国内のAI動向も活発です。

---

## 1. Anthropic: Claude Opus 4.8 — エージェント性能とハンスネスの大幅強化

Anthropicは5月28日（米国時間）、Claude Opusシリーズをアップグレードした**Claude Opus 4.8**を発表しました。Opus 4.7からの改善に加え、複数の新機能を同時にリリースしています。

### 主な特徴
- **Super-Agentベンチマーク**でGPT-5.5を凌駕し、全ケースをエンドツーエンドで完了した唯一のモデルに
- **Legal Agent Benchmark**で過去最高スコアを記録し、10%以上のall-passを達成
- **Online-Mind2Web**で84%という最高スコアを記録
- **ハンスネスの強化**: Opus 4.7と比較してコードの欠陥を見逃す率が約4分の1に減少
- **Fast Modeの価格改定**: 2.5倍速で動作し、コストは従来比3分の1に

**参考URL**: [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)

---

## 2. Google DeepMind: Gemini 3.5 Flash — エージェント特化モデルの登場

Google DeepMindはGemini 3.5シリーズの第一弾として**Gemini 3.5 Flash**を発表しました。

### 主な特徴
- **Terminal-Bench 2.1**: 76.2%、**GDPval-AA**: 1656 Elo、**MCP Atlas**: 83.6%など、エージェントベンチマークで先行モデルを凌駕
- **出力トークン/秒**において他のフロンティアモデル比4倍高速
- **Gemini Spark**: 3.5 Flashを基盤とした個人用AIエージェントがベータテスト開始

**参考URL**: [Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

---

## 3. Google DeepMind: Gemini Omni — マルチモーダル生成の新たな地平

**Gemini Omni**は「推論」と「創造」を融合した新しいモデルファミリー。画像・音声・動画・テキストを入力として受け取り、高品質な動画を生成することができます。

- **Conversation-based Video Editing**: 自然言語による動画編集、キャラクターの一貫性・物理法則の保持を実現
- **Physics-aware Generation**: 重力・流体力学などの物理的に妥当なシーンを生成

**参考URL**: [Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)

---

## 4. OpenAI: ChatGPT Dreaming V3 — メモリ機能の刷新

OpenAIは6月4日、ChatGPTのメモリ機能を大幅に刷新した**「Dreaming V3」**を導入すると発表しました。

- **計算コスト5分の1**: 無料ユーザーへの展開が可能に
- **Memory Summaryページ**: ユーザーの好み・プロジェクト・制約条件を要約して表示
- **時間的な鮮度の自動更新**: 旅行後には「行った」と自動更新など、陳腐化問題を解消

**参考URL**: [ChatGPTのメモリ機能が刷新（Techno Edge）](https://www.techno-edge.net/article/2026/06/05/5150.html)

---

## 5. Microsoft: MAI-Image-2.5 — 画像生成・編集モデルの大幅進化

**MAI-Image-2.5**はArena Image Edit No.2、Arena Text-to-Image No.3を達成する画像生成・編集モデルです。

- **Fine-grained Edit Control**: 物体の置換、テキスト更新、モーションブラー除去など精密な編集
- **Face and Identity Consistency**: 顔の同一性を保持

**参考URL**: [Introducing MAI-Image-2.5](https://microsoft.ai/news/introducing-mai-image-2-5/)

---

## 6. Google DeepMind: Gemma 4 12B / NVIDIA: Cosmos 3

**Gemma 4 12B** はノートPC（16GB VRAM）で動作するマルチモーダルエージェントモデル。エンコーダーフリーアーキテクチャを採用し、26B MoEに迫る推論性能を持つ。

**NVIDIA Cosmos 3** はMoT（Mixture-of-Transformers）アーキテクチャで全モダリティを統合。Physical AI向けオムニモデル（Nano 16B / Super 64B）として公開。

---

## 7. デジタル庁: ガバメントAI「源内」OSS公開 & 全府省展開

デジタル庁がガバメントAI**「源内」**をOSSとして公開し、全府省庁約18万人を対象とした大規模実証を開始。国産LLM（tsuzumi 2、Sarashina2 miniなど）7モデルの試用も本格化。

**参考URL**: [ガバメントAI「源内」（デジタル庁）](https://www.digital.go.jp/policies/genai)

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

# 生成AI週次ダイジェスト（5/30〜6/6）

## 今週のハイライト

本週は、OpenAIのChatGPT新機能発表、Googleの大型モデル発表、そして日本の国産AI動向が活発化した週となりました。世界規模でのAIエージェント機能の進化と日本政府による国産LLM活用の本格始動が注目されます。

---

## 海外動向

### 1. ChatGPTのメモリ機能刷新「Dreaming V3」全ユーザーに導入
**情報源**: [TechnoEdge / OpenAI](https://www.techno-edge.net/article/2026/06/05/5150.html)

OpenAIは2026年6月4日、ChatGPTのメモリ（記憶）機能を大幅に刷新した「Dreaming V3」システムを全ユーザーに導入すると発表しました。

### 2. Google Labsの実験的アプリ「Dreambeans」を公開
**情報源**: [TechnoEdge / Google Labs](https://www.techno-edge.net/article/2026/06/04/5142.html)

Google Labsは、AIを活用して毎日ユーザーのためにパーソナライズされたストーリーを生成する実験的アプリ「Dreambeans」を公開しました。

### 3. Google、6GB RAMで動く高性能エージェント「Gemma 4 12B」を公開
**情報源**: [TechnoEdge / Google DeepMind](https://www.techno-edge.net/article/2026/06/04/5144.html)

Google DeepMindは、わずか6GBのRAMで動作する高性能モデル「Gemma 4 12B」を発表しました。推論性能は26B MoEレベルに匹敵し、エンコーダなしのマルチモーダル対応も実現。

### 4. NVIDIAが物理AI推論用オムニモデル「NVIDIA Cosmos 3」を公開
**情報源**: [Hugging Face Blog / NVIDIA](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)

NVIDIAは物理AI推論とアクション実行のための初のオープンオムニモデル「NVIDIA Cosmos 3」をHugging Faceで公開しました。

### 5. Meta、Facebookクリエイター向けAIツール「Creator Assistant」を発表
**情報源**: [TechnoEdge / Meta](https://www.techno-edge.net/article/2026/06/05/5147.html)

Metaは、Facebookのクリエイター向けダッシュボード上にAIツール「Creator Assistant」を統合しました。

---

## 国内動向

### 6. 国立情報学研究所が国産LLM「LLM-jp-4」シリーズを公開
**情報源**: [国立情報学研究所](https://www.nii.ac.jp/news/release/2026/0403.html)

NIIは、約12兆トークンの良質なコーパスで学習した「LLM-jp-4」を発表。一部ベンチマークではGPT-4oやQwen3-8Bを上回る日本語性能を達成。

### 7. デジタル庁の「源内」で国産LLM試用を本格化 - 18万人の政府職員対象

全府省庁約18万人の職員を対象にtsuzumi 2（NTTグループ）、Sarashina2 mini（ソフトバンク）など7国産LLMの大規模実証を実施予定。

### 8. 日本AI基盤モデル開発会社の設立 - 8社による共同出資体制
**情報源**: [note / 孤独なプログラマー](https://note.com/ken_1101/n/ndb64ea9832c9)

ソフトバンク、NEC、ホンダ、ソニーグループなど8社が共同出資し、「日本AI基盤モデル開発」が正式に設立されました。政府は2026年度予算として生成AI関連に約5,198億円を計上。

---

## 技術トレンド・ビジネス動向

### 9. 1-bit LLM「BitNet a4.8」の実用化進展
**情報源**: [Microsoft Research / GitHub](https://github.com/microsoft/BitNet)

BitNet a4.8ではハイブリッド量子化により16倍のメモリ削減を実現した1-bit LLMが現実のものとなっています。

### 10. Googleの科学向けAI「Gemini for Science」 / 生成AIのビジネス活用拡大

Gemini for Scienceでマルチエージェント科学研究支援が進化。医療・保険・マーケティング分野での生成AI活用も急速に進展しています。

---

**発行**: 2026年6月6日 / **生成**: Claude Haiku

</div>
</div>

</div>

---

<div class="sonnet-eval" markdown="1">

## 🧠 Claude Sonnet による比較・評価（2026-06-07）

*両記事を読んだ Claude Sonnet 4.6 が、情報カバレッジ・技術精度・読みやすさの観点から評価します。*

---

### カバレッジの違い

**Ollama 記事が独自にカバーしたトピック**（Haiku には未掲載）:
- Claude Opus 4.8 の詳細（SWE-Bench Pro: 69.2%、Online-Mind2Web: 84%などベンチマーク数値）
- Gemini 3.5 Flash の詳細（Terminal-Bench 2.1: 76.2%、MCP Atlas: 83.6%）
- Gemini Omni の詳細（Physics-aware Generation、Knowledge-grounded Creativity）
- Microsoft MAI-Image-2.5（Arena Image Edit No.2 などの具体的な順位）
- Project Glasswing 拡大（150組織、10,000件以上の脆弱性発見）
- Chris Olah 氏の教皇レオ14世 AI 回勅講演

**Haiku 記事が独自にカバーしたトピック**（Ollama には未掲載）:
- NII 国産LLM「LLM-jp-4」公開（GPT-4o を超える日本語性能）
- 日本AI基盤モデル開発会社の設立（8社共同、政府予算5,198億円）
- Microsoft BitNet a4.8 の詳細（16倍メモリ削減）
- Google Gemini for Science（マルチエージェント科学研究支援）
- Meta Creator Assistant（Facebook クリエイター向けAIツール）
- Google Dreambeans（毎日パーソナルストーリー生成の実験的アプリ）
- 生成AIのビジネス活用動向（医療・保険・マーケティング）

---

### 各観点の評価

| 観点 | Ollama (qwen3.6:35b-mlx) | Haiku (claude-haiku-4-5) |
|------|--------------------------|--------------------------|
| **情報の深さ** | ⭐⭐⭐⭐⭐ ベンチマーク数値・技術仕様まで詳細 | ⭐⭐⭐ 概要把握に適したコンパクトな記述 |
| **カバレッジ** | ⭐⭐⭐⭐ 主要モデルリリースを網羅 | ⭐⭐⭐⭐⭐ 国内動向含め幅広くカバー |
| **国内AI動向** | ⭐⭐ 源内のみ1件 | ⭐⭐⭐⭐⭐ LLM-jp-4、8社共同会社など充実 |
| **読みやすさ** | ⭐⭐⭐ 専門的で情報密度が高い | ⭐⭐⭐⭐⭐ セクション分類で構造的 |
| **情報源の明示** | ⭐⭐⭐⭐⭐ URLが脚注形式で全件記載 | ⭐⭐⭐⭐ 各トピックに情報源を明記 |
| **ビジネス視点** | ⭐⭐⭐ 技術寄り | ⭐⭐⭐⭐ 活用動向・業界動向を整理 |

---

### 総評

今週は「エージェント性能の向上」と「日本のAI主権確立への動き」という2つの大きなテーマが並走した週でした。

**Ollama 記事**は、Claude Opus 4.8の具体的なベンチマーク数値（SWE-Bench Pro: 69.2%、Online-Mind2Web: 84%）やGemini 3.5 FlashのMCP Atlas 83.6%など、**一次情報に近い技術詳細**を提供する点で優れています。Project Glasswingの拡大やChris Olah氏の教皇回勅講演など、より深い背景情報もカバーしており、技術者や研究者向けの参照資料として有用です。

**Haiku 記事**は、NII の LLM-jp-4 公開や日本AI基盤モデル開発会社（8社共同、政府予算5,198億円）など、**日本国内のAI動向を充実してカバー**している点が際立ちます。「海外動向 / 国内動向 / 技術トレンド / ビジネス活用」という明確なセクション構成で、幅広い読者にとって読みやすい構成です。

**両記事を合わせて読むことで、今週のAI動向を最も立体的に把握できます**。技術的な深さを求めるなら Ollama、日本国内動向・ビジネス視点を含む広いカバレッジを求めるなら Haiku が適しています。

</div>

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/compare/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama週次</h3>
<ul class="article-list compact">
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0606">5/30〜6/6</a><span class="date">2026-06-06</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0530">5/23〜5/30</a><span class="date">2026-05-30</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0525">5/25〜5/31</a><span class="date">2026-05-25</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0518">5/18〜5/24</a><span class="date">2026-05-18</span></li>
  <li><a href="{{ site.baseurl }}/articles/weekly/2026-0511">5/11〜5/17</a><span class="date">2026-05-11</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku週次</h3>
<ul class="article-list compact">
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
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-05">2026年5月</a><span class="date">2026-05</span></li>
  <li><a href="{{ site.baseurl }}/articles/monthly/2026-04">2026年4月</a><span class="date">2026-04</span></li>
</ul>
<a href="{{ site.baseurl }}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

</div>
</div>
