-- ─────────────────────────────────────────────────────────────────────────────
-- Создать ВТОРУЮ базу + пользователя в СУЩЕСТВУЮЩЕМ контейнере wpdb (mariadb:11).
-- remarka.biz живёт в базе `wordpress` — её НЕ трогаем. Здесь только новая
-- база traduzione_tech и её пользователь.
--
-- Как выполнить (из ~/remarka-lab/sitelens; пароль root из .env: WP_DB_ROOT_PASSWORD):
--   COMPOSE="docker compose -f docker-compose.yml -f docker-compose.prod.yml"
--   $COMPOSE exec -T wpdb sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD"' \
--     < deploy/hetzner/init-traduzione-db.sql
--
-- ⚠️ Пароль '__ПОДСТАВИТЬ__' заменить на реальный TDT_DB_PASSWORD (тот же, что
-- в wp-config-traduzione). Можно сгенерировать:  openssl rand -hex 24
-- Не коммитить реальный пароль в git.
-- ─────────────────────────────────────────────────────────────────────────────

CREATE DATABASE IF NOT EXISTS traduzione_tech
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'traduzione'@'%' IDENTIFIED BY '__ПОДСТАВИТЬ_TDT_DB_PASSWORD__';

GRANT ALL PRIVILEGES ON traduzione_tech.* TO 'traduzione'@'%';

FLUSH PRIVILEGES;
