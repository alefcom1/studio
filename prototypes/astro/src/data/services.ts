export interface Service {
  slug: string;
  title: string;
  breadcrumb: string;
  heroSub: string;
  heroStatValue: string;
  heroStatLabel: string;
  perChi: string[];
  include: string[];
  miniCaso: { cliente: string; prima: number; dopo: number; testo: string };
  prezzoRange: string;
  prezzoNote: string[];
  faq: { q: string; a: string }[];
}

export const services: Service[] = [
  {
    slug: 'siti-aziendali',
    title: 'Siti aziendali',
    breadcrumb: 'Servizio / Siti aziendali',
    heroSub: 'Struttura chiara e caricamento sotto il secondo per chi vive di richieste di preventivo.',
    heroStatValue: '1,1 s',
    heroStatLabel: 'tempo di caricamento medio consegnato',
    perChi: [
      'Aziende B2B che ricevono richieste di preventivo dal sito',
      'PMI con un sito datato che carica in 4–6 secondi',
      'Chi ha bisogno di gestire contenuti senza uno sviluppatore',
    ],
    include: [
      'Fino a 15 pagine su misura',
      'CMS per aggiornare testi e immagini in autonomia',
      'Modulo contatti con notifica email e WhatsApp',
      'SEO tecnica: dati strutturati, sitemap, meta tag',
      'Ottimizzazione immagini e caricamento differito',
      'Certificato SSL e hosting incluso il primo anno',
      'Formazione all’uso del CMS (1 sessione)',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'TecnoIdraulica',
      prima: 29,
      dopo: 94,
      testo: 'Il sito precedente impiegava 5,8 secondi a caricare su mobile. Dopo il restyling tecnico, le richieste di preventivo sono più che raddoppiate in tre mesi.',
    },
    prezzoRange: '€ 3.900–5.800',
    prezzoNote: ['Numero di pagine e sezioni personalizzate', 'Lingue aggiuntive oltre l’italiano', 'Integrazioni (CRM, newsletter, prenotazioni)'],
    faq: [
      { q: 'Posso aggiornare i contenuti da solo?', a: 'Sì, il CMS incluso permette di modificare testi, immagini e aggiungere pagine senza competenze tecniche.' },
      { q: 'Cosa succede al dominio attuale?', a: 'Gestiamo noi la migrazione DNS, senza interruzioni di servizio o perdita di email.' },
      { q: 'Il sito funziona anche su mobile?', a: 'Sì, ogni sito è progettato mobile-first e testato su Lighthouse prima della consegna.' },
    ],
  },
  {
    slug: 'e-commerce',
    title: 'E-commerce',
    breadcrumb: 'Servizio / E-commerce',
    heroSub: 'Cataloghi veloci e checkout senza attriti, con fatturazione elettronica integrata.',
    heroStatValue: '1,4 s',
    heroStatLabel: 'tempo di caricamento medio consegnato',
    perChi: [
      'Attività che vendono online ma perdono clienti nel checkout',
      'Negozi fisici pronti ad aprire un canale e-commerce',
      'Chi ha bisogno di fatturazione elettronica automatica',
    ],
    include: [
      'Catalogo prodotti illimitato con varianti',
      'Checkout in un solo passaggio',
      'Pagamenti con carta, PayPal e bonifico',
      'Fatturazione elettronica via SDI integrata',
      'Gestione magazzino e spedizioni',
      'SEO tecnica per le pagine prodotto',
      'Formazione all’uso del pannello ordini',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'Cantina Serralta',
      prima: 22,
      dopo: 91,
      testo: 'Il vecchio store impiegava oltre 6 secondi a caricare le pagine prodotto. Con il nuovo catalogo veloce, il tasso di abbandono carrello è sceso del 34%.',
    },
    prezzoRange: '€ 7.500–14.000',
    prezzoNote: ['Numero di prodotti e varianti', 'Integrazioni con corrieri e magazzino', 'Metodi di pagamento aggiuntivi'],
    faq: [
      { q: 'Gestite anche la fatturazione elettronica?', a: 'Sì, ogni ordine genera automaticamente una fattura elettronica conforme SDI.' },
      { q: 'Posso vendere anche all’estero?', a: 'Sì, il catalogo supporta multi-lingua e multi-valuta su richiesta.' },
      { q: 'Quanto costa mantenere il negozio online?', a: 'Hosting e assistenza sono inclusi nei primi 12 mesi; dopo, un canone annuale contenuto copre aggiornamenti e sicurezza.' },
    ],
  },
  {
    slug: 'siti-pwa',
    title: 'Siti progressivi PWA',
    breadcrumb: 'Servizio / Siti progressivi PWA',
    heroSub: 'Un sito che si comporta come un’app: installabile, funziona anche offline, apre all’istante.',
    heroStatValue: '0,9 s',
    heroStatLabel: 'tempo di caricamento medio consegnato',
    perChi: [
      'Attività con clienti che tornano spesso sul sito',
      'Chi vuole un’app senza i costi di App Store e Play Store',
      'Servizi che devono funzionare anche con connessione debole',
    ],
    include: [
      'Installabile su smartphone come un’app',
      'Funziona offline per le pagine già visitate',
      'Notifiche push opzionali',
      'Caricamento istantaneo dopo la prima visita',
      'Service worker configurato e testato',
      'SEO tecnica completa',
      'Formazione all’uso del pannello contenuti',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'Studio Fontana',
      prima: 31,
      dopo: 96,
      testo: 'Trasformato in PWA, il sito si apre ora in meno di un secondo anche per i clienti che lo hanno già visitato, con un incremento del 28% nelle richieste ripetute.',
    },
    prezzoRange: '€ 4.900–7.200',
    prezzoNote: ['Funzionalità offline richieste', 'Notifiche push e integrazioni native', 'Numero di pagine e sezioni'],
    faq: [
      { q: 'Serve pubblicarlo sugli store?', a: 'No, si installa direttamente dal browser: nessuna revisione Apple o Google necessaria.' },
      { q: 'Funziona su tutti gli smartphone?', a: 'Sì, è compatibile con iOS e Android tramite qualsiasi browser moderno.' },
      { q: 'Posso passare da un sito esistente a una PWA?', a: 'Sì, è un percorso di restyling tecnico che manteniamo trasparente per i motori di ricerca.' },
    ],
  },
  {
    slug: 'restyling-migrazione',
    title: 'Restyling e migrazione',
    breadcrumb: 'Servizio / Restyling e migrazione',
    heroSub: 'Il vostro sito attuale, ricostruito: stessi contenuti, il triplo della velocità.',
    heroStatValue: '1,2 s',
    heroStatLabel: 'tempo di caricamento medio consegnato',
    perChi: [
      'Chi ha un sito lento ma non vuole perdere posizionamento SEO',
      'Attività con contenuti validi ma tecnologia datata',
      'Chi ha ricevuto un preventivo di rifacimento completo troppo costoso',
    ],
    include: [
      'Audit tecnico del sito attuale',
      'Migrazione dei contenuti esistenti',
      'Redirect 301 per mantenere il posizionamento SEO',
      'Nuova base tecnica performante',
      'Ottimizzazione immagini e font',
      'Test comparativo prima/dopo su PageSpeed',
      'Formazione all’uso del nuovo CMS',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'Officine Riva',
      prima: 27,
      dopo: 93,
      testo: 'Stessi contenuti, stessa struttura di navigazione: solo la base tecnica è cambiata. Il posizionamento su Google è rimasto invariato, la velocità è triplicata.',
    },
    prezzoRange: '€ 2.900–4.800',
    prezzoNote: ['Numero di pagine da migrare', 'Complessità delle integrazioni esistenti', 'Necessità di redesign grafico'],
    faq: [
      { q: 'Perdo il posizionamento su Google?', a: 'No, impostiamo redirect 301 corretti per ogni URL esistente prima di andare online.' },
      { q: 'Devo riscrivere i contenuti?', a: 'No, il restyling tecnico mantiene i contenuti esistenti; li aggiorniamo solo su richiesta.' },
      { q: 'Quanto dura la migrazione?', a: 'In media 2–4 settimane, con un ambiente di prova visibile fin dalla prima settimana.' },
    ],
  },
  {
    slug: 'seo-tecnica',
    title: 'SEO tecnica',
    breadcrumb: 'Servizio / SEO tecnica',
    heroSub: 'Struttura, dati e Core Web Vitals a posto prima ancora di scrivere i contenuti.',
    heroStatValue: '90+',
    heroStatLabel: 'punteggio Core Web Vitals garantito',
    perChi: [
      'Siti con buoni contenuti ma scarsa visibilità su Google',
      'Chi ha già investito in copywriting senza risultati',
      'Attività che competono in mercati locali affollati',
    ],
    include: [
      'Audit tecnico SEO completo',
      'Dati strutturati (schema.org) per ogni tipo di pagina',
      'Ottimizzazione Core Web Vitals',
      'Sitemap XML e file robots ottimizzati',
      'Struttura URL e gerarchia dei contenuti',
      'Ottimizzazione meta title e description',
      'Report mensile di posizionamento',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'B&B Il Cortile',
      prima: 33,
      dopo: 95,
      testo: 'Con la SEO tecnica sistemata, il B&B è passato dalla terza alla prima pagina di Google per le ricerche locali principali in otto settimane.',
    },
    prezzoRange: '€ 1.800–3.500',
    prezzoNote: ['Numero di pagine da ottimizzare', 'Presenza di contenuti multilingua', 'Storico tecnico da correggere'],
    faq: [
      { q: 'In quanto tempo si vedono risultati?', a: 'I miglioramenti tecnici sono immediati; il posizionamento su Google richiede in media 6–10 settimane.' },
      { q: 'Scrivete anche i contenuti?', a: 'Il servizio è tecnico; per la scrittura dei testi lavoriamo con copywriter partner su richiesta.' },
      { q: 'Fate SEO locale?', a: 'Sì, includiamo l’ottimizzazione della scheda Google Business Profile quando pertinente.' },
    ],
  },
  {
    slug: 'siti-multilingue',
    title: 'Siti multilingue',
    breadcrumb: 'Servizio / Siti multilingue',
    heroSub: 'Quattro lingue tradotte da madrelingua: dal 2001 è il mestiere del gruppo Remarka.',
    heroStatValue: '4',
    heroStatLabel: 'lingue native disponibili',
    perChi: [
      'Aziende che esportano o accolgono clienti stranieri',
      'Attività turistiche con visitatori internazionali',
      'Chi ha usato finora traduzioni automatiche poco professionali',
    ],
    include: [
      'Traduzione professionale da madrelingua (non plugin)',
      'Fino a 4 lingue: italiano, inglese, tedesco, francese',
      'Selettore lingua persistente',
      'SEO multilingue con hreflang corretti',
      'Contenuti localizzati, non solo tradotti',
      'Revisione linguistica da parte del gruppo Remarka',
      'Formazione all’uso del CMS multilingue',
      'PageSpeed 90+ garantito da contratto',
    ],
    miniCaso: {
      cliente: 'Cantina Serralta',
      prima: 40,
      dopo: 92,
      testo: 'Con il sito tradotto in tedesco e inglese da madrelingua, le richieste dall’estero sono passate dal 5% al 22% del totale in un anno.',
    },
    prezzoRange: '€ 3.200–5.500',
    prezzoNote: ['Numero di lingue aggiuntive', 'Volume di contenuti da tradurre', 'Necessità di revisione periodica'],
    faq: [
      { q: 'Le traduzioni sono automatiche?', a: 'No, sono realizzate da traduttori madrelingua del gruppo Remarka, non da plugin automatici.' },
      { q: 'Posso aggiungere una lingua in futuro?', a: 'Sì, la struttura multilingue è predisposta per aggiungere nuove lingue senza rifare il sito.' },
      { q: 'La SEO funziona in tutte le lingue?', a: 'Sì, ogni lingua ha URL e tag hreflang dedicati per essere indicizzata correttamente da Google.' },
    ],
  },
];
