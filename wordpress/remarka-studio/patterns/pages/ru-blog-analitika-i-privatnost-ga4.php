<?php
/**
 * Title: Pagina — RU Articolo: Аналитика и приватность: GA4 и закон ЕС о данных
 * Slug: remarka-studio/ru-blog-analitika-i-privatnost-ga4
 * Categories: remarka-pagine
 * Description: Articolo blog RU: Google Analytics и закон ЕС — как считать статистику сайта в GA4, не нарушая GDPR, что такое согласие и Consent Mode
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">26 ИЮЛ 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Аналитика и приватность: GA4 и закон ЕС о данных</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch12-ga4-cover.svg" alt="Google Analytics и закон ЕС: как считать статистику сайта в GA4, не нарушая GDPR" loading="lazy" width="1200" height="630" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Почти каждый, кто запускает сайт, хочет знать: сколько людей зашло, откуда они пришли, какие страницы читают. Самый популярный ответ на этот вопрос — Google Analytics, сегодня в версии GA4. Но если ваш бизнес работает в Евросоюзе или вы просто собираете посетителей из ЕС, к статистике добавляется второй вопрос — закон о данных. Google Analytics и закон ЕС уживаются, но не по умолчанию: чтобы считать аудиторию честно, нужно настроить согласие, минимизацию данных и прозрачность. Эта статья — для тех, кто открывает бизнес или сайт в Европе и хочет понимать, что здесь можно, а что нет, без юридических выдумок.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Почему Google Analytics и закон ЕС пересекаются<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Любая веб-аналитика следит за поведением людей: какие страницы открывают, сколько времени проводят, с какого устройства заходят. С точки зрения европейского права это обработка персональных данных, а значит, действует Общий регламент по защите данных — GDPR (Регламент ЕС 2016/679). Он работает не по тому, где зарегистрирована ваша компания, а по тому, где находятся ваши посетители: собираете аудиторию из ЕС — правила ваши. Отдельная история — cookie и аналогичные технологии, которые аналитика ставит в браузер: их использование в Европе требует согласия пользователя, полученного заранее, до того как трекинг начался. Именно поэтому нельзя просто «вставить счётчик и забыть»: это ровно тот случай, где статистика встречается с законом.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Важная оговорка: тема аналитики и трансграничной передачи данных в ЕС несколько лет была предметом споров и решений национальных регуляторов, включая итальянский Garante. Правила и практики менялись и продолжают уточняться, поэтому это обзор, а не юридическая консультация: по конкретной настройке под ваш бизнес лучше свериться с юристом по защите данных. Наша цель — чтобы вы понимали логику и не наступали на очевидные грабли.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch12-ga4-privacy.svg" alt="GA4 и GDPR: согласие до трекинга, минимизация данных, прозрачность и Consent Mode" loading="lazy" width="1200" height="600" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Четыре опоры честной аналитики в ЕС: согласие до трекинга, меньше лишних данных, ясная политика и корректная реакция на выбор пользователя.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Как считать статистику в GA4, не нарушая GDPR<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">GA4 задуман с оглядкой на приватность и даёт настройки, которые помогают соблюдать закон, — но включить их нужно осознанно. Практический минимум выглядит так. <strong>Согласие до трекинга.</strong> Баннер cookie должен давать реальный выбор — «Принять» и «Отклонить» на равных, — и аналитика запускается только после согласия. <strong>Consent Mode.</strong> Механизм Google, который подстраивает поведение тегов под выбор пользователя: отказался — данные не собираются или собираются в обезличенном виде. <strong>Минимизация.</strong> Не тащите в аналитику лишнее: никаких имён, почт и телефонов в параметрах, разумные сроки хранения. <strong>Прозрачность.</strong> В политике конфиденциальности честно напишите, что используете Google Analytics, зачем и как отказаться.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Проверить, как ваш сайт обходится с cookie и согласием, можно быстро — нашим <a href="/ru/instrumenty/proverka-gdpr/">бесплатным инструментом проверки GDPR и cookie</a>. Он показывает, что ставится в браузер и запрашивается ли согласие как положено. А базовые шаги по данным для бизнеса в ЕС, без паники и штата юристов, мы разобрали в <a href="/ru/blog/gdpr-dlya-russkoyazychnogo-biznesa-v-es/">статье про GDPR для русскоязычного бизнеса</a>.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/ru/instrumenty/proverka-gdpr/">Проверка GDPR и cookie: что ставит ваш сайт в браузер →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Есть ли альтернативы и что учесть в сайте заранее<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">GA4 — не единственный вариант. Есть аналитические сервисы, устроенные более «приватно»: они не используют cookie для идентификации, не собирают персональные данные и в некоторых случаях позволяют работать без баннера согласия. У них меньше возможностей, чем у Google, но для многих сайтов их достаточно, а хлопот с правом меньше. Какой инструмент выбрать — вопрос ваших задач, но и он, и GA4 одинаково требуют, чтобы техническая база сайта была в порядке: корректно подключённые теги, управление согласием, чистая загрузка скриптов. Это уже территория <a href="/ru/uslugi/tehnicheskoe-seo/">технического SEO</a> — там же, где живут скорость и разметка, от которых зависит и видимость, и аккуратность сбора данных.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Практический вывод: аналитика в ЕС — это не «ставить или не ставить», а «ставить правильно». Спрашивайте согласие до трекинга, включайте Consent Mode, не собирайте лишнего, честно пишите об этом в политике — и по спорным моментам сверяйтесь с юристом. Тогда вы будете знать свою аудиторию и спать спокойно.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Источники<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Утверждения этой статьи опираются на первоисточники. Откройте и проверьте.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://eur-lex.europa.eu/eli/reg/2016/679/oj" target="_blank" rel="noopener">EUR-Lex — Регламент ЕС 2016/679 (GDPR)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Первоисточник закона о защите данных: когда действует, что считается персональными данными, что такое согласие.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://support.google.com/analytics/" target="_blank" rel="noopener">Google Analytics — официальная справка</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Настройки GA4, Consent Mode, сроки хранения и минимизация данных.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.garanteprivacy.it/" target="_blank" rel="noopener">Garante per la protezione dei dati personali</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Итальянский регулятор по защите данных: разъяснения и решения по аналитике и cookie.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://edpb.europa.eu/" target="_blank" rel="noopener">Европейский совет по защите данных (EDPB)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Общие рекомендации регуляторов ЕС по согласию, cookie и передаче данных.</span></li></ul>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Поговорим о вашем сайте<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Бесплатный анализ текущего сайта и фиксированная смета в течение 24 часов после звонка.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/ru/#contatti">Смета за 24 часа</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/proverka-gdpr/">Проверить GDPR — бесплатно</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% бесплатно</strong><span>Никаких обязательств</span></div><div class="sr-cta-band__trust-item"><strong>Ответ за 24 часа</strong><span>Подробная смета</span></div><div class="sr-cta-band__trust-item"><strong>Данные под защитой</strong><span>Полная конфиденциальность</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:buttons {"style":{"spacing":{"blockGap":"14px"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/blog/">← Все статьи</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
