<?php
/**
 * Title: Pagina — Strumento: Test velocità
 * Slug: remarka-studio/ru-strumento-test-velocita
 * Categories: remarka-pagine
 * Description: Strumento interattivo con demo di analisi PageSpeed (punteggio, LCP/INP/CLS simulati).
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Бесплатный инструмент /01</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Тест скорости вашего сайта<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Оценка Google PageSpeed и три метрики, из которых она складывается, — объяснённые понятным языком. Без регистрации.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="speed" data-sr-locale="ru"
     data-label-suffix=" — PageSpeed на мобильных"
     data-verdict-good="Отличный результат: сайт соответствует стандартам Google для мобильного опыта."
     data-verdict-mid="Сайт на среднем уровне, но далёк от рекомендуемых Google стандартов. Есть конкретные, измеримые возможности для улучшения."
     data-verdict-poor="Сайт медленный на мобильных: большинство посетителей уходит, не дождавшись полной загрузки. Технический редизайн — приоритет.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Запустить тест</button>
    </div>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт замер Google — мобильная версия, до 30 секунд<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px">
      <div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div>
      <span class="sr-barra__tick" style="left:90%"></span>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:8px;font-family:var(--sr-font-mono);font-size:11px;color:var(--sr-grigio)"><span>0</span><span>50</span><span>90</span><span>100</span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">LCP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-lcp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Время загрузки основного контента. Меньше 2,5 с — хороший показатель.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">INP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-inp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Как быстро сайт реагирует на нажатия. Меньше 200 мс — хороший показатель.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">CLS</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-cls></p><p style="font-size:13.5px;color:var(--sr-grigio)">Визуальная стабильность при загрузке. Меньше 0,1 — хороший показатель.</p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Реальные данные Google PageSpeed Insights API — мобильная стратегия. LCP и CLS — из анализа Lighthouse; INP — из полевых данных Chrome UX, когда они доступны.</p>
  </div>
  </form>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Вставьте адрес</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Укажите URL сайта: главную страницу или внутреннюю, которая приносит больше всего визитов.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Измеряем через Google</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Обращаемся к API PageSpeed Insights в мобильной стратегии — к тем же данным, которые Google использует для ранжирования.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Смотрите, что тормозит сайт</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Оценка 0–100 и три метрики Core Web Vitals, объяснённые понятным языком, без технического жаргона.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Метод</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Что на самом деле измеряет проверка скорости сайта<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">За оценкой стоит один-единственный движок — API Google PageSpeed Insights, тот же, что работает на pagespeed.web.dev. Мы запускаем Lighthouse в мобильной стратегии, потому что именно мобильную версию Google берёт за основу при ранжировании. Число от 0 до 100 рождается в «лаборатории»: эмулируется один и тот же смартфон и одна и та же сеть, поэтому два замера одной страницы можно честно сравнивать между собой. А если у сайта достаточно реального трафика, к лабораторным цифрам добавляются Core Web Vitals, собранные у настоящих пользователей Chrome.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Не менее важно понимать, чего этот тест не делает. Он не оценивает качество текстов, не считает внешние ссылки, не проверяет безопасность сервера и не знает, сколько вы продаёте: он взвешивает только опыт загрузки одной конкретной страницы. Высокий балл — не обещание первой строчки в Google, а здоровый технический фундамент, на котором всё остальное работает лучше. Мы предпочитаем говорить об этом прямо: перед вами точный снимок одного аспекта, а не полный диагноз сайта.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как читать результат</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Как читать оценку скорости загрузки<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Результат читается как светофор. От 90 до 100 — зелёная зона: страница появляется быстро даже в движении, на городском 4G и на краю зоны покрытия. От 50 до 89 — средний уровень для европейского веба, с ощутимым запасом для роста. Ниже 50 — красная зона: заметная часть посетителей со смартфонов уходит, не дождавшись первой строки, а каждый евро, вложенный в рекламу, приносит заметно меньше.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Два ложных повода для паники. Оценка гуляет на несколько баллов от замера к замеру — это нормально: так работают измерительные серверы Google, ваш сайт ни при чём. Важны большие скачки, а не разница в два балла. И не пугайтесь, если десктоп показывает 95, а мобильный — 40: такой разрыв есть почти у всех, но позиции в поиске решает именно мобильная цифра. Смотрите всегда на неё.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Это настоящая оценка Google?</summary><!-- wp:paragraph -->
<p>Да: она приходит из официального API PageSpeed Insights, мобильная стратегия. Это тот же движок, что и на pagespeed.web.dev.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Почему измеряете только мобильную версию?</summary><!-- wp:paragraph -->
<p>Потому что Google индексирует и ранжирует сайт по его мобильной версии. Оценка для десктопа, почти всегда более высокая, мало влияет на позиции.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Низкая оценка вредит продажам?</summary><!-- wp:paragraph -->
<p>Ниже 50 баллов большая часть мобильных посетителей уходит, не дождавшись полной загрузки: рекламные кампании приносят клики, которые не превращаются в заявки.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как улучшить</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Как ускорить сайт: пять шагов, которые работают<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Низкий балл почти всегда объясняется одними и теми же причинами — и первые из них исправляются дешевле всего.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Облегчите изображения</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Переведите фотографии в WebP или AVIF и включите отложенную загрузку: это причина номер один медленных сайтов, и часто одна она сокращает время ожидания вдвое.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Включите кэширование</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Кэш страниц и браузера избавляет сервер от необходимости собирать всё заново при каждом визите: полдня работы — и результат виден в первом же замере.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Проредите CSS и JavaScript</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Вынесите критический CSS в страницу, отложите остальное и уберите сторонние скрипты, которые ничего не делают: меньше кода — быстрее первая отрисовка.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Выберите хостинг по задаче</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Перегруженный виртуальный хостинг тратит секунду ещё до начала загрузки: нормальный сервер с CDN впереди срезает это стартовое ожидание.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Наведите порядок в шрифтах</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ограничьте число гарнитур, предзагрузите основные и включите font-display: swap — текст появится сразу, а не после загрузки всех файлов.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/ru/uslugi/redizajn-i-migracija/">Хотите, чтобы ускорением занялись мы: редизайн и миграция →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/ru/blog/medlennyj-sajt-prichiny/">Разбор по теме: семь причин медленного сайта →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите, чтобы эти проблемы устранили мы<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Бесплатный отчёт с причинами, приоритетами и фиксированной сметой: 90+ гарантированы договором.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Запросить полный анализ</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/tehnicheskoe-seo/">Смотреть техническое SEO</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/ru/instrumenty/polnaya-proverka-sajta/" style="color:var(--sr-inchiostro);font-size:15.5px">Полная проверка сайта</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/ru/instrumenty/proverka-dostupnosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка доступности</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/ru/instrumenty/uglerodnyj-sled/" style="color:var(--sr-inchiostro);font-size:15.5px">Углеродный след</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/ru/instrumenty/signaly-eeat/" style="color:var(--sr-inchiostro);font-size:15.5px">Сигналы E-E-A-T</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
