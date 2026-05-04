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

- [5/4〜5/10](./articles/weekly/2026-0504.md)
- [4/27〜5/3](./articles/weekly/2026-0427.md)
- [4/21〜4/27](./articles/weekly/2026-0421.md)
- [4/14〜4/20](./articles/weekly/2026-0420.md)
- [4/13〜4/19](./articles/weekly/2026-0413.md)
- [4/6〜4/12](./articles/weekly/2026-0406.md)
- [3/30〜4/5](./articles/weekly/2026-0330.md)
- [3/23〜3/29](./articles/weekly/2026-0323.md)

<!-- articles/weekly/ のファイルへのリンクがここに追加される -->

### 月次まとめ

- [2026年5月](./articles/monthly/2026-05.md)
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

# 生成AI週次ダイジェスト（5/4〜5/10）

> 自動生成: 2026-05-04 | 対象期間: 2026-04-28 〜 2026-05-04

## 今週のハイライト

1. **Anthropic、評価額9,000億ドル超で50億ドル調達を検討 — OpenAI抜き世界最高評価AIスタートアップへ** — 年間換算売上高300〜400億ドルを背景に、複数の投資家から最大9,000億ドル超の評価額で約500億ドルの資金調達案が浮上。成立すれば直近評価額8,500億ドルのOpenAIを上回る。
2. **米国防総省がAI7社と機密ネットワーク協定（5/1）— Anthropicは安全条件で除外** — AWS・Google・Microsoft・Nvidia・OpenAI・SpaceX・Reflectionが協定に署名。Anthropicは完全自律型兵器への安全ガードレール条件をペンタゴンが拒否したとして交渉決裂。
3. **Microsoft Agent 365がGA（5/1）— AIエージェント統制基盤が正式提供** — 月額$15/ユーザーの独立プランと、M365 E7($99)へのバンドルで提供開始。AIエージェントの「観測・統制・保護」を統合する企業向け管理基盤が整備された。

---

## 🤖 モデル・技術リリース

### Claude Opus 4.7 — SWE-Bench Pro 64.3%達成・高解像度ビジョン対応

- **発表元**: Anthropic
- **公開日**: 2026年5月（GA）
- **概要**: Claude Opus 4.7が正式一般提供（GA）開始。SWE-Bench Pro（実際のGitHubイシュー解決）で64.3%を達成し、GPT-5.5の58.6%を上回る。ビジョン機能が大幅向上し、より高解像度の画像認識が可能になった。価格はOpus 4.6と同じ入力$5/出力$25 per 1Mトークン。
- **ポイント**: 「最も難しいコーディング作業を安心して委託できる」という位置づけで、長時間タスクでの一貫性と精確な指示遵守が改善。Adobe・Blender・Ableton・Affinity・Autodesk Fusionとのコネクタも追加。
- 参照: [Introducing Claude Opus 4.7（Anthropic公式）](https://www.anthropic.com/news/claude-opus-4-7)

### Qwen 3.6 — MoE・201言語・Apple Silicon対応のオープンモデル（4月）

- **発表元**: Alibaba Qwen Team
- **概要**: MoE（Mixture of Experts）アーキテクチャを採用し、201言語・方言をサポートする最新世代オープンモデル。llama.cpp・mlx-lm（Apple Silicon向け）でのローカル実行をサポートし、128Kコンテキスト（YaRN）対応。
- 参照: [Qwen3.6（GitHub）](https://github.com/QwenLM/Qwen3.6)

---

## 🏢 ビジネス・業界動向

- **Anthropic** — 評価額9,000億ドル超での50億ドル調達を検討。年間換算売上高は300〜400億ドルに急拡大し、Googleが最大400億ドル・Amazonが最大250億ドルを既に表明。参照: [Anthropic in talks at $900B valuation（TechCrunch）](https://techcrunch.com/2026/04/29/sources-anthropic-could-raise-a-new-50b-round-at-a-valuation-of-900b/)
- **Pentagon** — AWS・Google・Microsoft・Nvidia・OpenAI・SpaceX・Reflection・Oracleの8社とAI機密ネットワーク協定を締結。Anthropicは安全ガードレール条件で除外。参照: [Pentagon strikes deals with 7 Big Tech companies（CNN）](https://www.cnn.com/2026/05/01/tech/pentagon-ai-anthropic)
- **Microsoft** — Agent 365が5月1日にGA。エンタープライズAIエージェント管理基盤として月額$15/ユーザーで提供開始。参照: [Microsoft Agent 365 GA（Microsoft Security Blog）](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)

---

## 🛠️ ツール・OSS

- **Qwen-Scope（5/1）** — Alibaba QwenがQwen3/3.5向け14種のスパースオートエンコーダ（SAE）OSSスイートを公開。モデル解釈可能性・推論時出力制御のツール。参照: [Qwen-Scope公開（Dev|Journal）](https://earezki.com/ai-news/2026-05-01-qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/)

---

## 🇯🇵 国内動向

### 政府・行政

- **デジタル庁「源内」5月実証開始** — 全府省庁39機関・約18万人の国家公務員を対象とした国産LLM7件の大規模実証が2026年5月に正式スタート。8月頃から本格試用・2027年1月に評価結果公表予定。参照: [デジタル庁が国産AI「7人の侍」選定（SBビジネス）](https://www.sbbit.jp/article/cont1/182108)

### 企業・研究機関

- **PFN・さくらインターネット・NICT** — PLaMo 2.0後継モデルの共同開発が継続中。NICTデータとPFN独自合成データを活用した日本語特化LLMをさくらプラットフォームで提供計画。参照: [PFN・さくら・NICT 基本合意（さくらインターネット）](https://www.sakura.ad.jp/corporate/information/newsreleases/2025/09/18/1968220920/)

---

## 📜 規制・政策

- **EU AI Act GPAI全面適用（8月2日）** — EU AI ActのGPAI規制が8月2日に全面施行。日本企業もEU向けAIシステム提供時は対応必須。参照: [EU AI規制法の解説（PwC Japan）](https://www.pwc.com/jp/ja/knowledge/column/awareness-cyber-security/generative-ai-regulation10.html)
- **米AI安保政策** — Anthropicが安全基準を理由に軍事契約を断った唯一の大手AIラボとしてガバナンスの試金石に。

---

## 📰 Note注目記事

- **「国内AIエージェント動向(2026/5/1号)」** — 実業務フェーズに移行したAIエージェントの最新展開をPEST分析で整理。参照: [note / Yasuhito Morimoto](https://note.com/yasuhitoo/n/na9c8d890db85)
- **「AIエージェントは、ついにIT資産になった」** — エージェントが「実験的ツール」から「管理すべきIT資産」に変わった転換点を論じる注目記事。参照: [note / hirokaji](https://note.com/tasty_dunlin998/n/nf232c430a697)

---

## 編集後記

今週の最大のテーマは「Anthropicの台頭と孤立」の二面性だ。評価額9,000億ドル超・年間換算売上高400億ドルという数字はOpenAIを上回る勢いを示す一方、ペンタゴンとの契約を安全基準を理由に断ったAnthropicのスタンスは、AI倫理と安全保障のトレードオフが現実の商業的選択として顕在化した最初のケースとなった。

国内では5月から始まるガバメントAI「源内」の実証が静かに動き出す。18万人という規模と国産LLM7件という選択肢の多様さは、日本の行政AI導入が評価・選定フェーズに入ったことを意味する。2027年1月の評価公表まで、どのモデルがどの行政業務に適合するかが注目される。
