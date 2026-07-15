# Развёртывание на remarka.biz — шпаргалка по SSH

> Реальные пути и команды сервера, установленные опытным путём
> 13.07.2026. Обновлять по мере изменений на сервере.

## Топология сервера

- Хостинг: VPS, панель в стиле ISPmanager (пути вида `/var/www/<user>/data/www/<domain>`).
- Раздача сайтов — nginx напрямую из файловой системы (без Docker для WordPress).
- **Корень WordPress remarka.biz**:
  ```
  /var/www/alefcom/data/www/remarka.biz
  ```
  (это и есть каталог с `wp-config.php`, `wp-content/` и т.д.)
- На сервере также крутится куча Docker-контейнеров других продуктов группы
  (`tms-*`, `remarka-web/api/worker/converter/postgres/redis/minio`,
  `translateai-app-*`) — **это не WordPress, не трогать** при работе с сайтом.
  Судя по всему это TMS и AI-платформа перевода группы — реальные продукты,
  которые упомянуты в `concept-sviluppo-studio.md` как кандидаты на кейсы
  «Product Lab».
- Другие сайты на этом же сервере (для справки, не трогать):
  `/var/www/alef/data/www/perevod4.ru`, `/var/www/alefcom1/data/www/jivoetelo.ru`.

## Работа под root

Сайт админится с root на этом VPS (single-tenant), поэтому вместо поиска
непривилегированного пользователя проще добавлять `--allow-root` ко всем
командам `wp`. Единственный риск — стандартное предупреждение WP-CLI, для
одиночного VPS это нормально.

## WP-CLI: проверка / установка

```bash
which wp
# если пусто:
curl -sO https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
chmod +x wp-cli.phar
mv wp-cli.phar /usr/local/bin/wp
wp --info --allow-root
```

Дальше во всех командах ниже подразумевается:
```bash
WP="wp --allow-root --path=/var/www/alefcom/data/www/remarka.biz"
```
(или просто дописывать `--allow-root --path=/var/www/alefcom/data/www/remarka.biz`
к каждой команде).

## Бэкап перед любыми изменениями

```bash
tar czf ~/backup-remarka-biz-$(date +%F).tar.gz -C /var/www/alefcom/data/www/remarka.biz wp-content
wp db export ~/backup-remarka-biz-db-$(date +%F).sql --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

## Доставка темы на сервер

> ⚠️ **Точечное обновление одного файла через `curl raw.githubusercontent.com/.../<ветка>/...`
> может отдать УСТАРЕВШУЮ версию** сразу после пуша — у raw.githubusercontent.com
> свой CDN-кэш (Fastly) по имени ветки на несколько минут. Проверено на практике:
> после пуша трёх коммитов подряд `curl` по имени ветки дважды притащил версию
> файла на 1-2 коммита позади реального HEAD (файл не совпадал по содержимому,
> хотя сама команда отрабатывала без ошибок). Правильно — тянуть по точному
> **хэшу коммита**, у него неизменяемый адрес и кэш не мешает:
> ```bash
> curl -sL https://raw.githubusercontent.com/alefcom1/studio/<commit-sha>/wordpress/remarka-studio/assets/css/remarka.css \
>   -o /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/assets/css/remarka.css
> ```
> После любого точечного обновления файла — обязательно `grep` на признак
> самой свежей правки, чтобы убедиться, что реально прилетел актуальный контент,
> а не просто отсутствие ошибки в `curl`.

**Вариант А — git clone прямо на сервере:**
```bash
cd /tmp
git clone --depth 1 -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
cp -r studio/wordpress/remarka-studio /var/www/alefcom/data/www/remarka.biz/wp-content/themes/
rm -rf studio
```

**Вариант Б — rsync с локальной машины (выполнять у себя, не на сервере):**
```bash
git clone -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
cd studio
rsync -avz --delete wordpress/remarka-studio/ root@remarka.biz:/var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/
```

## Права доступа

```bash
cd /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
```

## Активация темы

```bash
wp theme activate remarka-studio --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

## ⚠️ Обязательный шаг: .htaccess (иначе все вложенные URL будут 404)

На этом сервере nginx — просто reverse proxy (`proxy_pass http://127.0.0.1:81`),
а реальный движок — **Apache** на 127.0.0.1:81 (FastPanel-конфигурация).
Без `.htaccess` Apache отдаёт СВОЙ 404 (не доходя до WordPress) на любой URL,
который не совпадает с реальным файлом — то есть все "красивые" адреса вида
`/servizi/siti-aziendali/` ломаются, а `/` работает (это DirectoryIndex).
Признак именно этой проблемы: тело 404-ответа содержит
`Apache/2.4.58 (Ubuntu) Server at remarka.biz` — если видите это, дело не в
WordPress и не в permalinks, а именно в отсутствующем `.htaccess`.

`AllowOverride All` на сервере уже включён (проверено), поэтому достаточно
создать файл. `wp rewrite flush --hard` его НЕ создаёт при запуске от root
(предупреждает "Regenerating a .htaccess file requires special configuration")
— нужно вручную:

```bash
cat > /var/www/alefcom/data/www/remarka.biz/.htaccess << 'HTACCESS'
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
HTACCESS
chown alefcom:alefcom /var/www/alefcom/data/www/remarka.biz/.htaccess
chmod 644 /var/www/alefcom/data/www/remarka.biz/.htaccess
```

Проверка: `curl -sI https://remarka.biz/servizi/siti-aziendali/` должен
вернуть `200 OK`, а не 404 с адресом Apache в теле ответа.

## Импорт всех страниц + меню + главная (deploy-import.php)

Скрипт лежит в репозитории: `wordpress/build-tools/deploy-import.php`.
Скопировать его в тему и запустить через `wp eval-file`:

```bash
cp studio/wordpress/build-tools/deploy-import.php \
   /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/deploy-import.php

wp eval-file /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/deploy-import.php \
   --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

Идемпотентен: повторный запуск ничего не сломает (существующие страницы
пропускаются). Для принудительного обновления страниц, созданных этим же
скриптом: поставить `REMARKA_FORCE=1` перед командой `wp eval-file`.

> ⚠️ **`wp eval-file file.php --force` не работает** — wp-cli проверяет
> каждый `--xxx`-токен по списку опций команды `eval-file` ещё ДО запуска
> самого файла, `--force` там не объявлен, поэтому команда падает с
> `Error: unknown --force parameter` (даже если поставить `--` перед ним).
> Поэтому флаг читается из переменной окружения, а не из аргумента:
> `REMARKA_FORCE=1 wp eval-file ... --allow-root --path=...`

> ⚠️ **Правки в файлах `patterns/*.php` (текст/разметка) требуют повторного
> `REMARKA_FORCE=1 wp eval-file deploy-import.php`**, просто скопировать
> файл темы недостаточно — контент уже лежит в базе как `post_content`
> конкретной страницы, тема на него не влияет. Точечный `curl` одного файла
> в теме годится только для `assets/css`/`assets/js`/`assets/img` (статика,
> отдаётся напрямую), но не для `patterns/` — там нужен полный цикл: обновить
> файлы темы → запустить
> `deploy-import.php -- --force`.

> ⚠️ **Баг (исправлен): `REMARKA_FORCE=1` мог унести в корзину саму Home**
> (и языковые главные `/en/`, `/ru/`). Раздел «2b. Pulizia pagine orfane»
> считает страницу «осиротевшей» и удаляет её, если её slug не встречается
> в `$page_map` — а Home/`en`/`ru` создаются отдельным путём (§1/§1b) и в
> `$page_map` никогда не попадали. Итог при первом же `--force`-деплое с
> расширившимся списком страниц (мультиязычный релиз): Home пропала,
> большинство URL стали отдавать 404 (главная была `page_on_front`, её
> исчезновение ломает и роутинг). Исправлено в коммите после этого —
> `home`, `en`, `ru` теперь всегда в списке защищённых slug'ов. Если после
> обновления кода `deploy-import.php` всё ещё видно похожее поведение,
> см. диагностику/восстановление ниже.

> ℹ️ **С фазы B у RU-главной собственный набор секций.** `deploy-import.php`
> теперь содержит отдельный список `$home_sections_ru` (13 секций из
> `patterns/lang-ru/`: hero-home, trust-strip, vyhod-evropa, tre-numeri,
> manifesto, seo-lingue, servizi-cards, caso-evidenza, come-lavoriamo,
> garanzie-dark, prezzi-teaser, faq, contatti) — RU-воронка самодостаточна и
> не зеркалит IT/EN (без `lingue-mercati`/`strumenti-cards`, вместо них
> `vyhod-evropa`/`seo-lingue`). Из-за этого предупреждение
> «`[ru] sezione mancante: lingue-mercati.php`», которое раньше появлялось
> при каждом деплое (RU использовал общий IT-список секций), больше не
> выводится — это ожидаемо, не повод искать регрессию.

## После импорта — ручные шаги

1. Внешний вид → Настроить → загрузить логотип (астериск), настроить меню
   (уже соберёт скрипт, но можно поправить порядок пунктов).
2. Внешний вид → Настроить → **Remarka — Contatti** → реальный номер WhatsApp.
3. Настройки → Постоянные ссылки → сохранить (на всякий случай, чтобы
   применились иерархические URL /servizi/siti-aziendali/ и т.д.).
4. Заменить P.IVA/адрес/телефон/скриншоты кейсов на реальные данные.
5. Проверить Lighthouse mobile на Home и одной внутренней странице.

## Диагностика (если что-то пойдёт не так)

```bash
# где физически лежит сайт (если путь вдруг изменится)
find / -name "wp-config.php" 2>/dev/null

# что раздаёт 80/443 и document root по доменам
nginx -T 2>/dev/null | grep -i "root\|server_name"

# список тем и активная тема
wp theme list --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# логи nginx/php при ошибках 500 после активации темы
tail -50 /var/log/nginx/error.log
wp eval 'error_reporting(E_ALL); ini_set("display_errors",1);' --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

### Дубли EN/RU в корне сайта (без /en//ru/) — найдены через Screaming Frog orphan-report

Во время инцидента с пропавшей Home (14.07.2026) резолвинг родителя `en`/`ru`
на секунду сломался в середине прогона — весь EN/RU-комплект страниц создался
**один раз в корне** (`/services/business-websites/` вместо
`/en/services/business-websites/`, и так далее для всего дерева, включая
`/pricing/`, `/uslugi/`, `/kejsy/`, `/instrumenty/`, `/blog/<en-или-ru-slug>/`
и т.д.). Позже, после фикса, скрипт создал **второй, уже правильно
вложенный** комплект под `en`/`ru` — но старый в корне остался висеть, потому
что «зачистка осиротевших страниц» в deploy-import.php сверяет только голый
`post_name`, а не полный путь: `services` в корне и `services` под `en`
неотличимы друг от друга для этой проверки.

Обнаруживается это по отчёту типа Screaming Frog «Orphan pages» (страницы,
которые есть в sitemap, но на которые нет ни одной внутренней ссылки) —
все дубли-сироты попадают именно туда.

**Признак**: страницы с `post_parent = 0` и `post_date`, совпадающим с
моментом сбоя (в данном случае `2026-07-14 06:21:05`/`06:21:06`), у которых
slug совпадает со slug'ом настоящей страницы под `en`/`ru`.

```bash
# найти дубли по временному окну инцидента (подставить свою дату/время сбоя)
wp post list --post_type=page --post_status=publish \
  --date_query='[{"after":"2026-07-14 06:21:04","before":"2026-07-14 06:21:07","inclusive":true}]' \
  --fields=ID,post_parent,post_name,post_title \
  --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# после проверки списка — в корзину (обратимо, не hard delete)
wp post list --post_type=page --post_status=publish \
  --date_query='[{"after":"2026-07-14 06:21:04","before":"2026-07-14 06:21:07","inclusive":true}]' \
  --field=ID --allow-root --path=/var/www/alefcom/data/www/remarka.biz \
  | xargs -I{} wp post update {} --post_status=trash --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

Чтобы старые проиндексированные плоские URL не превращались в 404,
`inc/multilang.php` теперь содержит `remarka_redirect_legacy_flat_urls()` —
301-редирект, построенный автоматически из `inc/lang-map.php` (для каждого
en/ru-пути минус языковой префикс). Работает независимо от того, снесены ли
уже дубли-сироты из базы — редирект перехватывает запрос на `template_redirect`
раньше рендера страницы. Не требует ручного списка URL — синхронизирован с
`lang.py` автоматически.

### Эндпоинт `remarka_tool_fetch` (инструменты Lab: GDPR/AI) — SSRF, rate-limit, диагностика 429

`wp_ajax_remarka_tool_fetch` / `wp_ajax_nopriv_remarka_tool_fetch` в
`functions.php` (`remarka_tool_fetch_handler`, около строки 1151) — серверный
прокси-фетч чужих URL для инструментов на `/strumenti/`, которым нужен доступ
к чужому сайту (Check GDPR — сырой HTML, Sito pronto per l'AI — llms.txt/
robots.txt/sitemap.xml): браузер не может зафетчить произвольный домен
из-за CORS, поэтому запрос уходит через WordPress-сервер.

**SSRF-защита** (`remarka_tool_check_url`, `remarka_tool_is_blocked_ip`,
`remarka_tool_resolve_host`, `remarka_tool_safe_fetch` — реальный код, не
пересказ):
- схема — только `http`/`https` (иначе `schema_non_ammesso`);
- порт — только 80/443 (иначе `porta_non_ammessa`);
- хост резолвится в A+AAAA, и **каждый** полученный IP проверяется через
  `filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)`
  — блокирует приватные/зарезервированные диапазоны (127/8, 10/8, 172.16/12,
  192.168/16, 169.254/16, 0/8, `::1`, `fc00::/7`, `fe80::/10` и весь
  остальной IANA-reserved), а не только жёстко прошитый список;
- редиректы — ручной цикл (`wp_remote_get` с `redirection => 0`), максимум
  3 хопа; на каждом хопе `Location` резолвится заново и **повторно**
  проходит ту же SSRF-проверку (защита от редиректа на приватный IP уже
  после первой валидной проверки хоста);
- таймаут — 8 секунд (`timeout => 8`);
- тело — обрезается до 512 КБ (`limit_response_size` + ручной `substr` на
  случай превышения);
- Content-Type — принимаются `text/*` плюс несколько текстовых XML/JSON
  типов (`application/xml`, `application/xhtml+xml`, `application/json`,
  `application/rss+xml`, `application/atom+xml`, `application/ld+json`) —
  расширено сознательно относительно чистого «только text/*», иначе не
  прошли бы `sitemap.xml` и JSON-LD;
- режимы (`mode`) — `html` (весь URL) или `path:llms.txt` / `path:robots.txt`
  / `path:sitemap.xml`, белый список путей в `remarka_tool_target_url`,
  остальное отклоняется (`path_non_ammesso`).
- отдельный nonce `remarka_tools` (не переиспользует `remarka_contact`),
  без валидного nonce — HTTP 403.

**Rate-limit:** transient `remarka_tl_` + `md5($ip)` по `REMOTE_ADDR`,
лимит 10 запросов/мин, инкремент через `set_transient(..., MINUTE_IN_SECONDS)`.
При превышении — `wp_send_json_error(..., 429)`.

**Диагностика HTTP 429 на проде:**

```bash
# если нет persistent object cache — transient лежит в wp_options
wp option list --search='_transient_remarka_tl_*' \
  --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp option get _transient_remarka_tl_<md5-ip> \
  --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# сбросить лимит вручную для конкретного IP (или просто подождать минуту —
# транзиент истекает сам через MINUTE_IN_SECONDS)
wp option delete _transient_remarka_tl_<md5-ip> \
  --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp option delete _transient_timeout_remarka_tl_<md5-ip> \
  --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

Если на сервере включён persistent object cache (Redis/Memcached),
транзиент **не** появится в `wp_options` — искать в кэше или просто ждать
минуту истечения.

⚠️ **Нюанс шаред-хостинга/NAT:** лимит считается по «сырому»
`$_SERVER['REMOTE_ADDR']`, без учёта `X-Forwarded-For`. Несколько
посетителей за одним NAT/корпоративным прокси/мобильным оператором делят
один и тот же внешний IP — если кто-то из них уже исчерпал лимит, следующий
пользователь за тем же IP тоже получит 429, хотя сам не превышал квоту.
Это ожидаемое поведение простого IP-лимита, не баг; при жалобах пользователя
на 429 стоит уточнить, не сидит ли он за общим корпоративным/мобильным IP.

### Check-up: PDF-отчёты и лиды

Эндпоинт `remarka_tool_report` (`wp_ajax_remarka_tool_report` /
`wp_ajax_nopriv_remarka_tool_report` в `functions.php`,
`remarka_tool_report_handler`) отправляет на e-mail PDF-отчёт check-up
completo и сохраняет лид. Порядок проверок в хендлере: nonce `remarka_tools`
→ honeypot (`sr_checkup_hp`, тихий успех без действий) → rate-limit по IP
(transient `remarka_rpt_` + `md5($ip)`, **3 запроса/час**, отдельный от
`remarka_tl_` у `remarka_tool_fetch`) → email/`consent` обязательны → JSON
`payload` санифицируется (`remarka_tool_report_sanitize_payload`: whitelist
ключей, числа клампятся 0–100, `url` только http/https, `locale`
whitelist `it|en|ru`). Композит и «measured» из клиента **игнорируются** —
пересчитываются на сервере из `scores` (`remarka_checkup_composite`), чтобы
PDF был внутренне непротиворечив, даже если клиент прислал что-то другое.

**Библиотека PDF:** `wordpress/remarka-studio/lib/dompdf/` — бандл dompdf
3.1.5 + php-font-lib 1.0.2 + php-svg-lib 1.0.2 + masterminds/html5 2.10.1 +
sabberworm/php-css-parser 9.4.0 + подмножество thecodingmachine/safe 3.4.0
(только 4 функции, реально используемые css-parser — не все ~80 upstream).
Версии и лицензии — `lib/dompdf/VERSIONS.md`. Автолоадер собственный
(`lib/dompdf/autoload.php`, PSR-4 вручную), не composer — тема не тянет
`vendor/` на проде. Шрифты — только 3 файла DejaVu (Sans, Sans-Bold,
SansMono; кириллица из коробки) в `lib/dompdf/dompdf/lib/fonts/`;
регистрируются в **писуемый** кэш-каталог `wp-content/uploads/checkup-reports/fonts/`
при каждой генерации (`FontMetrics::registerFont()` пишет туда, не в тему).

**Шаблон/копирайт отчёта:** `inc/checkup-report-pdf.php` —
`remarka_checkup_render_html()` (12-страничный HTML, IT/EN/RU verbatim из
`docs/copy-checkup.md` §2.5/3.5/4.5) → `remarka_checkup_render_pdf()`
(конвертация в PDF). Рантайм-проверка расширений PHP —
`remarka_checkup_pdf_missing_extensions()`: `dom`, `mbstring`, `gd`; если
хоть одного нет — эндпоинт отвечает JSON `{success:false, code:"pdf_unavailable"}`
(HTTP 500), а не падает фатально:

```bash
php -m | grep -Ei '^(dom|mbstring|gd)$'
# если чего-то не хватает на проде (обычно PHP-FPM собран без модуля):
apt list --installed 2>/dev/null | grep -Ei 'php.*-(dom|mbstring|gd)'
# Debian/Ubuntu: sudo apt install php-dom php-mbstring php-gd && systemctl restart php*-fpm
```

Файл PDF пишется временно в `wp-content/uploads/checkup-reports/`
(имя случайное, `wp_generate_password()`), с `index.php`-заглушкой в папке
против листинга директории; после `wp_mail()` с вложением файл **удаляется**
(`wp_delete_file()`) — на диске не остаётся копий отчётов, только e-mail
у получателя.

**Лиды — CPT `sr_lead`** (приватный: `public => false`, виден в админке
только `manage_options`, пункт меню «Lead check-up»). Список:
`Site → Lead check-up`, колонки Email · Sito · Punteggio · Lingua ·
Monitoraggio · Data. **Удаление лида из админки — это полное удаление
данных** (post + все post_meta: email, url, punteggio, locale, consenso
monitoraggio): используйте это как ответ на запрос об удалении по GDPR, без
дополнительных шагов.

```bash
# lead via WP-CLI (email/url/punteggio/lingua sono post_meta)
wp post list --post_type=sr_lead --allow-root \
  --path=/var/www/alefcom/data/www/remarka.biz \
  --fields=ID,post_title,post_date
wp post meta list <ID> --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

**Curl-диагностика эндпоинта.** Проверка ordine dei controlli: nonce viene
verificato **prima** di tutto il resto — con un nonce finto si resta sempre
a 403, quindi per vedere 400/429 serve un nonce reale, con cookie di sessione
anonima coerenti (li tiene un cookie-jar):

```bash
JAR=/tmp/remarka-cookies.txt

# 403 — nonce inventato (nessun cookie/nonce reale necessario)
curl -s -o /dev/null -w '%{http_code}\n' https://remarka.biz/wp-admin/admin-ajax.php \
  -d action=remarka_tool_report -d nonce=INVALIDO -d email=x -d consent=1
# → 403

# nonce reale: scaricare la pagina check-up e leggerlo da window.remarkaPSI
# (stesso cookie-jar, altrimenti il nonce non sarà valido per le richieste dopo)
NONCE=$(curl -s -c "$JAR" https://remarka.biz/strumenti/check-up-completo/ \
  | grep -oE '"toolsNonce":"[a-f0-9]+"' | head -1 | grep -oE '[a-f0-9]+$')
echo "nonce=$NONCE"

# 400 — email non valida (nonce reale, consenso presente)
curl -s -b "$JAR" -o /dev/null -w '%{http_code}\n' https://remarka.biz/wp-admin/admin-ajax.php \
  -d action=remarka_tool_report -d "nonce=$NONCE" -d email=non-una-email -d consent=1
# → 400 {"code":"invalid_email"}

# 429 — rate-limit: 4 richieste di fila dallo stesso IP entro un'ora
# (l'incremento del contatore avviene subito dopo il controllo del limite,
# quindi anche richieste poi respinte per email/payload contano nel conteggio)
for i in 1 2 3 4; do
  curl -s -b "$JAR" -o /dev/null -w '%{http_code}\n' https://remarka.biz/wp-admin/admin-ajax.php \
    -d action=remarka_tool_report -d "nonce=$NONCE" -d email=non-una-email -d consent=1
done
# → 400, 400, 400, 429 (il 4° scatta sul rate-limit, code=rate_limit)
```

### Пропала главная страница / почти всё 404 после `--force`-деплоя

```bash
# 1. Home в корзине?
wp post list --post_status=trash --post_type=page \
   --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# 2. что сейчас установлено как главная
wp option get show_on_front --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp option get page_on_front --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# 3. если Home (post_name=home) в корзине — восстановить и переустановить как главную
wp post update <ID> --post_status=publish --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp option update show_on_front page --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp option update page_on_front <ID> --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# 4. то же самое проверить для 'en' и 'ru' (главные языковых разделов),
#    если /en/ или /ru/ отдают 404 — они тоже могли попасть в корзину
wp post list --post_status=trash --post_type=page --name=en \
   --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp post list --post_status=trash --post_type=page --name=ru \
   --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# 5. после восстановления — освежить постоянные ссылки
wp rewrite flush --allow-root --path=/var/www/alefcom/data/www/remarka.biz

# 6. обновить deploy-import.php в теме на исправленную версию и перезапустить,
#    чтобы больше ни одна защищённая страница не попала под нож при следующем --force
```
