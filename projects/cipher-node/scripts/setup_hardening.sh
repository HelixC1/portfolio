#!/bin/bash
# CIPHER-NODE — Embedded hardening checklist (run on target Linux)
set -euo pipefail

echo "=== CIPHER-NODE Hardening ==="

echo "[1/4] Disable unused services..."
# systemctl disable telnet 2>/dev/null || true

echo "[2/4] Firewall — default deny inbound..."
# iptables -P INPUT DROP
# iptables -A INPUT -i lo -j ACCEPT
# iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

echo "[3/4] TLS — enforce TLS 1.3 minimum..."
# openssl s_client -connect broker:8883 -tls1_3

echo "[4/4] Rotate default credentials..."
# passwd sensor_user

echo "Hardening script completed (demo mode — uncomment on target)."
