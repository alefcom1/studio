# Remarka Studio — дочерняя тема Prespa

Дизайн-система Studio Remarka для WordPress: токены в `theme.json`,
компоненты в `assets/css/remarka.css`, анимации в `assets/js/remarka.js`,
контент собирается из Gutenberg-паттернов категории **Remarka**.

## Установка

1. Скопировать папку `remarka-studio` в `wp-content/themes/`
   (рядом с `prespa` и `prespa-saas`).
2. Внешний вид → Темы → активировать **Remarka Studio**.
   Родительская тема **Prespa** должна оставаться установленной.
3. Внешний вид → Настроить:
   - логотип — загрузить SVG/PNG астериск (из `public/favicon.svg` репозитория);
   - меню: Servizi · Casi studio · Prezzi · Strumenti · Blog;
   - последнему пункту меню («Preventivo in 24 ore», ссылка `/#contatti`)
     задать CSS-класс `sr-menu-cta` — он станет синей кнопкой.
     (Классы пунктов меню включаются в «Настройки экрана» наверху.)

## Шрифты

Пока файлов шрифтов нет, тема автоматически грузит их с CDN (Fontshare + Google).
Для продакшена (скорость + GDPR) положить в `assets/fonts/`:

- `ClashDisplay-Medium.woff2`, `ClashDisplay-Semibold.woff2` — [Fontshare](https://www.fontshare.com/fonts/clash-display)
- `GeneralSans-Regular.woff2`, `GeneralSans-Medium.woff2`, `GeneralSans-Semibold.woff2` — [Fontshare](https://www.fontshare.com/fonts/general-sans)
- `FragmentMono-Regular.woff2` — [Google Fonts](https://fonts.google.com/specimen/Fragment+Mono)

Как только появляется `ClashDisplay-Semibold.woff2`, тема сама переключается
на самохостинг (проверка `file_exists` в `functions.php`). Проверить лицензию
Fontshare для коммерческого использования.

## Как редактировать (для владельца)

**Тексты**: любой заголовок, абзац, кнопка, ссылка — обычные блоки Gutenberg.
Открыть страницу → кликнуть в текст → править. Числа в больших цифрах
(97, 4…) тоже просто текст — счётчик анимируется сам, если в абзаце
чистое число и есть класс `sr-counter`.

**Новая секция**: в редакторе «+» → Паттерны → **Remarka** → выбрать секцию.
Доступны: Hero (главная и внутренняя), Striscia di fiducia, Tre numeri,
Servizi, Caso studio, Come lavoriamo, Garanzie (тёмная), Prezzi,
Strumenti, FAQ, Contatti, CTA scura.

**Дизайн блока**: выделить блок → в правой панели «Стили» →
выбрать: Sezione Remarka / Sezione bianca / Sezione scura / Hero con griglia /
Card Remarka / Card su carta / Eyebrow (mono) / WhatsApp (для кнопок).
Цвета и шрифты — только из палитры темы (она уже открыта в панели).

**Barra dei cento** (полоса 0–100): это HTML-блок внутри паттернов.
Чтобы поменять значение, выделить HTML-блок и поправить два места:
`data-sr-target="96%"` (ширина заливки) и текст числа рядом.

**FAQ**: блоки «Details» — вопрос в первой строке, ответ внутри.
Дублировать блок → переписать. Работают без JavaScript.

**Формы**: в паттерне Contatti стоит блок «Шорткод» — вставить туда шорткод
из плагина форм (рекомендуется Fluent Forms; подойдёт и Contact Form 7).

## Анимации

- Собственные: класс `sr-reveal` (появление снизу) или `sr-cascade`
  (детям — каскад с шагом 80 мс) на любом блоке через
  «Дополнительно → CSS-классы».
- Из Prespa: `p-animation-zoom-in`, `p-animation-text-moveUp`,
  `p-animation-down-up`, `p-animation-move-sideways` — движок родительской
  темы добавит `.animated` при прокрутке (в нашем JS есть страховка).
- `prefers-reduced-motion` отключает всё: контент всегда видим.

## Что дальше (см. docs/piano-sviluppo-wordpress.md)

- Собрать страницы из паттернов на стейджинге.
- Заменить вымышленные данные (номера WhatsApp, P.IVA, кейсы) на реальные.
- Загрузить woff2-шрифты, скриншоты кейсов (WebP).
- Кэш-плагин, замер PageSpeed, доводка до 90+.
