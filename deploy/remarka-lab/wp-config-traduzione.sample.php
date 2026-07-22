<?php
/**
 * wp-config.php для traduzione.tech на Hetzner (второй сайт в общем контейнере).
 *
 * Образ wordpress авто-генерирует wp-config ТОЛЬКО для /var/www/html (remarka.biz).
 * Второй docroot /var/www/traduzione образ не трогает — поэтому этот файл кладём
 * руками (перезаписав им wp-config.php, приехавший из дампа REG.RU, у которого
 * реквизиты БД от старого хостинга).
 *
 * ⚠️ Секретов в git быть НЕ должно. Это .sample — реальные пароли/соли
 * подставляются НА СЕРВЕРЕ (см. раннбук docs/hetzner-migration-traduzione.md,
 * фаза 2). Файл на сервере назвать wp-config.php.
 */

// ── База: общий MariaDB-контейнер `wpdb`, но ОТДЕЛЬНАЯ база traduzione_tech ──
define( 'DB_NAME', 'traduzione_tech' );
define( 'DB_USER', 'traduzione' );
define( 'DB_PASSWORD', '__ПОДСТАВИТЬ_TDT_DB_PASSWORD_ИЗ_.env__' );
define( 'DB_HOST', 'wpdb' );            // имя сервиса в docker-сети, НЕ localhost
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', '' );

/**
 * ⚠️ Префикс таблиц ДОЛЖЕН совпадать со старым wp-config.php на REG.RU.
 * Узнать (фаза 1 раннбука):  grep table_prefix wp-config.php
 * Если там не wp_ — заменить здесь, иначе WordPress не найдёт свои таблицы.
 */
$table_prefix = 'wp_';

// ── Соли: сгенерировать УНИКАЛЬНЫЕ (не копировать с remarka.biz!) ──
//    https://api.wordpress.org/secret-key/1.1/salt/  → вставить 8 строк сюда.
define( 'AUTH_KEY',         '__salt__' );
define( 'SECURE_AUTH_KEY',  '__salt__' );
define( 'LOGGED_IN_KEY',    '__salt__' );
define( 'NONCE_KEY',        '__salt__' );
define( 'AUTH_SALT',        '__salt__' );
define( 'SECURE_AUTH_SALT', '__salt__' );
define( 'LOGGED_IN_SALT',   '__salt__' );
define( 'NONCE_SALT',       '__salt__' );

// ── HTTPS за обратным прокси Caddy (иначе редирект-цикл и mixed content) ──
if ( isset( $_SERVER['HTTP_X_FORWARDED_PROTO'] ) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https' ) {
	$_SERVER['HTTPS'] = 'on';
}

// ── Адреса сайта ──
//   Стейджинг (фаза 3–4): https://stage.traduzione.tech
//   Cutover  (фаза 5):    https://traduzione.tech
//   Задаём в БД через search-replace, а не хардкодом — эти define оставить
//   ЗАКОММЕНТИРОВАННЫМИ, если полагаемся на значения в таблице options.
//   Если хотите жёстко зафиксировать на время стейджинга — раскомментировать:
// define( 'WP_HOME',    'https://stage.traduzione.tech' );
// define( 'WP_SITEURL', 'https://stage.traduzione.tech' );

// ── Секреты приложения traduzione.tech (Cloudflare Worker и т.п.) ──
//    НЕ в git. Значения — из docs/launch-checklist.md, подставить на сервере.
// define( 'TDT_WORKER_URL',   '__https://...workers.dev__' );
// define( 'TDT_WORKER_TOKEN', '__secret__' );

define( 'WP_DEBUG', false );

if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}
require_once ABSPATH . 'wp-settings.php';
