<?php
/**
 * Title: Pagina — Strumento: Analisi SEO on-page
 * Slug: remarka-studio/ru-strumento-analisi-seo
 * Categories: remarka-pagine
 * Description: Strumento gratuito Analisi SEO on-page: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Бесплатный инструмент /03</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">SEO-анализ страницы: что видит Google на вашем сайте<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Заголовок, структура содержания и недостающие данные на странице, которая важнее всего для вашего бизнеса. SEO-оценка Google и конкретные рекомендации на русском языке. Без регистрации.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="seo" data-sr-locale="ru"
     data-label-suffix=" — SEO страницы"
     data-verdict-good="Отлично: базовые требования SEO страницы соблюдены."
     data-verdict-mid="SEO на среднем уровне: есть конкретные правки."
     data-verdict-poor="SEO страницы слабое: это приоритет для доработки."
     data-audits-empty="Существенных проблем SEO не обнаружено."
     data-err="Не удалось завершить анализ. Попробуйте ещё раз через несколько минут.">
  <form data-sr-tool-form>
    <div class="sr-tool-row"><input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required /><button type="submit" class="wp-block-button__link" style="padding:17px 30px">Проверить SEO</button></div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт анализ Google<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <ul class="sr-tool-audits" data-sr-tool-audits></ul>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Выберите нужную страницу</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Не обязательно главную: ту страницу, которая должна попасть в поиск — услугу, карточку товара, статью.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Google её анализирует</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Используем категорию SEO Lighthouse через API PageSpeed: заголовки, meta description, теги, ссылки и структуру.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Видите, что исправить</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Оценка 0–100 и список элементов страницы, которые стоит доработать, — по приоритету.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Этот анализ выведет сайт в топ?</summary><!-- wp:paragraph -->
<p>Сам по себе — нет: он проверяет технические основы страницы (заголовки, структуру, данные). Позиции в поиске зависят ещё и от содержания и авторитетности сайта, а это требует времени.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Чем это отличается от анализа контента?</summary><!-- wp:paragraph -->
<p>Здесь мы проверяем техническую сторону страницы — то, что читает Google. Качество текстов — отдельная работа, которую мы делаем с партнёрами-копирайтерами.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Анализирует весь сайт?</summary><!-- wp:paragraph -->
<p>Нет: одну страницу за раз — ту, что вы указали. Именно по странице Google оценивает релевантность запросу.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите, чтобы техническим SEO занялись мы<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Полный аудит, структурированные данные и Core Web Vitals в порядке: PageSpeed 90+ гарантирован договором.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/tehnicheskoe-seo/">Смотреть техническое SEO</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/gotovnost-k-ii/">Проверить готовность к ИИ</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/ru/instrumenty/test-skorosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Тест скорости</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/ru/instrumenty/proverka-dostupnosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка доступности</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/ru/instrumenty/uglerodnyj-sled/" style="color:var(--sr-inchiostro);font-size:15.5px">Углеродный след</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
