#!/opt/anaconda3/bin/python3
"""
generate_compare.py — Ollama記事とHaiku記事を並べた比較ページを生成する

使い方:
  python3 generate_compare.py \
    --week-file 0525 \
    --week-label "5/25〜5/31" \
    --year 2026
"""

import argparse
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
JST = timezone(timedelta(hours=9))


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


def insert_li_at_top_of_ul(md_path: Path, new_li: str) -> bool:
    """<ul class="article-list"> の直後に new_li を挿入する"""
    if not md_path.exists():
        return False
    lines = md_path.read_text(encoding="utf-8").split("\n")
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


def update_top_index(week_label: str, week_file: str, year: str) -> None:
    """トップページ (index.md) の比較リストに新しいエントリを追加する"""
    top = PROJECT_DIR / "index.md"
    if not top.exists():
        return

    # 比較リンクのフォーマット
    date_str = f"{year}-{week_file[:2]}-{week_file[2:]}"
    href = f"articles/compare/{year}-{week_file}"
    li = (
        f'  <li><a href="{{{{ site.baseurl }}}}/{href}">'
        f'{week_label}</a><span class="date">{date_str}</span></li>'
    )

    lines = top.read_text(encoding="utf-8").split("\n")
    out = []
    in_compare = False
    compare_done = False

    for line in lines:
        out.append(line)
        if '<h2 class="section-title">' in line:
            in_compare = "🔬 モデル比較" in line
        if in_compare and not compare_done and line.strip() == '<ul class="article-list" id="compare-list">':
            out.append(li)
            compare_done = True

    if compare_done:
        top.write_text("\n".join(out), encoding="utf-8")
        log(f"index.md 比較セクション更新: {week_label}")


def generate(week_file: str, week_label: str, year: str) -> bool:
    ollama_path = PROJECT_DIR / f"articles/weekly/{year}-{week_file}.md"
    haiku_path  = PROJECT_DIR / f"articles/haiku_weekly/{year}-{week_file}.md"
    compare_path = PROJECT_DIR / f"articles/compare/{year}-{week_file}.md"
    compare_index = PROJECT_DIR / "articles/compare/index.md"

    if not ollama_path.exists():
        log(f"SKIP: Ollama記事が存在しません: {ollama_path}")
        return False
    if not haiku_path.exists():
        log(f"SKIP: Haiku記事が存在しません: {haiku_path}")
        return False
    if compare_path.exists():
        log(f"SKIP: 比較ページは既に存在します: {compare_path}")
        return False

    ollama_content = strip_front_matter(ollama_path.read_text(encoding="utf-8"))
    haiku_content  = strip_front_matter(haiku_path.read_text(encoding="utf-8"))

    compare_md = f"""---
layout: compare
title: モデル比較（{week_label}）
---

<div class="compare-header">
  <h1>🔬 モデル比較（{week_label}）</h1>
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

{ollama_content}

</div>
</div>

<div class="compare-panel haiku-panel">
<div class="panel-header-bar">
  <span class="model-badge">⚡ Claude Haiku</span>
  <span class="model-name">claude-haiku-4-5</span>
</div>
<div class="panel-body" markdown="1">

{haiku_content}

</div>
</div>

</div>
"""

    compare_path.parent.mkdir(parents=True, exist_ok=True)
    compare_path.write_text(compare_md, encoding="utf-8")
    log(f"比較ページ生成完了: {compare_path}")

    # articles/compare/index.md を更新
    date_str = f"{year}-{week_file[:2]}-{week_file[2:]}"
    href = f"articles/compare/{year}-{week_file}"
    li = (
        f'  <li><a href="{{{{ site.baseurl }}}}/{href}">'
        f'{week_label}</a><span class="date">{date_str}</span></li>'
    )
    if insert_li_at_top_of_ul(compare_index, li):
        log(f"articles/compare/index.md 更新完了")

    # トップ index.md の比較セクションを更新
    update_top_index(week_label, week_file, year)

    # git commit & push
    files = [
        f"articles/compare/{year}-{week_file}.md",
        "articles/compare/index.md",
        "index.md",
    ]
    commit_msg = (
        f"{year}-{week_file} モデル比較ページを追加\n\n"
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
    parser = argparse.ArgumentParser(description="Ollama vs Haiku 比較ページ生成")
    parser.add_argument("--week-file",  required=True, help="MMDD形式（例: 0525）")
    parser.add_argument("--week-label", required=True, help="例: 5/25〜5/31")
    parser.add_argument("--year",       required=True, help="例: 2026")
    args = parser.parse_args()

    success = generate(args.week_file, args.week_label, args.year)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
