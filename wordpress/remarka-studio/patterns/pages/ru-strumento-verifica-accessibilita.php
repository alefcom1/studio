<?php
/**
 * Title: Pagina — Strumento: Verifica accessibilità
 * Slug: remarka-studio/ru-strumento-verifica-accessibilita
 * Categories: remarka-pagine
 * Description: Strumento gratuito Verifica accessibilità: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Бесплатный инструмент /05</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Проверка доступности: сайтом могут пользоваться все?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Проверяем через Google самые частые барьеры доступности — контраст, подписи, структуру. С 28 июня 2025 года European Accessibility Act делает доступность обязательной для многих сайтов в ЕС. Без регистрации.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="a11y" data-sr-locale="ru"
     data-label-suffix=" — доступность"
     data-verdict-good="Отлично: основные барьеры уже устранены."
     data-verdict-mid="Доступность на среднем уровне: часть барьеров ещё осталась."
     data-verdict-poor="Доступность слабая: есть серьёзные барьеры для пользователей."
     data-audits-empty="Существенных барьеров не обнаружено."
     data-err="Не удалось завершить анализ. Попробуйте ещё раз через несколько минут.">
  <form data-sr-tool-form>
    <div class="sr-tool-row"><input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required /><button type="submit" class="wp-block-button__link" style="padding:17px 30px">Проверить доступность</button></div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт анализ<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <ul class="sr-tool-audits" data-sr-tool-audits></ul>
      <p class="sr-disclaimer">Автоматическая проверка (Lighthouse) покрывает часть критериев WCAG 2.1 AA. Полное соответствие EAA требует и ручной проверки.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Введите адрес</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Страницу для проверки: главную или страницу услуги, куда приходит больше всего посетителей.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Анализ Lighthouse</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Используем категорию Accessibility Lighthouse через API PageSpeed: контраст, альтернативный текст, подписи полей, структуру заголовков.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Видите, что нужно устранить</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Оценка 0–100 и список найденных проблем на русском языке. Автоматическая проверка покрывает часть критериев WCAG, не все.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Что такое European Accessibility Act?</summary><!-- wp:paragraph -->
<p>Европейская директива (EAA), действующая в странах ЕС с 28 июня 2025 года: многие сайты компаний, продающих потребителям, должны быть доступны по стандарту WCAG 2.1 уровня AA. Это обязательное требование с отдельными исключениями для микропредприятий.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Этого теста достаточно для соответствия?</summary><!-- wp:paragraph -->
<p>Нет: автоматическая проверка улавливает лишь часть критериев WCAG. Полное соответствие требует и ручной проверки — навигации с клавиатуры, скринридеров, содержания. Это отличная отправная точка, но не сертификат.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Касается ли это моей компании?</summary><!-- wp:paragraph -->
<p>Если вы продаёте товары или услуги потребителям онлайн (интернет-магазин, банк, транспорт, услуги) в ЕС — почти наверняка да. У микропредприятий, оказывающих услуги, есть исключения: лучше проверить свой случай отдельно.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите сделать сайт доступным<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Проверяем барьеры один за другим — автоматически и вручную — и устраняем их по стандарту WCAG 2.1 AA.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Запросить проверку доступности</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/korporativnye-sajty/">Смотреть корпоративные сайты</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/ru/instrumenty/test-skorosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Тест скорости</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/ru/instrumenty/proverka-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка GDPR и cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/ru/instrumenty/uglerodnyj-sled/" style="color:var(--sr-inchiostro);font-size:15.5px">Углеродный след</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
