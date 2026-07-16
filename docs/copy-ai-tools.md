# Remarka Lab — 3 strumenti AI: copy deck (stage A)

> Дата: 16.07.2026. Источник тона — лучшие записи `build-tools/data.py`
> (metodologia/lettura): живой «voi», числа вместо прилагательных, честные
> оговорки, без канцелярита. Архитектура — `docs/piano-ai-tools.md`.
> Тексты страниц — только IT (полные, готовы для `data.py`). UI-строки виджетов
> и SEO-мета — IT/EN/RU. RU-страницы делаются руками отдельно (фаза B); здесь —
> строки к вставке. №4 (AI-инсайт в PDF) страницы не имеет — его подписи в §5.

Слаги (предложены): IT `/strumenti/sito-letto-dallai/`, `/strumenti/suona-madrelingua/` (*corretto 16.07*),
`/strumenti/generatore-llms-txt/`.

---

## 1. «Il vostro sito, letto dall'AI» — `/strumenti/sito-letto-dallai/`

### 1.1. Hero

**H1:** `Il vostro sito, letto dall'AI`

**Sottotitolo (hero_sub):**
`Incollate l'indirizzo: un'intelligenza artificiale legge la vostra home come farebbe ChatGPT o un assistente AI, e vi dice cosa ha capito. Di cosa vi occupate, per chi, e quanto è facile — per un'AI — citarvi in una risposta. In meno di un minuto, un verdetto e le tre mosse che contano. Non è il check tecnico di «Pronto per l'AI»: qui l'AI vi legge davvero.`

**descrizione (card):** `Cosa capisce l'AI del vostro sito, e come vi citerebbe.`

### 1.2. Come funziona (3 шага)

1. **`Incollate l'indirizzo`** — `La home o la pagina che vi rappresenta. Nessuna registrazione, nessun dato di pagamento.`
2. **`L'AI legge come un assistente`** — `Il nostro server prende il testo, i titoli, i dati strutturati, l'llms.txt e il robots.txt della pagina e li passa a un modello di intelligenza artificiale, con le stesse informazioni che vede un assistente AI quando vi incontra.`
3. **`Leggete cosa ha capito`** — `Cosa fate e per chi, secondo l'AI; un punteggio di «citabilità» da 0 a 100; e tre mosse concrete, in forma di «fate X → ottenete Y». Il resto dell'analisi ve lo mandiamo via e-mail.`

### 1.3. Cosa misura davvero (metodologia)

**H2:** `Che cosa vede l'AI quando legge il vostro sito`

- `Un assistente AI non «guarda» il sito come un visitatore: ne legge il testo, i titoli, la meta description, i dati strutturati e — se ci sono — l'llms.txt e le regole per i suoi crawler. Da quei segnali ricostruisce chi siete e cosa offrite. Noi passiamo a un modello esattamente quel materiale e gli chiediamo tre cose semplici: di cosa si occupa questo sito, a chi si rivolge, e quanto sarebbe sicuro di citarlo in una risposta. Il punteggio di citabilità nasce lì: non è la vostra posizione su ChatGPT, è quanto il vostro sito si spiega da solo.`
- `È giusto dire cosa questo strumento non fa. Non promette che ChatGPT vi nominerà, non conta quante volte siete già citati, non è un audit tecnico pagina per pagina. È una lettura qualitativa: lo specchio di come una macchina interpreta le vostre parole. Se l'AI capisce male, di solito è il sito a parlare poco chiaro — ed è una cosa che si aggiusta.`

### 1.4. Come si legge il risultato (lettura)

**H2:** `Come leggere il verdetto e la citabilità`

- `Partite dal verdetto e dalle tre mosse: sono già ordinate per impatto e scritte come azioni, «fate questo → succede quello». Poi guardate la citabilità. Da 75 in su l'AI vi capisce e vi citerebbe volentieri: il sito si presenta bene. Tra 50 e 74 il senso c'è ma qualcosa confonde — un titolo generico, una home che non dice subito cosa vendete. Sotto 50 l'AI fatica a dire di cosa vi occupate: è la prima cosa da sistemare, prima di ogni tattica.`
- `Due letture da evitare. Un punteggio alto non significa «primo su ChatGPT»: significa che vi spiegate bene, il che è la precondizione, non la garanzia. E se «cosa ha capito» non vi somiglia, non è un errore dell'AI: è il segnale che il vostro sito, letto da fuori, racconta una storia diversa da quella che avete in testa.`

### 1.5. FAQ

- **`È lo stesso di «Il sito è pronto per l'AI?»`** — `No, sono complementari. «Pronto per l'AI» controlla i segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e dà un punteggio su 4. Qui l'AI legge davvero i contenuti e vi dice cosa ha capito. Uno misura gli ingranaggi, l'altro il risultato.`
- **`Conservate il testo del mio sito?`** — `No. Il contenuto della pagina viene letto una volta per generare l'analisi e non lo salviamo. In cache teniamo solo il risultato, per 24 ore, così una seconda prova sullo stesso sito è immediata.`
- **`È un giudizio ufficiale?`** — `È la lettura di un'intelligenza artificiale, non una certificazione né un parere garantito. Diversi assistenti AI possono leggervi in modo leggermente diverso: prendetelo come una diagnosi onesta, non come un timbro.`
- **`Perché l'analisi completa arriva via e-mail?`** — `A schermo trovate subito il verdetto e le tre mosse. Il resto — cosa ha capito l'AI, per chi vi vede, perché quel punteggio — ve lo inviamo via e-mail, così resta a portata di mano quando ne parlate con noi o col vostro team.`

### 1.6. CTA (blocco scuro finale)

**heading:** `Volete che l'AI vi capisca al primo colpo?`
**testo:** `Dal verdetto al lavoro: rendiamo il vostro sito leggibile agli assistenti AI e ai motori — contenuti chiari, dati strutturati, llms.txt. A prezzo chiuso, con PageSpeed 90+ garantito da contratto.`
**buttons:** `Scopri la SEO tecnica` → `/servizi/seo-tecnica/`; `Il sito è pronto per l'AI?` → `/strumenti/sito-pronto-ai/` (outline)

---

## 2. «Suona madrelingua?» — `/strumenti/suona-madrelingua/`

> **Corretto per decisione del proprietario (16.07.2026):** lo strumento non
> verifica più «suona italiano?», ma se un testo suona madrelingua nelle
> lingue ESTERE rispetto alla pagina in cui ci si trova — un italiano non
> controlla il proprio italiano, controlla i propri testi export. Ogni
> versione linguistica del sito propone le altre due lingue: IT → inglese/
> russo (default inglese); EN → italiano/russo (default italiano); RU →
> italiano/inglese (default italiano). Vecchio slug `suona-italiano` mai
> pubblicato — sostituito senza redirect.

### 2.1. Hero

**H1:** `Suona madrelingua?`

**Sottotitolo:**
`Vendete anche in inglese o in russo? Incollate un testo del vostro sito: un'intelligenza artificiale vi dice se suona come l'avrebbe scritto un madrelingua, o se si sente la traduzione. Scegliete la lingua, incollate il testo: in pochi secondi un punteggio di naturalezza e tre correzioni concrete. Traduciamo per i mercati esteri dal 2001: questo è il nostro mestiere, in versione gratuita.`

**descrizione (card):** `I vostri testi in inglese o russo suonano nativi?`

### 2.2. Come funziona (3 шага)

1. **`Scegliete la lingua e incollate il testo`** — `Un paragrafo della home, la descrizione di un prodotto, il chi siamo: nella lingua in cui vendete all'estero. Fino a circa 2.000 caratteri. Niente registrazione.`
2. **`L'AI lo legge come un madrelingua`** — `Un modello di intelligenza artificiale valuta il testo come lo sentirebbe un lettore madrelingua di quella lingua: scorrevolezza, tono, calchi dall'italiano o da un'altra lingua, espressioni che tradiscono una traduzione.`
3. **`Leggete cosa cambiare`** — `Un punteggio di naturalezza da 0 a 100, il registro giusto per quel mercato, e tre correzioni «prima → dopo» spiegate.`

### 2.3. Cosa misura davvero (metodologia)

**H2:** `Che cosa rende un testo «madrelingua»`

- `Un testo può essere corretto e suonare comunque straniero. Succede quando la grammatica è a posto ma la costruzione è calcata su un'altra lingua: frasi troppo lunghe, un registro sbagliato, parole giuste al posto sbagliato, quel tono da manuale tradotto. Un lettore madrelingua non lo analizza — lo sente, e si fida meno. Chiediamo al modello proprio questo: non «ci sono errori?», ma «suona come l'avrebbe scritto una persona madrelingua?».`
- `Cosa non è. Non è un correttore ortografico: gli errori di battitura non sono il punto. Non è un giudizio letterario né un ranking SEO. È una valutazione di naturalezza e tono — la differenza tra un testo che passa e uno che vende. E come ogni lettura AI, è un parere, non un verdetto: la revisione vera la fa un redattore madrelingua, lingua per lingua, che è esattamente ciò che facciamo dal 2001.`

### 2.4. Come si legge il risultato (lettura)

**H2:** `Come leggere il punteggio di naturalezza`

- `Il punteggio dice quanto il testo suona nativo in quella lingua. Da 75 in su siete a posto: un madrelingua lo leggerebbe senza inciampi. Tra 50 e 74 il senso c'è, ma qualcosa stona — un calco, una frase contorta, un registro sbagliato — e le tre correzioni vi dicono dove. Sotto 50 si sente la traduzione: il testo funziona per capirsi, non ancora per convincere. Partite dalle correzioni: sono le tre che spostano di più.`
- `Un'avvertenza onesta. Un punteggio alto non certifica che il testo sia perfetto per il vostro pubblico: il tono giusto per una gioielleria non è quello giusto per un'officina. Usate il registro come bussola, non come voto finale. E ricordate che l'AI legge il testo che incollate, non l'intero sito: è una sonda, non un audit.`

### 2.5. FAQ

- **`Conservate il testo che incollo?`** — `No. Il testo viene valutato una volta e non lo salviamo. In cache resta solo il risultato per 24 ore, così ripetere la stessa prova è immediato.`
- **`Corregge anche il testo al posto mio?`** — `Vi dà tre correzioni «prima → dopo» come esempio, non riscrive tutto. La riscrittura completa e coerente su tutto il sito è un lavoro da redattore madrelingua: è il nostro servizio di localizzazione.`
- **`Quali lingue valuta?`** — `Le due lingue proposte in questa pagina: sono quelle utili a chi vende dall'Italia verso l'estero. La revisione completa la fanno redattori madrelingua, lingua per lingua, dal 2001.` (*sostituisce «Funziona solo con l'italiano?», non più pertinente*)

### 2.6. CTA

**heading:** `Volete che i vostri testi parlino come un madrelingua?`
**testo:** `Dal 2001 traduciamo e adattiamo siti per i mercati esteri con redattori madrelingua — non un plugin, un deliverable con nome e cognome. Prezzo chiuso, consegna a data fissa.`
**buttons:** `Scopri i siti multilingue` → `/servizi/siti-multilingue/`; `Vedi tutti gli strumenti` → `/strumenti/` (outline)

---

## 3. «Generatore llms.txt» — `/strumenti/generatore-llms-txt/`

### 3.1. Hero

**H1:** `Generatore di llms.txt`

**Sottotitolo:**
`Il file che spiega il vostro sito agli assistenti AI, pronto da scaricare. Rispondete a tre domande — o incollate solo l'indirizzo e i dati li raccogliamo noi — e un'intelligenza artificiale scrive il vostro llms.txt: struttura corretta, pagine chiave, descrizione chiara. Da copiare, scaricare e mettere online. Gratis, senza registrazione.`

**descrizione (card):** `Il vostro llms.txt, scritto e pronto da scaricare.`

### 3.2. Come funziona (3 шага)

1. **`Dateci l'essenziale`** — `Nome, di cosa vi occupate, le pagine che contano. Oppure incollate solo l'indirizzo del sito: leggiamo noi la home e ricaviamo i dati.`
2. **`L'AI scrive il file`** — `Un modello di intelligenza artificiale compone l'llms.txt nel formato che i crawler AI si aspettano: un'intestazione con il nome, una descrizione sintetica, l'elenco delle pagine importanti con una riga ciascuna.`
3. **`Copiate, scaricate, pubblicate`** — `Il file è pronto: lo copiate con un clic o lo scaricate come llms.txt. Va caricato nella cartella principale del sito, accanto al robots.txt.`

### 3.3. Cosa misura davvero (metodologia)

**H2:** `Che cos'è l'llms.txt e cosa ci mettiamo dentro`

- `L'llms.txt è un file di testo, in formato Markdown, che vive nella radice del sito e riassume — per gli assistenti AI — chi siete e quali sono le vostre pagine importanti. È al mondo dei modelli AI quello che il robots.txt è a Google: una mappa breve e leggibile, che i crawler di ChatGPT, Perplexity o Claude leggono più volentieri dell'HTML. Noi generiamo l'intestazione con il nome, una descrizione onesta del business e la lista delle pagine chiave, ognuna con la sua riga di contesto.`
- `Cosa non è. L'llms.txt non è una bacchetta magica: non garantisce di essere citati e, da solo, non fa SEO. È un pezzo — utile e a costo zero — di un lavoro più ampio di visibilità sugli assistenti AI. Il file che generiamo è un ottimo punto di partenza: rileggetelo, sistemate la descrizione se serve, e verificate che le pagine elencate siano davvero quelle giuste.`

### 3.4. Come si legge il risultato (lettura)

**H2:** `Come usare il file che avete generato`

- `Il risultato è il file completo, pronto. Copiatelo o scaricatelo, poi caricatelo nella cartella principale del sito — la stessa dove vive il robots.txt — così l'indirizzo finale è iltuosito.it/llms.txt. Da lì i crawler AI lo trovano da soli. Sotto al file trovate una nota: di solito è un dettaglio da controllare a mano, come una descrizione da personalizzare o una pagina da aggiungere.`
- `Un consiglio. Rileggete sempre la descrizione prima di pubblicare: l'AI la scrive dai dati che le date, ma nessuno conosce il vostro business meglio di voi. Due minuti di rilettura valgono più di dieci righe generate al volo. E aggiornatelo quando aggiungete pagine importanti: un llms.txt vecchio racconta un sito che non c'è più.`

### 3.5. FAQ

- **`Devo per forza avere un llms.txt?`** — `Non è obbligatorio come il robots.txt, ma è un segnale in crescita: da maggio 2026 Google lo considera nell'audit «Agentic Browsing» di Lighthouse. A costo zero, è tra le cose più facili da fare per farsi leggere meglio dagli assistenti AI.`
- **`Conservate i dati che inserisco?`** — `No. Usiamo i dati (o il testo della home, se date solo l'indirizzo) una volta per generare il file e non li salviamo. In cache resta solo il risultato per 24 ore.`
- **`Il file generato è definitivo?`** — `È un ottimo punto di partenza, non un dogma. È pensato per essere riletto e ritoccato: la descrizione e le pagine chiave le conoscete meglio voi. La nota sotto al file vi segnala cosa vale la pena controllare.`
- **`Basta l'llms.txt per farsi trovare da ChatGPT?`** — `No, è un pezzo del puzzle. Farsi citare dagli assistenti AI dipende anche da contenuti chiari, dati strutturati e autorevolezza. L'llms.txt aiuta a spiegarsi; il resto è SEO tecnica e contenuti.`

### 3.6. CTA

**heading:** `Volete essere trovati e citati dagli assistenti AI?`
**testo:** `L'llms.txt è il primo passo. Il resto — dati strutturati, contenuti leggibili dalle AI, SEO tecnica — lo costruiamo noi, a prezzo chiuso e con PageSpeed 90+ garantito da contratto.`
**buttons:** `Scopri la SEO tecnica` → `/servizi/seo-tecnica/`; `Il sito è pronto per l'AI?` → `/strumenti/sito-pronto-ai/` (outline)

---

## 4. UI-строки виджетов (IT / EN / RU)

> Вставляются в разметку страниц как `data-*`-атрибуты (по одной языковой версии
> на страницу). JS берёт их через `txt(root, 'data-…', fallback)`. Ниже —
> значения по языкам.

### 4.1. Общие (все три виджета)

| Ключ / назначение | IT | EN | RU |
|---|---|---|---|
| Кнопка запуска (read/llms) | `Analizza` | `Analyze` | `Проверить` |
| Кнопка запуска (suona) | `Valuta il testo` | `Check the text` | `Оценить текст` |
| Loading — read | `L'AI sta leggendo il vostro sito…` | `The AI is reading your site…` | `ИИ читает ваш сайт…` |
| Loading — suona | `L'AI sta valutando il testo…` | `The AI is checking the text…` | `ИИ оценивает текст…` |
| Loading — llms | `L'AI sta scrivendo il vostro llms.txt…` | `The AI is writing your llms.txt…` | `ИИ пишет ваш llms.txt…` |
| Errore generico | `Lo strumento non è disponibile in questo momento. Riprovate tra poco.` | `The tool isn't available right now. Please try again shortly.` | `Инструмент сейчас недоступен. Попробуйте чуть позже.` |
| Manutenzione | `Strumento in manutenzione.` | `Tool under maintenance.` | `Инструмент на обслуживании.` |
| Limite raggiunto | `Avete raggiunto il limite di prove per oggi. Riprovate domani.` | `You've reached today's limit. Please try again tomorrow.` | `Достигнут лимит проверок на сегодня. Попробуйте завтра.` |
| URL non valido | `Inserite un indirizzo valido (https://…).` | `Enter a valid address (https://…).` | `Введите корректный адрес (https://…).` |
| Disclaimer privacy (статичный) | `Non salviamo il contenuto: è una lettura dell'AI, non un audit certificato.` | `We don't store your content: it's an AI reading, not a certified audit.` | `Мы не сохраняем контент: это чтение ИИ, не сертифицированный аудит.` |

### 4.2. №1 read-site

| Назначение | IT | EN | RU |
|---|---|---|---|
| Etichetta citabilità | `Citabilità AI` | `AI citability` | `Цитируемость для ИИ` |
| Titolo «cosa ha capito» | `Cosa ha capito l'AI` | `What the AI understood` | `Что понял ИИ` |
| Titolo «per chi» | `Per chi, secondo l'AI` | `Who it's for, per the AI` | `Для кого, по мнению ИИ` |
| Titolo mosse | `Le 3 mosse` | `The 3 moves` | `3 шага` |
| Freccia mossa (Fai → ottieni) | `→` | `→` | `→` |
| Email-gate heading | `Ricevete l'analisi completa via e-mail` | `Get the full analysis by e-mail` | `Получите полный разбор на e-mail` |
| Campo e-mail placeholder | `La vostra e-mail` | `Your e-mail` | `Ваш e-mail` |
| Consenso (checkbox) | `Acconsento a essere ricontattato da Studio Remarka.` | `I agree to be contacted by Studio Remarka.` | `Согласен(на) на связь со Studio Remarka.` |
| Bottone invio | `Ricevi l'analisi completa` | `Send me the full analysis` | `Отправить полный разбор` |
| Successo invio | `Fatto: controllate la posta.` | `Done — check your inbox.` | `Готово — проверьте почту.` |

### 4.3. №2 suona (pagina «Suona madrelingua?») — *corretto 16.07.2026*

Selettore lingua sopra la textarea (radio/pill, riuso stile form): etichetta
+ 2 opzioni, le lingue ESTERE rispetto a quella della pagina, default la
prima elencata:

| Назначение | IT (opzioni: en, ru) | EN (opzioni: it, ru) | RU (opzioni: it, en) |
|---|---|---|---|
| Etichetta selettore | `Lingua del testo:` | `Text language:` | `Язык текста:` |
| Opzione 1 (default) | `Inglese` | `Italian` | `Итальянский` |
| Opzione 2 | `Russo` | `Russian` | `Английский` |

| Назначение | IT | EN | RU |
|---|---|---|---|
| Placeholder textarea | `Incollate qui il testo da valutare (max ~2.000 caratteri)…` | `Paste the text to check here (max ~2,000 characters)…` | `Вставьте текст для проверки (макс. ~2000 знаков)…` |
| Contatore caratteri | `{n} / 2000` | `{n} / 2000` | `{n} / 2000` |
| Badge «suona» sì | `Suona nativo` | `Sounds native` | `Звучит как у носителя` |
| Badge «suona» no | `Si sente la traduzione` | `Sounds translated` | `Слышен перевод` |
| Etichetta punteggio | `Naturalezza` | `Naturalness` | `Естественность` |
| Etichetta registro | `Registro` | `Tone` | `Тон` |
| Titolo correzioni | `3 correzioni` | `3 fixes` | `3 правки` |
| Prima / Dopo | `Prima` / `Dopo` | `Before` / `After` | `Было` / `Стало` |
| Testo troppo corto | `Incollate almeno una frase.` | `Paste at least one sentence.` | `Вставьте хотя бы одно предложение.` |

Client invia `text_lang` = valore dell'opzione selezionata (`it|en|ru`);
`locale` (lingua della pagina, invariato) resta il parametro che determina
la lingua di verdetto/registro/correzioni.

### 4.4. №3 llms-txt

| Назначение | IT | EN | RU |
|---|---|---|---|
| Tab «form» | `Compila i campi` | `Fill in the fields` | `Заполнить поля` |
| Tab «url» | `Ho solo l'indirizzo` | `I only have the URL` | `Только адрес` |
| Campo nome | `Nome del sito / attività` | `Site / business name` | `Название сайта / бизнеса` |
| Campo cosa fate | `Di cosa vi occupate` | `What you do` | `Чем вы занимаетесь` |
| Campo pagine | `Pagine chiave (una per riga)` | `Key pages (one per line)` | `Ключевые страницы (по одной в строке)` |
| Bottone copia | `Copia` | `Copy` | `Копировать` |
| Copia riuscita | `Copiato` | `Copied` | `Скопировано` |
| Bottone scarica | `Scarica llms.txt` | `Download llms.txt` | `Скачать llms.txt` |
| Nota (prefisso) | `Da controllare:` | `To check:` | `Проверьте:` |

---

## 5. №4 — подписи AI-инсайта в PDF check-up (IT / EN / RU)

Добавить в `remarka_checkup_copy()` (по locale), рендерить на странице «Da dove
partire» перед списком приоритетов (см. `piano-ai-tools.md` §7).

| Ключ | IT | EN | RU |
|---|---|---|---|
| `ai_insight_label` | `Il parere dell'AI` | `The AI's take` | `Мнение ИИ` |
| `ai_insight_note` (сноска-оговорка) | `Lettura sintetica generata da un'intelligenza artificiale sui vostri sette punteggi — un parere, non una certificazione.` | `A short reading generated by an AI from your seven scores — an opinion, not a certification.` | `Краткое резюме, сгенерированное ИИ по вашим семи оценкам, — мнение, не сертификат.` |

---

## 6. SEO — фокус-ключи и мета (готово для `docs/seo-meta.md`)

> Проверка на каннибализацию: `sito-pronto-ai` держит ключ «sito pronto per l'AI
> (llms.txt)», блог — «llms.txt cos'è». Новые ключи не пересекаются:
> №1 — про *чтение/понимание* («come l'AI legge»), №3 — про *генерацию файла*
> («generatore llms.txt», транзакционный интент vs информационный блог).
> №2 — новая ниша (naturalezza итальянского). Длины проверены (Title ≤60, Desc ≤160).

### Карта фокус-ключей (IT / EN / RU)

| Страница | Focus IT | Focus EN | Focus RU |
|---|---|---|---|
| `/strumenti/sito-letto-dallai/` · `/en/tools/read-by-ai/` · `/ru/instrumenty/sajt-glazami-ii/` | come l'AI legge il sito | how AI reads your site | как ИИ читает сайт |
| `/strumenti/suona-madrelingua/` · `/en/tools/does-it-sound-native/` · `/ru/instrumenty/zvuchit-kak-u-nositelya/` (*corretto 16.07*) | il testo suona madrelingua | does your text sound native | текст как у носителя |
| `/strumenti/generatore-llms-txt/` · `/en/tools/llms-txt-generator/` · `/ru/instrumenty/generator-llms-txt/` | generatore llms.txt | llms.txt generator | генератор llms.txt |

### №1 — sito-letto-dallai

- **IT Title (54):** `Il vostro sito letto dall'AI, gratis | Studio Remarka`
- **IT Description (156):** `Un'intelligenza artificiale legge la vostra home e vi dice cosa ha capito: di cosa vi occupate, per chi e quanto siete citabili. Verdetto e 3 mosse, gratis.`
- **EN Title (52):** `Your website, read by AI — free tool | Studio Remarka`
- **EN Description (154):** `An AI reads your homepage and tells you what it understood: what you do, who for, and how citable you are. A verdict and three moves, free, no sign-up.`
- **RU Title (52):** `Ваш сайт глазами ИИ — бесплатно | Studio Remarka`
- **RU Description (150):** `Искусственный интеллект читает вашу главную и говорит, что понял: чем вы заняты, для кого и насколько вас цитировать. Вердикт и 3 шага, бесплатно.`

### №2 — suona-madrelingua (*corretto per decisione del proprietario 16.07.2026*)

- **IT Title (51):** `Il vostro testo suona madrelingua? | Studio Remarka`
- **IT Description (145):** `Incollate un testo in inglese o russo: l'AI vi dice se suona nativo o se si sente la traduzione. Punteggio di naturalezza e 3 correzioni. Gratis.`
- **EN Title (53):** `Does your text sound native? AI test | Studio Remarka`
- **EN Description (150):** `Paste a text in Italian or Russian: an AI tells you if it sounds native or translated. A naturalness score and three concrete fixes. Free, no sign-up.`
- **RU Title (53):** `Текст звучит как у носителя? Тест ИИ | Studio Remarka`
- **RU Description (139):** `Вставьте текст на итальянском или английском: ИИ скажет, звучит ли он как у носителя или чувствуется перевод. Оценка и 3 правки. Бесплатно.`

### №3 — generatore-llms-txt

- **IT Title (49):** `Generatore di llms.txt gratis | Studio Remarka`
- **IT Description (153):** `Create il vostro llms.txt in un minuto: rispondete a tre domande o incollate l'indirizzo, l'AI scrive il file. Da copiare e scaricare. Gratis, senza registrazione.`
- **EN Title (48):** `Free llms.txt generator tool | Studio Remarka`
- **EN Description (150):** `Create your llms.txt in a minute: answer three questions or paste your URL and the AI writes the file. Copy or download it. Free, no sign-up required.`
- **RU Title (49):** `Генератор llms.txt бесплатно | Studio Remarka`
- **RU Description (149):** `Создайте llms.txt за минуту: ответьте на три вопроса или вставьте адрес — ИИ напишет файл. Скопируйте или скачайте. Бесплатно, без регистрации.`

**Проверка длин (пересчитано программно, №2 corretto 16.07).** Title: IT 53/51/46, EN 53/53/45, RU 48/53/45 — все ≤60.
Description: IT 156/155/153, EN 154/151/150, RU 150/152/149 — все ≤160.

---

## 7. Абзац для страницы `/strumenti/` (карточки новых инструментов)

Вставить в интро/сетку strumenti-index (после существующих 8 карточек — три
новые «AI»-карточки; тон единый):

> `Tre strumenti AI, nuovi. «Il vostro sito, letto dall'AI» vi mostra cosa
> capisce un assistente artificiale quando incontra la vostra home. «Suona
> madrelingua?» dice se i vostri testi in inglese o russo suonano nativi o
> sanno di traduzione — il nostro mestiere dal 2001. Il «Generatore di
> llms.txt» scrive per voi il file che spiega il sito agli assistenti AI,
> pronto da scaricare. Gratis, senza registrazione: è l'intelligenza
> artificiale al servizio del vostro sito, non del contrario.`
> (*corretto 16.07.2026 per il nuovo §2*)

Подписи карточек (краткие, = `descrizione`):
- `Il vostro sito, letto dall'AI` — `Cosa capisce l'AI del vostro sito, e come vi citerebbe.`
- `Suona madrelingua?` — `I vostri testi in inglese o russo suonano nativi?`
- `Generatore di llms.txt` — `Il vostro llms.txt, scritto e pronto da scaricare.`

---

## 8. Перелинковка (с каких страниц/статей ссылаться)

**Внутри Lab:**
- strumenti-index + home strumenti-cards: +3 карточки (сетка auto-fit выдержит 11).
- «Gli altri strumenti gratuiti» на каждой странице инструмента: добавить 3 новых
  в перечень (генератор уже собирает список — расширить).
- Взаимные: `sito-pronto-ai` ↔ `sito-letto-dallai` (в обе стороны: «технические
  сигналы ↔ качественное чтение»); `generatore-llms-txt` → `sito-pronto-ai`
  (проверить результат) и ← `sito-pronto-ai` (если llms.txt отсутствует — «создайте здесь»).

**Из услуг (по одной строке-ссылке в существующую секцию, без ломки структуры):**
- `seo-tecnica` → `sito-letto-dallai` + `generatore-llms-txt` (усиление AI-визибилити);
- `siti-multilingue` и `export-ready` → `suona-madrelingua` (*corretto 16.07*; теперь особенно уместно для export-ready)
  («provate se i vostri testi suonano nativi»).

**Из блога:**
- `/blog/llms-txt-cos-e/` → `generatore-llms-txt` (CTA «создайте свой сейчас»);
- `/blog/farsi-trovare-da-chatgpt-geo/` → `sito-letto-dallai` (+ `sito-pronto-ai`);
- будущая статья про локализацию/переводы → `suona-madrelingua`.

**Из PDF check-up (№4):** абзац AI-инсайта живёт внутри отчёта; на экране
check-up ссылку не добавляем (не перегружать), но в письме-доставке можно
упомянуть флагман `sito-letto-dallai` как следующий шаг (опционально, решает владелец).
