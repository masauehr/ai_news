#!/bin/bash
# run_ai_news_haiku.sh — Claude Haiku による生成AI週次まとめ 自動実行スクリプト
# launchd から毎週土曜 13:00 に呼び出される。
# Ollama版（09:00）と同じ週の記事を Haiku で別ファイルに生成し、
# 両者の比較ページを自動作成する。
#
# 【2026-07-13 変更】Anthropic API（従量課金クレジット）ではなく、
# Claude Code CLI（Pro/Maxサブスクリプション）経由で実行するように変更した。
# stock_analysis / rakuten_margin と同じ方式。ANTHROPIC_API_KEY は使わない
# （設定されていても haiku_agent.py / generate_compare.py 側で明示的に除去する）。

set -euo pipefail

# --- 設定 ---
# スクリプトの位置（scripts/ の1つ上）をプロジェクトディレクトリとする（絶対パスを埋め込まない）
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_FILE="${PROJECT_DIR}/ai_news_haiku.log"
PYTHON_BIN="/opt/anaconda3/bin/python3"
CLAUDE_BIN="${HOME}/.local/bin/claude"
HAIKU_MODEL="${HAIKU_MODEL:-haiku}"
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

# --- Claude Code CLI の存在確認（サブスクリプション認証。APIキーは使わない）---
if [ ! -x "${CLAUDE_BIN}" ]; then
  log "ERROR: Claude Code CLI が見つかりません: ${CLAUDE_BIN}"
  exit 1
fi
# ANTHROPIC_API_KEY が環境に残っているとAPIクレジット課金経路に戻ってしまうため、
# このプロセス内では明示的に外す（haiku_agent.py / generate_compare.py 側でも二重に除去する）
unset ANTHROPIC_API_KEY || true

# --- 開始 ---
log "=== ai_news Haiku 起動チェック ==="
log "今日: ${TODAY} / 実行日ファイル: ${YEAR}-${WEEK_FILE_MMDD} / 対象期間: ${WEEK_LABEL}"

cd "${PROJECT_DIR}"

MONTH=$(TZ=Asia/Tokyo date +%m)
HAIKU_MONTHLY_FILE="${PROJECT_DIR}/articles/haiku_monthly/${YEAR}-${MONTH}.md"

# --- 実行済みチェック（今週分のファイルが既にあればスキップ）---
if [ -f "${HAIKU_WEEKLY_FILE}" ]; then
  log "実行日分 Haiku 記事（${YEAR}-${WEEK_FILE_MMDD}）は実行済み。スキップします。"
  # 比較ページが未生成なら生成を試みる
  COMPARE_FILE="${PROJECT_DIR}/articles/compare/${YEAR}-${WEEK_FILE_MMDD}.md"
  if [ ! -f "${COMPARE_FILE}" ]; then
    log "比較ページが未生成のため生成を試みます..."
    "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/generate_compare.py" \
      --week-file "${WEEK_FILE_MMDD}" \
      --week-label "${WEEK_LABEL}" \
      --year "${YEAR}" \
      2>&1 | tee -a "${LOG_FILE}" || true
  fi
  exit 0
fi

log "=== ai_news Haiku 自動実行開始 ==="

# --- モード判定（第1週 = 月次も生成）---
if [ "${DAY_OF_MONTH}" -le 7 ]; then
  MODE="monthly"
  log "モード: 月次（月初週）"
else
  MODE="weekly"
  log "モード: 週次"
fi

# --- フェーズ2: オーケストレーターで事前収集＋ローカル要約（検索→取得→Ollama圧縮要約）---
# 成功すれば Haiku には生スクレイプでなく圧縮サマリ（ファイル）を渡す。失敗時は下の
# fetch_news.py の生スクレイプにフォールバックする。
ORCH_DIR="$(cd "${PROJECT_DIR}/.." && pwd)/agent_orchestrator"
PREFETCH_FILE="${PROJECT_DIR}/var/prefetch_${YEAR}-${WEEK_FILE_MMDD}.txt"
HAIKU_PREFETCH=""
mkdir -p "${PROJECT_DIR}/var"
if [ -d "${ORCH_DIR}" ]; then
  log "事前収集パイプライン(ai_news_prefetch)を実行します..."
  if PYTHONPATH="${ORCH_DIR}" "${PYTHON_BIN}" -m orchestrator.cli run ai_news_prefetch \
       -p out_file="${PREFETCH_FILE}" -p length=240 2>&1 | tee -a "${LOG_FILE}"; then
    if [ -s "${PREFETCH_FILE}" ]; then
      HAIKU_PREFETCH="@${PREFETCH_FILE}"
      log "事前収集サマリ取得: ${PREFETCH_FILE}（$(grep -c '' "${PREFETCH_FILE}") 行）"
    fi
  else
    log "WARN: 事前収集に失敗。fetch_news.py の生スクレイプにフォールバックします"
  fi
fi

# --- 事前スクレイピング（オーケストレーター事前収集が無い場合のフォールバック）---
if [ -z "${HAIKU_PREFETCH}" ]; then
  log "BeautifulSoup で記事一覧を事前取得中..."
  SCRAPED_NEWS=$("${PYTHON_BIN}" "${PROJECT_DIR}/scripts/fetch_news.py" 2>>"${LOG_FILE}" || true)
  if [ -z "${SCRAPED_NEWS}" ]; then
    log "WARN: スクレイピング失敗。エージェントが直接 fetch_url で補完します。"
    SCRAPED_NEWS=""
  else
    log "スクレイピング完了（$(echo "${SCRAPED_NEWS}" | wc -l) 行取得）"
  fi
  HAIKU_PREFETCH="${SCRAPED_NEWS}"
fi

# --- 共通: エージェント実行関数（リトライ付き）---
run_haiku_agent() {
  local _mode="$1"
  local _max_retry=2
  local _retry=0
  local _success=false

  while [ ${_retry} -lt ${_max_retry} ]; do
    _retry=$((_retry + 1))
    log "Haikuエージェントを起動します... mode=${_mode} model=${HAIKU_MODEL} (試行 ${_retry}/${_max_retry})"

    if "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/haiku_agent.py" \
        --mode "${_mode}" \
        --week-file "${WEEK_FILE_MMDD}" \
        --week-label "${WEEK_LABEL}" \
        --year "${YEAR}" \
        --month "${MONTH}" \
        --model "${HAIKU_MODEL}" \
        --prefetch "${HAIKU_PREFETCH}" \
        2>&1 | tee -a "${LOG_FILE}"; then
      _success=true
      break
    else
      EXIT_CODE=$?
      log "Haikuエージェントが終了コード ${EXIT_CODE} で失敗しました。"
      if [ ${_retry} -lt ${_max_retry} ]; then
        log "30秒後にリトライします..."
        sleep 30
      fi
    fi
  done

  if [ "${_success}" = false ]; then
    log "ERROR: ${_max_retry}回試行しましたがすべて失敗しました（mode=${_mode}）。手動確認が必要です。"
    return 1
  fi
  return 0
}

# --- 週次記事生成（常に実行）---
log "モード: weekly"
run_haiku_agent "weekly" || exit 1
log "=== Haiku 週次記事生成完了 ==="

# --- 月次記事生成（第1週のみ）---
if [ "${MODE}" = "monthly" ]; then
  if [ -f "${HAIKU_MONTHLY_FILE}" ]; then
    log "Haiku 月次記事（${YEAR}-${MONTH}）は実行済み。スキップします。"
  else
    log "=== Haiku 月次記事生成開始 ==="
    run_haiku_agent "monthly" || log "WARN: 月次記事生成に失敗しました（手動で実行してください）"
    log "=== Haiku 月次記事生成完了 ==="
  fi
fi

# --- 週次比較ページ生成（Ollama版記事が揃っている場合のみ）---
OLLAMA_FILE="${PROJECT_DIR}/articles/weekly/${YEAR}-${WEEK_FILE_MMDD}.md"
COMPARE_FILE="${PROJECT_DIR}/articles/compare/${YEAR}-${WEEK_FILE_MMDD}.md"

if [ -f "${OLLAMA_FILE}" ] && [ ! -f "${COMPARE_FILE}" ]; then
  log "=== 週次比較ページ生成開始 ==="
  "${PYTHON_BIN}" "${PROJECT_DIR}/scripts/generate_compare.py" \
    --week-file "${WEEK_FILE_MMDD}" \
    --week-label "${WEEK_LABEL}" \
    --year "${YEAR}" \
    2>&1 | tee -a "${LOG_FILE}" || log "WARN: 比較ページ生成に失敗しました（手動で実行してください）"
  log "=== 週次比較ページ生成完了 ==="
elif [ ! -f "${OLLAMA_FILE}" ]; then
  log "WARN: Ollama版記事（${OLLAMA_FILE}）が存在しません。比較ページはスキップします。"
  log "      Ollama版が生成された後、以下のコマンドで手動生成できます:"
  log "      python3 ${PROJECT_DIR}/scripts/generate_compare.py --week-file ${WEEK_FILE_MMDD} --week-label '${WEEK_LABEL}' --year ${YEAR}"
fi

log "=== ai_news Haiku 自動実行完了 ==="
