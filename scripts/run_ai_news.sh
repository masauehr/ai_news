#!/bin/bash
# run_ai_news.sh — 生成AI情報まとめ 自動実行スクリプト
# launchd から毎週土曜 09:00 に呼び出される。
# 今週分の記事がまだ生成されていない場合のみ実行する（月の第1土曜は月次まとめも生成）。

set -euo pipefail

# --- 設定 ---
PROJECT_DIR="/Users/masahiro/projects/ai_news"
LOG_FILE="${PROJECT_DIR}/ai_news.log"
PYTHON_BIN="/opt/anaconda3/bin/python3"
AI_NEWS_MODEL="${AI_NEWS_MODEL:-qwen3.6:35b-mlx}"
TODAY=$(TZ=Asia/Tokyo date +%Y-%m-%d)
DAY_OF_MONTH=$(TZ=Asia/Tokyo date +%d)
YEAR=$(TZ=Asia/Tokyo date +%Y)
# ファイル名: 実行日（MMDD）/ ラベル: 実行日の7日前〜実行日
WEEK_FILE_MMDD=$(TZ=Asia/Tokyo date +%m%d)
WEEK_END=$(TZ=Asia/Tokyo date +%-m/%-d)
WEEK_START=$(TZ=Asia/Tokyo date -v-7d +%-m/%-d)
WEEK_LABEL="${WEEK_START}〜${WEEK_END}"
WEEKLY_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-${WEEK_FILE_MMDD}.md"

# --- ログ関数 ---
log() {
  echo "[$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

# --- 開始 ---
log "=== ai_news 起動チェック ==="
log "今日: ${TODAY} / 実行日ファイル: ${YEAR}-${WEEK_FILE_MMDD} / 対象期間: ${WEEK_LABEL}"

cd "${PROJECT_DIR}"

# --- 実行済みチェック（今週分のファイルが既にあればスキップ）---
if [ -f "${WEEKLY_FILE}" ]; then
  log "実行日分（${YEAR}-${WEEK_FILE_MMDD}）は実行済み。スキップします。"
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

# --- 事前スクレイピング（BeautifulSoupで固定URLの記事一覧を取得）---
log "BeautifulSoup で記事一覧を事前取得中..."
SCRAPED_NEWS=$("${PYTHON_BIN}" "${PROJECT_DIR}/scripts/fetch_news.py" 2>>"${LOG_FILE}" || true)
if [ -z "${SCRAPED_NEWS}" ]; then
  log "WARN: スクレイピング失敗。エージェントが直接 fetch_url で補完します。"
  SCRAPED_NEWS=""
else
  log "スクレイピング完了（$(echo "${SCRAPED_NEWS}" | wc -l) 行取得）"
fi

# --- ローカルLLMエージェント実行（タイムアウト時リトライ最大3回）---
MAX_RETRY=3
RETRY=0
SUCCESS=false

while [ ${RETRY} -lt ${MAX_RETRY} ]; do
  RETRY=$((RETRY + 1))
  log "ローカルエージェントを起動します... model=${AI_NEWS_MODEL} (試行 ${RETRY}/${MAX_RETRY})"

  if "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/local_agent.py" \
      --mode "${MODE}" \
      --week-file "${WEEK_FILE_MMDD}" \
      --week-label "${WEEK_LABEL}" \
      --year "${YEAR}" \
      --month "$(TZ=Asia/Tokyo date +%m)" \
      --model "${AI_NEWS_MODEL}" \
      --prefetch "${SCRAPED_NEWS}" \
      2>&1 | tee -a "${LOG_FILE}"; then
    SUCCESS=true
    break
  else
    EXIT_CODE=$?
    log "ローカルエージェントが終了コード ${EXIT_CODE} で失敗しました。"
    if [ ${RETRY} -lt ${MAX_RETRY} ]; then
      log "60秒後にリトライします..."
      sleep 60
    fi
  fi
done

if [ "${SUCCESS}" = false ]; then
  log "ERROR: ${MAX_RETRY}回試行しましたがすべて失敗しました。手動確認が必要です。"
  exit 1
fi

log "=== ai_news 自動実行完了 ==="
