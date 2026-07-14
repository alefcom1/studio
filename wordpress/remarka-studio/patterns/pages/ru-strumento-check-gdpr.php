<?php
/**
 * Title: Pagina — Strumento: Check GDPR e cookie
 * Slug: remarka-studio/ru-strumento-check-gdpr
 * Categories: remarka-pagine
 * Description: Strumento gratuito Check GDPR e cookie: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Бесплатный инструмент /02</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Ваш сайт соответствует GDPR?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Проверяем баннер cookie, уведомления и трекеры, активные до согласия: четыре проверки, чтобы понять, чего не хватает. Это ориентировочная проверка, а не юридическая консультация.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="gdpr" data-sr-locale="ru"
     data-label-cmp-yes="Баннер cookie найден" data-label-cmp-no="Баннер cookie не найден"
     data-label-policy-yes="Есть ссылка на политику конфиденциальности/cookie" data-label-policy-no="Нет ссылки на политику конфиденциальности/cookie"
     data-label-trackers-clean="В исходном HTML трекеров нет"
     data-label-trackers-flag="Активные трекеры без баннера"
     data-label-trackers-ok="Трекеры есть (с баннером)"
     data-label-external="{n} внешних доменов загружают скрипты"
     data-err="Не удалось прочитать сайт. Попробуйте ещё раз через несколько минут.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.vashsajt.ru" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Проверить сайт</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Идёт чтение сайта<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">Баннер cookie</span><span data-sr-tool-cmp data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Политика</span><span data-sr-tool-policy data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Трекеры</span><span data-sr-tool-trackers data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Внешние скрипты</span><span data-sr-tool-external data-sr-flag></span></li>
    </ul>
    <p class="sr-disclaimer" data-sr-tool-disclaimer>Ориентировочная проверка, а не юридическая консультация. Полный аудит GDPR требует ручной проверки cookie, целей обработки и правовых оснований.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Введите адрес сайта</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Читаем главную страницу с нашего сервера — так, как её увидел бы посетитель при первом заходе.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Четыре автоматические проверки</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ищем баннер cookie (CMP), ссылки на политику конфиденциальности и cookie, трекеры, загруженные до согласия, и внешние домены.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Светофор, а не приговор</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Каждый пункт — зелёный, жёлтый или красный: показываем очевидные проблемы, а не полный юридический аудит.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Метод</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Что именно проверяет наш GDPR-тест<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">В отличие от тестов на движке Google, здесь вашу главную страницу читает наш собственный сервер — ровно так, как её увидел бы посетитель при первом открытии, до единого клика. На полученном HTML выполняются четыре автоматические проверки: есть ли баннер cookie (CMP — Iubenda, Cookiebot, Complianz и подобные), находятся ли ссылки на privacy policy и cookie policy, стартуют ли счётчики и пиксели до согласия и какие внешние домены страница вызывает.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Скажем сразу, потому что это важно: перед вами не юридическое заключение. Это ориентировочная техническая проверка — она ловит очевидные проблемы, за которые европейские регуляторы наказывают чаще всего, но не заменяет консультанта по защите данных. Тест не видит, что происходит после нажатия «Принять», не оценивает ваши журналы согласий и не читает тексты уведомлений построчно. Это хорошая отправная точка, а не сертификат соответствия.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как читать результат</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Как читать светофор соответствия<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Каждый пункт получает свой цвет, и цвет стоит воспринимать буквально. Зелёный — сигнал на месте и в порядке. Жёлтый — что-то есть, но требует ручной проверки: например, политика опубликована, но может оказаться неполной. Красный — не хватает важного элемента или, хуже, трекеры работают без баннера, который должен ими управлять. Общая картина важнее любого отдельного кружка.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Самый частый красный сигнал — «трекеры без баннера»: Google Analytics или пиксель Meta, зашитые прямо в исходный HTML и срабатывающие до согласия пользователя. Именно за это надзорные органы ЕС штрафуют решительнее всего — а для компании, выходящей на европейский рынок, такой штраф особенно обиден. Жёлтый же обычно не беда: чаще всего достаточно дополнить или обновить уже существующее уведомление.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Три частых вопроса</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Это юридическое заключение?</summary><!-- wp:paragraph -->
<p>Нет, и это важно уточнить: это ориентировочная автоматическая проверка, а не юридическая консультация. Она показывает очевидные технические проблемы; полное соответствие должен оценивать консультант по защите данных.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Что значит «трекеры без баннера»?</summary><!-- wp:paragraph -->
<p>Это означает, что в исходном HTML страницы уже есть инструменты слежения (Google Analytics, Meta Pixel и подобные), активные до того, как пользователь дал согласие. Это самый частый красный флаг на сайтах в ЕС.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Почему регуляторы так строги к cookie?</summary><!-- wp:paragraph -->
<p>Потому что согласие должно быть свободным, информированным и подтверждаемым: отказаться должно быть так же просто, как согласиться, а ни один рекламный трекер не может запускаться до того, как пользователь скажет «да».</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Как улучшить</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Как привести cookie и согласия в порядок<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Практическое соответствие складывается из нескольких правил — но соблюдать нужно каждое из них.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Поставьте CMP, которая реально блокирует</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Серьёзный баннер не просто появляется на экране: он не даёт трекерам стартовать, пока пользователь не согласился. В этом разница между «выглядеть по правилам» и «работать по правилам».</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Сделайте отказ таким же простым, как согласие</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Кнопка «Отклонить» должна весить столько же, сколько «Принять», и стоять на том же экране: без cookie wall и без квеста ради права сказать «нет».</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Опубликуйте полные уведомления</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Понятные и актуальные privacy policy и cookie policy, которые легко найти: что вы собираете, зачем и с кем этим делитесь.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Сделайте согласие доказуемым</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Храните запись о каждом согласии — когда и на что оно дано, — чтобы предъявить её по запросу: «да» должно быть свободным, осознанным и отслеживаемым.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Запускайте трекеры после «да»</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Аналитика, пиксели и тепловые карты включаются только после принятия, по условию: до согласия страница обязана оставаться чистой.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/ru/uslugi/korporativnye-sajty/">Мы включаем это в каждый корпоративный сайт →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/ru/blog/cookie-banner-trebovanija-2026/">Разбор по теме: требования к cookie-баннеру в 2026 году →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Хотите привести сайт в соответствие<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Баннер, уведомления и согласия по всем правилам — включены в каждый корпоративный сайт, который мы сдаём.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/korporativnye-sajty/">Смотреть корпоративные сайты</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Запросить анализ</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/ru/instrumenty/test-skorosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Тест скорости</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/ru/instrumenty/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">SEO-анализ страницы</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/ru/instrumenty/roi-lokalizacii/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI локализации</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/ru/instrumenty/proverka-dostupnosti/" style="color:var(--sr-inchiostro);font-size:15.5px">Проверка доступности</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/ru/instrumenty/gotovnost-k-ii/" style="color:var(--sr-inchiostro);font-size:15.5px">Готовность к ИИ</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/ru/instrumenty/uglerodnyj-sled/" style="color:var(--sr-inchiostro);font-size:15.5px">Углеродный след</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
