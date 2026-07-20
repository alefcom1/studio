# Шпаргалка владельца: команды обновления remarka.biz

> ⚠️ **Сайт живёт на Hetzner** (подтверждено владельцем 18.07.2026):
> актуальные сценарии — **H0–H3** в разделе «После переезда на Hetzner»
> ниже, команды на `ssh hetzner`. Сценарии 1–3 сразу под этой шапкой —
> АРХИВ старого хостинга (`/var/www/alefcom/...`), их не выполнять.
> Подробный раннбук с объяснениями — `docs/deploy-ssh.md`. Здесь — только
> «что менялось → что выполнить».
> В блоках клонирования подставляйте ветку с изменениями, о которой идёт
> речь в отчёте (в примерах указана ветка одного из прошлых деплоев).

---

## Как выбрать сценарий

| Что изменилось в репозитории | Сценарий |
|---|---|
| Тексты/блоки страниц: `patterns/**`, `deploy-import.php`, новые страницы | **Полный цикл** (контент живёт в базе — просто заменить файлы недостаточно) |
| Только код темы: `assets/css`, `assets/js`, `assets/img`, `functions.php`, `inc/`, `lib/` | **Синк темы** (быстро, база не трогается) |
| Один файл (например, только `remarka.css`) | **Точечный файл** |

Если сомневаетесь — выполняйте «Полный цикл»: он включает в себя всё и
идемпотентен (повторный запуск ничего не ломает).

---

## ~~Сценарии 1–3 (старый хостинг)~~ — АРХИВ, не выполнять

## 0. Бэкап (перед любым сценарием — 20 секунд)

```bash
tar czf ~/backup-remarka-biz-$(date +%F).tar.gz -C /var/www/alefcom/data/www/remarka.biz wp-content
wp db export ~/backup-remarka-biz-db-$(date +%F).sql --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

---

## 1. Полный цикл (изменился контент страниц)

```bash
cd /tmp && git clone --depth 1 -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
cp -r studio/wordpress/remarka-studio /var/www/alefcom/data/www/remarka.biz/wp-content/themes/
cd /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio
find . -type d -exec chmod 755 {} \; && find . -type f -exec chmod 644 {} \;

cp /tmp/studio/wordpress/build-tools/deploy-import.php ./deploy-import.php
REMARKA_FORCE=1 wp eval-file ./deploy-import.php --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp cache flush --allow-root --path=/var/www/alefcom/data/www/remarka.biz
rm -rf /tmp/studio
```

⚠️ `REMARKA_FORCE=1` — переменная окружения ПЕРЕД командой. Флаг `--force`
у `wp eval-file` не работает (падает с ошибкой).

## 2. Синк темы (изменился только код: CSS/JS/PHP/картинки)

```bash
cd /tmp && git clone --depth 1 -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
cp -r studio/wordpress/remarka-studio /var/www/alefcom/data/www/remarka.biz/wp-content/themes/
cd /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio
find . -type d -exec chmod 755 {} \; && find . -type f -exec chmod 644 {} \;
wp cache flush --allow-root --path=/var/www/alefcom/data/www/remarka.biz
rm -rf /tmp/studio
```

## 3. Точечный файл

⚠️ Тянуть ТОЛЬКО по хэшу коммита, не по имени ветки — CDN GitHub кэширует
ветку и может отдать устаревшую версию. Хэш смотрите в `git log` или спросите
у меня. Годится только для `assets/**` — файлы `patterns/` так обновлять
бессмысленно (см. сценарий 1).

```bash
curl -sL https://raw.githubusercontent.com/alefcom1/studio/<ХЭШ-КОММИТА>/wordpress/remarka-studio/assets/css/remarka.css \
  -o /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/assets/css/remarka.css
# после скачивания — проверить, что прилетела свежая версия:
grep -c 'sr-checkup' /var/www/alefcom/data/www/remarka.biz/wp-content/themes/remarka-studio/assets/css/remarka.css
```

---

## После переезда на Hetzner — АКТУАЛЬНЫЕ сценарии (docs/migrazione-wp-hetzner.md)

remarka.biz живёт на Hetzner: сценарии 1–3 выше — архив старого хостинга
(пути `/var/www/alefcom/...` там и остались). Действующие эквиваленты —
все команды на **`ssh hetzner`**, из каталога `~/remarka-lab/sitelens`:

### H0. Бэкап (перед любым сценарием)

```bash
cd ~/remarka-lab/sitelens && ./backup.sh
```

### H1. Полный цикл (изменился контент страниц)

```bash
cd ~/remarka-lab/sitelens
COMPOSE="docker compose -f docker-compose.yml -f docker-compose.prod.yml"

cd /tmp && rm -rf studio && git clone --depth 1 -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
# sudo обязателен: файлы темы на сервере принадлежат www-data (33) после
# предыдущего деплоя, обычный cp массимо их НЕ перезапишет (тихо, частично).
sudo rm -rf ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio
sudo cp -r studio/wordpress/remarka-studio ~/remarka-lab/sitelens/wp-html/wp-content/themes/
sudo cp studio/wordpress/build-tools/deploy-import.php ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio/deploy-import.php
sudo chown -R 33:33 ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio
rm -rf /tmp/studio

cd ~/remarka-lab/sitelens
$COMPOSE run --rm -e REMARKA_FORCE=1 wpcli eval-file wp-content/themes/remarka-studio/deploy-import.php
$COMPOSE run --rm wpcli cache flush
```

⚠️ `REMARKA_FORCE=1` теперь передаётся через `-e` у `docker compose run`
(это тот же принцип «переменная окружения, не флаг»).

### H2. Синк темы (изменился только код: CSS/JS/PHP/картинки)

```bash
cd /tmp && rm -rf studio && git clone --depth 1 -b claude/new-project-prep-zhmkg5 https://github.com/alefcom1/studio.git
sudo rm -rf ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio
sudo cp -r studio/wordpress/remarka-studio ~/remarka-lab/sitelens/wp-html/wp-content/themes/
sudo chown -R 33:33 ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio
rm -rf /tmp/studio
cd ~/remarka-lab/sitelens
docker compose -f docker-compose.yml -f docker-compose.prod.yml run --rm wpcli cache flush
```

### H3. Точечный файл (только по хэшу коммита, как раньше)

```bash
sudo curl -sL https://raw.githubusercontent.com/alefcom1/studio/<ХЭШ-КОММИТА>/wordpress/remarka-studio/assets/css/remarka.css \
  -o ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio/assets/css/remarka.css
sudo chown 33:33 ~/remarka-lab/sitelens/wp-html/wp-content/themes/remarka-studio/assets/css/remarka.css
```

Откат после переезда: восстановить из `~/backups/remarka-lab/wordpress-*`
(см. RESTORE-комментарий в backup.sh; база — `mariadb` вместо `psql`).

## Проверка после обновления

- Три главные: `/`, `/en/`, `/ru/` — открываются, блоки на месте.
- Если меняли инструменты: прогнать реальный адрес на `/strumenti/check-up-completo/`.
- Если меняли PDF/почту: отправить себе отчёт с формы, письмо должно прийти
  на языке страницы; лиды — в админке, меню «Lead check-up».
- Кэш-плагин (если установлен) — очистить кэш из админки.

## Откат (если что-то пошло не так)

```bash
# файлы темы:
tar xzf ~/backup-remarka-biz-<ДАТА>.tar.gz -C /var/www/alefcom/data/www/remarka.biz
# база (вернёт и контент страниц):
wp db import ~/backup-remarka-biz-db-<ДАТА>.sql --allow-root --path=/var/www/alefcom/data/www/remarka.biz
wp cache flush --allow-root --path=/var/www/alefcom/data/www/remarka.biz
```

## Частые вопросы

- **Сайт отдаёт 404 после импорта** → `wp rewrite flush --allow-root --path=...`,
  затем проверить «Настройки → Постоянные ссылки».
- **Инструменты пишут «Riprovate tra qualche minuto»** → сработал rate-limit
  (10 проверок/мин с IP) — это защита, не поломка; подробнее в `deploy-ssh.md`.
- **Письмо с PDF не приходит** → проверить FluentSMTP (лог отправки в админке)
  и папку спама; лид при этом всё равно сохраняется в «Lead check-up».
