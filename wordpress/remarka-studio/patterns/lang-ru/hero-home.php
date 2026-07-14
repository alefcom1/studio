<?php
/**
 * Title: Первый экран — главная с виджетом скорости
 * Slug: remarka-studio/ru-hero-home
 * Categories: remarka
 * Description: Главный первый экран: заголовок, подзаголовок, две CTA-кнопки и карточка с анимированным баллом PageSpeed.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group sr-section sr-hero"><!-- wp:html -->
<div class="sr-watermark" aria-hidden="true"><svg width="620" height="620" viewBox="0 0 32 32"><g stroke="#2440C8" stroke-width="2.6" fill="none"><path d="M16 2.5v27"></path><path d="M27.69 9.25 4.31 22.75"></path><path d="M4.31 9.25 27.69 22.75"></path></g></svg></div>
<!-- /wp:html -->

<!-- wp:columns {"verticalAlignment":"center","className":"sr-cascade","style":{"spacing":{"blockGap":{"left":"56px"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center sr-cascade"><!-- wp:column {"verticalAlignment":"center","width":"55%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:55%"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Студия веб-разработки</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Быстрые сайты, которые продают<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium","textColor":"grigio"} -->
<p class="has-grigio-color has-text-color has-medium-font-size">Проектируем прогрессивные сайты для итальянского малого и среднего бизнеса: PageSpeed 90+ с гарантией в договоре, сдача в фиксированную дату, фиксированная цена.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"36px"}}}} -->
<div class="wp-block-buttons" style="margin-top:36px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/test-skorosti/">Проверить ваш сайт — бесплатно</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="#contatti">Смета за 24 часа</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"45%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:45%"><!-- wp:group {"className":"sr-card","layout":{"type":"constrained"}} -->
<div class="wp-block-group sr-card"><!-- wp:paragraph {"className":"sr-eyebrow sr-no-margin"} -->
<p class="sr-eyebrow sr-no-margin">Google PageSpeed — мобильная версия</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"sr-score-line"} -->
<p class="sr-score-line"><span class="sr-score-num sr-counter">97</span><span class="sr-score-of">/ 100</span></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="sr-barra" data-sr-target="97%" data-sr-delay="400" role="img" aria-label="Балл 97 из 100" style="margin-top:18px"><div class="sr-barra__fill"></div><span class="sr-barra__tick" style="left:90%"></span></div>
<div class="sr-score-scale" aria-hidden="true"><span>0</span><span>50</span><span>100</span></div>
<!-- /wp:html -->

<!-- wp:paragraph {"fontSize":"small","textColor":"grigio"} -->
<p class="has-grigio-color has-text-color has-small-font-size">Средний балл сайтов, которые мы сдаём. Гарантирован договором.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<form data-sr-hero-form style="margin-top:24px;border-top:1px solid var(--sr-bordo);padding-top:24px">
  <label for="hero-url" class="sr-eyebrow" style="display:block;margin-bottom:10px">А сколько набирает ваш сайт?</label>
  <div class="sr-tool-row">
    <input id="hero-url" type="text" placeholder="www.tuosito.it" class="sr-text-input" />
    <button type="submit" class="wp-block-button__link" style="padding:13px 22px;font-size:15px;border:1px solid var(--sr-oltremare)">Проверить</button>
  </div>
  <p class="sr-tool-pending sr-mono" data-sr-hero-pending hidden>Идёт проверка Google — до 30 секунд<span class="sr-blink">…</span></p>
  <div data-sr-hero-result hidden style="margin-top:18px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px">
      <span data-sr-hero-url style="font-size:14px;color:var(--sr-grigio);overflow:hidden;text-overflow:ellipsis;white-space:nowrap"></span>
      <span data-sr-hero-score class="sr-mono" style="font-size:28px;color:var(--sr-inchiostro)"></span>
    </div>
    <div class="sr-barra sr-barra--h8" style="margin-top:8px">
      <div class="sr-barra__fill sr-barra__fill--muted" data-sr-hero-fill style="width:0%"></div>
    </div>
    <p style="margin:12px 0 0;font-size:14px;line-height:1.5;color:var(--sr-grigio)">Запас для роста: с прогрессивным сайтом мы гарантируем <span class="sr-mono" style="color:var(--sr-verde)">90+</span> по договору.</p>
  </div>
</form>
<!-- /wp:html --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
