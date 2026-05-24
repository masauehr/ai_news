#!/opt/anaconda3/bin/python3
"""
local_agent.py — Ollama tool-calling エージェントで ai_news 記事を自動生成する

使い方（run_ai_news.sh から呼ばれる）:
  python3 local_agent.py \
    --mode weekly|monthly \
    --week-file 0525 \
    --week-label "5/25〜5/31" \
    --year 2026 \
    --month 05 \
    [--prefetch "事前収集済みテキスト"]
    [--model qwen3.6:35b-mlx]
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
from ddgs import DDGS
import trafilatura

PROJECT_DIR = Path(__file__).resolve().parent.parent
OLLAMA_BASE = "http://localhost:11434"
JST = timezone(timedelta(hours=9))
DEFAULT_MODEL = "qwen3.6:35b-mlx"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ja,en;q=0.9",
}

# ------------------------------------------------------------------ #
# ツール定義（Ollama /api/chat の tools パラメータ用）
# ------------------------------------------------------------------ #

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": (
                "DuckDuckGo でウェブ検索し、タイトル・URL・スニペットを返す。"
                "直近ニュースを調べるときに使う。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "検索クエリ（日本語・英語可）",
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "取得件数（省略時 8）",
                        "default": 8,
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_url",
            "description": (
                "指定 URL のページを取得し、メインテキストを返す。"
                "JS 描画が必要なサイトは取得できないことがある。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "取得する URL"},
                },
                "required": ["url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_article",
            "description": (
                "新しい記事ファイルを書き込む。"
                "既存ファイルが存在する場合はエラーを返す（上書き禁止）。"
                "パスは PROJECT_DIR からの相対パスで指定する。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "書き込み先（例: articles/weekly/2026-0525.md）",
                    },
                    "content": {
                        "type": "string",
                        "description": "書き込む Markdown 内容",
                    },
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "ファイルを読み込んで内容を返す。パスは PROJECT_DIR からの相対パス。",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "読み込むファイルのパス"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "append_to_readme",
            "description": (
                "README.md の最新記事セクションに週次／月次リンクを追加する。"
                "README の直接編集には使わないこと。このツール専用。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "week_label": {
                        "type": "string",
                        "description": "週次ラベル（例: 5/25〜5/31）",
                    },
                    "week_path": {
                        "type": "string",
                        "description": "週次記事の相対パス（例: ./articles/weekly/2026-0525.md）",
                    },
                    "month_label": {
                        "type": "string",
                        "description": "月次ラベル（例: 2026年6月）。月次モード以外は省略。",
                    },
                    "month_path": {
                        "type": "string",
                        "description": "月次記事の相対パス（例: ./articles/monthly/2026-06.md）",
                    },
                },
                "required": ["week_label", "week_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_commit_push",
            "description": "変更ファイルを git add / commit / push する。記事と README の更新が完了してから呼ぶ。",
            "parameters": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "コミット対象ファイルのリスト（PROJECT_DIR からの相対パス）",
                    },
                    "message": {
                        "type": "string",
                        "description": "コミットメッセージ",
                    },
                },
                "required": ["files", "message"],
            },
        },
    },
]

# ------------------------------------------------------------------ #
# ツール実装
# ------------------------------------------------------------------ #

def tool_search_web(query: str, max_results: int = 8) -> str:
    log(f"search_web: {query!r} (max={max_results})")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "検索結果なし"
        lines = []
        for r in results:
            lines.append(
                f"- [{r.get('title','')}]({r.get('href','')})\n"
                f"  {r.get('body','')[:200]}"
            )
        return "\n\n".join(lines)
    except Exception as e:
        return f"search_web エラー: {e}"


def tool_fetch_url(url: str) -> str:
    log(f"fetch_url: {url}")
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded, include_links=True, favor_precision=True)
            if text:
                return text[:6000]
    except Exception:
        pass
    # trafilatura が失敗した場合は requests でフォールバック
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        # HTMLタグを簡易除去
        import re
        text = re.sub(r"<[^>]+>", " ", r.text)
        text = re.sub(r"\s+", " ", text).strip()
        return text[:6000]
    except Exception as e:
        return f"fetch_url エラー: {e}"


def tool_write_article(path: str, content: str) -> str:
    full = PROJECT_DIR / path
    if full.exists():
        return f"エラー: {path} は既に存在します。上書き禁止。"
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    log(f"write_article: {path} ({len(content)} chars)")
    return f"書き込み完了: {path}"


def tool_read_file(path: str) -> str:
    full = PROJECT_DIR / path
    if not full.exists():
        return f"ファイルが存在しません: {path}"
    return full.read_text(encoding="utf-8")


def tool_append_to_readme(
    week_label: str,
    week_path: str,
    month_label: str = None,
    month_path: str = None,
) -> str:
    readme = PROJECT_DIR / "README.md"
    lines = readme.read_text(encoding="utf-8").split("\n")

    new_week_line = f"- [{week_label}]({week_path})"
    new_month_line = f"- [{month_label}]({month_path})" if month_label else None

    result = []
    i = 0
    weekly_inserted = monthly_inserted = False

    while i < len(lines):
        result.append(lines[i])

        # 週次セクション: "### 週次まとめ" の直後の空行のあとに挿入
        if not weekly_inserted and lines[i].strip() == "### 週次まとめ":
            if i + 1 < len(lines) and lines[i + 1].strip() == "":
                result.append(lines[i + 1])
                i += 1
            result.append(new_week_line)
            weekly_inserted = True

        # 月次セクション
        if new_month_line and not monthly_inserted and lines[i].strip() == "### 月次まとめ":
            if i + 1 < len(lines) and lines[i + 1].strip() == "":
                result.append(lines[i + 1])
                i += 1
            result.append(new_month_line)
            monthly_inserted = True

        i += 1

    readme.write_text("\n".join(result), encoding="utf-8")
    log(f"append_to_readme: {new_week_line}")
    return f"README 更新完了: {new_week_line}" + (
        f" / {new_month_line}" if new_month_line and monthly_inserted else ""
    )


def tool_git_commit_push(files: list, message: str) -> str:
    log(f"git_commit_push: {files}")
    try:
        for f in files:
            subprocess.run(["git", "add", f], cwd=PROJECT_DIR, check=True)
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=PROJECT_DIR,
            check=True,
        )
        subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=PROJECT_DIR,
            check=True,
        )
        return "git add / commit / push 完了"
    except subprocess.CalledProcessError as e:
        return f"git エラー: {e}"


TOOL_HANDLERS = {
    "search_web":       lambda a: tool_search_web(**a),
    "fetch_url":        lambda a: tool_fetch_url(**a),
    "write_article":    lambda a: tool_write_article(**a),
    "read_file":        lambda a: tool_read_file(**a),
    "append_to_readme": lambda a: tool_append_to_readme(**a),
    "git_commit_push":  lambda a: tool_git_commit_push(**a),
}

# ------------------------------------------------------------------ #
# ロギング
# ------------------------------------------------------------------ #

def log(msg: str) -> None:
    ts = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

# ------------------------------------------------------------------ #
# システムプロンプト
# ------------------------------------------------------------------ #

SYSTEM_PROMPT_TMPL = """\
あなたは生成AI情報まとめライターです。
以下の手順に従い、ツールを使いながら週次まとめ記事を自動生成してください。

# 基本情報
- 今日: {today}
- 実行モード: {mode}
- 週次ファイルパス: articles/weekly/{year}-{week_file}.md
- 週表示ラベル: {week_label}（記事タイトル・READMEリンクに使用）
{monthly_info}

# 作業手順
1. **情報収集** — search_web で以下のキーワードを順番に検索する（各キーワード1回ずつ）
   - 「生成AI 最新ニュース 今週」
   - 「LLM release 今週」
   - 「OpenAI Anthropic Google AI news」
   - 「ローカルLLM Ollama 新モデル 今週」
   - 「AIエージェント MCP AutoGen 最新動向」
   - 「1-bit LLM BitNet 最新」
   - 「デジタル庁 生成AI 国産AI 最新」
   - 「国産LLM 新モデル リリース」
   - 「日本 生成AI 企業 最新ニュース 今週」
   - 「site:note.com 生成AI 使ってみた 今週」

2. **補足取得** — fetch_url で以下のサイトを直接確認する
   - https://www.digital.go.jp/news/
   - https://openai.com/news/

3. **記事生成** — 収集した情報と事前収集情報を統合して週次記事を生成し、write_article で保存する

4. **README 更新** — append_to_readme ツールで週次リンクを追加する

{monthly_step}

5. **コミット** — git_commit_push で articles/ と README.md をコミット・プッシュする

# 記事フォーマット（必ず守ること）
- ファイル: articles/weekly/{year}-{week_file}.md
- タイトル行: `# 生成AI週次ダイジェスト（{week_label}）`
- 最低 5 トピック以上収録（日本国内動向を必ず 1 件以上含める）
- 各情報源の URL を必ず記載
- 日本語で記述（技術用語・モデル名は原語のまま）
- 英語タイトルのリンクには日本語訳を併記
  例: `[Introducing GPT-5（GPT-5の発表）](URL)`
- Note 記事は「note / 著者名」形式でソース明記

# README append_to_readme の引数
- week_label: "{week_label}"
- week_path: "./articles/weekly/{year}-{week_file}.md"

# コミットメッセージ形式
```
{year}-{week_file} 週次まとめを追加（ローカルLLM生成）

Co-Authored-By: {model} via Ollama <noreply@local>
```

# 事前収集済み情報（BeautifulSoup で取得済み）
{prefetch}
"""


def build_system_prompt(args) -> str:
    today = datetime.now(JST).strftime("%Y-%m-%d")
    monthly_info = ""
    monthly_step = ""
    if args.mode == "monthly":
        monthly_info = f"- 月次ファイルパス: articles/monthly/{args.year}-{args.month}.md"
        monthly_step = (
            "4.5. **月次記事生成** — 前月の週次まとめを read_file で参照し、"
            f"月次まとめ（articles/monthly/{args.year}-{args.month}.md）を write_article で生成する\n"
        )
    prefetch = args.prefetch if args.prefetch else "（なし — すべて search_web / fetch_url で収集すること）"

    return SYSTEM_PROMPT_TMPL.format(
        today=today,
        mode=args.mode,
        year=args.year,
        week_file=args.week_file,
        week_label=args.week_label,
        month=args.month,
        monthly_info=monthly_info,
        monthly_step=monthly_step,
        prefetch=prefetch,
        model=args.model,
    )

# ------------------------------------------------------------------ #
# Ollama チャットループ
# ------------------------------------------------------------------ #

def call_ollama(model: str, messages: list) -> dict:
    payload = {
        "model": model,
        "messages": messages,
        "tools": TOOLS,
        "stream": False,
        "think": False,      # Qwen3 の thinking トークンを無効化（コンテキスト節約）
        "options": {
            "num_ctx": 65536,
            "temperature": 0.3,
            "top_p": 0.9,
        },
    }
    try:
        resp = requests.post(
            f"{OLLAMA_BASE}/api/chat",
            json=payload,
            timeout=600,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        log("ERROR: Ollama タイムアウト（600s）")
        raise
    except requests.exceptions.RequestException as e:
        log(f"ERROR: Ollama 接続エラー: {e}")
        raise


def run_agent(args) -> bool:
    system_prompt = build_system_prompt(args)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "記事生成を開始してください。"},
    ]

    log(f"エージェント開始: model={args.model}, mode={args.mode}, week={args.week_file}")

    MAX_TURNS = 40
    for turn in range(MAX_TURNS):
        log(f"--- ターン {turn + 1}/{MAX_TURNS} ---")

        data = call_ollama(args.model, messages)
        msg = data.get("message", {})
        tool_calls = msg.get("tool_calls", [])
        content = msg.get("content") or ""

        if content:
            log(f"モデル応答: {content[:300]}")

        # ツール呼び出しがなければ完了
        if not tool_calls:
            log("ツール呼び出しなし → 完了")
            return True

        # アシスタントメッセージを履歴に追加
        messages.append({"role": "assistant", "content": content, "tool_calls": tool_calls})

        # 各ツールを実行して結果を返す
        for tc in tool_calls:
            fn = tc.get("function", {})
            name = fn.get("name", "")
            raw_args = fn.get("arguments", {})

            # arguments が文字列の場合は JSON パース
            if isinstance(raw_args, str):
                try:
                    raw_args = json.loads(raw_args)
                except json.JSONDecodeError:
                    raw_args = {}

            log(f"ツール呼び出し: {name}({json.dumps(raw_args, ensure_ascii=False)[:120]})")

            handler = TOOL_HANDLERS.get(name)
            if handler:
                try:
                    result = handler(raw_args)
                except Exception as e:
                    result = f"ツール実行エラー: {e}"
            else:
                result = f"未知のツール: {name}"

            log(f"ツール結果: {str(result)[:300]}")

            messages.append({"role": "tool", "content": str(result)})

            # DuckDuckGo のレート制限を避けるため少し待機
            if name == "search_web":
                time.sleep(2)

    log(f"ERROR: 最大ターン数 ({MAX_TURNS}) に達しました")
    return False

# ------------------------------------------------------------------ #
# エントリポイント
# ------------------------------------------------------------------ #

def main():
    parser = argparse.ArgumentParser(description="ai_news ローカルLLMエージェント")
    parser.add_argument("--mode", required=True, choices=["weekly", "monthly"])
    parser.add_argument("--week-file", required=True, help="MMDD形式（例: 0525）")
    parser.add_argument("--week-label", required=True, help="例: 5/25〜5/31")
    parser.add_argument("--year", required=True, help="例: 2026")
    parser.add_argument("--month", required=True, help="例: 05")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama モデル名")
    parser.add_argument("--prefetch", default="", help="fetch_news.py の出力テキスト")
    args = parser.parse_args()

    # Ollama の疎通確認
    try:
        requests.get(f"{OLLAMA_BASE}/api/tags", timeout=5).raise_for_status()
    except Exception as e:
        log(f"ERROR: Ollama に接続できません: {e}")
        sys.exit(1)

    success = run_agent(args)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
