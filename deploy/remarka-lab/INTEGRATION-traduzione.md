# Подключение второго сайта traduzione.tech к стеку Hetzner

> Второй WordPress-сайт (traduzione.tech) подселяется в **тот же контейнер
> `wordpress`**, что и remarka.biz — один Apache/PHP обслуживает оба сайта
> через name-based virtual hosting, MariaDB одна, базы разные. Полный
> пошаговый раннбук миграции с REG.RU — в репозитории traduzione.tech,
> `docs/hetzner-migration-traduzione.md`. Здесь — только точки интеграции
> в ЭТОТ репозиторий (studio) и полные копипаст-блоки для сервера.
>
> ⚠️ На боевом сервере ещё НИЧЕГО из этого не применено. Живые `Caddyfile`
> и `backup.sh` намеренно НЕ отредактированы в этой ветке — их правит владелец
> по блокам ниже (чтобы правки remarka.biz оставались под его контролем).

## Новые файлы (безопасны, opt-in — сами по себе ничего не меняют)

| Файл | Роль |
|---|---|
| `docker-compose.traduzione.yml` | 3-й override: второй docroot + маунт vhost + лимит 512M→768M на сервис `wordpress` |
| `apache-traduzione.conf` | vhost Apache для traduzione.tech → `/var/www/traduzione` (грузится как `020-*` ПОСЛЕ `000-default` remarka.biz — дефолтный vhost не меняется) |
| `init-traduzione-db.sql` | создать базу+юзера `traduzione_tech` в общем `wpdb` |
| `wp-config-traduzione.sample.php` | шаблон wp-config второго сайта (заполнить на сервере, секреты не в git) |
| `Caddyfile.traduzione` | site-блоки Caddy (копия блока remarka.biz) — дописать в `Caddyfile` |
| `backup-traduzione.snippet.sh` | дополнение `backup.sh` под второй сайт |

## Расчёт памяти (почему это дёшево)

Apache один → пул PHP-воркеров общий на оба сайта, не удваивается. Буферный
пул MariaDB тоже общий. Прирост от второго сайта ≈ +50–150 МБ RSS (OPcache
второго набора PHP + запас). Лимиты Docker: `wordpress` 768M, `wpdb` 512M
(общий на две базы). Реальный расход двух сайтов ≈ 400–600 МБ. На CX23 (4 ГБ)
вместе с платформой Remarka Lab — тесно (swap); **рекомендован рескейл до
CX33 (8 ГБ)** — та же рекомендация, что уже стоит для remarka.biz.

⚠️ Обратная сторона общего контейнера: при одновременном всплеске трафика
обоих сайтов Apache может упереться в 768M и словить OOM — упадут оба.
Для двух сайтов-визиток редкость; страховка — ограничить `MaxRequestWorkers`
(~10–12) в mpm-конфиге (глобально, затронет и remarka.biz — согласовать).

## Точка интеграции 1 — `Caddyfile` (дописать в конец)

Блоки для traduzione.tech лежат в `Caddyfile.traduzione`. На боевом:

```bash
cd ~/remarka-lab/sitelens
cat Caddyfile.traduzione >> Caddyfile
# На время стейджинга (пока A-запись боевого домена не переключена) —
# временно превратить боевой блок в stage.traduzione.tech, чтобы ACME
# выпустил cert на уже существующую A-запись stage.*:
sed -i '0,/^traduzione\.tech {/s//stage.traduzione.tech {/' Caddyfile
docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec caddy caddy reload --config /etc/caddy/Caddyfile
```

На cutover (фаза 5 раннбука) — вернуть боевой хост:

```bash
cd ~/remarka-lab/sitelens
sed -i 's/^stage\.traduzione\.tech {/traduzione.tech {/' Caddyfile
docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## Точка интеграции 2 — `backup.sh` (вклеить блок второго сайта)

Содержимое `backup-traduzione.snippet.sh` вставить в `backup.sh` СРАЗУ ПОСЛЕ
блока «WordPress remarka.biz» (перед секцией «Rotation»), а также добавить
2 строки ротации и 2 строки offsite — они выписаны в комментариях сниппета.
После правки — проверить прогоном:

```bash
cd ~/remarka-lab/sitelens && ./backup.sh
ls -1 ~/backups/remarka-lab/traduzione-*    # появились db + content архивы
```

## Точка интеграции 3 — поднять второй сайт (после переноса данных с REG.RU)

Полные фазы 1–5 — в `docs/hetzner-migration-traduzione.md` (репо traduzione.tech).
Ядро compose-части (из ~/remarka-lab/sitelens):

```bash
COMPOSE="docker compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.traduzione.yml"
$COMPOSE config --quiet && echo "COMPOSE CONFIG OK"
$COMPOSE up -d wordpress          # пересоздаст контейнер с двумя docroot
```
