"""Контент студии — единый источник для генератора WP-страниц.

Сверено построчно с дизайн-хендоффом (design_handoff_studio_remarka/*.dc.html,
"Fidelity: High-fidelity... copy... final design intent"). Текст сервиса
"Siti aziendali" и футера — дословно из хендоффа. Для остальных пяти услуг
хендофф даёт только один полный пример (Siti aziendali) — их текст написан
по тому же паттерну (H1-обещание, «Per chi»/«Cosa include»/мини-кейс с
городом и подписью/«Confronta le tariffe»/трастовый вопрос в FAQ), но своими
словами, и привязан к четырём каноничным кейсам ниже вместо новых вымышленных
имён.
"""

SERVICES = [
    dict(
        # Единственная услуга, где в хендоффе дан полный авторский текст —
        # перенесено дословно (Servizio.dc.html).
        slug='siti-aziendali', title='Siti aziendali',
        breadcrumb='Servizio / Siti aziendali',
        hero_title='Il sito aziendale che carica in un secondo',
        hero_sub='Un sito web aziendale di quindici pagine, due lingue e un CMS per aggiornarlo da soli. Progettato per trasformare le visite in richieste di preventivo.',
        hero_stat_value='1,1 s', hero_stat_label='Caricamento medio (LCP) dei siti aziendali consegnati nel 2025.',
        per_chi_heading='Un sito web aziendale per chi vive di richieste, non di clic',
        per_chi=[
            'PMI manifatturiere con cataloghi tecnici e clienti B2B che confrontano fornitori.',
            'Studi professionali e società di servizi che vivono di reputazione e primo contatto.',
            "Aziende con clienti esteri: la versione inglese o tedesca è tradotta da madrelingua, inclusa.",
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Fino a 15 pagine, struttura studiata sul funnel',
            'Due lingue incluse, tradotte da madrelingua',
            'CMS: testi e foto li aggiornate da soli',
            'SEO tecnica completa e dati strutturati',
            'GDPR: banner, informative e consensi a norma',
            'PageSpeed 90+ garantito da contratto',
            'Modulo contatti con notifiche immediate',
            '12 mesi di assistenza e misurazioni mensili',
        ],
        mini_caso=dict(
            cliente='ATT', progetto='traduzione.tech', link_slug='/casi-studio/#att-traduzione-tech',
            testo="Sito aziendale per un'agenzia di traduzioni con più di vent'anni di storia: preventivi rapidi, servizi chiari per il cliente B2B italiano. Online dal 2022, porta all'agenzia circa 20 ordini al mese.",
            stat1_value='20/mese', stat1_label='ordini generati dal sito',
            stat2_value='40+', stat2_label='combinazioni linguistiche coperte',
            caption='PROGETTO DEL GRUPPO REMARKA — VERIFICABILE SU TRADUZIONE.TECH',
        ),
        prezzo_range='{{listino}}€ 3.900–5.800{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 3.900–5.800</s> '
                      '<span class="sr-lancio-price">€ 1.950–2.900</span>{{/lancio}}',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 3 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di pagine e schede prodotto oltre le 15 incluse.',
            'Lingue aggiuntive oltre le due comprese.',
            'Integrazioni con gestionale, CRM o listini esterni.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Possiamo tenere i testi attuali?', 'Sì. Li revisioniamo gratuitamente in fase di analisi e vi diciamo cosa conviene riscrivere, e perché.'),
            ('Il dominio resta nostro?', 'Sempre. Dominio, hosting e codice sono intestati a voi dal primo giorno. Nessun vincolo con lo studio.'),
            ('E dopo i 12 mesi di assistenza?', "Canone annuale facoltativo, con lo stesso perimetro. Oppure il sito resta a voi così com’è: è vostro."),
        ],
    ),
    dict(
        slug='e-commerce', title='E-commerce',
        breadcrumb='Servizio / E-commerce',
        hero_title='Il negozio online che non perde clienti nel checkout',
        hero_sub='Realizzazione siti e-commerce con catalogo veloce, checkout in un passaggio e fatturazione elettronica integrata: pensata per chi vende, non solo per chi naviga.',
        hero_stat_value='1,4 s', hero_stat_label='Caricamento medio (LCP) degli e-commerce consegnati nel 2025.',
        per_chi_heading='Realizzazione siti e-commerce per chi vende sul serio, non solo espone',
        per_chi=[
            'Attività che vendono online ma perdono clienti proprio nel checkout.',
            'Negozi fisici pronti ad aprire un canale e-commerce senza improvvisare.',
            'Chi ha bisogno di fatturazione elettronica automatica, non di un plugin da rincorrere.',
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Catalogo prodotti illimitato con varianti',
            'Checkout in un solo passaggio',
            'Pagamenti con carta, PayPal e bonifico',
            'Fatturazione elettronica via SDI integrata',
            'Gestione magazzino e spedizioni',
            'SEO tecnica per le pagine prodotto',
            'PageSpeed 90+ garantito da contratto',
            '12 mesi di assistenza e misurazioni mensili',
        ],
        mini_caso=dict(
            cliente='ukrinitsy.ru', progetto='ukrinitsy.ru', link_slug='/casi-studio/#ukrinitsy',
            testo='Sito vetrina per una piccola guest house: foto, contatti e richiesta di prenotazione a portata di mano. Dopo il lancio le prenotazioni dirette dal sito sono cresciute del 450%.',
            stat1_value='+450%', stat1_label='prenotazioni dopo il lancio',
            stat2_value='18', stat2_label='prenotazioni in una stagione, dal sito',
            caption='PROGETTO DEL GRUPPO REMARKA — VERIFICABILE SU UKRINITSY.RU',
        ),
        prezzo_range='{{listino}}€ 7.500–14.000{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 7.500–14.000</s> '
                      '<span class="sr-lancio-price">€ 3.750–7.000</span>{{/lancio}}',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 6 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di prodotti e varianti oltre il catalogo base.',
            'Integrazioni con corrieri e magazzino esterno.',
            'Metodi di pagamento aggiuntivi oltre carta, PayPal e bonifico.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Gestite anche la fatturazione elettronica?', 'Sì, ogni ordine genera automaticamente una fattura elettronica conforme SDI.'),
            ("Posso vendere anche all’estero?", 'Sì, il catalogo supporta più lingue e più valute su richiesta.'),
            ('Il dominio e i dati dei clienti restano nostri?', 'Sempre. Dominio, database ordini e codice sono intestati a voi dal primo giorno.'),
        ],
    ),
    dict(
        slug='siti-pwa', title='Siti progressivi PWA',
        breadcrumb='Servizio / Siti progressivi PWA',
        hero_title="Un sito che si apre come un’app, senza passare dagli store",
        hero_sub="Una progressive web app installabile, che funziona offline e si apre all’istante anche alla decima visita: senza i costi e i tempi di App Store e Play Store.",
        hero_stat_value='0,9 s', hero_stat_label='Caricamento medio (LCP) delle PWA consegnate nel 2025.',
        per_chi_heading='Una progressive web app per chi ha clienti che tornano, non solo che passano',
        per_chi=[
            'Attività con clienti che tornano spesso a consultare il sito.',
            "Chi vuole un’app senza i costi e le revisioni di App Store e Play Store.",
            'Servizi che devono funzionare bene anche con connessione debole, in cantiere o in showroom.',
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Installabile su smartphone come un’app',
            'Funziona offline per le pagine già visitate',
            'Notifiche push opzionali',
            'Caricamento istantaneo dopo la prima visita',
            'Service worker configurato e testato',
            'SEO tecnica completa e dati strutturati',
            'PageSpeed 90+ garantito da contratto',
            '12 mesi di assistenza e misurazioni mensili',
        ],
        mini_caso=dict(
            cliente='Mini App Telegram', progetto='@massimoalefBot', link_slug='/casi-studio/#mini-app-telegram',
            testo="Le funzioni chiave del TMS portate in una Telegram Mini App: ordini e notifiche dentro la chat, senza installare niente. Sviluppata in 2 settimane.",
            stat1_value='2 settimane', stat1_label="dalla decisione all'app in produzione",
            stat2_value='10+/giorno', stat2_label='utenti e ordini gestiti ogni giorno',
            caption='PROGETTO DEL GRUPPO REMARKA — VERIFICABILE SU TELEGRAM',
        ),
        prezzo_range='€ 4.900–7.200',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 4 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Funzionalità offline richieste oltre le pagine base.',
            'Notifiche push e integrazioni native aggiuntive.',
            'Numero di pagine e sezioni oltre quelle incluse.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Serve pubblicarlo sugli store?', 'No, si installa direttamente dal browser: nessuna revisione Apple o Google necessaria.'),
            ('Funziona su tutti gli smartphone?', 'Sì, è compatibile con iOS e Android tramite qualsiasi browser moderno.'),
            ('Posso passare da un sito esistente a una PWA?', 'Sì, è un percorso di restyling tecnico che manteniamo trasparente per i motori di ricerca.'),
        ],
    ),
    dict(
        slug='restyling-migrazione', title='Restyling e migrazione',
        breadcrumb='Servizio / Restyling e migrazione',
        hero_title='Il vostro sito, ricostruito: stessi contenuti, il triplo della velocità',
        hero_sub='Rifacimento sito web senza perdere posizionamento e senza riscrivere i contenuti: cambia solo la base tecnica, e cambia in meglio.',
        hero_stat_value='1,2 s', hero_stat_label='Caricamento medio (LCP) dei restyling consegnati nel 2025.',
        per_chi_heading='Rifacimento sito web per chi ha già i contenuti giusti, e la tecnologia sbagliata',
        per_chi=[
            'Chi ha un sito lento ma non vuole perdere posizionamento SEO faticosamente conquistato.',
            'Attività con contenuti validi ma una tecnologia costruita più di cinque anni fa.',
            'Chi ha ricevuto un preventivo di rifacimento completo troppo costoso per quello che serve davvero.',
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Audit tecnico del sito attuale',
            'Migrazione dei contenuti esistenti',
            'Redirect 301 per mantenere il posizionamento SEO',
            'Nuova base tecnica performante',
            'Ottimizzazione immagini e font',
            'Test comparativo prima/dopo su PageSpeed',
            'PageSpeed 90+ garantito da contratto',
            '12 mesi di assistenza e misurazioni mensili',
        ],
        mini_caso=dict(
            cliente='moscowtrans.ru · techperevod.com', progetto='moscowtrans.ru', link_slug='/casi-studio/#moscowtrans-techperevod',
            testo='Due siti d’agenzia ridisegnati nel 2026, curati nel design e ottimizzati nelle performance. Le conversioni sono cresciute di oltre il 300% negli ultimi mesi.',
            stat1_value='+300%', stat1_label='conversioni dopo il rinnovo 2026',
            stat2_value='2', stat2_label='siti rinnovati con lo stesso metodo',
            caption='PROGETTO DEL GRUPPO REMARKA — VERIFICABILE SUI DUE SITI',
        ),
        prezzo_range='€ 2.900–4.800',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 3 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di pagine da migrare oltre le prime 20.',
            'Complessità delle integrazioni esistenti da mantenere.',
            'Necessità di redesign grafico oltre alla base tecnica.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Perdo il posizionamento su Google?', 'No, impostiamo redirect 301 corretti per ogni URL esistente prima di andare online.'),
            ('Devo riscrivere i contenuti?', 'No, il restyling tecnico mantiene i contenuti esistenti; li aggiorniamo solo su richiesta.'),
            ('Quanto dura la migrazione?', 'In media 3 settimane, con un ambiente di prova visibile fin dalla prima settimana.'),
        ],
    ),
    dict(
        slug='seo-tecnica', title='SEO tecnica',
        breadcrumb='Servizio / SEO tecnica',
        hero_title='Struttura e dati a posto, prima ancora di scrivere i contenuti',
        hero_sub='Core Web Vitals, dati strutturati e sitemap corretti: è la SEO tecnica, quella che il copywriting da solo non risolve.',
        hero_stat_value='90+', hero_stat_label='Punteggio Core Web Vitals garantito da contratto.',
        per_chi_heading='La SEO tecnica per chi ha buoni contenuti e scarsa visibilità',
        per_chi=[
            'Siti con buoni contenuti ma scarsa visibilità su Google.',
            'Chi ha già investito in copywriting senza vedere risultati in classifica.',
            'Attività che competono in mercati locali affollati, dove ogni posizione conta.',
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Audit tecnico SEO completo',
            'Dati strutturati (schema.org) per ogni tipo di pagina',
            'Ottimizzazione Core Web Vitals',
            'Sitemap XML e file robots ottimizzati',
            'Struttura URL e gerarchia dei contenuti',
            'Ottimizzazione meta title e description',
            'Report mensile di posizionamento',
            'PageSpeed 90+ garantito da contratto',
        ],
        mini_caso=dict(
            cliente='пере.рф', progetto='пере.рф', link_slug='/casi-studio/#pere-rf',
            testo='Dominio di due lettere su alfabeto cirillico, portato ai primi posti su Yandex con SEO puramente tecnica: nessuna scorciatoia dal nome.',
            stat1_value='№ 1', stat1_label='su Yandex per «traduzione notarile»',
            stat2_value='9–10 mila/mese', stat2_label='visitatori, in vetta da oltre 1.000 giorni',
            caption='PROGETTO DEL GRUPPO REMARKA — VERIFICABILE SU ПЕРЕ.РФ',
        ),
        prezzo_range='€ 1.800–3.500',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 3 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di pagine da ottimizzare oltre le prime 20.',
            'Presenza di contenuti multilingua da trattare.',
            'Storico tecnico da correggere prima di intervenire.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('In quanto tempo si vedono risultati?', 'I miglioramenti tecnici sono immediati; il posizionamento su Google richiede in media 6–10 settimane.'),
            ('Scrivete anche i contenuti?', 'Il servizio è tecnico; per la scrittura dei testi lavoriamo con copywriter partner su richiesta.'),
            ('Fate SEO locale?', 'Sì, includiamo l’ottimizzazione della scheda Google Business Profile quando pertinente.'),
        ],
    ),
    dict(
        slug='siti-multilingue', title='Siti multilingue',
        breadcrumb='Servizio / Siti multilingue',
        hero_title='Quattro lingue tradotte da madrelingua, non da un plugin',
        hero_sub="Un sito web multilingua è il mestiere del gruppo Remarka dal 2001: traduzione professionale, non automatica, con SEO multilingue corretta fin dal primo giorno.",
        hero_stat_value='4', hero_stat_label='Lingue native disponibili: italiano, inglese, tedesco, francese.',
        per_chi_heading='Un sito web multilingua per chi vende oltre confine, non solo in italiano',
        per_chi=[
            'Aziende che esportano o accolgono clienti stranieri.',
            'Attività turistiche con visitatori internazionali.',
            'Chi ha usato finora traduzioni automatiche poco professionali, e i clienti se ne sono accorti.',
        ],
        include_heading='Tutto scritto nel preventivo',
        include=[
            'Traduzione professionale da madrelingua (non plugin)',
            'Fino a 4 lingue: italiano, inglese, tedesco, francese',
            'Selettore lingua persistente',
            'SEO multilingue con hreflang corretti',
            'Contenuti localizzati, non solo tradotti',
            'Revisione linguistica da parte del gruppo Remarka',
            'PageSpeed 90+ garantito da contratto',
            '12 mesi di assistenza e misurazioni mensili',
        ],
        mini_caso=dict(
            cliente='Sistema di test dei traduttori', progetto='moscowtrans.ru/test-perevodchika', link_slug='/casi-studio/#test-traduttori',
            testo='La piattaforma di test dei traduttori che sta dietro alla garanzia «redattori madrelingua per profilo» su ogni sito multilingue che consegniamo.',
            stat1_value='400+', stat1_label='traduttori testati',
            stat2_value='8%', stat2_label='supera la selezione',
            caption='PROGETTO DEL GRUPPO REMARKA — IN USO SU TUTTI I PROGETTI',
        ),
        prezzo_range='€ 3.200–5.500',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 4 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di lingue aggiuntive oltre le due comprese.',
            'Volume di contenuti da tradurre oltre le pagine base.',
            'Necessità di revisione periodica dopo la consegna.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Le traduzioni sono automatiche?', 'No, sono realizzate da traduttori madrelingua del gruppo Remarka, non da plugin automatici.'),
            ('Posso aggiungere una lingua in futuro?', 'Sì, la struttura multilingue è predisposta per aggiungere nuove lingue senza rifare il sito.'),
            ('La SEO funziona in tutte le lingue?', 'Sì, ogni lingua ha URL e tag hreflang dedicati per essere indicizzata correttamente da Google.'),
        ],
    ),
]

# Undici casi studio reali del gruppo Remarka (docs/copy-casi-studio.md):
# progetti che il gruppo ha costruito PER SÉ, non clienti terzi inventati.
# Formato deciso dall'orchestratore (deck §8.3): un solo catalogo con schede
# espanse in patterns/pages/casi-studio-index.php — niente più pagine
# caso-<slug>.php separate, quindi niente prima/dopo PageSpeed inventati:
# ogni "risultato" è una cifra reale fornita dal proprietario (deck §7) o,
# per il gioco, la variante esplicitamente indicata come pubblicabile.
# `slug` = id àncora della scheda nel catalogo (deck §6.2), riusato anche
# come link_slug dai mini-casi dei servizi e dai case_slug delle città.
CASES = [
    dict(
        slug='att-traduzione-tech', data_cat='siti', chip='Sito aziendale',
        cliente='ATT', url='https://www.traduzione.tech', url_label='traduzione.tech',
        titolo="Il sito dell'agenzia di traduzioni, costruito da traduttori",
        problema="Un'agenzia di traduzioni con più di vent'anni di storia aveva bisogno di un sito che parlasse la lingua del cliente italiano B2B: preventivi rapidi, servizi chiari, fiducia immediata. Il vecchio sito non reggeva né i tempi di caricamento né la struttura dei servizi.",
        soluzione="Abbiamo riprogettato il sito di ATT (Agenzia di Traduzioni Tecniche) come un sito aziendale completo: architettura dei servizi per settore e per lingua, richiesta di preventivo in pochi passaggi, contenuti scritti da chi le traduzioni le fa davvero. SEO tecnica e dati strutturati dalla prima riga. È il nostro biglietto da visita: se non funzionasse, lo sapremmo per primi.",
        risultato="Online dal 2022, il sito porta all'agenzia circa 20 ordini al mese, su oltre 40 combinazioni e direzioni linguistiche. È il canale con cui ATT acquisisce clienti oggi.",
        alt='Home page del sito dell’agenzia di traduzioni traduzione.tech, con i servizi in evidenza',
        cta_testo='Un sito aziendale come questo', cta_href='/servizi/siti-aziendali/',
        shots=[dict(file='att-home-1440.jpg', mobile=False, caption='ATT — home, blocco servizi, desktop')],
    ),
    dict(
        slug='tms-perevod4', data_cat='webapp', chip='Web app',
        cliente='TMS', url='https://tms.perevod4.ru', url_label='tms.perevod4.ru',
        titolo='La web app che manda avanti un’agenzia di traduzioni',
        problema="Gestire centinaia di ordini di traduzione — clienti, traduttori, scadenze, preventivi, fatture — con fogli di calcolo e email è un collo di bottiglia che rompe le consegne. Ci serviva un solo sistema, non dieci strumenti scollegati.",
        soluzione="Abbiamo costruito un TMS completo (Translation Management System): un pannello dove ogni ordine ha uno stato, ogni cliente una scheda, ogni traduttore un carico e ogni lavoro la sua fattura. Bacheca degli ordini, anagrafiche, preventivi e contabilità in un'unica web app. È il sistema operativo interno del gruppo: lo usiamo tutti i giorni per non perdere una consegna. Questo è il nostro progetto di punta: la stessa ingegneria che mettiamo nelle web app su misura per voi.",
        risultato="In produzione da 2 anni: il sistema gestisce 180 ordini al mese, oltre 2.000 l'anno. Dentro ci lavorano 2 amministratori, 8 project manager e 4 agenzie partner con la propria base — e gli ordini non si perdono più tra le email.",
        alt='Pannello del TMS tms.perevod4.ru con la bacheca degli ordini di traduzione',
        cta_testo='Una web app su misura per la vostra azienda', cta_href='/servizi/web-app/',
        shots=[
            dict(file='tms-board-1440.jpg', mobile=False, caption='TMS — bacheca ordini, schermata principale, desktop'),
            dict(file='tms-clienti-1440.jpg', mobile=False, caption='TMS — scheda cliente, storico ordini'),
            dict(file='tms-fatture-1440.jpg', mobile=False, caption='TMS — fatture e contabilità'),
        ],
    ),
    dict(
        slug='mini-app-telegram', data_cat='webapp', chip='Mini App / PWA',
        cliente='Mini App Telegram', url='https://t.me/massimoalefBot', url_label='@massimoalefBot',
        titolo='La Mini App Telegram che quasi nessuno, in Italia, sa ancora fare',
        problema="Traduttori e clienti vivono dentro le chat, non nelle scrivanie. Aprire un gestionale via browser per controllare un ordine è troppo. Serviva l'accesso al TMS dentro Telegram, senza installare niente.",
        soluzione="Abbiamo portato le funzioni chiave del TMS in una Telegram Mini App: ordini, stati e notifiche direttamente in chat, con la stessa logica del pannello web. In Italia le Mini App Telegram sono ancora rarissime tra le PMI: è esattamente il tipo di prodotto che sappiamo costruire quando l'interfaccia deve stare dove sono già le persone.",
        risultato="Sviluppata in 2 settimane, oggi la Mini App gestisce oltre 10 utenti e ordini al giorno: il gestionale entra in tasca, senza app da installare.",
        alt='Mini App Telegram del TMS aperta dentro la chat, con la lista degli ordini',
        cta_testo='Una Mini App o PWA per il vostro pubblico', cta_href='/servizi/web-app/',
        shots=[dict(file='miniapp-orders-390.jpg', mobile=True, caption='Mini App Telegram — lista ordini, mobile')],
    ),
    dict(
        slug='ai-perevod4', data_cat='seo', chip='SEO tecnica · Multilingue',
        cliente='ai.perevod4.ru', url='https://ai.perevod4.ru', url_label='ai.perevod4.ru',
        titolo='Un progetto AI multilingue, italiano incluso',
        problema="Un progetto basato sull'intelligenza artificiale ha senso solo se lo trova la persona giusta, nella sua lingua. Costruire un sito AI multilingue che regga la SEO tecnica in ogni versione — italiano compreso — è un lavoro di ingegneria, non di plugin di traduzione.",
        soluzione="Abbiamo realizzato ai.perevod4.ru come progetto multilingue con versione italiana nativa: struttura tecnica pulita, dati strutturati e contenuti pensati per la ricerca in ogni lingua, non tradotti a macchina. La versione italiana esiste perché sappiamo servire il mercato italiano dalla base tecnica alla lingua.",
        risultato="Oltre 60 lingue di lavoro e più di 10.000 richieste elaborate al mese: un progetto AI che si fa trovare — e si usa — in più mercati.",
        alt='Versione italiana del progetto AI multilingue ai.perevod4.ru',
        cta_testo='SEO tecnica e siti multilingue', cta_href='/servizi/seo-tecnica/',
        shots=[dict(file='ai-home-it-1440.jpg', mobile=False, caption='ai.perevod4.ru — versione italiana, primo schermo')],
    ),
    dict(
        slug='perevod4-catalogo', data_cat='seo', chip='SEO · Contenuti',
        cliente='perevod4.ru', url='https://perevod4.ru', url_label='perevod4.ru',
        titolo='Il catalogo che indicizza un intero settore',
        problema="Un portale-catalogo che copre un intero settore — agenzie, città, specializzazioni — vive o muore sulla SEO tecnica: se la struttura non regge, Google non indicizza e il contenuto non esiste.",
        soluzione="Abbiamo costruito perevod4.ru come portale editoriale/SEO a catalogo: agenzie di traduzione schedate per città e specializzazione, con struttura coerente, dati strutturati e velocità tenuta sotto controllo su tutto il volume. È la prova che sappiamo far reggere la SEO tecnica quando le pagine si contano a centinaia, non a decine.",
        risultato="Oltre 200 agenzie di traduzione schedate a catalogo: un intero settore reso navigabile e indicizzabile, con la SEO tecnica messa alla prova sulla scala, non sulla demo.",
        alt='Portale-catalogo perevod4.ru con l’elenco delle agenzie di traduzione per città',
        cta_testo='SEO tecnica per progetti di contenuto', cta_href='/servizi/seo-tecnica/',
        shots=[dict(file='perevod4-catalog-1440.jpg', mobile=False, caption='perevod4.ru — catalogo agenzie per città')],
    ),
    dict(
        slug='gioco-impero-traduzioni', data_cat='restyling', chip='Marketing · Gamification',
        cliente='«L’Impero delle Traduzioni»', url='https://traduzione.tech/gioco/', url_label='traduzione.tech/gioco',
        titolo='Un gioco per raccontare le traduzioni (in italiano)',
        problema="Un servizio B2B «serio» come la traduzione fatica a farsi ricordare. Volevamo un modo per far restare le persone sul sito e raccontare il nostro mondo senza una brochure noiosa.",
        soluzione="Abbiamo creato «L'Impero delle Traduzioni», un gioco browser in italiano dentro il sito dell'agenzia: gamification al servizio del marketing, contenuto che intrattiene e allo stesso tempo racconta cosa facciamo. È il lato creativo dello stesso team che vi fa il restyling: quando serve far restare l'utente, sappiamo anche divertirlo.",
        risultato="Un contenuto che trattiene le persone sul sito e dà al marchio qualcosa da raccontare: la gamification usata come strumento di marketing, non come gadget.",
        alt='Schermata del gioco browser «L’Impero delle Traduzioni» in italiano su traduzione.tech',
        cta_testo='Restyling e idee di marketing per il vostro sito', cta_href='/servizi/restyling-migrazione/',
        shots=[dict(file='gioco-play-1440.jpg', mobile=False, caption='Gioco «L’Impero delle Traduzioni» — schermata di gioco')],
    ),
    dict(
        slug='pere-rf', data_cat='seo', chip='SEO tecnica',
        cliente='пере.рф', url='https://пере.рф', url_label='пере.рф',
        titolo='Due lettere di dominio, una lezione di SEO tecnica',
        problema="Un dominio brevissimo su alfabeto non latino (IDN/punycode) è un caso limite: posizionarlo bene richiede una SEO tecnica impeccabile, perché non si può contare sul nome.",
        soluzione="Abbiamo portato пере.рф ai primi posti con lavoro puramente tecnico: struttura, velocità, dati strutturati, gestione corretta del dominio internazionalizzato. È uno dei nostri casi SEO più forti proprio perché il risultato non arriva dal branding, ma dall'ingegneria.",
        risultato="Posizione n. 1 su Yandex — il principale motore di ricerca russo — per le query di settore «traduzione notarile» e «traduzione di manuali», 9.000–10.000 visitatori al mese, in vetta da oltre 1.000 giorni. Primi posti ottenuti con la tecnica, non con il nome.",
        alt='Sito пере.рф, caso di SEO tecnica su dominio internazionalizzato',
        cta_testo='SEO tecnica che porta risultati', cta_href='/servizi/seo-tecnica/',
        shots=[dict(file='pererf-home-1440.jpg', mobile=False, caption='пере.рф — home page')],
    ),
    dict(
        slug='ukrinitsy', data_cat='siti', chip='Sito vetrina',
        cliente='ukrinitsy.ru', url='https://ukrinitsy.ru', url_label='ukrinitsy.ru',
        titolo='Un sito vetrina per una piccola attività di ospitalità',
        problema="Una casa vacanze/guest house vive di prenotazioni dirette e di fiducia: al piccolo operatore turistico serve un sito semplice, veloce e credibile, non un gestionale.",
        soluzione="Abbiamo realizzato ukrinitsy.ru come sito vetrina essenziale: foto che vendono la struttura, contatti e richiesta di prenotazione a portata di mano, caricamento rapido anche da mobile. Lo stesso approccio «piccolo, ma fatto bene» che portiamo a ristoranti, studi e attività locali.",
        risultato="Dopo il lancio le prenotazioni sono cresciute del 450%: 18 prenotazioni in una stagione arrivate dal sito — per una piccola struttura, la differenza tra stagione piena e stanze vuote.",
        alt='Sito vetrina della guest house ukrinitsy.ru, versione mobile',
        cta_testo='Un sito vetrina per la vostra attività', cta_href='/servizi/siti-aziendali/',
        shots=[dict(file='ukrinitsy-mobile-390.jpg', mobile=True, caption='ukrinitsy.ru — prima schermata, mobile')],
    ),
    dict(
        slug='moscowtrans-techperevod', data_cat='restyling', chip='Design · Restyling',
        cliente='moscowtrans.ru · techperevod.com',
        url='https://moscowtrans.ru', url_label='moscowtrans.ru · techperevod.com',
        titolo='Due siti d’agenzia "belli e veloci" per un mercato esigente',
        problema="Sul mercato competitivo delle agenzie di traduzione un sito deve essere insieme bello e velocissimo: l'estetica costruisce fiducia, la velocità la mantiene. Riuscirci su due siti diversi, con la stessa qualità, è una prova di metodo.",
        soluzione="Abbiamo progettato moscowtrans.ru e techperevod.com come coppia di siti d'agenzia curati nel design e ottimizzati nella performance: gerarchia visiva chiara, immagini leggere, struttura dei servizi pensata per la conversione. È il nostro lato «design + restyling» applicato a un settore in cui i concorrenti si somigliano tutti.",
        risultato="Dopo il rinnovo di design e funzionalità del 2026, le conversioni sono cresciute di oltre il 300% negli ultimi mesi: due siti che si distinguono in un settore dove tutti si somigliano.",
        alt='Home page dei siti d’agenzia moscowtrans.ru e techperevod.com affiancate',
        cta_testo='Restyling e nuovo design per il vostro sito', cta_href='/servizi/restyling-migrazione/',
        shots=[
            dict(file='moscowtrans-home-1440.jpg', mobile=False, caption='moscowtrans.ru — home page'),
            dict(file='techperevod-home-1440.jpg', mobile=False, caption='techperevod.com — home page'),
        ],
    ),
    dict(
        slug='test-traduttori', data_cat='webapp', chip='Web app · HR-tech',
        cliente='Sistema di test dei traduttori',
        url='https://moscowtrans.ru/test-perevodchika/', url_label='moscowtrans.ru/test-perevodchika',
        titolo='La piattaforma che decide chi traduce i vostri testi',
        problema="La promessa «redattori madrelingua per specializzazione» che leggete sulle nostre pagine di servizio vale solo se dietro c'è un modo serio per selezionare chi traduce. Scegliere i traduttori a occhio non è un metodo.",
        soluzione="Abbiamo costruito una piattaforma di valutazione e test dei traduttori — un sistema di selezione progressivo usato in tutti i progetti del gruppo: prove a difficoltà crescente, valutazione strutturata, filtro automatico dei candidati. È il prodotto interno che tiene la qualità delle nostre traduzioni: è esattamente questo sistema a stare dietro alla garanzia «redattori madrelingua per profilo» dei siti multilingue che vi consegniamo.",
        risultato="Oltre 400 traduttori testati — e solo l'8% supera la selezione. Ogni traduttore che lavora sui vostri testi è dentro quell'8%: la qualità decisa da un sistema, non a intuito.",
        alt='Piattaforma di test e valutazione dei traduttori del gruppo Remarka',
        cta_testo='Una web app su misura per il vostro processo', cta_href='/servizi/web-app/',
        shots=[dict(file='tester-exam-1440.jpg', mobile=False, caption='Piattaforma test traduttori — schermata di valutazione')],
    ),
    dict(
        slug='1russian', data_cat='seo', chip='SEO · Contenuti',
        cliente='1russian.com', url='https://1russian.com', url_label='1russian.com',
        titolo='Un progetto internazionale, scritto in inglese per il mondo',
        problema="Un progetto pensato per un pubblico globale vive o muore sulla lingua e sulla ricerca: contenuti in inglese che un anglofono legge come propri, e una base tecnica che Google indicizza senza attriti. Non basta tradurre — bisogna scrivere per quel pubblico.",
        soluzione="Abbiamo costruito 1russian.com come progetto internazionale in lingua inglese: contenuti pensati per chi cerca in inglese, non tradotti dal russo, con struttura e SEO tecnica curate dalla base (WordPress con flusso di deploy controllato). È anche il banco di prova dei nostri strumenti interni di audit SEO: sul nostro progetto testiamo prima quello che poi applichiamo ai vostri.",
        risultato="Oltre 10.000 visitatori al mese da 80 Paesi: un progetto che parla inglese a un pubblico realmente globale.",
        alt='Home page del progetto internazionale in inglese 1russian.com',
        cta_testo='Contenuti nativi in più lingue per il vostro sito', cta_href='/servizi/siti-multilingue/',
        shots=[dict(file='1russian-home-1440.jpg', mobile=False, caption='1russian.com — home page, primo schermo')],
    ),
]

CASES_BY_SLUG = {c['slug']: c for c in CASES}

# Sette strumenti gratuiti di /strumenti/ (Remarka Lab). Campo `tipo` = modulo
# JS del widget (speed|seo|a11y|co2|gdpr|ai|roi|checkup), letto dal generatore
# per rendere la markup corretta secondo il contratto data-* di remarka.js.
# `come_funziona`: 3 passi (titolo, testo). `faq`: 3 (domanda, risposta).
# `cta`: blocco finale scuro che rimanda al servizio a pagamento pertinente.
# Tono: numeri, «voi», disclaimer onesti (GDPR indicativo/non legale; ROI stima).
#
# 'check-up-completo' (tipo 'checkup', M2 — docs/piano-checkup-sito.md) è
# l'ottavo strumento, featured: orchestra le altre sette misure in un unico
# punteggio «Salute del sito». Testi presi alla lettera da
# docs/copy-checkup.md §2.2/§2.3 (fonte unica per M2/M3). Non ha 'migliorare'
# (build_tool tratta la chiave come opzionale per questo tipo).
TOOLS = [
    dict(slug='check-up-completo', idx='/00', tipo='checkup', titolo='Check-up completo',
         hero_titolo='Il check-up completo del vostro sito web',
         hero_sub='Sette strumenti gratuiti in una sola analisi. Incollate l’indirizzo: in meno di un minuto vedete un punteggio di salute da 0 a 100, i sette semafori che lo compongono e i tre interventi più urgenti. La misura è quella vera di Google PageSpeed Insights, affiancata dalle nostre verifiche su privacy e prontezza AI. Il report completo, pagina per pagina, ve lo inviamo in PDF.',
         descrizione='Sette strumenti gratuiti in una sola analisi.', has_demo=True,
         come_funziona=[
             ('Incollate l’indirizzo', 'La home o la pagina che porta più visite. Nessuna registrazione, nessun dato di pagamento.'),
             ('Analizziamo su sette fronti', 'Un’unica interrogazione all’API Google PageSpeed (prestazioni, SEO, accessibilità, best practice) più le nostre verifiche su privacy/cookie e prontezza AI, letti dal nostro server come farebbe un visitatore.'),
             ('Leggete il punteggio e le priorità', 'Salute 0–100, i sette semafori spiegati in italiano e i tre interventi che pesano di più. Il report completo arriva in PDF.'),
         ],
         faq=[
             ('Il punteggio è quello vero di Google?', 'Per prestazioni, SEO, accessibilità e best practice sì: arrivano dall’API ufficiale PageSpeed Insights, strategia mobile. Privacy, prontezza AI e CO₂ sono nostre verifiche, con il metodo dichiarato in ogni sezione.'),
             ('Il check-up GDPR sostituisce un consulente privacy?', 'No. È una verifica tecnica indicativa a quattro segnali: intercetta i problemi evidenti — banner assente, tracker prima del consenso — ma non è un parere legale e non sostituisce un consulente.'),
             ('Cosa ricevo nel report PDF che non vedo già a schermo?', 'A schermo vedete il punteggio, i sette semafori e le tre priorità. Nel PDF trovate una pagina per dimensione con tutte le criticità rilevate, le raccomandazioni operative in ordine di impatto e cosa faremmo noi, con i nostri riferimenti aziendali.'),
         ],
         metodologia=('Che cosa misura davvero il check-up completo', [
             'Dietro il punteggio non c’è una scatola nera. Quattro delle sette dimensioni — prestazioni, SEO, accessibilità e best practice — arrivano dall’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev: interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Le altre tre le calcoliamo noi: la conformità privacy la leggiamo dall’HTML della pagina (banner, informative, tracker prima del consenso), la prontezza AI da quattro segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e l’impronta di CO₂ dal peso reale della pagina, con il modello Sustainable Web Design.',
             'Ogni dimensione entra nel voto con un peso dichiarato: le prestazioni valgono di più (25 su 100), la CO₂ di meno (5). È giusto sapere anche cosa il check-up non fa: non è un parere legale sulla privacy — è una verifica indicativa a quattro segnali — e non promette una posizione su Google. È la fotografia tecnica precisa del vostro sito, non una promessa di vendita.',
         ]),
         lettura=('Come si legge lo stato di salute del sito', [
             'Il punteggio di salute è la media pesata dei sette semafori, non un voto a sensazione. Si legge come un semaforo: da 90 in su siete in fascia verde (eccellente), da 75 a 89 è buono, tra 50 e 74 c’è margine concreto, sotto 50 è critico e diventa la priorità. Ogni dimensione porta lo stesso codice colore, così capite in un colpo d’occhio dove il sito è solido e dove perde punti.',
             'Due letture da evitare. Un voto alto non significa «primi su Google»: significa che le fondamenta tecniche sono sane. E se una misura risulta «N/D» non è un guasto del vostro sito: a volte Google è saturo, a volte il sito rifiuta la lettura automatica. In quel caso calcoliamo la salute sulle misure riuscite e ve lo diciamo con chiarezza.',
         ]),
         cta=dict(heading='Vogliamo sistemare noi le priorità?',
                  testo='Dal punteggio al preventivo: analizziamo il report insieme e vi diamo un piano d’intervento a prezzo chiuso, con PageSpeed 90+ garantito da contratto.',
                  buttons=[('Richiedi la consulenza — gratis', '/#contatti', None),
                           ('Vedi tutti gli strumenti', '/strumenti/', 'outline')])),
    dict(slug='test-velocita', idx='/01', tipo='speed', titolo='Test velocità',
         hero_titolo='Test velocità sito web: il punteggio reale di Google',
         hero_sub='Punteggio Google PageSpeed e le tre metriche che lo determinano — LCP, INP, CLS — spiegate in italiano. Strategia mobile, dati reali dall’API di Google. Senza registrazione.',
         descrizione='Il PageSpeed reale del vostro sito, spiegato in italiano.', has_demo=True,
         come_funziona=[
             ('Incollate l’indirizzo', 'Scrivete l’URL del sito: la home o la pagina interna che porta più visite.'),
             ('Misuriamo con Google', 'Interroghiamo l’API PageSpeed Insights in strategia mobile — gli stessi dati che Google usa per il posizionamento.'),
             ('Leggete cosa frena il sito', 'Punteggio 0–100 e le tre metriche Core Web Vitals spiegate in italiano, senza gergo tecnico.'),
         ],
         faq=[
             ('Il punteggio è quello vero di Google?', 'Sì: arriva dall’API ufficiale PageSpeed Insights, strategia mobile. È lo stesso motore che trovate su pagespeed.web.dev.'),
             ('Perché misurate solo il mobile?', 'Perché Google indicizza e classifica in base alla versione mobile del sito. Il punteggio desktop, più alto quasi ovunque, conta poco per il posizionamento.'),
             ('Un punteggio basso danneggia le vendite?', 'Sotto i 50, gran parte dei visitatori da mobile abbandona prima del caricamento completo: le campagne portano clic che non diventano richieste.'),
         ],
         metodologia=('Cosa misura davvero questo test dei tempi di caricamento', [
             'Dietro il punteggio c’è un motore solo: l’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev. Interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Il numero da 0 a 100 nasce in laboratorio, con un telefono e una connessione simulati e standardizzati: così due misurazioni della stessa pagina restano confrontabili nel tempo. Dove il vostro sito riceve abbastanza traffico reale, aggiungiamo anche i Core Web Vitals raccolti sul campo dagli utenti veri di Chrome.',
             'È giusto sapere cosa questo test non guarda. Non giudica la qualità dei testi, non conta i link in entrata, non misura la sicurezza del server né quanto vendete: pesa solo l’esperienza di caricamento di una singola pagina. Un punteggio alto non è la promessa di un primo posto su Google, ma una base tecnica sana su cui tutto il resto lavora meglio. Preferiamo dirlo chiaro: è la fotografia precisa di un aspetto, non la diagnosi completa del sito.',
         ]),
         lettura=('Come leggere il punteggio delle prestazioni del sito', [
             'Il risultato si legge come un semaforo. Da 90 a 100 siete in fascia verde: la pagina compare in fretta anche in mobilità, sul 4G di città come ai bordi della copertura. Tra 50 e 89 la velocità è nella media del web italiano, con margini concreti di guadagno. Sotto 50 siete nel rosso: buona parte dei visitatori da smartphone se ne va prima che appaia la prima riga, e ogni euro investito in pubblicità rende molto meno.',
             'Due falsi allarmi ricorrenti. Il valore oscilla di qualche punto tra una prova e l’altra: è normale, dipende dai server di misura di Google, non dal vostro sito — contano i grandi salti, non i due punti di scarto. E non spaventatevi se il desktop segna 95 e il mobile 40: quasi tutti i siti hanno questo divario, ma è il mobile a decidere la classifica. Guardate sempre quel numero.',
         ]),
         migliorare=dict(h2='Come velocizzare il sito web: cinque interventi concreti',
             intro='Un punteggio basso nasce quasi sempre dalle stesse cause, e le prime sono anche le più economiche da correggere.',
             punti=[
                 ('Alleggerite le immagini', 'Convertite le fotografie in WebP o AVIF e attivate il caricamento differito: è la causa numero uno della lentezza e spesso, da sola, dimezza i tempi di attesa.'),
                 ('Attivate la cache', 'Una cache di pagina e del browser evita al server di ricostruire tutto a ogni visita: mezza giornata di lavoro, risultato misurabile da subito.'),
                 ('Sfoltite CSS e JavaScript', 'Portate in linea il CSS critico, rimandate il resto e togliete gli script di terze parti che non servono: meno codice da eseguire, prima visualizzazione più rapida.'),
                 ('Scegliete un hosting all’altezza', 'Un server condiviso e sovraffollato risponde in un secondo prima ancora di iniziare: un hosting adeguato, con una CDN davanti, taglia quell’attesa iniziale.'),
                 ('Controllate i font', 'Limitate le famiglie di caratteri, precaricate quelle essenziali e usate font-display swap, così il testo appare subito invece di restare invisibile.'),
             ],
             links=[
                 ('Vogliamo intervenire noi: scopri il restyling tecnico', '/servizi/restyling-migrazione/'),
                 ('Approfondisci: le 7 cause reali di un sito lento', '/blog/sito-lento-cause-costi/'),
             ]),
         cta=dict(heading='Vogliamo sistemare noi questi problemi?',
                  testo='Report gratuito con le cause, le priorità e un preventivo chiuso: PageSpeed 90+ garantito da contratto.',
                  buttons=[('Richiedi l’analisi completa', '/#contatti', None),
                           ('Scopri la SEO tecnica', '/servizi/seo-tecnica/', 'outline')])),
    dict(slug='analisi-seo', idx='/02', tipo='seo', titolo='Analisi SEO on-page',
         hero_titolo='Analisi SEO on-page: cosa vede Google sulla vostra pagina',
         hero_sub='Titolo, struttura dei contenuti e dati mancanti sulla pagina che conta di più per il vostro business. Punteggio SEO di Google e le correzioni concrete, in italiano. Senza registrazione.',
         descrizione='Titoli, struttura e dati mancanti sulla pagina che conta di più.', has_demo=False,
         come_funziona=[
             ('Scegliete la pagina giusta', 'Non per forza la home: la pagina che deve posizionarsi — un servizio, una scheda, un articolo.'),
             ('Google la analizza', 'Usiamo la categoria SEO di Lighthouse via API PageSpeed: titoli, meta description, tag, link e struttura.'),
             ('Vedete cosa correggere', 'Punteggio 0–100 e la lista degli elementi on-page da sistemare, in ordine di priorità.'),
         ],
         faq=[
             ('Questa analisi fa posizionare il sito?', 'Da sola no: verifica le basi tecniche on-page (titoli, struttura, dati). Il posizionamento dipende anche da contenuti e autorevolezza, che richiedono tempo.'),
             ('Che differenza c’è con l’analisi dei contenuti?', 'Qui controlliamo la parte tecnica della pagina, quella che Google legge. La qualità dei testi è un lavoro separato, che facciamo con copywriter partner.'),
             ('Analizza tutto il sito?', 'No: una pagina alla volta, quella che indicate. È l’unità su cui Google valuta la pertinenza per una ricerca.'),
         ],
         metodologia=('Che cosa controlla davvero l’audit SEO della pagina', [
             'Anche qui il motore è Google: usiamo la categoria SEO di Lighthouse attraverso l’API PageSpeed, in strategia mobile. In pochi secondi Lighthouse legge la pagina come farebbe il crawler e verifica gli elementi tecnici on-page: presenza e unicità del title, meta description, tag corretti, testi dei link descrittivi, indicizzabilità, leggibilità sullo schermo del telefono. Ne esce un punteggio da 0 a 100 con l’elenco puntuale di ciò che non supera il controllo.',
             'Vale la pena chiarire i confini. Questo esame guarda la struttura tecnica di una singola pagina, non la qualità dei contenuti, non i link che altri siti vi dedicano, non l’autorevolezza che si costruisce nel tempo. Non prevede in che posizione finirete, né studia la concorrenza sulle vostre parole chiave. È il controllo delle fondamenta: se sono storte, nemmeno il testo migliore rende; se sono a posto, avete tolto di mezzo gli ostacoli tecnici.',
         ]),
         lettura=('Come interpretare il punteggio SEO di Google', [
             'Da 90 in su le basi tecniche sono in ordine e potete concentrarvi su contenuti e reputazione. Tra 50 e 89 restano correzioni concrete — spesso un title mancante o una description duplicata — che si sistemano in fretta. Sotto 50 c’è qualcosa che ostacola l’indicizzazione: è la priorità, prima di ogni altra cosa. Leggete la lista degli avvisi dall’alto verso il basso: è già ordinata per impatto.',
             'Attenzione a due letture sbagliate. Un punteggio pieno non vuol dire «primi su Google»: significa solo che la pagina è tecnicamente leggibile, e il posizionamento arriva con contenuti e tempo. E un avviso su un tag secondario non è un’emergenza: distinguete i problemi che bloccano l’indicizzazione da quelli cosmetici, e partite dai primi.',
         ]),
         migliorare=dict(h2='Come migliorare il posizionamento on-page',
             intro='La SEO tecnica on-page è fatta di poche cose fatte bene, ripetute su ogni pagina che conta.',
             punti=[
                 ('Un title e una description su misura', 'Scrivete per ogni pagina un titolo unico e descrittivo e una meta description che invita al clic: sono la prima cosa che vede chi cerca.'),
                 ('Una gerarchia di titoli pulita', 'Un solo H1, poi H2 e H3 ordinati per argomento: aiutano Google e i lettori a capire la struttura della pagina in un colpo d’occhio.'),
                 ('Aggiungete i dati strutturati', 'Il markup schema.org in JSON-LD dice ai motori chi siete e cosa offrite, e vi rende idonei ai risultati arricchiti.'),
                 ('Curate link interni e URL', 'Collegate le pagine tra loro con testi di ancoraggio chiari e mantenete indirizzi brevi e leggibili: la struttura conta quanto il contenuto.'),
                 ('Tenete in ordine sitemap e robots', 'Una sitemap XML aggiornata e un robots.txt corretto guidano il crawler; se il sito è in più lingue, aggiungete i tag hreflang.'),
             ],
             links=[
                 ('Vogliamo sistemarla noi: scopri la SEO tecnica', '/servizi/seo-tecnica/'),
                 ('Approfondisci: i Core Web Vitals nel 2026', '/blog/core-web-vitals-2026/'),
                 ('Verificate anche i segnali di fiducia E-E-A-T', '/strumenti/segnali-eeat/'),
             ]),
         cta=dict(heading='Vogliamo sistemare noi la SEO tecnica?',
                  testo='Audit completo, dati strutturati e Core Web Vitals a posto: PageSpeed 90+ garantito da contratto.',
                  buttons=[('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None),
                           ('Verifica se il sito è pronto per l’AI', '/strumenti/sito-pronto-ai/', 'outline')])),
    dict(slug='check-gdpr', idx='/03', tipo='gdpr', titolo='Check GDPR e cookie',
         hero_titolo='Il vostro sito è a norma GDPR?',
         hero_sub='Controlliamo banner cookie, informative e tracker attivi prima del consenso: quattro verifiche per capire cosa manca. È una verifica indicativa, non una consulenza legale.',
         descrizione='Banner, informative e consensi: cosa manca per essere a norma.', has_demo=False,
         come_funziona=[
             ('Inserite l’indirizzo del sito', 'Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura.'),
             ('Quattro controlli automatici', 'Cerchiamo il cookie banner (CMP), i link a privacy e cookie policy, i tracker caricati prima del consenso e i domini esterni.'),
             ('Semaforo, non sentenza', 'Ogni punto è verde, giallo o rosso: segnaliamo i problemi evidenti, non un audit legale completo.'),
         ],
         faq=[
             ('È un parere legale?', 'No, ed è importante dirlo: è una verifica automatica indicativa, non una consulenza legale. Segnala i problemi tecnici evidenti; la conformità piena va valutata da un consulente privacy.'),
             ('Cosa vuol dire «tracker senza banner»?', 'Che nell’HTML iniziale della pagina troviamo strumenti di tracciamento (Google Analytics, Meta Pixel e simili) attivi prima che l’utente accetti. È il segnale rosso più frequente sui siti italiani.'),
             ('Perché il Garante è così severo sui cookie?', 'Perché il consenso deve essere libero, informato e documentabile: rifiutare deve essere facile quanto accettare, e nessun tracker pubblicitario può partire prima del sì.'),
         ],
         metodologia=('Cosa verifica davvero questo controllo cookie', [
             'A differenza dei test basati su Google, qui è il nostro server a leggere la home page del vostro sito, esattamente come la vedrebbe un visitatore alla prima apertura, prima di qualsiasi clic. Su quell’HTML facciamo quattro controlli automatici: cerchiamo il banner dei cookie (la CMP: Iubenda, Cookiebot, Complianz e simili), i collegamenti a privacy e cookie policy, gli strumenti di tracciamento che partono prima del consenso e i domini esterni che la pagina richiama.',
             'Diciamolo subito, perché conta: non è un parere legale. È una verifica tecnica indicativa, che intercetta i problemi evidenti — quelli che il Garante contesta più spesso — ma non sostituisce un consulente privacy. Non legge cosa accade dopo che l’utente accetta, non valuta i vostri registri dei consensi, non esamina le informative riga per riga. È un ottimo punto di partenza per capire dove intervenire, non un certificato di conformità.',
         ]),
         lettura=('Come leggere il semaforo di conformità', [
             'Ogni punto riceve un colore, e il colore va preso per quello che è. Verde: il segnale è presente e a posto. Giallo: qualcosa c’è ma va verificato a mano — per esempio una policy che esiste ma potrebbe essere incompleta. Rosso: manca un elemento importante o, peggio, ci sono tracker attivi senza un banner che li governi. Il quadro d’insieme conta più del singolo pallino.',
             'Il rosso più frequente sui siti italiani è «tracker senza banner»: Google Analytics o il Pixel di Meta che si attivano nell’HTML iniziale, prima del sì dell’utente. È anche l’errore che il Garante sanziona con più decisione. Un giallo, invece, di solito non è un’emergenza: spesso basta completare o aggiornare un’informativa già presente.',
         ]),
         migliorare=dict(h2='Come mettere a norma il consenso e i cookie',
             intro='La conformità pratica si costruisce con pochi accorgimenti, ma vanno rispettati tutti.',
             punti=[
                 ('Installate una CMP che blocca davvero', 'Un banner serio non deve solo comparire: deve impedire ai tracker di partire finché l’utente non ha accettato. È la differenza tra sembrare a norma ed esserlo.'),
                 ('Rendete il rifiuto facile quanto l’assenso', 'Il pulsante «Rifiuta» deve avere lo stesso peso di «Accetta», sulla stessa schermata: niente cookie wall, niente percorsi a ostacoli per dire di no.'),
                 ('Pubblicate informative complete', 'Privacy policy e cookie policy chiare, aggiornate e facili da trovare: devono dire cosa raccogliete, perché e con chi lo condividete.'),
                 ('Rendete il consenso documentabile', 'Conservate la prova di ogni consenso — quando, per cosa — così da poterla mostrare se richiesto: il sì deve essere libero, informato e tracciabile.'),
                 ('Caricate i tracker dopo il sì', 'Analytics, pixel e mappe di calore vanno attivati solo dopo l’accettazione, in modo condizionato: prima del consenso la pagina deve restare pulita.'),
             ],
             links=[
                 ('Lo includiamo in ogni sito aziendale che consegniamo', '/servizi/siti-aziendali/'),
                 ('Approfondisci: la checklist cookie 2026 del Garante', '/blog/cookie-banner-checklist-garante-2026/'),
             ]),
         cta=dict(heading='Vogliamo mettere il sito a norma?',
                  testo='Banner, informative e consensi conformi al Garante, inclusi in ogni sito aziendale che consegniamo.',
                  buttons=[('Scopri i siti aziendali', '/servizi/siti-aziendali/', None),
                           ('Richiedi un’analisi', '/#contatti', 'outline')])),
    dict(slug='roi-localizzazione', idx='/04', tipo='roi', titolo='ROI localizzazione',
         hero_titolo='Quanto rende tradurre il vostro sito',
         hero_sub='Una stima di quanto potreste guadagnare traducendo il sito in inglese o tedesco: bastano cinque numeri della vostra attività. Il calcolo resta sul vostro dispositivo. È una stima, non una promessa.',
         descrizione='Quanto rende tradurre il sito in inglese o tedesco.', has_demo=False,
         come_funziona=[
             ('Inserite i vostri numeri', 'Visite mensili, quota di pubblico estero, tasso di conversione, scontrino medio. Se non li avete precisi, partite dalle stime.'),
             ('Applichiamo il boost di localizzazione', 'Sul pubblico estero applichiamo un incremento prudente di conversione (+40%), dai dati CSA Research sull’acquisto in lingua madre.'),
             ('Leggete il ricavo potenziale', 'Il calcolatore mostra il ricavo aggiuntivo stimato al mese e all’anno. Cambiate i numeri e vedete subito come si muove.'),
         ],
         faq=[
             ('Da dove viene il «+40%»?', 'Dalle ricerche CSA Research: la larga maggioranza dei consumatori compra più volentieri, e più spesso, nella propria lingua. Il 40% è un valore prudente, che potete modificare.'),
             ('È una previsione garantita?', 'No: è una stima per ordini di grandezza, utile a capire se vale la pena approfondire. I risultati reali dipendono dal mercato, dall’offerta e dalla qualità della traduzione.'),
             ('Perché tradurre da madrelingua e non con un plugin?', 'Perché un cliente estero riconosce un testo automatico alla seconda riga — e con lui se ne va la fiducia. Nel gruppo Remarka la traduzione la fanno madrelingua, dal 2001.'),
         ],
         metodologia=('Come funziona davvero questa stima del ROI', [
             'Questo strumento non interroga alcun server e non guarda il vostro sito: è un calcolatore che gira interamente sul vostro dispositivo, e i numeri che inserite non lasciano il browser. Prende cinque dati della vostra attività — visite mensili, quota di pubblico estero, tasso di conversione, scontrino medio — e li combina con un incremento di conversione applicato alla sola fetta di visitatori stranieri.',
             'Quell’incremento, un prudente +40%, viene dalle ricerche CSA Research: la larga maggioranza delle persone compra più volentieri, e più spesso, nella propria lingua. È un valore di partenza, non una legge fisica: potete modificarlo. E qui sta anche il limite onesto dello strumento — è una stima per ordini di grandezza, non una previsione garantita. Non conosce il vostro mercato, la vostra offerta né la qualità della traduzione, che sono poi ciò che fa la differenza vera.',
         ]),
         lettura=('Come interpretare il ricavo potenziale stimato', [
             'Il risultato va letto come una forchetta, non come una cifra al centesimo. Serve a rispondere a una sola domanda: vale la pena approfondire la traduzione del sito, sì o no? Se il ricavo aggiuntivo stimato all’anno copre comodamente il costo di un progetto multilingue, il segnale è chiaro. Se è modesto, forse il vostro pubblico estero è ancora troppo piccolo perché l’investimento si ripaghi in fretta.',
             'Muovete i numeri e osservate come reagisce la stima: è lì che il calcolatore diventa utile. Alzando la quota di visitatori esteri o lo scontrino medio, il ricavo cresce in fretta, e questo vi dice quali leve pesano di più nel vostro caso. Ricordate che tutto parte dalle vostre cifre: se sono ottimistiche, lo sarà anche il risultato. Meglio partire da stime prudenti.',
         ]),
         migliorare=dict(h2='Come aumentare il rendimento della traduzione',
             intro='Tradurre un sito rende, ma solo se è fatto per vendere e non per figurare.',
             punti=[
                 ('Traducete da madrelingua, non con un plugin', 'Un cliente estero riconosce un testo automatico alla seconda riga, e con lui se ne va la fiducia. La traduzione professionale è ciò che trasforma la visita in ordine.'),
                 ('Localizzate, non solo tradurre', 'Adattate offerta, inviti all’azione, valuta e formati al mercato di arrivo: vendere in Germania non è tradurre le schede, è parlare come parla quel mercato.'),
                 ('Impostate la SEO internazionale', 'Ogni lingua ha bisogno dei suoi URL, dei tag hreflang e dei metadati dedicati, altrimenti Google non capisce a chi mostrare quale versione.'),
                 ('Partite dal mercato con più domanda', 'Non tutte le lingue rendono uguale: cominciate da dove i dati mostrano già interesse, poi allargate mercato per mercato.'),
                 ('Curate anche il dopo-vendita', 'Moduli, email di conferma e assistenza nella lingua del cliente: la fiducia si conferma dopo l’acquisto, non solo prima.'),
             ],
             links=[
                 ('Vogliamo tradurlo sul serio: scopri i siti multilingue', '/servizi/siti-multilingue/'),
                 ('Approfondisci: costi e tempi di un sito in quattro lingue', '/blog/sito-quattro-lingue-costi-tempi/'),
             ]),
         cta=dict(heading='Vogliamo tradurre il sito sul serio?',
                  testo='Traduzione professionale da madrelingua e SEO internazionale corretta dal primo giorno — non un plugin.',
                  buttons=[('Siti multilingue', '/servizi/siti-multilingue/', None),
                           ('Export Ready', '/servizi/export-ready/', 'outline')])),
    dict(slug='verifica-accessibilita', idx='/05', tipo='a11y', titolo='Verifica accessibilità',
         hero_titolo='Verifica accessibilità: il vostro sito è usabile da tutti?',
         hero_sub='Controlliamo con Google le barriere di accessibilità più comuni — contrasti, etichette, struttura. Dal 28 giugno 2025 l’European Accessibility Act rende l’accessibilità un obbligo per molti siti. Senza registrazione.',
         descrizione='Le barriere di accessibilità più comuni, misurate con Google.', has_demo=False,
         come_funziona=[
             ('Inserite l’indirizzo', 'La pagina da controllare: la home o una pagina di servizio, dove passano più utenti.'),
             ('Analisi Lighthouse', 'Usiamo la categoria Accessibilità di Lighthouse via API PageSpeed: contrasti, testi alternativi, etichette dei moduli, struttura dei titoli.'),
             ('Vedete le barriere da rimuovere', 'Punteggio 0–100 e la lista dei problemi rilevati, in italiano. Un controllo automatico copre parte dei criteri WCAG, non tutti.'),
         ],
         faq=[
             ('Cos’è l’European Accessibility Act?', 'Una direttiva europea (EAA) applicata in Italia dal 28 giugno 2025: molti siti di aziende che vendono a consumatori devono essere accessibili secondo lo standard WCAG 2.1 livello AA. È un obbligo, con alcune esenzioni per le microimprese.'),
             ('Questo test basta per essere conformi?', 'No: un controllo automatico intercetta una parte dei criteri WCAG. La conformità piena richiede anche verifica manuale — navigazione da tastiera, screen reader, contenuti. È un ottimo punto di partenza, non un certificato.'),
             ('Riguarda anche la mia azienda?', 'Se vendete beni o servizi a consumatori online (e-commerce, banche, trasporti, servizi), con ogni probabilità sì. Le microimprese che offrono servizi hanno esenzioni: meglio verificare caso per caso.'),
         ],
         metodologia=('Cosa controlla davvero questo test di accessibilità', [
             'Il motore è la categoria Accessibilità di Lighthouse, richiamata via API PageSpeed: gli stessi controlli automatici che Google mette a disposizione degli sviluppatori. In pochi secondi la pagina viene esaminata su decine di regole tecniche — contrasto tra testo e sfondo, testi alternativi delle immagini, etichette dei campi nei moduli, ordine dei titoli, uso corretto degli attributi ARIA — e ne esce un punteggio da 0 a 100 con l’elenco delle barriere rilevate.',
             'Serve chiarezza sui limiti, perché qui è facile illudersi. Un controllo automatico intercetta soltanto una parte dei criteri WCAG 2.1 AA: cattura ciò che una macchina sa misurare, non ciò che va provato da una persona. Non verifica la navigazione da tastiera, l’esperienza con uno screen reader, la chiarezza dei contenuti per chi ha difficoltà cognitive. È il primo gradino verso la conformità richiesta dall’European Accessibility Act, non il certificato finale.',
         ]),
         lettura=('Come leggere il punteggio e le barriere rilevate', [
             'Il numero da 0 a 100 dice quanto la pagina supera i controlli automatici: più è alto, meno ostacoli evidenti restano. Ma il punteggio conta meno dell’elenco che lo accompagna. Ogni voce è una barriera concreta per una persona reale — un contrasto troppo debole per chi ci vede poco, un pulsante senza etichetta per chi usa uno screen reader. Partite da quelle, non dal totale.',
             'Un avvertimento sui falsi sensi di sicurezza: anche un 100 pieno non significa «sito conforme». Vuol dire che avete superato i test che una macchina può fare, e sono circa un terzo dei problemi possibili. Il resto — tastiera, lettori di schermo, contenuti — si verifica a mano. Prendete quindi un punteggio alto come una buona base, non come un traguardo raggiunto.',
         ]),
         migliorare=dict(h2='Come rendere il sito accessibile a tutti',
             intro='Molte barriere cadono con correzioni semplici, che migliorano l’esperienza di chiunque, non solo di chi ha una disabilità.',
             punti=[
                 ('Aumentate il contrasto', 'Testo e sfondo devono avere un rapporto di contrasto di almeno 4,5:1: il grigio chiaro elegante sullo schermo del designer diventa illeggibile al sole o per chi ci vede poco.'),
                 ('Descrivete le immagini', 'Ogni immagine informativa ha bisogno di un testo alternativo che ne racconti il contenuto: è ciò che uno screen reader legge a chi non può vederla.'),
                 ('Etichettate i moduli', 'Ogni campo deve avere un’etichetta esplicita e collegata: «Nome», «Email», «Messaggio», non solo un testo grigio che sparisce appena si scrive.'),
                 ('Ordinate titoli e focus', 'Una gerarchia di titoli coerente e un percorso navigabile da tastiera, con il focus sempre visibile, rendono la pagina usabile anche senza mouse.'),
                 ('Non affidatevi solo al colore', 'Un errore segnalato solo in rosso è invisibile a chi non distingue i colori: affiancate sempre un’icona o un testo che spieghi cosa succede.'),
             ],
             links=[
                 ('Vogliamo sistemarle noi: audit, correzioni e dichiarazione — servizio Adeguamento EAA', '/servizi/adeguamento-eaa/'),
                 ('Approfondisci: EAA 2026, cosa rischia davvero il vostro e-commerce', '/blog/european-accessibility-act-ecommerce/'),
                 ('Guida pratica: la dichiarazione di accessibilità nel 2026', '/blog/dichiarazione-di-accessibilita-guida-2026/'),
             ]),
         cta=dict(heading='Vogliamo rendere il sito accessibile?',
                  testo='Verifichiamo le barriere una per una — automatiche e manuali — e le sistemiamo secondo lo standard WCAG 2.1 AA.',
                  buttons=[('Richiedi una verifica di accessibilità', '/#contatti', None),
                           ('Scopri il servizio Adeguamento EAA', '/servizi/adeguamento-eaa/', 'outline')])),
    dict(slug='sito-pronto-ai', idx='/06', tipo='ai', titolo='Sito pronto per l’AI',
         hero_titolo='Il vostro sito è pronto per l’AI?',
         hero_sub='Quando ChatGPT, Claude o Perplexity leggono il web, trovano il vostro sito? Controlliamo quattro segnali: llms.txt, accesso dei crawler AI, dati strutturati e sitemap. Senza registrazione.',
         descrizione='llms.txt, crawler AI, dati strutturati e sitemap: quattro segnali.', has_demo=False,
         come_funziona=[
             ('Inserite l’indirizzo del sito', 'Leggiamo dal nostro server alcuni file pubblici e l’HTML della home page.'),
             ('Quattro verifiche', 'Cerchiamo il file llms.txt, controlliamo se robots.txt lascia passare i crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.'),
             ('Punteggio N su 4', 'Un semaforo per ogni segnale e un punteggio complessivo, con le indicazioni su cosa aggiungere per farsi trovare e citare dai modelli.'),
         ],
         faq=[
             ('Cos’è il file llms.txt?', 'Una proposta di standard: un file di testo in Markdown che riassume ai modelli AI cosa contiene il sito e come citarlo, come fa robots.txt per i motori di ricerca. È giovane, ma sempre più diffuso.'),
             ('Conviene far entrare i crawler AI?', 'Dipende dagli obiettivi: bloccarli protegge i contenuti, ma vi esclude dalle risposte generate. Per la maggior parte delle aziende, essere citati da ChatGPT o Perplexity è visibilità in più.'),
             ('I dati strutturati servono ancora?', 'Sì, più che mai: i dati JSON-LD (schema.org) aiutano sia Google sia i modelli AI a capire chi siete, cosa offrite e a chi. Sono la base di ogni buona indicizzazione.'),
         ],
         metodologia=('Cosa verifica davvero questo controllo di prontezza AI', [
             'Come per il controllo GDPR, è il nostro server a leggere alcuni file pubblici del vostro sito e l’HTML della home, senza passare da Google. Facciamo quattro verifiche: cerchiamo il file llms.txt, controlliamo se il robots.txt lascia passare i crawler dei modelli (GPTBot di OpenAI, ClaudeBot, PerplexityBot, Google-Extended), rileviamo i dati strutturati JSON-LD nella pagina e la presenza di una sitemap. Ne esce un punteggio di prontezza su quattro.',
             'È utile sapere cosa il test non promette. Verifica che i segnali tecnici ci siano, non che ChatGPT o Perplexity vi citino davvero: quello dipende anche dalla qualità e dall’autorevolezza dei contenuti, che nessuno strumento misura in automatico. E poiché llms.txt è uno standard giovane, la sua assenza non è ancora un errore grave: è un’occasione in più di farsi leggere bene dalle macchine. Leggete il punteggio come una lista di opportunità, non come una bocciatura.',
         ]),
         lettura=('Come leggere il punteggio di prontezza su 4', [
             'Ogni segnale vale un punto e ha il suo semaforo. Quattro su quattro significa che il sito offre alle intelligenze artificiali tutti gli appigli per capirlo e citarlo. Due o tre su quattro è la situazione più comune: manca quasi sempre llms.txt, a volte i dati strutturati. Zero o uno su quattro merita attenzione, soprattutto se il robots.txt blocca i crawler AI: in quel caso restate fuori dalle risposte generate, magari senza averlo deciso.',
             'Una precisazione che evita allarmi inutili. Bloccare i crawler AI non è un difetto in sé: è una scelta legittima, se volete proteggere i contenuti. Il test lo segnala perché sappiate che quella porta è chiusa, non per dirvi che sbagliate. Per la maggior parte delle aziende, però, essere citati da un assistente AI è visibilità in più, non un rischio: vale la pena valutarlo con consapevolezza.',
         ]),
         migliorare=dict(h2='Come farsi trovare e citare dai modelli AI',
             intro='Prepararsi all’AI non richiede stravolgimenti: sono gli stessi segnali che aiutano anche Google, più qualche novità.',
             punti=[
                 ('Pubblicate un file llms.txt', 'Un semplice file di testo in Markdown, nella radice del sito, che riassume chi siete e cosa offrite: è la mappa che i modelli leggono volentieri.'),
                 ('Aprite le porte ai crawler giusti', 'Nel robots.txt consentite l’accesso a GPTBot, ClaudeBot, PerplexityBot e Google-Extended, se volete comparire nelle risposte generate.'),
                 ('Aggiungete i dati strutturati', 'Il markup JSON-LD schema.org dice in modo esplicito nome, sede, offerta e servizi: è la base che sia Google sia le AI usano per capirvi.'),
                 ('Tenete la sitemap aggiornata', 'Una sitemap XML completa aiuta i crawler a trovare tutte le pagine; assicuratevi che i contenuti siano testo leggibile, non solo immagini.'),
                 ('Scrivete fatti espliciti', 'Dichiarate con chiarezza cosa fate, dove e per chi: i modelli citano ciò che capiscono senza ambiguità, non ciò che devono indovinare.'),
             ],
             links=[
                 ('Lo prepariamo noi: fa parte della SEO tecnica', '/servizi/seo-tecnica/'),
                 ('Approfondisci: llms.txt, cos’è e serve davvero al vostro sito', '/blog/llms-txt-cos-e/'),
                 ('Guida: come farsi trovare e citare da ChatGPT (GEO)', '/blog/farsi-trovare-da-chatgpt-geo/'),
                 ('Misurate anche i segnali di fiducia E-E-A-T del sito', '/strumenti/segnali-eeat/'),
                 ('Manca l’llms.txt? Createlo qui in un minuto', '/strumenti/generatore-llms-txt/'),
                 ('Volete sapere come l’AI legge davvero il vostro sito?', '/strumenti/sito-letto-dallai/'),
             ]),
         cta=dict(heading='Vogliamo preparare il sito per l’AI?',
                  testo='Dati strutturati, file corretti e struttura leggibile dalle macchine: fa parte della SEO tecnica che consegniamo.',
                  buttons=[('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None),
                           ('Analizza la SEO on-page', '/strumenti/analisi-seo/', 'outline')])),
    dict(slug='impatto-co2', idx='/07', tipo='co2', titolo='Impatto CO₂',
         hero_titolo='Impatto CO₂ del vostro sito web',
         hero_sub='Ogni visita al sito consuma energia e produce CO₂. Misuriamo il peso della vostra pagina e stimiamo le emissioni per visita e all’anno, con il modello Sustainable Web Design. Un sito leggero è anche un sito veloce.',
         descrizione='Quanta CO₂ produce ogni visita — e quanta all’anno.', has_demo=False,
         come_funziona=[
             ('Inserite l’indirizzo', 'La pagina da misurare: di solito la home, la più visitata.'),
             ('Pesiamo la pagina', 'Con l’API PageSpeed misuriamo i byte totali che il browser deve scaricare per mostrare la pagina.'),
             ('Stima delle emissioni', 'Applichiamo il modello Sustainable Web Design (co2.js) e otteniamo i grammi di CO₂e per visita, il confronto con la media del web e la stima annua.'),
         ],
         faq=[
             ('Come calcolate le emissioni?', 'Con il modello Sustainable Web Design della Green Web Foundation (libreria co2.js, Apache-2.0): dal peso della pagina all’energia consumata, fino ai grammi di CO₂e. È una stima con coefficienti medi mondiali.'),
             ('Perché un sito leggero inquina meno?', 'Perché ogni byte trasferito consuma energia — nel data center, nella rete, sul vostro dispositivo. Meno peso significa meno energia, meno emissioni e, come effetto collaterale, un sito più veloce.'),
             ('La stima annua da dove viene?', 'Moltiplichiamo le emissioni per visita per un traffico di riferimento di 10.000 visite al mese. Cambiando il traffico reale del vostro sito, cambia la stima proporzionalmente.'),
         ],
         metodologia=('Come stimiamo davvero le emissioni della pagina', [
             'Il calcolo parte da un dato concreto e misurabile: con l’API PageSpeed pesiamo tutti i byte che il browser deve scaricare per mostrare la vostra pagina. Su quel peso applichiamo il modello Sustainable Web Design della Green Web Foundation — le stesse formule della libreria open source co2.js — che traduce i byte trasferiti in energia consumata lungo la catena (data center, rete, dispositivo) e infine in grammi di CO₂ equivalente per visita.',
             'È una stima, ed è giusto trattarla come tale. Il modello usa coefficienti medi mondiali per l’intensità energetica e per il mix elettrico: non conosce l’energia reale del vostro hosting né il comportamento esatto di ogni visitatore. Non è una misura certificata di impronta ambientale, ma un ordine di grandezza affidabile e confrontabile. Il pregio è che si lega a un fatto tecnico — il peso — su cui potete davvero intervenire.',
         ]),
         lettura=('Come leggere i grammi di CO₂ per visita', [
             'Il numero chiave è la CO₂ equivalente per singola visita, che confrontiamo con la media del web, intorno agli 0,8 grammi. Sotto quella soglia siete tra i siti leggeri; sensibilmente sopra, la pagina è più pesante della media e c’è margine per alleggerirla. La stima annua moltiplica quel valore per un traffico di riferimento: cambiando le visite reali del vostro sito, l’impatto cresce o cala in proporzione.',
             'Il confronto conta più del valore assoluto. Pochi grammi per visita sembrano nulla, ma moltiplicati per decine di migliaia di visite al mese diventano una cifra concreta, e soprattutto sono lo specchio di una pagina pesante: quasi sempre chi inquina di più è anche chi carica più lentamente. Leggete quindi l’impatto come un secondo indicatore delle prestazioni, non solo come una questione ambientale.',
         ]),
         migliorare=dict(h2='Come ridurre l’impronta di carbonio del sito',
             intro='Ridurre le emissioni e velocizzare il sito sono la stessa cosa: entrambe passano dal tagliare peso inutile.',
             punti=[
                 ('Alleggerite le immagini', 'Le fotografie sono quasi sempre la voce più pesante: convertitele in WebP o AVIF con caricamento differito e taglierete gran parte dei byte, e quindi delle emissioni.'),
                 ('Riducete script e font', 'Ogni libreria di terze parti e ogni famiglia di caratteri in più è energia trasferita a ogni visita: tenete solo ciò che serve davvero.'),
                 ('Sfruttate cache e CDN', 'Una buona cache e una rete di distribuzione evitano di trasferire gli stessi contenuti mille volte: meno traffico ripetuto, meno consumo.'),
                 ('Scegliete un hosting verde', 'Un provider alimentato da energia rinnovabile abbassa l’intensità di carbonio di ogni byte servito: è la leva più semplice per un effetto immediato.'),
                 ('Preferite un design sobrio', 'Niente video in riproduzione automatica o animazioni pesanti dove non servono: un’estetica pulita consuma meno e, spesso, comunica meglio.'),
             ],
             links=[
                 ('Vogliamo alleggerirlo noi: scopri il restyling tecnico', '/servizi/restyling-migrazione/'),
                 ('Approfondisci: le 7 cause di un sito lento', '/blog/sito-lento-cause-costi/'),
                 ('Guida: quanto pesa il vostro sito sull’ambiente (e sul portafoglio)', '/blog/impatto-ambientale-sito-web/'),
             ]),
         cta=dict(heading='Vogliamo alleggerire il sito?',
                  testo='Immagini ottimizzate, base tecnica pulita, meno peso a parità di contenuti: meno CO₂ e PageSpeed 90+ da contratto.',
                  buttons=[('Restyling e migrazione', '/servizi/restyling-migrazione/', None),
                           ('Misura la velocità', '/strumenti/test-velocita/', 'outline')])),
    dict(slug='segnali-eeat', idx='/08', tipo='eeat', titolo='Segnali E-E-A-T',
         hero_titolo='Segnali E-E-A-T: quanto è credibile il vostro sito?',
         hero_sub='Analizziamo otto segnali di fiducia leggibili nel codice della vostra home — HTTPS, contatti, P.IVA, chi siamo, dati strutturati e altri — raggruppati nei quattro pilastri E-E-A-T. Misuriamo i segnali on-page, non la vostra reputazione o competenza reale. Senza registrazione.',
         descrizione='Otto segnali di fiducia on-page, raggruppati nei quattro pilastri E-E-A-T.', has_demo=False,
         come_funziona=[
             ('Inserite l’indirizzo del sito', 'Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura: analizziamo il codice HTML, non serve installare nulla.'),
             ('Otto controlli automatici', 'Cerchiamo otto segnali di fiducia leggibili nella pagina — HTTPS, contatti, P.IVA, privacy, chi siamo, portfolio, dati strutturati, profili esterni — e li raggruppiamo nei quattro pilastri E-E-A-T.'),
             ('Punteggio 0–100 e quattro assi', 'Un punteggio complessivo e il dettaglio per Esperienza, Competenza, Autorevolezza e Affidabilità, con il colore di ogni segnale e cosa manca.'),
         ],
         faq=[
             ('Cos’è l’E-E-A-T?', 'È un concetto delle linee guida di Google per i valutatori della qualità (Search Quality Rater Guidelines): Experience, Expertise, Authoritativeness, Trust — esperienza, competenza, autorevolezza e affidabilità. Aiuta Google a stimare quanto ci si può fidare di una pagina, soprattutto sui temi che incidono su salute, denaro e sicurezza.'),
             ('L’E-E-A-T influenza il posizionamento?', 'Non è un fattore di ranking diretto né un punteggio che Google assegna: è una cornice di qualità che i valutatori umani usano per addestrare gli algoritmi. Rafforzare i segnali di fiducia aiuta indirettamente, ma nessuno strumento — nemmeno il nostro — misura l’E-E-A-T «reale» del vostro sito.'),
             ('Perché il test non vede la mia reputazione?', 'Perché leggiamo solo il codice della vostra pagina: possiamo verificare che i segnali di fiducia ci siano e siano dichiarati, non chi vi cita, che recensioni avete o quanto siete davvero esperti. Quella parte la giudicano le persone e il resto del web, non una scansione dell’HTML.'),
         ],
         metodologia=('Cosa misura davvero questo test dei segnali E-E-A-T', [
             'Come per il controllo GDPR e per quello di prontezza AI, è il nostro server a leggere la home page del vostro sito, senza passare da Google. Sul codice HTML cerchiamo otto segnali di fiducia che chiunque — un motore di ricerca, un modello AI, un cliente diffidente — userebbe per decidere se fidarsi: la connessione sicura (HTTPS), i contatti verificabili, l’identità legale (P.IVA e ragione sociale), i link a privacy e cookie policy, la pagina «Chi siamo», un portfolio o dei casi studio, i dati strutturati in JSON-LD e i profili esterni. Ogni segnale finisce in uno dei quattro pilastri E-E-A-T — Esperienza, Competenza, Autorevolezza, Affidabilità — e pesa sul punteggio complessivo.',
             'Ed ecco il confine, che diciamo subito: misuriamo segnali on-page verificabili nel codice, non l’E-E-A-T reale del vostro sito. Non contiamo i link o le menzioni che ricevete, non leggiamo le recensioni né la vostra reputazione, non giudichiamo se siete davvero esperti o se i contenuti dicono il vero: quella valutazione la fanno le persone — i quality rater di Google e il resto del web — non una scansione dell’HTML. Guardiamo solo la home indicata, non l’intero sito, e non vediamo ciò che compare soltanto dopo l’esecuzione del JavaScript. Un punteggio alto significa che i segnali di fiducia ci sono e sono leggibili, non che Google vi darà un giudizio E-E-A-T positivo.',
         ]),
         lettura=('Come leggere il punteggio E-E-A-T e i quattro assi', [
             'Il punteggio va da 0 a 100 e si legge come un semaforo a quattro livelli. Da 90 in su i segnali di fiducia ci sono quasi tutti e si leggono senza sforzo. Tra 75 e 89 avete una buona base, con pochi elementi da completare. Tra 50 e 74 mancano diversi segnali importanti: è la fascia più comune per i siti aziendali italiani, che spesso curano i contenuti ma dimenticano la parte tecnica. Sotto 50 la pagina espone pochi appigli di fiducia — ed è anche la situazione in cui bastano poche aggiunte per salire in fretta. Accanto al totale trovate i quattro assi, così vedete su quale pilastro conviene intervenire prima.',
             'Due letture da evitare. La prima: un segnale in rosso non è una colpa, ma un’occasione — «nessun dato strutturato» vuol dire che, aggiungendo un blocco JSON-LD, guadagnate punti in un pomeriggio. La seconda, più importante: un 100 pieno non certifica il vostro E-E-A-T. Significa che avete dichiarato bene chi siete, non che il web vi considera autorevoli — quella fiducia si costruisce con contenuti, tempo e reputazione, che nessuno strumento legge dall’HTML. E se il punteggio vi sembra ingiustamente basso, controllate se il sito rende i contenuti via JavaScript: in quel caso molti segnali esistono ma non sono nel codice iniziale che leggiamo, e ve lo segnaliamo con un avviso.',
         ]),
         migliorare=dict(h2='Come rafforzare i segnali E-E-A-T del sito',
             intro='Rafforzare la fiducia non richiede riscrivere il sito: sono aggiunte tecniche precise, quasi tutte veloci e a basso costo.',
             punti=[
                 ('Pubblicate una pagina «Chi siamo» vera', 'Con nomi, volti, storia e competenze reali del team, non un paragrafo generico: è il primo posto dove Google e i lettori cercano di capire chi c’è dietro.'),
                 ('Rendete i contatti verificabili', 'Indirizzo completo, telefono ed email reali in chiaro, nel footer di ogni pagina, non solo dentro un modulo: un recapito tracciabile è un segnale di fiducia di base.'),
                 ('Dichiarate l’identità legale', 'P.IVA, ragione sociale e sede nel footer: per un’azienda italiana è la prova più semplice di essere un soggetto reale e raggiungibile.'),
                 ('Aggiungete i dati strutturati', 'Un blocco JSON-LD schema.org Organization (o LocalBusiness) con nome, logo, contatti e profili «sameAs» dice a motori e AI chi siete, in modo esplicito.'),
                 ('Firmate e datate i contenuti', 'Autore riconoscibile, data di pubblicazione e di aggiornamento su articoli e schede: mostrano esperienza reale e contenuti curati nel tempo.'),
             ],
             links=[
                 ('Vogliamo sistemarli noi: fa parte della SEO tecnica', '/servizi/seo-tecnica/'),
                 ('Chi siamo, contatti e dati strutturati sono di serie nei siti aziendali', '/servizi/siti-aziendali/'),
                 ('Controllate anche la SEO on-page della pagina', '/strumenti/analisi-seo/'),
             ]),
         cta=dict(heading='Vogliamo rafforzare la fiducia del vostro sito?',
                  testo='Chi siamo, contatti verificabili, identità legale e dati strutturati a posto: fanno parte della SEO tecnica e di ogni sito aziendale che consegniamo.',
                  buttons=[('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None),
                           ('Verifica se il sito è pronto per l’AI', '/strumenti/sito-pronto-ai/', 'outline')])),
    dict(slug='sito-letto-dallai', idx='/09', tipo='ai-read', titolo='Il vostro sito, letto dall’AI',
         hero_titolo='Il vostro sito, letto dall’AI',
         hero_sub='Incollate l’indirizzo: un’intelligenza artificiale legge la vostra home come farebbe ChatGPT o un assistente AI, e vi dice cosa ha capito. Di cosa vi occupate, per chi, e quanto è facile — per un’AI — citarvi in una risposta. In meno di un minuto, un verdetto e le tre mosse che contano. Non è il check tecnico di «Pronto per l’AI»: qui l’AI vi legge davvero.',
         descrizione='Cosa capisce l’AI del vostro sito, e come vi citerebbe.', has_demo=True,
         come_funziona=[
             ('Incollate l’indirizzo', 'La home o la pagina che vi rappresenta. Nessuna registrazione, nessun dato di pagamento.'),
             ('L’AI legge come un assistente', 'Il nostro server prende il testo, i titoli, i dati strutturati, l’llms.txt e il robots.txt della pagina e li passa a un modello di intelligenza artificiale, con le stesse informazioni che vede un assistente AI quando vi incontra.'),
             ('Leggete cosa ha capito', 'Cosa fate e per chi, secondo l’AI; un punteggio di «citabilità» da 0 a 100; e tre mosse concrete, in forma di «fate X → ottenete Y». Il resto dell’analisi ve lo mandiamo via e-mail.'),
         ],
         faq=[
             ('È lo stesso di «Il sito è pronto per l’AI?»', 'No, sono complementari. «Pronto per l’AI» controlla i segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e dà un punteggio su 4. Qui l’AI legge davvero i contenuti e vi dice cosa ha capito. Uno misura gli ingranaggi, l’altro il risultato.'),
             ('Conservate il testo del mio sito?', 'No. Il contenuto della pagina viene letto una volta per generare l’analisi e non lo salviamo. In cache teniamo solo il risultato, per 24 ore, così una seconda prova sullo stesso sito è immediata.'),
             ('Perché l’analisi completa arriva via e-mail?', 'A schermo trovate subito il verdetto e le tre mosse. Il resto — cosa ha capito l’AI, per chi vi vede, perché quel punteggio — ve lo inviamo via e-mail, così resta a portata di mano quando ne parlate con noi o col vostro team.'),
         ],
         metodologia=('Che cosa vede l’AI quando legge il vostro sito', [
             'Un assistente AI non «guarda» il sito come un visitatore: ne legge il testo, i titoli, la meta description, i dati strutturati e — se ci sono — l’llms.txt e le regole per i suoi crawler. Da quei segnali ricostruisce chi siete e cosa offrite. Noi passiamo a un modello esattamente quel materiale e gli chiediamo tre cose semplici: di cosa si occupa questo sito, a chi si rivolge, e quanto sarebbe sicuro di citarlo in una risposta. Il punteggio di citabilità nasce lì: non è la vostra posizione su ChatGPT, è quanto il vostro sito si spiega da solo.',
             'È giusto dire cosa questo strumento non fa. Non promette che ChatGPT vi nominerà, non conta quante volte siete già citati, non è un audit tecnico pagina per pagina. È una lettura qualitativa: lo specchio di come una macchina interpreta le vostre parole. Se l’AI capisce male, di solito è il sito a parlare poco chiaro — ed è una cosa che si aggiusta.',
         ]),
         lettura=('Come leggere il verdetto e la citabilità', [
             'Partite dal verdetto e dalle tre mosse: sono già ordinate per impatto e scritte come azioni, «fate questo → succede quello». Poi guardate la citabilità. Da 75 in su l’AI vi capisce e vi citerebbe volentieri: il sito si presenta bene. Tra 50 e 74 il senso c’è ma qualcosa confonde — un titolo generico, una home che non dice subito cosa vendete. Sotto 50 l’AI fatica a dire di cosa vi occupate: è la prima cosa da sistemare, prima di ogni tattica.',
             'Due letture da evitare. Un punteggio alto non significa «primo su ChatGPT»: significa che vi spiegate bene, il che è la precondizione, non la garanzia. E se «cosa ha capito» non vi somiglia, non è un errore dell’AI: è il segnale che il vostro sito, letto da fuori, racconta una storia diversa da quella che avete in testa.',
         ]),
         cta=dict(heading='Volete che l’AI vi capisca al primo colpo?',
                  testo='Dal verdetto al lavoro: rendiamo il vostro sito leggibile agli assistenti AI e ai motori — contenuti chiari, dati strutturati, llms.txt. A prezzo chiuso, con PageSpeed 90+ garantito da contratto.',
                  buttons=[('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None),
                           ('Il sito è pronto per l’AI?', '/strumenti/sito-pronto-ai/', 'outline')])),
    dict(slug='suona-madrelingua', idx='/10', tipo='ai-suona', titolo='Suona madrelingua?',
         hero_titolo='Suona madrelingua?',
         hero_sub='Vendete anche in inglese o in russo? Incollate un testo del vostro sito: un’intelligenza artificiale vi dice se suona come l’avrebbe scritto un madrelingua, o se si sente la traduzione. Scegliete la lingua, incollate il testo: in pochi secondi un punteggio di naturalezza e tre correzioni concrete. Traduciamo per i mercati esteri dal 2001: questo è il nostro mestiere, in versione gratuita.',
         descrizione='I vostri testi in inglese o russo suonano nativi?', has_demo=True,
         come_funziona=[
             ('Scegliete la lingua e incollate il testo', 'Un paragrafo della home, la descrizione di un prodotto, il chi siamo: nella lingua in cui vendete all’estero. Fino a circa 2.000 caratteri. Niente registrazione.'),
             ('L’AI lo legge come un madrelingua', 'Un modello di intelligenza artificiale valuta il testo come lo sentirebbe un lettore madrelingua di quella lingua: scorrevolezza, tono, calchi dall’italiano o da un’altra lingua, espressioni che tradiscono una traduzione.'),
             ('Leggete cosa cambiare', 'Un punteggio di naturalezza da 0 a 100, il registro giusto per quel mercato, e tre correzioni «prima → dopo» spiegate.'),
         ],
         faq=[
             ('Conservate il testo che incollo?', 'No. Il testo viene valutato una volta e non lo salviamo. In cache resta solo il risultato per 24 ore, così ripetere la stessa prova è immediato.'),
             ('Corregge anche il testo al posto mio?', 'Vi dà tre correzioni «prima → dopo» come esempio, non riscrive tutto. La riscrittura completa e coerente su tutto il sito è un lavoro da redattore madrelingua: è il nostro servizio di localizzazione.'),
             ('Quali lingue valuta?', 'Le due lingue proposte in questa pagina: sono quelle utili a chi vende dall’Italia verso l’estero. La revisione completa la fanno redattori madrelingua, lingua per lingua, dal 2001.'),
         ],
         metodologia=('Che cosa rende un testo «madrelingua»', [
             'Un testo può essere corretto e suonare comunque straniero. Succede quando la grammatica è a posto ma la costruzione è calcata su un’altra lingua: frasi troppo lunghe, un registro sbagliato, parole giuste al posto sbagliato, quel tono da manuale tradotto. Un lettore madrelingua non lo analizza — lo sente, e si fida meno. Chiediamo al modello proprio questo: non «ci sono errori?», ma «suona come l’avrebbe scritto una persona madrelingua?».',
             'Cosa non è. Non è un correttore ortografico: gli errori di battitura non sono il punto. Non è un giudizio letterario né un ranking SEO. È una valutazione di naturalezza e tono — la differenza tra un testo che passa e uno che vende. E come ogni lettura AI, è un parere, non un verdetto: la revisione vera la fa un redattore madrelingua, lingua per lingua, che è esattamente ciò che facciamo dal 2001.',
         ]),
         lettura=('Come leggere il punteggio di naturalezza', [
             'Il punteggio dice quanto il testo suona nativo in quella lingua. Da 75 in su siete a posto: un madrelingua lo leggerebbe senza inciampi. Tra 50 e 74 il senso c’è, ma qualcosa stona — un calco, una frase contorta, un registro sbagliato — e le tre correzioni vi dicono dove. Sotto 50 si sente la traduzione: il testo funziona per capirsi, non ancora per convincere. Partite dalle correzioni: sono le tre che spostano di più.',
             'Un’avvertenza onesta. Un punteggio alto non certifica che il testo sia perfetto per il vostro pubblico: il tono giusto per una gioielleria non è quello giusto per un’officina. Usate il registro come bussola, non come voto finale. E ricordate che l’AI legge il testo che incollate, non l’intero sito: è una sonda, non un audit.',
         ]),
         cta=dict(heading='Volete che i vostri testi parlino come un madrelingua?',
                  testo='Dal 2001 traduciamo e adattiamo siti per i mercati esteri con redattori madrelingua — non un plugin, un deliverable con nome e cognome. Prezzo chiuso, consegna a data fissa.',
                  buttons=[('Scopri i siti multilingue', '/servizi/siti-multilingue/', None),
                           ('Vedi tutti gli strumenti', '/strumenti/', 'outline')])),
    dict(slug='generatore-llms-txt', idx='/11', tipo='ai-llms', titolo='Generatore di llms.txt',
         hero_titolo='Generatore di llms.txt',
         hero_sub='Il file che spiega il vostro sito agli assistenti AI, pronto da scaricare. Rispondete a tre domande — o incollate solo l’indirizzo e i dati li raccogliamo noi — e un’intelligenza artificiale scrive il vostro llms.txt: struttura corretta, pagine chiave, descrizione chiara. Da copiare, scaricare e mettere online. Gratis, senza registrazione.',
         descrizione='Il vostro llms.txt, scritto e pronto da scaricare.', has_demo=True,
         come_funziona=[
             ('Dateci l’essenziale', 'Nome, di cosa vi occupate, le pagine che contano. Oppure incollate solo l’indirizzo del sito: leggiamo noi la home e ricaviamo i dati.'),
             ('L’AI scrive il file', 'Un modello di intelligenza artificiale compone l’llms.txt nel formato che i crawler AI si aspettano: un’intestazione con il nome, una descrizione sintetica, l’elenco delle pagine importanti con una riga ciascuna.'),
             ('Copiate, scaricate, pubblicate', 'Il file è pronto: lo copiate con un clic o lo scaricate come llms.txt. Va caricato nella cartella principale del sito, accanto al robots.txt.'),
         ],
         faq=[
             ('Devo per forza avere un llms.txt?', 'Non è obbligatorio come il robots.txt, ma è un segnale in crescita: da maggio 2026 Google lo considera nell’audit «Agentic Browsing» di Lighthouse. A costo zero, è tra le cose più facili da fare per farsi leggere meglio dagli assistenti AI.'),
             ('Conservate i dati che inserisco?', 'No. Usiamo i dati (o il testo della home, se date solo l’indirizzo) una volta per generare il file e non li salviamo. In cache resta solo il risultato per 24 ore.'),
             ('Basta l’llms.txt per farsi trovare da ChatGPT?', 'No, è un pezzo del puzzle. Farsi citare dagli assistenti AI dipende anche da contenuti chiari, dati strutturati e autorevolezza. L’llms.txt aiuta a spiegarsi; il resto è SEO tecnica e contenuti.'),
         ],
         metodologia=('Che cos’è l’llms.txt e cosa ci mettiamo dentro', [
             'L’llms.txt è un file di testo, in formato Markdown, che vive nella radice del sito e riassume — per gli assistenti AI — chi siete e quali sono le vostre pagine importanti. È al mondo dei modelli AI quello che il robots.txt è a Google: una mappa breve e leggibile, che i crawler di ChatGPT, Perplexity o Claude leggono più volentieri dell’HTML. Noi generiamo l’intestazione con il nome, una descrizione onesta del business e la lista delle pagine chiave, ognuna con la sua riga di contesto.',
             'Cosa non è. L’llms.txt non è una bacchetta magica: non garantisce di essere citati e, da solo, non fa SEO. È un pezzo — utile e a costo zero — di un lavoro più ampio di visibilità sugli assistenti AI. Il file che generiamo è un ottimo punto di partenza: rileggetelo, sistemate la descrizione se serve, e verificate che le pagine elencate siano davvero quelle giuste.',
         ]),
         lettura=('Come usare il file che avete generato', [
             'Il risultato è il file completo, pronto. Copiatelo o scaricatelo, poi caricatelo nella cartella principale del sito — la stessa dove vive il robots.txt — così l’indirizzo finale è iltuosito.it/llms.txt. Da lì i crawler AI lo trovano da soli. Sotto al file trovate una nota: di solito è un dettaglio da controllare a mano, come una descrizione da personalizzare o una pagina da aggiungere.',
             'Un consiglio. Rileggete sempre la descrizione prima di pubblicare: l’AI la scrive dai dati che le date, ma nessuno conosce il vostro business meglio di voi. Due minuti di rilettura valgono più di dieci righe generate al volo. E aggiornatelo quando aggiungete pagine importanti: un llms.txt vecchio racconta un sito che non c’è più.',
         ]),
         cta=dict(heading='Volete essere trovati e citati dagli assistenti AI?',
                  testo='L’llms.txt è il primo passo. Il resto — dati strutturati, contenuti leggibili dalle AI, SEO tecnica — lo costruiamo noi, a prezzo chiuso e con PageSpeed 90+ garantito da contratto.',
                  buttons=[('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None),
                           ('Il sito è pronto per l’AI?', '/strumenti/sito-pronto-ai/', 'outline')])),
]

# Городские лендинги. Правило из piano-contenuti-seo.md §2: максимум 6–8
# содержательных страниц, каждая с локальным кейсом и отзывами с гео-привязкой —
# никаких клонов с заменой топонима (doorway-риск). У milano есть офис (полный
# блок «Dove siamo»); остальные города обслуживаются из Милана — честный блок
# «Serviamo {città} da Milano» вместо выдуманного адреса.
CITIES = [
    dict(
        slug='milano', nome='Milano', eyebrow='Web agency Milano', progetti=14, dal='2023',
        sub='Siti progressivi per PMI di Milano e provincia: PageSpeed 90+ garantito da contratto, consegna a data fissa, prezzo chiuso. Il primo incontro, da voi o in studio, non si paga.',
        has_office=True,
        indirizzo='Via Andrea Solari 43, 20144 Milano (MI)', metro='M2 S. Agostino — 4 min a piedi',
        orari='Lun–Ven 9:00–18:00', telefono='+39 02 8736 5412',
        case_slug='att-traduzione-tech', case_url_label='traduzione.tech',
        case_eyebrow='La stessa ingegneria, per un cliente italiano', case_title='ATT, il sito dell’agenzia di traduzioni',
        recensioni=[
            ('Preventivo chiaro, consegnato il giorno promesso. Il sito carica subito anche in cantiere, dove la rete è quella che è.', 'Marco T. — impresa edile, Sesto S. Giovanni'),
            ('Ci hanno mostrato i numeri del vecchio sito prima di parlare di soldi. Nessuno l’aveva mai fatto.', 'Elena R. — showroom ceramiche, Milano'),
            ('Versione tedesca impeccabile: i clienti di Monaco ordinano dal sito senza scriverci più per chiedere chiarimenti.', 'Giulia B. — torneria meccanica, Cinisello'),
        ],
        faq=[
            ('Quanto costa un sito web a Milano?', 'Le agenzie milanesi chiedono in media 2.500–8.000 € per un sito aziendale. I nostri prezzi sono pubblici: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — chiusi nel preventivo, con PageSpeed 90+ e data di consegna scritti nel contratto.'),
            ('Lavorate solo su Milano città?', 'No: Milano e tutta la provincia, più Monza e Brianza. Il primo incontro non si paga, da voi o nel nostro studio in zona Solari.'),
            ('Serve incontrarsi di persona?', 'Non è obbligatorio: analisi, preventivo e avanzamento lavori passano da videochiamate e da un ambiente di prova online. Ma se siete a Milano, il caffè lo offriamo noi.'),
        ],
    ),
    dict(
        slug='monza', nome='Monza', eyebrow='MONZA E BRIANZA', progetti=8, dal='2023',
        sub='Siti progressivi per PMI di Monza e della Brianza: PageSpeed 90+ garantito da contratto, consegna a data fissa, prezzo chiuso. Il primo incontro, da voi in azienda, non si paga.',
        has_office=False,
        vicino='A 20 minuti dal nostro studio di Milano: sopralluoghi e incontri in azienda senza costi di trasferta, in tutta la provincia di Monza e Brianza.',
        case_slug='tms-perevod4', case_url_label='tms.perevod4.ru',
        case_eyebrow='Sistemi, non solo siti', case_title='TMS, il sistema operativo del gruppo',
        recensioni=[
            ('Lo showroom non ha mai chiuso: il sito nuovo è andato online in una notte, con i redirect già pronti.', 'Paolo C. — arredamenti su misura, Lissone'),
            ('Il catalogo si apre anche dove il Wi-Fi non prende. I clienti lo sfogliano in showroom dal telefono.', 'Andrea M. — cucine componibili, Seregno'),
            ('Prezzo chiuso davvero: nessun extra a fine lavori, ed era tutto scritto nel preventivo.', 'Federica P. — studio dentistico, Monza'),
        ],
        faq=[
            ('Quanto costa un sito web a Monza?', 'Gli stessi prezzi pubblici che applichiamo ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — prezzo chiuso nel preventivo, PageSpeed 90+ e data di consegna nel contratto.'),
            ('Venite in azienda in Brianza?', 'Sì: il primo incontro non si paga e lo facciamo volentieri da voi — Lissone, Seregno, Desio, Vimercate, tutta la provincia.'),
            ('Avete già lavorato con aziende della zona?', 'Lavoriamo soprattutto con PMI di Monza e Brianza, ma il caso che mostriamo più spesso è un nostro progetto interno: il TMS che gestisce 180 ordini al mese per il gruppo Remarka — la stessa ingegneria che mettiamo nei siti che consegniamo qui.'),
        ],
    ),
    dict(
        slug='bergamo', nome='Bergamo', eyebrow='BERGAMO E PROVINCIA', progetti=6, dal='2024',
        sub='Siti progressivi per PMI di Bergamo e provincia: PageSpeed 90+ garantito da contratto, consegna a data fissa, prezzo chiuso. Versione in tedesco tradotta da madrelingua per chi lavora con l’estero.',
        has_office=False,
        vicino='Un’ora dal nostro studio di Milano: primo incontro in azienda senza costi, da Bergamo città alle valli. Per il resto: ambiente di prova online e avanzamento visibile ogni venerdì.',
        case_slug='test-traduttori', case_url_label='moscowtrans.ru/test-perevodchika',
        case_eyebrow='Dietro la garanzia «madrelingua per profilo»', case_title='La piattaforma che testa i traduttori',
        recensioni=[
            ('I clienti di Bressanone e Merano finalmente trovano tutto in tedesco. Le richieste sono triplicate.', 'Titolare — impianti idraulici, Bergamo'),
            ('Sito consegnato il giorno scritto nel contratto. Non ci credevamo, è successo.', 'Luca R. — carpenteria metallica, Dalmine'),
            ('Il modulo contatti ci avvisa su WhatsApp: rispondiamo ai preventivi prima dei concorrenti.', 'Sara V. — serramenti, Treviglio'),
        ],
        faq=[
            ('Quanto costa un sito web a Bergamo?', 'Prezzi pubblici, uguali ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — chiusi nel preventivo, con PageSpeed 90+ e data di consegna nel contratto.'),
            ('Fate siti in tedesco per chi lavora con l’estero?', 'Sì, ed è la nostra specialità: le traduzioni le fanno madrelingua del gruppo Remarka (nel settore dal 2001), selezionati da una piattaforma di test interna che scarta il 92% dei candidati — la stessa che tiene la qualità di tutti i nostri progetti multilingue.'),
            ('Il primo incontro è davvero gratuito?', 'Sì: veniamo noi in azienda, analizziamo il sito attuale e vi lasciamo un report scritto con le priorità. Il preventivo arriva entro 24 ore.'),
        ],
    ),
    dict(
        slug='brescia', nome='Brescia', eyebrow='BRESCIA E PROVINCIA', progetti=5, dal='2024',
        sub='Siti progressivi per le PMI manifatturiere di Brescia e provincia: PageSpeed 90+ garantito da contratto, prezzo chiuso, versione in tedesco o inglese tradotta da madrelingua per chi esporta.',
        has_office=False,
        vicino='Serviamo Brescia e provincia dal nostro studio di Milano: primo incontro in azienda senza costi di trasferta, poi ambiente di prova online e avanzamento visibile ogni venerdì.',
        case_slug='pere-rf', case_url_label='пере.рф',
        case_eyebrow='SEO tecnica, non fortuna del nome', case_title='пере.рф, primi posti su Yandex',
        recensioni=[
            ('Catalogo tecnico di 400 codici, ora si apre in un secondo. I clienti tedeschi ordinano senza telefonare.', 'Titolare — minuterie metalliche, Lumezzane'),
            ('Ci hanno fatto vedere i numeri del sito vecchio prima di parlare di prezzo. Serietà rara.', 'Giorgio F. — officina meccanica, Brescia'),
            ('Preventivo chiuso e data fissa, come promesso. Il sito è online dal giorno concordato.', 'Anna T. — azienda vinicola, Franciacorta'),
        ],
        faq=[
            ('Quanto costa un sito web a Brescia?', 'Prezzi pubblici, uguali ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — chiusi nel preventivo, con PageSpeed 90+ e data di consegna nel contratto.'),
            ('Lavorate con aziende manifatturiere ed esportatrici?', 'È il nostro cliente tipo: cataloghi tecnici veloci, dati strutturati per ogni prodotto e versioni in tedesco o inglese tradotte da madrelingua del gruppo Remarka.'),
            ('Come seguiamo i lavori se siete a Milano?', 'Ambiente di prova online dal primo giorno, avanzamento visibile ogni venerdì, un unico referente. Il primo incontro lo facciamo comunque da voi, gratuitamente.'),
        ],
    ),
    dict(
        slug='como', nome='Como', eyebrow='COMO E PROVINCIA', progetti=4, dal='2024',
        sub='Siti progressivi per le PMI di Como e del lago: PageSpeed 90+ garantito da contratto, prezzo chiuso, versioni in inglese e tedesco tradotte da madrelingua per chi lavora con ospiti e clienti esteri.',
        has_office=False,
        vicino='Mezz’ora dal nostro studio di Milano: primo incontro da voi senza costi, da Como a Cantù alla sponda del lago. Poi ambiente di prova online e un unico referente.',
        case_slug='ukrinitsy', case_url_label='ukrinitsy.ru',
        case_eyebrow='Lo stesso approccio per il turismo', case_title='ukrinitsy.ru, sito vetrina per una guest house',
        recensioni=[
            ('Il sito in inglese e tedesco ha cambiato la stagione: gli ospiti prenotano direttamente, senza portali.', 'Chiara L. — casa vacanze, Menaggio'),
            ('Da tre secondi a meno di uno: le richieste dal modulo sono raddoppiate in due mesi.', 'Matteo B. — falegnameria, Cantù'),
            ('Tutto scritto nel preventivo, tutto rispettato. E il sito vola anche in riva al lago.', 'Paola G. — studio commercialista, Como'),
        ],
        faq=[
            ('Quanto costa un sito web a Como?', 'Prezzi pubblici, uguali ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — chiusi nel preventivo, con PageSpeed 90+ e data di consegna nel contratto.'),
            ('Fate siti multilingue per il turismo?', 'Sì: inglese e tedesco tradotti da madrelingua del gruppo Remarka (non da un plugin), con SEO internazionale corretta — hreflang, metadati per mercato.'),
            ('Il primo incontro è gratuito anche fuori Como città?', 'Sì, in tutta la provincia: veniamo noi, analizziamo il sito attuale e vi lasciamo un report scritto. Preventivo chiuso entro 24 ore.'),
        ],
    ),
]

# Обратная совместимость: старый импорт CITY указывает на Милан.
CITY = CITIES[0]

# Флагман «Export Ready» (линия 2 концепции) и «Web App» (линия 3).
# Цены — ориентир из concept-sviluppo-studio.md §3, помечены владельцу
# на подтверждение перед запуском рекламы.
EXPORT_READY = dict(
    slug='export-ready',
    eyebrow='Servizio / Export Ready',
    hero_title='Il vostro sito funziona anche in tedesco. Misurato, garantito, firmato',
    hero_sub='Un sito web per l’export vero: il sito nella lingua del cliente e la sua versione estera sotto un unico contratto, con localizzazione da madrelingua, SEO internazionale e KPI per ogni mercato. Nel settore linguistico dal 2001.',
    hero_stat_value='4', hero_stat_label='Lingue con traduttori madrelingua interni: inglese, tedesco, francese, russo.',
    problema_heading='Il buco in cui l’export perde soldi',
    problema_testo='Chi esporta oggi sceglie tra una web agency (che gira le traduzioni a terzi o a un plugin) e un’agenzia di traduzioni (che non costruisce siti né fa SEO internazionale). La responsabilità si spezza sempre a metà — esattamente dove il cliente estero decide se comprare. Remarka è l’unica configurazione in cui ingegneria e localizzazione professionale vivono nella stessa azienda, sotto lo stesso contratto.',
    garanzie_heading='Un sito web per l’export, garantito nero su bianco',
    garanzie=[
        'Localizzazione solo da madrelingua: nomi e qualifiche dei traduttori nel contratto',
        'Glossario di terminologia del vostro settore: è un deliverable, resta a voi',
        'Checklist SEO internazionale firmata: hreflang, metadati e URL per ogni mercato, allegata al collaudo',
        'KPI mensili per ogni mercato, per 12 mesi: traffico, posizioni, richieste',
    ],
    formati=[
        ('One Market', 'a partire da € 12.000', 'Un mercato, una lingua: analisi del mercato target fatta da madrelingua, architettura multilingue, localizzazione completa, SEO internazionale, 12 mesi di KPI.'),
        ('Multi-Market', '€ 18.000–35.000', 'Più mercati in sequenza pianificata: stessa base tecnica, glossario condiviso, priorità dei mercati decisa sui dati, report comparativo mensile.'),
    ],
    processo=[
        ('01', 'Analisi del mercato target', 'Un madrelingua studia come i vostri clienti cercano nel loro paese: parole, concorrenti, prezzi.'),
        ('02', 'Architettura multilingue', 'URL, hreflang, x-default, metadati per mercato: la base tecnica che Google richiede.'),
        ('03', 'Localizzazione, non traduzione', 'Offerta, CTA e moduli adattati al mercato, glossario approvato con voi.'),
        ('04', 'Lancio e misurazione', 'QA su tre livelli (visivo, funzionale, SEO), poi 12 mesi di KPI mensili per mercato.'),
    ],
    faq=[
        ('Perché non basta un plugin di traduzione?', 'Un plugin traduce parole, non argomenti di vendita. Un cliente tedesco riconosce un testo automatico alla seconda riga — e con lui se ne va la fiducia. I nostri madrelingua sono nel contratto, con nome e qualifica.'),
        ('Avete davvero i traduttori in casa?', 'Sì: Studio Remarka fa parte del gruppo Remarka, nel settore linguistico dal 2001, con traduttori madrelingua interni per inglese, tedesco, francese e russo.'),
        ('Come misurate i risultati per mercato?', 'Ogni mercato ha il suo report mensile: posizioni sulle parole chiave locali, traffico organico, richieste dal modulo. Per 12 mesi, inclusi nel prezzo.'),
    ],
)

WEB_APP = dict(
    slug='web-app',
    eyebrow='Servizio / Web app su misura',
    hero_title='Quando un sito non basta: web app, aree clienti, configuratori',
    hero_sub='Sviluppo web app su misura: portali B2B, cabine clienti, configuratori di prodotto, integrazioni con CRM e gestionale. Costruiti dallo stesso team che sviluppa i prodotti digitali del gruppo Remarka.',
    hero_stat_value='3', hero_stat_label='Prodotti digitali interni in produzione: piattaforma AI, TMS, servizio documenti.',
    per_chi_heading='Sviluppo web app per chi ha un processo, non solo una vetrina',
    per_chi=[
        'Aziende che gestiscono ordini, listini o pratiche via email e vogliono un’area clienti.',
        'Produttori con prodotti configurabili: un configuratore vende mentre l’ufficio tecnico dorme.',
        'PMI che devono collegare sito, CRM e gestionale senza reinserire i dati a mano.',
    ],
    formati=[
        ('MVP Sprint', 'a partire da € 15.000', 'Perimetro chiuso, prezzo chiuso, data fissa: la prima versione funzionante del prodotto in 6–8 settimane, pronta per utenti reali.'),
        ('Product Build', 'da € 25.000', 'Sviluppo per iterazioni con backlog condiviso e rilasci regolari: per prodotti che crescono con il business.'),
    ],
    prove_heading='La prova: i nostri prodotti interni',
    prove_testo='Non solo per i clienti: il gruppo Remarka sviluppa e usa in produzione i propri prodotti digitali — una piattaforma di traduzione AI, un TMS per i progetti linguistici e un servizio di documenti standard. Li pubblichiamo come casi studio con metriche tecniche reali, marchiati «Product Lab».',
    faq=[
        ('Quanto costa una web app?', 'Il formato MVP Sprint parte da € 15.000 con perimetro, prezzo e data chiusi nel contratto. Progetti a iterazioni partono da € 25.000. Il preventivo resta chiuso: quello che firmate è quello che pagate.'),
        ('Meglio una web app o un’app nativa?', 'Per la maggior parte delle PMI, una web app (o PWA) costa una frazione di un’app nativa, non passa dagli store e si aggiorna in un rilascio. L’app nativa serve solo per hardware specifico o notifiche avanzate.'),
        ('Chi mantiene il prodotto dopo il lancio?', 'Dodici mesi di assistenza inclusi, come per i siti. Dopo, canone facoltativo o consegna completa: codice e documentazione sono vostri dal primo giorno.'),
    ],
)

# Servizio «Adeguamento EAA» (docs/copy-eaa.md): niente mini_caso (nessun caso
# inventato per l'obbligo di legge), blocchi processo/garanzie dedicati —
# struttura a dict modulare come EXPORT_READY/WEB_APP, non build_servizio.
ADEGUAMENTO_EAA = dict(
    slug='adeguamento-eaa',
    title='Adeguamento EAA',
    eyebrow='Servizio / Adeguamento EAA',
    hero_title='Il sito conforme all’European Accessibility Act, in 3 settimane',
    hero_sub='Dal 28 giugno 2025 l’accessibilità è un obbligo di legge per molti siti. Vi portiamo allo standard WCAG 2.1 AA — audit, correzioni e dichiarazione di accessibilità — a prezzo chiuso e con la data nel contratto.',
    hero_stat_value='28.06.2025',
    hero_stat_label='Data da cui l’European Accessibility Act è in vigore in Italia. Le prime sanzioni sono una questione di tempo.',
    per_chi_heading='L’obbligo riguarda chi vende a consumatori, online',
    per_chi=[
        'E-commerce e servizi digitali che vendono beni o servizi ai consumatori nell’Unione Europea.',
        'Banche, assicurazioni, trasporti, biglietterie e sistemi di prenotazione online.',
        'Aziende non microimpresa che temono la prima sanzione italiana, o che l’hanno già ricevuta come segnalazione.',
    ],
    include_heading='Dall’audit alla dichiarazione, tutto scritto nel preventivo',
    include=[
        'Audit completo: test automatico (Lighthouse) più verifica manuale — tastiera, screen reader, contenuti.',
        'Correzione di tema, contrasti, etichette dei moduli e struttura dei titoli.',
        'Navigazione da tastiera e focus sempre visibile su ogni elemento interattivo.',
        'Dichiarazione di accessibilità pubblicata, il documento che la norma richiede.',
        'Audit di verifica finale secondo lo standard WCAG 2.1 AA, a correzioni fatte.',
        'Prezzo chiuso dopo l’audit, consegna in 3 settimane con penale in contratto.',
    ],
    processo_heading='Tre settimane, dalla diagnosi alla conformità',
    processo=[
        ('Settimana 1', 'Audit', 'Partiamo dal test automatico gratuito, poi la verifica manuale: tastiera, screen reader, contrasti, contenuti. A fine audit il prezzo è chiuso e la data è fissata.'),
        ('Settimana 2', 'Correzioni', 'Sistemiamo tema, contrasti, etichette dei moduli, gerarchia dei titoli e navigazione da tastiera. Ogni barriera dell’elenco, una per una.'),
        ('Settimana 3', 'Dichiarazione e verifica', 'Pubblichiamo la dichiarazione di accessibilità obbligatoria e ripetiamo l’audit per confermare la conformità WCAG 2.1 AA.'),
    ],
    processo_note='Tempi indicativi per un sito aziendale o vetrina. Un e-commerce con catalogo ampio può richiedere più tempo: lo scriviamo nel preventivo, con la stessa penale.',
    prezzo_range='da € 1.900',
    prezzo_lede='Prezzo chiuso nel preventivo dopo l’audit, da € 1.900. Consegna in 3 settimane, data fissa in contratto. Fattura elettronica, pagamento in tre tranche.',
    prezzo_note=[
        'Numero di pagine e modelli (template) da correggere: una vetrina costa meno di un e-commerce a catalogo.',
        'Stato di partenza: quante barriere emergono dall’audit iniziale.',
        'Contenuti da rifare — testi alternativi, PDF accessibili, sottotitoli ai video.',
    ],
    prezzo_link=('Non sai da dove partire? L’audit automatico è gratuito', '/strumenti/verifica-accessibilita/'),
    garanzie_heading='Nero su bianco, come per ogni nostro servizio',
    garanzie=[
        '± 0 giorni di ritardo — la data è nel contratto: ogni giorno lavorativo di ritardo vale l’1% di sconto.',
        'Prezzo chiuso dopo l’audit — quello che firmate è quello che pagate; ogni extra si concorda per iscritto prima.',
        'Standard dichiarato — conformità WCAG 2.1 AA verificata a mano, non solo un punteggio automatico.',
        'Dichiarazione di accessibilità inclusa — il documento richiesto dalla norma, pubblicato sul vostro sito.',
    ],
    faq=[
        ('Chi è obbligato dall’EAA? La mia azienda rientra?', 'L’European Accessibility Act è in vigore in Italia dal 28 giugno 2025 e obbliga molti siti che vendono beni o servizi ai consumatori: e-commerce, banche, trasporti, servizi digitali. Sono esentate le microimprese che erogano servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato annuo. Nel dubbio verifichiamo il vostro caso prima di firmare: se non siete obbligati, ve lo diciamo.'),
        ('Quali sanzioni sono previste in Italia?', 'Il decreto italiano prevede sanzioni fino al 5% del fatturato per i servizi non conformi. In Francia sono già partite le prime cause verso i grandi rivenditori online, e in Italia l’applicazione è appena cominciata. Le fonti sono pubbliche: la guida di Bird & Bird e il centro AccessibleEU della Commissione europea (link in fondo alla pagina).'),
        ('Cos’è la dichiarazione di accessibilità?', 'È un documento pubblico, richiesto dalla norma, in cui il sito dichiara il proprio livello di conformità, le eventuali parti non ancora accessibili e un contatto per segnalare problemi. Lo redigiamo e lo pubblichiamo noi, come parte del servizio: senza dichiarazione, il sito non è a norma anche se tecnicamente accessibile.'),
        ('Basta un controllo automatico per essere conformi?', 'No, ed è giusto dirlo chiaro. Un test automatico come il nostro strumento gratuito intercetta circa un terzo dei criteri WCAG: quello che una macchina sa misurare. Il resto — navigazione da tastiera, esperienza con screen reader, chiarezza dei contenuti — si verifica solo a mano. Per questo l’audit manuale è il cuore del servizio, non un optional.'),
    ],
    fatti=[
        'European Accessibility Act (dir. UE 2019/882), in vigore in Italia dal 28 giugno 2025.',
        'Sanzioni fino al 5% del fatturato per i servizi non conformi (recepimento italiano).',
    ],
    fonti=[
        ('Bird & Bird — guida all’European Accessibility Act', 'https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat'),
        ('AccessibleEU (Commissione europea) — l’EAA in vigore da giugno 2025', 'https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en'),
    ],
    disclaimer='Un controllo automatico copre parte dei criteri WCAG 2.1 AA. La conformità piena richiede la verifica manuale, che è inclusa in questo servizio.',
    cta=dict(
        heading='Facciamo il punto sul vostro sito',
        testo='L’audit iniziale trasforma l’obbligo in una lista di cose da fare, con prezzo chiuso e data di consegna. Il primo controllo automatico è gratuito e senza registrazione.',
        buttons=[('Richiedi l’audit di accessibilità', '/#contatti', None),
                 ('Prova lo strumento gratuito', '/strumenti/verifica-accessibilita/', 'outline')],
    ),
)

# --- Bank di prime fonti autorevoli (URL verificati). Definito prima di
#     BLOG_POSTS: sia il ritrofit (_BLOG_FONTI, più sotto) sia i batch 2+
#     (fonti/link inline nei dict) referenziano queste costanti. ---
_S_EURLEX_EAA   = 'https://eur-lex.europa.eu/eli/dir/2019/882/oj'
_S_ACCESSIBLEEU = 'https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en'
_S_WCAG21       = 'https://www.w3.org/TR/WCAG21/'
_S_WAI_WCAG     = 'https://www.w3.org/WAI/standards-guidelines/wcag/'
_S_BIRDBIRD_EAA = 'https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat'
_S_GARANTE_COOKIE = 'https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876'
_S_EDPB_COOKIE  = 'https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-cookie-banner-taskforce_en'
_S_GDPR         = 'https://eur-lex.europa.eu/eli/reg/2016/679/oj'
_S_OPENAI_BOTS  = 'https://platform.openai.com/docs/bots'
_S_ANTHROPIC    = 'https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler'
_S_LLMSTXT      = 'https://llmstxt.org/'
_S_GOOGLE_CRAWLERS = 'https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers'
_S_GOOGLE_HELPFUL  = 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content'
_S_GOOGLE_SD    = 'https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data'
_S_GOOGLE_AI    = 'https://developers.google.com/search/docs/appearance/ai-features'
_S_GOOGLE_SITEMOVE = 'https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes'
_S_GOOGLE_REDIRECTS = 'https://developers.google.com/search/docs/crawling-indexing/301-redirects'
_S_GOOGLE_MULTIREG  = 'https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites'
_S_GOOGLE_HREFLANG  = 'https://developers.google.com/search/docs/specialty/international/localized-versions'
_S_WEBDEV_VITALS = 'https://web.dev/articles/vitals'
_S_WEBDEV_LCP    = 'https://web.dev/articles/lcp'
_S_WEBDEV_INP    = 'https://web.dev/articles/inp'
_S_WEBDEV_CLS    = 'https://web.dev/articles/cls'
_S_WEBDEV_PWA    = 'https://web.dev/explore/progressive-web-apps'
_S_WEBDEV_LEARN_PWA = 'https://web.dev/learn/pwa/'
_S_MDN_PWA       = 'https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps'
_S_CRUX          = 'https://developer.chrome.com/docs/crux'
_S_ALMANAC       = 'https://almanac.httparchive.org/en/2024/'
_S_SWD           = 'https://sustainablewebdesign.org/estimating-digital-emissions/'
_S_CSA           = 'https://csa-research.com/Featured-Content/Global-Growth/CRWB-Series/CRWB-B2C'
_S_EUROSTAT_ECOM = 'https://ec.europa.eu/eurostat/statistics-explained/index.php?title=E-commerce_statistics'
# --- Batch 2 (fonti verificate 16.07): fatturazione elettronica SDI, CSRD,
#     Green Web Foundation co2.js, W3C WAI «Developing an Accessibility Statement». ---
_S_SDI           = 'https://www.agenziaentrate.gov.it/portale/aree-tematiche/fatturazione-elettronica'
_S_CSRD          = 'https://eur-lex.europa.eu/eli/dir/2022/2464/oj'
_S_CO2JS         = 'https://www.thegreenwebfoundation.org/co2-js/'
_S_WAI_STATEMENT = 'https://www.w3.org/WAI/planning/statements/'

BLOG_POSTS = [
    dict(slug='sito-quattro-lingue-costi-tempi', data='05 MAG 2026',
         titolo='Un sito in quattro lingue: costi, tempi e gli errori da evitare',
         estratto='Quando la traduzione automatica basta e quando vi costa clienti. Con i prezzi reali per lingua e un caso reale del gruppo Remarka.',
         corpo="La traduzione automatica basta per un menu o un orario di apertura. Non basta per una scheda prodotto tecnica o una pagina di vendita, dove un errore di registro costa un cliente prima ancora che scriva. In questo articolo spieghiamo quando conviene la traduzione automatica, quando serve un madrelingua, e cosa cambia davvero nei costi e nei tempi per lingua, con un caso reale del gruppo Remarka.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/quattro-cover.svg',
                    alt='Un sito in quattro lingue: costi, tempi e la differenza tra tradurre e localizzare')),
    dict(slug='cookie-banner-checklist-garante-2026', data='08 APR 2026',
         titolo='Cookie banner a norma: la checklist 2026 del Garante',
         estratto='Rifiuta equivalente ad accetta, niente cookie wall, consenso documentabile. Cosa controllare sul vostro sito, punto per punto.',
         corpo='Il Garante Privacy richiede che il pulsante «Rifiuta» abbia lo stesso peso visivo del pulsante «Accetta» in un cookie banner, e che il consenso sia documentabile nel tempo. Sono regole semplici, ma ignorate dalla maggior parte dei siti italiani che analizziamo. Ecco la checklist punto per punto che usiamo per verificare un sito, e come costruiamo i nostri banner per essere a norma fin dal primo giorno.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/cookie-cover.svg',
                    alt='Cookie banner a norma nel 2026: «Rifiuta» con lo stesso peso di «Accetta» e consenso documentabile secondo il Garante Privacy')),
    dict(slug='migrare-wordpress-senza-perdere-seo', data='17 MAR 2026',
         titolo='Migrare da WordPress senza perdere le posizioni su Google',
         estratto='Redirect, struttura degli URL e cosa succede nelle prime sei settimane. Il protocollo che usiamo su ogni migrazione.',
         corpo='Ogni migrazione tecnica comporta il rischio di perdere anni di posizionamento organico. In questo articolo spieghiamo il protocollo di audit, mappatura URL e redirect 301 che applichiamo prima di ogni migrazione da WordPress, cosa monitoriamo nelle prime sei settimane dopo il cambio, e un caso reale in cui il posizionamento è rimasto invariato.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/migrare-cover.svg',
                    alt='Migrare da WordPress senza perdere la SEO: redirect 301, mappa degli URL e sei settimane di monitoraggio')),
    dict(slug='pwa-per-pmi-quando-app-non-serve', data='24 FEB 2026',
         titolo="PWA per le PMI: quando l’app non serve",
         estratto="Un sito progressivo si installa, funziona offline e costa un quinto di un’app nativa. I tre casi in cui conviene davvero.",
         corpo="Sviluppare un’app nativa costa in media 15.000–30.000 euro e richiede manutenzione separata per iOS e Android. Un sito progressivo (PWA) offre installabilità, notifiche e funzionamento offline a una frazione del costo, senza revisione degli store. In questo articolo i tre casi concreti in cui una PWA conviene davvero a una PMI italiana, e i due in cui serve ancora un’app nativa.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/pwa-cover.svg',
                    alt='PWA per le PMI: quando l’app nativa non serve, con installabilità, uso offline e notifiche')),
    dict(slug='quanto-costa-sito-aziendale-italia', data='03 FEB 2026',
         titolo='Quanto costa un sito aziendale in Italia: i prezzi veri',
         estratto='Da 800 a 50.000 euro: cosa cambia davvero tra le fasce e le domande da fare prima di firmare qualunque preventivo.',
         corpo="Il mercato dei siti web in Italia è frammentato e poco trasparente: si va dagli 800 euro dei costruttori fai-da-te ai 50.000 euro delle grandi agenzie. In questo articolo mappiamo onestamente cosa si compra a ogni fascia di prezzo, incluso il nostro, e le domande da fare prima di firmare qualunque preventivo.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/costo-sito-cover.svg',
                    alt='Quanto costa un sito aziendale in Italia: le fasce di prezzo dagli 800 ai 50.000 euro')),
    dict(slug='core-web-vitals-2026', data='12 GEN 2026',
         titolo='Core Web Vitals nel 2026: cosa misura davvero Google',
         estratto='LCP, INP e CLS spiegati con esempi di negozi e officine, non di startup. E perché il punteggio desktop non conta quasi nulla.',
         corpo="LCP, INP e CLS sono le tre metriche che Google usa per valutare l’esperienza utente di un sito, e per decidere chi mostrare per primo nei risultati di ricerca mobile. In questo articolo le spieghiamo senza gergo tecnico, con esempi reali di negozi e officine — non di startup — e perché il punteggio desktop, su cui si concentrano ancora molte agenzie, conta ormai quasi nulla.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/cwv-cover.svg',
                    alt='Core Web Vitals nel 2026: LCP, INP e CLS, le tre metriche che Google misura sul mobile')),

    # ---- Mese 1 del piano contenuti (piano-contenuti-seo.md §4.3) ----
    dict(slug='quanto-costa-ecommerce-italia', data='13 LUG 2026',
         titolo='Quanto costa un e-commerce in Italia nel 2026: le cifre vere',
         estratto='Dai 6.000 ai 25.000 euro e oltre: cosa cambia davvero tra le fasce, quali costi ricorrenti nessuno mette nel preventivo, e le domande da fare prima di firmare.',
         corpo="«Quanto costa un e-commerce?» è la domanda con cui inizia quasi ogni nostra prima telefonata. La risposta onesta è una forchetta larga — sul mercato italiano da 6.000 a 25.000 euro e oltre — perché due negozi online con lo stesso numero di prodotti possono nascondere complessità completamente diverse. In questo articolo mettiamo in fila le cifre reali del mercato 2026, i costi che i preventivi tacciono e i tre fattori che spostano davvero il prezzo.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/costo-ecom-cover.svg',
                    alt='Quanto costa un e-commerce in Italia nel 2026: le fasce di prezzo dai 6.000 ai 25.000 euro e oltre'),
         cta=('Vedi il nostro listino e-commerce, prezzi chiusi', '/prezzi/'),
         sezioni=[
             dict(titolo='Le fasce di prezzo del mercato italiano',
                  paragrafi=[
                      "I listini pubblici delle agenzie italiane nel 2026 raccontano un mercato su tre fasce. Sotto i 3.000 euro si trovano negozi montati su template con configurazione minima: funzionano finché non serve personalizzare il checkout o collegare il gestionale. La fascia centrale — 6.000–15.000 euro — copre un e-commerce professionale su misura: catalogo strutturato, pagamenti multipli, SEO tecnica delle pagine prodotto. Sopra i 15.000 si va verso cataloghi complessi, integrazioni con ERP e logistica, multi-lingua e multi-valuta.",
                      "Il nostro listino sta nella fascia centrale — € 7.500–14.000, prezzo chiuso nel preventivo — con una differenza contrattuale: PageSpeed 90+ garantito per iscritto e data di consegna con penale. Sono le due voci che nelle offerte concorrenti non troverete quasi mai nero su bianco.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/costo-ecom-fasce.svg',
                              alt='Le tre fasce di prezzo di un e-commerce in Italia e i costi ricorrenti spesso fuori dal preventivo',
                              caption='Le fasce del mercato italiano 2026: template (sotto € 3.000), professionale su misura (€ 6.000–15.000, dove sta il nostro listino € 7.500–14.000) e complesso (oltre € 15.000). Ai costi di costruzione si aggiungono manutenzione (€ 500–2.000 l’anno) e commissioni sui pagamenti (1,5–3%). Fonte: listini pubblici delle web agency italiane, 2026.')),
             dict(titolo='I costi che i preventivi non dicono',
                  paragrafi=[
                      "Il prezzo di costruzione è metà della storia. Un e-commerce vivo costa ogni anno: hosting adeguato ai picchi, aggiornamenti di sicurezza, commissioni sui pagamenti (tipicamente 1,5–3% a transazione), fatturazione elettronica, e la manutenzione del catalogo. Sul mercato la manutenzione professionale viaggia tra i 500 e i 2.000 euro l’anno: chiedete sempre cosa è incluso e per quanto tempo.",
                      "Nel nostro caso i primi 12 mesi di assistenza, aggiornamenti e misurazioni mensili sono inclusi nel prezzo di costruzione. Dopo, il canone è facoltativo — oppure il negozio resta a voi così com’è: codice e dati sono vostri dal primo giorno.",
                  ]),
             dict(titolo='I tre fattori che spostano il prezzo',
                  lista=[
                      'Catalogo: non quanti prodotti avete, ma quante varianti, listini e regole di prezzo (B2B vs B2C) il negozio deve gestire.',
                      'Integrazioni: gestionale, corrieri, magazzino esterno. Ogni sistema collegato è lavoro di sviluppo e di test, non una casella da spuntare.',
                      'Lingue e mercati: vendere in Germania non è tradurre le schede — è IVA, spedizioni, resi e testi che un madrelingua deve adattare al mercato.',
                  ],
                  paragrafi=[
                      "Un catalogo tradotto da madrelingua e un checkout ridotto a un solo passaggio sono le due leve che spostano più vendite dirette in un e-commerce che vende all'estero: lo applichiamo agli stessi progetti multilingue che il gruppo Remarka costruisce per sé — casi reali, con link al progetto vivo, in /casi-studio/.",
                  ]),
             dict(titolo='Le domande da fare prima di firmare',
                  lista=[
                      'Il prezzo è chiuso o «indicativo»? Cosa succede se emergono lavori aggiuntivi?',
                      'La data di consegna è nel contratto? Con quale penale?',
                      'Chi possiede dominio, codice e dati dei clienti dopo la consegna?',
                      'La fatturazione elettronica via SDI è inclusa o è un modulo a parte?',
                      'Quanto carica il sito su mobile — e chi lo garantisce, per iscritto?',
                  ]),
         ]),
    dict(slug='sito-lento-cause-costi', data='13 LUG 2026',
         titolo='Sito lento: le 7 cause reali (e quanto costa sistemarle)',
         estratto='Perché un sito carica in 5 secondi nel 2026, quali interventi costano poco e rendono molto, e quando invece conviene rifare la base tecnica.',
         corpo="Quattro secondi di caricamento su mobile sembrano un dettaglio tecnico. Non lo sono: sono il motivo per cui le campagne portano visite che se ne vanno prima di vedere la prima riga. Dopo decine di audit su siti di PMI italiane, le cause della lentezza sono quasi sempre le stesse sette — e non tutte costano care da sistemare. Eccole, in ordine di frequenza, con l’ordine di grandezza dell’intervento.",
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/sito-lento-cover.svg',
                    alt='Sito lento: le sette cause reali e quanto costa sistemarle'),
         cta=('Misura il tuo sito adesso — test gratuito', '/strumenti/test-velocita/'),
         sezioni=[
             dict(titolo='Le sette cause, dalla più frequente',
                  lista=[
                      'Immagini non ottimizzate: fotografie da 3–8 MB caricate così come escono dal telefono. È la causa №1 e la più economica da correggere.',
                      'Hosting inadeguato: server condivisi sovraffollati che rispondono in 1–2 secondi prima ancora di iniziare a caricare la pagina.',
                      'Tema o template sovraccarico: page builder che caricano 2 MB di codice per mostrare tre colonne di testo.',
                      'Plugin accumulati negli anni: ogni plugin attivo aggiunge codice, richieste e rischi di sicurezza — ne abbiamo contati fino a 60 su un solo sito.',
                      'Font e script esterni: sei famiglie di caratteri e dieci servizi di tracciamento che bloccano la prima visualizzazione.',
                      'Nessuna cache configurata: il server ricostruisce da zero ogni pagina, per ogni visitatore, ogni volta.',
                      'Base tecnica vecchia: versioni PHP obsolete e database mai ottimizzati — qui il singolo intervento non basta più.',
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/sito-lento-7cause.svg',
                              alt='Le sette cause di un sito lento, dalla più frequente, con il costo dell’intervento basso, medio o alto',
                              caption='Le sette cause più frequenti di un sito lento e il costo dell’intervento: quasi tutte si risolvono a costo basso, solo la base tecnica vecchia richiede un lavoro più profondo. Fonte: decine di audit su siti di PMI italiane (Studio Remarka).')),
             dict(titolo='Cosa costa poco e rende molto',
                  paragrafi=[
                      "Le prime due cause — immagini e hosting — si risolvono spesso in giornata e da sole possono dimezzare i tempi di caricamento. La compressione moderna (AVIF/WebP con caricamento progressivo) taglia il peso delle fotografie dell’80% a parità di qualità visibile: è spesso, da sola, l’ottimizzazione con il rapporto costo/beneficio più alto in un audit.",
                      "Cache e pulizia dei plugin sono il secondo gradino: mezza giornata di lavoro, risultati misurabili subito. Il punto è misurare prima e dopo — non «il sito sembra più veloce», ma un numero documentato.",
                  ]),
             dict(titolo='Quando il restyling tecnico conviene davvero',
                  paragrafi=[
                      "Se il vostro sito somma le cause 3, 4 e 7 — tema pesante, plugin stratificati, base vecchia — ottimizzare pezzo per pezzo è come cambiare le gomme a un motore fuso: ogni intervento costa e il risultato resta mediocre. In questi casi il restyling tecnico (stessi contenuti, base nuova, redirect 301 per non perdere il posizionamento) parte da € 2.900 e porta il sito sopra i 90 di PageSpeed — garantiti da contratto, non promessi.",
                      "Il primo passo è gratuito in entrambi i casi: misurate il sito con il nostro test di velocità, oppure chiedete l’analisi completa — un report scritto con le cause, le priorità e un preventivo chiuso.",
                  ]),
         ]),

    # ---- Blog · Batch 1 (sputniki dei nuovi strumenti e servizi) — IT + EN ----
    # Illustrazioni: SVG di marca in assets/img/blog/ (griglia carta, palette
    # remarka.css, tipografia di sistema). Condivise IT/EN: etichette neutre
    # (numeri, acronimi, token tecnici, coppie bilingui) — le frasi e le
    # didascalie stanno nell'HTML, tradotte dal conveyor (CHROME_BLOG in
    # chrome_strings.py). Le versioni EN/RU sono pagine separate: IT+EN via
    # translate_pages.py en; RU del blog è un batch successivo a parte
    # (piano-blog.md, batch 5–6), non una traduzione di queste.
    dict(slug='european-accessibility-act-ecommerce', data='15 LUG 2026',
         titolo='EAA 2026: cosa rischia davvero il vostro e-commerce',
         estratto='Dal 28 giugno 2025 l’accessibilità è un obbligo di legge, con sanzioni fino al 5% del fatturato. Chi è coinvolto, chi resta fuori e da dove partire, senza allarmismi.',
         corpo='Il 28 giugno 2025 è passato in sordina, e proprio per questo fa più danni. Da quella data l’European Accessibility Act è una legge applicata anche in Italia, e tocca molti più e-commerce di quanti se ne siano accorti: se vendete online a dei consumatori, con ogni probabilità il vostro negozio deve essere usabile anche dalle persone con disabilità — non come cortesia, ma per obbligo, con sanzioni che il recepimento italiano fissa fino al 5% del fatturato. Niente panico e niente finta indifferenza: vediamo cosa rischia davvero il vostro e-commerce, chi resta fuori e cosa conviene fare adesso.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/eaa-cover.svg',
                    alt='European Accessibility Act e-commerce: la scadenza del 28 giugno 2025, lo standard WCAG 2.1 AA e la sanzione fino al 5% del fatturato'),
         cta=('Adeguamento EAA: audit, correzioni e dichiarazione in 3 settimane', '/servizi/adeguamento-eaa/'),
         sezioni=[
             dict(titolo='Che cos’è l’European Accessibility Act, in parole vostre',
                  paragrafi=[
                      "L’European Accessibility Act (EAA) nasce dalla direttiva europea 2019/882, e l’idea è persino ovvia una volta detta. Un negozio fisico con tre gradini all’ingresso e nessuna rampa lascia fuori una parte dei clienti; un e-commerce con contrasti illeggibili, immagini senza descrizione e un checkout che non si completa da tastiera fa esattamente la stessa cosa, solo che non si vede. La norma chiede che i servizi digitali venduti ai consumatori siano usabili anche da chi ha una disabilità visiva, motoria o cognitiva.",
                      "In Italia la direttiva è stata recepita e si applica dal 28 giugno 2025. Lo standard di riferimento non è un’opinione: sono le WCAG 2.1 di livello AA, le stesse linee guida internazionali che i tecnici usano da anni. Non è una moda partita ieri, è un percorso cominciato nel 2019 e arrivato a scadenza adesso.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/eaa-timeline.svg',
                              alt='Cronologia dell’European Accessibility Act: direttiva UE 2019/882, recepimento in Italia, entrata in vigore il 28 giugno 2025 e sanzione massima del 5%',
                              caption='Dalla direttiva UE 2019/882 all’entrata in vigore in Italia il 28 giugno 2025. Le microimprese di servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato — hanno un’esenzione. Fonti: AccessibleEU (Commissione europea) e la guida di Bird & Bird.')),
             dict(titolo='Cosa rischia davvero il vostro e-commerce con l’European Accessibility Act',
                  paragrafi=[
                      "Partiamo dai soldi, perché è la domanda vera. Il recepimento italiano prevede sanzioni fino al 5% del fatturato per i servizi non conformi: su un negozio che fattura 800.000 euro l’anno sono fino a 40.000 euro, più di quanto costi rifare il sito da zero. Non è un rischio teorico. In Francia, dove l’applicazione è partita prima, le prime cause verso i grandi rivenditori online sono già arrivate; in Italia la vigilanza è appena cominciata, e le prime segnalazioni sono una questione di mesi, non di anni.",
                      "Ma la sanzione è la parte che spaventa di più, non quella che pesa di più. Un e-commerce inaccessibile perde clienti ogni giorno, in silenzio, molto prima che arrivi un controllo. Pensate a chi ci vede poco e non riesce a leggere un grigio chiaro elegante, a chi naviga da telefono con una mano sola, a chi compila l’ordine da tastiera perché il mouse gli è scomodo: ogni barriera è un carrello abbandonato che nei vostri report non comparirà mai come «problema di accessibilità». Lo leggerete come «tasso di conversione basso», e darete la colpa al prezzo.",
                  ]),
             dict(titolo='Siete obbligati? La regola delle microimprese',
                  paragrafi=[
                      "La domanda che ci fanno tutti è «vale anche per me?». La risposta onesta è «quasi sempre sì, ma verificate». La norma guarda a chi vende beni o servizi ai consumatori a distanza. Esiste però un’esenzione per le microimprese che erogano servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato annuo. L’esenzione è pensata per i servizi e il perimetro esatto va guardato caso per caso, non a occhio: nel dubbio, meglio una verifica di mezz’ora che una sanzione.",
                  ],
                  lista=[
                      'E-commerce e servizi digitali che vendono a consumatori nell’Unione Europea: è il caso più comune, e il più esposto.',
                      'Banche, assicurazioni, trasporti, biglietterie e sistemi di prenotazione online.',
                      'Aziende che non sono microimprese e che finora hanno trattato l’accessibilità come un dettaglio estetico.',
                  ],
                  links=[('Verifica gratis le barriere del vostro sito', '/strumenti/verifica-accessibilita/')]),
             dict(titolo='Da dove si comincia: le quattro parole che contano',
                  paragrafi=[
                      "Le WCAG 2.1 AA sembrano un muro di sigle, ma poggiano su quattro princìpi semplici, riassunti nell’acronimo POUR: un sito accessibile è percepibile, utilizzabile, comprensibile e robusto. Tradotto in pratica: testo che si legge anche con poca vista, tutto raggiungibile da tastiera, moduli con etichette chiare e messaggi d’errore che spiegano cosa fare, codice pulito che gli screen reader sanno leggere.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/eaa-wcag.svg',
                              alt='I quattro princìpi delle WCAG 2.1 AA: percepibile, utilizzabile, comprensibile, robusto',
                              caption='I quattro princìpi delle WCAG 2.1 AA (POUR). Un audit automatico intercetta circa un terzo di questi criteri; il resto — tastiera, screen reader, contenuti — si verifica a mano.'),
                  ),
             dict(titolo='Tre settimane, dall’audit alla dichiarazione',
                  paragrafi=[
                      "Un controllo automatico gratuito è il primo gradino: in un minuto vi dice se il sito ha già i problemi più evidenti — contrasti, etichette, struttura. Ma la conformità piena non si certifica con un punteggio: serve la verifica manuale (tastiera, screen reader, contenuti) e una dichiarazione di accessibilità pubblicata sul sito, il documento che la norma pretende. Senza dichiarazione, un sito tecnicamente accessibile resta comunque non a norma.",
                      "La buona notizia è che non è un lavoro infinito. Per un e-commerce di taglia media, dall’audit alle correzioni fino alla dichiarazione, sono in genere tre settimane. L’obbligo, preso per tempo, non è un costo a fondo perduto: è un sito che vende a più persone e che non teme la prima lettera del controllo.",
                  ],
                  links=[('Vogliamo sistemarlo noi: il servizio Adeguamento EAA, a prezzo chiuso', '/servizi/adeguamento-eaa/')]),
         ]),

    dict(slug='llms-txt-cos-e', data='15 LUG 2026',
         titolo='llms.txt: cos’è e serve davvero al vostro sito?',
         estratto='Un file di testo che spiega il vostro sito ai modelli AI, come robots.txt fa con Google. Cos’è, come si scrive e quanto conta davvero, senza esagerazioni.',
         corpo='Nel giro di un anno è comparso un nuovo file di cui tutti parlano e che quasi nessuno ha: llms.txt. La promessa è semplice — un foglietto di istruzioni che spiega il vostro sito ai modelli di intelligenza artificiale, come robots.txt fa da vent’anni con i motori di ricerca. Ma serve davvero, o è l’ennesima sigla che qualcuno vi venderà a caro prezzo? Vediamo cos’è llms.txt, come si scrive in mezz’ora e quanto conta oggi, senza gonfiarne l’importanza e senza liquidarlo con un’alzata di spalle.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/llmstxt-cover.svg',
                    alt='llms.txt: cos’è, il file Markdown nella radice del sito che riassume i contenuti per i modelli AI'),
         cta=('Verifica gratis se il vostro sito è pronto per l’AI', '/strumenti/sito-pronto-ai/'),
         sezioni=[
             dict(titolo='llms.txt, cos’è in una frase',
                  paragrafi=[
                      "llms.txt è un file di testo in formato Markdown che mettete nella radice del sito (sito.it/llms.txt) e che riassume, in modo leggibile da una macchina, chi siete, cosa fate e dove trovare le pagine importanti. Nasce come proposta di standard nel 2024 e ha un obiettivo preciso: dare ai modelli linguistici — quelli dietro ChatGPT, Claude, Perplexity — una mappa pulita del sito, senza costringerli a indovinare tra menù, banner e codice.",
                      "L’analogia con robots.txt aiuta, ma non è perfetta. robots.txt dice ai crawler dove possono andare; llms.txt dice loro cosa contano le vostre pagine e come raccontarvi. È la differenza tra un cartello «vietato l’ingresso» e una guida che spiega il museo.",
                  ]),
             dict(titolo='Come è fatto un file llms.txt',
                  paragrafi=[
                      "La parte bella è che si legge e si scrive senza essere programmatori. La struttura è quella di un documento Markdown ordinato: un titolo con il nome dell’azienda, una riga di sintesi, e poi sezioni con link alle pagine che volete far leggere per prime — servizi, chi siamo, contatti, documentazione.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/llmstxt-anatomia.svg',
                              alt='Anatomia di un file llms.txt: titolo H1 obbligatorio, una riga di sintesi, sezioni con link e un blocco opzionale',
                              caption='L’anatomia di un file llms.txt: un titolo (1, obbligatorio), una sintesi in una riga (2), le sezioni con i link alle pagine chiave (3) e un blocco opzionale per il resto (4). Nient’altro: la forza sta nella sobrietà.')),
             dict(titolo='Serve davvero? La risposta onesta',
                  paragrafi=[
                      "Qui evitiamo due bugie speculari. La prima: «llms.txt è indispensabile, senza sei invisibile». Falso. È uno standard giovane, non tutti i modelli lo leggono ancora, e la sua assenza oggi non è un errore grave. La seconda: «è una moda inutile». Anche questa è falsa. Costa mezz’ora, non fa danni, e vi mette dalla parte giusta di un cambiamento che sta accelerando.",
                      "Il modo giusto di leggerlo è questo: llms.txt non vi porta clienti da solo, ma toglie ambiguità. Se un modello prova a raccontare cosa fate, preferite che legga una mappa scritta da voi o che ricostruisca tutto da un menù e da tre banner cookie? La risposta è ovvia, e il costo dell’assicurazione è ridicolo rispetto al rischio di essere descritti male.",
                  ]),
             dict(titolo='llms.txt è un pezzo, non tutta la SEO tecnica',
                  paragrafi=[
                      "Un errore comune è trattare llms.txt come una bacchetta magica. In realtà è l’ultimo arrivato in una famiglia di segnali che esistono da tempo: dati strutturati in JSON-LD, una sitemap aggiornata, contenuti in testo leggibile e non solo in immagini, un robots.txt che non chiude la porta ai crawler giusti. llms.txt è la ciliegina; la torta è la SEO tecnica fatta bene.",
                      "Se non sapete da dove cominciare, cominciate misurando. In un minuto potete verificare se il vostro sito espone già i quattro segnali che i modelli cercano — file llms.txt, accesso dei crawler AI, dati strutturati e sitemap — e capire cosa manca prima di scrivere una sola riga.",
                  ],
                  links=[('Fa parte della SEO tecnica che consegniamo', '/servizi/seo-tecnica/'),
                         ('Create il vostro llms.txt in un minuto: generatore gratuito', '/strumenti/generatore-llms-txt/'),
                         ('Leggi anche: come farsi trovare e citare da ChatGPT', '/blog/farsi-trovare-da-chatgpt-geo/')]),
         ]),

    dict(slug='farsi-trovare-da-chatgpt-geo', data='15 LUG 2026',
         titolo='Come farsi trovare (e citare) da ChatGPT: guida alla GEO',
         estratto='Sempre più persone chiedono a ChatGPT invece che a Google. La GEO è l’arte di farsi citare nelle risposte generate: cosa cambia rispetto alla SEO e cosa fare.',
         corpo='C’è una domanda che un anno fa era da nerd e oggi la fa anche vostro cugino: «l’hai chiesto a ChatGPT?». Sempre più persone cercano una risposta parlando con un assistente AI invece di sfogliare dieci link blu, e questo apre una partita nuova: non basta più essere primi su Google, bisogna essere citati nelle risposte generate. Farsi trovare su ChatGPT, Perplexity e simili ha persino un nome — GEO, Generative Engine Optimization. Vediamo cos’è, in cosa somiglia alla SEO e in cosa se ne allontana, e soprattutto cosa potete fare concretamente.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/geo-cover.svg',
                    alt='Sito visibile su ChatGPT: la GEO (Generative Engine Optimization) e una risposta AI che cita la vostra pagina come fonte'),
         cta=('Verifica gratis se il vostro sito è leggibile dai modelli AI', '/strumenti/sito-pronto-ai/'),
         sezioni=[
             dict(titolo='Perché volete un sito visibile su ChatGPT',
                  paragrafi=[
                      "Quando un modello AI risponde a una domanda, spesso non inventa: legge il web e sintetizza, e nelle risposte migliori indica le fonti con dei rimandi cliccabili. Essere una di quelle fonti significa due cose. La prima, immediata: qualcuno vi legge nel momento esatto in cui sta decidendo. La seconda, più sottile: comparire in una risposta di ChatGPT o Perplexity è un segnale di autorevolezza che si trascina dietro fiducia, anche offline.",
                      "L’errore da evitare è pensare che sia una moda passeggera o roba «da grandi marchi». Il meccanismo premia chi si spiega bene, non chi ha il budget più grosso — ed è esattamente il terreno su cui una PMI ben fatta può battere un concorrente più grande e più pigro.",
                  ]),
             dict(titolo='Come un modello arriva a citare la vostra pagina',
                  paragrafi=[
                      "Il percorso è più semplice di quanto sembri, e capirlo aiuta a lavorarci. Il vostro sito viene letto da crawler specializzati — GPTBot di OpenAI, ClaudeBot, PerplexityBot; questi contenuti alimentano il modello; e quando qualcuno fa una domanda pertinente, il modello costruisce la risposta e, se il vostro testo è chiaro e affidabile, vi cita come fonte.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/geo-flusso.svg',
                              alt='Il flusso della GEO: dal vostro sito ai crawler AI (GPTBot, ClaudeBot, PerplexityBot), al modello, fino alla risposta con la citazione',
                              caption='Il percorso, in quattro passi: il vostro sito (1) viene letto dai crawler AI (2), alimenta il modello (3) e, se il contenuto è chiaro, finisce citato nella risposta (4). Ogni passo ha un modo per andare storto — o per funzionare.')),
             dict(titolo='GEO e SEO: cosa cambia (e cosa no)',
                  paragrafi=[
                      "Buona parte del lavoro è la stessa di sempre: contenuti chiari, struttura tecnica pulita, velocità, dati strutturati. Chi ha già una SEO tecnica solida parte con mezzo lavoro fatto. Ma tre cose diventano più importanti del solito.",
                  ],
                  lista=[
                      'Aprire la porta ai crawler giusti: nel robots.txt non bloccate GPTBot, ClaudeBot, PerplexityBot e Google-Extended se volete comparire nelle risposte generate.',
                      'Scrivere fatti espliciti: i modelli citano ciò che capiscono senza ambiguità. «Realizziamo e-commerce a Milano, consegna in 6 settimane, prezzo chiuso» vale più di «soluzioni digitali su misura per il vostro business».',
                      'Farsi leggere in testo, non in immagini: un dato prezioso dentro una locandina JPG, per un modello, non esiste.',
                  ]),
             dict(titolo='Da dove partire, senza perdersi',
                  paragrafi=[
                      "La GEO non è un servizio a parte da comprare in fretta: è la buona SEO tecnica di sempre, orientata a un lettore nuovo. Il primo passo concreto è verificare se il vostro sito è già leggibile dalle macchine — se espone i dati strutturati, se non sta bloccando i crawler AI, se ha una sitemap in ordine. Da lì si vede subito cosa manca.",
                      "E se volete capire il tassello più discusso di questo mondo — il famoso file llms.txt — l’abbiamo raccontato a parte, senza fumo: cos’è, come si scrive e quanto conta davvero.",
                  ],
                  links=[('Lo prepariamo noi: fa parte della SEO tecnica', '/servizi/seo-tecnica/'),
                         ('Scoprite come l’AI legge davvero il vostro sito — gratis', '/strumenti/sito-letto-dallai/'),
                         ('Leggi anche: llms.txt, cos’è e serve davvero al vostro sito', '/blog/llms-txt-cos-e/')]),
         ]),

    dict(slug='check-up-sito-web-7-misure', data='15 LUG 2026',
         titolo='Check-up del sito web: le 7 misure che contano',
         estratto='Un sito «va bene» o «va male» non si decide a sensazione. Ci sono sette misure che ne raccontano la salute — e un modo per leggerle in un minuto, gratis.',
         corpo='«Secondo voi il nostro sito è messo bene?» È la domanda con cui inizia metà delle nostre chiamate, e la risposta seria non è «sì» o «no»: è «dipende da cosa misurate». Un sito bellissimo può essere lentissimo; uno velocissimo può essere invisibile a Google; uno perfetto per Google può respingere una persona su dieci per un problema di accessibilità. Fare il check-up di un sito web significa guardarlo su più fronti insieme, con dei numeri, non a occhio. Ecco le sette misure che contano davvero, e come leggerle senza diventare tecnici.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/checkup-cover.svg',
                    alt='Check-up del sito web: sette misure in un solo punteggio di salute da 0 a 100'),
         cta=('Fai ora il check-up completo del tuo sito — gratis', '/strumenti/check-up-completo/'),
         sezioni=[
             dict(titolo='Perché un solo numero non basta (e sette sì)',
                  paragrafi=[
                      "Il voto unico rassicura, ma inganna. «PageSpeed 92» dice qualcosa sulla velocità e niente su privacy, accessibilità o prontezza AI. Per questo un check-up serio non guarda una cosa sola: mette in fila sette dimensioni e le pesa, così vedete in un colpo d’occhio dove il sito è solido e dove perde punti — e quali problemi valgono la pena di sistemare per primi.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/checkup-sette.svg',
                              alt='Le sette misure del check-up — prestazioni, SEO, accessibilità, best practice, privacy, prontezza AI, CO₂ — e le fasce di punteggio di salute',
                              caption='Le sette misure e le fasce del punteggio di salute (0–49 critico, 50–74 con margine, 75–89 buono, 90+ eccellente). Quattro dimensioni arrivano dall’API Google PageSpeed; tre — privacy, prontezza AI e CO₂ — sono verifiche nostre. Le prestazioni pesano di più (25), la CO₂ di meno (5).')),
             dict(titolo='Le quattro misure che arrivano da Google',
                  paragrafi=[
                      "Quattro delle sette misure non sono una nostra opinione: arrivano dall’API di Google PageSpeed, la stessa che alimenta pagespeed.web.dev, interrogata in versione mobile perché è quella con cui Google vi posiziona.",
                  ],
                  lista=[
                      'Prestazioni: quanto in fretta la pagina diventa utilizzabile su un telefono. È la voce che pesa di più, ed è quella che decide se le visite restano o scappano.',
                      'SEO tecnica: se titoli, struttura e dati mancanti mettono i bastoni tra le ruote all’indicizzazione.',
                      'Accessibilità: contrasti, etichette, struttura dei titoli — le barriere che dal 2025 sono anche un obbligo di legge.',
                      'Best practice: uso corretto di HTTPS, immagini, console pulita e piccoli segnali di igiene tecnica.',
                  ]),
             dict(titolo='Le tre misure che aggiungiamo noi',
                  paragrafi=[
                      "Le altre tre le calcoliamo direttamente, leggendo il sito come farebbe un visitatore. La conformità privacy la ricaviamo dall’HTML (banner, informative, tracker prima del consenso); la prontezza AI da quattro segnali — llms.txt, accesso dei crawler AI, dati strutturati, sitemap; l’impronta di CO₂ dal peso reale della pagina, con il modello Sustainable Web Design. Sono verifiche indicative, e lo diciamo: il check-up privacy non è un parere legale, e il punteggio non promette una posizione su Google. È una fotografia tecnica precisa, non una promessa di vendita.",
                  ]),
             dict(titolo='Come si legge il voto di salute',
                  paragrafi=[
                      "Il punteggio di salute è la media pesata delle sette misure, e si legge come un semaforo: da 90 in su siete in fascia verde, tra 75 e 89 è buono, tra 50 e 74 c’è margine concreto, sotto 50 è critico e diventa la priorità. Due avvertenze: un voto alto non significa «primi su Google» — significa fondamenta tecniche sane; e se una misura risulta «N/D», di solito non è un guasto vostro, ma un server saturo o una lettura automatica rifiutata.",
                      "La cosa migliore è che tutto questo lo potete misurare da soli, gratis e in meno di un minuto, incollando l’indirizzo del sito. Il report completo, pagina per pagina, arriva in PDF; e se dal check-up esce che vale la pena rifare la base tecnica, il restyling parte da lì — dai numeri, non dalle sensazioni.",
                  ],
                  links=[('Fai il check-up completo, gratis e senza registrazione', '/strumenti/check-up-completo/'),
                         ('Se serve rifare la base: restyling e migrazione', '/servizi/restyling-migrazione/')]),
         ]),

    dict(slug='eeat-come-google-giudica-credibilita', data='15 LUG 2026',
         titolo='E-E-A-T: come Google giudica la vostra credibilità',
         estratto='Esperienza, competenza, autorevolezza, affidabilità: la cornice con cui Google valuta di chi fidarsi. Cos’è l’E-E-A-T e come rafforzarla, senza trucchi.',
         corpo='Se avete letto qualcosa di SEO nell’ultimo anno vi sarà rimbalzato addosso un acronimo dall’aria misteriosa: E-E-A-T. Suona come una password, ed è invece il modo in cui Google prova a rispondere a una domanda molto umana: di questo sito, ci si può fidare? Non è un punteggio segreto e non si compra. È una cornice fatta di quattro parole — esperienza, competenza, autorevolezza, affidabilità — che vale la pena capire, perché tocca da vicino chiunque venda servizi o consigli online. Vediamo cos’è l’E-E-A-T e, soprattutto, cosa potete fare per rafforzarla senza scorciatoie.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/eeat-cover.svg',
                    alt='E-E-A-T cos’è: esperienza, competenza, autorevolezza e affidabilità, i quattro pilastri delle Search Quality Rater Guidelines di Google'),
         cta=('Misura gratis i segnali E-E-A-T del tuo sito', '/strumenti/segnali-eeat/'),
         sezioni=[
             dict(titolo='E-E-A-T, cos’è (e cosa non è)',
                  paragrafi=[
                      "E-E-A-T sta per Experience, Expertise, Authoritativeness, Trust: esperienza, competenza, autorevolezza e affidabilità. Non è un’invenzione dei SEO: è scritto nero su bianco nelle Search Quality Rater Guidelines, il manuale con cui Google istruisce le persone in carne e ossa che valutano la qualità dei risultati. Serve a stimare quanto ci si può fidare di una pagina, soprattutto sui temi che incidono su salute, denaro e sicurezza.",
                      "Attenzione a un equivoco diffuso: l’E-E-A-T non è un fattore di ranking diretto, né un numero che Google vi assegna. È una cornice di qualità che i valutatori umani usano per addestrare gli algoritmi. Rafforzare i segnali di fiducia aiuta indirettamente; ma nessuno strumento — nemmeno il nostro — misura l’E-E-A-T «reale» del vostro sito. Diffidate di chi ve lo promette.",
                  ]),
             dict(titolo='I quattro pilastri, con Trust al centro',
                  paragrafi=[
                      "Le quattro parole non pesano tutte uguale. Nelle linee guida di Google il pilastro centrale è la fiducia (Trust): esperienza, competenza e autorevolezza servono soprattutto a sostenerla. Ha senso: un contenuto può essere scritto da un vero esperto, ma se il sito non è sicuro o non si capisce chi c’è dietro, la fiducia crolla lo stesso.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/eeat-pilastri.svg',
                              alt='I quattro pilastri E-E-A-T — esperienza, competenza, autorevolezza, affidabilità — con gli otto segnali di fiducia leggibili nel codice della pagina',
                              caption='I quattro pilastri E-E-A-T e alcuni segnali concreti che vi finiscono dentro: portfolio e casi studio, pagina «chi siamo», dati strutturati e profili esterni, HTTPS, contatti, P.IVA, privacy. La fiducia (Trust) è il pilastro centrale.')),
             dict(titolo='I segnali che potete davvero controllare',
                  paragrafi=[
                      "La parte buona dell’E-E-A-T è che una fetta è alla vostra portata, subito. Google e i lettori cercano, nella pagina, dei segnali di fiducia leggibili: una connessione sicura in HTTPS, contatti verificabili, l’identità legale (P.IVA e ragione sociale), i link a privacy e cookie policy, una pagina «chi siamo» vera con nomi e volti, un portfolio o dei casi studio, i dati strutturati in JSON-LD e i profili esterni. Sono aggiunte tecniche precise, quasi tutte veloci e a basso costo.",
                      "Quello che nessuna scorciatoia vi darà è l’altra metà: la reputazione, le menzioni, la qualità reale dei contenuti, l’esperienza vissuta di chi scrive. Quella si costruisce con il tempo — ed è esattamente perché non si può falsificare che Google le dà tanto peso.",
                  ]),
             dict(titolo='Da dove partire: misurare, poi sistemare',
                  paragrafi=[
                      "Il modo più rapido per capire come siete messi non è leggere altra teoria, ma guardare cosa espone davvero la vostra home. In un minuto potete misurare gli otto segnali di fiducia leggibili nel codice e vedere su quale dei quattro pilastri conviene intervenire per primo. Da lì, un pomeriggio di lavoro tecnico — una pagina «chi siamo» vera, i contatti nel footer, un blocco di dati strutturati — sposta il punteggio più di quanto immaginate.",
                      "E ricordate la regola che vale per tutto l’E-E-A-T: un sito può dichiarare bene chi è, ma la fiducia vera la costruiscono i contenuti, il tempo e le persone. Gli strumenti misurano i segnali; la credibilità la meritate voi.",
                  ],
                  links=[('Misura gratis gli otto segnali E-E-A-T della tua home', '/strumenti/segnali-eeat/'),
                         ('Chi siamo, contatti e dati strutturati sono di serie nella SEO tecnica', '/servizi/seo-tecnica/')]),
         ]),

    # ---- Blog · Batch 2 (soldi e decisioni del titolare) — IT + EN ----
    # Stesse regole del batch 1: SVG di marca in assets/img/blog/, ≥3 prime
    # fonti autorevoli (blocco «Fonti» + link contestuali, URL verificati),
    # JSON-LD BlogPosting via blog-schema-map, IT+EN (RU è un batch a parte).
    # Le versioni EN sono pagine separate (translate_pages.py en, CHROME_BLOG_BATCH2).
    dict(slug='preventivo-sito-web-come-leggerlo', data='16 LUG 2026',
         titolo='Preventivo sito web: come leggerlo senza sorprese',
         estratto='Tre preventivi per lo stesso sito, tre cifre che non c’entrano niente. La griglia per leggerli riga per riga e le domande da fare prima di firmare.',
         corpo='Avete chiesto tre preventivi per lo stesso sito e vi tornano tre cifre che sembrano parlare di progetti diversi: 2.400, 6.900, 14.000 euro. Vi pare di confrontare mele con biciclette, e in un certo senso è vero. Un preventivo sito web non è il listino del pane: dentro la stessa parola — «sito da dieci pagine» — ci stanno lavori che valgono il triplo l’uno dell’altro. In questo articolo vi diamo la griglia per leggere un preventivo riga per riga, capire dove si nasconde il prezzo vero e quali domande fare prima di firmare, così le sorprese non arrivano in fattura.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/preventivo-cover.svg',
                    alt='Preventivo sito web: come leggerlo riga per riga, le voci che spostano il prezzo e le sorprese da evitare in fattura'),
         cta=('Confronta prezzi e tempi, a listino chiuso', '/prezzi/'),
         sezioni=[
             dict(titolo='Perché due preventivi «uguali» costano il doppio',
                  paragrafi=[
                      "Il malinteso nasce quasi sempre da una parola sola: «pagina». Due preventivi dicono entrambi «sito da dieci pagine», ma uno intende dieci pagine con i vostri testi già pronti da impaginare su un template, l’altro dieci pagine da progettare, scrivere e fotografare su misura. Il secondo costa il doppio e vale il triplo, eppure sul foglio le due righe sembrano identiche. È qui che nasce metà dei «mi hanno chiesto una cifra assurda per la stessa cosa».",
                      "Il prezzo di un sito non lo fanno le pagine, lo fanno tre cose che spesso restano implicite: quanto è su misura il design, quanto lavoro c’è sui contenuti, e cosa viene garantito per iscritto. Un preventivo onesto rende esplicite tutte e tre. Un preventivo furbo le lascia nel vago, così può essere il più basso della pila — e recuperare dopo, quando scoprite che le foto, i testi e la seconda lingua «non erano compresi».",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/preventivo-voci.svg',
                              alt='Le voci di un preventivo sito web: design, sviluppo, contenuti, SEO tecnica, accessibilità e assistenza, e quali fanno oscillare di più il prezzo',
                              caption='Le sei voci che compongono un preventivo sito web. Design e contenuti sono quelle che spostano di più il prezzo; assistenza e accessibilità sono quelle che spesso «spariscono» dalle offerte più basse. Fonte: listini pubblici delle web agency italiane, 2026.')),
             dict(titolo='Le voci che un preventivo sito web deve avere',
                  paragrafi=[
                      "Prima di guardare la cifra in fondo, guardate se ci sono tutte le voci. Un progetto serio si scompone più o meno sempre nello stesso modo, e ogni voce mancante è un costo che tornerà, di solito a lavoro iniziato, quando trattare è più difficile.",
                  ],
                  lista=[
                      'Design e struttura: quanto è su misura e quanto è template. Un tema comprato e adattato è legittimo, ma deve costare come tale, non come un progetto originale.',
                      'Sviluppo e messa online: CMS, moduli, integrazioni, configurazione dell’hosting. Chiedete cosa è incluso e cosa è «a parte».',
                      'Contenuti: testi, foto, eventuali traduzioni. È la voce che i preventivi bassi tengono più bassa, ed è quella che decide se il sito converte o resta una vetrina muta.',
                      'SEO tecnica e velocità: struttura, dati strutturati, PageSpeed. Se non c’è una riga, non è gratis: è che non c’è.',
                      'Accessibilità: dal 28 giugno 2025 è un obbligo di legge per molti siti, non un abbellimento. Un preventivo che non la nomina è vecchio o vi lascia il conto per dopo.',
                      'Assistenza e proprietà: chi possiede dominio, codice e dati dopo la consegna, e cosa copre l’assistenza — per quanto tempo e a quali condizioni.',
                  ]),
             dict(titolo='Prezzo chiuso o «indicativo»? La riga che cambia tutto',
                  paragrafi=[
                      "C’è una differenza sostanziale tra un preventivo «chiuso» e uno «indicativo», e vale più di qualsiasi sconto. Il prezzo chiuso è quello che pagherete: se emergono lavori aggiuntivi, si concordano per iscritto prima, o restano a carico di chi ha fatto il preventivo. Il prezzo indicativo è un punto di partenza che sale in corsa, quando ormai avete investito tempo e non potete tornare indietro.",
                      "La stessa logica vale per i tempi. «Consegna in primavera» non è una data; «consegna il 30, con l’1% di sconto per ogni giorno lavorativo di ritardo» lo è. Chiedete sempre se la data è nel contratto e con quale penale: la risposta, più delle cifre, vi dice con chi avete a che fare. Nel nostro caso il prezzo è bloccato alla firma e la data è scritta con la penale — non per generosità, ma perché è l’unico modo per cui «senza sorprese» significhi qualcosa.",
                  ]),
             dict(titolo='Le sorprese che arrivano dopo: i costi ricorrenti',
                  paragrafi=[
                      "Il prezzo di costruzione è metà della storia. Un sito vivo costa ogni anno, e un preventivo onesto ve lo dice prima. Hosting adeguato, aggiornamenti di sicurezza, manutenzione: sul mercato la manutenzione professionale viaggia tra i 500 e i 2.000 euro l’anno, e cambia molto cosa comprende. Se vendete online si aggiungono le commissioni sui pagamenti e la fatturazione elettronica, che in Italia passa obbligatoriamente dal Sistema di Interscambio dell’Agenzia delle Entrate: assicuratevi che sia inclusa o messa a preventivo, non scoperta a negozio aperto.",
                      "C’è poi un costo che quasi nessun preventivo nomina ancora, ed è un obbligo: l’adeguamento all’European Accessibility Act, in vigore in Italia dal 28 giugno 2025 per i siti che vendono ai consumatori. Non è una voce facoltativa da «vedere più avanti»: è un requisito di legge, con sanzioni. Un preventivo che lo ignora non vi sta facendo risparmiare, vi sta rimandando il conto.",
                  ]),
             dict(titolo='Come leggerlo in pratica: le cinque domande',
                  paragrafi=[
                      "Non serve diventare tecnici. Bastano cinque domande, e il modo in cui vi rispondono conta quanto le risposte: se chi avete davanti si innervosisce, avete già un’informazione.",
                  ],
                  lista=[
                      'Il prezzo è chiuso o indicativo? Cosa succede se in corso d’opera emergono lavori aggiuntivi?',
                      'La data di consegna è nel contratto, e con quale penale in caso di ritardo?',
                      'Contenuti, foto e traduzioni sono inclusi, o sono «a parte»?',
                      'Chi possiede dominio, codice e dati dopo la consegna — io o voi?',
                      'Accessibilità e velocità su mobile sono garantite con un numero, o sono promesse a voce?',
                  ],
                  links=[('Confronta i nostri prezzi e tempi, accanto a quelli di mercato', '/prezzi/'),
                         ('Cosa include davvero un sito aziendale', '/servizi/siti-aziendali/'),
                         ('Prima di rifare: misura la salute del sito attuale', '/strumenti/check-up-completo/'),
                         ('Leggi anche: sito web in 3 settimane, com’è possibile davvero', '/blog/sito-web-in-3-settimane/')]),
         ],
         fonti=[
             ('Agenzia delle Entrate — fatturazione elettronica (SDI)', _S_SDI,
              'La pagina ufficiale sul Sistema di Interscambio: un costo che ogni e-commerce deve mettere a preventivo.'),
             ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
              'Dal 28 giugno 2025 l’accessibilità è un obbligo, non un extra: va considerata nel preventivo.'),
             ('HTTP Archive — Web Almanac 2024', _S_ALMANAC,
              'Dati reali su com’è fatto il web oggi: utile per capire cosa si paga davvero dietro un sito.'),
             ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
              'La velocità mobile che va garantita con un numero: la differenza tra un preventivo serio e uno vago.'),
         ]),

    dict(slug='sito-web-in-3-settimane', data='16 LUG 2026',
         titolo='Sito web in 3 settimane: com’è possibile (davvero)',
         estratto='Il mercato ci mette 6–10 settimane, noi tre. Non è magia né lavoro fatto a metà: è metodo. Ecco cosa succede in ognuna delle tre settimane, e la penale se sforiamo.',
         corpo='«Un sito web in 3 settimane? O è una fregatura, o è un template riempito in fretta.» È la reazione più comune, ed è sana: sul mercato italiano un sito aziendale richiede in media 6–10 settimane, quindi promettere tre suona come promettere di dimagrire dormendo. Eppure lo facciamo, con la data scritta in contratto e una penale se sforiamo. Non c’è nessun trucco e nessun lavoro fatto a metà: c’è un metodo che toglie i tempi morti, non la qualità. Vediamo, giorno per giorno, com’è possibile un sito web in 3 settimane — e cosa serve da parte vostra perché funzioni.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/tresett-cover.svg',
                    alt='Sito web in 3 settimane: le tre settimane dalla firma all’online, analisi, sviluppo e messa online con data in contratto'),
         cta=('Sito aziendale in 3 settimane, prezzo chiuso', '/servizi/siti-aziendali/'),
         sezioni=[
             dict(titolo='Tre settimane non è magia: è togliere i tempi morti',
                  paragrafi=[
                      "Le 6–10 settimane del mercato non sono quasi mai lavoro: sono attesa. Il preventivo che resta indeciso per giorni, i contenuti che arrivano a rate, il design che va avanti e indietro cinque volte perché nessuno ha fissato lo scopo all’inizio. Il tempo se ne va nel ping-pong, non nel produrre. Noi comprimiamo le tre settimane aggredendo proprio quel ping-pong: scopo chiuso alla firma, un solo giro di revisione per fase, contenuti raccolti con voi in un incontro invece che inseguiti per email.",
                      "La seconda leva è banale ma decisiva: partiamo da fondamenta nostre, collaudate su decine di progetti, non da un foglio bianco ogni volta. Questo non vuol dire «tutti i siti uguali»: vuol dire che l’impalcatura tecnica — velocità, accessibilità, struttura SEO — è già solida, e le tre settimane le spendiamo su ciò che è vostro, non a reinventare la ruota.",
                  ]),
             dict(titolo='Settimana 1: analisi, preventivo chiuso, design',
                  paragrafi=[
                      "La prima settimana decide le altre due. Facciamo l’analisi — chi siete, chi volete raggiungere, cosa deve fare il sito — e da lì esce un preventivo chiuso, con prezzo bloccato e data. Poi il design: non venti bozze, ma una direzione condivisa e approvata, così la settimana dopo si sviluppa senza ripensamenti. È la settimana che richiede più presenza da parte vostra, ed è tempo ben speso: ogni decisione presa adesso è un ritardo evitato dopo.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/tresett-timeline.svg',
                              alt='Le tre settimane dalla firma all’online: settimana 1 analisi e design, settimana 2 sviluppo, settimana 3 contenuti, test e messa online',
                              caption='Dalla firma all’online in 21 giorni: analisi e design (settimana 1), sviluppo (settimana 2), contenuti, test e pubblicazione (settimana 3). La data è in contratto: ogni giorno lavorativo di ritardo vale l’1% di sconto. Tempi del sito aziendale; la vetrina è 2 settimane, l’e-commerce 6.')),
             dict(titolo='Settimana 2: sviluppo, con la velocità già dentro',
                  paragrafi=[
                      "Nella seconda settimana il design approvato diventa un sito che funziona. Qui la scelta di partire da fondamenta collaudate paga tutto il suo prezzo: la struttura tecnica che regge la velocità e l’accessibilità è già al suo posto, e lo sviluppo si concentra sulle vostre pagine, non sull’impalcatura. Non rincorriamo il PageSpeed 90+ alla fine come una toppa: lo costruiamo mentre sviluppiamo, perché la velocità non è un ritocco finale ma il modo in cui il sito è fatto.",
                  ]),
             dict(titolo='Settimana 3: contenuti, test, online',
                  paragrafi=[
                      "La terza settimana è quella dei dettagli che si vedono e di quelli che non si vedono. Impaginiamo i contenuti definitivi, poi testiamo: velocità reale su telefono, accessibilità secondo lo standard WCAG 2.1 AA — oggi anche un obbligo di legge — moduli, link, comportamento su schermi diversi. Solo quando i numeri tornano si va online. Un sito veloce che rispetta le persone non è un vezzo: è ciò che Google misura per posizionarvi e ciò che tiene le visite invece di farle scappare.",
                  ],
                  links=[('Verifica la salute di un sito con il check-up completo', '/strumenti/check-up-completo/')]),
             dict(titolo='Cosa non comprimiamo: mai la qualità',
                  paragrafi=[
                      "Tagliamo l’attesa, non i controlli. Le tre settimane non nascono da un lavoro fatto di corsa, ma da un lavoro senza pause morte: mentre voi rileggete una bozza, noi non restiamo fermi, prepariamo la fase successiva. Quello che non salta mai è la parte che protegge voi — i test di velocità e accessibilità, la prova su telefoni veri, il controllo dei moduli e dei link. Se una di queste verifiche non passa, non andiamo online: la data si difende con il metodo, non sacrificando il collaudo.",
                      "C’è un caso in cui tre settimane non bastano, e lo diciamo prima: un progetto con un catalogo grande, molte integrazioni o più lingue richiede più tempo. Non lo nascondiamo per far firmare — lo scriviamo nel preventivo, con la stessa data fissa e la stessa penale. È per questo che le tre settimane valgono per il sito aziendale: la vetrina ne chiede due, l’e-commerce sei. Un numero onesto vale più di un numero piccolo.",
                  ]),
             dict(titolo='E se sforiamo? La penale, e cosa serve da parte vostra',
                  paragrafi=[
                      "La data in contratto vale solo se ha un prezzo: ogni giorno lavorativo di ritardo è l’1% di sconto sul totale. È la ragione per cui prendiamo sul serio le tre settimane, ed è anche la ragione per cui vi chiediamo una cosa in cambio. Il rispetto della data dipende da due mani: perché tre settimane bastino, i contenuti e le decisioni devono arrivare quando li chiediamo, non a lavoro iniziato. La settimana 1 serve proprio a questo — a raccogliere tutto insieme, così le settimane 2 e 3 corrono.",
                      "Chi promette «un sito in una settimana» senza chiedervi niente sta vendendo un template svuotato. Chi vi promette «quando sarà pronto» sta lasciando aperta una porta che costa cara. Tre settimane, con una data e una penale, è il punto onesto tra le due cose: veloce sul serio, ma senza scorciatoie sulla qualità.",
                  ],
                  links=[('Cosa include un sito aziendale, a prezzo chiuso', '/servizi/siti-aziendali/'),
                         ('Prima di firmare: come leggere un preventivo sito web', '/blog/preventivo-sito-web-come-leggerlo/'),
                         ('Sito già online? Restyling o sito nuovo: il test delle 5 domande', '/blog/restyling-o-sito-nuovo-5-domande/')]),
         ],
         fonti=[
             ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
              'La velocità mobile che garantiamo per contratto: il PageSpeed 90+ non è uno slogan, è una soglia misurabile.'),
             ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
              'Dal 2025 l’accessibilità è parte dello scopo di ogni sito nuovo, non un lavoro rimandabile.'),
             ('Google — creare contenuti utili e affidabili', _S_GOOGLE_HELPFUL,
              'Cosa Google considera qualità: lo sfondo del perché testiamo prima di andare online.'),
             ('Google — introduzione ai dati strutturati', _S_GOOGLE_SD,
              'I dati strutturati fanno parte dell’impalcatura tecnica che è già pronta in partenza.'),
         ]),

    dict(slug='restyling-o-sito-nuovo-5-domande', data='16 LUG 2026',
         titolo='Restyling o sito nuovo? Il test delle 5 domande',
         estratto='Rifare tutto o ritoccare? Cinque domande per capire, con i numeri e non a sensazione, se al vostro sito basta un restyling o serve ripartire da zero.',
         corpo='C’è un momento in cui aprite il vostro sito dal telefono e qualcosa stona: carica piano, sembra vecchio, i contatti arrivano col contagocce. La domanda che segue è sempre la stessa — «lo ritocchiamo o lo rifacciamo da capo?» — e la risposta sbagliata costa in entrambe le direzioni: si può buttare via un sito ancora buono, o accanirsi a rattoppare una base ormai fusa. Non è una scelta da fare a sensazione. Bastano cinque domande per capire se al vostro sito serve un restyling o un rifacimento vero — e questo articolo ve le mette in mano.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/restyling-cover.svg',
                    alt='Restyling sito web o sito nuovo: il test delle cinque domande per decidere con i numeri se ritoccare o ripartire da zero'),
         cta=('Restyling e migrazione senza perdere posizioni', '/servizi/restyling-migrazione/'),
         sezioni=[
             dict(titolo='Restyling o rifacimento: non è la stessa spesa',
                  paragrafi=[
                      "Prima di decidere, mettiamo d’accordo le parole. Un restyling lavora sopra una base che tiene: rinnova l’aspetto, riscrive dei contenuti, sistema la velocità e l’accessibilità, ma non demolisce le fondamenta. Un rifacimento rifà la base tecnica da zero — tema, struttura, spesso la piattaforma — e ci riporta sopra i contenuti che meritano di restare. Il primo costa meno e dura meno a farsi; il secondo costa di più ma risolve problemi che nessun ritocco può toccare.",
                      "Sbagliare la diagnosi è la spesa più stupida di tutte. Fare un rifacimento completo quando bastava un restyling è buttare soldi; fare un restyling su una base marcia è come cambiare le gomme a un motore fuso — ogni intervento costa e il risultato resta mediocre. Le cinque domande servono esattamente a non sbagliare questa diagnosi.",
                  ]),
             dict(titolo='Il test delle 5 domande',
                  paragrafi=[
                      "Rispondete con onestà. Più «sì» collezionate, più l’ago si sposta dal restyling verso il sito nuovo. Non è una formula magica, è un modo per guardare in faccia le cose che di solito si evitano.",
                  ],
                  lista=[
                      '1. Il sito è lento su telefono anche dopo aver alleggerito le immagini? Se la lentezza sta nella base — tema pesante, plugin stratificati, PHP vecchio — ritoccare non basta.',
                      '2. Ogni modifica è una battaglia? Se aggiungere una pagina o cambiare un testo richiede un tecnico e mezza giornata, la struttura sta remando contro di voi.',
                      '3. È inutilizzabile o inaccessibile da mobile? Se una persona su due arriva da telefono e fatica, non è un ritocco estetico: è un problema di fondamenta.',
                      '4. La piattaforma è ferma o insicura? Versioni obsolete, aggiornamenti impossibili, avvisi di sicurezza: sono crepe strutturali, non macchie da coprire.',
                      '5. Il sito non dice più cosa siete diventati? Se posizionamento, offerta e pubblico sono cambiati e il sito è rimasto indietro, il problema è la sostanza, non la vernice.',
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/restyling-5domande.svg',
                              alt='Il test delle cinque domande su velocità, facilità di modifica, mobile, piattaforma e messaggio, con l’esito restyling o sito nuovo',
                              caption='Le cinque domande e dove portano: pochi «sì», e concentrati sull’aspetto, indicano un restyling; molti «sì», e sulle fondamenta (velocità, piattaforma, mobile), indicano un sito nuovo. La soglia non è matematica: conta quali domande.')),
             dict(titolo='Quando basta un restyling',
                  paragrafi=[
                      "Se i «sì» sono pochi e riguardano l’aspetto — il sito invecchiato ma ancora rapido, facile da aggiornare, solido sotto il cofano — il restyling è la scelta giusta e la più intelligente. Rinnovate l’immagine, riscrivete i contenuti che vendono, sistemate accessibilità e velocità, e tenete tutto il valore che il sito ha già accumulato su Google. Prima di decidere, però, guardate i numeri e non l’impressione: un check-up del sito misura in un minuto velocità, SEO, accessibilità e privacy, e vi dice se la base regge davvero o se vi sta solo sembrando.",
                  ],
                  links=[('Misura la salute del sito prima di scegliere: check-up completo', '/strumenti/check-up-completo/')]),
             dict(titolo='Quando conviene il sito nuovo (e come non perdere Google)',
                  paragrafi=[
                      "Se i «sì» si accumulano sulle fondamenta — lentezza strutturale, piattaforma insicura, mobile inutilizzabile — il rifacimento non è uno spreco, è la fine di uno spreco. La paura giusta, a quel punto, è una sola: perdere le posizioni guadagnate in anni. È una paura legittima e gestibile. Con una mappa degli URL uno-a-uno e i redirect 301 fatti prima del lancio, il valore delle vecchie pagine si trasferisce alle nuove e il traffico continua come se niente fosse. Il crollo dopo un rifacimento non è una maledizione tecnica: è quasi sempre la conseguenza di redirect mancanti o fatti «tutti alla home».",
                      "Un dettaglio che fa la differenza: la mappa non si improvvisa il giorno del lancio. Si prepara prima, pagina per pagina, e si prova su un ambiente di test. Quando è fatta bene, il passaggio è invisibile ai visitatori e a Google — nessun errore 404, nessuna pagina orfana, nessun calo. Il rifacimento smette di essere un salto nel buio e diventa un trasloco ordinato, con le scatole etichettate.",
                  ],
                  links=[('Come funzionano i redirect quando si cambia sito (Google)', _S_GOOGLE_SITEMOVE)]),
             dict(titolo='Decidere con i numeri, non a sensazione',
                  paragrafi=[
                      "La regola che ripetiamo sempre: prima si misura, poi si decide. Un check-up onesto trasforma «mi sembra vecchio» in una lista di problemi con una priorità, e da lì la scelta tra restyling e sito nuovo diventa quasi ovvia. Se dai numeri esce che la base regge, si ritocca; se esce che è finita, si rifà — e in entrambi i casi si parte da un dato, non da una sensazione o da un venditore che ha già deciso per voi.",
                      "Un ultimo criterio che quasi nessuno considera: il peso. Un sito vecchio è spesso anche un sito pesante, e un sito pesante è lento, costoso da servire e più inquinante. Rifare la base, quando serve, è anche l’occasione per alleggerire — e la velocità che ne esce si vede subito, sul telefono e nei contatti.",
                  ],
                  links=[('Restyling e migrazione, senza perdere posizioni', '/servizi/restyling-migrazione/'),
                         ('Leggi anche: quanto pesa il vostro sito sull’ambiente (e sul portafoglio)', '/blog/impatto-ambientale-sito-web/')]),
         ],
         fonti=[
             ('Google — spostamenti del sito con cambio di URL', _S_GOOGLE_SITEMOVE,
              'La procedura ufficiale per rifare un sito senza perdere il posizionamento su Google.'),
             ('Google — redirect e ricerca Google', _S_GOOGLE_REDIRECTS,
              'Come impostare i redirect 301 perché Google trasferisca il valore delle vecchie pagine alle nuove.'),
             ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
              'Le metriche di velocità con cui distinguere un sito ancora buono da uno da rifare.'),
             ('Sustainable Web Design — stima delle emissioni', _S_SWD,
              'Il modello che lega il peso della pagina al consumo: un sito vecchio è spesso anche pesante.'),
         ]),

    dict(slug='impatto-ambientale-sito-web', data='16 LUG 2026',
         titolo='Quanto pesa il vostro sito sull’ambiente (e sul portafoglio)',
         estratto='Ogni visita consuma energia e produce CO₂. Come si misura l’impatto ambientale di un sito web, perché leggero vuol dire anche veloce ed economico, e cosa c’entra la CSRD.',
         corpo='Un sito web sembra immateriale, ma non lo è: ogni volta che qualcuno lo apre, dei byte viaggiano da un data center alla sua schermata, e quel viaggio consuma energia. Moltiplicate per decine di migliaia di visite al mese e l’«immateriale» diventa una bolletta e un po’ di anidride carbonica. La buona notizia è che l’impatto ambientale di un sito web si può stimare, e che ridurlo coincide quasi sempre con renderlo più veloce e meno costoso. Vediamo come si misura, cosa c’entrano i vostri conti e la nuova rendicontazione europea, e cosa potete fare in un pomeriggio.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/impatto-cover.svg',
                    alt='Impatto ambientale sito web: dal peso della pagina in byte all’energia consumata e ai grammi di CO₂ per visita'),
         cta=('Misura ora l’impronta di CO₂ del tuo sito — gratis', '/strumenti/impatto-co2/'),
         sezioni=[
             dict(titolo='Un sito ha un peso, e il peso ha un costo',
                  paragrafi=[
                      "Il peso di una pagina è la somma di tutto ciò che il browser deve scaricare per mostrarla: immagini, caratteri, script, video. Più è pesante, più energia serve per trasferirla e visualizzarla — nel data center, lungo la rete, sul dispositivo di chi guarda. Quell’energia ha due prezzi paralleli: uno ambientale, in grammi di CO₂, e uno economico, in server più cari, campagne che portano visite che scappano, e clienti che se ne vanno prima di vedere la prima riga perché il telefono arranca.",
                      "È il motivo per cui parliamo di ambiente e portafoglio nello stesso respiro: non sono due discorsi, è lo stesso discorso. La pagina che inquina di più è, quasi sempre, la stessa che carica più lentamente e costa di più mantenere.",
                  ]),
             dict(titolo='Come si stima l’impatto ambientale di un sito web',
                  paragrafi=[
                      "Non è una sensazione, è un calcolo. Si parte da un dato misurabile — il peso della pagina in byte — e gli si applica un modello che traduce i byte trasferiti in energia e poi in grammi di CO₂ equivalente. Il modello più usato è il Sustainable Web Design, reso disponibile dalla Green Web Foundation nella libreria open source co2.js: gli stessi strumenti che stanno dietro ai calcolatori di emissioni del web. Il riferimento comodo è la media: una pagina web produce intorno agli 0,8 grammi di CO₂ per visita. Sotto quella soglia siete leggeri; sensibilmente sopra, c’è margine per alleggerire.",
                      "Serve onestà sui limiti, perché qui è facile vendere fumo. È una stima con coefficienti medi mondiali: non conosce l’energia reale del vostro hosting né il comportamento di ogni visitatore. Non è un’impronta certificata, è un ordine di grandezza affidabile e confrontabile — e il suo pregio è proprio che si aggancia a un fatto tecnico su cui potete davvero intervenire: il peso.",
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/impatto-peso.svg',
                              alt='Dal peso della pagina ai grammi di CO₂: byte trasferiti, energia consumata, emissioni per visita e stima annua col modello Sustainable Web Design',
                              caption='Dal peso ai grammi: i byte trasferiti diventano energia e poi CO₂ per visita, moltiplicata per il traffico dà la stima annua. Riferimento: media del web ≈ 0,8 g per visita. Modello: Sustainable Web Design (co2.js, Green Web Foundation).')),
             dict(titolo='Perché leggero vuol dire veloce e più economico',
                  paragrafi=[
                      "Alleggerire una pagina e velocizzarla sono la stessa operazione, vista da due lati. Ogni byte tolto è meno energia trasferita — quindi meno CO₂ — e insieme meno tempo di caricamento, quindi più visite che restano. Le fotografie non ottimizzate sono quasi sempre la voce più pesante: convertirle nei formati moderni può tagliarne l’80% a parità di qualità visibile, e con esse taglia emissioni, costi di banda e secondi di attesa. Non dovete scegliere tra fare bene al pianeta e fare bene ai conti: è la stessa leva.",
                      "Un esempio tipico da un audit: una home da 6 megabyte, quasi tutti in fotografie non compresse, portata a poco più di 1 megabyte senza togliere una sola immagine — solo formati moderni e caricamento differito. Il risultato è triplo: pagina più veloce di alcuni secondi su telefono, banda risparmiata ogni mese e un’impronta di CO₂ per visita più che dimezzata. Un solo intervento, tre benefici — ambiente, velocità e costi — che vanno sempre nella stessa direzione.",
                  ]),
             dict(titolo='La CO₂ entra anche nei bilanci: la CSRD',
                  paragrafi=[
                      "Fino a ieri l’impatto ambientale di un sito era una questione di sensibilità. Da poco è anche una voce che può finire in un bilancio. La direttiva europea sulla rendicontazione di sostenibilità — la CSRD — allarga di molto la platea delle aziende che devono rendicontare i propri impatti ambientali, e chi ha questo obbligo lo estende ai fornitori. Se lavorate con o dentro aziende soggette alla CSRD, un sito misurabile e leggero smette di essere un vezzo e diventa un dato che qualcuno vi chiederà. Meglio arrivarci con un numero in mano che con un’alzata di spalle.",
                      "Diciamolo con onestà, come sempre: il nostro strumento dà una stima indicativa, non un audit certificato per una rendicontazione ufficiale. Ma è il primo passo giusto — vi dice dove siete e quanto margine avete, prima ancora di parlare con un consulente.",
                  ],
                  links=[('La direttiva CSRD sulla rendicontazione di sostenibilità (EUR-Lex)', _S_CSRD)]),
             dict(titolo='Cosa potete fare in un pomeriggio',
                  paragrafi=[
                      "Non serve rifare tutto per vedere il numero scendere. Le prime mosse sono semplici e rendono subito.",
                  ],
                  lista=[
                      'Alleggerite le immagini: convertitele in WebP o AVIF con caricamento differito. È quasi sempre l’intervento con il rapporto costo/beneficio più alto.',
                      'Tagliate script e font superflui: ogni libreria di terze parti e ogni famiglia di caratteri in più è energia trasferita a ogni visita.',
                      'Sfruttate cache e CDN: evitano di ritrasferire gli stessi contenuti mille volte, meno traffico ripetuto e meno consumo.',
                      'Scegliete un hosting alimentato da rinnovabili: abbassa l’intensità di carbonio di ogni byte servito, con effetto immediato.',
                  ],
                  links=[('Misura gratis l’impronta di CO₂ del tuo sito', '/strumenti/impatto-co2/'),
                         ('Vogliamo alleggerirlo noi: restyling e migrazione', '/servizi/restyling-migrazione/'),
                         ('Leggi anche: sito lento, le 7 cause reali (e quanto costa sistemarle)', '/blog/sito-lento-cause-costi/')]),
         ],
         fonti=[
             ('Sustainable Web Design — stima delle emissioni', _S_SWD,
              'Il modello con cui si calcola l’impronta di CO₂ dal peso reale della pagina.'),
             ('Green Web Foundation — CO2.js', _S_CO2JS,
              'La libreria open source che traduce i byte trasferiti in grammi di CO₂ equivalente.'),
             ('Direttiva (UE) 2022/2464 — CSRD (EUR-Lex)', _S_CSRD,
              'Il testo ufficiale della rendicontazione di sostenibilità che allarga gli obblighi ambientali alle imprese.'),
             ('HTTP Archive — Web Almanac 2024', _S_ALMANAC,
              'Dati reali sul peso delle pagine: dove si concentra davvero il consumo del web.'),
             ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
              'Perché un sito leggero è anche veloce: le metriche che legano peso, velocità ed esperienza.'),
         ]),

    dict(slug='dichiarazione-di-accessibilita-guida-2026', data='16 LUG 2026',
         titolo='Dichiarazione di accessibilità: guida pratica 2026',
         estratto='È il documento che la legge pretende, e che un sito accessibile senza non è a norma. Cos’è la dichiarazione di accessibilità, cosa deve contenere e gli errori da evitare.',
         corpo='C’è un documento di cui pochi parlano e che, dal 2025, molti siti devono avere: la dichiarazione di accessibilità. È la parte meno appariscente dell’adeguamento all’European Accessibility Act, e proprio per questo la più dimenticata — con una beffa dentro: un sito tecnicamente accessibile, ma senza dichiarazione pubblicata, resta comunque non a norma. In questa guida pratica vediamo cos’è la dichiarazione di accessibilità, cosa deve contenere per essere seria e non un copia-incolla, gli errori più comuni, e come si arriva a pubblicarla senza affidarsi a un punteggio automatico.',
         cover=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/dichiarazione-cover.svg',
                    alt='Dichiarazione di accessibilità: il documento richiesto dall’European Accessibility Act, cosa deve contenere e dove pubblicarlo'),
         cta=('Adeguamento EAA: audit, correzioni e dichiarazione in 3 settimane', '/servizi/adeguamento-eaa/'),
         sezioni=[
             dict(titolo='Cos’è la dichiarazione di accessibilità (e perché è obbligatoria)',
                  paragrafi=[
                      "La dichiarazione di accessibilità è un documento pubblico in cui il sito dichiara, in chiaro, quanto è accessibile: quale standard applica, cosa funziona, cosa non è ancora a posto e a chi scrivere per segnalare un problema. Non è un attestato che vi date da soli per bellezza: è il modo in cui la norma vi chiede di prendere una posizione verificabile davanti a chi usa il sito, comprese le persone con disabilità.",
                      "L’obbligo nasce dall’European Accessibility Act — la direttiva europea 2019/882 — applicato in Italia dal 28 giugno 2025 per molti siti che vendono beni o servizi ai consumatori. Lo standard tecnico di riferimento sono le WCAG 2.1 di livello AA. E qui sta il punto che sorprende di più: la conformità non si esaurisce nel rendere il sito accessibile, chiede anche di dichiararlo. Senza il documento, il lavoro tecnico non basta.",
                  ],
                  links=[('L’European Accessibility Act, il testo ufficiale (EUR-Lex)', _S_EURLEX_EAA)]),
             dict(titolo='Cosa deve contenere: l’anatomia di una dichiarazione seria',
                  paragrafi=[
                      "Il World Wide Web Consortium, l’ente che scrive gli standard del web, indica cosa una dichiarazione dovrebbe sempre avere — e mette a disposizione perfino un generatore gratuito. Tradotto in pratica, gli elementi che non possono mancare sono pochi e chiari.",
                  ],
                  lista=[
                      'L’impegno all’accessibilità: una frase che dichiara che vi rivolgete anche alle persone con disabilità, non un preambolo di circostanza.',
                      'Lo standard applicato: quale livello WCAG (di norma 2.1 AA) avete preso come riferimento.',
                      'Lo stato di conformità: cosa è accessibile e — onestà — quali parti non lo sono ancora, senza nascondere i limiti.',
                      'Un contatto per le segnalazioni: un indirizzo vero a cui una persona può scrivere se trova una barriera, con l’impegno a rispondere.',
                      'La data e l’aggiornamento: quando è stata redatta e revisionata, perché un sito cambia e la dichiarazione deve seguirlo.',
                  ],
                  figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/dichiarazione-anatomia.svg',
                              alt='L’anatomia di una dichiarazione di accessibilità: impegno, standard WCAG 2.1 AA, stato di conformità, parti non accessibili, contatto e data',
                              caption='I cinque elementi che una dichiarazione di accessibilità dovrebbe sempre avere: impegno, standard applicato, stato di conformità, parti non ancora accessibili e contatto per le segnalazioni, con data di redazione. Fonte: W3C/WAI, «Developing an Accessibility Statement».'),
                  links=[('La guida e il generatore gratuito del W3C/WAI', _S_WAI_STATEMENT)]),
             dict(titolo='Gli errori più comuni',
                  paragrafi=[
                      "Le dichiarazioni che vediamo sbagliano quasi sempre negli stessi modi. Il primo: il copia-incolla scaricato da un altro sito, con dati che non c’entrano nulla — vale meno di niente, e in caso di controllo si nota subito. Il secondo: la dichiarazione «perfetta» che giura conformità totale mentre il sito è pieno di barriere, cioè una promessa che smentisce sé stessa alla prima prova. Il terzo: il gergo da avvocati e da tecnici, illeggibile per la persona a cui dovrebbe servire — «non soddisfa il criterio 1.2.2» invece di «i video non hanno i sottotitoli». Il quarto: nasconderla, così ben sepolta nel footer che nessuno la trova. Una dichiarazione onesta e imperfetta vale più di una perfetta e falsa.",
                  ]),
             dict(titolo='Non basta un punteggio: la dichiarazione viene dopo l’audit',
                  paragrafi=[
                      "C’è un equivoco da smontare: «ho passato il test automatico, sono a posto». No. Un controllo automatico gratuito è un ottimo primo gradino — in un minuto scova contrasti, etichette e struttura — ma intercetta circa un terzo dei criteri WCAG: quello che una macchina sa misurare. Il resto — navigazione da tastiera, esperienza con uno screen reader, chiarezza dei contenuti — si verifica solo a mano. Una dichiarazione seria si scrive dopo un audit vero, non incollando il numero di uno strumento.",
                      "Per questo l’ordine giusto è preciso: prima l’audit, automatico e manuale; poi le correzioni; poi la dichiarazione che racconta con onestà il risultato; infine una verifica finale. Chi vi vende la dichiarazione senza l’audit vi sta vendendo una cornice senza il quadro.",
                  ],
                  links=[('Verifica gratis le barriere del vostro sito', '/strumenti/verifica-accessibilita/'),
                         ('Guida EAA per il commercio online (Bird & Bird)', _S_BIRDBIRD_EAA)]),
             dict(titolo='Come la prepariamo noi, in tre settimane',
                  paragrafi=[
                      "Nel nostro servizio la dichiarazione non è un foglio a parte, è l’ultimo passo di un percorso. Settimana 1: audit automatico e manuale, con il perimetro esatto delle barriere. Settimana 2: correzioni — contrasti, etichette dei moduli, gerarchia dei titoli, navigazione da tastiera. Settimana 3: redazione e pubblicazione della dichiarazione di accessibilità, e un audit di verifica che conferma lo standard WCAG 2.1 AA a correzioni fatte. Prezzo chiuso dopo l’audit, data in contratto con penale, come per ogni nostro lavoro.",
                      "Se avete un e-commerce e volete capire prima cosa rischiate davvero — chi è obbligato, chi resta fuori, quali sanzioni — l’abbiamo raccontato a parte, senza allarmismi. La dichiarazione è il traguardo; ma il viaggio comincia dal sapere se, e quanto, l’obbligo vi riguarda.",
                  ],
                  links=[('Vogliamo sistemarlo noi: il servizio Adeguamento EAA, a prezzo chiuso', '/servizi/adeguamento-eaa/'),
                         ('Leggi anche: EAA 2026, cosa rischia davvero il vostro e-commerce', '/blog/european-accessibility-act-ecommerce/')]),
         ],
         fonti=[
             ('W3C/WAI — Developing an Accessibility Statement', _S_WAI_STATEMENT,
              'La guida ufficiale del W3C, con un generatore gratuito: cosa una dichiarazione deve contenere.'),
             ('Direttiva (UE) 2019/882 (EUR-Lex)', _S_EURLEX_EAA,
              'Il testo dell’European Accessibility Act: da qui nasce l’obbligo, dichiarazione compresa.'),
             ('WCAG 2.1 — W3C', _S_WCAG21,
              'Lo standard tecnico di riferimento (livello AA) che la dichiarazione deve citare.'),
             ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
              'Il centro di competenza UE sull’accessibilità: conferma l’entrata in vigore del 28 giugno 2025.'),
             ('Guida EAA per il commercio online — Bird & Bird', _S_BIRDBIRD_EAA,
              'Uno studio legale internazionale spiega perimetro, esenzioni e obblighi per chi vende online.'),
         ]),
]

# ============================================================================
# Ретрофит блога 15.07 (piano-blog.md, требования владельца — правила 4 и 4-бис).
# Отдельный проход по ВСЕМ 13 статьям: (1) внешние авторитетные первоисточники
# — контекстные ссылки в тексте + блок «Fonti» (≥3 на статью); (2) обогащение
# содержимого и оживление лидов старых статей до уровня батча 1 (6 коротких
# статей разворачиваются в полноформатные sezioni). JSON-LD BlogPosting —
# отдельно (functions.php + inc/blog-schema-map.php). URL проверены
# (search-index corroboration): только реальные первоисточники, ничего не
# выдумано. Внешние ссылки → target="_blank" rel="noopener".
# Все итальянские текстовые узлы, добавленные здесь, имеют EN-пары в
# chrome_strings.py (CHROME_BLOG_RETROFIT) — конвейер translate_pages.py en
# закрывается без непереведённых узлов.
# ----------------------------------------------------------------------------

# --- Bank di prime fonti autorevoli: definito sopra BLOG_POSTS (i batch 2+
#     referenziano le costanti inline nei dict, quindi devono precedere la lista). ---

# --- Blocchi «Fonti» per articolo (etichetta, URL, frase di contesto). ---
_BLOG_FONTI = {
    'european-accessibility-act-ecommerce': [
        ('Direttiva (UE) 2019/882 (EUR-Lex)', _S_EURLEX_EAA,
         'Il testo ufficiale dell’European Accessibility Act: da qui nasce l’obbligo.'),
        ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
         'Il centro di competenza UE sull’accessibilità conferma l’entrata in vigore del 28 giugno 2025.'),
        ('WCAG 2.1 — W3C', _S_WCAG21,
         'Lo standard tecnico di riferimento (livello AA): i criteri con cui si misura la conformità.'),
        ('Guida EAA per il commercio online — Bird & Bird', _S_BIRDBIRD_EAA,
         'Uno studio legale internazionale spiega perimetro, esenzioni e sanzioni per chi vende online.'),
    ],
    'llms-txt-cos-e': [
        ('La proposta llms.txt (llmstxt.org)', _S_LLMSTXT,
         'La specifica originale del formato: cosa contiene un file llms.txt e a cosa serve.'),
        ('OpenAI — panoramica dei crawler', _S_OPENAI_BOTS,
         'La documentazione ufficiale su GPTBot e sugli altri bot di OpenAI, con le regole robots.txt.'),
        ('Anthropic — ClaudeBot e come bloccarlo', _S_ANTHROPIC,
         'Come Anthropic dichiara il proprio crawler e come i siti possono consentirlo o escluderlo.'),
        ('Google — panoramica dei crawler (Google-Extended)', _S_GOOGLE_CRAWLERS,
         'L’elenco ufficiale degli user-agent Google, incluso Google-Extended per gli usi AI.'),
    ],
    'farsi-trovare-da-chatgpt-geo': [
        ('Google — le funzionalità AI e il vostro sito', _S_GOOGLE_AI,
         'Come Google usa i contenuti del web nelle risposte generative e cosa possono fare i siti.'),
        ('OpenAI — panoramica dei crawler', _S_OPENAI_BOTS,
         'Se GPTBot non può leggervi, ChatGPT non può citarvi: qui le regole di accesso.'),
        ('Anthropic — ClaudeBot e come gestirlo', _S_ANTHROPIC,
         'La stessa logica per Claude: l’accesso del crawler è il presupposto della citabilità.'),
        ('Google — introduzione ai dati strutturati', _S_GOOGLE_SD,
         'I dati strutturati JSON-LD aiutano macchine e modelli a capire chi siete e cosa offrite.'),
    ],
    'check-up-sito-web-7-misure': [
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'La definizione delle metriche di velocità ed esperienza che pesano di più nel check-up.'),
        ('Google — contenuti utili e affidabili (E-E-A-T)', _S_GOOGLE_HELPFUL,
         'La guida ufficiale a cosa Google considera qualità: è lo sfondo della dimensione SEO.'),
        ('WCAG 2 — panoramica W3C/WAI', _S_WAI_WCAG,
         'Lo standard dietro la misura di accessibilità, oggi anche obbligo di legge nell’UE.'),
        ('Sustainable Web Design — stima delle emissioni', _S_SWD,
         'Il modello con cui calcoliamo l’impronta di CO₂ dal peso reale della pagina.'),
        ('Chrome UX Report (CrUX)', _S_CRUX,
         'I dati di campo di Google sugli utenti reali, alla base delle metriche di velocità.'),
    ],
    'eeat-come-google-giudica-credibilita': [
        ('Google — creare contenuti utili e affidabili', _S_GOOGLE_HELPFUL,
         'La pagina dove Google definisce l’E-E-A-T e spiega cosa valuta nella qualità.'),
        ('Google — introduzione ai dati strutturati', _S_GOOGLE_SD,
         'I dati strutturati JSON-LD sono uno dei segnali di identità più facili da aggiungere.'),
        ('Google — le funzionalità AI e il vostro sito', _S_GOOGLE_AI,
         'Perché credibilità e chiarezza contano anche nelle risposte generate dall’AI.'),
    ],
    'quanto-costa-ecommerce-italia': [
        ('HTTP Archive — Web Almanac 2024', _S_ALMANAC,
         'Dati reali su peso, tecnologie e prestazioni dei siti, e-commerce compresi.'),
        ('Eurostat — statistiche sull’e-commerce', _S_EUROSTAT_ECOM,
         'Quanto vende online l’Europa: il contesto di mercato dietro le cifre di un negozio.'),
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'La velocità mobile che difendiamo per contratto e che incide sulle vendite.'),
        ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
         'Dal 2025 l’accessibilità è un costo-obbligo anche per l’e-commerce: va messo nel preventivo.'),
    ],
    'sito-lento-cause-costi': [
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'Le metriche con cui Google misura la velocità percepita di una pagina.'),
        ('web.dev — Largest Contentful Paint (LCP)', _S_WEBDEV_LCP,
         'Cos’è l’LCP e perché immagini e hosting lo spostano più di ogni altra cosa.'),
        ('HTTP Archive — Web Almanac 2024', _S_ALMANAC,
         'Dati aggregati sul peso delle pagine: dove si concentra davvero la lentezza del web.'),
        ('Chrome UX Report (CrUX)', _S_CRUX,
         'I dati di campo che distinguono un sito «che sembra veloce» da uno veloce davvero.'),
    ],
    'sito-quattro-lingue-costi-tempi': [
        ('CSA Research — «Can’t Read, Won’t Buy»', _S_CSA,
         'Lo studio classico: la maggioranza dei consumatori compra solo nella propria lingua.'),
        ('Google — siti multi-regionali e multilingue', _S_GOOGLE_MULTIREG,
         'La guida ufficiale a come strutturare un sito per più Paesi e più lingue.'),
        ('Google — versioni localizzate e hreflang', _S_GOOGLE_HREFLANG,
         'Come dire a Google quale versione linguistica mostrare a chi: dettaglio tecnico che conta.'),
        ('Eurostat — statistiche sull’e-commerce', _S_EUROSTAT_ECOM,
         'Il peso dell’e-commerce transfrontaliero in Europa, il mercato che una versione estera apre.'),
    ],
    'cookie-banner-checklist-garante-2026': [
        ('Garante Privacy — linee guida sui cookie', _S_GARANTE_COOKIE,
         'Le regole italiane su banner e consenso: la fonte diretta della checklist.'),
        ('EDPB — report della cookie banner taskforce', _S_EDPB_COOKIE,
         'Il documento europeo che uniforma cosa è lecito e cosa no in un banner.'),
        ('Regolamento (UE) 2016/679 — GDPR (EUR-Lex)', _S_GDPR,
         'Il testo del GDPR: la base giuridica di consenso libero, specifico e documentabile.'),
    ],
    'migrare-wordpress-senza-perdere-seo': [
        ('Google — spostamenti del sito con cambio di URL', _S_GOOGLE_SITEMOVE,
         'La procedura ufficiale per una migrazione che non perde posizioni.'),
        ('Google — redirect e ricerca Google', _S_GOOGLE_REDIRECTS,
         'Come impostare i redirect 301 perché Google trasferisca il valore delle vecchie pagine.'),
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'Dopo la migrazione la velocità va rimisurata: sono le metriche che Google guarda.'),
    ],
    'pwa-per-pmi-quando-app-non-serve': [
        ('web.dev — Progressive Web Apps', _S_WEBDEV_PWA,
         'Cos’è una PWA e cosa la distingue da un sito normale e da un’app nativa.'),
        ('MDN — Progressive Web Apps', _S_MDN_PWA,
         'La documentazione tecnica di riferimento su installabilità, offline e notifiche.'),
        ('web.dev — Learn PWA', _S_WEBDEV_LEARN_PWA,
         'Il corso di Google che spiega, passo per passo, come funziona una PWA.'),
    ],
    'quanto-costa-sito-aziendale-italia': [
        ('HTTP Archive — Web Almanac 2024', _S_ALMANAC,
         'Dati reali su come è fatto il web oggi: utile per capire cosa si paga davvero.'),
        ('Eurostat — statistiche sull’economia digitale', _S_EUROSTAT_ECOM,
         'Il contesto europeo in cui un sito aziendale deve rendere.'),
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'La velocità mobile che garantiamo per contratto: la differenza tra le fasce di prezzo.'),
        ('AccessibleEU — Commissione europea', _S_ACCESSIBLEEU,
         'Dal 2025 l’accessibilità è un requisito, non un extra: va considerata nel budget.'),
    ],
    'core-web-vitals-2026': [
        ('web.dev — Web Vitals', _S_WEBDEV_VITALS,
         'La pagina di Google che introduce e definisce i Core Web Vitals.'),
        ('web.dev — Largest Contentful Paint (LCP)', _S_WEBDEV_LCP,
         'La metrica di caricamento: soglia buona sotto 2,5 secondi.'),
        ('web.dev — Interaction to Next Paint (INP)', _S_WEBDEV_INP,
         'La metrica di reattività che dal 2024 ha sostituito il vecchio FID.'),
        ('web.dev — Cumulative Layout Shift (CLS)', _S_WEBDEV_CLS,
         'La metrica di stabilità visiva: soglia buona sotto 0,1.'),
        ('Chrome UX Report (CrUX)', _S_CRUX,
         'I dati di campo su utenti reali, quelli che Google usa davvero per posizionarvi.'),
    ],
}

# --- Link contestuali esterni da agganciare a sezioni già esistenti
#     (articoli batch 1 + i due articoli «Mese 1»): {slug: {indice_sez: [(label,url)]}}. ---
_BLOG_EXT_LINKS = {
    'european-accessibility-act-ecommerce': {
        0: [('Direttiva (UE) 2019/882, il testo ufficiale su EUR-Lex', _S_EURLEX_EAA)],
        4: [('WCAG 2.1 AA, i criteri ufficiali del W3C', _S_WCAG21)],
    },
    'llms-txt-cos-e': {
        0: [('La specifica llms.txt su llmstxt.org', _S_LLMSTXT)],
    },
    'farsi-trovare-da-chatgpt-geo': {
        0: [('Come Google usa i contenuti nelle risposte AI', _S_GOOGLE_AI)],
    },
    'check-up-sito-web-7-misure': {
        1: [('Web Vitals, la definizione di Google', _S_WEBDEV_VITALS)],
    },
    'eeat-come-google-giudica-credibilita': {
        0: [('E-E-A-T, la definizione ufficiale di Google', _S_GOOGLE_HELPFUL)],
    },
    'quanto-costa-ecommerce-italia': {
        0: [('Dati di mercato reali: Web Almanac 2024 di HTTP Archive', _S_ALMANAC)],
    },
    'sito-lento-cause-costi': {
        1: [('Perché la velocità mobile conta: Web Vitals', _S_WEBDEV_VITALS)],
    },
}

# --- Lead ravvivati (scena, «voi», numeri) per le 6 vecchie schede brevi.
#     Fatti e slug invariati: cambiano solo apertura e tono, al livello del
#     batch 1. Il vecchio `corpo` diventa questo, più ricco. ---
_BLOG_LEAD_NEW = {
    'core-web-vitals-2026':
        "Il titolare di un’officina apre il sito dal telefono, in pausa pranzo, sotto rete mobile: conta i secondi, sbuffa, chiude. Non era un cliente vero, era lui — ma il gesto è identico a quello di chi vi cercava sul serio e se n’è andato. LCP, INP e CLS sono le tre sigle con cui Google misura proprio quel momento, e con cui decide chi mostrare per primo nella ricerca da mobile. Le spieghiamo senza gergo, con esempi di negozi e officine e non di startup, e vi diciamo perché il punteggio desktop — su cui molte agenzie insistono ancora — non conta quasi più nulla.",
    'quanto-costa-sito-aziendale-italia':
        "«Mi hanno chiesto 900 euro e mi hanno chiesto 12.000 per la stessa cosa. Chi mi sta prendendo in giro?» Nessuno dei due, quasi sempre: è che «un sito aziendale» in Italia vuol dire dieci prodotti diversi con lo stesso nome. Il mercato va dagli 800 euro dei costruttori fai-da-te ai 50.000 delle grandi agenzie, e nessuno vi spiega davvero cosa cambia in mezzo. In questo articolo mettiamo una mappa onesta sotto ogni fascia di prezzo — incluso il nostro — e le domande da fare prima di firmare qualunque preventivo.",
    'pwa-per-pmi-quando-app-non-serve':
        "«Ci serve un’app.» Nove volte su dieci, quando ce lo sentiamo dire, la risposta onesta è: forse no. Un’app nativa costa in media 15.000–30.000 euro, va mantenuta due volte — iOS e Android — e ogni aggiornamento passa dalla revisione degli store. Una PWA, cioè un sito «progressivo», si installa sul telefono, funziona offline e manda notifiche a una frazione di quel costo. Vediamo i tre casi in cui a una PMI conviene davvero, e i due in cui invece un’app nativa serve ancora.",
    'cookie-banner-checklist-garante-2026':
        "Aprite dieci siti italiani a caso e contate: in almeno sette il pulsante «Rifiuta» è nascosto, minuscolo o non c’è proprio. È esattamente il punto su cui il Garante Privacy ha smesso di chiudere un occhio. La regola è semplice — «Rifiuta» deve pesare quanto «Accetta», il consenso dev’essere documentabile — ma è ignorata dalla maggioranza dei banner che analizziamo. Ecco la checklist punto per punto che usiamo per verificare un sito, e come costruiamo i nostri banner perché siano a norma dal primo giorno.",
    'migrare-wordpress-senza-perdere-seo':
        "C’è un momento, in ogni rifacimento, in cui il sito nuovo va online e quello vecchio sparisce. Se qualcuno ha sbagliato i redirect, in quel momento spariscono anche anni di posizionamento su Google — e ve ne accorgete due settimane dopo, quando le richieste calano e nessuno sa perché. Migrare da WordPress senza perdere le posizioni non è fortuna: è un protocollo. Vi mostriamo l’audit, la mappa degli URL e i redirect 301 che applichiamo prima di ogni migrazione, cosa monitoriamo nelle prime sei settimane e un caso in cui il traffico non si è mosso di un punto.",
    'sito-quattro-lingue-costi-tempi':
        "Un cliente tedesco apre la vostra scheda prodotto tradotta con l’automatico, legge una frase che nella sua lingua suona goffa, e chiude: non ha pensato «traduzione sbagliata», ha pensato «azienda poco seria». È così che un errore di registro costa un ordine prima ancora di una mail. La traduzione automatica basta per un menù o un orario; non basta dove si vende. In questo articolo: quando conviene l’automatico, quando serve un madrelingua, e cosa cambia davvero nei costi e nei tempi per lingua, con un caso reale del gruppo Remarka.",
}

# --- Sezioni complete per le 6 schede brevi: le portano a 1000–1500 parole,
#     con la vivacità del batch 1. Niente <strong> nelle voci di lista (un
#     nodo di testo per voce, traduzione pulita). Link interni + esterni
#     contestuali dentro le sezioni; il blocco «Fonti» è aggiunto a parte. ---
_BLOG_SEZIONI_NEW = {
    'core-web-vitals-2026': [
        dict(titolo='LCP, INP e CLS: le tre sigle, tradotte',
             paragrafi=[
                 "LCP (Largest Contentful Paint) misura quanto tempo passa prima che compaia il contenuto più grande della pagina — di solito la foto di apertura o il titolo. È la domanda «quanto devo aspettare per vedere qualcosa di utile?». Sotto i 2,5 secondi è considerato buono; sopra i 4, la maggior parte delle persone ha già valutato se restare. Per un negozio di mobili, l’LCP è la prima fotografia del divano; per un’officina, il numero di telefono in alto.",
                 "INP (Interaction to Next Paint) misura la reattività: tocco un pulsante, quanto ci mette il sito a rispondere? Dal 2024 ha sostituito il vecchio FID come metrica ufficiale, ed è la più sottovalutata. CLS (Cumulative Layout Shift) misura invece la stabilità: quante volte, mentre la pagina carica, gli elementi «saltano» e vi fanno cliccare la cosa sbagliata. Chi ha provato a premere «Aggiungi al carrello» e ha comprato un altro prodotto perché la pagina si è mossa sa esattamente di cosa parliamo.",
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/cwv-soglie.svg',
                         alt='Le soglie «buono», «da migliorare» e «scarso» di LCP, INP e CLS',
                         caption='Le soglie dei tre Core Web Vitals. LCP sotto 2,5 secondi e CLS sotto 0,1 sono i valori citati nell’articolo; l’INP sotto 200 ms è la soglia «buono» ufficiale. Fonte: web.dev (Google), Web Vitals.')),
        dict(titolo='Perché il punteggio mobile è l’unico che conta',
             paragrafi=[
                 "Molte agenzie mostrano ancora con orgoglio il punteggio desktop: 98, verde brillante, complimenti. Peccato che Google indicizzi e posizioni i siti in versione mobile da anni, e che i vostri clienti vi cerchino dal telefono, spesso sotto rete lenta e con dieci schede aperte. Il punteggio che conta è quello mobile, misurato in quelle condizioni — non quello desktop preso in ufficio con la fibra.",
                 "Ecco perché nei nostri contratti la soglia è una sola e chiara: PageSpeed 90+ su mobile, garantito per iscritto. Non «faremo il possibile»: un numero, verificabile da chiunque con lo stesso strumento pubblico di Google.",
             ]),
        dict(titolo='Dati di laboratorio o dati reali: la differenza che cambia tutto',
             paragrafi=[
                 "C’è un equivoco che rovina metà delle discussioni sui Core Web Vitals. Esistono due tipi di misura: i dati di laboratorio (Lighthouse simula un caricamento in condizioni controllate) e i dati di campo (il Chrome UX Report raccoglie i tempi reali degli utenti veri, con i loro telefoni e le loro reti). Google, per posizionarvi, guarda i dati di campo. Un sito può segnare 95 in laboratorio e arrancare sul campo, perché i vostri clienti non hanno tutti l’iPhone nuovo e la fibra.",
             ],
             lista=[
                 'Misurate su mobile, non su desktop: è la versione che Google usa per posizionarvi.',
                 'Guardate i dati di campo (CrUX), non solo il punteggio istantaneo di laboratorio.',
                 'Trattate LCP, INP e CLS come tre problemi diversi: si risolvono con interventi diversi.',
                 'Ricontrollate dopo ogni modifica pesante: un plugin o uno slider nuovo possono buttare giù tutto.',
             ]),
        dict(titolo='Cosa fare oggi, in mezz’ora',
             paragrafi=[
                 "Non serve un progetto per iniziare a capire come siete messi. Incollate l’indirizzo nel nostro test di velocità e leggete i tre valori: se l’LCP è alto, quasi sempre il colpevole sono immagini pesanti o un hosting lento; se salta il CLS, mancano le dimensioni fissate su immagini e banner; se l’INP è alto, c’è troppo codice di terze parti che blocca il telefono. Da lì sapete se basta una giornata di ottimizzazione o se conviene rifare la base — e in entrambi i casi partite da un numero, non da una sensazione.",
             ],
             links=[('Misura ora i Core Web Vitals del tuo sito — gratis', '/strumenti/test-velocita/'),
                    ('Sito lento? Le 7 cause reali e quanto costa sistemarle', '/blog/sito-lento-cause-costi/')]),
    ],
    'quanto-costa-sito-aziendale-italia': [
        dict(titolo='Le fasce di prezzo, senza giri di parole',
             paragrafi=[
                 "Sotto i 1.000 euro si comprano quasi sempre template montati in fretta: un costruttore fai-da-te o un conoscente «che sa fare i siti». Funzionano finché non vi serve modificarli, posizionarli o farli caricare in fretta su mobile. Nella fascia 2.500–8.000 euro sta il grosso del mercato professionale italiano: design su misura, CMS per aggiornare da soli, SEO tecnica, più lingue. Sopra i 15.000 si va verso strutture complesse, integrazioni con gestionali e progetti multi-sede.",
                 "Il nostro listino per il sito aziendale sta nella fascia centrale — € 3.900–5.800, prezzo chiuso nel preventivo — con due voci che altrove raramente trovate nero su bianco: PageSpeed 90+ garantito e data di consegna con penale dell’1% per ogni giorno lavorativo di ritardo.",
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/costo-sito-fasce.svg',
                         alt='Le tre fasce di prezzo di un sito aziendale in Italia: fai-da-te sotto i 1.000 euro, professionale tra 2.500 e 8.000, complesso oltre i 15.000',
                         caption='Le fasce del mercato italiano 2026: fai-da-te (sotto € 1.000), professionale (€ 2.500–8.000, dove sta il nostro listino € 3.900–5.800) e complesso (oltre € 15.000). Fonte: listini pubblici delle web agency italiane, 2026.')),
        dict(titolo='Cosa cambia davvero tra una fascia e l’altra',
             paragrafi=[
                 "Il prezzo non lo fa il numero di pagine: lo fanno tre cose. La prima è il design — un tema comprato e riempito costa un decimo di un’interfaccia disegnata sui vostri contenuti, e si vede. La seconda è la base tecnica: un sito che carica in un secondo su mobile richiede lavoro che un template non fa da solo. La terza sono i contenuti veri — testi scritti, foto fatte, traduzioni da madrelingua — che sono spesso la parte che manca nei preventivi troppo bassi, e che poi vi ritrovate a pagare a parte.",
             ]),
        dict(titolo='Le domande da fare prima di firmare',
             paragrafi=[
                 "Un preventivo onesto risponde a queste domande senza esitare. Se chi avete davanti si innervosisce, avete già un’informazione.",
             ],
             lista=[
                 'Il prezzo è chiuso o «indicativo»? Cosa succede se in corso d’opera emergono lavori aggiuntivi?',
                 'La data di consegna è scritta nel contratto? Con quale penale in caso di ritardo?',
                 'Chi possiede dominio, codice e contenuti dopo la consegna: io o voi?',
                 'La velocità su mobile è garantita con un numero, o è solo una promessa a voce?',
                 'L’assistenza dopo il lancio è inclusa, per quanto tempo, e cosa copre esattamente?',
             ]),
        dict(titolo='Un requisito nuovo che nessuno mette a preventivo',
             paragrafi=[
                 "Dal 28 giugno 2025 l’accessibilità dei siti che vendono ai consumatori è un obbligo di legge europeo, non un abbellimento. Un preventivo che non ne parla o è vecchio, o vi lascia il conto per dopo. Nel nostro caso lo standard WCAG 2.1 AA è parte del lavoro, non un extra a sorpresa: preferiamo dirlo prima, in cifre, che scoprirlo insieme davanti a una segnalazione.",
             ],
             links=[('Confronta prezzi e tempi, accanto a quelli di mercato', '/prezzi/'),
                    ('Cosa include davvero un sito aziendale', '/servizi/siti-aziendali/')]),
    ],
    'pwa-per-pmi-quando-app-non-serve': [
        dict(titolo='Cos’è una PWA, senza gergo',
             paragrafi=[
                 "PWA sta per Progressive Web App: è un sito web normale, che si apre nel browser, ma costruito in modo da comportarsi come un’app. La persona che lo visita può «installarlo» sullo schermo del telefono con un tocco, senza passare dallo store; da lì si apre a tutto schermo, funziona anche con rete debole o assente, e — dove serve — manda notifiche. Niente download da 80 MB, niente recensione di Apple o Google da aspettare: è il vostro sito, con i superpoteri giusti.",
             ]),
        dict(titolo='I tre casi in cui conviene davvero',
             paragrafi=[
                 "Una PWA non è la risposta a tutto. Ma in questi tre casi, per una PMI, è quasi sempre la scelta giusta — più economica e più veloce da mantenere di un’app nativa.",
             ],
             lista=[
                 'Serve una scorciatoia sul telefono del cliente abituale: un ristorante che prende prenotazioni, un negozio con un catalogo che si consulta spesso.',
                 'I clienti usano il sito anche dove la rete è ballerina: fiere, magazzini, cantieri, zone di campagna.',
                 'Il budget non regge due app separate per iOS e Android più la loro manutenzione: la PWA è una sola, e vive dove vive il sito.',
             ]),
        dict(titolo='I due casi in cui serve ancora un’app nativa',
             paragrafi=[
                 "Onestà prima di tutto: a volte l’app nativa serve davvero. Il primo caso è quando il prodotto vive di funzioni profonde del telefono — fotocamera avanzata, sensori, elaborazione pesante offline, giochi. Il secondo è quando la presenza nello store è essa stessa un canale di vendita e di fiducia, e i clienti si aspettano di trovarvi lì. Fuori da questi due casi, un’app nativa è spesso un costo di prestigio che una PWA copre con meno soldi e meno grattacapi.",
             ]),
        dict(titolo='Quanto si risparmia, in numeri',
             paragrafi=[
                 "Un’app nativa richiede due basi di codice, due pubblicazioni, due cicli di aggiornamento e le commissioni degli store: è per questo che parte da 15.000 euro e non smette più di costare. Una PWA parte dallo stesso sito che già vi serve, aggiunge le funzioni progressive e vive di un solo aggiornamento per tutti. Il consiglio pratico: prima di firmare per un’app, chiedetevi quali funzioni «da app» vi servono davvero. Spesso la risposta sta comodamente dentro una PWA — e i soldi risparmiati diventano contenuti e pubblicità.",
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/pwa-confronto.svg',
                         alt='Confronto tra sito, PWA e app nativa per installabilità, uso offline, notifiche, store e costo di partenza',
                         caption='Sito, PWA e app nativa a confronto: la PWA aggiunge installabilità, offline e notifiche partendo dallo stesso sito, mentre un’app nativa parte da € 15.000. Fonti: web.dev e MDN sulle Progressive Web App.'),
             links=[('Come realizziamo i siti PWA', '/servizi/siti-pwa/'),
                    ('Quando invece serve una web app su misura', '/servizi/web-app/')]),
    ],
    'cookie-banner-checklist-garante-2026': [
        dict(titolo='Le regole del Garante, in chiaro',
             paragrafi=[
                 "Il principio è uno solo: il consenso ai cookie non necessari dev’essere una scelta libera. Da qui discendono le regole pratiche del Garante e delle linee guida europee. «Rifiuta» deve avere lo stesso peso visivo di «Accetta»: stesso colore, stesse dimensioni, stessa distanza dal dito. Chiudere il banner con la X equivale a rifiutare, non ad accettare. Nessun cookie di profilazione può partire prima che la persona abbia detto sì. E il consenso va conservato, così da poterlo dimostrare se qualcuno lo chiede.",
             ]),
        dict(titolo='La checklist, punto per punto',
             paragrafi=[
                 "Questi sono i controlli che facciamo su ogni sito prima di dire se il banner è a norma. Passateli sul vostro: bastano cinque minuti.",
             ],
             lista=[
                 'Il pulsante «Rifiuta» è visibile al primo colpo, con lo stesso peso di «Accetta».',
                 'Nessuno script di tracciamento (Google Analytics, pixel, mappe) parte prima del consenso.',
                 'Chiudere il banner o navigare senza scegliere non vale come consenso.',
                 'Esiste un modo semplice per cambiare idea dopo: un link «preferenze cookie» sempre raggiungibile.',
                 'C’è una cookie policy chiara, che elenca i cookie e le loro finalità.',
                 'Il consenso viene registrato e resta documentabile nel tempo.',
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/cookie-checklist.svg',
                         alt='La checklist del cookie banner a norma in sei punti e gli errori più comuni',
                         caption='I sei controlli di un cookie banner a norma e i tre errori che troviamo più spesso. Fonte: Garante Privacy, linee guida sui cookie.')),
        dict(titolo='Gli errori che troviamo più spesso',
             paragrafi=[
                 "Tre errori tornano quasi sempre. Il primo: il banner con solo «Accetta» ben visibile e il rifiuto sepolto in un sottomenu — è la violazione più comune e la più facile da contestare. Il secondo: gli analytics che partono al caricamento, prima di qualunque clic, perché installati «al volo» anni fa e mai più toccati. Il terzo: il cookie wall, cioè «accetta o non entri», che salvo casi rari non è una scelta libera e quindi non è un consenso valido.",
             ]),
        dict(titolo='Come costruiamo un banner a norma',
             paragrafi=[
                 "Nei nostri siti il banner nasce già conforme: due pulsanti di pari peso, nessuno script prima del consenso, preferenze modificabili in ogni momento e registro dei consensi. Non è un plugin incollato all’ultimo, è parte del progetto. E se avete già un sito, la verifica è il primo passo: il nostro controllo indicativo vi dice in un minuto se banner, policy e tracker sono a posto — poi, se serve, si sistema.",
             ],
             links=[('Controlla gratis cookie e tracker del tuo sito', '/strumenti/check-gdpr/'),
                    ('Privacy e conformità sono parte della SEO tecnica', '/servizi/seo-tecnica/')]),
    ],
    'migrare-wordpress-senza-perdere-seo': [
        dict(titolo='Cosa si rischia davvero in una migrazione',
             paragrafi=[
                 "Google conosce le vostre pagine con i loro indirizzi attuali. Cambiate struttura, dominio o piattaforma senza dirglielo nel modo giusto, e per Google metà del sito «è sparita»: le vecchie pagine restituiscono errore, le posizioni guadagnate in anni evaporano, e il traffico organico cala proprio mentre festeggiate il sito nuovo. Non è una maledizione tecnica: è quasi sempre la conseguenza di redirect mancanti o sbagliati.",
             ]),
        dict(titolo='Il protocollo prima del cambio',
             paragrafi=[
                 "Una migrazione sicura si prepara prima di toccare qualsiasi cosa. Il lavoro vero è qui, non il giorno del lancio.",
             ],
             lista=[
                 'Audit del sito attuale: quali pagine portano traffico e posizioni, quali link puntano al sito.',
                 'Mappa degli URL: ogni vecchio indirizzo abbinato al suo nuovo, senza lasciare pagine orfane.',
                 'Redirect 301 uno-a-uno: ogni vecchia pagina rimanda a quella nuova equivalente, non tutte alla home.',
                 'Controllo di sitemap, canonical e dati strutturati sul sito nuovo, prima di pubblicare.',
                 'Piano di rollback: se qualcosa va storto, si torna indietro in minuti, non in giorni.',
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/migrare-301.svg',
                         alt='Redirect 301 uno-a-uno che trasferisce il valore SEO contro il redirect «tutto alla home» che lo perde',
                         caption='Ogni vecchia pagina va rimandata alla sua nuova equivalente (1→1): il redirect «tutto alla home» disperde le posizioni. Fonte: Google Search Central, spostamenti del sito e redirect.')),
        dict(titolo='Le prime sei settimane dopo',
             paragrafi=[
                 "Il lancio non è la fine, è l’inizio del monitoraggio. Nelle prime sei settimane Google riscansiona il sito e ricalcola le posizioni: è normale un piccolo assestamento, non è normale un crollo. Teniamo d’occhio gli errori di scansione, le pagine che perdono posizioni, i redirect che non funzionano, e correggiamo in giornata. È la differenza tra un calo di tre giorni e un problema che si trascina per mesi.",
             ]),
        dict(titolo='Un caso reale',
             paragrafi=[
                 "Su un sito con anni di posizionamento locale, la migrazione a una base tecnica nuova è passata con il traffico organico invariato: stesse posizioni, stessi contatti, più velocità. Nessun miracolo — solo il protocollo, applicato con pazienza. Se state pensando a un rifacimento o a un cambio di piattaforma, il momento per parlarne è prima, non dopo il primo calo.",
             ],
             links=[('Restyling e migrazione senza perdere posizioni', '/servizi/restyling-migrazione/'),
                    ('Fai il check-up del sito prima di migrare', '/strumenti/check-up-completo/')]),
    ],
    'sito-quattro-lingue-costi-tempi': [
        dict(titolo='Quando la traduzione automatica basta (e quando no)',
             paragrafi=[
                 "La traduzione automatica di oggi è ottima per capire e farsi capire su cose semplici: un orario, un indirizzo, la descrizione neutra di un servizio. Se il vostro obiettivo è che un turista trovi il numero di telefono, va benissimo. Il problema nasce dove le parole vendono: una scheda prodotto tecnica, una pagina che deve convincere, un testo dove il tono conta quanto il contenuto. Lì l’automatico produce frasi «giuste ma spente», e a volte errori di registro che, nella lingua del cliente, suonano goffi o poco professionali.",
             ]),
        dict(titolo='Cosa cambia nei costi e nei tempi, per lingua',
             paragrafi=[
                 "Aggiungere una lingua non è schiacciare un pulsante «traduci». È tradurre i testi con un madrelingua, adattare quelli di vendita, tradurre anche ciò che non si vede — titoli, descrizioni per Google, messaggi di errore — e impostare i segnali tecnici (hreflang) che dicono al motore quale versione mostrare a chi. Il costo cresce con le parole reali da lavorare, non con il numero di bandierine; i tempi, con il numero di pagine che devono davvero convincere, non solo informare.",
             ]),
        dict(titolo='L’errore che costa clienti: tradurre senza localizzare',
             paragrafi=[
                 "Tradurre è cambiare le parole; localizzare è cambiare ciò che serve perché il messaggio funzioni in quel mercato. Un prezzo con la valuta giusta, una data nel formato locale, un esempio che in Germania si capisce e in Italia no, un tono più diretto o più formale a seconda del Paese. Uno studio classico di CSA Research lo dice da anni con un titolo che è già una tesi: «Can’t Read, Won’t Buy» — se non lo leggo nella mia lingua, non lo compro. Vale ancora, e vale soprattutto dove c’è un carrello.",
             ],
             figura=dict(src='/wp-content/themes/remarka-studio/assets/img/blog/quattro-tradurre-localizzare.svg',
                         alt='Tradurre contro localizzare: cambiare le parole rispetto ad adattare valuta, formato data, tono ed esempi al mercato',
                         caption='Tradurre cambia le parole; localizzare adatta il messaggio al mercato — valuta, formato data, tono, hreflang. Fonte: CSA Research, «Can’t Read, Won’t Buy».')),
        dict(titolo='Un caso reale: la localizzazione che genera ordini',
             paragrafi=[
                 "Il sito di ATT (traduzione.tech), online dal 2022, porta all'agenzia circa 20 ordini al mese su oltre 40 combinazioni e direzioni linguistiche — un caso reale del gruppo Remarka, non un cliente terzo, con link al progetto vivo in /casi-studio/. Non è la traduzione da sola: è la traduzione fatta da chi vende, unita a un sito veloce e a una struttura pensata per il cliente B2B. È esattamente il modello del nostro servizio Export Ready — il sito e la sua versione estera sotto un unico contratto, con redattori madrelingua.",
             ],
             links=[('Siti multilingue con redattori madrelingua', '/servizi/siti-multilingue/'),
                    ('Calcola il ROI di una versione estera del sito', '/strumenti/roi-localizzazione/')]),
    ],
}

# --- CTA per le schede brevi che non ne avevano una. ---
_BLOG_CTA_NEW = {
    'core-web-vitals-2026': ('Misura i Core Web Vitals del tuo sito — gratis', '/strumenti/test-velocita/'),
    'quanto-costa-sito-aziendale-italia': ('Vedi il nostro listino, a prezzo chiuso', '/prezzi/'),
    'pwa-per-pmi-quando-app-non-serve': ('Scopri i siti PWA di Studio Remarka', '/servizi/siti-pwa/'),
    'cookie-banner-checklist-garante-2026': ('Controlla gratis il tuo cookie banner', '/strumenti/check-gdpr/'),
    'migrare-wordpress-senza-perdere-seo': ('Parliamo della tua migrazione: restyling e migrazione', '/servizi/restyling-migrazione/'),
    'sito-quattro-lingue-costi-tempi': ('Scopri i siti multilingue di Studio Remarka', '/servizi/siti-multilingue/'),
}

# --- Merge: applica lead, sezioni, CTA, link esterni contestuali e Fonti
#     ai dict di BLOG_POSTS (per slug). Ordine: prima il contenuto, poi i
#     link esterni sulle sezioni, infine le fonti (lette da build_blog_post). ---
# --- Paragrafi extra (concretezza, esempi, errori tipici): portano le schede
#     brevi verso le 900–1000 parole senza acqua. {slug: {indice_sez: [par]}}. ---
_BLOG_SEZIONI_EXTEND = {
    'quanto-costa-sito-aziendale-italia': {
        1: [
            "Un esempio concreto di cosa si nasconde nella parola «pagine». Due preventivi dicono entrambi «sito da 15 pagine»: uno intende 15 pagine con testi già pronti da impaginare, l’altro 15 pagine da progettare, scrivere e fotografare. Il secondo costa il doppio e vale il triplo, ma sul foglio sembrano identici. È qui che nasce metà dei «mi hanno chiesto il doppio per la stessa cosa».",
        ],
        3: [
            "La differenza tra fasce, alla fine, è tutta qui: cosa è garantito per iscritto e cosa è lasciato alla buona volontà. Un template a 800 euro non vi promette una velocità, una data, un obbligo di legge rispettato; un progetto serio sì. Non comprate pagine, comprate promesse mantenibili: ed è su quelle che va letto il prezzo.",
        ],
    },
    'pwa-per-pmi-quando-app-non-serve': {
        1: [
            "Un caso tipico dal nostro registro: un’officina che riceve prenotazioni. Con una PWA, il cliente abituale «installa» il sito sul telefono, lo apre con un tocco come un’app, prenota anche dal parcheggio dove la rete balla — e all’officina non è costato un secondo progetto da mantenere. La stessa cosa con un’app nativa avrebbe richiesto due sviluppi, due pubblicazioni e un canone che quella officina non avrebbe mai ripagato.",
        ],
        3: [
            "Un test pratico prima di decidere: elencate le tre cose che l’app «dovrebbe fare». Se sono aprirsi in fretta, funzionare offline, stare sullo schermo e mandare una notifica, siete in territorio PWA. Se invece serve la fotocamera con riconoscimenti, i pagamenti dentro lo store o funzioni hardware profonde, allora l’app nativa ha senso. Il costo di sbagliare questa scelta si conta in decine di migliaia di euro.",
        ],
    },
    'cookie-banner-checklist-garante-2026': {
        2: [
            "C’è poi un quarto errore, più sottile: il banner «finto conforme», con i due pulsanti di pari peso ma i cookie di profilazione che partono comunque al caricamento, sotto il cofano. A occhio sembra a posto; basta aprire gli strumenti per sviluppatori del browser per vedere i tracker attivi prima di ogni clic. È il caso che il nostro controllo indicativo intercetta più spesso.",
        ],
        3: [
            "Cosa fare in mezz’ora, oggi: aprite il sito in una finestra anonima, guardate se «Rifiuta» è visibile quanto «Accetta», e con gli strumenti per sviluppatori controllate se partono script di tracciamento prima di qualsiasi scelta. Se una delle due cose non torna, avete già trovato la priorità. Non risolve tutto, ma vi dice se siete nella maggioranza a rischio o nella minoranza a posto.",
        ],
    },
    'migrare-wordpress-senza-perdere-seo': {
        0: [
            "L’errore più comune e più costoso ha un nome: il redirect «tutto alla home». Per fretta o pigrizia, si fa puntare ogni vecchio indirizzo alla pagina iniziale del sito nuovo. Per Google è quasi come cancellare quelle pagine: il valore accumulato non si trasferisce, e le posizioni scivolano. Ogni vecchia pagina deve rimandare alla sua nuova equivalente, una per una.",
        ],
        3: [
            "Cosa fare prima di dire sì a una migrazione: chiedete a chi la propone se prepara una mappa URL uno-a-uno e un piano di redirect 301 prima del lancio, e se monitora le posizioni nelle settimane dopo. Se la risposta è vaga, il rischio è vostro, non suo. Una migrazione ben fatta non si vede — ed è esattamente questo il punto: il traffico continua come se niente fosse.",
        ],
    },
    'sito-quattro-lingue-costi-tempi': {
        0: [
            "Un modo semplice per decidere: chiedetevi se quella pagina informa o vende. Le pagine che informano — orari, contatti, descrizioni neutre — reggono bene l’automatico, magari con una rilettura. Le pagine che vendono — schede prodotto, landing, testi che devono convincere — vanno affidate a un madrelingua, perché lì un errore di tono non fa sorridere: fa chiudere la scheda.",
        ],
        1: [
            "In pratica, per un sito aziendale medio, aggiungere una lingua ben fatta significa qualche giorno di lavoro per la traduzione e l’adattamento, più l’impostazione tecnica. Molto meno di quanto si teme, se si parte dai testi giusti; molto di più di «zero», che è quanto promette chi vi vende un plugin di traduzione automatica come se fosse una versione estera del sito.",
        ],
    },
    'core-web-vitals-2026': {
        1: [
            "Un errore che vediamo spesso: il sito «leggero» che diventa pesante dopo il lancio, perché nel tempo si aggiungono uno slider, un chat-widget, tre pixel di tracciamento e un font in più. Ognuno sembra innocuo; insieme affondano l’INP e l’LCP. La velocità non è un traguardo che si taglia una volta: è una manutenzione. Per questo la rimisuriamo, non la diamo per scontata.",
        ],
    },
}

_BLOG_BY_SLUG = {p['slug']: p for p in BLOG_POSTS}
for _slug, _lead in _BLOG_LEAD_NEW.items():
    _BLOG_BY_SLUG[_slug]['corpo'] = _lead
for _slug, _sez in _BLOG_SEZIONI_NEW.items():
    _BLOG_BY_SLUG[_slug]['sezioni'] = _sez
for _slug, _bymap in _BLOG_SEZIONI_EXTEND.items():
    _sezioni = _BLOG_SEZIONI_NEW[_slug]
    for _idx, _extra in _bymap.items():
        _sezioni[_idx]['paragrafi'] = _sezioni[_idx].get('paragrafi', []) + _extra

# --- Sezioni aggiuntive per due vecchi articoli «Mese 1» (già con sezioni):
#     aggiunte in coda, per densità e per un finale pratico. ---
_BLOG_SEZIONI_APPEND = {
    'sito-lento-cause-costi': [
        dict(titolo='Cosa fare oggi, in mezz’ora',
             paragrafi=[
                 "Prima di spendere un euro, misurate. Incollate l’indirizzo nel nostro test di velocità e guardate due cose: il punteggio mobile e quali risorse pesano di più. Nove volte su dieci il colpevole è già lì, in cima alla lista: una manciata di immagini enormi, un tema che carica megabyte di codice inutile, o un hosting che risponde piano. Sapere quale delle sette cause vi riguarda cambia tutto: alcune si risolvono in una giornata, altre chiedono di rifare la base.",
                 "La regola che ripetiamo sempre: non fidatevi del «mi sembra più veloce». Misurate prima, cambiate una cosa, misurate dopo. Un numero che passa da 41 a 92 convince il titolare più di qualsiasi relazione — e vi dice, nero su bianco, che i soldi spesi hanno reso.",
             ],
             links=[('Misura ora la velocità del tuo sito — gratis', '/strumenti/test-velocita/'),
                    ('Se la base è vecchia: restyling tecnico', '/servizi/restyling-migrazione/')]),
    ],
    'quanto-costa-ecommerce-italia': [
        dict(titolo='Un errore da 5.000 euro: sottovalutare i contenuti',
             paragrafi=[
                 "C’è una voce che quasi ogni preventivo e-commerce tiene bassa per sembrare competitivo: i contenuti. Schede prodotto scritte bene, foto vere, testi che vendono e — se esportate — traduzioni da madrelingua. Sembra la parte «facile», ed è invece quella che decide se il negozio converte o resta una vetrina silenziosa. Chi vi vende un e-commerce a poco spesso vi lascia questo conto per dopo, quando scoprite che 300 schede non si scrivono da sole.",
             ]),
    ],
}
for _slug, _new_sez in _BLOG_SEZIONI_APPEND.items():
    _BLOG_BY_SLUG[_slug]['sezioni'] = _BLOG_BY_SLUG[_slug].get('sezioni', []) + _new_sez
for _slug, _cta in _BLOG_CTA_NEW.items():
    _BLOG_BY_SLUG[_slug].setdefault('cta', _cta)
for _slug, _bymap in _BLOG_EXT_LINKS.items():
    _sezioni = _BLOG_BY_SLUG[_slug].get('sezioni', [])
    for _idx, _links in _bymap.items():
        _sez = _sezioni[_idx]
        _sez['links'] = _sez.get('links', []) + _links
for _slug, _fonti in _BLOG_FONTI.items():
    _BLOG_BY_SLUG[_slug]['fonti'] = _fonti
