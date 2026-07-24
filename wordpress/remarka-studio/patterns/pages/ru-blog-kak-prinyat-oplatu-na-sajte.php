<?php
/**
 * Title: Pagina — RU Articolo: Как принять оплату на сайте в Италии и ЕС: способы и нюансы
 * Slug: remarka-studio/ru-blog-kak-prinyat-oplatu-na-sajte
 * Categories: remarka-pagine
 * Description: Articolo blog RU: приём оплаты на сайте в Италии и ЕС — способы, комиссии, правила SCA и электронный счёт. Практический разбор без юридических выдумок.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">25 ИЮЛ 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Как принять оплату на сайте в Италии и ЕС: способы и нюансы</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch11-oplata-cover.svg" alt="Приём оплаты на сайте в Италии и ЕС: способы, комиссии и правила SCA" loading="lazy" width="1200" height="630" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Клиент дошёл до конца, выбрал товар, готов заплатить — и тут упирается в неудобную оплату: карту не принимают, привычной кнопки нет, платёж срывается на непонятном шаге. Это самая обидная потеря, потому что человек уже решил купить. Приём оплаты на сайте в Италии и ЕС кажется технической мелочью, но на нём спотыкаются даже хорошие магазины: где-то не учли обязательное подтверждение платежа, где-то забыли про комиссию, где-то запутались со счётом. Разберём по-человечески: какие способы бывают, сколько они стоят и какие правила придётся соблюдать. Сразу оговорка: это обзор, а не юридическая или налоговая консультация — тонкости всегда сверяйте со своим бухгалтером.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Способы приёма оплаты на сайте: что выбрать<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch11-oplata-sposoby.svg" alt="Способы приёма оплаты на сайте: карты, PayPal, Apple и Google Pay, банковский перевод, SCA и электронный счёт" loading="lazy" width="1200" height="600" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Шесть узлов, которые важно учесть заранее: способы оплаты, комиссии, обязательное подтверждение SCA и правильный счёт.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Банковские карты — база: Visa и Mastercard принимают через платёжный сервис (например, известные международные провайдеры), который берёт процент с каждой транзакции. PayPal привычен и повышает доверие, особенно у осторожных покупателей, но комиссия обычно выше. Apple Pay и Google Pay ускоряют оплату до одного касания — на телефоне это заметно снижает число брошенных корзин. Банковский перевод (в Италии — bonifico, в ЕС — SEPA) почти без комиссии и хорош для крупных сумм или B2B, но медленнее и требует ручной сверки. Практический принцип: не пытайтесь подключить всё сразу. Дайте два-три способа, которыми реально пользуются ваши клиенты, — лишние варианты только загромождают кассу.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Правило, которое нельзя игнорировать: SCA<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">В Европе действует директива PSD2, и вместе с ней — требование строгой аутентификации клиента (Strong Customer Authentication, SCA). На практике это тот самый шаг, когда при оплате картой банк просит подтвердить платёж — через приложение, код или отпечаток. Для большинства онлайн-платежей картой в ЕС это обязательно; есть отдельные исключения для некоторых операций, но их определяет банк и платёжная система, а не вы. Что это значит для сайта: ваш платёжный модуль должен корректно поддерживать это подтверждение, иначе часть платежей будет срываться. Хорошая новость — современные платёжные провайдеры делают SCA из коробки; важно лишь не использовать устаревшую интеграцию, которая её ломает.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Ещё до оплаты человек должен вам доверять настолько, чтобы ввести данные карты. Здесь снова работают базовые вещи: скорость, понятная касса, отсутствие лишних полей. Если платежей меньше, чем визитов с товаром в корзине, причина часто не в оплате как таковой, а в утечках по дороге — мы разбирали их в <a href="/ru/blog/pochemu-sajt-ne-prinosit-zayavok/">статье о семи тихих утечках</a>.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Счёт и налоги: где легко ошибиться<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Здесь начинается зона, где выдумывать нельзя, а нужно свериться с бухгалтером. В Италии действует электронный счёт (fatturazione elettronica) через государственную систему SdI — это обязательный порядок выставления счетов для сторон, зарегистрированных в стране. Но не переносите это правило автоматически на всех: продажа частному клиенту из другой страны ЕС подчиняется своим правилам, и порядок счёта и НДС там иной. То же с налогом: трансграничные продажи потребителям в ЕС имеют собственный режим учёта НДС, и его лучше настроить с бухгалтером до запуска, а не после. Технически сайт должен уметь сформировать корректный документ и передать нужные данные, но какой именно документ и с какой ставкой — это вопрос вашего налогового статуса, а не движка магазина. Поэтому мы всегда советуем: сначала консультация с commercialista, потом настройка.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">С технической стороны приём оплаты — это часть <a href="/ru/uslugi/internet-magaziny/">интернет-магазина</a>: подключение провайдера, поддержка SCA, корректная касса и передача данных для счёта. Если же вы продаёте услуги, а не товары, полноценный магазин может быть избыточен — иногда достаточно кнопки оплаты на <a href="/ru/uslugi/korporativnye-sajty/">корпоративном сайте</a>. А с чего вообще начинать продвижение готового магазина — с рекламы или SEO — мы разобрали в <a href="/ru/blog/reklama-ili-seo-s-chego-nachat/">соседней статье</a>.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/ru/uslugi/internet-magaziny/">Интернет-магазин: оплата, SCA и счёт — настроено правильно →</a></p>
<!-- /wp:html -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Практический вывод: выберите два-три способа оплаты под своих клиентов, убедитесь, что модуль поддерживает SCA, и заранее согласуйте со своим бухгалтером порядок счёта и НДС — особенно для продаж за пределы Италии. Тогда оплата перестанет быть местом, где теряются уже готовые купить люди.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Источники<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Утверждения этой статьи опираются на первоисточники. Откройте и проверьте.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://eur-lex.europa.eu/eli/dir/2015/2366/oj" target="_blank" rel="noopener">EUR-Lex — Директива (ЕС) 2015/2366 (PSD2)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Правовая база платёжных услуг в ЕС, включая строгую аутентификацию клиента (SCA).</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://finance.ec.europa.eu/" target="_blank" rel="noopener">Еврокомиссия — платёжные услуги</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Официальные материалы ЕС о правилах онлайн-платежей и защите потребителей.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.agenziaentrate.gov.it/" target="_blank" rel="noopener">Agenzia delle Entrate — электронный счёт</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Итальянская налоговая: порядок электронного счёта (fatturazione elettronica) через систему SdI.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://ec.europa.eu/eurostat" target="_blank" rel="noopener">Eurostat — электронная торговля в ЕС</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Официальная статистика ЕС о том, как и чем платят покупатели в интернете.</span></li></ul>
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
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/instrumenty/polnaya-proverka-sajta/">Проверить сайт — бесплатно</a></div>
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
