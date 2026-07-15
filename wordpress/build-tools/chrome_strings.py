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

# On-page SEO pass (fase A): stringhe IT ritoccate per le parole chiave di
# focus. Solo 'en' — il RU è fase B e non si rigenera qui.
CHROME_SEO = {
    # servizio-siti-aziendali — «sito web aziendale» / «business website design»
    'Un sito web aziendale di quindici pagine, due lingue e un CMS per aggiornarlo da soli. Progettato per trasformare le visite in richieste di preventivo.': {
        'en': 'Business website design: fifteen pages, two languages and a CMS you update yourselves. Built to turn visits into quote requests.'},
    'Un sito web aziendale per chi vive di richieste, non di clic': {
        'en': 'Business website design for those who live on inquiries, not clicks'},
    # servizio-e-commerce — «realizzazione siti e-commerce» / «e-commerce website»
    'Realizzazione siti e-commerce con catalogo veloce, checkout in un passaggio e fatturazione elettronica integrata: pensata per chi vende, non solo per chi naviga.': {
        'en': 'E-commerce website with a fast catalog, one-step checkout and built-in e-invoicing: designed for businesses that sell, not just get browsed.'},
    'Realizzazione siti e-commerce per chi vende sul serio, non solo espone': {
        'en': 'An e-commerce website for businesses serious about selling, not just displaying'},
    # servizio-siti-pwa — «progressive web app»
    'Una progressive web app installabile, che funziona offline e si apre all’istante anche alla decima visita: senza i costi e i tempi di App Store e Play Store.': {
        'en': 'A progressive web app: installable, works offline, opens instantly even on the tenth visit — without the costs and timelines of the App Store and Play Store.'},
    'Una progressive web app per chi ha clienti che tornano, non solo che passano': {
        'en': 'A progressive web app for businesses with customers who come back, not just pass by'},
    # servizio-restyling-migrazione — «rifacimento sito web» / «website redesign»
    'Rifacimento sito web senza perdere posizionamento e senza riscrivere i contenuti: cambia solo la base tecnica, e cambia in meglio.': {
        'en': 'Website redesign with no rankings lost and no content to rewrite: only the technical foundation changes, and it changes for the better.'},
    'Rifacimento sito web per chi ha già i contenuti giusti, e la tecnologia sbagliata': {
        'en': 'Website redesign for businesses with the right content and the wrong technology'},
    # servizio-seo-tecnica — «SEO tecnica» / «technical SEO»
    'Core Web Vitals, dati strutturati e sitemap corretti: è la SEO tecnica, quella che il copywriting da solo non risolve.': {
        'en': 'Core Web Vitals, structured data and correct sitemaps: this is technical SEO, the part copywriting alone can’t fix.'},
    'La SEO tecnica per chi ha buoni contenuti e scarsa visibilità': {
        'en': 'Technical SEO for sites with good content and poor visibility'},
    # servizio-siti-multilingue — «sito web multilingua» / «multilingual website»
    'Un sito web multilingua è il mestiere del gruppo Remarka dal 2001: traduzione professionale, non automatica, con SEO multilingue corretta fin dal primo giorno.': {
        'en': 'A multilingual website has been the Remarka group’s trade since 2001: professional translation, not machine translation, with multilingual SEO done right from day one.'},
    'Un sito web multilingua per chi vende oltre confine, non solo in italiano': {
        'en': 'A multilingual website for businesses that sell across borders, not just in Italian'},
    # servizio-export-ready — «sito web per l’export» / «export website»
    'Un sito web per l’export vero: il sito nella lingua del cliente e la sua versione estera sotto un unico contratto, con localizzazione da madrelingua, SEO internazionale e KPI per ogni mercato. Nel settore linguistico dal 2001.': {
        'en': 'A real export website: your site in the customer’s language and its foreign version under a single contract, with native-speaker localization, international SEO and KPIs for every market. In the language business since 2001.'},
    'Un sito web per l’export, garantito nero su bianco': {
        'en': 'An export website, guaranteed in black and white'},
    # servizio-web-app — «sviluppo web app» / «custom web app»
    'Sviluppo web app su misura: portali B2B, cabine clienti, configuratori di prodotto, integrazioni con CRM e gestionale. Costruiti dallo stesso team che sviluppa i prodotti digitali del gruppo Remarka.': {
        'en': 'Custom web app development: B2B portals, client dashboards, product configurators, CRM and ERP integrations. Built by the same team that develops the Remarka group’s own digital products.'},
    'Sviluppo web app per chi ha un processo, non solo una vetrina': {
        'en': 'Custom web app for businesses with a process, not just a storefront'},
    # citta-milano — «web agency Milano» / «web agency Milan»
    'Web agency Milano': {'en': 'Web agency Milan'},
    'Web agency Milano: sei servizi, una garanzia': {
        'en': 'Web agency Milan: six services, one guarantee'},
    'Web agency Milano: il sito di Studio Legale Fontana': {
        'en': 'Web agency Milan: the Studio Legale Fontana website'},
    # strumento-test-velocita — «test velocità sito web» / «website speed test»
    'Test velocità sito web: il punteggio reale di Google': {
        'en': 'Website speed test: your real Google score'},
}
CHROME.update(CHROME_SEO)

# Remarka Lab — sette strumenti (fase T3): copy editoriale EN dei tre nuovi
# strumenti, delle tre schede rianimate, del widget test-velocità (data-*) e
# delle carte strumenti-index/cross-link servizi. Solo 'en' — il RU è scritto
# a mano nelle pagine ru-strumento-*.php (regola piano-strumenti-lab §3).
CHROME_TOOLS = {
    # ---- ricorrenti su tutte le pagine-strumento ----
    'Come funziona': {'en': 'How it works'},
    'Tre passaggi, nessuna registrazione': {'en': 'Three steps, no sign-up'},
    'Tre domande tipiche': {'en': 'Three common questions'},
    'Strumento gratuito /05': {'en': 'Free tool /05'},
    'Strumento gratuito /06': {'en': 'Free tool /06'},
    'Strumento gratuito /07': {'en': 'Free tool /07'},
    'Inserite l’indirizzo': {'en': 'Enter the address'},
    'Inserite l’indirizzo del sito': {'en': 'Enter the website address'},

    # ---- etichette-link canoniche (index, home-cards, "altri strumenti") ----
    'Test velocità': {'en': 'Speed test'},
    'Analisi SEO on-page': {'en': 'On-page SEO analysis'},
    'Check GDPR e cookie': {'en': 'GDPR and cookie check'},
    'ROI localizzazione': {'en': 'Localization ROI'},
    'Verifica accessibilità': {'en': 'Accessibility check'},
    'Sito pronto per l’AI': {'en': 'AI readiness check'},
    'Impatto CO₂': {'en': 'CO₂ impact'},
    'Le barriere di accessibilità più comuni, misurate con Google.': {
        'en': 'The most common accessibility barriers, measured with Google.'},
    'llms.txt, crawler AI, dati strutturati e sitemap: quattro segnali.': {
        'en': 'llms.txt, AI crawlers, structured data and sitemap: four signals.'},
    'Quanta CO₂ produce ogni visita — e quanta all’anno.': {
        'en': 'How much CO₂ each visit produces — and how much per year.'},

    # ---- cross-link dai servizi verso gli strumenti ----
    'Obbligo di accessibilità (EAA dal 2025): verifica il vostro sito →': {
        'en': 'Accessibility is now a legal duty (EAA from 2025): check your website →'},
    'Misura l’impatto CO₂ del sito attuale →': {
        'en': 'Measure your current website’s CO₂ impact →'},
    'Analizza la SEO on-page della vostra pagina →': {
        'en': 'Analyze the on-page SEO of your page →'},
    'Verifica se il sito è pronto per l’AI →': {
        'en': 'Check if your website is ready for AI →'},
    'Verifica se il sito è pronto per l’AI': {'en': 'Check if your website is ready for AI'},
    'Calcola il ROI della localizzazione →': {
        'en': 'Calculate your localization ROI →'},

    # ---- test-velocità: data-* del widget (aggiunti in T3 per i18n) ----
    ' — PageSpeed mobile': {'en': ' — PageSpeed mobile'},
    'Ottimo punteggio: il sito rispetta gli standard Google per l’esperienza mobile.': {
        'en': 'Great score: the website meets Google’s standards for the mobile experience.'},
    'Il sito è nella media, ma lontano dagli standard consigliati da Google. Ci sono margini di miglioramento concreti e misurabili.': {
        'en': 'The website is average, but far from the standards Google recommends. There is concrete, measurable room to improve.'},
    'Il sito è lento su mobile: la maggior parte dei visitatori abbandona prima del caricamento completo. Un restyling tecnico è la priorità.': {
        'en': 'The website is slow on mobile: most visitors leave before it finishes loading. A technical rebuild is the priority.'},
    'Punteggio Google PageSpeed e le tre metriche che lo determinano — LCP, INP, CLS — spiegate in italiano. Strategia mobile, dati reali dall’API di Google. Senza registrazione.': {
        'en': 'Your real Google PageSpeed score and the three metrics behind it — LCP, INP, CLS — explained in plain English. Mobile strategy, real data from Google’s API. No sign-up.'},
    'Scrivete l’URL del sito: la home o la pagina interna che porta più visite.': {
        'en': 'Enter the website URL: the homepage or the internal page that gets the most visits.'},
    'Misuriamo con Google': {'en': 'We measure it with Google'},
    'Interroghiamo l’API PageSpeed Insights in strategia mobile — gli stessi dati che Google usa per il posizionamento.': {
        'en': 'We query the PageSpeed Insights API in mobile strategy — the same data Google uses for ranking.'},
    'Leggete cosa frena il sito': {'en': 'See what’s slowing the website down'},
    'Punteggio 0–100 e le tre metriche Core Web Vitals spiegate in italiano, senza gergo tecnico.': {
        'en': 'A 0–100 score and the three Core Web Vitals explained in plain English, no technical jargon.'},
    'Il punteggio è quello vero di Google?': {'en': 'Is this Google’s real score?'},
    'Sì: arriva dall’API ufficiale PageSpeed Insights, strategia mobile. È lo stesso motore che trovate su pagespeed.web.dev.': {
        'en': 'Yes: it comes from the official PageSpeed Insights API, mobile strategy. It’s the same engine you’ll find on pagespeed.web.dev.'},
    'Perché misurate solo il mobile?': {'en': 'Why do you only measure mobile?'},
    'Perché Google indicizza e classifica in base alla versione mobile del sito. Il punteggio desktop, più alto quasi ovunque, conta poco per il posizionamento.': {
        'en': 'Because Google indexes and ranks based on the mobile version of the website. The desktop score, higher almost everywhere, counts for little in rankings.'},
    'Un punteggio basso danneggia le vendite?': {'en': 'Does a low score hurt sales?'},
    'Sotto i 50, gran parte dei visitatori da mobile abbandona prima del caricamento completo: le campagne portano clic che non diventano richieste.': {
        'en': 'Below 50, most mobile visitors leave before the page finishes loading: campaigns bring clicks that never become inquiries.'},
    'Report gratuito con le cause, le priorità e un preventivo chiuso: PageSpeed 90+ garantito da contratto.': {
        'en': 'A free report with the causes, the priorities and a fixed quote: PageSpeed 90+ guaranteed by contract.'},

    # ---- strumento-analisi-seo ----
    'Analisi SEO on-page: cosa vede Google sulla vostra pagina': {
        'en': 'On-page SEO analysis: what Google sees on your page'},
    'Titolo, struttura dei contenuti e dati mancanti sulla pagina che conta di più per il vostro business. Punteggio SEO di Google e le correzioni concrete, in italiano. Senza registrazione.': {
        'en': 'Title, content structure and missing data on the page that matters most to your business. Your Google SEO score and concrete fixes, explained in plain English. No sign-up.'},
    'Analizza la SEO': {'en': 'Analyze the SEO'},
    'Analisi Google in corso': {'en': 'Google analysis in progress'},
    'Scegliete la pagina giusta': {'en': 'Pick the right page'},
    'Non per forza la home: la pagina che deve posizionarsi — un servizio, una scheda, un articolo.': {
        'en': 'Not necessarily the homepage: the page that needs to rank — a service, a product page, an article.'},
    'Google la analizza': {'en': 'Google analyzes it'},
    'Usiamo la categoria SEO di Lighthouse via API PageSpeed: titoli, meta description, tag, link e struttura.': {
        'en': 'We use Lighthouse’s SEO category via the PageSpeed API: titles, meta descriptions, tags, links and structure.'},
    'Vedete cosa correggere': {'en': 'See what to fix'},
    'Punteggio 0–100 e la lista degli elementi on-page da sistemare, in ordine di priorità.': {
        'en': 'A 0–100 score and the list of on-page elements to fix, in priority order.'},
    'Questa analisi fa posizionare il sito?': {'en': 'Will this analysis get my site ranking?'},
    'Da sola no: verifica le basi tecniche on-page (titoli, struttura, dati). Il posizionamento dipende anche da contenuti e autorevolezza, che richiedono tempo.': {
        'en': 'Not on its own: it checks the technical on-page basics (titles, structure, data). Rankings also depend on content and authority, which take time to build.'},
    'Che differenza c’è con l’analisi dei contenuti?': {'en': 'How is this different from content analysis?'},
    'Qui controlliamo la parte tecnica della pagina, quella che Google legge. La qualità dei testi è un lavoro separato, che facciamo con copywriter partner.': {
        'en': 'Here we check the technical side of the page — the part Google reads. Copy quality is a separate job, one we do with partner copywriters.'},
    'Analizza tutto il sito?': {'en': 'Does it analyze the whole website?'},
    'No: una pagina alla volta, quella che indicate. È l’unità su cui Google valuta la pertinenza per una ricerca.': {
        'en': 'No: one page at a time, whichever you enter. That’s the unit Google uses to judge relevance for a search.'},
    'Vogliamo sistemare noi la SEO tecnica': {'en': 'Want us to handle your technical SEO'},
    'Audit completo, dati strutturati e Core Web Vitals a posto: PageSpeed 90+ garantito da contratto.': {
        'en': 'A full audit, structured data and Core Web Vitals sorted: PageSpeed 90+ guaranteed by contract.'},
    'Scopri la SEO tecnica': {'en': 'Discover technical SEO'},
    'Analizza la SEO on-page': {'en': 'Analyze the on-page SEO'},
    ' — SEO on-page': {'en': ' — on-page SEO'},
    'Ottimo: le basi SEO on-page sono a posto.': {'en': 'Great: the on-page SEO basics are in place.'},
    'SEO nella media: ci sono correzioni concrete da fare.': {'en': 'Average SEO: there are concrete fixes to make.'},
    'SEO on-page carente: è la priorità da sistemare.': {'en': 'Weak on-page SEO: it’s the priority to fix.'},
    'Nessun problema SEO rilevante rilevato.': {'en': 'No significant SEO issues found.'},
    'Non siamo riusciti a completare l’analisi. Riprovate tra qualche minuto.': {
        'en': 'We couldn’t complete the analysis. Please try again in a few minutes.'},

    # ---- strumento-check-gdpr ----
    'Il vostro sito è a norma GDPR?': {'en': 'Is your website GDPR compliant?'},
    'Controlliamo banner cookie, informative e tracker attivi prima del consenso: quattro verifiche per capire cosa manca. È una verifica indicativa, non una consulenza legale.': {
        'en': 'We check the cookie banner, privacy notices and trackers active before consent: four checks to see what’s missing. It’s an indicative check, not legal advice.'},
    'Controlla il sito': {'en': 'Check the website'},
    'Lettura del sito in corso': {'en': 'Reading the website'},
    'Verifica indicativa, non una consulenza legale. Un audit GDPR completo richiede la verifica manuale di cookie, finalità e basi giuridiche.': {
        'en': 'An indicative check, not legal advice. A full GDPR audit requires a manual review of cookies, purposes and legal bases.'},
    'Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura.': {
        'en': 'We read the homepage from our server, the way a first-time visitor would.'},
    'Quattro controlli automatici': {'en': 'Four automatic checks'},
    'Cerchiamo il cookie banner (CMP), i link a privacy e cookie policy, i tracker caricati prima del consenso e i domini esterni.': {
        'en': 'We look for the cookie banner (CMP), links to the privacy and cookie policy, trackers loaded before consent, and external domains.'},
    'Semaforo, non sentenza': {'en': 'A traffic light, not a verdict'},
    'Ogni punto è verde, giallo o rosso: segnaliamo i problemi evidenti, non un audit legale completo.': {
        'en': 'Each point is green, yellow or red: we flag the obvious issues, not a full legal audit.'},
    'È un parere legale?': {'en': 'Is this legal advice?'},
    'No, ed è importante dirlo: è una verifica automatica indicativa, non una consulenza legale. Segnala i problemi tecnici evidenti; la conformità piena va valutata da un consulente privacy.': {
        'en': 'No, and it’s important to say so: this is an indicative automatic check, not legal advice. It flags the obvious technical issues; full compliance should be assessed by a privacy consultant.'},
    'Cosa vuol dire «tracker senza banner»?': {'en': 'What does “trackers without a banner” mean?'},
    'Che nell’HTML iniziale della pagina troviamo strumenti di tracciamento (Google Analytics, Meta Pixel e simili) attivi prima che l’utente accetti. È il segnale rosso più frequente sui siti italiani.': {
        'en': 'That the page’s initial HTML already contains tracking tools (Google Analytics, Meta Pixel and similar) active before the user consents. It’s the most common red flag on Italian websites.'},
    'Perché il Garante è così severo sui cookie?': {'en': 'Why is Italy’s data protection authority so strict on cookies?'},
    'Perché il consenso deve essere libero, informato e documentabile: rifiutare deve essere facile quanto accettare, e nessun tracker pubblicitario può partire prima del sì.': {
        'en': 'Because consent must be free, informed and provable: refusing must be as easy as accepting, and no advertising tracker can fire before the user says yes.'},
    'Vogliamo mettere il sito a norma': {'en': 'Want us to bring the website into compliance'},
    'Banner, informative e consensi conformi al Garante, inclusi in ogni sito aziendale che consegniamo.': {
        'en': 'A compliant banner, notices and consent flow, included in every business website we deliver.'},
    'Scopri i siti aziendali': {'en': 'See business websites'},
    'Richiedi un’analisi': {'en': 'Request an analysis'},
    'Cookie banner': {'en': 'Cookie banner'},
    'Policy': {'en': 'Policy'},
    'Tracker': {'en': 'Trackers'},
    'Script esterni': {'en': 'External scripts'},
    'Cookie banner rilevato': {'en': 'Cookie banner detected'},
    'Nessun cookie banner rilevato': {'en': 'No cookie banner detected'},
    'Link a privacy/cookie policy presente': {'en': 'Link to a privacy/cookie policy present'},
    'Nessun link a privacy/cookie policy': {'en': 'No link to a privacy/cookie policy'},
    'Nessun tracker nell’HTML iniziale': {'en': 'No trackers in the initial HTML'},
    'Tracker attivi senza banner': {'en': 'Active trackers without a banner'},
    'Tracker presenti (con banner)': {'en': 'Trackers present (with banner)'},
    '{n} domini esterni caricano script': {'en': '{n} external domains load scripts'},
    'Non siamo riusciti a leggere il sito. Riprovate tra qualche minuto.': {
        'en': 'We couldn’t read the website. Please try again in a few minutes.'},

    # ---- strumento-impatto-co2 ----
    'Impatto CO₂ del vostro sito web': {'en': 'Your website’s CO₂ impact'},
    'Ogni visita al sito consuma energia e produce CO₂. Misuriamo il peso della vostra pagina e stimiamo le emissioni per visita e all’anno, con il modello Sustainable Web Design. Un sito leggero è anche un sito veloce.': {
        'en': 'Every website visit consumes energy and produces CO₂. We measure your page weight and estimate emissions per visit and per year, using the Sustainable Web Design model. A lighter website is also a faster one.'},
    'Misura l’impatto': {'en': 'Measure the impact'},
    'Misurazione in corso': {'en': 'Measuring'},
    'Peso pagina': {'en': 'Page weight'},
    'Stima annua': {'en': 'Annual estimate'},
    'Modello Sustainable Web Design (co2.js, Apache-2.0). Stima per visita; anno calcolato su 10.000 visite/mese.': {
        'en': 'Sustainable Web Design model (co2.js, Apache-2.0). Per-visit estimate; the annual figure is based on 10,000 visits/month.'},
    'La pagina da misurare: di solito la home, la più visitata.': {
        'en': 'The page to measure: usually the homepage, the most visited one.'},
    'Pesiamo la pagina': {'en': 'We weigh the page'},
    'Con l’API PageSpeed misuriamo i byte totali che il browser deve scaricare per mostrare la pagina.': {
        'en': 'Using the PageSpeed API we measure the total bytes the browser must download to show the page.'},
    'Stima delle emissioni': {'en': 'Emissions estimate'},
    'Applichiamo il modello Sustainable Web Design (co2.js) e otteniamo i grammi di CO₂e per visita, il confronto con la media del web e la stima annua.': {
        'en': 'We apply the Sustainable Web Design model (co2.js) and get the grams of CO₂e per visit, a comparison with the web average, and the annual estimate.'},
    'Come calcolate le emissioni?': {'en': 'How do you calculate emissions?'},
    'Con il modello Sustainable Web Design della Green Web Foundation (libreria co2.js, Apache-2.0): dal peso della pagina all’energia consumata, fino ai grammi di CO₂e. È una stima con coefficienti medi mondiali.': {
        'en': 'With the Green Web Foundation’s Sustainable Web Design model (the co2.js library, Apache-2.0): from page weight to energy consumed, down to grams of CO₂e. It’s an estimate using global average coefficients.'},
    'Perché un sito leggero inquina meno?': {'en': 'Why does a lighter website pollute less?'},
    'Perché ogni byte trasferito consuma energia — nel data center, nella rete, sul vostro dispositivo. Meno peso significa meno energia, meno emissioni e, come effetto collaterale, un sito più veloce.': {
        'en': 'Because every byte transferred consumes energy — in the data center, on the network, on your device. Less weight means less energy, fewer emissions and, as a side effect, a faster website.'},
    'La stima annua da dove viene?': {'en': 'Where does the annual estimate come from?'},
    'Moltiplichiamo le emissioni per visita per un traffico di riferimento di 10.000 visite al mese. Cambiando il traffico reale del vostro sito, cambia la stima proporzionalmente.': {
        'en': 'We multiply the per-visit emissions by a reference traffic of 10,000 visits a month. Change it to your website’s real traffic and the estimate scales proportionally.'},
    'Vogliamo alleggerire il sito': {'en': 'Want to lighten up the website'},
    'Immagini ottimizzate, base tecnica pulita, meno peso a parità di contenuti: meno CO₂ e PageSpeed 90+ da contratto.': {
        'en': 'Optimized images, a clean technical foundation, less weight for the same content: less CO₂ and PageSpeed 90+ by contract.'},
    'Misura la velocità': {'en': 'Measure your speed'},
    'kg CO₂e / anno': {'en': 'kg CO₂e / year'},
    'Sotto la media del web: pagina leggera, bene così.': {'en': 'Below the web average: a light page, well done.'},
    'Vicino alla media del web: c’è margine per alleggerire.': {'en': 'Close to the web average: there’s room to trim it down.'},
    'Sopra la media del web: pagina pesante, conviene ottimizzare.': {'en': 'Above the web average: a heavy page, worth optimizing.'},
    'Non siamo riusciti a misurare il peso della pagina. Riprovate.': {
        'en': 'We couldn’t measure the page weight. Please try again.'},

    # ---- strumento-roi-localizzazione ----
    'Quanto rende tradurre il vostro sito': {'en': 'What translating your website is worth'},
    'Una stima di quanto potreste guadagnare traducendo il sito in inglese o tedesco: bastano cinque numeri della vostra attività. Il calcolo resta sul vostro dispositivo. È una stima, non una promessa.': {
        'en': 'An estimate of what you could gain by translating your website into English or German: just five numbers about your business. The calculation stays on your device. It’s an estimate, not a promise.'},
    'Visite / mese': {'en': 'Visits / month'},
    'Quota estera (%)': {'en': 'Foreign share (%)'},
    'Conversione (%)': {'en': 'Conversion rate (%)'},
    'Scontrino medio (€)': {'en': 'Average order value (€)'},
    'Boost localizzazione (%)': {'en': 'Localization boost (%)'},
    'Ricalcola': {'en': 'Recalculate'},
    'Ricavo aggiuntivo / mese': {'en': 'Extra revenue / month'},
    'Ricavo aggiuntivo / anno': {'en': 'Extra revenue / year'},
    'Stima indicativa. Il boost di localizzazione (+40% conservativo) deriva da dati CSA Research sull’acquisto in lingua madre.': {
        'en': 'An indicative estimate. The localization boost (+40% conservative) is based on CSA Research data on shopping in one’s native language.'},
    'Inserite i vostri numeri': {'en': 'Enter your numbers'},
    'Visite mensili, quota di pubblico estero, tasso di conversione, scontrino medio. Se non li avete precisi, partite dalle stime.': {
        'en': 'Monthly visits, share of foreign visitors, conversion rate, average order value. If you don’t have exact figures, start with estimates.'},
    'Applichiamo il boost di localizzazione': {'en': 'We apply the localization boost'},
    'Sul pubblico estero applichiamo un incremento prudente di conversione (+40%), dai dati CSA Research sull’acquisto in lingua madre.': {
        'en': 'On foreign visitors we apply a conservative conversion increase (+40%), based on CSA Research data on buying in one’s native language.'},
    'Leggete il ricavo potenziale': {'en': 'See the potential revenue'},
    'Il calcolatore mostra il ricavo aggiuntivo stimato al mese e all’anno. Cambiate i numeri e vedete subito come si muove.': {
        'en': 'The calculator shows the estimated extra revenue per month and per year. Change the numbers and watch it move instantly.'},
    'Da dove viene il «+40%»?': {'en': 'Where does the “+40%” come from?'},
    'Dalle ricerche CSA Research: la larga maggioranza dei consumatori compra più volentieri, e più spesso, nella propria lingua. Il 40% è un valore prudente, che potete modificare.': {
        'en': 'From CSA Research: the large majority of consumers buy more willingly, and more often, in their own language. 40% is a conservative figure, and you can change it.'},
    'È una previsione garantita?': {'en': 'Is this a guaranteed forecast?'},
    'No: è una stima per ordini di grandezza, utile a capire se vale la pena approfondire. I risultati reali dipendono dal mercato, dall’offerta e dalla qualità della traduzione.': {
        'en': 'No: it’s a ballpark estimate, useful for deciding whether it’s worth digging deeper. Real results depend on the market, the offer and translation quality.'},
    'Perché tradurre da madrelingua e non con un plugin?': {'en': 'Why translate with a native speaker and not a plugin?'},
    'Perché un cliente estero riconosce un testo automatico alla seconda riga — e con lui se ne va la fiducia. Nel gruppo Remarka la traduzione la fanno madrelingua, dal 2001.': {
        'en': 'Because a foreign customer spots machine-translated text by the second line — and trust leaves with them. At the Remarka group, translation has been done by native speakers since 2001.'},
    'Vogliamo tradurre il sito sul serio': {'en': 'Want to translate the website properly'},
    'Traduzione professionale da madrelingua e SEO internazionale corretta dal primo giorno — non un plugin.': {
        'en': 'Professional translation by native speakers and correct international SEO from day one — not a plugin.'},

    # ---- strumento-sito-pronto-ai ----
    'Il vostro sito è pronto per l’AI?': {'en': 'Is your website ready for AI?'},
    'Quando ChatGPT, Claude o Perplexity leggono il web, trovano il vostro sito? Controlliamo quattro segnali: llms.txt, accesso dei crawler AI, dati strutturati e sitemap. Senza registrazione.': {
        'en': 'When ChatGPT, Claude or Perplexity read the web, do they find your website? We check four signals: llms.txt, AI crawler access, structured data and sitemap. No sign-up.'},
    'Verifica la prontezza AI': {'en': 'Check AI readiness'},
    'Verifica in corso': {'en': 'Checking'},
    'Crawler AI': {'en': 'AI crawlers'},
    'Controlla llms.txt, l’accesso dei crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.': {
        'en': 'Checks llms.txt, AI crawler access (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), JSON-LD structured data and the sitemap.'},
    'Leggiamo dal nostro server alcuni file pubblici e l’HTML della home page.': {
        'en': 'We read a few public files and the homepage HTML from our server.'},
    'Quattro verifiche': {'en': 'Four checks'},
    'Cerchiamo il file llms.txt, controlliamo se robots.txt lascia passare i crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.': {
        'en': 'We look for the llms.txt file, check whether robots.txt lets AI crawlers through (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), plus JSON-LD structured data and the sitemap.'},
    'Punteggio N su 4': {'en': 'Score N out of 4'},
    'Un semaforo per ogni segnale e un punteggio complessivo, con le indicazioni su cosa aggiungere per farsi trovare e citare dai modelli.': {
        'en': 'A traffic light for each signal and an overall score, with guidance on what to add to get found and cited by AI models.'},
    'Cos’è il file llms.txt?': {'en': 'What is the llms.txt file?'},
    'Una proposta di standard: un file di testo in Markdown che riassume ai modelli AI cosa contiene il sito e come citarlo, come fa robots.txt per i motori di ricerca. È giovane, ma sempre più diffuso.': {
        'en': 'A proposed standard: a Markdown text file that tells AI models what the website contains and how to cite it, the way robots.txt does for search engines. It’s young, but increasingly common.'},
    'Conviene far entrare i crawler AI?': {'en': 'Should you let AI crawlers in?'},
    'Dipende dagli obiettivi: bloccarli protegge i contenuti, ma vi esclude dalle risposte generate. Per la maggior parte delle aziende, essere citati da ChatGPT o Perplexity è visibilità in più.': {
        'en': 'It depends on your goals: blocking them protects your content, but excludes you from generated answers. For most businesses, being cited by ChatGPT or Perplexity is extra visibility.'},
    'I dati strutturati servono ancora?': {'en': 'Is structured data still worth it?'},
    'Sì, più che mai: i dati JSON-LD (schema.org) aiutano sia Google sia i modelli AI a capire chi siete, cosa offrite e a chi. Sono la base di ogni buona indicizzazione.': {
        'en': 'Yes, more than ever: JSON-LD data (schema.org) helps both Google and AI models understand who you are, what you offer and to whom. It’s the foundation of good indexing.'},
    'Vogliamo preparare il sito per l’AI': {'en': 'Want to get the website ready for AI'},
    'Dati strutturati, file corretti e struttura leggibile dalle macchine: fa parte della SEO tecnica che consegniamo.': {
        'en': 'Structured data, the right files and a machine-readable structure: it’s part of the technical SEO we deliver.'},
    'Sì': {'en': 'Yes'},
    'No': {'en': 'No'},
    'Parziale': {'en': 'Partial'},

    # ---- strumento-verifica-accessibilita ----
    'Verifica accessibilità: il vostro sito è usabile da tutti?': {
        'en': 'Accessibility check: is your website usable by everyone?'},
    'Controlliamo con Google le barriere di accessibilità più comuni — contrasti, etichette, struttura. Dal 28 giugno 2025 l’European Accessibility Act rende l’accessibilità un obbligo per molti siti. Senza registrazione.': {
        'en': 'We use Google to check the most common accessibility barriers — contrast, labels, structure. Since 28 June 2025 the European Accessibility Act makes accessibility a legal duty for many websites. No sign-up.'},
    'Verifica l’accessibilità': {'en': 'Check accessibility'},
    'Analisi in corso': {'en': 'Analyzing'},
    'Controllo automatico (Lighthouse): copre parte dei criteri WCAG 2.1 AA. La conformità EAA richiede anche verifica manuale.': {
        'en': 'Automatic check (Lighthouse): it covers part of the WCAG 2.1 AA criteria. Full EAA compliance also requires a manual review.'},
    'La pagina da controllare: la home o una pagina di servizio, dove passano più utenti.': {
        'en': 'The page to check: the homepage or a service page, wherever most users land.'},
    'Analisi Lighthouse': {'en': 'Lighthouse analysis'},
    'Usiamo la categoria Accessibilità di Lighthouse via API PageSpeed: contrasti, testi alternativi, etichette dei moduli, struttura dei titoli.': {
        'en': 'We use Lighthouse’s Accessibility category via the PageSpeed API: contrast, alt text, form labels, heading structure.'},
    'Vedete le barriere da rimuovere': {'en': 'See the barriers to remove'},
    'Punteggio 0–100 e la lista dei problemi rilevati, in italiano. Un controllo automatico copre parte dei criteri WCAG, non tutti.': {
        'en': 'A 0–100 score and the list of issues found, explained in plain English. An automatic check covers part of the WCAG criteria, not all of them.'},
    'Cos’è l’European Accessibility Act?': {'en': 'What is the European Accessibility Act?'},
    'Una direttiva europea (EAA) applicata in Italia dal 28 giugno 2025: molti siti di aziende che vendono a consumatori devono essere accessibili secondo lo standard WCAG 2.1 livello AA. È un obbligo, con alcune esenzioni per le microimprese.': {
        'en': 'A European directive (EAA), in force in Italy since 28 June 2025: many websites of businesses selling to consumers must be accessible to the WCAG 2.1 level AA standard. It’s a legal duty, with some exemptions for microenterprises.'},
    'Questo test basta per essere conformi?': {'en': 'Is this test enough to be compliant?'},
    'No: un controllo automatico intercetta una parte dei criteri WCAG. La conformità piena richiede anche verifica manuale — navigazione da tastiera, screen reader, contenuti. È un ottimo punto di partenza, non un certificato.': {
        'en': 'No: an automatic check catches only part of the WCAG criteria. Full compliance also requires manual testing — keyboard navigation, screen readers, content. It’s a great starting point, not a certificate.'},
    'Riguarda anche la mia azienda?': {'en': 'Does this apply to my business too?'},
    'Se vendete beni o servizi a consumatori online (e-commerce, banche, trasporti, servizi), con ogni probabilità sì. Le microimprese che offrono servizi hanno esenzioni: meglio verificare caso per caso.': {
        'en': 'If you sell goods or services to consumers online (e-commerce, banking, transport, services), most likely yes. Microenterprises offering services have exemptions: it’s best to check case by case.'},
    'Vogliamo rendere il sito accessibile': {'en': 'Want to make the website accessible'},
    'Verifichiamo le barriere una per una — automatiche e manuali — e le sistemiamo secondo lo standard WCAG 2.1 AA.': {
        'en': 'We check the barriers one by one — automatic and manual — and fix them to the WCAG 2.1 AA standard.'},
    'Richiedi una verifica di accessibilità': {'en': 'Request an accessibility check'},
    ' — accessibilità': {'en': ' — accessibility'},
    'Ottimo: le barriere principali sono già rimosse.': {'en': 'Great: the main barriers are already removed.'},
    'Accessibilità nella media: alcune barriere restano.': {'en': 'Average accessibility: some barriers remain.'},
    'Accessibilità carente: barriere importanti per gli utenti.': {'en': 'Poor accessibility: significant barriers for users.'},
    'Nessuna barriera rilevante rilevata.': {'en': 'No significant barriers found.'},
}
CHROME.update(CHROME_TOOLS)

# Sezioni SEO L2 delle 7 pagine strumenti (metodologia / lettura del
# risultato / come migliorare) — coppie IT→EN per il conveyor EN.
CHROME_TOOLS_L2 = {
    # Due residui T3 sfuggiti all'euristica ITALIAN_HINT (nessuna parola
    # frequente nel testo) — scoperti al rendering delle pagine EN.
    'Incollate l’indirizzo': {'en': 'Paste in the address'},
    'Vogliamo sistemare noi questi problemi': {'en': 'Want us to fix these problems'},
    'Il metodo': {'en': 'The method'},
    'Leggere il risultato': {'en': 'Reading the result'},
    'Come migliorare': {'en': 'How to improve'},
    'Cosa misura davvero questo test dei tempi di caricamento': {
        'en': 'What this website loading-speed test actually measures'},
    'Dietro il punteggio c’è un motore solo: l’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev. Interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Il numero da 0 a 100 nasce in laboratorio, con un telefono e una connessione simulati e standardizzati: così due misurazioni della stessa pagina restano confrontabili nel tempo. Dove il vostro sito riceve abbastanza traffico reale, aggiungiamo anche i Core Web Vitals raccolti sul campo dagli utenti veri di Chrome.': {
        'en': 'There’s only one engine behind the score: Google’s PageSpeed Insights API, the same one that powers pagespeed.web.dev. We query Lighthouse in mobile strategy, because that’s the version of your site Google uses to rank you. The 0–100 number is born in a lab, with a simulated phone and connection kept standard: that way two measurements of the same page stay comparable over time. Where your site gets enough real traffic, we also add the Core Web Vitals collected in the field from actual Chrome users.'},
    'È giusto sapere cosa questo test non guarda. Non giudica la qualità dei testi, non conta i link in entrata, non misura la sicurezza del server né quanto vendete: pesa solo l’esperienza di caricamento di una singola pagina. Un punteggio alto non è la promessa di un primo posto su Google, ma una base tecnica sana su cui tutto il resto lavora meglio. Preferiamo dirlo chiaro: è la fotografia precisa di un aspetto, non la diagnosi completa del sito.': {
        'en': 'It’s only fair to say what this test doesn’t look at. It doesn’t judge the quality of your copy, doesn’t count inbound links, doesn’t measure server security or how much you sell: it only weighs the loading experience of a single page. A high score isn’t a promise of a first-place ranking on Google, but a healthy technical base that everything else works better on. We’d rather say it plainly: it’s a precise snapshot of one aspect, not a complete diagnosis of your site.'},
    'Come leggere il punteggio delle prestazioni del sito': {
        'en': 'How to read your website’s performance score'},
    'Il risultato si legge come un semaforo. Da 90 a 100 siete in fascia verde: la pagina compare in fretta anche in mobilità, sul 4G di città come ai bordi della copertura. Tra 50 e 89 la velocità è nella media del web italiano, con margini concreti di guadagno. Sotto 50 siete nel rosso: buona parte dei visitatori da smartphone se ne va prima che appaia la prima riga, e ogni euro investito in pubblicità rende molto meno.': {
        'en': 'Read the result like a traffic light. From 90 to 100 you’re in the green zone: the page appears quickly even on the move, on city 4G as well as at the edge of coverage. Between 50 and 89, speed is around the average for the Italian web, with concrete room to gain. Below 50 you’re in the red: a good share of mobile visitors leave before the first line even appears, and every euro spent on advertising returns much less.'},
    'Due falsi allarmi ricorrenti. Il valore oscilla di qualche punto tra una prova e l’altra: è normale, dipende dai server di misura di Google, non dal vostro sito — contano i grandi salti, non i due punti di scarto. E non spaventatevi se il desktop segna 95 e il mobile 40: quasi tutti i siti hanno questo divario, ma è il mobile a decidere la classifica. Guardate sempre quel numero.': {
        'en': 'Two recurring false alarms. The value swings by a few points between one run and the next: that’s normal, it depends on Google’s measuring servers, not your site — the big jumps matter, not a two-point gap. And don’t panic if desktop scores 95 while mobile scores 40: almost every site has this gap, but it’s mobile that decides your ranking. Always watch that number.'},
    'Come velocizzare il sito web: cinque interventi concreti': {
        'en': 'How to speed up your website: five concrete fixes'},
    'Un punteggio basso nasce quasi sempre dalle stesse cause, e le prime sono anche le più economiche da correggere.': {
        'en': 'A low score almost always comes from the same handful of causes, and the first ones are also the cheapest to fix.'},
    'Alleggerite le immagini': {'en': 'Lighten your images'},
    'Convertite le fotografie in WebP o AVIF e attivate il caricamento differito: è la causa numero uno della lentezza e spesso, da sola, dimezza i tempi di attesa.': {
        'en': 'Convert photos to WebP or AVIF and turn on lazy loading: it’s the number-one cause of slowness, and on its own it often cuts waiting times in half.'},
    'Attivate la cache': {'en': 'Turn on caching'},
    'Una cache di pagina e del browser evita al server di ricostruire tutto a ogni visita: mezza giornata di lavoro, risultato misurabile da subito.': {
        'en': 'Page and browser caching stop the server from rebuilding everything on every visit: half a day of work, with results you can measure right away.'},
    'Sfoltite CSS e JavaScript': {'en': 'Trim your CSS and JavaScript'},
    'Portate in linea il CSS critico, rimandate il resto e togliete gli script di terze parti che non servono: meno codice da eseguire, prima visualizzazione più rapida.': {
        'en': 'Inline the critical CSS, defer the rest, and remove third-party scripts you don’t need: less code to run, a faster first paint.'},
    'Scegliete un hosting all’altezza': {'en': 'Choose hosting that’s up to the job'},
    'Un server condiviso e sovraffollato risponde in un secondo prima ancora di iniziare: un hosting adeguato, con una CDN davanti, taglia quell’attesa iniziale.': {
        'en': 'An overcrowded shared server takes a full second to respond before it even starts loading the page: proper hosting, with a CDN in front of it, cuts that initial wait.'},
    'Controllate i font': {'en': 'Keep your fonts in check'},
    'Limitate le famiglie di caratteri, precaricate quelle essenziali e usate font-display swap, così il testo appare subito invece di restare invisibile.': {
        'en': 'Limit the number of typefaces, preload the essential ones, and use font-display: swap, so text shows up immediately instead of staying invisible.'},
    'Vogliamo intervenire noi: scopri il restyling tecnico →': {
        'en': 'Want us to fix it for you? See our technical redesign service →'},
    'Approfondisci: le 7 cause reali di un sito lento →': {
        'en': 'Read more: the 7 real causes of a slow website →'},
    'Che cosa controlla davvero l’audit SEO della pagina': {
        'en': 'What this on-page SEO audit actually checks'},
    'Anche qui il motore è Google: usiamo la categoria SEO di Lighthouse attraverso l’API PageSpeed, in strategia mobile. In pochi secondi Lighthouse legge la pagina come farebbe il crawler e verifica gli elementi tecnici on-page: presenza e unicità del title, meta description, tag corretti, testi dei link descrittivi, indicizzabilità, leggibilità sullo schermo del telefono. Ne esce un punteggio da 0 a 100 con l’elenco puntuale di ciò che non supera il controllo.': {
        'en': 'Here too the engine is Google: we use Lighthouse’s SEO category through the PageSpeed API, in mobile strategy. In a few seconds, Lighthouse reads the page the way a crawler would and checks the technical on-page elements: whether the title exists and is unique, the meta description, correct tags, descriptive link text, indexability, readability on a phone screen. The result is a 0–100 score with a precise list of what fails the check.'},
    'Vale la pena chiarire i confini. Questo esame guarda la struttura tecnica di una singola pagina, non la qualità dei contenuti, non i link che altri siti vi dedicano, non l’autorevolezza che si costruisce nel tempo. Non prevede in che posizione finirete, né studia la concorrenza sulle vostre parole chiave. È il controllo delle fondamenta: se sono storte, nemmeno il testo migliore rende; se sono a posto, avete tolto di mezzo gli ostacoli tecnici.': {
        'en': 'It’s worth being clear about the boundaries. This test looks at the technical structure of a single page, not the quality of your writing, not the links other sites give you, not the authority that builds up over time. It doesn’t predict what position you’ll rank in, and it doesn’t study your competitors on your keywords. It’s a check of the foundations: if they’re crooked, not even the best copy pays off; if they’re solid, you’ve cleared the technical obstacles out of the way.'},
    'Come interpretare il punteggio SEO di Google': {
        'en': 'How to interpret your Google SEO score'},
    'Da 90 in su le basi tecniche sono in ordine e potete concentrarvi su contenuti e reputazione. Tra 50 e 89 restano correzioni concrete — spesso un title mancante o una description duplicata — che si sistemano in fretta. Sotto 50 c’è qualcosa che ostacola l’indicizzazione: è la priorità, prima di ogni altra cosa. Leggete la lista degli avvisi dall’alto verso il basso: è già ordinata per impatto.': {
        'en': 'From 90 up, the technical basics are in order and you can focus on content and reputation. Between 50 and 89 there are still concrete fixes to make — often a missing title or a duplicate description — that are quick to sort out. Below 50, something is standing in the way of indexing: that’s the priority, before anything else. Read the list of warnings from top to bottom: it’s already sorted by impact.'},
    'Attenzione a due letture sbagliate. Un punteggio pieno non vuol dire «primi su Google»: significa solo che la pagina è tecnicamente leggibile, e il posizionamento arriva con contenuti e tempo. E un avviso su un tag secondario non è un’emergenza: distinguete i problemi che bloccano l’indicizzazione da quelli cosmetici, e partite dai primi.': {
        'en': 'Watch out for two common misreadings. A perfect score doesn’t mean “first on Google”: it only means the page is technically readable, and ranking comes with content and time. And a warning on a minor tag isn’t an emergency: tell the problems that block indexing apart from the cosmetic ones, and start with the former.'},
    'Come migliorare il posizionamento on-page': {'en': 'How to improve your on-page rankings'},
    'La SEO tecnica on-page è fatta di poche cose fatte bene, ripetute su ogni pagina che conta.': {
        'en': 'Technical on-page SEO comes down to a few things done well, repeated on every page that matters.'},
    'Un title e una description su misura': {'en': 'A title and description built for the page'},
    'Scrivete per ogni pagina un titolo unico e descrittivo e una meta description che invita al clic: sono la prima cosa che vede chi cerca.': {
        'en': 'Write a unique, descriptive title for every page and a meta description that invites the click: they’re the first thing a searcher sees.'},
    'Una gerarchia di titoli pulita': {'en': 'A clean heading hierarchy'},
    'Un solo H1, poi H2 e H3 ordinati per argomento: aiutano Google e i lettori a capire la struttura della pagina in un colpo d’occhio.': {
        'en': 'One single H1, then H2s and H3s ordered by topic: they help both Google and readers grasp the page’s structure at a glance.'},
    'Aggiungete i dati strutturati': {'en': 'Add structured data'},
    'Il markup schema.org in JSON-LD dice ai motori chi siete e cosa offrite, e vi rende idonei ai risultati arricchiti.': {
        'en': 'Schema.org markup in JSON-LD tells search engines who you are and what you offer, and makes you eligible for rich results.'},
    'Curate link interni e URL': {'en': 'Take care of internal links and URLs'},
    'Collegate le pagine tra loro con testi di ancoraggio chiari e mantenete indirizzi brevi e leggibili: la struttura conta quanto il contenuto.': {
        'en': 'Link your pages to each other with clear anchor text and keep addresses short and readable: structure matters as much as content.'},
    'Tenete in ordine sitemap e robots': {'en': 'Keep your sitemap and robots file in order'},
    'Una sitemap XML aggiornata e un robots.txt corretto guidano il crawler; se il sito è in più lingue, aggiungete i tag hreflang.': {
        'en': 'An up-to-date XML sitemap and a correct robots.txt guide the crawler; if your site has multiple languages, add hreflang tags.'},
    'Vogliamo sistemarla noi: scopri la SEO tecnica →': {
        'en': 'Want us to fix it for you? See our technical SEO service →'},
    'Approfondisci: i Core Web Vitals nel 2026 →': {'en': 'Read more: Core Web Vitals in 2026 →'},
    'Cosa verifica davvero questo controllo cookie': {
        'en': 'What this cookie compliance check actually verifies'},
    'A differenza dei test basati su Google, qui è il nostro server a leggere la home page del vostro sito, esattamente come la vedrebbe un visitatore alla prima apertura, prima di qualsiasi clic. Su quell’HTML facciamo quattro controlli automatici: cerchiamo il banner dei cookie (la CMP: Iubenda, Cookiebot, Complianz e simili), i collegamenti a privacy e cookie policy, gli strumenti di tracciamento che partono prima del consenso e i domini esterni che la pagina richiama.': {
        'en': 'Unlike the Google-based tests, here it’s our own server that reads your website’s home page, exactly as a visitor would see it on first landing, before any click. On that HTML we run four automatic checks: we look for the cookie banner (the CMP: Iubenda, Cookiebot, Complianz and similar tools), links to the privacy and cookie policies, tracking tools that fire before consent, and the external domains the page calls.'},
    'Diciamolo subito, perché conta: non è un parere legale. È una verifica tecnica indicativa, che intercetta i problemi evidenti — quelli che il Garante contesta più spesso — ma non sostituisce un consulente privacy. Non legge cosa accade dopo che l’utente accetta, non valuta i vostri registri dei consensi, non esamina le informative riga per riga. È un ottimo punto di partenza per capire dove intervenire, non un certificato di conformità.': {
        'en': 'Let’s say it upfront, because it matters: this is not legal advice. It’s an indicative technical check that catches the obvious problems — the ones Italy’s Data Protection Authority challenges most often — but it doesn’t replace a privacy consultant. It doesn’t see what happens after the user accepts, doesn’t evaluate your consent records, and doesn’t examine your policies line by line. It’s a great starting point to see where to act, not a certificate of compliance.'},
    'Come leggere il semaforo di conformità': {'en': 'How to read your compliance traffic light'},
    'Ogni punto riceve un colore, e il colore va preso per quello che è. Verde: il segnale è presente e a posto. Giallo: qualcosa c’è ma va verificato a mano — per esempio una policy che esiste ma potrebbe essere incompleta. Rosso: manca un elemento importante o, peggio, ci sono tracker attivi senza un banner che li governi. Il quadro d’insieme conta più del singolo pallino.': {
        'en': 'Every checkpoint gets a colour, and the colour should be read for exactly what it is. Green: the signal is present and correct. Yellow: something is there but needs a manual check — a policy that exists but might be incomplete, for instance. Red: an important element is missing or, worse, there are active trackers with no banner governing them. The overall picture matters more than any single dot.'},
    'Il rosso più frequente sui siti italiani è «tracker senza banner»: Google Analytics o il Pixel di Meta che si attivano nell’HTML iniziale, prima del sì dell’utente. È anche l’errore che il Garante sanziona con più decisione. Un giallo, invece, di solito non è un’emergenza: spesso basta completare o aggiornare un’informativa già presente.': {
        'en': 'The most common red flag on Italian websites is “trackers without a banner”: Google Analytics or the Meta Pixel firing in the initial HTML, before the user has said yes. It’s also the mistake Italy’s Data Protection Authority penalises most decisively. A yellow, on the other hand, is usually not an emergency: often it just takes completing or updating a policy that’s already there.'},
    'Come mettere a norma il consenso e i cookie': {
        'en': 'How to bring your consent and cookies up to standard'},
    'La conformità pratica si costruisce con pochi accorgimenti, ma vanno rispettati tutti.': {
        'en': 'Practical compliance is built from a handful of measures, but every one of them has to be respected.'},
    'Installate una CMP che blocca davvero': {'en': 'Install a CMP that actually blocks trackers'},
    'Un banner serio non deve solo comparire: deve impedire ai tracker di partire finché l’utente non ha accettato. È la differenza tra sembrare a norma ed esserlo.': {
        'en': 'A proper banner shouldn’t just appear: it has to stop trackers from firing until the user has accepted. That’s the difference between looking compliant and being compliant.'},
    'Rendete il rifiuto facile quanto l’assenso': {'en': 'Make refusing as easy as accepting'},
    'Il pulsante «Rifiuta» deve avere lo stesso peso di «Accetta», sulla stessa schermata: niente cookie wall, niente percorsi a ostacoli per dire di no.': {
        'en': 'The “Reject” button must carry the same visual weight as “Accept”, on the same screen: no cookie walls, no obstacle course for saying no.'},
    'Pubblicate informative complete': {'en': 'Publish complete policies'},
    'Privacy policy e cookie policy chiare, aggiornate e facili da trovare: devono dire cosa raccogliete, perché e con chi lo condividete.': {
        'en': 'Clear, up-to-date privacy and cookie policies that are easy to find: they need to state what you collect, why, and who you share it with.'},
    'Rendete il consenso documentabile': {'en': 'Make consent provable'},
    'Conservate la prova di ogni consenso — quando, per cosa — così da poterla mostrare se richiesto: il sì deve essere libero, informato e tracciabile.': {
        'en': 'Keep a record of every consent — when, for what — so you can show it if asked: the yes has to be freely given, informed and traceable.'},
    'Caricate i tracker dopo il sì': {'en': 'Load trackers only after the yes'},
    'Analytics, pixel e mappe di calore vanno attivati solo dopo l’accettazione, in modo condizionato: prima del consenso la pagina deve restare pulita.': {
        'en': 'Analytics, pixels and heatmaps should only activate after acceptance, conditionally: before consent, the page has to stay clean.'},
    'Lo includiamo in ogni sito aziendale che consegniamo →': {
        'en': 'We include it in every business website we deliver →'},
    'Approfondisci: la checklist cookie 2026 del Garante →': {
        'en': 'Read more: the 2026 cookie checklist from Italy’s Data Protection Authority →'},
    'Come funziona davvero questa stima del ROI': {'en': 'How this ROI estimate actually works'},
    'Questo strumento non interroga alcun server e non guarda il vostro sito: è un calcolatore che gira interamente sul vostro dispositivo, e i numeri che inserite non lasciano il browser. Prende cinque dati della vostra attività — visite mensili, quota di pubblico estero, tasso di conversione, scontrino medio — e li combina con un incremento di conversione applicato alla sola fetta di visitatori stranieri.': {
        'en': 'This tool doesn’t query any server and doesn’t look at your website: it’s a calculator that runs entirely on your device, and the numbers you enter never leave your browser. It takes five figures from your business — monthly visits, share of foreign visitors, conversion rate, average order value — and combines them with a conversion boost applied only to the slice of foreign visitors.'},
    'Quell’incremento, un prudente +40%, viene dalle ricerche CSA Research: la larga maggioranza delle persone compra più volentieri, e più spesso, nella propria lingua. È un valore di partenza, non una legge fisica: potete modificarlo. E qui sta anche il limite onesto dello strumento — è una stima per ordini di grandezza, non una previsione garantita. Non conosce il vostro mercato, la vostra offerta né la qualità della traduzione, che sono poi ciò che fa la differenza vera.': {
        'en': 'That boost, a conservative +40%, comes from CSA Research: the large majority of people buy more willingly, and more often, in their own language. It’s a starting value, not a law of physics: you can change it. And that’s also the tool’s honest limit — it’s an order-of-magnitude estimate, not a guaranteed forecast. It doesn’t know your market, your offer, or the quality of your translation, which is what really makes the difference.'},
    'Come interpretare il ricavo potenziale stimato': {
        'en': 'How to interpret the estimated potential revenue'},
    'Il risultato va letto come una forchetta, non come una cifra al centesimo. Serve a rispondere a una sola domanda: vale la pena approfondire la traduzione del sito, sì o no? Se il ricavo aggiuntivo stimato all’anno copre comodamente il costo di un progetto multilingue, il segnale è chiaro. Se è modesto, forse il vostro pubblico estero è ancora troppo piccolo perché l’investimento si ripaghi in fretta.': {
        'en': 'Read the result as a range, not as a figure down to the cent. It exists to answer a single question: is it worth looking further into translating your website, yes or no? If the estimated extra revenue per year comfortably covers the cost of a multilingual project, the signal is clear. If it’s modest, your foreign audience may still be too small for the investment to pay off quickly.'},
    'Muovete i numeri e osservate come reagisce la stima: è lì che il calcolatore diventa utile. Alzando la quota di visitatori esteri o lo scontrino medio, il ricavo cresce in fretta, e questo vi dice quali leve pesano di più nel vostro caso. Ricordate che tutto parte dalle vostre cifre: se sono ottimistiche, lo sarà anche il risultato. Meglio partire da stime prudenti.': {
        'en': 'Move the numbers around and watch how the estimate reacts: that’s where the calculator becomes useful. Raise the share of foreign visitors or the average order value, and revenue climbs quickly — which tells you which levers matter most in your case. Remember it all starts from your own figures: if they’re optimistic, so will the result be. Better to start from conservative estimates.'},
    'Come aumentare il rendimento della traduzione': {
        'en': 'How to increase the return on translating your website'},
    'Tradurre un sito rende, ma solo se è fatto per vendere e non per figurare.': {
        'en': 'Translating a website pays off, but only if it’s done to sell, not just to look good.'},
    'Traducete da madrelingua, non con un plugin': {
        'en': 'Translate with native speakers, not a plugin'},
    'Un cliente estero riconosce un testo automatico alla seconda riga, e con lui se ne va la fiducia. La traduzione professionale è ciò che trasforma la visita in ordine.': {
        'en': 'A foreign customer spots machine-translated text by the second line, and trust leaves with them. Professional translation is what turns a visit into an order.'},
    'Localizzate, non solo tradurre': {'en': 'Localise, don’t just translate'},
    'Adattate offerta, inviti all’azione, valuta e formati al mercato di arrivo: vendere in Germania non è tradurre le schede, è parlare come parla quel mercato.': {
        'en': 'Adapt your offer, calls to action, currency and formats to the target market: selling in Germany isn’t about translating product pages, it’s about speaking the way that market speaks.'},
    'Impostate la SEO internazionale': {'en': 'Set up international SEO'},
    'Ogni lingua ha bisogno dei suoi URL, dei tag hreflang e dei metadati dedicati, altrimenti Google non capisce a chi mostrare quale versione.': {
        'en': 'Every language needs its own URLs, hreflang tags and dedicated metadata, otherwise Google can’t tell who to show which version to.'},
    'Partite dal mercato con più domanda': {'en': 'Start with the market with the most demand'},
    'Non tutte le lingue rendono uguale: cominciate da dove i dati mostrano già interesse, poi allargate mercato per mercato.': {
        'en': 'Not every language pays off equally: start where the data already shows interest, then expand market by market.'},
    'Curate anche il dopo-vendita': {'en': 'Take care of after-sales too'},
    'Moduli, email di conferma e assistenza nella lingua del cliente: la fiducia si conferma dopo l’acquisto, non solo prima.': {
        'en': 'Forms, confirmation emails and support in the customer’s language: trust is confirmed after the purchase, not only before it.'},
    'Vogliamo tradurlo sul serio: scopri i siti multilingue →': {
        'en': 'Want it translated properly? See our multilingual websites service →'},
    'Approfondisci: costi e tempi di un sito in quattro lingue →': {
        'en': 'Read more: the costs and timeline of a website in four languages →'},
    'Cosa controlla davvero questo test di accessibilità': {
        'en': 'What this website accessibility test actually checks'},
    'Il motore è la categoria Accessibilità di Lighthouse, richiamata via API PageSpeed: gli stessi controlli automatici che Google mette a disposizione degli sviluppatori. In pochi secondi la pagina viene esaminata su decine di regole tecniche — contrasto tra testo e sfondo, testi alternativi delle immagini, etichette dei campi nei moduli, ordine dei titoli, uso corretto degli attributi ARIA — e ne esce un punteggio da 0 a 100 con l’elenco delle barriere rilevate.': {
        'en': 'The engine is Lighthouse’s Accessibility category, called through the PageSpeed API: the same automatic checks Google makes available to developers. In a few seconds the page is examined against dozens of technical rules — contrast between text and background, image alt text, form field labels, heading order, correct use of ARIA attributes — producing a 0–100 score with the list of barriers found.'},
    'Serve chiarezza sui limiti, perché qui è facile illudersi. Un controllo automatico intercetta soltanto una parte dei criteri WCAG 2.1 AA: cattura ciò che una macchina sa misurare, non ciò che va provato da una persona. Non verifica la navigazione da tastiera, l’esperienza con uno screen reader, la chiarezza dei contenuti per chi ha difficoltà cognitive. È il primo gradino verso la conformità richiesta dall’European Accessibility Act, non il certificato finale.': {
        'en': 'It’s worth being clear about the limits, because it’s easy to fool yourself here. An automatic check only catches part of the WCAG 2.1 AA criteria: it captures what a machine can measure, not what a person needs to test. It doesn’t check keyboard navigation, the experience with a screen reader, or how clear your content is for people with cognitive difficulties. It’s the first step toward the compliance required by the European Accessibility Act, not the final certificate.'},
    'Come leggere il punteggio e le barriere rilevate': {
        'en': 'How to read the score and the barriers found'},
    'Il numero da 0 a 100 dice quanto la pagina supera i controlli automatici: più è alto, meno ostacoli evidenti restano. Ma il punteggio conta meno dell’elenco che lo accompagna. Ogni voce è una barriera concreta per una persona reale — un contrasto troppo debole per chi ci vede poco, un pulsante senza etichetta per chi usa uno screen reader. Partite da quelle, non dal totale.': {
        'en': 'The 0–100 number tells you how well the page passes the automatic checks: the higher it is, the fewer obvious obstacles remain. But the score matters less than the list that comes with it. Each entry is a concrete barrier for a real person — contrast too weak for someone with low vision, a button with no label for someone using a screen reader. Start from those, not from the total.'},
    'Un avvertimento sui falsi sensi di sicurezza: anche un 100 pieno non significa «sito conforme». Vuol dire che avete superato i test che una macchina può fare, e sono circa un terzo dei problemi possibili. Il resto — tastiera, lettori di schermo, contenuti — si verifica a mano. Prendete quindi un punteggio alto come una buona base, non come un traguardo raggiunto.': {
        'en': 'A warning against false confidence: even a perfect 100 doesn’t mean “compliant website”. It means you’ve passed the tests a machine can run, which cover roughly a third of the possible issues. The rest — keyboard, screen readers, content — has to be checked by hand. So treat a high score as a good foundation, not as a finish line already crossed.'},
    'Come rendere il sito accessibile a tutti': {
        'en': 'How to make your website accessible to everyone'},
    'Molte barriere cadono con correzioni semplici, che migliorano l’esperienza di chiunque, non solo di chi ha una disabilità.': {
        'en': 'Many barriers fall with simple fixes that improve the experience for everyone, not just for people with disabilities.'},
    'Aumentate il contrasto': {'en': 'Increase your contrast'},
    'Testo e sfondo devono avere un rapporto di contrasto di almeno 4,5:1: il grigio chiaro elegante sullo schermo del designer diventa illeggibile al sole o per chi ci vede poco.': {
        'en': 'Text and background need a contrast ratio of at least 4.5:1: the elegant light grey that looks fine on a designer’s screen becomes unreadable in sunlight or for people with low vision.'},
    'Descrivete le immagini': {'en': 'Describe your images'},
    'Ogni immagine informativa ha bisogno di un testo alternativo che ne racconti il contenuto: è ciò che uno screen reader legge a chi non può vederla.': {
        'en': 'Every informative image needs alt text describing its content: it’s what a screen reader reads out to someone who can’t see it.'},
    'Etichettate i moduli': {'en': 'Label your forms'},
    'Ogni campo deve avere un’etichetta esplicita e collegata: «Nome», «Email», «Messaggio», non solo un testo grigio che sparisce appena si scrive.': {
        'en': 'Every field needs an explicit, properly linked label — “Name”, “Email”, “Message” — not just grey placeholder text that vanishes as soon as you start typing.'},
    'Ordinate titoli e focus': {'en': 'Put your headings and focus order in order'},
    'Una gerarchia di titoli coerente e un percorso navigabile da tastiera, con il focus sempre visibile, rendono la pagina usabile anche senza mouse.': {
        'en': 'A consistent heading hierarchy and a keyboard-navigable path, with focus always visible, make the page usable even without a mouse.'},
    'Non affidatevi solo al colore': {'en': 'Don’t rely on colour alone'},
    'Un errore segnalato solo in rosso è invisibile a chi non distingue i colori: affiancate sempre un’icona o un testo che spieghi cosa succede.': {
        'en': 'An error flagged only in red is invisible to someone who can’t distinguish colours: always pair it with an icon or text explaining what’s happening.'},
    'Vogliamo sistemarle noi: l’accessibilità è inclusa nei siti aziendali →': {
        'en': 'Want us to fix them for you? Accessibility is included in our business websites →'},
    'Cosa verifica davvero questo controllo di prontezza AI': {
        'en': 'What this AI-readiness check actually verifies'},
    'Come per il controllo GDPR, è il nostro server a leggere alcuni file pubblici del vostro sito e l’HTML della home, senza passare da Google. Facciamo quattro verifiche: cerchiamo il file llms.txt, controlliamo se il robots.txt lascia passare i crawler dei modelli (GPTBot di OpenAI, ClaudeBot, PerplexityBot, Google-Extended), rileviamo i dati strutturati JSON-LD nella pagina e la presenza di una sitemap. Ne esce un punteggio di prontezza su quattro.': {
        'en': 'As with the GDPR check, it’s our own server that reads a few public files from your site and the HTML of your home page, without going through Google. We run four checks: we look for the llms.txt file, check whether robots.txt lets the model crawlers through (OpenAI’s GPTBot, ClaudeBot, PerplexityBot, Google-Extended), detect JSON-LD structured data on the page, and check for a sitemap. The result is a readiness score out of four.'},
    'È utile sapere cosa il test non promette. Verifica che i segnali tecnici ci siano, non che ChatGPT o Perplexity vi citino davvero: quello dipende anche dalla qualità e dall’autorevolezza dei contenuti, che nessuno strumento misura in automatico. E poiché llms.txt è uno standard giovane, la sua assenza non è ancora un errore grave: è un’occasione in più di farsi leggere bene dalle macchine. Leggete il punteggio come una lista di opportunità, non come una bocciatura.': {
        'en': 'It’s worth knowing what this test doesn’t promise. It checks that the technical signals are there, not that ChatGPT or Perplexity will actually cite you: that also depends on the quality and authority of your content, which no tool measures automatically. And since llms.txt is a young standard, its absence isn’t yet a serious mistake: it’s one more opportunity to be read well by machines. Read the score as a list of opportunities, not as a failing grade.'},
    'Come leggere il punteggio di prontezza su 4': {
        'en': 'How to read your readiness score out of 4'},
    'Ogni segnale vale un punto e ha il suo semaforo. Quattro su quattro significa che il sito offre alle intelligenze artificiali tutti gli appigli per capirlo e citarlo. Due o tre su quattro è la situazione più comune: manca quasi sempre llms.txt, a volte i dati strutturati. Zero o uno su quattro merita attenzione, soprattutto se il robots.txt blocca i crawler AI: in quel caso restate fuori dalle risposte generate, magari senza averlo deciso.': {
        'en': 'Each signal is worth one point and has its own traffic light. Four out of four means your site gives AI models every handhold they need to understand and cite it. Two or three out of four is the most common situation: llms.txt is almost always the missing piece, sometimes structured data too. Zero or one out of four deserves attention, especially if robots.txt is blocking AI crawlers: in that case you’re left out of generated answers, possibly without having decided to be.'},
    'Una precisazione che evita allarmi inutili. Bloccare i crawler AI non è un difetto in sé: è una scelta legittima, se volete proteggere i contenuti. Il test lo segnala perché sappiate che quella porta è chiusa, non per dirvi che sbagliate. Per la maggior parte delle aziende, però, essere citati da un assistente AI è visibilità in più, non un rischio: vale la pena valutarlo con consapevolezza.': {
        'en': 'One clarification to avoid needless alarm. Blocking AI crawlers isn’t a flaw in itself: it’s a legitimate choice if you want to protect your content. The test flags it so you know that door is closed, not to tell you you’re wrong. For most businesses, though, being cited by an AI assistant is extra visibility, not a risk: it’s worth weighing with open eyes.'},
    'Come farsi trovare e citare dai modelli AI': {'en': 'How to get found and cited by AI models'},
    'Prepararsi all’AI non richiede stravolgimenti: sono gli stessi segnali che aiutano anche Google, più qualche novità.': {
        'en': 'Getting ready for AI doesn’t take an overhaul: it’s largely the same signals that help you with Google, plus a few new ones.'},
    'Pubblicate un file llms.txt': {'en': 'Publish an llms.txt file'},
    'Un semplice file di testo in Markdown, nella radice del sito, che riassume chi siete e cosa offrite: è la mappa che i modelli leggono volentieri.': {
        'en': 'A simple Markdown text file at the root of your site that sums up who you are and what you offer: it’s the map that models are happy to read.'},
    'Aprite le porte ai crawler giusti': {'en': 'Open the door to the right crawlers'},
    'Nel robots.txt consentite l’accesso a GPTBot, ClaudeBot, PerplexityBot e Google-Extended, se volete comparire nelle risposte generate.': {
        'en': 'In robots.txt, allow access to GPTBot, ClaudeBot, PerplexityBot and Google-Extended if you want to appear in generated answers.'},
    'Il markup JSON-LD schema.org dice in modo esplicito nome, sede, offerta e servizi: è la base che sia Google sia le AI usano per capirvi.': {
        'en': 'JSON-LD schema.org markup states your name, location, offer and services explicitly: it’s the foundation both Google and AI models use to understand you.'},
    'Tenete la sitemap aggiornata': {'en': 'Keep your sitemap up to date'},
    'Una sitemap XML completa aiuta i crawler a trovare tutte le pagine; assicuratevi che i contenuti siano testo leggibile, non solo immagini.': {
        'en': 'A complete XML sitemap helps crawlers find every page; make sure your content is readable text, not just images.'},
    'Scrivete fatti espliciti': {'en': 'State facts explicitly'},
    'Dichiarate con chiarezza cosa fate, dove e per chi: i modelli citano ciò che capiscono senza ambiguità, non ciò che devono indovinare.': {
        'en': 'State clearly what you do, where, and for whom: models cite what they understand unambiguously, not what they have to guess at.'},
    'Lo prepariamo noi: fa parte della SEO tecnica →': {
        'en': 'We’ll prepare it for you: it’s part of our technical SEO service →'},
    'Come stimiamo davvero le emissioni della pagina': {
        'en': 'How we actually estimate your website’s carbon emissions'},
    'Il calcolo parte da un dato concreto e misurabile: con l’API PageSpeed pesiamo tutti i byte che il browser deve scaricare per mostrare la vostra pagina. Su quel peso applichiamo il modello Sustainable Web Design della Green Web Foundation — le stesse formule della libreria open source co2.js — che traduce i byte trasferiti in energia consumata lungo la catena (data center, rete, dispositivo) e infine in grammi di CO₂ equivalente per visita.': {
        'en': 'The calculation starts from a concrete, measurable figure: with the PageSpeed API we weigh every byte the browser has to download to show your page. On that weight we apply the Green Web Foundation’s Sustainable Web Design model — the same formulas as the open-source co2.js library — which translates transferred bytes into energy consumed along the chain (data centre, network, device) and finally into grams of CO₂ equivalent per visit.'},
    'È una stima, ed è giusto trattarla come tale. Il modello usa coefficienti medi mondiali per l’intensità energetica e per il mix elettrico: non conosce l’energia reale del vostro hosting né il comportamento esatto di ogni visitatore. Non è una misura certificata di impronta ambientale, ma un ordine di grandezza affidabile e confrontabile. Il pregio è che si lega a un fatto tecnico — il peso — su cui potete davvero intervenire.': {
        'en': 'It’s an estimate, and it’s only fair to treat it as one. The model uses global average coefficients for energy intensity and the electricity mix: it doesn’t know the real energy source of your hosting or the exact behaviour of each visitor. It isn’t a certified measurement of environmental footprint, but a reliable, comparable order of magnitude. Its strength is that it ties back to a technical fact — page weight — that you can genuinely act on.'},
    'Come leggere i grammi di CO₂ per visita': {
        'en': 'How to read your website’s CO₂ grams per visit'},
    'Il numero chiave è la CO₂ equivalente per singola visita, che confrontiamo con la media del web, intorno agli 0,8 grammi. Sotto quella soglia siete tra i siti leggeri; sensibilmente sopra, la pagina è più pesante della media e c’è margine per alleggerirla. La stima annua moltiplica quel valore per un traffico di riferimento: cambiando le visite reali del vostro sito, l’impatto cresce o cala in proporzione.': {
        'en': 'The key number is the CO₂ equivalent per single visit, which we compare against the web average, around 0.8 grams. Below that threshold you’re among the lighter sites; noticeably above it, your page is heavier than average and there’s room to lighten it. The annual estimate multiplies that value by a reference traffic figure: change it to your site’s real visits, and the impact grows or shrinks proportionally.'},
    'Il confronto conta più del valore assoluto. Pochi grammi per visita sembrano nulla, ma moltiplicati per decine di migliaia di visite al mese diventano una cifra concreta, e soprattutto sono lo specchio di una pagina pesante: quasi sempre chi inquina di più è anche chi carica più lentamente. Leggete quindi l’impatto come un secondo indicatore delle prestazioni, non solo come una questione ambientale.': {
        'en': 'The comparison matters more than the absolute value. A few grams per visit look like nothing, but multiplied by tens of thousands of visits a month they become a real figure — and above all, they mirror a heavy page: the sites that pollute more are almost always the ones that load more slowly, too. So read the impact as a second performance indicator, not only as an environmental issue.'},
    'Come ridurre l’impronta di carbonio del sito': {
        'en': 'How to reduce your website’s carbon footprint'},
    'Ridurre le emissioni e velocizzare il sito sono la stessa cosa: entrambe passano dal tagliare peso inutile.': {
        'en': 'Cutting emissions and speeding up your site are the same job: both come down to trimming unnecessary weight.'},
    'Le fotografie sono quasi sempre la voce più pesante: convertitele in WebP o AVIF con caricamento differito e taglierete gran parte dei byte, e quindi delle emissioni.': {
        'en': 'Photos are almost always the heaviest line item: convert them to WebP or AVIF with lazy loading, and you’ll cut most of the bytes — and the emissions — right there.'},
    'Riducete script e font': {'en': 'Cut down scripts and fonts'},
    'Ogni libreria di terze parti e ogni famiglia di caratteri in più è energia trasferita a ogni visita: tenete solo ciò che serve davvero.': {
        'en': 'Every extra third-party library and every additional typeface is energy transferred on every visit: keep only what you truly need.'},
    'Sfruttate cache e CDN': {'en': 'Make the most of caching and a CDN'},
    'Una buona cache e una rete di distribuzione evitano di trasferire gli stessi contenuti mille volte: meno traffico ripetuto, meno consumo.': {
        'en': 'Good caching and a content delivery network avoid transferring the same content a thousand times over: less repeated traffic, less consumption.'},
    'Scegliete un hosting verde': {'en': 'Choose green hosting'},
    'Un provider alimentato da energia rinnovabile abbassa l’intensità di carbonio di ogni byte servito: è la leva più semplice per un effetto immediato.': {
        'en': 'A provider running on renewable energy lowers the carbon intensity of every byte served: it’s the simplest lever for an immediate effect.'},
    'Preferite un design sobrio': {'en': 'Favour a sober design'},
    'Niente video in riproduzione automatica o animazioni pesanti dove non servono: un’estetica pulita consuma meno e, spesso, comunica meglio.': {
        'en': 'No autoplaying video or heavy animation where it isn’t needed: a clean aesthetic consumes less and, often, communicates better.'},
    'Vogliamo alleggerirlo noi: scopri il restyling tecnico →': {
        'en': 'Want us to lighten it for you? See our technical redesign service →'},
    'Approfondisci: le 7 cause di un sito lento →': {
        'en': 'Read more: the 7 causes of a slow website →'},
}
CHROME.update(CHROME_TOOLS_L2)

# Full-site check-up (M4, docs/piano-checkup-sito.md): copy editoriale EN
# della pagina /en/tools/full-site-checkup/ e della card in evidenza su
# en-strumenti-index.php. Fonte: docs/copy-checkup.md §3.2/§3.3. Solo 'en' —
# il RU è scritto a mano nella pagina ru-strumento-check-up-completo.php.
CHROME_CHECKUP = {
    # ---- eyebrow / hero / intro ----
    'Check-up completo · gratuito': {'en': 'Full check-up · free'},
    'Il check-up completo del vostro sito web': {'en': 'The complete check-up for your website'},
    'Sette strumenti gratuiti in una sola analisi. Incollate l’indirizzo: in meno di un minuto vedete un punteggio di salute da 0 a 100, i sette semafori che lo compongono e i tre interventi più urgenti. La misura è quella vera di Google PageSpeed Insights, affiancata dalle nostre verifiche su privacy e prontezza AI. Il report completo, pagina per pagina, ve lo inviamo in PDF.': {
        'en': 'Seven free tools in a single analysis. Paste your address: in under a minute you get a 0–100 health score, the seven traffic lights behind it and the three most urgent fixes. The measurement is the real one from Google PageSpeed Insights, alongside our own privacy and AI-readiness checks. The full report, page by page, we send you as a PDF.'},

    # ---- widget: form / stati ----
    'Analizza il sito — gratis': {'en': 'Analyse the site — free'},
    'Analisi in corso su sette fronti — può richiedere fino a 30 secondi': {
        'en': 'Analysis in progress on seven fronts — this can take up to 30 seconds'},
    'Check-up incompleto': {'en': 'Check-up incomplete'},
    'Riprovate tra qualche minuto: alcune misure non hanno risposto (il servizio Google potrebbe essere saturo, oppure il sito ha rifiutato la lettura).': {
        'en': 'Try again in a few minutes: some measures didn’t respond (Google’s service may be overloaded, or the website refused the reading).'},
    'Riprova': {'en': 'Retry'},

    # ---- composito ----
    'Salute del sito': {'en': 'Site health'},
    'Media pesata di 7 misure. Prestazioni, SEO, accessibilità e best practice arrivano da Google PageSpeed Insights; privacy, prontezza AI e impatto CO₂ dalle verifiche di Studio Remarka.': {
        'en': 'Weighted average of 7 measures. Performance, SEO, accessibility and best practices from Google PageSpeed; privacy, AI and CO₂ from Studio Remarka checks.'},

    # ---- le sette dimensioni ----
    'Le sette misure': {'en': 'The seven measures'},
    'Sette semafori, un punteggio': {'en': 'Seven traffic lights, one score'},
    'Prestazioni': {'en': 'Performance'},
    'Accessibilità': {'en': 'Accessibility'},
    'Peso 25': {'en': 'Weight 25'},
    'Peso 20': {'en': 'Weight 20'},
    'Peso 15': {'en': 'Weight 15'},
    'Peso 10': {'en': 'Weight 10'},
    'Peso 5': {'en': 'Weight 5'},
    'Privacy e cookie': {'en': 'Privacy & cookies'},
    'Verifica indicativa · non legale': {'en': 'Indicative check · not legal advice'},
    'Best practice': {'en': 'Best practices'},
    'Pronto per l’AI': {'en': 'AI-readiness'},
    '4 segnali tecnici': {'en': '4 technical signals'},
    'Modello SWD': {'en': 'SWD model'},

    # ---- verdetti per dimensione (data-verdict-0..3) ----
    'Il sito è rapido su mobile: rispetta gli standard Google.': {'en': 'Fast on mobile: meets Google’s standards.'},
    'Velocità buona; restano margini misurabili su qualche pagina.': {'en': 'Good speed; measurable room on some pages.'},
    'Nella media del web, ma lontano dagli standard consigliati.': {'en': 'Average for the web, but far from the recommended standards.'},
    'Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.': {
        'en': 'Slow on mobile: most visitors leave before it loads.'},
    'Basi tecniche on-page in ordine: nessun ostacolo all’indicizzazione.': {'en': 'On-page foundations in order: no barrier to indexing.'},
    'Struttura solida; poche correzioni per completare le basi.': {'en': 'Solid structure; a few fixes to finish the basics.'},
    'Alcuni elementi on-page mancano o sono duplicati.': {'en': 'Some on-page elements are missing or duplicated.'},
    'Qualcosa ostacola l’indicizzazione: da sistemare prima di tutto.': {'en': 'Something blocks indexing: fix this first.'},
    'Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA.': {'en': 'Few or no barriers: usable under WCAG 2.1 AA.'},
    'Buon livello; restano barriere minori da rimuovere.': {'en': 'Good level; minor barriers left to remove.'},
    'Diverse barriere rilevate: contrasti, etichette, navigazione.': {'en': 'Several barriers found: contrast, labels, navigation.'},
    'Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).': {
        'en': 'Serious barriers: hard to use for many people (EAA obligation).'},
    'Banner, informative e tracker in ordine nell’HTML iniziale.': {'en': 'Banner, policies and trackers in order in the initial HTML.'},
    'Impianto presente; un paio di punti da verificare a mano.': {'en': 'Framework in place; a couple of points to check by hand.'},
    'Mancano elementi o alcuni tracker vanno governati meglio.': {'en': 'Elements missing or some trackers poorly governed.'},
    'Tracker attivi senza banner o policy assenti: rischio concreto col Garante.': {
        'en': 'Trackers active without a banner, or policies missing: real regulatory risk.'},
    'Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate.': {
        'en': 'Technically clean: HTTPS, no console errors, up-to-date libraries.'},
    'Buon livello tecnico; qualche avviso da chiudere.': {'en': 'Good technical level; a few warnings to close.'},
    'Diversi avvisi tecnici: sicurezza, errori console, immagini.': {'en': 'Several technical warnings: security, console errors, images.'},
    'Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.': {
        'en': 'Widespread technical issues weakening reliability and security.'},
    '4 segnali su 4: il sito è leggibile e citabile dai modelli AI.': {'en': '4 of 4 signals: readable and citable by AI models.'},
    '3 segnali su 4: manca poco alla piena prontezza AI.': {'en': '3 of 4 signals: nearly fully AI-ready.'},
    '2 segnali su 4: dati strutturati o sitemap da completare.': {'en': '2 of 4 signals: structured data or sitemap to complete.'},
    '0–1 segnali: i modelli AI faticano a leggere e citare il sito.': {'en': '0–1 signals: AI models struggle to read and cite the site.'},
    'Pagina leggera: emissioni sotto la media del web.': {'en': 'Light page: emissions below the web average.'},
    'Vicino alla media; c’è margine per alleggerire.': {'en': 'Near the average; room to slim down.'},
    'Sopra la media: la pagina è pesante da caricare.': {'en': 'Above average: the page is heavy to load.'},
    'Molto sopra la media: pagina pesante, costo ambientale e di velocità.': {
        'en': 'Well above average: heavy page, an environmental and speed cost.'},

    # ---- parole di verdetto e composito (data-word-*/data-composite-*) ----
    'Eccellente': {'en': 'Excellent'},
    'Buono': {'en': 'Good'},
    'Da migliorare': {'en': 'Needs work'},
    'Critico': {'en': 'Critical'},
    'Sito in salute eccellente': {'en': 'Excellent site health'},
    'Sito in buona salute': {'en': 'Good site health'},
    'Sito da migliorare': {'en': 'Site needs work'},
    'Sito a rischio': {'en': 'Site at risk'},
    '— analisi mobile': {'en': '— mobile analysis'},
    ' / 4 segnali': {'en': ' / 4 signals'},
    'Calcolato su {n} misurazioni su 7.': {'en': 'Calculated on {n} of 7 measurements.'},
    'Non siamo riusciti a misurare questo aspetto: il sito ha rifiutato la lettura o il servizio Google era saturo.': {
        'en': 'We couldn’t measure this aspect: the website refused automated reading, or Google’s service was overloaded.'},
    'Non siamo riusciti a completare il check-up. Riprovate tra qualche minuto.': {
        'en': 'We couldn’t complete the check-up. Please try again in a few minutes.'},

    # ---- priorità ----
    'Le priorità': {'en': 'Priorities'},
    'I 3 interventi che pesano di più': {'en': 'The 3 fixes that matter most'},
    'Ordinati per impatto sul punteggio: quanto guadagnereste sistemandoli.': {
        'en': 'Ranked by impact on your score: how much you’d gain by fixing them.'},

    # ---- form e-mail / report PDF ----
    'Report completo': {'en': 'Full report'},
    'Il report completo, in PDF': {'en': 'The full report, as a PDF'},
    'Vi inviamo l’analisi integrale: una pagina per ognuna delle sette dimensioni, tutte le criticità rilevate e le raccomandazioni in ordine di impatto.': {
        'en': 'We send you the complete analysis: one page per dimension, every issue found and the fixes ranked by impact.'},
    'Il punteggio di salute con i sette semafori': {'en': 'The health score with the seven traffic lights'},
    'Una pagina per dimensione: punteggio, cosa abbiamo trovato, cosa fare': {
        'en': 'A page per dimension: score, what we found, what to do'},
    'I tre interventi prioritari con le contromisure': {'en': 'The three priority fixes with countermeasures'},
    '«Cosa faremmo noi» e i riferimenti di Studio Remarka': {'en': '«What we would do» and Studio Remarka’s details'},
    'Sito web': {'en': 'Website'},
    'Inviatemi il report PDF': {'en': 'Send me the PDF report'},
    'Ho letto la': {'en': 'I have read the'},
    'e acconsento all’invio del report e a essere ricontattato.': {'en': 'and consent to receiving the report and being contacted.'},
    'Inviatemi ogni mese il monitoraggio dei Core Web Vitals di questo sito.': {
        'en': 'Send me the monthly Core Web Vitals monitoring for this site.'},
    'Fatto. Il report è in viaggio verso la vostra casella: se non arriva entro qualche minuto, controllate lo spam o scriveteci.': {
        'en': 'Done. The report is on its way to your inbox: if it doesn’t arrive within a few minutes, check spam or drop us a line.'},
    'Non siamo riusciti a inviare il report. Riprovate tra poco o scriveteci: ve lo mandiamo a mano.': {
        'en': 'We couldn’t send the report. Try again shortly, or write to us and we’ll send it by hand.'},
    'Niente spam. Usiamo l’indirizzo solo per il report ed eventuale ricontatto. Studio Remarka S.r.l., P.IVA GE 302230994.': {
        'en': 'No spam. We use your address only for the report and possible follow-up. Studio Remarka S.r.l., VAT GE 302230994.'},
    'nome@vostraazienda.it': {'en': 'name@yourcompany.com'},

    # ---- come funziona (3 passi) ----
    'La home o la pagina che porta più visite. Nessuna registrazione, nessun dato di pagamento.': {
        'en': 'Your home page or the page that brings the most traffic. No sign-up, no payment details.'},
    'Analizziamo su sette fronti': {'en': 'We analyse on seven fronts'},
    'Un’unica interrogazione all’API Google PageSpeed (prestazioni, SEO, accessibilità, best practice) più le nostre verifiche su privacy/cookie e prontezza AI, letti dal nostro server come farebbe un visitatore.': {
        'en': 'A single Google PageSpeed API call (performance, SEO, accessibility, best practices) plus our own privacy/cookie and AI-readiness checks, read from our server the way a visitor would see the page.'},
    'Leggete il punteggio e le priorità': {'en': 'Read the score and priorities'},
    'Salute 0–100, i sette semafori spiegati in italiano e i tre interventi che pesano di più. Il report completo arriva in PDF.': {
        'en': 'Health 0–100, the seven traffic lights in plain English and the three fixes that matter most. The full report follows as a PDF.'},

    # ---- il metodo ----
    'Che cosa misura davvero il check-up completo': {'en': 'What the full check-up actually measures'},
    'Dietro il punteggio non c’è una scatola nera. Quattro delle sette dimensioni — prestazioni, SEO, accessibilità e best practice — arrivano dall’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev: interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Le altre tre le calcoliamo noi: la conformità privacy la leggiamo dall’HTML della pagina (banner, informative, tracker prima del consenso), la prontezza AI da quattro segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e l’impronta di CO₂ dal peso reale della pagina, con il modello Sustainable Web Design.': {
        'en': 'There’s no black box behind the score. Four of the seven dimensions — performance, SEO, accessibility and best practices — come from Google’s PageSpeed Insights API, the same engine behind pagespeed.web.dev: we query Lighthouse in mobile strategy, because that’s the version Google uses to rank you. The other three we compute ourselves: privacy compliance we read from the page’s HTML (banner, policies, trackers before consent), AI-readiness from four technical signals — llms.txt, crawler access, structured data, sitemap — and the CO₂ footprint from the page’s real weight, using the Sustainable Web Design model.'},
    'Ogni dimensione entra nel voto con un peso dichiarato: le prestazioni valgono di più (25 su 100), la CO₂ di meno (5). È giusto sapere anche cosa il check-up non fa: non è un parere legale sulla privacy — è una verifica indicativa a quattro segnali — e non promette una posizione su Google. È la fotografia tecnica precisa del vostro sito, non una promessa di vendita.': {
        'en': 'Each dimension enters the score with a stated weight: performance counts most (25 of 100), CO₂ least (5). It’s fair to know what the check-up does not do: it’s not a legal opinion on privacy — it’s an indicative, four-signal check — and it never promises a Google ranking. It’s a precise technical snapshot of your site, not a sales promise.'},

    # ---- come leggere il risultato ----
    'Come si legge lo stato di salute del sito': {'en': 'How to read your site’s health score'},
    'Il punteggio di salute è la media pesata dei sette semafori, non un voto a sensazione. Si legge come un semaforo: da 90 in su siete in fascia verde (eccellente), da 75 a 89 è buono, tra 50 e 74 c’è margine concreto, sotto 50 è critico e diventa la priorità. Ogni dimensione porta lo stesso codice colore, così capite in un colpo d’occhio dove il sito è solido e dove perde punti.': {
        'en': 'The health score is the weighted average of the seven traffic lights, not a gut-feel grade. Read it like a traffic light: 90 and up is green (excellent), 75–89 is good, 50–74 leaves real room, below 50 is critical and becomes the priority. Every dimension carries the same colour code, so you see at a glance where the site is solid and where it loses points.'},
    'Due letture da evitare. Un voto alto non significa «primi su Google»: significa che le fondamenta tecniche sono sane. E se una misura risulta «N/D» non è un guasto del vostro sito: a volte Google è saturo, a volte il sito rifiuta la lettura automatica. In quel caso calcoliamo la salute sulle misure riuscite e ve lo diciamo con chiarezza.': {
        'en': 'Two readings to avoid. A high score doesn’t mean «number one on Google»: it means the technical foundations are sound. And if a measure shows «N/A» it’s not your site failing: sometimes Google is overloaded, sometimes a site refuses automated reading. In that case we compute health on the successful measures and tell you so clearly.'},

    # ---- FAQ ----
    'Per prestazioni, SEO, accessibilità e best practice sì: arrivano dall’API ufficiale PageSpeed Insights, strategia mobile. Privacy, prontezza AI e CO₂ sono nostre verifiche, con il metodo dichiarato in ogni sezione.': {
        'en': 'For performance, SEO, accessibility and best practices, yes — it comes from the official PageSpeed Insights API, mobile strategy. Privacy, AI-readiness and CO₂ are our own checks, with the method stated in each section.'},
    'Il check-up GDPR sostituisce un consulente privacy?': {'en': 'Does the GDPR check replace a privacy consultant?'},
    'No. È una verifica tecnica indicativa a quattro segnali: intercetta i problemi evidenti — banner assente, tracker prima del consenso — ma non è un parere legale e non sostituisce un consulente.': {
        'en': 'No. It’s an indicative, four-signal technical check: it catches the obvious problems — missing banner, trackers before consent — but it’s not a legal opinion and doesn’t replace a consultant.'},
    'Cosa ricevo nel report PDF che non vedo già a schermo?': {'en': 'What’s in the PDF that I don’t already see on screen?'},
    'A schermo vedete il punteggio, i sette semafori e le tre priorità. Nel PDF trovate una pagina per dimensione con tutte le criticità rilevate, le raccomandazioni operative in ordine di impatto e cosa faremmo noi, con i nostri riferimenti aziendali.': {
        'en': 'On screen you see the score, the seven traffic lights and the three priorities. The PDF gives you a page per dimension with every issue found, the fixes ranked by impact, and what we would do, with our company details.'},

    # ---- CTA finale ----
    'Vogliamo sistemare noi le priorità': {'en': 'Want us to fix the priorities'},
    'Dal punteggio al preventivo: analizziamo il report insieme e vi diamo un piano d’intervento a prezzo chiuso, con PageSpeed 90+ garantito da contratto.': {
        'en': 'From score to quote: we review the report together and hand you a fixed-price action plan, with PageSpeed 90+ guaranteed by contract.'},
    'Richiedi la consulenza — gratis': {'en': 'Book a free consultation'},
    'Vedi tutti gli strumenti': {'en': 'See all tools'},

    # ---- strumenti-index: card in evidenza ----
    'Novità · gratuito': {'en': 'New · free'},
    'Check-up completo': {'en': 'Full check-up'},
    'Sette strumenti gratuiti in una sola analisi.': {'en': 'Seven free tools in a single analysis.'},
}
CHROME.update(CHROME_CHECKUP)

# ---- Servizio «Adeguamento EAA» (docs/copy-eaa.md §4, EN madrelingua) ----
# CHROME_EAA copre servizio-adeguamento-eaa.php, la card premium in
# servizi-index.php, la nota in prezzi.php e le due stringhe di CTA
# aggiornate in strumento-verifica-accessibilita.php (data.py TOOLS).
CHROME_EAA = {
    'Servizio / Adeguamento EAA': {'en': 'Service / EAA compliance'},
    'Il sito conforme all’European Accessibility Act, in 3 settimane': {
        'en': 'Your website compliant with the European Accessibility Act, in 3 weeks'},
    'Dal 28 giugno 2025 l’accessibilità è un obbligo di legge per molti siti. Vi portiamo allo standard WCAG 2.1 AA — audit, correzioni e dichiarazione di accessibilità — a prezzo chiuso e con la data nel contratto.': {
        'en': 'Since 28 June 2025 accessibility is a legal requirement for many websites. We bring yours up to the WCAG 2.1 AA standard — audit, fixes and accessibility statement — at a fixed price, with the date in the contract.'},
    'Data da cui l’European Accessibility Act è in vigore in Italia. Le prime sanzioni sono una questione di tempo.': {
        'en': 'The date the European Accessibility Act took effect in Italy. The first fines are only a matter of time.'},
    'Richiedi l’audit di accessibilità': {'en': 'Request the accessibility audit'},
    'Verifica subito il tuo sito': {'en': 'Check your site now'},
    'L’obbligo riguarda chi vende a consumatori, online': {'en': 'The duty applies to those who sell to consumers, online'},
    'E-commerce e servizi digitali che vendono beni o servizi ai consumatori nell’Unione Europea.': {
        'en': 'E-commerce and digital services selling goods or services to consumers in the EU.'},
    'Banche, assicurazioni, trasporti, biglietterie e sistemi di prenotazione online.': {
        'en': 'Banks, insurers, transport, ticketing and online booking systems.'},
    'Aziende non microimpresa che temono la prima sanzione italiana, o che l’hanno già ricevuta come segnalazione.': {
        'en': 'Non-micro companies facing the first Italian fines, or already flagged for non-compliance.'},
    'Dall’audit alla dichiarazione, tutto scritto nel preventivo': {'en': 'From audit to statement, all spelled out in the quote'},
    'Audit completo: test automatico (Lighthouse) più verifica manuale — tastiera, screen reader, contenuti.': {
        'en': 'Full audit: automated test (Lighthouse) plus manual review — keyboard, screen reader, content.'},
    'Correzione di tema, contrasti, etichette dei moduli e struttura dei titoli.': {
        'en': 'Fixes to theme, contrast, form labels and heading structure.'},
    'Navigazione da tastiera e focus sempre visibile su ogni elemento interattivo.': {
        'en': 'Keyboard navigation and a visible focus state on every interactive element.'},
    'Dichiarazione di accessibilità pubblicata, il documento che la norma richiede.': {
        'en': 'A published accessibility statement, the document the law requires.'},
    'Audit di verifica finale secondo lo standard WCAG 2.1 AA, a correzioni fatte.': {
        'en': 'A final verification audit against the WCAG 2.1 AA standard, once fixes are done.'},
    'Prezzo chiuso dopo l’audit, consegna in 3 settimane con penale in contratto.': {
        'en': 'Fixed price after the audit, delivery in 3 weeks with a contractual penalty.'},
    'Tre settimane, dalla diagnosi alla conformità': {'en': 'Three weeks, from diagnosis to compliance'},
    'Settimana 1': {'en': 'Week 1'},
    'Settimana 2': {'en': 'Week 2'},
    'Settimana 3': {'en': 'Week 3'},
    'Audit': {'en': 'Audit'},
    'Correzioni': {'en': 'Fixes'},
    'Dichiarazione e verifica': {'en': 'Statement and verification'},
    'Partiamo dal test automatico gratuito, poi la verifica manuale: tastiera, screen reader, contrasti, contenuti. A fine audit il prezzo è chiuso e la data è fissata.': {
        'en': 'We start from the free automated test, then the manual review: keyboard, screen reader, contrast, content. By the end of the audit the price is fixed and the date is set.'},
    'Sistemiamo tema, contrasti, etichette dei moduli, gerarchia dei titoli e navigazione da tastiera. Ogni barriera dell’elenco, una per una.': {
        'en': 'We correct theme, contrast, form labels, heading hierarchy and keyboard navigation. Every barrier on the list, one by one.'},
    'Pubblichiamo la dichiarazione di accessibilità obbligatoria e ripetiamo l’audit per confermare la conformità WCAG 2.1 AA.': {
        'en': 'We publish the required accessibility statement and re-run the audit to confirm WCAG 2.1 AA compliance.'},
    'Tempi indicativi per un sito aziendale o vetrina. Un e-commerce con catalogo ampio può richiedere più tempo: lo scriviamo nel preventivo, con la stessa penale.': {
        'en': 'Indicative timing for a business or brochure site. A large-catalogue e-commerce may take longer: we write it in the quote, with the same penalty.'},
    'Prezzo chiuso, dopo l’audit': {'en': 'A fixed price, after the audit'},
    'da € 1.900': {'en': 'from € 1,900'},
    'Prezzo chiuso nel preventivo dopo l’audit, da € 1.900. Consegna in 3 settimane, data fissa in contratto. Fattura elettronica, pagamento in tre tranche.': {
        'en': 'Fixed price locked in the quote after the audit, from € 1,900. Delivery in 3 weeks, date fixed in the contract. E-invoicing, payment in three installments.'},
    'Non sai da dove partire? L’audit automatico è gratuito →': {'en': 'Not sure where to start? The automated audit is free →'},
    'Numero di pagine e modelli (template) da correggere: una vetrina costa meno di un e-commerce a catalogo.': {
        'en': 'Number of pages and templates to fix: a brochure site costs less than a catalogue e-commerce.'},
    'Stato di partenza: quante barriere emergono dall’audit iniziale.': {
        'en': 'Starting point: how many barriers the initial audit reveals.'},
    'Contenuti da rifare — testi alternativi, PDF accessibili, sottotitoli ai video.': {
        'en': 'Content to redo — alt text, accessible PDFs, video captions.'},
    'Nero su bianco, come per ogni nostro servizio': {'en': 'In writing, like every service we deliver'},
    '± 0 giorni di ritardo — la data è nel contratto: ogni giorno lavorativo di ritardo vale l’1% di sconto.': {
        'en': '± 0 days late — the date is in the contract: every working day of delay is 1% off.'},
    'Prezzo chiuso dopo l’audit — quello che firmate è quello che pagate; ogni extra si concorda per iscritto prima.': {
        'en': 'Fixed price after the audit — what you sign is what you pay; any extra is agreed in writing first.'},
    'Standard dichiarato — conformità WCAG 2.1 AA verificata a mano, non solo un punteggio automatico.': {
        'en': 'A declared standard — WCAG 2.1 AA compliance verified by hand, not just an automated score.'},
    'Dichiarazione di accessibilità inclusa — il documento richiesto dalla norma, pubblicato sul vostro sito.': {
        'en': 'Accessibility statement included — the document the law requires, published on your site.'},
    'Domande frequenti': {'en': 'Frequently asked questions'},
    'Chi è obbligato dall’EAA? La mia azienda rientra?': {'en': 'Who is required to comply with the EAA? Does my company qualify?'},
    'L’European Accessibility Act è in vigore in Italia dal 28 giugno 2025 e obbliga molti siti che vendono beni o servizi ai consumatori: e-commerce, banche, trasporti, servizi digitali. Sono esentate le microimprese che erogano servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato annuo. Nel dubbio verifichiamo il vostro caso prima di firmare: se non siete obbligati, ve lo diciamo.': {
        'en': 'The European Accessibility Act took effect in Italy on 28 June 2025 and covers many sites selling goods or services to consumers: e-commerce, banks, transport, digital services. Micro-enterprises providing services are exempt — fewer than 10 people and under € 2 million in annual turnover. If in doubt we check your case before signing: if you’re not required to comply, we tell you.'},
    'Quali sanzioni sono previste in Italia?': {'en': 'What fines apply in Italy?'},
    'Il decreto italiano prevede sanzioni fino al 5% del fatturato per i servizi non conformi. In Francia sono già partite le prime cause verso i grandi rivenditori online, e in Italia l’applicazione è appena cominciata. Le fonti sono pubbliche: la guida di Bird & Bird e il centro AccessibleEU della Commissione europea (link in fondo alla pagina).': {
        'en': 'The Italian decree sets fines of up to 5% of turnover for non-compliant services. In France the first lawsuits against large online retailers have already begun, and enforcement in Italy has just started. The sources are public: the Bird & Bird guide and the European Commission’s AccessibleEU centre (links at the bottom of the page).'},
    'Cos’è la dichiarazione di accessibilità?': {'en': 'What is an accessibility statement?'},
    'È un documento pubblico, richiesto dalla norma, in cui il sito dichiara il proprio livello di conformità, le eventuali parti non ancora accessibili e un contatto per segnalare problemi. Lo redigiamo e lo pubblichiamo noi, come parte del servizio: senza dichiarazione, il sito non è a norma anche se tecnicamente accessibile.': {
        'en': 'It’s a public document, required by the law, in which the site declares its level of compliance, any parts not yet accessible, and a contact for reporting problems. We write and publish it as part of the service: without a statement a site isn’t compliant, even if technically accessible.'},
    'Basta un controllo automatico per essere conformi?': {'en': 'Is an automated check enough to be compliant?'},
    'No, ed è giusto dirlo chiaro. Un test automatico come il nostro strumento gratuito intercetta circa un terzo dei criteri WCAG: quello che una macchina sa misurare. Il resto — navigazione da tastiera, esperienza con screen reader, chiarezza dei contenuti — si verifica solo a mano. Per questo l’audit manuale è il cuore del servizio, non un optional.': {
        'en': 'No, and it’s fair to say so plainly. An automated test like our free tool catches roughly a third of the WCAG criteria: what a machine can measure. The rest — keyboard navigation, screen-reader experience, content clarity — can only be checked by hand. That’s why the manual audit is the core of this service, not an add-on.'},
    'European Accessibility Act (dir. UE 2019/882), in vigore in Italia dal 28 giugno 2025.': {
        'en': 'European Accessibility Act (EU Directive 2019/882), in effect in Italy since 28 June 2025.'},
    'Sanzioni fino al 5% del fatturato per i servizi non conformi (recepimento italiano).': {
        'en': 'Fines up to 5% of turnover for non-compliant services (Italian transposition).'},
    'Standard di riferimento:': {'en': 'Reference standard:'},
    'WCAG 2.1 livello AA': {'en': 'WCAG 2.1 level AA'},
    'Bird & Bird — guida all’European Accessibility Act →': {'en': 'Bird & Bird — a guide to the European Accessibility Act →'},
    'AccessibleEU (Commissione europea) — l’EAA in vigore da giugno 2025 →': {
        'en': 'AccessibleEU (European Commission) — the EAA in effect since June 2025 →'},
    'Un controllo automatico copre parte dei criteri WCAG 2.1 AA. La conformità piena richiede la verifica manuale, che è inclusa in questo servizio.': {
        'en': 'An automated check covers part of the WCAG 2.1 AA criteria. Full compliance requires manual review, which is included in this service.'},
    'Facciamo il punto sul vostro sito': {'en': 'Let’s take stock of your website'},
    'L’audit iniziale trasforma l’obbligo in una lista di cose da fare, con prezzo chiuso e data di consegna. Il primo controllo automatico è gratuito e senza registrazione.': {
        'en': 'The initial audit turns the legal duty into a to-do list, with a fixed price and delivery date. The first automated check is free and needs no sign-up.'},
    'Prova lo strumento gratuito': {'en': 'Try the free tool'},

    # ---- premium card (servizi-index.php) ----
    'Obbligo di legge': {'en': 'Legal duty'},
    'Adeguamento EAA': {'en': 'EAA compliance'},
    'Il vostro sito già online, portato allo standard WCAG 2.1 AA: audit, correzioni e dichiarazione di accessibilità. Obbligo di legge dal 2025.': {
        'en': 'Your website, already online, brought up to the WCAG 2.1 AA standard: audit, fixes and accessibility statement. A legal duty since 2025.'},

    # ---- nota in prezzi.php ----
    'Sito già online? L’adeguamento all’European Accessibility Act è un servizio a sé →': {
        'en': 'Website already online? Bringing it up to European Accessibility Act standard is a separate service →'},

    # ---- CTA strumento-verifica-accessibilita.php (data.py TOOLS) ----
    'Vogliamo sistemarle noi: audit, correzioni e dichiarazione — servizio Adeguamento EAA →': {
        'en': 'Want us to fix them for you? Audit, fixes and statement — our EAA compliance service →'},
    'Scopri il servizio Adeguamento EAA': {'en': 'Discover the EAA compliance service'},
}
CHROME.update(CHROME_EAA)


CHROME_EEAT = {
    'Strumento gratuito /08': {'en': 'Free tool /08'},
    'Segnali E-E-A-T': {'en': 'E-E-A-T signals'},
    'Segnali E-E-A-T: quanto è credibile il vostro sito?': {'en': 'E-E-A-T signals: how credible does your site look?'},
    'Analizziamo otto segnali di fiducia leggibili nel codice della vostra home — HTTPS, contatti, P.IVA, chi siamo, dati strutturati e altri — raggruppati nei quattro pilastri E-E-A-T. Misuriamo i segnali on-page, non la vostra reputazione o competenza reale. Senza registrazione.': {'en': 'We analyse eight trust signals readable in your homepage code — HTTPS, contacts, VAT number, an about page, structured data and more — grouped into the four E-E-A-T pillars. We measure on-page signals, not your real reputation or expertise. No sign-up.'},
    'Otto segnali di fiducia on-page, raggruppati nei quattro pilastri E-E-A-T.': {'en': 'Eight on-page trust signals, grouped into the four E-E-A-T pillars.'},
    'Inserite l’indirizzo del sito': {'en': 'Enter the site address'},
    'Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura: analizziamo il codice HTML, non serve installare nulla.': {'en': 'We read the home page from our own server, the way a first-time visitor would: we analyse the HTML, nothing to install.'},
    'Otto controlli automatici': {'en': 'Eight automatic checks'},
    'Cerchiamo otto segnali di fiducia leggibili nella pagina — HTTPS, contatti, P.IVA, privacy, chi siamo, portfolio, dati strutturati, profili esterni — e li raggruppiamo nei quattro pilastri E-E-A-T.': {'en': 'We look for eight trust signals in the page — HTTPS, contacts, VAT, privacy, about page, portfolio, structured data, external profiles — and group them into the four E-E-A-T pillars.'},
    'Punteggio 0–100 e quattro assi': {'en': 'A 0–100 score and four pillars'},
    'Un punteggio complessivo e il dettaglio per Esperienza, Competenza, Autorevolezza e Affidabilità, con il colore di ogni segnale e cosa manca.': {'en': 'An overall score plus the breakdown by Experience, Expertise, Authoritativeness and Trust, with a colour for each signal and what’s missing.'},
    'Cos’è l’E-E-A-T?': {'en': 'What is E-E-A-T?'},
    'È un concetto delle linee guida di Google per i valutatori della qualità (Search Quality Rater Guidelines): Experience, Expertise, Authoritativeness, Trust — esperienza, competenza, autorevolezza e affidabilità. Aiuta Google a stimare quanto ci si può fidare di una pagina, soprattutto sui temi che incidono su salute, denaro e sicurezza.': {'en': 'It’s a concept from Google’s Search Quality Rater Guidelines: Experience, Expertise, Authoritativeness and Trust. It helps Google estimate how much a page can be trusted, especially on topics that affect health, money and safety.'},
    'L’E-E-A-T influenza il posizionamento?': {'en': 'Does E-E-A-T affect rankings?'},
    'Non è un fattore di ranking diretto né un punteggio che Google assegna: è una cornice di qualità che i valutatori umani usano per addestrare gli algoritmi. Rafforzare i segnali di fiducia aiuta indirettamente, ma nessuno strumento — nemmeno il nostro — misura l’E-E-A-T «reale» del vostro sito.': {'en': 'It’s not a direct ranking factor or a score Google assigns: it’s a quality framework human raters use to train the algorithms. Strengthening your trust signals helps indirectly, but no tool — ours included — measures your site’s “real” E-E-A-T.'},
    'Perché il test non vede la mia reputazione?': {'en': 'Why doesn’t the test see my reputation?'},
    'Perché leggiamo solo il codice della vostra pagina: possiamo verificare che i segnali di fiducia ci siano e siano dichiarati, non chi vi cita, che recensioni avete o quanto siete davvero esperti. Quella parte la giudicano le persone e il resto del web, non una scansione dell’HTML.': {'en': 'Because we only read your page’s code: we can confirm the trust signals are there and declared, not who cites you, what reviews you have or how expert you really are. That part is judged by people and the wider web, not by scanning HTML.'},
    'Cosa misura davvero questo test dei segnali E-E-A-T': {'en': 'What this E-E-A-T signal test actually measures'},
    'Come per il controllo GDPR e per quello di prontezza AI, è il nostro server a leggere la home page del vostro sito, senza passare da Google. Sul codice HTML cerchiamo otto segnali di fiducia che chiunque — un motore di ricerca, un modello AI, un cliente diffidente — userebbe per decidere se fidarsi: la connessione sicura (HTTPS), i contatti verificabili, l’identità legale (P.IVA e ragione sociale), i link a privacy e cookie policy, la pagina «Chi siamo», un portfolio o dei casi studio, i dati strutturati in JSON-LD e i profili esterni. Ogni segnale finisce in uno dei quattro pilastri E-E-A-T — Esperienza, Competenza, Autorevolezza, Affidabilità — e pesa sul punteggio complessivo.': {'en': 'As with the GDPR and AI-readiness checks, it’s our server that reads your home page, without going through Google. In the HTML we look for eight trust signals that anyone — a search engine, an AI model, a cautious customer — would use to decide whether to trust you: a secure connection (HTTPS), verifiable contacts, legal identity (VAT and company name), links to privacy and cookie policy, an about page, a portfolio or case studies, JSON-LD structured data, and external profiles. Each signal falls into one of the four E-E-A-T pillars — Experience, Expertise, Authoritativeness, Trust — and weighs on the overall score.'},
    'Ed ecco il confine, che diciamo subito: misuriamo segnali on-page verificabili nel codice, non l’E-E-A-T reale del vostro sito. Non contiamo i link o le menzioni che ricevete, non leggiamo le recensioni né la vostra reputazione, non giudichiamo se siete davvero esperti o se i contenuti dicono il vero: quella valutazione la fanno le persone — i quality rater di Google e il resto del web — non una scansione dell’HTML. Guardiamo solo la home indicata, non l’intero sito, e non vediamo ciò che compare soltanto dopo l’esecuzione del JavaScript. Un punteggio alto significa che i segnali di fiducia ci sono e sono leggibili, non che Google vi darà un giudizio E-E-A-T positivo.': {'en': 'And here’s the boundary, stated up front: we measure on-page signals readable in the code, not your site’s real E-E-A-T. We don’t count the links or mentions you receive, we don’t read reviews or reputation, we don’t judge whether you’re genuinely expert or whether the content is true: that call is made by people — Google’s quality raters and the wider web — not by scanning HTML. We look only at the home page you give us, not the whole site, and we don’t see anything that appears only after JavaScript runs. A high score means the trust signals are present and readable, not that Google will give you a positive E-E-A-T judgement.'},
    'Come leggere il punteggio E-E-A-T e i quattro assi': {'en': 'How to read the E-E-A-T score and the four pillars'},
    'Il punteggio va da 0 a 100 e si legge come un semaforo a quattro livelli. Da 90 in su i segnali di fiducia ci sono quasi tutti e si leggono senza sforzo. Tra 75 e 89 avete una buona base, con pochi elementi da completare. Tra 50 e 74 mancano diversi segnali importanti: è la fascia più comune per i siti aziendali italiani, che spesso curano i contenuti ma dimenticano la parte tecnica. Sotto 50 la pagina espone pochi appigli di fiducia — ed è anche la situazione in cui bastano poche aggiunte per salire in fretta. Accanto al totale trovate i quattro assi, così vedete su quale pilastro conviene intervenire prima.': {'en': 'The score runs from 0 to 100 and reads like a four-level traffic light. From 90 up, almost all trust signals are there and easy to read. Between 75 and 89 you have a solid base, with a few items to complete. Between 50 and 74 several important signals are missing: this is the most common band for business sites that look after content but forget the technical side. Below 50 the page exposes few trust cues — which is also the situation where a handful of additions lift you quickly. Next to the total you’ll find the four pillars, so you can see which one to fix first.'},
    'Due letture da evitare. La prima: un segnale in rosso non è una colpa, ma un’occasione — «nessun dato strutturato» vuol dire che, aggiungendo un blocco JSON-LD, guadagnate punti in un pomeriggio. La seconda, più importante: un 100 pieno non certifica il vostro E-E-A-T. Significa che avete dichiarato bene chi siete, non che il web vi considera autorevoli — quella fiducia si costruisce con contenuti, tempo e reputazione, che nessuno strumento legge dall’HTML. E se il punteggio vi sembra ingiustamente basso, controllate se il sito rende i contenuti via JavaScript: in quel caso molti segnali esistono ma non sono nel codice iniziale che leggiamo, e ve lo segnaliamo con un avviso.': {'en': 'Two readings to avoid. First: a red signal isn’t a fault, it’s an opportunity — “no structured data” means that by adding a JSON-LD block you gain points in an afternoon. Second, and more important: a perfect 100 doesn’t certify your E-E-A-T. It means you’ve declared who you are well, not that the web considers you authoritative — that trust is built with content, time and reputation, which no tool reads from HTML. And if the score seems unfairly low, check whether the site renders its content via JavaScript: in that case many signals exist but aren’t in the initial code we read, and we flag it with a notice.'},
    'Come rafforzare i segnali E-E-A-T del sito': {'en': 'How to strengthen your site’s E-E-A-T signals'},
    'Rafforzare la fiducia non richiede riscrivere il sito: sono aggiunte tecniche precise, quasi tutte veloci e a basso costo.': {'en': 'Strengthening trust doesn’t mean rewriting the site: these are precise technical additions, most of them quick and low-cost.'},
    'Pubblicate una pagina «Chi siamo» vera': {'en': 'Publish a real about page'},
    'Con nomi, volti, storia e competenze reali del team, non un paragrafo generico: è il primo posto dove Google e i lettori cercano di capire chi c’è dietro.': {'en': 'With names, faces, history and the team’s actual expertise, not a generic paragraph: it’s the first place Google and readers look to understand who’s behind the site.'},
    'Rendete i contatti verificabili': {'en': 'Make your contacts verifiable'},
    'Indirizzo completo, telefono ed email reali in chiaro, nel footer di ogni pagina, non solo dentro un modulo: un recapito tracciabile è un segnale di fiducia di base.': {'en': 'A full address, a real phone number and email in plain sight, in every page footer, not just inside a form: a traceable contact is a baseline trust signal.'},
    'Dichiarate l’identità legale': {'en': 'Declare your legal identity'},
    'P.IVA, ragione sociale e sede nel footer: per un’azienda italiana è la prova più semplice di essere un soggetto reale e raggiungibile.': {'en': 'VAT number, company name and registered address in the footer: it’s the simplest proof of being a real, reachable business.'},
    'Aggiungete i dati strutturati': {'en': 'Add structured data'},
    'Un blocco JSON-LD schema.org Organization (o LocalBusiness) con nome, logo, contatti e profili «sameAs» dice a motori e AI chi siete, in modo esplicito.': {'en': 'A JSON-LD schema.org Organization (or LocalBusiness) block with name, logo, contacts and “sameAs” profiles tells engines and AI who you are, explicitly.'},
    'Firmate e datate i contenuti': {'en': 'Sign and date your content'},
    'Autore riconoscibile, data di pubblicazione e di aggiornamento su articoli e schede: mostrano esperienza reale e contenuti curati nel tempo.': {'en': 'A named author, a publish date and a last-updated date on articles and pages: they show real experience and content kept current.'},
    'Vogliamo sistemarli noi: fa parte della SEO tecnica →': {'en': 'We can fix them for you: it’s part of technical SEO →'},
    'Chi siamo, contatti e dati strutturati sono di serie nei siti aziendali →': {'en': 'About page, contacts and structured data come standard on business websites →'},
    'Controllate anche la SEO on-page della pagina →': {'en': 'Check the page’s on-page SEO too →'},
    'Vogliamo rafforzare la fiducia del vostro sito': {'en': 'Want to strengthen your site’s credibility'},
    'Chi siamo, contatti verificabili, identità legale e dati strutturati a posto: fanno parte della SEO tecnica e di ogni sito aziendale che consegniamo.': {'en': 'About page, verifiable contacts, legal identity and structured data in place: they’re part of the technical SEO and every business website we deliver.'},
    'Analizza i segnali di fiducia': {'en': 'Check the trust signals'},
    'Punteggio E-E-A-T on-page': {'en': 'On-page E-E-A-T score'},
    'I quattro pilastri': {'en': 'The four pillars'},
    'Otto segnali di fiducia': {'en': 'Eight trust signals'},
    'Connessione HTTPS': {'en': 'HTTPS connection'},
    'Contatti verificabili': {'en': 'Verifiable contacts'},
    'Identità legale (P.IVA)': {'en': 'Legal identity (VAT)'},
    'Privacy e cookie policy': {'en': 'Privacy & cookie policy'},
    'Pagina «Chi siamo»': {'en': 'About page'},
    'Portfolio / casi studio': {'en': 'Portfolio / case studies'},
    'Dati strutturati (JSON-LD)': {'en': 'Structured data (JSON-LD)'},
    'Profili esterni': {'en': 'External profiles'},
    'Esperienza': {'en': 'Experience'},
    'Competenza': {'en': 'Expertise'},
    'Autorevolezza': {'en': 'Authoritativeness'},
    'Affidabilità': {'en': 'Trust'},
    'Ottimo: i segnali di fiducia E-E-A-T sono presenti e leggibili nel codice. Ricordate che parliamo di segnali on-page, non del vostro E-E-A-T reale.': {'en': 'Excellent: the E-E-A-T trust signals are present and readable in the code. Remember these are on-page signals, not your real E-E-A-T.'},
    'Buona base: la maggior parte dei segnali di fiducia c’è. Sistemate i pochi punti in giallo o rosso per completare il quadro.': {'en': 'Solid base: most trust signals are there. Fix the few amber or red items to complete the picture.'},
    'A metà strada: diversi segnali di fiducia mancano o non sono leggibili. La lista qui sotto indica da dove partire.': {'en': 'Halfway there: several trust signals are missing or unreadable. The list below shows where to start.'},
    'Segnali deboli: la pagina espone pochi elementi di fiducia verificabili — che sono anche i più facili da aggiungere.': {'en': 'Weak signals: the page exposes few verifiable trust cues — which are also the easiest to add.'},
    'Il sito rende i contenuti via JavaScript: alcuni segnali potrebbero esistere ma non essere leggibili nell’HTML iniziale. Il punteggio è indicativo.': {'en': 'The site renders content via JavaScript: some signals may exist but aren’t readable in the initial HTML. The score is indicative.'},
    'non rilevato (possibile rendering JavaScript)': {'en': 'not detected (possible JavaScript rendering)'},
    'Non siamo riusciti a leggere la pagina. Controllate l’indirizzo e riprovate tra qualche minuto.': {'en': 'We couldn’t read the page. Check the address and try again in a few minutes.'},
    'Misuriamo segnali on-page verificabili nel codice della pagina, non la vostra reputazione o competenza reale. Un punteggio alto non garantisce un giudizio E-E-A-T positivo da parte di Google.': {'en': 'We measure on-page signals readable in the page code, not your real reputation or expertise. A high score doesn’t guarantee a positive E-E-A-T judgement from Google.'},
    'Connessione sicura (HTTPS)': {'en': 'Secure connection (HTTPS)'},
    'Nessun HTTPS: connessione non sicura': {'en': 'No HTTPS: insecure connection'},
    'Contatti verificabili presenti': {'en': 'Verifiable contacts present'},
    'Solo un’email, nessun telefono o indirizzo': {'en': 'Only an email, no phone or address'},
    'Nessun contatto verificabile': {'en': 'No verifiable contacts'},
    'P.IVA / dati fiscali presenti': {'en': 'VAT / tax details present'},
    'Nessuna P.IVA o identità legale': {'en': 'No VAT or legal identity'},
    'Privacy e cookie policy presenti': {'en': 'Privacy and cookie policy present'},
    'Presente solo una delle due policy': {'en': 'Only one of the two policies'},
    'Nessuna privacy o cookie policy': {'en': 'No privacy or cookie policy'},
    'Pagina «Chi siamo» presente': {'en': 'About page present'},
    'Nessuna pagina «Chi siamo»': {'en': 'No about page'},
    'Portfolio o casi studio presenti': {'en': 'Portfolio or case studies present'},
    'Nessun portfolio o caso studio': {'en': 'No portfolio or case studies'},
    'Dati strutturati d’identità presenti': {'en': 'Identity structured data present'},
    'JSON-LD presente ma solo generico': {'en': 'JSON-LD present but generic only'},
    'Nessun dato strutturato JSON-LD': {'en': 'No JSON-LD structured data'},
    'Profili esterni collegati': {'en': 'External profiles linked'},
    'Un solo profilo esterno': {'en': 'Only one external profile'},
    'Nessun profilo esterno collegato': {'en': 'No external profiles linked'},
    'Misurate anche i segnali di fiducia E-E-A-T del sito →': {'en': 'Also measure your site’s E-E-A-T trust signals →'},
    'Verificate anche i segnali di fiducia E-E-A-T →': {'en': 'Also check your E-E-A-T trust signals →'},
    'Misura i segnali E-E-A-T del sito →': {'en': 'Check your site’s E-E-A-T signals →'},
}
CHROME.update(CHROME_EEAT)
