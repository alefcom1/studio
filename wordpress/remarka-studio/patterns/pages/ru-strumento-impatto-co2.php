<?php
/**
 * Title: Pagina — Strumento: Impatto CO₂
 * Slug: remarka-studio/ru-strumento-impatto-co2
 * Categories: remarka-pagine
 * Description: Strumento gratuito Impatto CO₂: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Бесплатный инструмент /07</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Углеродный след вашего сайта<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Каждый визит на сайт расходует энергию и создаёт CO₂. Измеряем вес вашей страницы и оцениваем выбросы на визит и за год по модели Sustainable Web Design. Лёгкий сайт — это и быстрый сайт.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="co2" data-sr-locale="ru"
     data-co2-average="0.8" data-co2-visits="10000"
     data-label-unit-year="кг CO₂e / год"
     data-verdict-good="Ниже среднего по вебу: лёгкая страница, так держать."
     data-verdict-mid="Близко к среднему по вебу: есть куда облегчить."
     data-verdict-poor="Выше среднего по вебу: страница тяжёлая, стоит оптимизировать."
     data-err="Не удалось измерить вес страницы. Попробуйте ещё раз.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Измерить след</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт измерение<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-grams>0 г</span>
    </div>
    <div class="sr-barra" style="height:10px;margin-top:8px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Вес страницы</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-weight></p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Оценка за год</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-year></p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Модель Sustainable Web Design (co2.js, Apache-2.0). Оценка на визит; год рассчитан на 10 000 визитов/месяц.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Введите адрес</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Страницу для измерения: обычно это главная — самая посещаемая.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Взвешиваем страницу</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Через API PageSpeed измеряем общий объём байтов, которые браузер должен скачать, чтобы показать страницу.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Оценка выбросов</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Применяем модель Sustainable Web Design (co2.js) и получаем граммы CO₂e на визит, сравнение со средним по вебу и оценку за год.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Как вы считаете выбросы?</summary><!-- wp:paragraph -->
<p>По модели Sustainable Web Design от Green Web Foundation (библиотека co2.js, Apache-2.0): от веса страницы к потреблённой энергии и далее к граммам CO₂e. Это оценка со среднемировыми коэффициентами.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Почему лёгкий сайт меньше загрязняет?</summary><!-- wp:paragraph -->
<p>Потому что каждый переданный байт расходует энергию — в дата-центре, в сети, на вашем устройстве. Меньше вес — меньше энергии, меньше выбросов и, как побочный эффект, более быстрый сайт.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Откуда берётся оценка за год?</summary><!-- wp:paragraph -->
<p>Умножаем выбросы на визит на условный трафик в 10 000 визитов в месяц. Если подставить реальный трафик вашего сайта, оценка изменится пропорционально.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите облегчить сайт<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Оптимизированные изображения, чистая техническая база, меньше веса при том же содержании: меньше CO₂ и PageSpeed 90+ по договору.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/redizajn-i-migracija/">Редизайн и миграция</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/test-skorosti/">Измерить скорость</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Другие бесплатные инструменты</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/ru/instrumenty/test-skorosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Тест скорости</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/ru/instrumenty/proverka-dostupnosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка доступности</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
