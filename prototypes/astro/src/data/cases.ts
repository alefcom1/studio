export interface CaseStudy {
  slug: string;
  cliente: string;
  titolo: string;
  settore: string;
  citta: string;
  intervento: string;
  anno: string;
  keyMetric: string;
  prima: number;
  dopo: number;
  problema: { narrativa: string; stats: { value: string; label: string }[] };
  soluzione: { narrativa: string; interventi: string[] };
  risultati: {
    narrativa: string;
    stats: { value: string; label: string }[];
    quote: string;
    attribuzione: string;
  };
}

export const cases: CaseStudy[] = [
  {
    slug: 'arredamenti-colombo',
    cliente: 'Arredamenti Colombo',
    titolo: 'Da 34 a 96 in sei settimane, con il 41% di richieste in più.',
    settore: 'Arredamento su misura',
    citta: 'Lissone (MB)',
    intervento: 'Restyling e migrazione',
    anno: '2025',
    keyMetric: '+41%',
    prima: 34,
    dopo: 96,
    problema: {
      narrativa: 'Il sito di Arredamenti Colombo caricava in 4,1 secondi su mobile, con immagini non ottimizzate e una struttura costruita per una versione desktop del 2015. Il 68% dei visitatori da mobile abbandonava la pagina prima del caricamento completo, e solo l’1,2% arrivava al modulo contatti.',
      stats: [
        { value: '4,1 s', label: 'tempo di caricamento mobile' },
        { value: '68%', label: 'abbandono prima del caricamento' },
        { value: '1,2%', label: 'tasso di conversione al modulo contatti' },
      ],
    },
    soluzione: {
      narrativa: 'Abbiamo ricostruito la base tecnica mantenendo intatti i contenuti e la struttura di navigazione a cui i clienti erano abituati, con redirect 301 per non perdere il posizionamento già acquisito.',
      interventi: [
        'Migrazione su base tecnica performante con generazione statica',
        'Compressione e lazy loading di tutte le immagini del catalogo',
        'Nuovo modulo contatti con notifica WhatsApp Business',
        'SEO tecnica: dati strutturati per ogni prodotto',
      ],
    },
    risultati: {
      narrativa: 'Sei settimane dopo la messa online, il punteggio PageSpeed mobile è passato da 34 a 96, con un tempo di caricamento sceso a 1,2 secondi.',
      stats: [
        { value: '−2,9 s', label: 'di caricamento: da 4,1 a 1,2 secondi' },
        { value: '+41%', label: 'richieste di preventivo in sei mesi' },
        { value: 'Pag. 1', label: 'su Google per «arredamenti su misura Lissone»' },
      ],
      quote: 'Non ci aspettavamo che un problema “tecnico” portasse così tante richieste in più. Il sito adesso si apre prima che io finisca di sbloccare il telefono.',
      attribuzione: 'Marco Colombo, titolare',
    },
  },
  {
    slug: 'officine-riva',
    cliente: 'Officine Riva',
    titolo: 'Tre volte più veloce, stesso posizionamento su Google.',
    settore: 'Meccanica industriale',
    citta: 'Monza (MB)',
    intervento: 'Restyling e migrazione',
    anno: '2025',
    keyMetric: '3×',
    prima: 27,
    dopo: 93,
    problema: {
      narrativa: 'Il sito precedente di Officine Riva era tecnicamente valido nei contenuti ma costruito su una piattaforma obsoleta, con un tempo di caricamento medio di 3,8 secondi e nessuna ottimizzazione per mobile.',
      stats: [
        { value: '3,8 s', label: 'tempo di caricamento mobile' },
        { value: '52%', label: 'traffico da mobile non ottimizzato' },
        { value: '2,1%', label: 'tasso di conversione al modulo contatti' },
      ],
    },
    soluzione: {
      narrativa: 'Restyling tecnico completo mantenendo il posizionamento SEO esistente, con particolare attenzione ai redirect e alla struttura dati per i macchinari a catalogo.',
      interventi: [
        'Nuova base tecnica con generazione statica',
        'Redirect 301 per tutte le pagine prodotto esistenti',
        'Catalogo macchinari con schema.org Product',
        'Compressione immagini tecniche ad alta risoluzione',
      ],
    },
    risultati: {
      narrativa: 'Il punteggio PageSpeed è passato da 27 a 93 mantenendo invariato il posizionamento organico su tutte le parole chiave principali.',
      stats: [
        { value: '3×', label: 'più veloce nel caricamento mobile' },
        { value: '0', label: 'posizioni perse in SEO durante la migrazione' },
        { value: '+19%', label: 'richieste di preventivo in tre mesi' },
      ],
      quote: 'Temevamo di perdere il posizionamento che avevamo faticosamente conquistato. È rimasto identico, e il sito ora è irriconoscibile in velocità.',
      attribuzione: 'Laura Riva, responsabile marketing',
    },
  },
  {
    slug: 'studio-fontana',
    cliente: 'Studio Fontana',
    titolo: 'Un sito che si apre come un’app, senza costi da app store.',
    settore: 'Studio professionale',
    citta: 'Milano',
    intervento: 'Sito progressivo PWA',
    anno: '2024',
    keyMetric: '+63%',
    prima: 31,
    dopo: 96,
    problema: {
      narrativa: 'I clienti di Studio Fontana tornavano spesso sul sito per consultare documenti e orari, ma ogni visita richiedeva un nuovo caricamento completo, con tempi di attesa fino a 5 secondi su connessioni mobili instabili.',
      stats: [
        { value: '5,0 s', label: 'tempo di caricamento su connessione debole' },
        { value: '0', label: 'funzionalità offline disponibili' },
        { value: '41%', label: 'visite ripetute abbandonate' },
      ],
    },
    soluzione: {
      narrativa: 'Abbiamo trasformato il sito in una Progressive Web App installabile, con le pagine più consultate disponibili anche offline dopo la prima visita.',
      interventi: [
        'Service worker per il caricamento istantaneo dopo la prima visita',
        'Installazione diretta da browser, senza store',
        'Pagine chiave disponibili offline',
        'Notifiche push opzionali per comunicazioni dello studio',
      ],
    },
    risultati: {
      narrativa: 'Le visite ripetute si aprono ora in meno di un secondo, anche offline, con un aumento significativo delle richieste da parte di clienti già acquisiti.',
      stats: [
        { value: '+63%', label: 'richieste ripetute da clienti esistenti' },
        { value: '<1 s', label: 'caricamento nelle visite successive' },
        { value: '100%', label: 'pagine chiave disponibili offline' },
      ],
      quote: 'I nostri clienti installano il sito come un’app senza nemmeno accorgersene. Semplicemente, funziona sempre.',
      attribuzione: 'Elena Fontana, titolare dello studio',
    },
  },
  {
    slug: 'bb-il-cortile',
    cliente: 'B&B Il Cortile',
    titolo: 'Dalla terza pagina di Google alla prima, in otto settimane.',
    settore: 'Ricettività turistica',
    citta: 'Como',
    intervento: 'SEO tecnica',
    anno: '2025',
    keyMetric: 'Pag. 1',
    prima: 33,
    dopo: 95,
    problema: {
      narrativa: 'I contenuti del B&B Il Cortile erano curati, ma il sito non aveva dati strutturati, sitemap aggiornata né ottimizzazione Core Web Vitals: risultato, terza pagina su Google per le ricerche locali principali.',
      stats: [
        { value: '3ª pag.', label: 'posizionamento medio su Google' },
        { value: '0', label: 'dati strutturati presenti' },
        { value: '2,4 s', label: 'tempo di caricamento mobile' },
      ],
    },
    soluzione: {
      narrativa: 'Intervento tecnico mirato su SEO e Core Web Vitals, senza toccare i contenuti già scritti, più ottimizzazione della scheda Google Business Profile.',
      interventi: [
        'Dati strutturati schema.org per l’attività ricettiva',
        'Ottimizzazione Core Web Vitals fino a PageSpeed 95',
        'Sitemap XML e struttura URL rivista',
        'Ottimizzazione scheda Google Business Profile',
      ],
    },
    risultati: {
      narrativa: 'In otto settimane il B&B è passato dalla terza alla prima pagina di Google per le ricerche locali principali, con un incremento diretto delle prenotazioni.',
      stats: [
        { value: 'Pag. 1', label: 'su Google per le ricerche locali principali' },
        { value: '+54%', label: 'prenotazioni dirette dal sito' },
        { value: '95/100', label: 'PageSpeed mobile finale' },
      ],
      quote: 'Non abbiamo cambiato una parola del sito. Solo la parte tecnica, e le prenotazioni dirette sono aumentate più della metà.',
      attribuzione: 'Giulia Bianchi, gestione B&B Il Cortile',
    },
  },
];
