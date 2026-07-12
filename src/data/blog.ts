export interface BlogPost {
  slug: string;
  data: string;
  titolo: string;
  estratto: string;
  corpo: string;
}

export const posts: BlogPost[] = [
  {
    slug: 'perche-pagespeed-conta',
    data: '05 MAG 2026',
    titolo: 'Perché il PageSpeed conta più del design',
    estratto: 'Un sito bellissimo che carica in 5 secondi perde più clienti di uno essenziale che carica in uno. I numeri dei nostri ultimi 12 progetti.',
    corpo: 'Un sito bellissimo che carica in 5 secondi perde più clienti di uno essenziale che carica in uno. Negli ultimi 12 progetti consegnati, il punteggio medio PageSpeed su mobile è stato 97, con un tempo di caricamento medio di 1,1 secondi. Questo articolo spiega come misuriamo la velocità e perché la mettiamo per iscritto nel contratto.',
  },
  {
    slug: 'redirect-301-senza-perdere-seo',
    data: '18 APR 2026',
    titolo: 'Come migriamo un sito senza perdere il posizionamento SEO',
    estratto: 'Ogni migrazione tecnica comporta il rischio di perdere anni di posizionamento organico. Ecco il processo di redirect che usiamo per evitarlo.',
    corpo: 'Ogni migrazione tecnica comporta il rischio di perdere anni di posizionamento organico. In questo articolo spieghiamo il processo di audit, mappatura URL e redirect 301 che applichiamo prima di ogni restyling, con un caso reale in cui il posizionamento è rimasto invariato.',
  },
  {
    slug: 'pwa-vs-app-nativa',
    data: '02 APR 2026',
    titolo: 'PWA o app nativa? Cosa conviene a una PMI italiana',
    estratto: 'Sviluppare un’app nativa costa in media 15-30mila euro. Una Progressive Web App offre gran parte dei benefici a una frazione del costo.',
    corpo: 'Sviluppare un’app nativa costa in media 15-30mila euro e richiede manutenzione separata per iOS e Android. Una Progressive Web App offre installabilità, notifiche e funzionamento offline a una frazione del costo, senza revisione degli store. Ecco quando ha senso scegliere l’una o l’altra.',
  },
  {
    slug: 'core-web-vitals-spiegati',
    data: '20 MAR 2026',
    titolo: 'Core Web Vitals spiegati senza gergo tecnico',
    estratto: 'LCP, INP e CLS: cosa misurano davvero e perché Google li usa per decidere chi mostrare per primo nei risultati di ricerca.',
    corpo: 'LCP, INP e CLS sono le tre metriche che Google usa per valutare l’esperienza utente di un sito. In questo articolo le spieghiamo senza gergo tecnico, con esempi reali di cosa le peggiora e come si sistemano.',
  },
  {
    slug: 'gdpr-cookie-banner-regole',
    data: '08 MAR 2026',
    titolo: 'Cookie banner GDPR: le regole che (quasi) nessuno rispetta',
    estratto: 'Il pulsante "Rifiuta" deve avere lo stesso peso visivo di "Accetta". Una regola semplice, ignorata dalla maggior parte dei siti italiani.',
    corpo: 'Il Garante Privacy richiede che il pulsante "Rifiuta" abbia lo stesso peso visivo del pulsante "Accetta" in un cookie banner. È una regola semplice, ma ignorata dalla maggior parte dei siti italiani che analizziamo. Ecco come costruiamo i nostri banner per essere a norma fin dal primo giorno.',
  },
  {
    slug: 'quanto-costa-davvero-un-sito',
    data: '22 FEB 2026',
    titolo: 'Quanto costa davvero un sito web in Italia nel 2026',
    estratto: 'Dai 500 euro dei costruttori fai-da-te ai 20mila delle grandi agenzie: una mappa onesta dei prezzi e di cosa comprano davvero.',
    corpo: 'Dai 500 euro dei costruttori fai-da-te ai 20mila euro delle grandi agenzie, il mercato dei siti web in Italia è frammentato e poco trasparente. In questo articolo proviamo a mappare onestamente cosa si compra a ogni fascia di prezzo, incluso il nostro.',
  },
];
