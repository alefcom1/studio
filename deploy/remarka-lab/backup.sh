#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# Remarka Lab · Monitor — daily Postgres backup
#
# Dumps the `sitelens` database from the running `db` container, gzips it, keeps
# 14 days locally, and (optionally) ships it offsite to the reg.ru VPS via scp.
#
# Install (on the server, as massimo):
#   cp deploy/remarka-lab/backup.sh ~/remarka-lab/sitelens/backup.sh
#   chmod +x ~/remarka-lab/sitelens/backup.sh
#   mkdir -p ~/backups/remarka-lab
#
# Cron (daily 03:30 server time) — `crontab -e`:
#   30 3 * * * /home/massimo/remarka-lab/sitelens/backup.sh >> /home/massimo/backups/remarka-lab/backup.log 2>&1
#
# PII NOTE (added with the K1 client portal, piano-cabinet-k1.md §7.5/§8):
# this dump now also contains the cabinet's cab_* tables — client e-mails,
# names, login IPs/user-agents, audit log. No script change needed (the
# dump already covers the whole `sitelens` DB), but if OFFSITE_HOST is
# enabled below, that destination must stay in the EU and on encrypted
# storage, and consider `gpg`-encrypting the dump before shipping it.
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

# ── Config ───────────────────────────────────────────────────────────────────
COMPOSE_DIR="${COMPOSE_DIR:-/home/massimo/remarka-lab/sitelens}"
BACKUP_DIR="${BACKUP_DIR:-/home/massimo/backups/remarka-lab}"
DB_SERVICE="db"
DB_USER="sitelens"
DB_NAME="sitelens"
RETENTION_DAYS="${RETENTION_DAYS:-14}"

# Offsite (optional). Leave OFFSITE_HOST empty to skip the scp step.
#   OFFSITE_HOST="user@REG-RU-VPS-HOST"
#   OFFSITE_PATH="/home/user/remarka-lab-backups/"
#   OFFSITE_SSH_KEY="/home/massimo/.ssh/regru_key"
OFFSITE_HOST="${OFFSITE_HOST:-}"          # e.g. backup@123.45.67.89
OFFSITE_PATH="${OFFSITE_PATH:-}"          # e.g. /home/backup/remarka-lab/
OFFSITE_SSH_KEY="${OFFSITE_SSH_KEY:-}"    # e.g. /home/massimo/.ssh/regru_key

COMPOSE="docker compose -f docker-compose.yml -f docker-compose.prod.yml"

# ── Dump ─────────────────────────────────────────────────────────────────────
mkdir -p "$BACKUP_DIR"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT="$BACKUP_DIR/sitelens-$STAMP.sql.gz"

echo "[$(date -Is)] Starting pg_dump → $OUT"
cd "$COMPOSE_DIR"

# pg_dump inside the db container; gzip on the host. --clean lets the dump be
# restored over an existing DB. Fail loudly (pipefail) if pg_dump errors.
$COMPOSE exec -T "$DB_SERVICE" pg_dump -U "$DB_USER" --clean --if-exists "$DB_NAME" \
  | gzip -9 > "$OUT"

SIZE="$(du -h "$OUT" | cut -f1)"
echo "[$(date -Is)] Dump complete ($SIZE)"

# ── Rotation ─────────────────────────────────────────────────────────────────
find "$BACKUP_DIR" -name 'sitelens-*.sql.gz' -type f -mtime "+$RETENTION_DAYS" -print -delete
echo "[$(date -Is)] Rotation done (kept last $RETENTION_DAYS days)"

# ── Offsite copy (optional) ──────────────────────────────────────────────────
if [ -n "$OFFSITE_HOST" ] && [ -n "$OFFSITE_PATH" ]; then
  echo "[$(date -Is)] Shipping offsite → $OFFSITE_HOST:$OFFSITE_PATH"
  SCP_OPTS=(-o StrictHostKeyChecking=accept-new)
  [ -n "$OFFSITE_SSH_KEY" ] && SCP_OPTS+=(-i "$OFFSITE_SSH_KEY")
  scp "${SCP_OPTS[@]}" "$OUT" "$OFFSITE_HOST:$OFFSITE_PATH"
  echo "[$(date -Is)] Offsite copy done"
else
  echo "[$(date -Is)] Offsite disabled (set OFFSITE_HOST/OFFSITE_PATH to enable)"
fi

echo "[$(date -Is)] Backup finished OK"

# ─────────────────────────────────────────────────────────────────────────────
# RESTORE (manual, when needed):
#   gunzip -c sitelens-YYYYMMDD-HHMMSS.sql.gz \
#     | docker compose -f docker-compose.yml -f docker-compose.prod.yml \
#         exec -T db psql -U sitelens -d sitelens
#
# EXTERNAL UPTIME MONITORING (e.g. UptimeRobot / Better Uptime / healthchecks.io):
#   Monitor this URL with HTTP Basic Auth (expect HTTP 200 + body {"status":"ok"}):
#     https://lab.remarka.biz/health
#   Set the monitor's credentials to the Caddy Basic Auth user/password.
#   (Optional) also ping a healthchecks.io URL at the end of this script to alert
#   if the daily backup itself stops running:
#     curl -fsS -m 10 https://hc-ping.com/YOUR-UUID > /dev/null || true
# ─────────────────────────────────────────────────────────────────────────────
