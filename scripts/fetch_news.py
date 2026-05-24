#!/usr/bin/env python3
"""
fetch_news.py — 固定URLのニュースサイトから記事一覧をBeautifulSoupで取得し、
Claudeに渡す構造化テキストを出力する。
WebFetchを使わずに済む分、Claudeのトークン消費を削減する。

使い方: python3 fetch_news.py
出力:   標準出力に記事リスト（Markdown形式）
エラー: 標準エラー出力に進捗・警告
"""

import re
import sys
import time
from datetime import date, datetime, timedelta, timezone

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ja,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
}
TIMEOUT = 15
JST = timezone(timedelta(hours=9))
# 略称・正式名称の両方に対応（DeepMindは正式名称、Anthropicは略称を使用）
MONTHS_RE = (
    r"January|February|March|April|May|June|July|August"
    r"|September|October|November|December"
    r"|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
)


def fetch(url, encoding=None):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        r.encoding = encoding or r.apparent_encoding
        return r.text
    except Exception as e:
        print(f"  [fetch error] {url}: {e}", file=sys.stderr)
        return None


def dedup(items, key="url"):
    seen = set()
    result = []
    for item in items:
        k = item.get(key, "")
        if k and k not in seen:
            seen.add(k)
            result.append(item)
    return result


# --- サイト別抽出関数 ---

def extract_itmedia_aiplus(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for tag in soup.find_all(["h2", "h3"]):
        a = tag.find("a")
        if not a:
            continue
        title = a.get_text(strip=True)
        href = a.get("href", "")
        if "aiplus/articles/" in href and title:
            articles.append({"title": title, "url": href})
    return dedup(articles)[:12]


def extract_techno_edge(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    seen = set()
    cutoff = date.today() - timedelta(days=30)
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/"):
            href = "https://www.techno-edge.net" + href
        m = re.search(r"/article/(\d{4})/(\d{2})/(\d{2})/\d+\.html$", href)
        if not m:
            continue
        # 30日以内の記事のみ対象
        art_date = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if art_date < cutoff:
            continue
        if href in seen:
            continue
        seen.add(href)
        text = a.get_text(strip=True)
        # "カテゴリ2026 May 15タイトル" → "タイトル" に整形
        title = re.sub(rf"^.*?(?:{MONTHS_RE})\s*\d{{1,2}}", "", text).strip()
        if not title:
            title = text
        if len(title) > 5:
            articles.append({"title": title[:100], "url": href})
    return articles[:12]


def extract_ainow(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    # 2025〜2026年の記事のみ（古い固定記事を除外）
    pattern = re.compile(r"ainow\.ai/(202[56])/\d{2}/\d{2}/\d+/?")
    for a in soup.find_all("a", href=True):
        if not pattern.search(a["href"]):
            continue
        title = a.get_text(strip=True)
        if title and len(title) > 5:
            articles.append({"title": title, "url": a["href"]})
    return dedup(articles)[:10]


def extract_anthropic(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    skip = {"https://www.anthropic.com/news"}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/news/" not in href or "mailto:" in href:
            continue
        if href.startswith("/"):
            href = "https://www.anthropic.com" + href
        if href in skip or not href.startswith("https://www.anthropic.com/news/"):
            continue
        # テキストは日付・カテゴリが混入して複雑なため、URLスラグから生成
        slug = href.rstrip("/").split("/")[-1]
        # 数字間のハイフンはバージョン番号扱いでピリオドに変換（例: 4-7 → 4.7）
        slug = re.sub(r"(\d)-(\d)", r"\1.\2", slug)
        title = " ".join(w.capitalize() for w in slug.split("-"))
        if title:
            articles.append({"title": title, "url": href})
    return dedup(articles)[:10]


def extract_huggingface(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for art in soup.find_all("article"):
        a = art.find("a", href=True)
        if not a:
            continue
        href = a["href"]
        if href.startswith("/"):
            href = "https://huggingface.co" + href
        h = art.find(["h2", "h3", "h4"])
        title = h.get_text(strip=True) if h else a.get_text(strip=True)
        if title and len(title) > 5:
            articles.append({"title": title[:100], "url": href})
    return dedup(articles)[:10]


def extract_deepmind(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for art in soup.find_all("article"):
        a = art.find("a", href=True)
        if not a:
            continue
        href = a["href"]
        if href.startswith("/"):
            href = "https://deepmind.google" + href
        text = art.get_text(separator=" ", strip=True)
        # "タイトル May 2026 Research Learn more" → "タイトル" に整形
        title = re.sub(
            rf"\s+(?:{MONTHS_RE})\s+\d{{4}}\s.*", "", text, flags=re.DOTALL
        ).strip()
        if title and len(title) > 5:
            articles.append({"title": title[:100], "url": href})
    return dedup(articles)[:10]


# --- サイト定義 ---
# fallback=True のサイトはBeautifulSoupで取得不可 → ClaudeがWebFetchで補完

SITES = [
    {
        "name": "ITmedia AI+",
        "url": "https://www.itmedia.co.jp/aiplus/",
        "encoding": "shift_jis",
        "extractor": extract_itmedia_aiplus,
    },
    {
        "name": "Techno Edge",
        "url": "https://www.techno-edge.net/",
        "encoding": "utf-8",
        "extractor": extract_techno_edge,
    },
    {
        "name": "AINOW",
        "url": "https://ainow.ai/",
        "encoding": "utf-8",
        "extractor": extract_ainow,
    },
    {
        "name": "Anthropic News",
        "url": "https://www.anthropic.com/news",
        "extractor": extract_anthropic,
    },
    {
        "name": "Hugging Face Blog",
        "url": "https://huggingface.co/blog",
        "encoding": "utf-8",
        "extractor": extract_huggingface,
    },
    {
        "name": "Google DeepMind Blog",
        "url": "https://deepmind.google/discover/blog/",
        "encoding": "utf-8",
        "extractor": extract_deepmind,
    },
    # 以下はJS描画 or アクセス拒否のためClaudeのWebFetchで補完
    {"name": "デジタル庁ニュース", "url": "https://www.digital.go.jp/news/", "fallback": True},
    {"name": "OpenAI Blog", "url": "https://openai.com/news/", "fallback": True},
]


def main():
    now_jst = datetime.now(JST)
    out = []
    out.append(f"# 事前収集済みサイト情報（{now_jst.strftime('%Y-%m-%d %H:%M')} JST）\n\n")
    out.append("以下のサイトはBeautifulSoupで記事一覧を取得済み。**これらへのWebFetchは不要**。\n\n")

    fallbacks = []

    for site in SITES:
        name = site["name"]
        url = site["url"]

        if site.get("fallback"):
            fallbacks.append(f"- {name}: {url}")
            continue

        print(f"  取得中: {name} ...", file=sys.stderr)
        html = fetch(url, site.get("encoding"))

        if html is None:
            fallbacks.append(f"- {name}: {url}（取得失敗 → WebFetchで補完）")
            continue

        articles = site["extractor"](html)

        if not articles:
            fallbacks.append(f"- {name}: {url}（記事抽出失敗 → WebFetchで補完）")
            continue

        out.append(f"## {name}\n")
        for a in articles:
            out.append(f"- [{a['title']}]({a['url']})\n")
        out.append("\n")

        time.sleep(1)

    if fallbacks:
        out.append("---\n\n")
        out.append("## WebFetch が必要なサイト（JS描画 or アクセス制限）\n\n")
        out.extend(f"{s}\n" for s in fallbacks)
        out.append("\n")

    print("".join(out))


if __name__ == "__main__":
    main()
