# SPEC.md — 情報収集・記事生成仕様

最終更新: 2026-03-26（注目トピック追加）

---

## 収集対象

### 主要情報源

| カテゴリ | サイト・URL | 収集内容 |
|---|---|---|
| モデルリリース | OpenAI Blog / Anthropic News / Google DeepMind Blog | 新モデル・機能発表 |
| 研究論文 | arXiv (cs.AI, cs.CL, cs.LG) / Hugging Face Papers | 注目論文のアブスト |
| ビジネス動向 | TechCrunch / VentureBeat / The Information | 資金調達・提携・動向 |
| 国内情報（一般） | ASCII.jp / ITmedia AI+ / Impress Watch / AINOW | 日本語AI情報 |
| 国内情報（スタートアップ） | Sakana AI Blog / PFN Blog / SB Intuitions / さくらインターネット | 国内AI企業の研究・製品動向 |
| 国内情報（政府・研究機関） | デジタル庁 / 総務省 / 経産省 / NEDO / JST | 政策・研究開発・補助金 |
| コミュニティ | Hacker News (AI関連) / Reddit r/MachineLearning | コミュニティ反応 |
| 規制・政策 | 総務省 / 経産省 / EU AI Act 関連 | 法規制・ガイドライン |

### 収集フィルター

以下のキーワードを中心に情報を収集する:
- `LLM`, `大規模言語モデル`, `GPT`, `Claude`, `Gemini`, `Llama`, `Mistral`
- `生成AI`, `Generative AI`, `Foundation Model`
- `マルチモーダル`, `エージェント`, `RAG`, `ファインチューニング`
- `AI規制`, `AI安全`, `AI倫理`
- `画像生成`, `動画生成`, `音声合成`

### 特に注目しているトピック（優先収集・必ず記事に含める）

#### 1. ローカル動作する小型LLM
- **対象**: Llama / Gemma / Phi / Qwen / Mistral Small / DeepSeek 等のオンデバイスモデル
- **注目点**: モデルサイズ（パラメータ数）・量子化（GGUF/GPTQ）・ベンチマーク性能
- **ツール**: Ollama / LM Studio / llama.cpp / MLX（Apple Silicon）
- **キーワード**: `ローカルLLM`, `edge AI`, `on-device`, `小型モデル`, `量子化`, `Ollama`

#### 2. AIエージェントの動向
- **対象**: 自律エージェント・マルチエージェント・ツール呼び出し・ワークフロー自動化
- **注目点**: フレームワーク比較・実用事例・精度・コスト・安全性
- **ツール**: LangGraph / AutoGen / CrewAI / MCP（Model Context Protocol）/ OpenAI Agents SDK
- **キーワード**: `AIエージェント`, `agentic AI`, `MCP`, `マルチエージェント`, `autonomous agent`

#### 3. 生成AIを動かせるPC・ハードウェア
- **対象**: GPU/NPU搭載PC・Apple Silicon・NVIDIA GeForce / RTX / GB200・AMD Radeon AI
- **注目点**: VRAM容量・推論速度・消費電力・価格帯・ローカルLLMとの相性
- **メーカー**: NVIDIA / AMD / Intel / Apple / Qualcomm（Snapdragon X）
- **キーワード**: `AI PC`, `NPU`, `ローカルAI 推奨スペック`, `RTX AI`, `Apple Silicon LLM`

#### 4. 日本政府・行政機関の生成AI活用
- **対象**: 各省庁・自治体・デジタル庁・内閣府の生成AI導入・実証実験・ガイドライン
- **注目点**: 調達状況・活用事例・セキュリティ方針・国産LLM活用の動き
- **情報源**: デジタル庁 / 総務省 / 経産省 / 内閣サイバーセキュリティセンター（NISC）
- **キーワード**: `デジタル庁 生成AI`, `行政 AI活用`, `政府 ChatGPT`, `自治体 生成AI`, `国産LLM`

#### 5. 日本のAI企業・研究動向（重点収集）
- **対象**: 国内のAI研究機関・スタートアップ・大企業のAI部門
- **注目企業**: Sakana AI / PFN（Preferred Networks）/ SB Intuitions / さくらインターネット /
  Rinna / AI Shift / ELYZA / cyberagent AI Lab / NTT / 富士通 / NEC
- **注目点**: 新モデルリリース・論文発表・資金調達・製品リリース・産学連携
- **キーワード**: `Sakana AI`, `PFN AI`, `国産LLM`, `日本 生成AI スタートアップ`, `ELYZA`, `SB Intuitions`

---

## 記事フォーマット

### 週次まとめ（articles/weekly/YYYY-WXX.md）

```markdown
# 生成AI週次ダイジェスト（MM/DD〜MM/DD）

> 自動生成: YYYY-MM-DD | 対象期間: YYYY-MM-DD 〜 YYYY-MM-DD

## 今週のハイライト

1. **[タイトル]** — 1〜2行の要点
2. **[タイトル]** — 1〜2行の要点
3. **[タイトル]** — 1〜2行の要点

---

## 🤖 モデル・技術リリース

### [モデル名・技術名]
- **発表元**: XXX
- **概要**: 〜
- **ポイント**: 〜
- 参照: [リンク]

---

## 📄 注目論文

### [論文タイトル（日本語訳）]
- **著者/機関**: XXX
- **概要**: 〜
- **意義**: 〜
- arXiv: [リンク]

---

## 🏢 ビジネス・業界動向

- **[企業名]**: 〜
- **[企業名]**: 〜

---

## 🛠️ ツール・OSS

- **[ツール名]**: 〜（GitHub: [リンク]）

---

## 🇯🇵 国内動向

> 国内企業・政府・研究機関の動向を必ず収録すること。Sakana AI / PFN / ELYZA 等の
> 日本のAI企業の動向を個別に検索して含めること。

### 国内AI企業・研究

- **[企業/機関名]**: 〜（参照: [日本語タイトル or 英語タイトル（日本語訳）](URL)）

### 政府・行政

- **[省庁/自治体名]**: 〜

---

## 📜 規制・政策

- 〜

---

## 編集後記

今週の総括と来週の注目点。
```

### 月次まとめ（articles/monthly/YYYY-MM.md）

```markdown
# 生成AI月次ダイジェスト YYYY年MM月

> 自動生成: YYYY-MM-DD | 対象期間: YYYY-MM-01 〜 YYYY-MM-末日

## 月のサマリー

YYYY年MM月の生成AI分野の主要動向を要約（3〜5段落）。

## 主要トピック

### 1. [トピックタイトル]
詳細な解説（300〜500字程度）

### 2. [トピックタイトル]
詳細な解説

（以下続く）

---

## 統計・数字で見る今月

- 📦 主要モデルリリース数: X件
- 📄 注目論文数: X件
- 💰 主要資金調達: X件（合計約XXX億円）

---

## 来月の注目点

- 〜
- 〜

---

## 今月の週次まとめリンク

| 週 | リンク |
|---|---|
| W01 | [YYYY-W01](../weekly/YYYY-W01.md) |
```

---

## 自動実行フロー

```
launchd（毎週月曜 09:00）
  └─ run_ai_news.sh
       ├─ 日付判定（第1月曜か否か）
       ├─ claude CLI 起動
       │    └─ CLAUDE.md の指示に従い記事生成
       │         ├─ WebSearch で最新情報を収集
       │         ├─ 記事ファイルを生成（Write）
       │         └─ README.md のリンク一覧を更新（Edit）
       └─ git add / commit / push
```

---

## 品質基準

- 情報ソースのURLを必ず記載する
- 推測・憶測は「〜とみられる」「〜の可能性がある」と明示する
- 週次まとめ: 最低5トピック以上
- 月次まとめ: 最低3つの主要トピックを深掘り
- 日本語で記述（技術用語・モデル名は原語のまま）
