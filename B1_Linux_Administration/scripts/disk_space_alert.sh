#!/usr/bin/env bash
set -euo pipefail
THRESHOLD="${THRESHOLD:-80}"
TARGET="${1:-/}"
USAGE=$(df -P "$TARGET" | awk 'NR==2 {gsub("%","",$5); print $5}')
echo "Disk usage for $TARGET: ${USAGE}% (alert threshold: ${THRESHOLD}%)"
if [ "$USAGE" -ge "$THRESHOLD" ]; then
  echo "ALERT: filesystem usage has reached or exceeded ${THRESHOLD}%"
else
  echo "OK: filesystem usage is below the threshold"
fi
