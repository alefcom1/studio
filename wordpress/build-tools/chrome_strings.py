"""Шаблонная микро-копия генератора (eyebrow/кнопки/заголовки секций),
не входящая в корпус data.py. Переведена редактором (носитель EN/RU),
терминология согласована с corpus_en/corpus_ru: preventivo chiuso →
EN "fixed quote" / RU «фиксированная смета»; цены в EN — американский
формат (€2,500), в RU — итальянский локальный (€ 2.500) сохраняется.
Формат: {it_string: {'en': ..., 'ru': ...}}"""

CHROME = {
    '100% DEI PREVENTIVI 2025 CHIUSI AL PREZZO FIRMATO': {
        'en': '100% OF 2025 QUOTES CLOSED AT THE SIGNED PRICE',
        'ru': '100% СМЕТ 2025 ГОДА ЗАКРЫТЫ ПО ПОДПИСАННОЙ ЦЕНЕ',
    },
    '12 mesi': {'en': '12 months', 'ru': '12 месяцев'},
    'Analisi gratuita del sito attuale e del mercato target. Preventivo chiuso entro 24 ore.': {
        'en': 'Free analysis of your current website and target market. A fixed quote within 24 hours.',
        'ru': 'Бесплатный анализ текущего сайта и целевого рынка. Фиксированная смета в течение 24 часов.',
    },
    'Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.': {
        'en': 'Free analysis of your current website; a fixed quote within 24 hours of the call.',
        'ru': 'Бесплатный анализ текущего сайта и фиксированная смета в течение 24 часов после звонка.',
    },
    'Analisi gratuita e un preventivo chiuso: perimetro, prezzo e data, tutti e tre nel contratto.': {
        'en': 'A free analysis and a fixed quote: scope, price and date — all three in the contract.',
        'ru': 'Бесплатный анализ и фиксированная смета: объём, цена и срок — все три пункта в договоре.',
    },
    'Analizza il tuo sito — gratis': {'en': 'Test your website — free', 'ru': 'Проверить сайт — бесплатно'},
    'Aree clienti, configuratori, portali B2B e integrazioni: quando un sito non basta.': {
        'en': 'Client areas, product configurators, B2B portals and integrations: for when a website isn’t enough.',
        'ru': 'Личные кабинеты, конфигураторы, B2B-порталы и интеграции: когда сайта уже недостаточно.',
    },
    'Avvia il test': {'en': 'Run the test', 'ru': 'Запустить тест'},
    'CMS per aggiornarlo da soli': {'en': 'CMS to update it yourself', 'ru': 'CMS для самостоятельных правок'},
    'Calcola il ROI della localizzazione': {'en': 'Calculate your localization ROI', 'ru': 'Рассчитать ROI локализации'},
    'Come lavoriamo': {'en': 'How we work', 'ru': 'Как мы работаем'},
    'Confronta tutte le tariffe →': {'en': 'Compare all plans →', 'ru': 'Сравнить все тарифы →'},
    'Consegna': {'en': 'Delivery', 'ru': 'Срок сдачи'},
    'Contenuto legale da redigere con un consulente privacy prima del lancio. I dati raccolti tramite il modulo contatti restano nell’Unione Europea, come indicato nel sito, e non vengono ceduti a terzi per finalità di profilazione.': {
        'en': 'Legal copy to be drafted with a privacy consultant before launch. Data collected through the contact form stays within the European Union, as stated on the website, and is never shared with third parties for profiling.',
        'ru': 'Юридический текст будет подготовлен с консультантом по приватности до запуска. Данные из формы обратной связи хранятся в Европейском союзе, как указано на сайте, и не передаются третьим лицам для профилирования.',
    },
    'Cosa fa variare il prezzo': {'en': 'What changes the price', 'ru': 'Из чего складывается цена'},
    'Descriveteci il progetto: ricevete prezzo e data di consegna, entrambi vincolanti.': {
        'en': 'Describe your project: you get a price and a delivery date, both binding.',
        'ru': 'Опишите проект — вы получите цену и срок сдачи, и оба пункта будут обязательными.',
    },
    'Design su misura, senza template': {'en': 'Custom design, no templates', 'ru': 'Дизайн с нуля, без шаблонов'},
    'Dopo': {'en': 'After', 'ru': 'После'},
    'Gli altri strumenti gratuiti': {'en': 'The other free tools', 'ru': 'Другие бесплатные инструменты'},
    'Il problema': {'en': 'The problem', 'ru': 'Проблема'},
    'Il prossimo caso può essere il vostro': {'en': 'The next case study could be yours', 'ru': 'Следующим кейсом может стать ваш'},
    'Il sito e la sua versione estera sotto un unico contratto: localizzazione da madrelingua, SEO internazionale, KPI per mercato.': {
        'en': 'Your website and its foreign version under one contract: native-speaker localization, international SEO, per-market KPIs.',
        'ru': 'Сайт и его зарубежная версия по одному договору: локализация носителями, международное SEO, KPI по каждому рынку.',
    },
    'Il sito usa solo cookie tecnici necessari: non esistono al momento preferenze facoltative da gestire. Questa pagina sarà ampliata se in futuro verranno introdotti cookie di terze parti.': {
        'en': 'This website only uses strictly necessary technical cookies: there are currently no optional preferences to manage. This page will be expanded if third-party cookies are ever introduced.',
        'ru': 'Сайт использует только технически необходимые cookie: настраиваемых параметров сейчас нет. Эта страница будет дополнена, если появятся cookie третьих сторон.',
    },
    'Il vostro prossimo mercato parla un’altra lingua': {
        'en': 'Your next market speaks another language',
        'ru': 'Ваш следующий рынок говорит на другом языке',
    },
    'Impianti idraulici · Bergamo · Sito aziendale IT/DE': {
        'en': 'Plumbing systems · Bergamo · Business website IT/DE',
        'ru': 'Сантехнические системы · Бергамо · Корпоративный сайт IT/DE',
    },
    'Quanto costa un sito web? La tabella qui sotto è pubblica; il preventivo che firmate è un prezzo chiuso. Se in corso d’opera serve altro, si concorda prima, per iscritto.': {
        'en': 'How much does a website cost? The table below is public; the quote you sign is a fixed price. If anything extra comes up mid-project, it’s agreed first — in writing.',
        'ru': 'Сколько стоит сайт? Таблица ниже открыта для всех; смета, которую вы подписываете, — это фиксированная цена. Если по ходу проекта нужно что-то ещё, это согласуется заранее и письменно.',
    },
    'Leggi il caso completo →': {'en': 'Read the full case study →', 'ru': 'Читать кейс целиком →'},
    'Leggi il caso →': {'en': 'Read the case study →', 'ru': 'Читать кейс →'},
    'Leggi un caso completo →': {'en': 'Read a full case study →', 'ru': 'Читать полный кейс →'},
    'L’analisi del sito attuale è gratuita e vi arriva come report scritto, con le priorità.': {
        'en': 'The analysis of your current website is free and arrives as a written report, priorities included.',
        'ru': 'Анализ текущего сайта бесплатен — вы получаете письменный отчёт с приоритетами.',
    },
    'Misura il tuo sito adesso — test gratuito →': {
        'en': 'Measure your website now — free test →',
        'ru': 'Измерьте свой сайт сейчас — бесплатный тест →',
    },
    'Niente marketing travestito da articolo: solo quello che impariamo consegnando siti veloci.': {
        'en': 'No marketing dressed up as articles: only what we learn shipping fast websites.',
        'ru': 'Никакого маркетинга под видом статей: только то, чему мы учимся, сдавая быстрые сайты.',
    },
    'Numeri simili per il vostro settore': {
        'en': 'Similar numbers for your industry',
        'ru': 'Похожие цифры для вашей отрасли',
    },
    'Ogni servizio nasce con lo stesso obiettivo: PageSpeed 90+ da contratto, prezzo chiuso, data fissa.': {
        'en': 'Every service is built around the same promise: PageSpeed 90+ by contract, fixed price, fixed date.',
        'ru': 'Каждая услуга строится вокруг одного обещания: PageSpeed 90+ по договору, фиксированная цена, фиксированный срок.',
    },
    'Oltre il sito': {'en': 'Beyond the website', 'ru': 'Больше, чем сайт'},
    'Pagine incluse': {'en': 'Pages included', 'ru': 'Страниц включено'},
    'Parliamo del vostro progetto': {'en': 'Let’s talk about your project', 'ru': 'Поговорим о вашем проекте'},
    'Parliamo del vostro sito': {'en': 'Let’s talk about your website', 'ru': 'Поговорим о вашем сайте'},
    'Per chi è': {'en': 'Who it’s for', 'ru': 'Для кого это'},
    'Per confronto: le agenzie italiane chiedono in media € 2.500–8.000 per un sito aziendale e € 5.000–20.000 per un e-commerce (listini pubblici 2026). Siamo nella stessa fascia — con tre garanzie scritte nel contratto che altrove non trovate.': {
        'en': 'For comparison: Italian agencies charge on average €2,500–8,000 for a business website and €5,000–20,000 for an e-commerce store (public 2026 price lists). We sit in the same range — with three written contract guarantees you won’t find elsewhere.',
        'ru': 'Для сравнения: итальянские агентства просят в среднем € 2.500–8.000 за корпоративный сайт и € 5.000–20.000 за интернет-магазин (открытые прайсы 2026 года). Мы в той же вилке — но с тремя письменными гарантиями в договоре, которых больше нигде нет.',
    },
    'Perimetro chiuso o crescita per iterazioni': {
        'en': 'Fixed scope, or growth by iterations',
        'ru': 'Закрытый объём или рост итерациями',
    },
    'Preventivo chiuso in 24 ore': {'en': 'A fixed quote in 24 hours', 'ru': 'Фиксированная смета за 24 часа'},
    'Prezzi chiari, anche qui': {'en': 'Clear prices, here too', 'ru': 'Прозрачные цены — и здесь тоже'},
    'Prezzo': {'en': 'Price', 'ru': 'Цена'},
    'Prezzo chiuso nel preventivo, PageSpeed 90+ e data di consegna scritti nel contratto. Gli stessi prezzi pubblici, ovunque siate.': {
        'en': 'A fixed price in the quote, PageSpeed 90+ and the delivery date written into the contract. The same public prices, wherever you are.',
        'ru': 'Фиксированная цена в смете, PageSpeed 90+ и срок сдачи прописаны в договоре. Одни и те же открытые цены, где бы вы ни находились.',
    },
    'Prezzo chiuso nel preventivo, come per tutti i nostri servizi. Fattura elettronica, pagamento in tre tranche.': {
        'en': 'A fixed price in the quote, as with all our services. E-invoicing, payment in three installments.',
        'ru': 'Фиксированная цена в смете, как и во всех наших услугах. Электронный счёт-фактура, оплата тремя траншами.',
    },
    'Prima': {'en': 'Before', 'ru': 'До'},
    'Prima misurate, poi decidete': {'en': 'Measure first, then decide', 'ru': 'Сначала измерьте, потом решайте'},
    'Prima misuriamo il sito attuale, poi vi diciamo — con numeri — cosa possiamo garantire.': {
        'en': 'First we measure your current website; then we tell you — in numbers — what we can guarantee.',
        'ru': 'Сначала мы измеряем текущий сайт, потом говорим — в цифрах — что можем гарантировать.',
    },
    'Primo incontro gratuito, da voi in azienda. Preventivo chiuso entro 24 ore.': {
        'en': 'The first meeting is free, at your company. A fixed quote within 24 hours.',
        'ru': 'Первая встреча бесплатна, у вас в компании. Фиксированная смета в течение 24 часов.',
    },
    'Quando serve di più': {'en': 'When you need more', 'ru': 'Когда нужно больше'},
    'Quanto costa un sito web a Milano': {
        'en': 'How much does a website cost in Milan',
        'ru': 'Сколько стоит сайт в Милане',
    },
    'Quattro passaggi, un contratto': {'en': 'Four steps, one contract', 'ru': 'Четыре шага, один договор'},
    'Questo strumento è in fase di sviluppo. Nel frattempo richiedete un’analisi gratuita: vi rispondiamo entro un giorno lavorativo.': {
        'en': 'This tool is under development. In the meantime, request a free analysis: we reply within one business day.',
        'ru': 'Этот инструмент в разработке. А пока запросите бесплатный анализ: ответим в течение одного рабочего дня.',
    },
    'Raccontateci il processo da automatizzare': {
        'en': 'Tell us about the process you want to automate',
        'ru': 'Расскажите, какой процесс нужно автоматизировать',
    },
    'Realizzazione siti web a Milano': {'en': 'Website development in Milan', 'ru': 'Создание сайтов в Милане'},
    'Reattività del sito al tocco. Sotto i 200 ms è considerato buono.': {
        'en': 'How quickly the site reacts to taps. Under 200 ms is considered good.',
        'ru': 'Как быстро сайт реагирует на нажатия. Меньше 200 мс — хороший показатель.',
    },
    'Report gratuito con le cause, le priorità e un preventivo chiuso: 90+ garantito da contratto.': {
        'en': 'A free report with the causes, the priorities and a fixed quote: 90+ guaranteed by contract.',
        'ru': 'Бесплатный отчёт с причинами, приоритетами и фиксированной сметой: 90+ гарантированы договором.',
    },
    'Richiedi preventivo dettagliato': {'en': 'Request a detailed quote', 'ru': 'Запросить подробную смету'},
    'Richiedi preventivo in 24 ore': {'en': 'Get a quote in 24 hours', 'ru': 'Смета за 24 часа'},
    'Risultati misurati, non promessi': {'en': 'Results measured, not promised', 'ru': 'Результаты измеренные, а не обещанные'},
    'SETTORE IMPIANTI IDRAULICI · SEDE BERGAMO · INTERVENTO SITO AZIENDALE IT/DE · ANNO 2025': {
        'en': 'INDUSTRY: PLUMBING SYSTEMS · LOCATION: BERGAMO · PROJECT: BUSINESS WEBSITE IT/DE · YEAR 2025',
        'ru': 'ОТРАСЛЬ: САНТЕХНИЧЕСКИЕ СИСТЕМЫ · ГОРОД: БЕРГАМО · ПРОЕКТ: КОРПОРАТИВНЫЙ САЙТ IT/DE · ГОД 2025',
    },
    'SETTORE STUDIO LEGALE · SEDE MILANO · INTERVENTO SITO VETRINA + BLOG · ANNO 2025': {
        'en': 'INDUSTRY: LAW FIRM · LOCATION: MILAN · PROJECT: BROCHURE SITE + BLOG · YEAR 2025',
        'ru': 'ОТРАСЛЬ: ЮРИДИЧЕСКАЯ ФИРМА · ГОРОД: МИЛАН · ПРОЕКТ: САЙТ-ВИЗИТКА + БЛОГ · ГОД 2025',
    },
    'Sei cose che sappiamo fare bene': {'en': 'Six things we do well', 'ru': 'Шесть вещей, которые мы умеем делать хорошо'},
    'Sei servizi, un’unica garanzia': {'en': 'Six services, one guarantee', 'ru': 'Шесть услуг, одна гарантия'},
    'Sito aziendale': {'en': 'Business website', 'ru': 'Корпоративный сайт'},
    'Sito vetrina': {'en': 'Brochure site', 'ru': 'Сайт-визитка'},
    'Stabilità visiva durante il caricamento. Sotto 0,1 è considerato buono.': {
        'en': 'Visual stability while loading. Under 0.1 is considered good.',
        'ru': 'Визуальная стабильность при загрузке. Меньше 0,1 — хороший показатель.',
    },
    'Strumenti professionali, gratuiti, senza registrazione.': {
        'en': 'Professional tools, free, no sign-up.',
        'ru': 'Профессиональные инструменты — бесплатно и без регистрации.',
    },
    'Studio Remarka nasce all’interno del gruppo Remarka, agenzia di traduzioni attiva dal 2001. Applichiamo la stessa precisione contrattuale alla velocità dei siti che progettiamo: numeri misurati, non promesse commerciali.': {
        'en': 'Studio Remarka was born inside the Remarka group, a translation company in business since 2001. We apply the same contractual precision to the speed of the websites we build: measured numbers, not sales promises.',
        'ru': 'Studio Remarka выросла внутри группы Remarka — переводческой компании, работающей с 2001 года. К скорости сайтов мы применяем ту же договорную точность: измеренные цифры вместо рекламных обещаний.',
    },
    'Studio legale · Milano · Sito vetrina + blog': {
        'en': 'Law firm · Milan · Brochure site + blog',
        'ru': 'Юридическая фирма · Милан · Сайт-визитка + блог',
    },
    'Tempo di caricamento del contenuto principale. Sotto i 2,5 s è considerato buono.': {
        'en': 'How long the main content takes to load. Under 2.5 s is considered good.',
        'ru': 'Время загрузки основного контента. Меньше 2,5 с — хороший показатель.',
    },
    'Tre voci, sempre le stesse. Le trovate esplicitate riga per riga nel preventivo.': {
        'en': 'Three items, always the same. You’ll find them itemized line by line in the quote.',
        'ru': 'Три статьи расходов, всегда одни и те же. В смете они расписаны строка за строкой.',
    },
    'Un gruppo che lavora con le lingue e il web dal 2001': {
        'en': 'A group working with languages and the web since 2001',
        'ru': 'Группа, которая работает с языками и вебом с 2001 года',
    },
    'Un mercato o una strategia': {'en': 'One market, or a strategy', 'ru': 'Один рынок или стратегия'},
    'Usiamo solo cookie tecnici necessari al funzionamento del sito. Nessun cookie di profilazione o tracciamento pubblicitario è attivo senza consenso esplicito. Contenuto legale completo da redigere con un consulente privacy prima del lancio.': {
        'en': 'We only use technical cookies required for the website to work. No profiling or ad-tracking cookies are active without explicit consent. Full legal copy to be drafted with a privacy consultant before launch.',
        'ru': 'Мы используем только технические cookie, необходимые для работы сайта. Cookie профилирования и рекламного трекинга не включаются без явного согласия. Полный юридический текст будет подготовлен с консультантом до запуска.',
    },
    'Vedi il nostro listino e-commerce, prezzi chiusi →': {
        'en': 'See our e-commerce price list, fixed prices →',
        'ru': 'Смотрите наш прайс на интернет-магазины, цены фиксированные →',
    },
    'Vuoi che sistemiamo noi questi problemi': {
        'en': 'Want us to fix these problems for you',
        'ru': 'Хотите, чтобы эти проблемы устранили мы',
    },
    'ogni lingua oltre quelle comprese, tradotta da madrelingua del gruppo Remarka.': {
        'en': 'each language beyond those included, translated by Remarka group native speakers.',
        'ru': 'каждый язык сверх включённых, в переводе носителей группы Remarka.',
    },
    'pagine e schede oltre quelle incluse, servizi fotografici, testi da scrivere ex novo.': {
        'en': 'pages and product sheets beyond those included, photo shoots, copy written from scratch.',
        'ru': 'страницы и карточки сверх включённых, фотосъёмка, тексты, которые нужно писать с нуля.',
    },
    '← Tutti gli articoli': {'en': '← All articles', 'ru': '← Все статьи'},
}

# Второй проход: пропуски, найденные аудитом неизменённых узлов.
CHROME_EXTRA = {
    '01 — Problema': {'en': '01 — The problem', 'ru': '01 — Проблема'},
    '02 — Soluzione': {'en': '02 — The solution', 'ru': '02 — Решение'},
    '03 — Risultati': {'en': '03 — The results', 'ru': '03 — Результаты'},
    '3 sett.': {'en': '3 wks', 'ru': '3 нед.'},
    '5–7 sett.': {'en': '5–7 wks', 'ru': '5–7 нед.'},
    '8–10 sett.': {'en': '8–10 wks', 'ru': '8–10 нед.'},
    # --- Fase A: prezzi (compare-table delivery + market-table). EN only (RU → fase B). ---
    '2 sett.': {'en': '2 wks'},
    '6 sett.': {'en': '6 wks'},
    'PageSpeed 90+ da contratto': {'en': 'PageSpeed 90+ by contract'},
    'Prezzi e tempi, accanto a quelli di mercato': {'en': 'Prices and timelines, next to the market’s'},
    'Le forbici di mercato vengono dai listini pubblici delle web agency italiane (2026). Le nostre cifre sono quelle del contratto.': {
        'en': 'The market ranges come from the public price lists of Italian web agencies (2026). Our figures are the ones in the contract.'},
    'Prodotto': {'en': 'Product'},
    'Prezzo di mercato': {'en': 'Market price'},
    'Prezzo Remarka': {'en': 'Remarka price'},
    'Tempi di mercato': {'en': 'Market timeline'},
    'Tempi Remarka': {'en': 'Remarka timeline'},
    '2–4 settimane': {'en': '2–4 weeks'},
    '6–10 settimane': {'en': '6–10 weeks'},
    '8–14 settimane': {'en': '8–14 weeks'},
    '2 settimane': {'en': '2 weeks'},
    '3 settimane': {'en': '3 weeks'},
    '6 settimane': {'en': '6 weeks'},
    'Forbici di mercato dai listini pubblici delle web agency italiane, 2026. Analisi completa con le fonti nel nostro blog:': {
        'en': 'Market ranges from the public price lists of Italian web agencies, 2026. Full breakdown with sources on our blog:'},
    '«Quanto costa un sito aziendale in Italia»': {'en': '“How much a business website costs in Italy”'},
    'Prezzo chiuso nel preventivo, consegna in 3 settimane. Fattura elettronica, pagamento in tre tranche.': {
        'en': 'Fixed price locked in the quote, delivery in 3 weeks. E-invoicing, payment in three installments.'},
    'Prezzo chiuso nel preventivo, consegna in 6 settimane. Fattura elettronica, pagamento in tre tranche.': {
        'en': 'Fixed price locked in the quote, delivery in 6 weeks. E-invoicing, payment in three installments.'},
    # --- Fase A: tightened delivery timelines (PWA, restyling, technical SEO,
    #     multilingual, web app). EN only (RU → fase B). ---
    'Prezzo chiuso nel preventivo, consegna in 4 settimane. Fattura elettronica, pagamento in tre tranche.': {
        'en': 'Fixed price locked in the quote, delivery in 4 weeks. E-invoicing, payment in three installments.'},
    'In media 3 settimane, con un ambiente di prova visibile fin dalla prima settimana.': {
        'en': 'On average 3 weeks, with a staging environment you can see from the first week.'},
    'Perimetro chiuso, prezzo chiuso, data fissa: la prima versione funzionante del prodotto in 6–8 settimane, pronta per utenti reali.': {
        'en': 'Fixed scope, fixed price, fixed date: the first working version of your product in 6–8 weeks, ready for real users.'},
    # --- Fase A: residui italiani pre-esistenti in chi-siamo (report translate_pages en);
    #     valori identici alla versione EN già committata per evitare regressioni. EN only. ---
    'La nostra sede, in centro a Milano': {'en': 'Our office, in central Milan'},
    'La sede di Studio Remarka in centro a Milano': {'en': "Studio Remarka's office in central Milan"},
    'Lo spazio di lavoro dello studio': {'en': 'The studio workspace'},
    'Ingresso dello studio, civico 12': {'en': 'Studio entrance, number 12'},
    'Altri casi studio →': {'en': 'More case studies →', 'ru': 'Другие кейсы →'},
    'Appunti tecnici, in italiano': {'en': 'Technical notes, in plain language', 'ru': 'Технические заметки, понятным языком'},
    'Arredo su misura · Lissone (MB) · Restyling + PWA + SEO': {
        'en': 'Custom furniture · Lissone (MB) · Rebuild + PWA + SEO',
        'ru': 'Мебель на заказ · Лиссоне (MB) · Редизайн + PWA + SEO'},
    'Assistenza inclusa': {'en': 'Support included', 'ru': 'Поддержка включена'},
    'Casi studio': {'en': 'Case studies', 'ru': 'Кейсы'},
    'Casi studio / Arredamenti Colombo': {'en': 'Case studies / Arredamenti Colombo', 'ru': 'Кейсы / Arredamenti Colombo'},
    'Casi studio / Cantina Serralta': {'en': 'Case studies / Cantina Serralta', 'ru': 'Кейсы / Cantina Serralta'},
    'Casi studio / Studio Legale Fontana': {'en': 'Case studies / Studio Legale Fontana', 'ru': 'Кейсы / Studio Legale Fontana'},
    'Casi studio / TecnoIdraulica': {'en': 'Case studies / TecnoIdraulica', 'ru': 'Кейсы / TecnoIdraulica'},
    'Catalogo': {'en': 'Catalog', 'ru': 'Каталог'},
    'Catalogo, carrello e pagamenti': {'en': 'Catalog, cart and payments', 'ru': 'Каталог, корзина и оплата'},
    'Chi siamo': {'en': 'About us', 'ru': 'О студии'},
    'Contenuti:': {'en': 'Content:', 'ru': 'Контент:'},
    'Cookie policy': {'ru': 'Политика cookie'},
    'Cosa facciamo': {'en': 'What we do', 'ru': 'Что мы делаем'},
    'Cosa include': {'en': 'What’s included', 'ru': 'Что входит'},
    'Dal registro consegne': {'en': 'From the delivery log', 'ru': 'Из журнала сдачи проектов'},
    'Dati reali da Google PageSpeed Insights API — strategia mobile. LCP e CLS da analisi Lighthouse; INP da dati di campo Chrome UX quando disponibili.': {
        'en': 'Real data from the Google PageSpeed Insights API — mobile strategy. LCP and CLS from Lighthouse analysis; INP from Chrome UX field data when available.',
        'ru': 'Реальные данные Google PageSpeed Insights API — мобильная стратегия. LCP и CLS — из анализа Lighthouse; INP — из полевых данных Chrome UX, когда они доступны.'},
    'Dicono di noi, da Milano e dintorni': {'en': 'What clients say, from Milan and around', 'ru': 'Что о нас говорят — Милан и окрестности'},
    'Domande da Milano': {'en': 'Questions from Milan', 'ru': 'Вопросы из Милана'},
    'Dove siamo': {'en': 'Where we are', 'ru': 'Где мы находимся'},
    'Due formati': {'en': 'Two formats', 'ru': 'Два формата'},
    'Fattura elettronica via SDI. Pagamento in tre tranche: 40 / 40 / 20.': {
        'en': 'E-invoicing via SDI (the Italian exchange system). Payment in three installments: 40 / 40 / 20.',
        'ru': 'Электронный счёт-фактура через SDI. Оплата тремя траншами: 40 / 40 / 20.'},
    'Flagship': {'ru': 'Флагман'},
    'Garanzie': {'en': 'Guarantees', 'ru': 'Гарантии'},
    'In arrivo': {'en': 'Coming soon', 'ru': 'Скоро'},
    'Integrazioni:': {'en': 'Integrations:', 'ru': 'Интеграции:'},
    'Lingue tradotte da madrelingua': {'en': 'Languages translated by native speakers', 'ru': 'Языки в переводе носителей'},
    'Lingue:': {'en': 'Languages:', 'ru': 'Языки:'},
    'PWA: offline e installabile': {'en': 'PWA: offline and installable', 'ru': 'PWA: офлайн и установка на телефон'},
    'Preferenze cookie': {'en': 'Cookie preferences', 'ru': 'Настройки cookie'},
    'Prezzi': {'en': 'Pricing', 'ru': 'Цены'},
    'Prezzi trasparenti. Nessuna sorpresa in corso d’opera': {
        'en': 'Transparent prices. No surprises mid-project',
        'ru': 'Прозрачные цены. Без сюрпризов по ходу проекта'},
    'Privacy policy': {'ru': 'Политика конфиденциальности'},
    'Prodotti digitali': {'en': 'Digital products', 'ru': 'Цифровые продукты'},
    'Prova →': {'en': 'Try it →', 'ru': 'Попробовать →'},
    'Punteggi Google PageSpeed su mobile — report disponibili su richiesta': {
        'en': 'Google PageSpeed scores on mobile — reports available on request',
        'ru': 'Баллы Google PageSpeed на мобильных — отчёты по запросу'},
    'Recensioni Google verificate': {'en': 'Verified Google reviews', 'ru': 'Подтверждённые отзывы Google'},
    'Richiedi analisi gratuita': {'en': 'Request a free analysis', 'ru': 'Запросить бесплатный анализ'},
    'Richiedi l’analisi completa': {'en': 'Request the full analysis', 'ru': 'Запросить полный анализ'},
    'Richiedi l’analisi gratuita': {'en': 'Request the free analysis', 'ru': 'Запросить бесплатный анализ'},
    'Rilevazione Google in corso — mobile, può richiedere fino a 30 secondi': {
        'en': 'Google test running — mobile, may take up to 30 seconds',
        'ru': 'Идёт замер Google — мобильная версия, до 30 секунд'},
    'SEO tecnica e dati strutturati': {'en': 'Technical SEO and structured data', 'ru': 'Техническое SEO и структурированные данные'},
    'SETTORE ARREDO SU MISURA · SEDE LISSONE (MB) · INTERVENTO RESTYLING + PWA + SEO · ANNO 2025': {
        'en': 'INDUSTRY: CUSTOM FURNITURE · LOCATION: LISSONE (MB) · PROJECT: REBUILD + PWA + SEO · YEAR 2025',
        'ru': 'ОТРАСЛЬ: МЕБЕЛЬ НА ЗАКАЗ · ГОРОД: ЛИССОНЕ (MB) · ПРОЕКТ: РЕДИЗАЙН + PWA + SEO · ГОД 2025'},
    'SETTORE VINO · SEDE ASTI · INTERVENTO E-COMMERCE IN 3 LINGUE · ANNO 2025': {
        'en': 'INDUSTRY: WINE · LOCATION: ASTI · PROJECT: E-COMMERCE IN 3 LANGUAGES · YEAR 2025',
        'ru': 'ОТРАСЛЬ: ВИНОДЕЛИЕ · ГОРОД: АСТИ · ПРОЕКТ: ИНТЕРНЕТ-МАГАЗИН НА 3 ЯЗЫКАХ · ГОД 2025'},
    'Scopri →': {'en': 'Learn more →', 'ru': 'Подробнее →'},
    'Servizi': {'en': 'Services', 'ru': 'Услуги'},
    'Strumenti gratuiti': {'en': 'Free tools', 'ru': 'Бесплатные инструменты'},
    'Strumento gratuito /01': {'en': 'Free tool /01', 'ru': 'Бесплатный инструмент /01'},
    'Strumento gratuito /02': {'en': 'Free tool /02', 'ru': 'Бесплатный инструмент /02'},
    'Strumento gratuito /03': {'en': 'Free tool /03', 'ru': 'Бесплатный инструмент /03'},
    'Strumento gratuito /04': {'en': 'Free tool /04', 'ru': 'Бесплатный инструмент /04'},
    'Vedi i casi studio': {'en': 'See the case studies', 'ru': 'Смотреть кейсы'},
    'Vino · Asti · E-commerce in 3 lingue': {'en': 'Wine · Asti · E-commerce in 3 languages', 'ru': 'Виноделие · Асти · Интернет-магазин на 3 языках'},
    'Web app su misura': {'en': 'Custom web apps', 'ru': 'Веб-приложения на заказ'},
    'base': {'en': 'basic', 'ru': 'база'},
    'completa': {'en': 'full', 'ru': 'полное'},
    'gestionale, CRM, listini, sistemi di prenotazione o pagamento particolari.': {
        'en': 'ERP, CRM, price lists, booking or custom payment systems.',
        'ru': 'учётная система, CRM, прайс-листы, бронирование или нестандартные платежи.'},
    'progetti consegnati a Milano e provincia dal 2023': {
        'en': 'projects delivered in Milan and its province since 2023',
        'ru': 'проектов сдано в Милане и провинции с 2023 года'},
    '★ 4,9 · 47 recensioni': {'en': '★ 4.9 · 47 reviews', 'ru': '★ 4,9 · 47 отзывов'},
}
CHROME.update(CHROME_EXTRA)
