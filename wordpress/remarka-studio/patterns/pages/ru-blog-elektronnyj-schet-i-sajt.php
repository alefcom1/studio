<?php
/**
 * Title: Pagina — RU Articolo: Электронный счёт (fattura elettronica) и сайт: что учесть
 * Slug: remarka-studio/ru-blog-elektronnyj-schet-i-sajt
 * Categories: remarka-pagine
 * Description: Articolo blog RU: электронный счёт в Италии и сайт — что такое SdI, кому fattura elettronica обязательна, какие данные передаёт чекаут
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">26 ИЮЛ 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Электронный счёт (fattura elettronica) и сайт: что учесть</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch12-fattura-cover.svg" alt="Электронный счёт в Италии и сайт: система SdI, формат XML и данные из чекаута" loading="lazy" width="1200" height="630" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Продать товар на сайте — это половина дела; вторую половину в Италии определяет счёт. Здесь давно действует электронный счёт — fattura elettronica: документ формируется не как обычный PDF, а как файл строгого формата, который проходит через государственную систему обмена. Для бизнеса это значит, что сайт или магазин должны не просто «принять оплату», а собрать правильные данные покупателя, чтобы счёт вообще можно было выставить. Электронный счёт в Италии касается почти каждого, кто здесь продаёт, и лучше понимать его логику до запуска сайта, а не после первой сделки. Сразу оговоримся: это обзор, а не бухгалтерская консультация — конкретику всегда сверяйте со своим commercialista.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Что такое электронный счёт и система SdI<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Электронный счёт — это не «PDF по почте», а структурированный файл в формате XML, оформленный по правилам налоговой (Agenzia delle Entrate). Такой файл нельзя просто отправить контрагенту напрямую: он проходит через государственную систему обмена — Sistema di Interscambio, сокращённо SdI. По сути SdI работает как почтовое отделение для счетов: получает ваш файл, проверяет его на корректность, доставляет получателю и одновременно передаёт данные налоговой. Если в счёте ошибка формата или не хватает обязательного поля, система его отклоняет — и счёт считается невыставленным. Поэтому «выставить fattura elettronica» технически означает сформировать корректный XML и провести его через SdI, а не приложить картинку к письму.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Кому это обязательно? В общем случае электронный счёт в Италии распространяется очень широко — на большинство продавцов, работающих в стране, с отдельными нюансами по режимам и категориям. Именно из-за этих нюансов мы не беремся утверждать, что «обязательно всем без исключения»: ваш конкретный случай — например, особый налоговый режим или продажи за рубеж — определяет commercialista. Здесь важно понять принцип: если вы продаёте в Италии, с большой вероятностью счёт придётся выставлять электронно, и сайт должен быть к этому готов.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/batch12-fattura-flusso.svg" alt="Путь электронного счёта: заказ на сайте, данные покупателя, XML, система SdI и получатель" loading="lazy" width="1200" height="600" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Путь счёта: сайт собирает данные покупателя → формируется XML → SdI проверяет и доставляет → копия уходит в налоговую. Сбой на первом шаге ломает всю цепочку.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Какие данные должен передавать чекаут для счёта<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Вот где электронный счёт напрямую встречается с сайтом. Чтобы счёт сформировался, в момент оформления заказа нужно собрать данные, которых обычному магазину часто не хватает. Для покупателя-компании (B2B) это, как правило, налоговый номер (partita IVA), а также идентификаторы для доставки счёта через SdI — так называемый codice destinatario или сертифицированный адрес PEC. Для частного лица (B2C) обычно нужен codice fiscale. То есть чекаут должен уметь спрашивать «вы компания или частное лицо?» и в зависимости от ответа показывать правильные поля — и проверять их формат, чтобы система потом не отклонила счёт. Без этой развилки бизнес-покупатель либо не сможет купить, либо получит счёт, который не пройдёт через SdI.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Отдельная развилка — продажи за рубеж. Для клиентов из других стран ЕС и из-за пределов Союза правила по НДС и оформлению документов отличаются, и часть операций отражается иначе. Технически это значит, что магазин должен различать страну и статус покупателя ещё на чекауте — и передавать это в систему выставления счетов. Мы намеренно не приводим конкретные ставки, пороги и коды: они меняются и зависят от вашей ситуации, а выдумывать цифры в такой теме недопустимо. Правильный порядок — сначала обсудить схему продаж с commercialista, а потом закладывать её в логику сайта.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Важно не путать два разных вопроса: как принять деньги и как выставить счёт. Подробно о способах оплаты, комиссиях и обязательной аутентификации SCA мы разбирали в <a href="/ru/blog/kak-prinyat-oplatu-na-sajte/">соседней статье про приём оплаты на сайте</a> — эта же статья про сам счёт, который идёт после оплаты. Оплата и счёт связаны, но это разные слои, и в хорошем магазине оба продуманы заранее.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Как это встроить в сайт или магазин<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">На практике сайт редко сам генерирует XML и общается с SdI — обычно это делает бухгалтерский сервис или специальный провайдер, а магазин передаёт им нужные данные заказа. Задача сайта — правильно их собрать и корректно отдать: развилка B2B/B2C, проверка формата налоговых полей, аккуратная передача в систему выставления счетов через интеграцию. Для <a href="/ru/uslugi/internet-magaziny/">интернет-магазина</a> это часть архитектуры чекаута, а для <a href="/ru/uslugi/korporativnye-sajty/">корпоративного сайта</a> с продажами услуг — часть формы заказа и последующего документооборота. Мы закладываем эти поля и интеграции сразу, чтобы после первой же продажи не переделывать чекаут в спешке.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/ru/uslugi/internet-magaziny/">Интернет-магазин с чекаутом под электронный счёт →</a></p>
<!-- /wp:html -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Практический вывод: электронный счёт — не «бухгалтерская мелочь после сайта», а требование, которое влияет на то, как устроен ваш чекаут. Соберите правильные данные, разведите частных лиц и компании, учтите зарубежные продажи и передавайте всё в систему выставления счетов через интеграцию. А конкретную схему по вашему налоговому режиму согласуйте с commercialista — это тот случай, где догадки дороже консультации.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Источники<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Утверждения этой статьи опираются на первоисточники. Откройте и проверьте.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://www.agenziaentrate.gov.it/" target="_blank" rel="noopener">Agenzia delle Entrate — налоговая служба Италии</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Официальные правила электронного счёта: формат, обязанности, кого касается.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.fatturapa.gov.it/" target="_blank" rel="noopener">FatturaPA — официальный портал электронного счёта</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Государственный портал о формате XML и системе обмена SdI: спецификации и документация.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://europa.eu/youreurope/business/" target="_blank" rel="noopener">Your Europe — Business (Еврокомиссия)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">НДС и выставление счетов при продажах в другие страны ЕС и за пределы Союза.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://eur-lex.europa.eu/" target="_blank" rel="noopener">EUR-Lex — законодательство ЕС по НДС</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Первоисточник директив ЕС по НДС, на которых строятся национальные правила счетов.</span></li></ul>
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
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/ru/uslugi/internet-magaziny/">Интернет-магазины</a></div>
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
