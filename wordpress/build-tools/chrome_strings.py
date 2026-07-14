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
