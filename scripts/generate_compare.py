#!/opt/anaconda3/bin/python3
"""
generate_compare.py — 複数モデルの週次記事を並べた比較ページを生成する

メイン比較（2カラム）: Ollama（qwen3.6:35b-mlx） vs Claude Haiku
追加ローカルモデル（縦積み・任意）: articles/weekly_<variant>/ に記事があれば下段に追加
  - ornith   … ornith-1.5:35b（土曜 10:00 生成）
  - nemotron … nemotron-3.5-lightning:30b-mlx（土曜 11:00 生成）

Claude Sonnet による比較・評価は、その週に揃っている全モデルを対象にする。

使い方:
  python3 generate_compare.py \
    --week-file 0525 \
    --week-label "5/25〜5/31" \
    --year 2026
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
JST = timezone(timedelta(hours=9))
CLAUDE_BIN = str(Path.home() / ".local" / "bin" / "claude")

# 追加ローカルモデル（比較用サブモデル）の定義
#   key      : articles/weekly_<key>/ のディレクトリ接尾辞・CSSクラス接頭辞
#   badge    : パネルヘッダーのバッジ表記
#   model    : モデル名（表示用）
#   schedule : 生成タイミングの説明
VARIANT_MODELS = [
    {
        "key": "ornith",
        "badge": "🦉 ornith",
        "model": "ornith-1.5:35b",
        "schedule": "土曜 10:00 生成",
    },
    {
        "key": "nemotron",
        "badge": "🌩️ nemotron",
        "model": "nemotron-3.5-lightning:30b-mlx",
        "schedule": "土曜 11:00 生成",
    },
]


def log(msg: str) -> None:
    ts = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def strip_front_matter(content: str) -> str:
    """Jekyll front matter（--- ... ---）を除去して本文を返す"""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content.strip()


def extract_li_items(md_path: Path, limit: int = 5) -> str:
    """index.md から <li> エントリを最大 limit 件取得して文字列で返す"""
    if not md_path.exists():
        return ""
    lines = md_path.read_text(encoding="utf-8").split("\n")
    items = [l for l in lines if l.strip().startswith("<li>")]
    return "\n".join(items[:limit])


def insert_li_at_top_of_ul(md_path: Path, new_li: str) -> bool:
    """<ul class="article-list"> の直後に new_li を挿入する（重複チェック付き）"""
    if not md_path.exists():
        return False
    content = md_path.read_text(encoding="utf-8")
    if new_li.strip() in content:
        return False  # 既に存在する場合はスキップ
    lines = content.split("\n")
    result = []
    inserted = False
    for line in lines:
        result.append(line)
        if not inserted and line.strip() == '<ul class="article-list">':
            result.append(new_li)
            inserted = True
    if inserted:
        md_path.write_text("\n".join(result), encoding="utf-8")
    return inserted


def run_claude_cli_text(prompt: str, model: str = "sonnet", budget_usd: str = "1.00", timeout_sec: int = 600) -> str:
    """Claude Code CLI（Pro/Maxサブスクリプション）にプロンプトを渡し、応答テキストを返す。
    ANTHROPIC_API_KEY は明示的に除去し、APIクレジットではなくサブスク認証を強制する。"""
    env = os.environ.copy()
    env.pop("ANTHROPIC_API_KEY", None)
    env.pop("ANTHROPIC_BASE_URL", None)

    cmd = [
        CLAUDE_BIN,
        "--print",
        "--dangerously-skip-permissions",
        "--model", model,
        "--max-budget-usd", budget_usd,
        "--allowedTools", "",
        "--input-format", "text",
    ]
    result = subprocess.run(
        cmd, input=prompt, text=True, cwd=PROJECT_DIR, env=env,
        capture_output=True, timeout=timeout_sec,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude Code CLI が終了コード {result.returncode} で失敗: {result.stderr[:500]}")
    return result.stdout.strip()


# ------------------------------------------------------------------ #
# モデル情報の収集
# ------------------------------------------------------------------ #

def collect_models(week_file: str, year: str) -> list:
    """その週に揃っている全モデルの記事を読み込み、描画用の dict リストを返す。

    返す各要素: {css, badge, model, schedule, content}
      css   … CSSクラス接頭辞（ollama / haiku / ornith / nemotron）
    先頭2件（ollama / haiku）が無ければ空リストを返す（比較不成立）。
    """
    ollama_path = PROJECT_DIR / f"articles/weekly/{year}-{week_file}.md"
    haiku_path = PROJECT_DIR / f"articles/haiku_weekly/{year}-{week_file}.md"

    if not ollama_path.exists():
        log(f"SKIP: Ollama記事が存在しません: {ollama_path}")
        return []
    if not haiku_path.exists():
        log(f"SKIP: Haiku記事が存在しません: {haiku_path}")
        return []

    models = [
        {
            "css": "ollama",
            "badge": "🖥️ qwen3.6",
            "model": "qwen3.6:35b-mlx",
            "schedule": "土曜 09:00 生成",
            "content": strip_front_matter(ollama_path.read_text(encoding="utf-8")),
        },
        {
            "css": "haiku",
            "badge": "⚡ Claude Haiku",
            "model": "claude-haiku-4-5",
            "schedule": "土曜 13:00 生成",
            "content": strip_front_matter(haiku_path.read_text(encoding="utf-8")),
        },
    ]

    for v in VARIANT_MODELS:
        vpath = PROJECT_DIR / f"articles/weekly_{v['key']}/{year}-{week_file}.md"
        if vpath.exists():
            models.append({
                "css": v["key"],
                "badge": v["badge"],
                "model": v["model"],
                "schedule": v["schedule"],
                "content": strip_front_matter(vpath.read_text(encoding="utf-8")),
            })
            log(f"追加モデルを検出: {v['key']} ({vpath.name})")
        else:
            log(f"追加モデルなし（スキップ）: {v['key']}")

    return models


# ------------------------------------------------------------------ #
# Markdown ブロック生成
# ------------------------------------------------------------------ #

def _panel(m: dict) -> str:
    return f"""<div class="compare-panel {m['css']}-panel">
<div class="panel-header-bar">
  <span class="model-badge">{m['badge']}</span>
  <span class="model-name">{m['model']}</span>
</div>
<div class="panel-body" markdown="1">

{m['content']}

</div>
</div>"""


def build_compare_block(models: list, week_label: str, sonnet_eval_section: str) -> str:
    """比較ヘッダー + メイン2カラム + 追加モデル縦積み + Sonnet評価 をまとめた Markdown を返す。"""
    main_models = models[:2]      # ollama / haiku
    extra_models = models[2:]     # ornith / nemotron ...

    meta_badges = [
        '<span class="badge ollama">🖥️ qwen3.6</span> '
        '<span style="font-family:monospace;font-size:0.82rem;color:#666">qwen3.6:35b-mlx（土曜 09:00 生成）</span>',
        '<span style="margin: 0 0.5rem;">vs</span>',
        '<span class="badge haiku">⚡ Claude</span> '
        '<span style="font-family:monospace;font-size:0.82rem;color:#666">claude-haiku-4-5（土曜 13:00 生成）</span>',
    ]
    for m in extra_models:
        meta_badges.append(
            f'<span class="badge {m["css"]}">{m["badge"]}</span> '
            f'<span style="font-family:monospace;font-size:0.82rem;color:#666">{m["model"]}（{m["schedule"]}）</span>'
        )
    meta_html = "\n    ".join(meta_badges)

    main_panels = "\n\n".join(_panel(m) for m in main_models)

    extra_block = ""
    if extra_models:
        extra_panels = "\n\n".join(_panel(m) for m in extra_models)
        extra_block = f"""
<div class="compare-extra-header">
  <h2>🧩 追加ローカルモデル（比較用）</h2>
  <p>メイン比較と同じ週・同じ収集条件で、別のローカルLLMが生成した週次まとめです。</p>
</div>

<div class="compare-extra">

{extra_panels}

</div>
"""

    return f"""<div class="compare-header">
  <h1>🔬 モデル比較（{week_label}）</h1>
  <div class="compare-meta">
    {meta_html}
  </div>
</div>

<div class="compare-wrapper">

{main_panels}

</div>
{extra_block}
{sonnet_eval_section}"""


# ------------------------------------------------------------------ #
# Sonnet 評価
# ------------------------------------------------------------------ #

def generate_sonnet_eval(models: list, week_label: str) -> str:
    """Claude Sonnet（Claude Code CLI経由）で全モデルの記事を評価し、
    sonnet-evalセクションのMarkdownを返す。"""
    today_str = datetime.now(JST).strftime("%Y-%m-%d")

    # 記事本文セクション
    article_sections = []
    for m in models:
        article_sections.append(
            f"## {m['badge']} 記事（{m['model']} 生成）\n\n{m['content']}"
        )
    articles_md = "\n\n---\n\n".join(article_sections)

    # 評価表のヘッダー行（モデルごとに1列）
    header_cols = " | ".join(f"**{m['badge']}**<br>{m['model']}" for m in models)
    sep_cols = "|".join(["------"] * (len(models) + 1))
    model_list_str = "、".join(f"{m['badge']}（{m['model']}）" for m in models)

    prompt = f"""以下の {len(models)} つの生成AIニュース週次まとめ記事（{week_label}）を読んで、比較・評価を行ってください。
いずれも同じ週・同じ収集条件で、異なるモデルが生成したものです。

対象モデル: {model_list_str}

---

{articles_md}

---

以下の形式で出力してください。HTMLタグは使わず、Markdown記法のみで記述してください。
（表のヘッダー行のみ、指定どおり `<br>` を含めてそのまま使ってください）

### カバレッジの違い

各モデルが「独自にカバーしたトピック」（他モデルには未掲載のもの）を、モデルごとに箇条書きで列挙してください。

- **{models[0]['badge']}**: （箇条書き）
- **{models[1]['badge']}**: （箇条書き）
{chr(10).join(f"- **{m['badge']}**: （箇条書き）" for m in models[2:])}

---

### 各観点の評価

| 観点 | {header_cols} |
|{sep_cols}|
| **情報の深さ** | {" | ".join(["⭐×N 説明"] * len(models))} |
| **カバレッジ** | {" | ".join(["⭐×N 説明"] * len(models))} |
| **国内AI動向** | {" | ".join(["⭐×N 説明"] * len(models))} |
| **読みやすさ** | {" | ".join(["⭐×N 説明"] * len(models))} |
| **情報源の明示** | {" | ".join(["⭐×N 説明"] * len(models))} |
| **ビジネス視点** | {" | ".join(["⭐×N 説明"] * len(models))} |

---

### 総評

（300〜400字程度。今週の特徴的なテーマ、各モデルの強み・弱みを端的に述べ、
特にローカルモデル同士（Ollama系）の違いに触れること。
「各記事を合わせて読むことで〜」という締め方で締める）
"""

    eval_body = run_claude_cli_text(prompt, model="sonnet", budget_usd="1.00")

    return f"""<div class="sonnet-eval" markdown="1">

## 🧠 Claude Sonnet による比較・評価（{today_str}）

*その週に揃った全モデルの記事を読んだ Claude Sonnet が、情報カバレッジ・技術精度・読みやすさの観点から評価します。*

---

{eval_body}

</div>"""


# ------------------------------------------------------------------ #
# トップページ更新
# ------------------------------------------------------------------ #

def update_top_page(
    week_label: str,
    models: list,
    sonnet_eval_section: str = "",
) -> None:
    """index.md を最新比較コンテンツ + 過去記事グリッドで完全に書き換える"""

    compare_items = extract_li_items(PROJECT_DIR / "articles/compare/index.md")
    weekly_items  = extract_li_items(PROJECT_DIR / "articles/weekly/index.md")
    haiku_items   = extract_li_items(PROJECT_DIR / "articles/haiku_weekly/index.md")
    monthly_items = extract_li_items(PROJECT_DIR / "articles/monthly/index.md")

    # Liquid の {{ }} は f-string と衝突するので {{ }} にエスケープ
    baseurl = "{{ site.baseurl }}"

    compare_block = build_compare_block(models, week_label, sonnet_eval_section)

    index_md = f"""---
layout: compare
title: 生成AI週次ダイジェスト
---

{compare_block}

<div class="past-articles">
<h2>📚 過去の記事</h2>
<div class="past-articles-grid">

<div class="past-col">
<h3>🔬 モデル比較</h3>
<ul class="article-list compact">
{compare_items}
</ul>
<a href="{baseurl}/articles/compare/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>🖥️ Ollama週次</h3>
<ul class="article-list compact">
{weekly_items}
</ul>
<a href="{baseurl}/articles/weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>⚡ Haiku週次</h3>
<ul class="article-list compact">
{haiku_items}
</ul>
<a href="{baseurl}/articles/haiku_weekly/" class="view-all">すべて見る →</a>
</div>

<div class="past-col">
<h3>📅 月次まとめ</h3>
<ul class="article-list compact">
{monthly_items}
</ul>
<a href="{baseurl}/articles/monthly/" class="view-all">すべて見る →</a>
</div>

</div>
</div>
"""

    (PROJECT_DIR / "index.md").write_text(index_md, encoding="utf-8")
    log(f"index.md をトップ比較ページとして更新: {week_label}")


# ------------------------------------------------------------------ #
# メイン処理
# ------------------------------------------------------------------ #

def generate(week_file: str, week_label: str, year: str) -> bool:
    compare_path = PROJECT_DIR / f"articles/compare/{year}-{week_file}.md"
    compare_index = PROJECT_DIR / "articles/compare/index.md"

    models = collect_models(week_file, year)
    if not models:
        return False

    model_names = " / ".join(m["css"] for m in models)
    log(f"比較対象モデル: {model_names}")

    # Sonnet評価生成
    log("Claude Sonnet で評価文を生成中...")
    try:
        sonnet_eval_section = generate_sonnet_eval(models, week_label)
        log("Sonnet評価生成完了")
    except Exception as e:
        log(f"WARN: Sonnet評価生成に失敗しました: {e}")
        sonnet_eval_section = ""

    compare_block = build_compare_block(models, week_label, sonnet_eval_section)

    # 比較ページ（articles/compare/YYYY-MMDD.md）
    if not compare_path.exists():
        compare_md = f"""---
layout: compare
title: モデル比較（{week_label}）
---

{compare_block}
"""
        compare_path.parent.mkdir(parents=True, exist_ok=True)
        compare_path.write_text(compare_md, encoding="utf-8")
        log(f"比較ページ生成完了: {compare_path}")
    else:
        log(f"比較ページは既に存在します（スキップ）: {compare_path}")

    # articles/compare/index.md を更新
    date_str = f"{year}-{week_file[:2]}-{week_file[2:]}"
    href = f"articles/compare/{year}-{week_file}"
    li = (
        f'  <li><a href="{{{{ site.baseurl }}}}/{href}">'
        f'{week_label}</a><span class="date">{date_str}</span></li>'
    )
    if insert_li_at_top_of_ul(compare_index, li):
        log("articles/compare/index.md 更新完了")

    # トップページを最新比較コンテンツで完全書き換え
    update_top_page(week_label, models, sonnet_eval_section)

    # git commit & push
    files = [
        f"articles/compare/{year}-{week_file}.md",
        "articles/compare/index.md",
        "index.md",
    ]
    # 追加モデルの記事ファイルも（存在すれば）コミット対象に含める
    for v in VARIANT_MODELS:
        vrel = f"articles/weekly_{v['key']}/{year}-{week_file}.md"
        if (PROJECT_DIR / vrel).exists():
            files.append(vrel)

    commit_msg = (
        f"{year}-{week_file} モデル比較ページを追加・トップページを更新\n\n"
        f"対象モデル: {model_names}\n\n"
        f"Co-Authored-By: generate_compare.py <noreply@local>"
    )
    try:
        for f in files:
            subprocess.run(["git", "add", f], cwd=PROJECT_DIR, check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=PROJECT_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_DIR, check=True)
        log("git commit & push 完了")
    except subprocess.CalledProcessError as e:
        log(f"git エラー: {e}")
        return False

    return True


def main():
    parser = argparse.ArgumentParser(description="複数モデル 週次比較ページ生成")
    parser.add_argument("--week-file",  required=True, help="MMDD形式（例: 0525）")
    parser.add_argument("--week-label", required=True, help="例: 5/25〜5/31")
    parser.add_argument("--year",       required=True, help="例: 2026")
    args = parser.parse_args()

    success = generate(args.week_file, args.week_label, args.year)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
