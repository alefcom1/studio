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

<div class="sr-tool-widget sr-card">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
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
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите, чтобы эти проблемы устранили мы<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Бесплатный отчёт с причинами, приоритетами и фиксированной сметой: 90+ гарантированы договором.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Запросить полный анализ</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
