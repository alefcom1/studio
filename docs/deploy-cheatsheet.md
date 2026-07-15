# Шпаргалка владельца: команды обновления remarka.biz

> Все команды выполняются на сервере по SSH (root@remarka.biz).
> Подробный раннбук с объяснениями — `docs/deploy-ssh.md`. Здесь — только
> «что менялось → что выполнить».

---

## Как выбрать сценарий

| Что изменилось в репозитории | Сценарий |
|---|---|
| Тексты/блоки страниц: `patterns/**`, `deploy-import.php`, новые страницы | **1. Полный цикл** (контент живёт в базе — просто заменить файлы недостаточно) |
| Только код темы: `assets/css`, `assets/js`, `assets/img`, `functions.php`, `inc/`, `lib/` | **2. Синк темы** (быстро, база не трогается) |
| Один файл (например, только `remarka.css`) | **3. Точечный файл** |

Если сомневаетесь — выполняйте сценарий 1: он включает в себя всё и идемпотентен
(повторный запуск ничего не ломает).

---

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
