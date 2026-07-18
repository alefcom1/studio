<?php
/**
 * Title: Страница — Инструмент: Полная проверка сайта
 * Slug: remarka-studio/ru-strumento-check-up-completo
 * Categories: remarka-pagine
 * Description: Бесплатный инструмент «Полная проверка сайта»: интерактивный виджет, как это работает, вопросы, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Полная проверка · бесплатно</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Полная проверка вашего сайта<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Семь бесплатных инструментов в одном анализе. Вставьте адрес — меньше чем за минуту вы увидите оценку здоровья от 0 до 100, семь светофоров за ней и три самые срочные задачи. Скорость, SEO, доступность и технические стандарты измеряет Google PageSpeed Insights; приватность и готовность к ИИ проверяем мы. Полный отчёт, страница за страницей, пришлём в PDF.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card sr-checkup" data-sr-tool="checkup" data-sr-locale="ru"
     data-word-0="Отлично" data-word-1="Хорошо" data-word-2="Внимание" data-word-3="Критично"
     data-composite-0="Отличное здоровье сайта" data-composite-1="Хорошее здоровье сайта"
     data-composite-2="Сайт требует доработки" data-composite-3="Сайт в зоне риска"
     data-label-suffix="— мобильный анализ"
     data-calc-note="Рассчитано на {n} измерениях из 7."
     data-na-text="Не удалось измерить этот показатель: сайт отказал в автоматическом чтении, либо сервис Google был перегружен."
     data-err="Не удалось завершить проверку. Попробуйте ещё раз через несколько минут."
     data-ai-suffix=" / 4 сигналов"
     data-more-label="Подробный тест →">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Проверить сайт — бесплатно</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт анализ по семи направлениям — это может занять до 30 секунд<span class="sr-blink">…</span></p>

  <div class="sr-tool-result" data-sr-tool-result hidden>

    <div class="sr-checkup-incomplete" data-sr-checkup-incomplete hidden>
      <h3 class="wp-block-heading">Проверка не завершена</h3>
      <p>Попробуйте через несколько минут: часть измерений не ответила (сервис Google мог быть перегружен, либо сайт отказал в чтении).</p>
      <button type="button" class="wp-block-button__link" data-sr-checkup-retry>Повторить</button>
    </div>

    <div data-sr-checkup-composite>
      <p class="sr-eyebrow">Здоровье сайта</p>
      <div class="sr-checkup-composite">
        <div class="sr-gauge" data-sr-gauge>
          <div class="sr-gauge__num"><span class="sr-gauge__num-value" data-sr-gauge-num>0</span><span class="sr-gauge__num-suffix">/100</span></div>
        </div>
        <div>
          <p class="sr-mono sr-checkup-url" data-sr-checkup-url></p>
          <h2 class="wp-block-heading sr-checkup-label" data-sr-checkup-label></h2>
          <p class="sr-checkup-method-note">Взвешенное среднее 7 измерений. Скорость, SEO, доступность и стандарты — из Google PageSpeed; приватность, ИИ и CO₂ — проверки Студии Ремарка.</p>
          <p class="sr-mono sr-checkup-calc" data-sr-checkup-calc></p>
        </div>
      </div>
    </div>

    <div style="margin-top:32px">
      <p class="sr-eyebrow">Семь измерений</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">Семь светофоров, одна оценка</h2>
      <div class="sr-dim-grid" style="margin-top:24px"><div class="sr-card sr-dim-card" data-sr-dim="perf" data-verdict-0="Сайт быстрый на мобильном: соответствует стандартам Google." data-verdict-1="Скорость хорошая; на части страниц есть измеримый запас." data-verdict-2="В среднем по вебу, но далеко от рекомендуемых стандартов." data-verdict-3="Сайт медленный на мобильном: большинство уходит до загрузки.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Скорость</p><span class="sr-dim-card__weight">Вес 25</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="seo" data-verdict-0="Технические основы страницы в порядке: ничто не мешает индексации." data-verdict-1="Структура крепкая; несколько правок, чтобы завершить основы." data-verdict-2="Часть элементов страницы отсутствует или дублируется." data-verdict-3="Что-то мешает индексации: исправить в первую очередь.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">SEO</p><span class="sr-dim-card__weight">Вес 20</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="a11y" data-verdict-0="Барьеров мало или нет: сайт пригоден по WCAG 2.1 AA." data-verdict-1="Хороший уровень; остались мелкие барьеры." data-verdict-2="Найдено несколько барьеров: контраст, подписи, навигация." data-verdict-3="Серьёзные барьеры: сайтом трудно пользоваться многим (требование EAA).">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Доступность</p><span class="sr-dim-card__weight">Вес 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">WCAG 2.1 / EAA</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="gdpr" data-verdict-0="Баннер, политики и трекеры в начальном HTML в порядке." data-verdict-1="Механизм есть; пару пунктов стоит проверить вручную." data-verdict-2="Не хватает элементов или трекеры управляются плохо." data-verdict-3="Трекеры работают без баннера или нет политик: реальный юридический риск.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Приватность и cookie</p><span class="sr-dim-card__weight">Вес 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Ориентировочная проверка · не юридическая</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="bp" data-verdict-0="Технически чисто: HTTPS, консоль без ошибок, актуальные библиотеки." data-verdict-1="Хороший уровень; несколько предупреждений закрыть." data-verdict-2="Несколько технических предупреждений: безопасность, ошибки консоли, картинки." data-verdict-3="Много технических проблем, ослабляющих надёжность и безопасность.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Технические стандарты</p><span class="sr-dim-card__weight">Вес 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
</div><div class="sr-card sr-dim-card" data-sr-dim="ai" data-verdict-0="4 сигнала из 4: сайт читаем и цитируем ИИ-моделями." data-verdict-1="3 сигнала из 4: до полной готовности немного." data-verdict-2="2 сигнала из 4: доработать структурированные данные или sitemap." data-verdict-3="0–1 сигнал: ИИ-моделям трудно читать и цитировать сайт.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Готовность к ИИ</p><span class="sr-dim-card__weight">Вес 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span><span class="sr-dim-card__extra" data-sr-dim-extra></span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">4 технических сигнала</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="co2" data-verdict-0="Лёгкая страница: выбросы ниже среднего по вебу." data-verdict-1="Около среднего; есть запас, чтобы облегчить." data-verdict-2="Выше среднего: страница тяжёлая при загрузке." data-verdict-3="Заметно выше среднего: тяжёлая страница, цена для экологии и скорости.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Углеродный след</p><span class="sr-dim-card__weight">Вес 5</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Модель SWD</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Подробный тест →</a></p>
</div></div>
    </div>

    <div data-sr-checkup-priorities-wrap style="margin-top:32px">
      <p class="sr-eyebrow">Приоритеты</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">3 задачи, которые весят больше всего</h2>
      <p style="margin:8px 0 20px;color:var(--sr-grigio);font-size:15.5px">По степени влияния на оценку: сколько вы выиграете, решив их.</p>
      <div class="sr-priorities" data-sr-checkup-priorities></div>
    </div>

    <div data-sr-checkup-form-wrap style="margin-top:32px">
      <div class="sr-card sr-checkup-lead">
        <p class="sr-eyebrow">Полный отчёт</p>
        <h2 class="wp-block-heading" style="font-size:clamp(22px,2.6vw,28px)">Полный отчёт в PDF</h2>
        <p style="margin-top:10px;color:var(--sr-grigio);font-size:15.5px;line-height:1.6">Пришлём анализ целиком: по странице на каждое из семи измерений, все найденные проблемы и рекомендации по степени влияния.</p>
        <ul class="sr-tool-audits" style="margin-top:18px">
          <li>Оценка здоровья с семью светофорами</li>
          <li>Страница на каждое измерение: балл, что нашли, что делать</li>
          <li>Три приоритетные задачи с мерами</li>
          <li>«Что сделали бы мы» и реквизиты Студии Ремарка</li>
        </ul>
        <form data-sr-checkup-report-form style="margin-top:24px">
          <p class="sr-hp-field" aria-hidden="true"><label>Сайт<input type="text" name="sr_checkup_hp" tabindex="-1" autocomplete="off"></label></p>
          <div class="sr-tool-row">
            <input type="email" placeholder="imya@vashakompaniya.ru" class="sr-text-input" required />
            <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Прислать отчёт в PDF</button>
          </div>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent required /><span>Я прочитал <a href="/ru/privacy/">политику конфиденциальности</a> и согласен на отправку отчёта и на обратную связь.</span></label>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent-monthly /><span>Присылайте мне ежемесячный мониторинг Core Web Vitals этого сайта.</span></label>
          <p class="sr-mono" data-sr-checkup-success hidden style="margin-top:16px;color:var(--sr-verde)">Готово. Отчёт уже в пути к вашей почте: если не придёт за пару минут, проверьте спам или напишите нам.</p>
          <p class="sr-form-error" data-sr-checkup-error hidden>Не удалось отправить отчёт. Попробуйте ещё раз или напишите нам — пришлём вручную.</p>
        </form>
        <p class="sr-mono" style="margin-top:20px;font-size:11px;color:var(--sr-grigio);opacity:.85">Без спама. Адрес используем только для отправки отчёта и, при необходимости, обратной связи. Студия Ремарка, ИНН 231149349191.</p>
      </div>
    </div>

  </div>
</div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как это работает</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Три шага, без регистрации<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Вставьте адрес</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Главная или страница, которая приносит больше всего визитов. Без регистрации и без платёжных данных.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Анализируем по семи направлениям</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Один запрос к API Google PageSpeed (скорость, SEO, доступность, стандарты) плюс наши проверки приватности и готовности к ИИ: сайт мы читаем со своего сервера, как его увидел бы посетитель.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Читаете оценку и приоритеты</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Здоровье 0–100, семь светофоров по-русски и три задачи, которые весят больше всего. Полный отчёт придёт в PDF.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Метод</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Что на самом деле измеряет полная проверка<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">За оценкой нет чёрного ящика. Четыре из семи измерений — скорость, SEO, доступность и технические стандарты — приходят из API Google PageSpeed Insights, того же, что стоит за pagespeed.web.dev: мы опрашиваем Lighthouse в мобильной стратегии, потому что именно эту версию сайта Google использует для ранжирования. Остальные три считаем мы: приватность читаем из HTML страницы (баннер, политики, трекеры до согласия), готовность к ИИ — по четырём техническим сигналам (llms.txt, доступ краулеров, структурированные данные, sitemap), а углеродный след — по реальному весу страницы, по модели Sustainable Web Design.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Каждое измерение входит в оценку со своим весом: скорость весит больше всего (25 из 100), CO₂ — меньше всего (5). Стоит знать и то, чего проверка не делает: это не юридическое заключение по GDPR — это ориентировочная проверка по четырём сигналам — и она не обещает позиций в Google. Это точный технический снимок сайта, а не обещание продаж.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как читать результат</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Как читать оценку состояния сайта<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Оценка здоровья — это взвешенное среднее семи светофоров, а не отметка «на глаз». Читается как светофор: от 90 и выше — зелёная зона (отлично), 75–89 — хорошо, 50–74 — есть реальный запас, ниже 50 — критично и становится приоритетом. У каждого измерения один и тот же цветовой код, поэтому сразу видно, где сайт крепок, а где теряет баллы.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Два неверных прочтения. Высокая оценка не значит «первые в Google»: она значит, что технический фундамент здоров. А если измерение показывает «Н/Д», это не поломка вашего сайта: иногда Google перегружен, иногда сайт отказывает в автоматическом чтении. В этом случае мы считаем здоровье по удавшимся измерениям и честно об этом сообщаем.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Оценка — настоящая от Google?</summary><!-- wp:paragraph -->
<p>Для скорости, SEO, доступности и стандартов — да: она из официального API PageSpeed Insights, мобильная стратегия. Приватность, готовность к ИИ и CO₂ — наши проверки, метод описан в каждом разделе.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Проверка GDPR заменяет консультанта по приватности?</summary><!-- wp:paragraph -->
<p>Нет. Это ориентировочная техническая проверка по четырём сигналам: она ловит очевидные проблемы — нет баннера, трекеры до согласия, — но это не юридическое заключение и не замена консультанту.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Что в PDF-отчёте, чего нет на экране?</summary><!-- wp:paragraph -->
<p>На экране — оценка, семь светофоров и три приоритета. В PDF — по странице на каждое из семи измерений со всеми найденными проблемами, рекомендации по степени влияния и раздел «что сделали бы мы» с нашими реквизитами.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите, чтобы приоритеты закрыли мы<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">От оценки — к смете: разберём отчёт вместе и дадим план работ по фиксированной цене, со скоростью PageSpeed 90+ по договору.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Бесплатная консультация</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/">Все инструменты</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% бесплатно</strong><span>Никаких обязательств</span></div><div class="sr-cta-band__trust-item"><strong>Ответ за 24 часа</strong><span>Подробная смета</span></div><div class="sr-cta-band__trust-item"><strong>Данные под защитой</strong><span>Полная конфиденциальность</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Другие бесплатные инструменты</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/ru/instrumenty/test-skorosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Тест скорости</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/ru/instrumenty/proverka-dostupnosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка доступности</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/ru/instrumenty/uglerodnyj-sled/" style="color:var(--sr-inchiostro);font-size:15.5px">Углеродный след</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/ru/instrumenty/signaly-eeat/" style="color:var(--sr-inchiostro);font-size:15.5px">Сигналы E-E-A-T</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
