export interface Tool {
  slug: string;
  idx: string;
  titolo: string;
  heroTitolo: string;
  heroSub: string;
  descrizione: string;
  hasDemo: boolean;
}

export const tools: Tool[] = [
  {
    slug: 'test-velocita',
    idx: '/01',
    titolo: 'Test velocità',
    heroTitolo: 'Test di velocità del tuo sito.',
    heroSub: 'Misuriamo il PageSpeed reale del vostro sito su mobile e vi spieghiamo cosa significa, in italiano.',
    descrizione: 'Il PageSpeed reale del vostro sito, spiegato in italiano.',
    hasDemo: true,
  },
  {
    slug: 'check-gdpr',
    idx: '/02',
    titolo: 'Check GDPR e cookie',
    heroTitolo: 'Il vostro sito è a norma GDPR?',
    heroSub: 'Verifichiamo banner cookie, informative e consensi: cosa manca per essere a norma con il Garante Privacy.',
    descrizione: 'Banner, informative e consensi: cosa manca per essere a norma.',
    hasDemo: false,
  },
  {
    slug: 'analisi-seo',
    idx: '/03',
    titolo: 'Analisi SEO on-page',
    heroTitolo: 'Analisi SEO della vostra pagina.',
    heroSub: 'Controlliamo titoli, struttura e dati mancanti sulla pagina che conta di più per il vostro business.',
    descrizione: 'Titoli, struttura e dati mancanti sulla pagina che conta di più.',
    hasDemo: false,
  },
  {
    slug: 'roi-localizzazione',
    idx: '/04',
    titolo: 'ROI localizzazione',
    heroTitolo: 'Quanto rende tradurre il vostro sito.',
    heroSub: 'Stimiamo quanto può rendere tradurre il sito in inglese o tedesco per la vostra attività.',
    descrizione: 'Quanto rende tradurre il sito in inglese o tedesco.',
    hasDemo: false,
  },
];
