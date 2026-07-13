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
скриптом: добавить `-- --force` в конец команды.

> ⚠️ **Правки в файлах `patterns/*.php` (текст/разметка) требуют повторного
> `deploy-import.php --force`**, просто скопировать файл темы недостаточно —
> контент уже лежит в базе как `post_content` конкретной страницы, тема на
> него не влияет. Точечный `curl` одного файла в теме годится только для
> `assets/css`/`assets/js`/`assets/img` (статика, отдаётся напрямую), но не
> для `patterns/` — там нужен полный цикл: обновить файлы темы → запустить
> `deploy-import.php -- --force`.

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
