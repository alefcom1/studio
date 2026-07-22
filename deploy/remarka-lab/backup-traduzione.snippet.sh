# ─────────────────────────────────────────────────────────────────────────────
# Дополнение к backup.sh (репо studio, deploy/remarka-lab/backup.sh) для
# бэкапа второго сайта traduzione.tech. Вставить СРАЗУ ПОСЛЕ блока
# «WordPress remarka.biz» (после строки, где закрывается его if/else,
# перед секцией «Rotation»).
#
# Логика та же, что у remarka.biz: если база traduzione_tech существует и есть
# docroot wp-html-traduzione — дампим mariadb + tar wp-content второго сайта.
# ─────────────────────────────────────────────────────────────────────────────

# ── WordPress traduzione.tech (второй сайт, общий контейнер) ──────────────────
TDT_DB_OUT="$BACKUP_DIR/traduzione-db-$STAMP.sql.gz"
if $COMPOSE exec -T wpdb sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD" -e "USE traduzione_tech"' 2>/dev/null && [ -d "wp-html-traduzione" ]; then
  echo "[$(date -Is)] Dumping traduzione.tech DB → $TDT_DB_OUT"
  $COMPOSE exec -T wpdb sh -c 'mariadb-dump -u root -p"$MARIADB_ROOT_PASSWORD" traduzione_tech' \
    | gzip -9 > "$TDT_DB_OUT"
  echo "[$(date -Is)] traduzione.tech DB dump complete ($(du -h "$TDT_DB_OUT" | cut -f1))"

  TDT_FILES_OUT="$BACKUP_DIR/traduzione-content-$STAMP.tar.gz"
  echo "[$(date -Is)] Archiving traduzione wp-content → $TDT_FILES_OUT"
  tar -czf "$TDT_FILES_OUT" -C "$COMPOSE_DIR/wp-html-traduzione" wp-content
  echo "[$(date -Is)] traduzione wp-content archive complete ($(du -h "$TDT_FILES_OUT" | cut -f1))"
else
  echo "[$(date -Is)] traduzione.tech not deployed yet — skipping"
  TDT_DB_OUT=""
  TDT_FILES_OUT=""
fi

# И в секции Rotation добавить две строки:
#   find "$BACKUP_DIR" -name 'traduzione-db-*.sql.gz'      -type f -mtime "+$RETENTION_DAYS" -print -delete
#   find "$BACKUP_DIR" -name 'traduzione-content-*.tar.gz' -type f -mtime "+$RETENTION_DAYS" -print -delete
#
# И в секции Offsite (если включена) добавить:
#   [ -n "$TDT_DB_OUT" ]    && scp "${SCP_OPTS[@]}" "$TDT_DB_OUT"    "$OFFSITE_HOST:$OFFSITE_PATH"
#   [ -n "$TDT_FILES_OUT" ] && scp "${SCP_OPTS[@]}" "$TDT_FILES_OUT" "$OFFSITE_HOST:$OFFSITE_PATH"
