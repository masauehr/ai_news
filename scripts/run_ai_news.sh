#!/bin/bash
# run_ai_news.sh — 生成AI情報まとめ 自動実行スクリプト
# launchd から毎週土曜 09:00 に呼び出される（メインの Ollama 記事）。
# 今週分の記事がまだ生成されていない場合のみ実行する（月の第1土曜は月次まとめも生成）。
#
# 【比較用サブモデル】環境変数 AI_NEWS_VARIANT を指定すると、比較専用の軽量モードで動く:
#   - 保存先: articles/weekly_<variant>/YYYY-MMDD.md
#   - ログ:   ai_news_<variant>.log
#   - 月次生成・README/index更新は行わない（記事生成と push のみ）
#   例: AI_NEWS_VARIANT=ornith   AI_NEWS_MODEL=ornith-1.5:35b            （土曜 10:00）
#       AI_NEWS_VARIANT=nemotron AI_NEWS_MODEL=nemotron-3.5-lightning:30b-mlx （土曜 11:00）

set -euo pipefail

# --- 設定 ---
PROJECT_DIR="/Users/masahiro/projects/ai_news"
PYTHON_BIN="/opt/anaconda3/bin/python3"
AI_NEWS_MODEL="${AI_NEWS_MODEL:-qwen3.6:35b-mlx}"
AI_NEWS_VARIANT="${AI_NEWS_VARIANT:-}"
TODAY=$(TZ=Asia/Tokyo date +%Y-%m-%d)
DAY_OF_MONTH=$(TZ=Asia/Tokyo date +%d)
YEAR=$(TZ=Asia/Tokyo date +%Y)
# ファイル名: 実行日（MMDD）/ ラベル: 実行日の7日前〜実行日
WEEK_FILE_MMDD=$(TZ=Asia/Tokyo date +%m%d)
WEEK_END=$(TZ=Asia/Tokyo date +%-m/%-d)
WEEK_START=$(TZ=Asia/Tokyo date -v-7d +%-m/%-d)
WEEK_LABEL="${WEEK_START}〜${WEEK_END}"

if [ -n "${AI_NEWS_VARIANT}" ]; then
  LOG_FILE="${PROJECT_DIR}/ai_news_${AI_NEWS_VARIANT}.log"
  WEEKLY_FILE="${PROJECT_DIR}/articles/weekly_${AI_NEWS_VARIANT}/${YEAR}-${WEEK_FILE_MMDD}.md"
else
  LOG_FILE="${PROJECT_DIR}/ai_news.log"
  WEEKLY_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-${WEEK_FILE_MMDD}.md"
fi

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

# --- モード判定（第1週 = 月次も生成。ただし比較用サブモデルは常に週次のみ）---
if [ -n "${AI_NEWS_VARIANT}" ]; then
  MODE="weekly"
  log "モード: 週次（比較用サブモデル: ${AI_NEWS_VARIANT}）"
elif [ "${DAY_OF_MONTH}" -le 7 ]; then
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
      --variant "${AI_NEWS_VARIANT}" \
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
