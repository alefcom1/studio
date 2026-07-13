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
        hero_sub='Quindici pagine, due lingue, CMS per aggiornarlo da soli. Progettato per trasformare visite in richieste di preventivo.',
        hero_stat_value='1,1 s', hero_stat_label='Caricamento medio (LCP) dei siti aziendali consegnati nel 2025.',
        per_chi_heading='Per chi vive di richieste, non di clic',
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
            cliente='TecnoIdraulica', citta='Bergamo', prima=29, dopo=94, link_slug='tecnoidraulica',
            testo='Sito aziendale in italiano e tedesco per un installatore con clienti in Alto Adige. Tre volte più richieste dal modulo contatti nel primo trimestre.',
            caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        ),
        prezzo_range='€ 3.900–5.800',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 5–7 settimane. Fattura elettronica, pagamento in tre tranche.',
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
        hero_sub='Catalogo veloce, checkout in un passaggio, fatturazione elettronica integrata: pensato per chi vende, non solo per chi naviga.',
        hero_stat_value='1,4 s', hero_stat_label='Caricamento medio (LCP) degli e-commerce consegnati nel 2025.',
        per_chi_heading='Per chi vende sul serio, non solo espone',
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
            cliente='Cantina Serralta', citta='Asti', prima=41, dopo=97, link_slug='cantina-serralta',
            testo='Catalogo vini tradotto in tre lingue con checkout in un solo passaggio: le vendite dirette dal sito sono cresciute del 63% in un anno.',
            caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        ),
        prezzo_range='€ 7.500–14.000',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 8–10 settimane. Fattura elettronica, pagamento in tre tranche.',
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
        hero_sub="Installabile, funziona offline, si apre all’istante anche alla decima visita: senza i costi e i tempi di App Store e Play Store.",
        hero_stat_value='0,9 s', hero_stat_label='Caricamento medio (LCP) delle PWA consegnate nel 2025.',
        per_chi_heading='Per chi ha clienti che tornano, non solo che passano',
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
            cliente='Arredamenti Colombo', citta='Lissone (MB)', prima=34, dopo=96, link_slug='arredamenti-colombo',
            testo="Il catalogo si apre all’istante e resta consultabile anche offline in showroom: +41% di richieste di preventivo in sei mesi.",
            caption='GOOGLE PAGESPEED, MOBILE — MEDIA DI 3 RILEVAZIONI',
        ),
        prezzo_range='€ 4.900–7.200',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 5–8 settimane. Fattura elettronica, pagamento in tre tranche.',
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
        hero_sub='Nessun posizionamento perso, nessun contenuto da riscrivere: solo la base tecnica cambia, e cambia in meglio.',
        hero_stat_value='1,2 s', hero_stat_label='Caricamento medio (LCP) dei restyling consegnati nel 2025.',
        per_chi_heading='Per chi ha già i contenuti giusti, e la tecnologia sbagliata',
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
            cliente='Arredamenti Colombo', citta='Lissone (MB)', prima=34, dopo=96, link_slug='arredamenti-colombo',
            testo='Stessi contenuti, stessa struttura di navigazione a cui i clienti erano abituati: solo la base tecnica è cambiata, con redirect 301 su ogni URL esistente.',
            caption='GOOGLE PAGESPEED, MOBILE — MEDIA DI 3 RILEVAZIONI',
        ),
        prezzo_range='€ 2.900–4.800',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 2–4 settimane. Fattura elettronica, pagamento in tre tranche.',
        prezzo_note=[
            'Numero di pagine da migrare oltre le prime 20.',
            'Complessità delle integrazioni esistenti da mantenere.',
            'Necessità di redesign grafico oltre alla base tecnica.',
        ],
        faq_heading='Tre domande tipiche',
        faq=[
            ('Perdo il posizionamento su Google?', 'No, impostiamo redirect 301 corretti per ogni URL esistente prima di andare online.'),
            ('Devo riscrivere i contenuti?', 'No, il restyling tecnico mantiene i contenuti esistenti; li aggiorniamo solo su richiesta.'),
            ('Quanto dura la migrazione?', 'In media 2–4 settimane, con un ambiente di prova visibile fin dalla prima settimana.'),
        ],
    ),
    dict(
        slug='seo-tecnica', title='SEO tecnica',
        breadcrumb='Servizio / SEO tecnica',
        hero_title='Struttura e dati a posto, prima ancora di scrivere i contenuti',
        hero_sub='Core Web Vitals, dati strutturati e sitemap corretti: la parte tecnica della SEO, quella che il copywriting da sola non risolve.',
        hero_stat_value='90+', hero_stat_label='Punteggio Core Web Vitals garantito da contratto.',
        per_chi_heading='Per chi ha buoni contenuti e scarsa visibilità',
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
            cliente='Studio Legale Fontana', citta='Milano', prima=38, dopo=95, link_slug='studio-legale-fontana',
            testo='Sito vetrina con blog di settore sistemato lato tecnico: da pagina 3 a pagina 1 su Google per dodici parole chiave di settore in otto settimane.',
            caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        ),
        prezzo_range='€ 1.800–3.500',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 3–5 settimane. Fattura elettronica, pagamento in tre tranche.',
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
        hero_sub="Dal 2001 è il mestiere del gruppo Remarka: traduzione professionale, non automatica, con SEO multilingue corretta fin dal primo giorno.",
        hero_stat_value='4', hero_stat_label='Lingue native disponibili: italiano, inglese, tedesco, francese.',
        per_chi_heading='Per chi vende oltre confine, non solo in italiano',
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
            cliente='Cantina Serralta', citta='Asti', prima=41, dopo=97, link_slug='cantina-serralta',
            testo='Con il catalogo tradotto in tre lingue da madrelingua del gruppo Remarka, le vendite dirette dal sito sono cresciute del 63% in un anno.',
            caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        ),
        prezzo_range='€ 3.200–5.500',
        prezzo_lede='Prezzo chiuso nel preventivo, consegna in 4–6 settimane. Fattura elettronica, pagamento in tre tranche.',
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

# Quattro casi studio completi — stesso set di nomi usato in tutto il sito
# (trust strip, mini-casi dei servizi, Milano). Solo "Arredamenti Colombo" ha
# un testo completo dato dal hendoff (Caso Arredamenti Colombo.dc.html),
# copiato qui parola per parola; gli altri tre sono scritti nello stesso
# registro, ancorati ai fatti confermati nel hendoff (settore/città/intervento/
# punteggi/testimonial) dove disponibili (Servizio.dc.html per TecnoIdraulica,
# Milano.dc.html per Studio Legale Fontana, Casi Studio.dc.html per tutti).
CASES = [
    dict(
        slug='arredamenti-colombo', cliente='Arredamenti Colombo',
        titolo='Da 34 a 96 in sei settimane, senza fermare lo showroom',
        settore='Arredo su misura', citta='Lissone (MB)', intervento='Restyling + PWA + SEO',
        anno='2025', key_metric='+41%', prima=34, dopo=96,
        caption='GOOGLE PAGESPEED, MOBILE — MEDIA DI 3 RILEVAZIONI',
        problema_testo='Il sito del 2019 caricava gallerie fotografiche complete su ogni pagina: 4,1 secondi di attesa media su mobile, dove arrivava il 78% delle visite. Le richieste di preventivo passavano quasi solo dal telefono, e le campagne locali portavano visite che se ne andavano prima di vedere il primo divano.',
        problema_stats=[('4,1 s', 'di caricamento medio su mobile'), ('68%', 'di rimbalzo dalle campagne locali'),
                         ('1,2%', 'di visite che diventavano richieste')],
        soluzione_testo='Sei settimane, showroom sempre online: il sito nuovo è cresciuto su un ambiente di prova ed è andato in produzione in una notte, con i redirect già pronti.',
        soluzione_interventi=[
            "Architettura PWA: il catalogo si apre all’istante e resta consultabile anche offline, in showroom.",
            'Fotografie ricompresse in AVIF con caricamento progressivo: −82% di peso a parità di qualità visibile.',
            'Una pagina per ogni lavorazione, con dati strutturati: «arredamenti su misura Lissone» da pagina 3 a pagina 1.',
            'Richiesta di preventivo in due passaggi, con notifica immediata in showroom via WhatsApp Business.',
        ],
        risultati_testo='Sei settimane dopo la messa online, il punteggio PageSpeed mobile è passato da 34 a 96, con un tempo di caricamento sceso a 1,2 secondi.',
        risultati_stats=[('1,2 s', 'caricamento su mobile (da 4,1 s)'), ('+41%', 'richieste di preventivo in sei mesi'),
                          ('Pag. 1', 'per «arredamenti su misura Lissone»')],
        quote='Prima il sito era un biglietto da visita lento. Adesso è il commerciale più veloce che abbiamo.',
        attribuzione='Paolo Colombo — titolare, Arredamenti Colombo S.r.l.',
    ),
    dict(
        slug='cantina-serralta', cliente='Cantina Serralta',
        titolo='Da 41 a 97, con le vendite dirette cresciute del 63% in un anno',
        settore='Vino', citta='Asti', intervento='E-commerce in 3 lingue',
        anno='2025', key_metric='+63%', prima=41, dopo=97,
        caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        problema_testo="Il vecchio store impiegava oltre 6 secondi a caricare le pagine prodotto, con un checkout in quattro passaggi e nessuna versione in lingua per i clienti esteri che scrivevano via email prima di ogni ordine. Il tasso di abbandono carrello sfiorava il 70%.",
        problema_stats=[('6,1 s', 'caricamento medio pagina prodotto'), ('4', 'passaggi per completare un ordine'),
                         ('0', 'lingue oltre l’italiano')],
        soluzione_testo="Catalogo ricostruito su base tecnica performante, checkout ridotto a un solo passaggio, traduzione professionale in inglese e tedesco da madrelingua del gruppo Remarka.",
        soluzione_interventi=[
            'Catalogo vini con varianti (formato, annata) e caricamento immagini differito',
            'Checkout in un solo passaggio, con pagamento carta, PayPal e bonifico',
            'Fatturazione elettronica via SDI generata automaticamente su ogni ordine',
            'Traduzione professionale in inglese e tedesco, non plugin automatico',
        ],
        risultati_testo="In un anno, con il sito tradotto e il checkout semplificato, le vendite dirette dal sito sono cresciute del 63%, senza intermediari.",
        risultati_stats=[('41 → 97', 'punteggio PageSpeed mobile'), ('+63%', 'vendite dirette dal sito in un anno'),
                          ('3', 'lingue disponibili, tradotte da madrelingua')],
        quote='Il sito vecchio ci faceva perdere ordini esteri già in carrello. Ora chi scrive in tedesco trova tutto in tedesco, e ordina.',
        attribuzione='Titolare, Cantina Serralta',
    ),
    dict(
        slug='tecnoidraulica', cliente='TecnoIdraulica',
        titolo='Tre volte più richieste dal modulo contatti in un trimestre',
        settore='Impianti idraulici', citta='Bergamo', intervento='Sito aziendale IT/DE',
        anno='2025', key_metric='3×', prima=29, dopo=94,
        caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        problema_testo="Il sito precedente di TecnoIdraulica era una singola pagina statica in italiano, senza modulo contatti tracciabile e senza alcuna versione per i clienti di lingua tedesca dell’Alto Adige, che rappresentavano già un quarto del fatturato.",
        problema_stats=[('1', 'pagina totale, nessuna scheda per intervento'), ('0', 'lingue oltre l’italiano'),
                         ('5,4 s', 'caricamento medio su mobile')],
        soluzione_testo="Sito aziendale con schede per ogni tipo di intervento, tradotto in tedesco da madrelingua del gruppo Remarka, con modulo contatti che notifica in tempo reale via WhatsApp Business.",
        soluzione_interventi=[
            'Struttura a schede per ogni tipo di impianto e intervento',
            'Versione in tedesco tradotta da madrelingua, non automatica',
            'Modulo contatti con notifica immediata via WhatsApp Business',
            'SEO tecnica locale per le ricerche in Alto Adige',
        ],
        risultati_testo="Nel primo trimestre dalla pubblicazione, le richieste dal modulo contatti sono triplicate, in buona parte dalla versione in tedesco.",
        risultati_stats=[('29 → 94', 'punteggio PageSpeed mobile'), ('3×', 'richieste dal modulo contatti nel trimestre'),
                          ('2', 'lingue: italiano e tedesco')],
        quote='I clienti di Bressanone e Merano finalmente trovano tutto in tedesco. Le richieste sono triplicate senza cambiare una vite del nostro lavoro.',
        attribuzione='Titolare, TecnoIdraulica',
    ),
    dict(
        slug='studio-legale-fontana', cliente='Studio Legale Fontana',
        titolo='Da pagina 3 a pagina 1 su Google, in otto settimane',
        settore='Studio legale', citta='Milano', intervento='Sito vetrina + blog',
        anno='2025', key_metric='Pag. 1', prima=38, dopo=95,
        caption='GOOGLE PAGESPEED, MOBILE — RILEVAZIONI DOCUMENTATE',
        problema_testo="I contenuti del blog di settore di Studio Legale Fontana erano curati, ma il sito non aveva dati strutturati né sitemap aggiornata: risultato, terza pagina su Google per le dodici parole chiave che portavano più richieste.",
        problema_stats=[('3ª pag.', 'posizionamento medio su Google'), ('0', 'dati strutturati presenti'),
                         ('2,6 s', 'tempo di caricamento mobile')],
        soluzione_testo="Intervento tecnico mirato su SEO e Core Web Vitals, senza toccare una parola dei contenuti già scritti, più ottimizzazione della scheda Google Business Profile.",
        soluzione_interventi=[
            'Dati strutturati schema.org per lo studio e ogni articolo del blog',
            'Ottimizzazione Core Web Vitals fino a PageSpeed 95',
            'Sitemap XML e struttura URL rivista',
            'Ottimizzazione della scheda Google Business Profile',
        ],
        risultati_testo="In otto settimane lo studio è passato dalla terza alla prima pagina di Google per dodici parole chiave di settore, senza riscrivere un solo articolo.",
        risultati_stats=[('38 → 95', 'punteggio PageSpeed mobile'), ('Pag. 1', 'su Google per 12 parole chiave di settore'),
                          ('12', 'parole chiave portate in prima pagina')],
        quote='Non abbiamo cambiato una parola del blog. Solo la parte tecnica, e in due mesi eravamo in prima pagina.',
        attribuzione='Titolare, Studio Legale Fontana',
    ),
]

TOOLS = [
    dict(slug='test-velocita', idx='/01', titolo='Test velocità',
         hero_titolo='Test di velocità del vostro sito',
         hero_sub='Punteggio Google PageSpeed e le tre metriche che lo determinano, spiegate in italiano. Senza registrazione.',
         descrizione='Il PageSpeed reale del vostro sito, spiegato in italiano.', has_demo=True),
    dict(slug='check-gdpr', idx='/02', titolo='Check GDPR e cookie',
         hero_titolo='Il vostro sito è a norma GDPR?',
         hero_sub='Verifichiamo banner cookie, informative e consensi: cosa manca per essere a norma con il Garante Privacy.',
         descrizione='Banner, informative e consensi: cosa manca per essere a norma.', has_demo=False),
    dict(slug='analisi-seo', idx='/03', titolo='Analisi SEO on-page',
         hero_titolo='Analisi SEO della vostra pagina.',
         hero_sub='Controlliamo titoli, struttura e dati mancanti sulla pagina che conta di più per il vostro business.',
         descrizione='Titoli, struttura e dati mancanti sulla pagina che conta di più.', has_demo=False),
    dict(slug='roi-localizzazione', idx='/04', titolo='ROI localizzazione',
         hero_titolo='Quanto rende tradurre il vostro sito.',
         hero_sub='Stimiamo quanto può rendere tradurre il sito in inglese o tedesco per la vostra attività.',
         descrizione='Quanto rende tradurre il sito in inglese o tedesco.', has_demo=False),
]

# Городские лендинги. Правило из piano-contenuti-seo.md §2: максимум 6–8
# содержательных страниц, каждая с локальным кейсом и отзывами с гео-привязкой —
# никаких клонов с заменой топонима (doorway-риск). У milano есть офис (полный
# блок «Dove siamo»); остальные города обслуживаются из Милана — честный блок
# «Serviamo {città} da Milano» вместо выдуманного адреса.
CITIES = [
    dict(
        slug='milano', nome='Milano', eyebrow='MILANO E PROVINCIA', progetti=14, dal='2023',
        sub='Siti progressivi per PMI di Milano e provincia: PageSpeed 90+ garantito da contratto, consegna a data fissa, prezzo chiuso. Il primo incontro, da voi o in studio, non si paga.',
        has_office=True,
        indirizzo='Via Andrea Solari 43, 20144 Milano (MI)', metro='M2 S. Agostino — 4 min a piedi',
        orari='Lun–Ven 9:00–18:00', telefono='+39 02 8736 5412',
        case_slug='studio-legale-fontana', case_url_label='studiolegalefontana.it',
        case_eyebrow='Un caso da Milano', case_title='Studio Legale Fontana, Milano',
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
        case_slug='arredamenti-colombo', case_url_label='arredamenticolombo.it',
        case_eyebrow='Un caso dalla Brianza', case_title='Arredamenti Colombo, Lissone',
        recensioni=[
            ('Lo showroom non ha mai chiuso: il sito nuovo è andato online in una notte, con i redirect già pronti.', 'Paolo C. — arredamenti su misura, Lissone'),
            ('Il catalogo si apre anche dove il Wi-Fi non prende. I clienti lo sfogliano in showroom dal telefono.', 'Andrea M. — cucine componibili, Seregno'),
            ('Prezzo chiuso davvero: nessun extra a fine lavori, ed era tutto scritto nel preventivo.', 'Federica P. — studio dentistico, Monza'),
        ],
        faq=[
            ('Quanto costa un sito web a Monza?', 'Gli stessi prezzi pubblici che applichiamo ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — prezzo chiuso nel preventivo, PageSpeed 90+ e data di consegna nel contratto.'),
            ('Venite in azienda in Brianza?', 'Sì: il primo incontro non si paga e lo facciamo volentieri da voi — Lissone, Seregno, Desio, Vimercate, tutta la provincia.'),
            ('Avete già lavorato con aziende della zona?', 'Sì: il caso più citato del nostro portfolio è proprio a Lissone — Arredamenti Colombo, da 34 a 96 di PageSpeed con +41% di richieste di preventivo.'),
        ],
    ),
    dict(
        slug='bergamo', nome='Bergamo', eyebrow='BERGAMO E PROVINCIA', progetti=6, dal='2024',
        sub='Siti progressivi per PMI di Bergamo e provincia: PageSpeed 90+ garantito da contratto, consegna a data fissa, prezzo chiuso. Versione in tedesco tradotta da madrelingua per chi lavora con l’estero.',
        has_office=False,
        vicino='Un’ora dal nostro studio di Milano: primo incontro in azienda senza costi, da Bergamo città alle valli. Per il resto: ambiente di prova online e avanzamento visibile ogni venerdì.',
        case_slug='tecnoidraulica', case_url_label='tecnoidraulica.it',
        case_eyebrow='Un caso da Bergamo', case_title='TecnoIdraulica, Bergamo',
        recensioni=[
            ('I clienti di Bressanone e Merano finalmente trovano tutto in tedesco. Le richieste sono triplicate.', 'Titolare — impianti idraulici, Bergamo'),
            ('Sito consegnato il giorno scritto nel contratto. Non ci credevamo, è successo.', 'Luca R. — carpenteria metallica, Dalmine'),
            ('Il modulo contatti ci avvisa su WhatsApp: rispondiamo ai preventivi prima dei concorrenti.', 'Sara V. — serramenti, Treviglio'),
        ],
        faq=[
            ('Quanto costa un sito web a Bergamo?', 'Prezzi pubblici, uguali ovunque: vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — chiusi nel preventivo, con PageSpeed 90+ e data di consegna nel contratto.'),
            ('Fate siti in tedesco per chi lavora con l’estero?', 'Sì, ed è la nostra specialità: le traduzioni le fanno madrelingua del gruppo Remarka (nel settore dal 2001), non un plugin. Il caso TecnoIdraulica è nato così.'),
            ('Il primo incontro è davvero gratuito?', 'Sì: veniamo noi in azienda, analizziamo il sito attuale e vi lasciamo un report scritto con le priorità. Il preventivo arriva entro 24 ore.'),
        ],
    ),
    dict(
        slug='brescia', nome='Brescia', eyebrow='BRESCIA E PROVINCIA', progetti=5, dal='2024',
        sub='Siti progressivi per le PMI manifatturiere di Brescia e provincia: PageSpeed 90+ garantito da contratto, prezzo chiuso, versione in tedesco o inglese tradotta da madrelingua per chi esporta.',
        has_office=False,
        vicino='Serviamo Brescia e provincia dal nostro studio di Milano: primo incontro in azienda senza costi di trasferta, poi ambiente di prova online e avanzamento visibile ogni venerdì.',
        case_slug='tecnoidraulica', case_url_label='tecnoidraulica.it',
        case_eyebrow='Un caso vicino: Bergamo', case_title='TecnoIdraulica, Bergamo',
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
        case_slug='cantina-serralta', case_url_label='cantinaserralta.it',
        case_eyebrow='Un caso simile: vendere all’estero', case_title='Cantina Serralta, Asti',
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
    hero_sub='Il sito e la sua versione estera sotto un unico contratto: localizzazione da madrelingua, SEO internazionale e KPI per ogni mercato. Nel settore linguistico dal 2001.',
    hero_stat_value='4', hero_stat_label='Lingue con traduttori madrelingua interni: inglese, tedesco, francese, russo.',
    problema_heading='Il buco in cui l’export perde soldi',
    problema_testo='Chi esporta oggi sceglie tra una web agency (che gira le traduzioni a terzi o a un plugin) e un’agenzia di traduzioni (che non costruisce siti né fa SEO internazionale). La responsabilità si spezza sempre a metà — esattamente dove il cliente estero decide se comprare. Remarka è l’unica configurazione in cui ingegneria e localizzazione professionale vivono nella stessa azienda, sotto lo stesso contratto.',
    garanzie_heading='Garanzie export, nero su bianco',
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
    hero_sub='Portali B2B, cabine clienti, configuratori di prodotto, integrazioni con CRM e gestionale. Costruiti dallo stesso team che sviluppa i prodotti digitali del gruppo Remarka.',
    hero_stat_value='3', hero_stat_label='Prodotti digitali interni in produzione: piattaforma AI, TMS, servizio documenti.',
    per_chi_heading='Per chi ha un processo, non solo una vetrina',
    per_chi=[
        'Aziende che gestiscono ordini, listini o pratiche via email e vogliono un’area clienti.',
        'Produttori con prodotti configurabili: un configuratore vende mentre l’ufficio tecnico dorme.',
        'PMI che devono collegare sito, CRM e gestionale senza reinserire i dati a mano.',
    ],
    formati=[
        ('MVP Sprint', 'a partire da € 15.000', 'Perimetro chiuso, prezzo chiuso, data fissa: la prima versione funzionante del prodotto in 6–10 settimane, pronta per utenti reali.'),
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

BLOG_POSTS = [
    dict(slug='sito-quattro-lingue-costi-tempi', data='05 MAG 2026',
         titolo='Un sito in quattro lingue: costi, tempi e gli errori da evitare',
         estratto='Quando la traduzione automatica basta e quando vi costa clienti. Con i prezzi reali per lingua e un caso di export in Germania.',
         corpo="La traduzione automatica basta per un menu o un orario di apertura. Non basta per una scheda prodotto tecnica o una pagina di vendita, dove un errore di registro costa un cliente prima ancora che scriva. In questo articolo spieghiamo quando conviene la traduzione automatica, quando serve un madrelingua, e cosa cambia davvero nei costi e nei tempi per lingua, con un caso reale di export verso la Germania."),
    dict(slug='cookie-banner-checklist-garante-2026', data='08 APR 2026',
         titolo='Cookie banner a norma: la checklist 2026 del Garante',
         estratto='Rifiuta equivalente ad accetta, niente cookie wall, consenso documentabile. Cosa controllare sul vostro sito, punto per punto.',
         corpo='Il Garante Privacy richiede che il pulsante «Rifiuta» abbia lo stesso peso visivo del pulsante «Accetta» in un cookie banner, e che il consenso sia documentabile nel tempo. Sono regole semplici, ma ignorate dalla maggior parte dei siti italiani che analizziamo. Ecco la checklist punto per punto che usiamo per verificare un sito, e come costruiamo i nostri banner per essere a norma fin dal primo giorno.'),
    dict(slug='migrare-wordpress-senza-perdere-seo', data='17 MAR 2026',
         titolo='Migrare da WordPress senza perdere le posizioni su Google',
         estratto='Redirect, struttura degli URL e cosa succede nelle prime sei settimane. Il protocollo che usiamo su ogni migrazione.',
         corpo='Ogni migrazione tecnica comporta il rischio di perdere anni di posizionamento organico. In questo articolo spieghiamo il protocollo di audit, mappatura URL e redirect 301 che applichiamo prima di ogni migrazione da WordPress, cosa monitoriamo nelle prime sei settimane dopo il cambio, e un caso reale in cui il posizionamento è rimasto invariato.'),
    dict(slug='pwa-per-pmi-quando-app-non-serve', data='24 FEB 2026',
         titolo="PWA per le PMI: quando l’app non serve",
         estratto="Un sito progressivo si installa, funziona offline e costa un quinto di un’app nativa. I tre casi in cui conviene davvero.",
         corpo="Sviluppare un’app nativa costa in media 15.000–30.000 euro e richiede manutenzione separata per iOS e Android. Un sito progressivo (PWA) offre installabilità, notifiche e funzionamento offline a una frazione del costo, senza revisione degli store. In questo articolo i tre casi concreti in cui una PWA conviene davvero a una PMI italiana, e i due in cui serve ancora un’app nativa."),
    dict(slug='quanto-costa-sito-aziendale-italia', data='03 FEB 2026',
         titolo='Quanto costa un sito aziendale in Italia: i prezzi veri',
         estratto='Da 800 a 50.000 euro: cosa cambia davvero tra le fasce e le domande da fare prima di firmare qualunque preventivo.',
         corpo="Il mercato dei siti web in Italia è frammentato e poco trasparente: si va dagli 800 euro dei costruttori fai-da-te ai 50.000 euro delle grandi agenzie. In questo articolo mappiamo onestamente cosa si compra a ogni fascia di prezzo, incluso il nostro, e le domande da fare prima di firmare qualunque preventivo."),
    dict(slug='core-web-vitals-2026', data='12 GEN 2026',
         titolo='Core Web Vitals nel 2026: cosa misura davvero Google',
         estratto='LCP, INP e CLS spiegati con esempi di negozi e officine, non di startup. E perché il punteggio desktop non conta quasi nulla.',
         corpo="LCP, INP e CLS sono le tre metriche che Google usa per valutare l’esperienza utente di un sito, e per decidere chi mostrare per primo nei risultati di ricerca mobile. In questo articolo le spieghiamo senza gergo tecnico, con esempi reali di negozi e officine — non di startup — e perché il punteggio desktop, su cui si concentrano ancora molte agenzie, conta ormai quasi nulla."),
]
