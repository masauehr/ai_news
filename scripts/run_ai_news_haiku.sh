#!/bin/bash
# run_ai_news_haiku.sh — Claude Haiku による生成AI週次まとめ 自動実行スクリプト
# launchd から毎週土曜 13:00 に呼び出される。
# Ollama版（09:00）と同じ週の記事を Haiku で別ファイルに生成し、
# 両者の比較ページを自動作成する。

set -euo pipefail

# --- 設定 ---
PROJECT_DIR="/Users/masahiro/projects/ai_news"
LOG_FILE="${PROJECT_DIR}/ai_news_haiku.log"
PYTHON_BIN="/opt/anaconda3/bin/python3"
HAIKU_MODEL="${HAIKU_MODEL:-claude-haiku-4-5-20251001}"
TODAY=$(TZ=Asia/Tokyo date +%Y-%m-%d)
DAY_OF_MONTH=$(TZ=Asia/Tokyo date +%d)
YEAR=$(TZ=Asia/Tokyo date +%Y)
# ファイル名: 実行日（MMDD）/ ラベル: 実行日の7日前〜実行日
WEEK_FILE_MMDD=$(TZ=Asia/Tokyo date +%m%d)
WEEK_END=$(TZ=Asia/Tokyo date +%-m/%-d)
WEEK_START=$(TZ=Asia/Tokyo date -v-7d +%-m/%-d)
WEEK_LABEL="${WEEK_START}〜${WEEK_END}"
HAIKU_WEEKLY_FILE="${PROJECT_DIR}/articles/haiku_weekly/${YEAR}-${WEEK_FILE_MMDD}.md"

# --- ログ関数 ---
log() {
  echo "[$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

# --- ANTHROPIC_API_KEY の読み込み ---
if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  if [ -f "${HOME}/.anthropic_env" ]; then
    # shellcheck disable=SC1090
    source "${HOME}/.anthropic_env"
    log "ANTHROPIC_API_KEY を ~/.anthropic_env から読み込みました"
  fi
fi

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  log "ERROR: ANTHROPIC_API_KEY が設定されていません"
  log "  ~/.anthropic_env に ANTHROPIC_API_KEY=sk-ant-... を記載してください"
  exit 1
fi
export ANTHROPIC_API_KEY

# --- 開始 ---
log "=== ai_news Haiku 起動チェック ==="
log "今日: ${TODAY} / 実行日ファイル: ${YEAR}-${WEEK_FILE_MMDD} / 対象期間: ${WEEK_LABEL}"

cd "${PROJECT_DIR}"

# --- 実行済みチェック（今週分のファイルが既にあればスキップ）---
if [ -f "${HAIKU_WEEKLY_FILE}" ]; then
  log "実行日分 Haiku 記事（${YEAR}-${WEEK_FILE_MMDD}）は実行済み。スキップします。"
  # 比較ページが未生成なら生成を試みる
  COMPARE_FILE="${PROJECT_DIR}/articles/compare/${YEAR}-${WEEK_FILE_MMDD}.md"
  if [ ! -f "${COMPARE_FILE}" ]; then
    log "比較ページが未生成のため生成を試みます..."
    "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/generate_compare.py" \
      --week-file "${WEEK_MON_MMDD}" \
      --week-label "${WEEK_LABEL}" \
      --year "${YEAR}" \
      2>&1 | tee -a "${LOG_FILE}" || true
  fi
  exit 0
fi

log "=== ai_news Haiku 自動実行開始 ==="

# --- モード判定（第1週 = 月次も考慮、ただしHaikuは週次のみ）---
MODE="weekly"
log "モード: ${MODE}"

# --- 事前スクレイピング（Ollama版と共通の fetch_news.py を流用）---
log "BeautifulSoup で記事一覧を事前取得中..."
SCRAPED_NEWS=$("${PYTHON_BIN}" "${PROJECT_DIR}/scripts/fetch_news.py" 2>>"${LOG_FILE}" || true)
if [ -z "${SCRAPED_NEWS}" ]; then
  log "WARN: スクレイピング失敗。エージェントが直接 fetch_url で補完します。"
  SCRAPED_NEWS=""
else
  log "スクレイピング完了（$(echo "${SCRAPED_NEWS}" | wc -l) 行取得）"
fi

# --- Haikuエージェント実行（タイムアウト時リトライ最大2回）---
MAX_RETRY=2
RETRY=0
SUCCESS=false

while [ ${RETRY} -lt ${MAX_RETRY} ]; do
  RETRY=$((RETRY + 1))
  log "Haikuエージェントを起動します... model=${HAIKU_MODEL} (試行 ${RETRY}/${MAX_RETRY})"

  if "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/haiku_agent.py" \
      --mode "${MODE}" \
      --week-file "${WEEK_FILE_MMDD}" \
      --week-label "${WEEK_LABEL}" \
      --year "${YEAR}" \
      --month "$(TZ=Asia/Tokyo date +%m)" \
      --model "${HAIKU_MODEL}" \
      --prefetch "${SCRAPED_NEWS}" \
      2>&1 | tee -a "${LOG_FILE}"; then
    SUCCESS=true
    break
  else
    EXIT_CODE=$?
    log "Haikuエージェントが終了コード ${EXIT_CODE} で失敗しました。"
    if [ ${RETRY} -lt ${MAX_RETRY} ]; then
      log "30秒後にリトライします..."
      sleep 30
    fi
  fi
done

if [ "${SUCCESS}" = false ]; then
  log "ERROR: ${MAX_RETRY}回試行しましたがすべて失敗しました。手動確認が必要です。"
  exit 1
fi

log "=== Haiku 記事生成完了 ==="

# --- 比較ページ生成（Ollama版記事が揃っている場合のみ）---
OLLAMA_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-${WEEK_FILE_MMDD}.md"
COMPARE_FILE="${PROJECT_DIR}/articles/compare/${YEAR}-${WEEK_FILE_MMDD}.md"

if [ -f "${OLLAMA_FILE}" ] && [ ! -f "${COMPARE_FILE}" ]; then
  log "=== 比較ページ生成開始 ==="
  "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/generate_compare.py" \
    --week-file "${WEEK_MON_MMDD}" \
    --week-label "${WEEK_LABEL}" \
    --year "${YEAR}" \
    2>&1 | tee -a "${LOG_FILE}" || log "WARN: 比較ページ生成に失敗しました（手動で実行してください）"
  log "=== 比較ページ生成完了 ==="
elif [ ! -f "${OLLAMA_FILE}" ]; then
  log "WARN: Ollama版記事（${OLLAMA_FILE}）が存在しません。比較ページはスキップします。"
  log "      Ollama版が生成された後、以下のコマンドで手動生成できます:"
  log "      python3 ${PROJECT_DIR}/scripts/generate_compare.py --week-file ${WEEK_FILE_MMDD} --week-label '${WEEK_LABEL}' --year ${YEAR}"
fi

log "=== ai_news Haiku 自動実行完了 ==="
