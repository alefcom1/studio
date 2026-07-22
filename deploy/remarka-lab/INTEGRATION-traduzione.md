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

## Расчёт памяти + БЕЗ рескейла (решение владельца 22.07.2026)

Apache один → пул PHP-воркеров общий на оба сайта, не удваивается. Буферный
пул MariaDB тоже общий. Прирост от второго сайта ≈ +50–150 МБ RSS (OPcache
второго набора PHP). Лимиты Docker: `wordpress` 768M, `wpdb` 512M (общий на
две базы). Реальный расход двух сайтов ≈ 400–600 МБ.

**Владелец решил рескейл CX33 НЕ делать — остаёмся на CX23 (4 ГБ) + 2 ГБ
swap.** Поэтому в override добавлен `apache-mpm-tuning.conf`, ограничивающий
`MaxRequestWorkers` 150→10 (+ ServerLimit 10). Это ОБЯЗАТЕЛЬНО, а не опция:
без него общий Apache под всплеском трафика вышел бы за 768M и словил OOM
(упали бы оба сайта). 10 воркеров × ~60 МБ + база/OPcache ~150 МБ ≈ 750 МБ
< 768M — держится в лимите под нагрузкой.

⚠️ Файл `apache-mpm-tuning.conf` монтируется как замена дефолтного
`mpm_prefork.conf` и потому ГЛОБАЛЕН — управляет и remarka.biz. Для него это
тоже плюс к безопасности (сейчас 150 дефолтных воркеров на лимите 512M = уже
риск OOM при всплеске), но поведение remarka.biz формально меняется —
**согласовать перед применением.** Остаточный риск (принят): тяжёлый краулинг
Remarka Lab (worker ~1 ГБ) + пик обоих WP-сайтов может выйти за 4 ГБ+swap.

## Точка интеграции 1 — `Caddyfile` (дописать в конец)

Заливаем сразу на боевой домен (без поддомена). Блоки для traduzione.tech —
в `Caddyfile.traduzione`. Пока A-запись не переключена, публичный серт
выпустить нельзя, поэтому на время проверки через hosts-файл включаем
временный `tls internal`:

```bash
cd ~/remarka-lab/sitelens
cat Caddyfile.traduzione >> Caddyfile
sed -i '/^traduzione\.tech {/a tls internal' Caddyfile   # временный self-signed
docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec caddy caddy reload --config /etc/caddy/Caddyfile
```

На cutover (фаза 5 раннбука) — убрать `tls internal`, чтобы Caddy выпустил
настоящий Let's Encrypt-серт после переключения DNS:

```bash
cd ~/remarka-lab/sitelens
sed -i '/^[[:space:]]*tls internal$/d' Caddyfile
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
