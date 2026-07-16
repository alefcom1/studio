# Миграция remarka.biz (WordPress) на сервер Hetzner — раннбук

> Решение владельца 16.07.2026 (см. `docs/server-hetzner.md`). Сайт-визитка
> переезжает с РФ-хостинга (`/var/www/alefcom/data/www/remarka.biz`) на
> Hetzner-сервер платформы (178.105.192.76): один Caddy — три сайта
> (`remarka.biz` + `lab.remarka.biz` + `cab.remarka.biz`), WordPress и
> MariaDB — в контейнерах того же compose-проекта.
>
> **Стратегия: полный dump/restore, НЕ «свежий WP + deploy-import».**
> В живой базе есть то, чего нет в репозитории: лиды check-up, статьи блога,
> настройки Customizer (API-ключи!), конфиг FluentSMTP, счётчики. Переносим
> базу и wp-content целиком — тогда после переезда ничего не надо
> перенастраивать. Стейджинг-проверка на `new.remarka.biz` ДО переключения
> DNS; переключение — отдельной короткой фазой со свежим дампом.
>
> В командах три места выполнения, каждое помечено:
> **[Mac]** — терминал на компьютере владельца;
> **[старый]** — `ssh root@remarka.biz`;
> **[hetzner]** — `ssh hetzner`.

---

## Фаза 0. Ресурсы и DNS-подготовка (10 минут, можно заранее)

1. **[панель Hetzner]** Рекомендуется рескейл CX23 (4 ГБ) → **CX33 (8 ГБ)**:
   Server → Rescale → выбрать CX33, галку «Disk» НЕ увеличивать (тогда
   можно откатиться обратно на CX23). Сервер перезагрузится (~2 мин),
   после ребута проверить **[hetzner]** `docker compose -f docker-compose.yml
   -f docker-compose.prod.yml ps` из `~/remarka-lab/sitelens` — всё
   поднимается само (`restart: unless-stopped`).
   *Обоснование:* лимиты платформы уже 3328M; +WP (512M) +MariaDB (512M)
   = 4352M — на 4 ГБ это жизнь на swap'е, на 8 ГБ — комфорт. Стоимость
   CX33 ≈ вдвое выше CX23 (порядка +5–6 €/мес).
2. **[панель DNS]** Создать A-запись **`new.remarka.biz → 178.105.192.76`**
   (стейджинг-хост).
3. **[панель DNS]** У записей `remarka.biz` (@) и `www` **понизить TTL до
   300** (5 минут) — сам IP пока НЕ менять. Это ускорит cutover в фазе 5.
4. **[панель DNS]** Записи **MX, TXT (SPF/DKIM/DMARC) НЕ трогать вообще** —
   почта домена к переезду сайта отношения не имеет.

## Фаза 1. Снять данные со старого хостинга

**[старый]** — узнать префикс таблиц (понадобится в .env на hetzner):

```bash
grep table_prefix /var/www/alefcom/data/www/remarka.biz/wp-config.php
```

**[Mac]** — выкачать дамп базы и wp-content (тянем через ssh-пайп, на
старом сервере ничего не остаётся):

```bash
ssh root@remarka.biz "wp db export - --allow-root --path=/var/www/alefcom/data/www/remarka.biz | gzip -9" > ~/wp-db.sql.gz
ssh root@remarka.biz "tar czf - -C /var/www/alefcom/data/www/remarka.biz wp-content" > ~/wp-content.tar.gz
ls -lh ~/wp-db.sql.gz ~/wp-content.tar.gz   # оба файла не нулевые
```

**[Mac]** — закинуть на hetzner:

```bash
scp ~/wp-db.sql.gz ~/wp-content.tar.gz hetzner:~/
```

## Фаза 2. Развернуть WordPress-контейнеры на hetzner

**[hetzner]**:

```bash
# 1. Свежий деплой-конфиг из studio
cd ~/remarka-lab
git fetch origin && git checkout claude/new-project-prep-zhmkg5 && git pull
cp deploy/remarka-lab/docker-compose.prod.yml sitelens/
cp deploy/remarka-lab/Caddyfile sitelens/
cp deploy/remarka-lab/backup.sh sitelens/backup.sh
cp deploy/remarka-lab/wp-uploads.ini sitelens/
chmod +x sitelens/backup.sh

# 2. Каталоги данных
cd sitelens
mkdir -p wp-html wp-db

# 3. Переменные WP в существующий .env (пароли сгенерировать!)
cat >> .env <<EOF
WP_DB_PASSWORD=$(openssl rand -hex 24)
WP_DB_ROOT_PASSWORD=$(openssl rand -hex 24)
WP_TABLE_PREFIX=wp_
EOF
nano .env   # WP_TABLE_PREFIX заменить на реальный префикс из фазы 1!

# 4. Поднять wpdb + wordpress + перечитать Caddyfile
docker compose -f docker-compose.yml -f docker-compose.prod.yml config --quiet && echo "COMPOSE CONFIG OK"
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build wpdb wordpress caddy
docker compose -f docker-compose.yml -f docker-compose.prod.yml exec caddy caddy reload --config /etc/caddy/Caddyfile 2>/dev/null || true

# 5. Дождаться, пока образ WP разложит core-файлы (10–20 сек), проверить
sleep 20 && ls wp-html/wp-load.php && echo "WP CORE OK"
```

## Фаза 3. Восстановить данные

**[hetzner]** (из `~/remarka-lab/sitelens`):

```bash
# 1. wp-content поверх свежего (старая тема/плагины/медиа заменяют дефолт)
rm -rf wp-html/wp-content
tar xzf ~/wp-content.tar.gz -C wp-html/
chown -R 33:33 wp-html/wp-content   # www-data внутри контейнера

# 2. Импорт базы
gunzip -c ~/wp-db.sql.gz | docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec -T wpdb sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD" wordpress'

# 3. Обновить схему БД под версию WP образа + перезалить permalinks
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli core update-db
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli rewrite flush

# 4. СТЕЙДЖИНГ: переписать адрес сайта на new.remarka.biz (только для проверки;
#    в фазе 5 будет свежий импорт без этого шага)
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli \
  search-replace 'remarka.biz' 'new.remarka.biz' --skip-columns=guid --all-tables
```

## Фаза 4. Проверка стейджинга (браузер, new.remarka.biz)

- `/`, `/en/`, `/ru/` — открываются, блоки/шрифты/картинки на месте, TLS валиден.
- `/strumenti/check-up-completo/` — прогнать реальный адрес; PDF-отчёт
  приходит на почту (FluentSMTP переехал в базе, должен работать как был).
- ИИ-инструменты работают (ключ Anthropic переехал в базе вместе с
  theme_mods — вводить заново НЕ нужно).
- Форма контактов шлёт письмо; в админке видны лиды и статьи блога.
- Логин в /wp-admin работает (пароли те же — база та же).
- **[hetzner]** `docker stats --no-stream` — wordpress/wpdb в лимитах,
  Monitor/кабинет не деградировали.

Если что-то не так — чинится без спешки: боевой сайт всё ещё на старом
хостинге, DNS не тронут.

## Фаза 5. Cutover (15 минут; лучше в тихие часы)

С момента снятия дампа в фазе 1 на боевом сайте могли появиться новые лиды
и статьи — поэтому дамп снимаем заново, а стейджинг-базу затираем.

```bash
# ── [Mac] свежий дамп и передача ─────────────────────────────────────────────
ssh root@remarka.biz "wp db export - --allow-root --path=/var/www/alefcom/data/www/remarka.biz | gzip -9" > ~/wp-db-final.sql.gz
ssh root@remarka.biz "tar czf - -C /var/www/alefcom/data/www/remarka.biz wp-content" > ~/wp-content-final.tar.gz
scp ~/wp-db-final.sql.gz ~/wp-content-final.tar.gz hetzner:~/

# ── [hetzner] финальный импорт (БЕЗ search-replace — сайт остаётся remarka.biz)
cd ~/remarka-lab/sitelens
rm -rf wp-html/wp-content
tar xzf ~/wp-content-final.tar.gz -C wp-html/
chown -R 33:33 wp-html/wp-content
gunzip -c ~/wp-db-final.sql.gz | docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec -T wpdb sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD" wordpress'
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli core update-db
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli rewrite flush

# ── [hetzner] включить боевые хосты в Caddyfile (раскомментировать блок cutover)
sed -i 's/^# \(remarka\.biz {\)/\1/; s/^# \(www\.remarka\.biz {\)/\1/; s/^# \(\treverse_proxy wordpress:80\)/\1/; s/^# \(\tredir https:\/\/remarka\.biz{uri} permanent\)/\1/; s/^# \(\tlog {\)/\1/; s/^# \(\t\toutput stdout\)/\1/; s/^# \(\t\tformat console\)/\1/; s/^# \(\t}\)/\1/; s/^# \(}\)/\1/' Caddyfile
grep -A2 '^remarka.biz' Caddyfile   # блок должен быть раскомментирован
docker compose -f docker-compose.yml -f docker-compose.prod.yml restart caddy
```

**[панель DNS]** — переключить A-записи: `remarka.biz` (@) и `www` →
**178.105.192.76**. С TTL 300 переключение доедет за ~5 минут.

**[браузер]** — проверить `https://remarka.biz` (сертификат Caddy выпустит
при первом запросе после переключения DNS, до минуты): главная, /en/, /ru/,
инструмент, форма, /wp-admin.

## Фаза 6. После переезда

1. **[hetzner]** `./backup.sh` вручную — убедиться, что появились
   `wordpress-db-*.sql.gz` и `wordpress-content-*.tar.gz` (скрипт уже
   расширен на WP).
2. **[панель DNS]** Через сутки-двое вернуть TTL записей на обычный (3600).
3. **Старый хостинг НЕ отключать 2 недели** (страховка + возможные
   отставшие DNS-кэши). Через 2 недели: снять финальный архив на Mac и
   гасить/не продлевать. ⚠️ Перед отключением проверить, не живут ли на
   старом хостинге почтовые ящики @remarka.biz — если да, почту переносить
   отдельно (MX-записи), сайт этого не касается.
4. Деплой контента сайта теперь идёт по-новому: **сценарии для Hetzner —
   `docs/deploy-cheatsheet.md`, раздел «После переезда»** (wp-cli через
   контейнер wpcli, пути изменились). Старые сценарии с путями
   `/var/www/alefcom/...` больше не действуют.
5. `new.remarka.biz` — A-запись можно удалить (или оставить как стейджинг
   на будущее; Caddy-блок безвреден).

## Откат (если после cutover что-то серьёзно сломалось)

**[панель DNS]** вернуть A-записи `@` и `www` на IP старого хостинга — с
TTL 300 сайт вернётся на старый сервер за ~5 минут. Старый хостинг всё это
время продолжает работать нетронутым.
