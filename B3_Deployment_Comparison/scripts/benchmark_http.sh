#!/usr/bin/env bash
set -euo pipefail
URL="${1:-http://127.0.0.1:8000/}"
REQUESTS="${REQUESTS:-1000}"
CONCURRENCY="${CONCURRENCY:-20}"
if ! command -v ab >/dev/null 2>&1; then
  echo "ApacheBench is missing. Install it with: sudo apt install apache2-utils" >&2
  exit 1
fi
echo "URL=$URL REQUESTS=$REQUESTS CONCURRENCY=$CONCURRENCY"
ab -n "$REQUESTS" -c "$CONCURRENCY" "$URL"
