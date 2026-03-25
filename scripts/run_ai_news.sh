#!/bin/bash
# run_ai_news.sh — 生成AI情報まとめ 自動実行スクリプト
# launchd から毎日 09:00 に呼び出される。
# 今週分の記事がまだ生成されていない場合のみ実行する。

set -euo pipefail

# --- 設定 ---
PROJECT_DIR="/Users/masahiro/projects/ai_news"
LOG_FILE="${PROJECT_DIR}/ai_news.log"
CLAUDE_BIN="/Users/masahiro/.local/bin/claude"
TODAY=$(TZ=Asia/Tokyo date +%Y-%m-%d)
DAY_OF_MONTH=$(TZ=Asia/Tokyo date +%d)
WEEK_NUM=$(TZ=Asia/Tokyo date +%V)
YEAR=$(TZ=Asia/Tokyo date +%Y)
WEEKLY_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-W${WEEK_NUM}.md"

# --- ログ関数 ---
log() {
  echo "[$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

# --- 開始 ---
log "=== ai_news 起動チェック ==="
log "今日: ${TODAY} / 対象週: ${YEAR}-W${WEEK_NUM}"

cd "${PROJECT_DIR}"

# --- 実行済みチェック（今週分のファイルが既にあればスキップ）---
if [ -f "${WEEKLY_FILE}" ]; then
  log "今週分（${YEAR}-W${WEEK_NUM}）は実行済み。スキップします。"
  exit 0
fi

log "=== ai_news 自動実行開始 ==="

# --- モード判定（第1週 = 月次も生成）---
if [ "${DAY_OF_MONTH}" -le 7 ]; then
  MODE="monthly"
  log "モード: 月次（月初週）"
else
  MODE="weekly"
  log "モード: 週次"
fi

# --- プロンプト生成 ---
PROMPT="今日は ${TODAY} です。
CLAUDE.md の手順に従って、生成AIの最新情報まとめ記事を自動生成してください。

実行モード: ${MODE}
対象週: ${YEAR}-W${WEEK_NUM}

手順:
1. WebSearch で直近7日間の生成AI関連ニュースを収集する
2. 週次まとめ記事（articles/weekly/${YEAR}-W${WEEK_NUM}.md）を生成する
$([ "${MODE}" = "monthly" ] && echo "3. 月次まとめ記事（articles/monthly/${YEAR}-$(TZ=Asia/Tokyo date +%m).md）も生成する")
$([ "${MODE}" = "monthly" ] && echo "4." || echo "3.") README.md の最新記事リストを更新する
$([ "${MODE}" = "monthly" ] && echo "5." || echo "4.") git add / commit / push する

注意: 既存ファイルが存在する場合は上書きしないこと。"

# --- claude CLI 実行 ---
log "claude CLI を起動します..."

"${CLAUDE_BIN}" \
  --print \
  --dangerously-skip-permissions \
  -p "${PROMPT}" \
  2>&1 | tee -a "${LOG_FILE}"

log "=== ai_news 自動実行完了 ==="
