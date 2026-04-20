# SPEC.md — 情報収集・記事生成仕様

最終更新: 2026-03-26（日本国内情報ソース見直し）

---

## 収集対象

### 主要情報源

| カテゴリ | サイト・URL | 収集内容 |
|---|---|---|
| モデルリリース | OpenAI Blog / Anthropic News / Google DeepMind Blog | 新モデル・機能発表 |
| 研究論文 | arXiv (cs.AI, cs.CL, cs.LG) / Hugging Face Papers | 注目論文のアブスト |
| ビジネス動向 | TechCrunch / VentureBeat / The Information | 資金調達・提携・動向 |
| 国内情報（メディア） | ITmedia AI+ / ASCII.jp / Impress Watch / 日経クロステック / CNET Japan | 日本語AI情報全般 |
| 国内情報（政府・公式） | デジタル庁ニュース（digital.go.jp/news）/ 内閣府AI戦略 / 経産省AI政策 / 総務省 | 政策・ガイドライン・実証事業 |
| 国内情報（研究機関） | NEDO / JST / 理研 / 産総研 | 研究開発・補助金採択 |
| 国内情報（企業動向） | 各社プレスリリース・IRニュース（WebSearchで横断収集） | 国内AI企業の製品・研究動向 |
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

#### 1.5 1ビット・超低ビット量子化LLM（優先収集）
- **対象**: 重みを1ビットまたは1.58ビットに量子化した超軽量LLM。CPU・NPUでの推論が現実的になるアーキテクチャ
- **注目モデル**: Microsoft Research「BitNet」シリーズ（BitNet b1.58 / BitNet 3B）・**Bonsai**（1ビットLLM）・その他1bit量子化モデル
- **注目点**: 推論速度・メモリ使用量・精度劣化の程度・CPU推論の実用性
- **情報源（直接確認）**:
  - Microsoft Research Blog: https://www.microsoft.com/en-us/research/blog/
  - arXiv（cs.CL / cs.LG）: `bitnet`, `1-bit LLM`, `binary LLM`, `Bonsai LLM`
  - Hugging Face Blog: https://huggingface.co/blog
- **キーワード**: `1-bit LLM`, `BitNet`, `Bonsai LLM`, `1ビットLLM`, `binary quantization LLM`,
  `超低ビット量子化`, `CPU推論 LLM`, `Microsoft Research LLM`

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
- **注目点**: 国産AI選定状況・令和8年度試行・調達・セキュリティ方針
- **情報源（直接確認）**:
  - デジタル庁ニュース: https://www.digital.go.jp/news/
  - 経産省AIポリシー: https://www.meti.go.jp/policy/it_policy/ai/
  - 内閣府AI戦略: https://www8.cao.go.jp/cstp/ai/
  - NISC: https://www.nisc.go.jp/
- **キーワード**: `デジタル庁 生成AI`, `国産AI 選定 令和8年度`, `行政 LLM 試行`, `自治体 生成AI導入`,
  `政府 AI調達`, `内閣府 AI戦略`

#### 5. 日本のAI企業・研究動向
- **対象**: 国内のAI研究機関・スタートアップ・大企業のAI部門
- **注目企業（例示・偏り禁止）**:
  - スタートアップ: Sakana AI / ELYZA / Rinna / AI Shift / Lightblue
  - 大手テック: 楽天（RakutenAI）/ ソフトバンク（SB Intuitions）/ KDDI / さくらインターネット
  - 研究機関・大手: PFN（Preferred Networks）/ NTT / NEC / 富士通 / サイバーエージェント AI Lab
- **注意**: 特定企業だけをクローズアップせず、その週に動きのあった企業を幅広く収録する
- **キーワード**: `日本 生成AI 企業 最新`, `国産LLM リリース`, `RakutenAI 楽天AI`,
  `日本 AI スタートアップ 資金調達`, `ELYZA SB Intuitions PFN`

---

## 記事フォーマット

### 週次まとめ（articles/weekly/YYYY-MMDD.md）

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

### トピックス（articles/topics/YYYY-MM-DD_slug.md）

週次・月次とは別に、特定テーマを深掘りする単発レポート。手動作成またはユーザー指示で生成する。

```markdown
# 【トピックス】[タイトル]

> 作成: YYYY-MM-DD | カテゴリ: [カテゴリ] | タグ: `タグ1`, `タグ2`

---

## 概要

（200〜300字のリード文）

---

## 技術背景 / 経緯

（詳細な解説）

---

## [主要セクション1]

（深掘り内容）

---

## [主要セクション2]

（深掘り内容）

---

## 現状の課題

（課題の整理）

---

## 今後の展望

（今後の注目点・見通し）

---

## まとめ

（総括）

---

*関連週次まとめ: [リンク]*
```

---

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
