#!/usr/bin/env bash
set -euo pipefail
echo "===== DATE / HOST ====="
date
hostname
echo
echo "===== PROCESS SNAPSHOT (ps) ====="
ps -eo pid,ppid,user,stat,%cpu,%mem,comm --sort=-%cpu | head -n 16
echo
echo "===== TOP SNAPSHOT ====="
top -b -n 1 | head -n 18
echo
echo "===== MEMORY (free) ====="
free -h
echo
echo "===== VIRTUAL MEMORY (vmstat) ====="
vmstat 1 2
echo
echo "===== DISK I/O (iostat) ====="
if command -v iostat >/dev/null 2>&1; then
  iostat -xz 1 2
else
  echo "iostat not installed. Install with: sudo apt install sysstat"
fi
echo
echo "===== FILESYSTEM SPACE (df) ====="
df -hT
echo
echo "===== NETWORK SOCKETS (ss) ====="
ss -tulpen || ss -tuln
echo
echo "===== END ====="
