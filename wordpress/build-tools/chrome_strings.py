"""Шаблонная микро-копия генератора (eyebrow/кнопки/заголовки секций),
не входящая в корпус data.py. Переведена редактором (носитель EN/RU),
терминология согласована с corpus_en/corpus_ru: preventivo chiuso →
EN "fixed quote" / RU «фиксированная смета»; цены в EN — американский
формат (€2,500), в RU — итальянский локальный (€ 2.500) сохраняется.
Формат: {it_string: {'en': ..., 'ru': ...}}"""

CHROME = {
    # Riga di fiducia sotto i bottoni della card premium .sr-cta-band
    # (redesign 18.07.2026, generate_pages.py:cta_trust_row()).
    '100% gratuito': {'en': '100% free', 'ru': '100% бесплатно'},
    'Nessun impegno': {'en': 'No obligation', 'ru': 'Никаких обязательств'},
    'Risposta in 24 ore': {'en': 'Response within 24 hours', 'ru': 'Ответ за 24 часа'},
    'Preventivo dettagliato': {'en': 'Detailed quote', 'ru': 'Подробная смета'},
    'Dati al sicuro': {'en': 'Your data, protected', 'ru': 'Данные под защитой'},
    'Massima riservatezza': {'en': 'Full confidentiality', 'ru': 'Полная конфиденциальность'},

    'Scopri i siti multilingue': {'en': 'Discover our multilingual websites', 'ru': 'Многоязычные сайты'},
    'Manca l’llms.txt? Createlo qui in un minuto →': {'en': 'Missing an llms.txt? Create one here in a minute →', 'ru': 'Нет llms.txt? Создайте его здесь за минуту →'},
    'Volete sapere come l’AI legge davvero il vostro sito? →': {'en': 'Want to know how AI actually reads your site? →', 'ru': 'Хотите узнать, как ИИ на самом деле читает ваш сайт? →'},
    'Scoprite come l’AI legge davvero il vostro sito →': {'en': 'See how AI actually reads your site →', 'ru': 'Узнайте, как ИИ на самом деле читает ваш сайт →'},
    'Createvi un llms.txt in un minuto →': {'en': 'Create your llms.txt in a minute →', 'ru': 'Создайте llms.txt за минуту →'},
    'Scoprite come l’AI legge davvero il vostro sito — gratis →': {'en': 'See how AI actually reads your site — free →', 'ru': 'Узнайте, как ИИ на самом деле читает ваш сайт — бесплатно →'},
    'Create il vostro llms.txt in un minuto: generatore gratuito →': {'en': 'Create your llms.txt in a minute: free generator →', 'ru': 'Создайте llms.txt за минуту: бесплатный генератор →'},
    'Provate se i vostri testi suonano madrelingua →': {'en': 'Test whether your texts sound native →', 'ru': 'Проверьте, звучат ли ваши тексты как у носителя →'},
    'Il vostro sito, letto dall’AI': {'en': 'Your website, read by AI', 'ru': 'Ваш сайт, прочитанный ИИ'},
    'Incollate l’indirizzo: un’intelligenza artificiale legge la vostra home come farebbe ChatGPT o un assistente AI, e vi dice cosa ha capito. Di cosa vi occupate, per chi, e quanto è facile — per un’AI — citarvi in una risposta. In meno di un minuto, un verdetto e le tre mosse che contano. Non è il check tecnico di «Pronto per l’AI»: qui l’AI vi legge davvero.': {'en': 'Paste your address: an artificial intelligence reads your homepage the way ChatGPT or an AI assistant would, and tells you what it understood. What you do, who for, and how easy it is — for an AI — to cite you in an answer. In under a minute, a verdict and the three moves that matter. This isn’t the technical check from «Ready for AI»: here the AI actually reads you.', 'ru': 'Вставьте адрес: искусственный интеллект читает вашу главную страницу так, как это сделал бы ChatGPT или ИИ-ассистент, и говорит, что понял. Чем вы занимаетесь, для кого, и насколько легко — для ИИ — процитировать вас в ответе. Меньше чем за минуту — вердикт и три шага, которые важнее всего. Это не технический чек «Готов к ИИ»: здесь ИИ по-настоящему вас читает.'},
    'Cosa capisce l’AI del vostro sito, e come vi citerebbe.': {'en': 'What the AI understands about your site, and how it would cite you.', 'ru': 'Что ИИ понимает о вашем сайте и как бы он вас процитировал.'},
    'Incollate l’indirizzo': {'en': 'Paste the address', 'ru': 'Вставьте адрес'},
    'La home o la pagina che vi rappresenta. Nessuna registrazione, nessun dato di pagamento.': {'en': 'Your homepage or the page that represents you. No sign-up, no payment details.', 'ru': 'Главная страница или та, что представляет вас. Без регистрации, без платёжных данных.'},
    'L’AI legge come un assistente': {'en': 'The AI reads like an assistant', 'ru': 'ИИ читает как ассистент'},
    'Il nostro server prende il testo, i titoli, i dati strutturati, l’llms.txt e il robots.txt della pagina e li passa a un modello di intelligenza artificiale, con le stesse informazioni che vede un assistente AI quando vi incontra.': {'en': 'Our server takes the text, headings, structured data, llms.txt and robots.txt of the page and passes them to an AI model — the same information an AI assistant sees when it comes across you.', 'ru': 'Наш сервер забирает текст, заголовки, структурированные данные, llms.txt и robots.txt страницы и передаёт их модели искусственного интеллекта — ту же информацию, что видит ИИ-ассистент, когда встречает вас.'},
    'Leggete cosa ha capito': {'en': 'See what it understood', 'ru': 'Узнайте, что он понял'},
    'Cosa fate e per chi, secondo l’AI; un punteggio di «citabilità» da 0 a 100; e tre mosse concrete, in forma di «fate X → ottenete Y». Il resto dell’analisi ve lo mandiamo via e-mail.': {'en': 'What you do and who for, according to the AI; a «citability» score from 0 to 100; and three concrete moves, in the form «do X → get Y». We send you the rest of the analysis by e-mail.', 'ru': 'Чем вы занимаетесь и для кого — по мнению ИИ; оценка «цитируемости» от 0 до 100; и три конкретных шага в формате «сделайте X → получите Y». Остальной разбор мы пришлём вам на e-mail.'},
    'È lo stesso di «Il sito è pronto per l’AI?»': {'en': 'Is this the same as «Is your site ready for AI?»', 'ru': 'Это то же самое, что «Сайт готов к ИИ?»'},
    'No, sono complementari. «Pronto per l’AI» controlla i segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e dà un punteggio su 4. Qui l’AI legge davvero i contenuti e vi dice cosa ha capito. Uno misura gli ingranaggi, l’altro il risultato.': {'en': 'No, they’re complementary. «Ready for AI» checks the technical signals — llms.txt, crawler access, structured data, sitemap — and gives a score out of 4. Here the AI actually reads your content and tells you what it understood. One measures the gears, the other the result.', 'ru': 'Нет, это дополняющие друг друга инструменты. «Готов к ИИ» проверяет технические сигналы — llms.txt, доступ для краулеров, структурированные данные, sitemap — и даёт оценку из 4. Здесь же ИИ по-настоящему читает контент и говорит, что понял. Один измеряет механику, другой — результат.'},
    'Conservate il testo del mio sito?': {'en': 'Do you store my site’s text?', 'ru': 'Вы сохраняете текст моего сайта?'},
    'No. Il contenuto della pagina viene letto una volta per generare l’analisi e non lo salviamo. In cache teniamo solo il risultato, per 24 ore, così una seconda prova sullo stesso sito è immediata.': {'en': 'No. The page content is read once to generate the analysis and we don’t save it. We only cache the result, for 24 hours, so a second run on the same site is instant.', 'ru': 'Нет. Содержимое страницы читается один раз для генерации анализа и не сохраняется. В кэше остаётся только результат — на 24 часа, поэтому повторная проверка того же сайта происходит мгновенно.'},
    'Perché l’analisi completa arriva via e-mail?': {'en': 'Why does the full analysis arrive by e-mail?', 'ru': 'Почему полный разбор приходит на e-mail?'},
    'A schermo trovate subito il verdetto e le tre mosse. Il resto — cosa ha capito l’AI, per chi vi vede, perché quel punteggio — ve lo inviamo via e-mail, così resta a portata di mano quando ne parlate con noi o col vostro team.': {'en': 'On screen you get the verdict and the three moves right away. We send you the rest — what the AI understood, who it thinks you’re for, why that score — by e-mail, so it stays handy when you talk about it with us or your team.', 'ru': 'На экране вы сразу видите вердикт и три шага. Остальное — что понял ИИ, для кого он вас видит, почему такая оценка — мы присылаем на e-mail, чтобы это было под рукой, когда вы обсуждаете это с нами или с командой.'},
    'Che cosa vede l’AI quando legge il vostro sito': {'en': 'What the AI sees when it reads your site', 'ru': 'Что видит ИИ, когда читает ваш сайт'},
    'Un assistente AI non «guarda» il sito come un visitatore: ne legge il testo, i titoli, la meta description, i dati strutturati e — se ci sono — l’llms.txt e le regole per i suoi crawler. Da quei segnali ricostruisce chi siete e cosa offrite. Noi passiamo a un modello esattamente quel materiale e gli chiediamo tre cose semplici: di cosa si occupa questo sito, a chi si rivolge, e quanto sarebbe sicuro di citarlo in una risposta. Il punteggio di citabilità nasce lì: non è la vostra posizione su ChatGPT, è quanto il vostro sito si spiega da solo.': {'en': 'An AI assistant doesn’t «look at» a site the way a visitor does: it reads the text, the headings, the meta description, the structured data and — if there are any — the llms.txt and the rules for its crawlers. From those signals it reconstructs who you are and what you offer. We pass a model exactly that material and ask it three simple things: what this site does, who it’s for, and how confident it would be citing it in an answer. That’s where the citability score comes from: it isn’t your ranking on ChatGPT, it’s how well your site explains itself.', 'ru': 'ИИ-ассистент не «смотрит» на сайт, как посетитель: он читает текст, заголовки, meta description, структурированные данные и — если они есть — llms.txt и правила для своих краулеров. По этим сигналам он восстанавливает, кто вы и что предлагаете. Мы передаём модели ровно этот материал и задаём три простых вопроса: чем занимается этот сайт, для кого он, и насколько уверенно модель процитировала бы его в ответе. Именно отсюда берётся оценка цитируемости: это не ваша позиция в ChatGPT, а то, насколько ваш сайт объясняет себя сам.'},
    'È giusto dire cosa questo strumento non fa. Non promette che ChatGPT vi nominerà, non conta quante volte siete già citati, non è un audit tecnico pagina per pagina. È una lettura qualitativa: lo specchio di come una macchina interpreta le vostre parole. Se l’AI capisce male, di solito è il sito a parlare poco chiaro — ed è una cosa che si aggiusta.': {'en': 'It’s only fair to say what this tool doesn’t do. It doesn’t promise ChatGPT will name you, it doesn’t count how many times you’re already cited, it isn’t a page-by-page technical audit. It’s a qualitative reading: a mirror of how a machine interprets your words. If the AI misunderstands, it’s usually the site that isn’t speaking clearly — and that’s something you can fix.', 'ru': 'Важно честно сказать, чего этот инструмент не делает. Он не обещает, что ChatGPT назовёт вас, не считает, сколько раз вас уже цитировали, это не постраничный технический аудит. Это качественное чтение: зеркало того, как машина интерпретирует ваши слова. Если ИИ понимает неверно, обычно дело в том, что сайт говорит недостаточно ясно, — а это можно исправить.'},
    'Come leggere il verdetto e la citabilità': {'en': 'How to read the verdict and the citability score', 'ru': 'Как читать вердикт и оценку цитируемости'},
    'Partite dal verdetto e dalle tre mosse: sono già ordinate per impatto e scritte come azioni, «fate questo → succede quello». Poi guardate la citabilità. Da 75 in su l’AI vi capisce e vi citerebbe volentieri: il sito si presenta bene. Tra 50 e 74 il senso c’è ma qualcosa confonde — un titolo generico, una home che non dice subito cosa vendete. Sotto 50 l’AI fatica a dire di cosa vi occupate: è la prima cosa da sistemare, prima di ogni tattica.': {'en': 'Start with the verdict and the three moves: they’re already ranked by impact and written as actions, «do this → that happens». Then look at the citability score. From 75 up, the AI understands you and would gladly cite you: the site presents itself well. Between 50 and 74, the sense is there but something is confusing — a generic title, a homepage that doesn’t say straight away what you sell. Below 50, the AI struggles to say what you do: that’s the first thing to fix, before any tactic.', 'ru': 'Начните с вердикта и трёх шагов: они уже упорядочены по влиянию и написаны как действия — «сделайте это → произойдёт то». Затем посмотрите на цитируемость. От 75 и выше ИИ вас понимает и охотно бы вас процитировал: сайт хорошо себя представляет. От 50 до 74 смысл понятен, но что-то сбивает с толку — общий заголовок, главная, которая не говорит сразу, что вы продаёте. Ниже 50 ИИ с трудом понимает, чем вы занимаетесь: это первое, что нужно исправить, раньше любой тактики.'},
    'Due letture da evitare. Un punteggio alto non significa «primo su ChatGPT»: significa che vi spiegate bene, il che è la precondizione, non la garanzia. E se «cosa ha capito» non vi somiglia, non è un errore dell’AI: è il segnale che il vostro sito, letto da fuori, racconta una storia diversa da quella che avete in testa.': {'en': 'Two readings to avoid. A high score doesn’t mean «first on ChatGPT»: it means you explain yourselves well, which is the precondition, not the guarantee. And if «what it understood» doesn’t sound like you, that isn’t the AI’s mistake: it’s a sign that your site, read from the outside, tells a different story from the one in your head.', 'ru': 'Есть два неверных толкования. Высокая оценка не значит «первое место в ChatGPT»: она значит, что вы хорошо объясняете себя, — это предпосылка, а не гарантия. А если «что понял ИИ» не похоже на вас — это не ошибка ИИ: это сигнал, что ваш сайт, если читать его со стороны, рассказывает другую историю, чем та, что у вас в голове.'},
    'Volete che l’AI vi capisca al primo colpo': {'en': 'Want the AI to understand you on the first try', 'ru': 'Хотите, чтобы ИИ понял вас с первого раза'},
    'Dal verdetto al lavoro: rendiamo il vostro sito leggibile agli assistenti AI e ai motori — contenuti chiari, dati strutturati, llms.txt. A prezzo chiuso, con PageSpeed 90+ garantito da contratto.': {'en': 'From verdict to work: we make your site readable by AI assistants and search engines — clear content, structured data, llms.txt. At a fixed price, with PageSpeed 90+ guaranteed by contract.', 'ru': 'От вердикта к делу: делаем ваш сайт понятным для ИИ-ассистентов и поисковых систем — понятный контент, структурированные данные, llms.txt. По фиксированной цене, с PageSpeed 90+ по договору.'},
    'Il sito è pronto per l’AI?': {'en': 'Is your site ready for AI?', 'ru': 'Готов ли сайт к ИИ?'},
    'Suona madrelingua?': {'en': 'Does it sound native?', 'ru': 'Звучит как у носителя?'},
    'Vendete anche in inglese o in russo? Incollate un testo del vostro sito: un’intelligenza artificiale vi dice se suona come l’avrebbe scritto un madrelingua, o se si sente la traduzione. Scegliete la lingua, incollate il testo: in pochi secondi un punteggio di naturalezza e tre correzioni concrete. Traduciamo per i mercati esteri dal 2001: questo è il nostro mestiere, in versione gratuita.': {'en': 'Do you also sell in English or Russian? Paste a text from your site: an artificial intelligence tells you if it sounds like a native speaker wrote it, or if it feels translated. Choose the language, paste the text: in a few seconds, a naturalness score and three concrete fixes. We’ve translated for foreign markets since 2001 — this is our trade, in a free version.', 'ru': 'Продаёте также на английском или русском? Вставьте текст с вашего сайта: искусственный интеллект скажет, звучит ли он так, как написал бы носитель языка, или чувствуется перевод. Выберите язык, вставьте текст: за несколько секунд — оценка естественности и три конкретные правки. Мы переводим для зарубежных рынков с 2001 года — это наше ремесло, в бесплатной версии.'},
    'I vostri testi in inglese o russo suonano nativi?': {'en': 'Do your English or Russian texts sound native?', 'ru': 'Ваши тексты на английском или русском звучат как у носителя?'},
    'Scegliete la lingua e incollate il testo': {'en': 'Choose the language and paste the text', 'ru': 'Выберите язык и вставьте текст'},
    'Un paragrafo della home, la descrizione di un prodotto, il chi siamo: nella lingua in cui vendete all’estero. Fino a circa 2.000 caratteri. Niente registrazione.': {'en': 'A paragraph from the homepage, a product description, the about page: in the language you sell abroad in. Up to about 2,000 characters. No sign-up.', 'ru': 'Абзац с главной страницы, описание товара, страница «о нас» — на языке, на котором вы продаёте за рубежом. До ~2000 знаков. Без регистрации.'},
    'L’AI lo legge come un madrelingua': {'en': 'The AI reads it like a native speaker', 'ru': 'ИИ читает его как носитель языка'},
    'Un modello di intelligenza artificiale valuta il testo come lo sentirebbe un lettore madrelingua di quella lingua: scorrevolezza, tono, calchi dall’italiano o da un’altra lingua, espressioni che tradiscono una traduzione.': {'en': 'An AI model evaluates the text the way a native reader of that language would feel it: flow, tone, calques from Italian or another language, phrasing that gives away a translation.', 'ru': 'Модель искусственного интеллекта оценивает текст так, как его почувствовал бы носитель этого языка: плавность, тон, кальки с итальянского или другого языка, обороты, выдающие перевод.'},
    'Leggete cosa cambiare': {'en': 'See what to change', 'ru': 'Узнайте, что изменить'},
    'Un punteggio di naturalezza da 0 a 100, il registro giusto per quel mercato, e tre correzioni «prima → dopo» spiegate.': {'en': 'A naturalness score from 0 to 100, the right tone for that market, and three explained «before → after» fixes.', 'ru': 'Оценка естественности от 0 до 100, подходящий тон для этого рынка и три объяснённые правки «было → стало».'},
    'Conservate il testo che incollo?': {'en': 'Do you store the text I paste?', 'ru': 'Вы сохраняете вставленный текст?'},
    'No. Il testo viene valutato una volta e non lo salviamo. In cache resta solo il risultato per 24 ore, così ripetere la stessa prova è immediato.': {'en': 'No. The text is evaluated once and we don’t save it. Only the result stays cached, for 24 hours, so repeating the same test is instant.', 'ru': 'Нет. Текст оценивается один раз и не сохраняется. В кэше остаётся только результат — на 24 часа, поэтому повторить ту же проверку можно мгновенно.'},
    'Corregge anche il testo al posto mio?': {'en': 'Does it rewrite the text for me?', 'ru': 'Он переписывает текст за меня?'},
    'Vi dà tre correzioni «prima → dopo» come esempio, non riscrive tutto. La riscrittura completa e coerente su tutto il sito è un lavoro da redattore madrelingua: è il nostro servizio di localizzazione.': {'en': 'It gives you three «before → after» fixes as examples, it doesn’t rewrite everything. A complete, consistent rewrite across the whole site is a native editor’s job: that’s our localization service.', 'ru': 'Он даёт три правки «было → стало» как пример, а не переписывает всё. Полная и последовательная переработка всего сайта — работа редактора-носителя языка: это наша услуга локализации.'},
    'Quali lingue valuta?': {'en': 'Which languages does it check?', 'ru': 'Какие языки он проверяет?'},
    'Le due lingue proposte in questa pagina: sono quelle utili a chi vende dall’Italia verso l’estero. La revisione completa la fanno redattori madrelingua, lingua per lingua, dal 2001.': {'en': 'The two languages offered on this page: the ones useful if you sell from Italy abroad. The full review is done by native-speaking editors, language by language, since 2001.', 'ru': 'Два языка, предложенных на этой странице: те, что полезны тем, кто продаёт из Италии за рубеж. Полную вычитку делают редакторы-носители языка, для каждого языка отдельно, с 2001 года.'},
    'Che cosa rende un testo «madrelingua»': {'en': 'What makes a text sound «native»', 'ru': 'Что делает текст «как у носителя»'},
    'Un testo può essere corretto e suonare comunque straniero. Succede quando la grammatica è a posto ma la costruzione è calcata su un’altra lingua: frasi troppo lunghe, un registro sbagliato, parole giuste al posto sbagliato, quel tono da manuale tradotto. Un lettore madrelingua non lo analizza — lo sente, e si fida meno. Chiediamo al modello proprio questo: non «ci sono errori?», ma «suona come l’avrebbe scritto una persona madrelingua?».': {'en': 'A text can be grammatically correct and still sound foreign. It happens when the grammar is fine but the construction is calqued from another language: sentences that run too long, the wrong tone, the right words in the wrong place, that translated-manual feel. A native reader doesn’t analyse it — they feel it, and trust it less. That’s exactly what we ask the model: not «are there errors?», but «does it sound like a native speaker would have written it?».', 'ru': 'Текст может быть грамматически верным и всё равно звучать иностранно. Это происходит, когда грамматика в порядке, но конструкция калькирована с другого языка: слишком длинные фразы, неверный тон, правильные слова не на своём месте, тот самый «переводной» привкус. Носитель языка это не анализирует — он это чувствует и доверяет меньше. Именно это мы и спрашиваем у модели: не «есть ли ошибки?», а «звучит ли это так, как написал бы носитель языка?».'},
    'Cosa non è. Non è un correttore ortografico: gli errori di battitura non sono il punto. Non è un giudizio letterario né un ranking SEO. È una valutazione di naturalezza e tono — la differenza tra un testo che passa e uno che vende. E come ogni lettura AI, è un parere, non un verdetto: la revisione vera la fa un redattore madrelingua, lingua per lingua, che è esattamente ciò che facciamo dal 2001.': {'en': 'What it isn’t. It isn’t a spell-checker: typos aren’t the point. It isn’t a literary judgement or an SEO ranking. It’s an assessment of naturalness and tone — the difference between a text that’s passable and one that sells. And like any AI reading, it’s an opinion, not a verdict: the real review is done by a native-speaking editor, language by language, which is exactly what we’ve done since 2001.', 'ru': 'Чего это не делает. Это не орфографическая проверка: опечатки — не главное. Это не литературная оценка и не SEO-рейтинг. Это оценка естественности и тона — разница между текстом, который «сойдёт», и тем, который продаёт. И, как любое чтение ИИ, это мнение, а не приговор: настоящую вычитку делает редактор-носитель языка, для каждого языка отдельно, — именно этим мы занимаемся с 2001 года.'},
    'Come leggere il punteggio di naturalezza': {'en': 'How to read the naturalness score', 'ru': 'Как читать оценку естественности'},
    'Il punteggio dice quanto il testo suona nativo in quella lingua. Da 75 in su siete a posto: un madrelingua lo leggerebbe senza inciampi. Tra 50 e 74 il senso c’è, ma qualcosa stona — un calco, una frase contorta, un registro sbagliato — e le tre correzioni vi dicono dove. Sotto 50 si sente la traduzione: il testo funziona per capirsi, non ancora per convincere. Partite dalle correzioni: sono le tre che spostano di più.': {'en': 'The score tells you how native the text sounds in that language. From 75 up, you’re fine: a native speaker would read it without stumbling. Between 50 and 74, the sense is there, but something feels off — a calque, a twisted sentence, the wrong tone — and the three fixes tell you where. Below 50, the translation shows: the text works to be understood, not yet to convince. Start with the fixes: they’re the three that move the needle most.', 'ru': 'Оценка показывает, насколько текст звучит как у носителя этого языка. От 75 и выше всё в порядке: носитель прочтёт без запинок. От 50 до 74 смысл понятен, но что-то режет слух — калька, витиеватая фраза, неверный тон — и три правки подскажут, где именно. Ниже 50 чувствуется перевод: текст работает, чтобы его поняли, но ещё не для того, чтобы убедить. Начните с правок: это те три, что дают наибольший эффект.'},
    'Un’avvertenza onesta. Un punteggio alto non certifica che il testo sia perfetto per il vostro pubblico: il tono giusto per una gioielleria non è quello giusto per un’officina. Usate il registro come bussola, non come voto finale. E ricordate che l’AI legge il testo che incollate, non l’intero sito: è una sonda, non un audit.': {'en': 'An honest caveat. A high score doesn’t certify the text is perfect for your audience: the right tone for a jewellery shop isn’t the right tone for a workshop. Use the register as a compass, not a final grade. And remember the AI reads the text you paste, not the whole site: it’s a probe, not an audit.', 'ru': 'Честная оговорка. Высокая оценка не гарантирует, что текст идеален именно для вашей аудитории: верный тон для ювелирного салона — не тот же, что для мастерской. Используйте регистр как компас, а не как окончательную оценку. И помните: ИИ читает вставленный вами текст, а не весь сайт целиком — это зонд, а не аудит.'},
    'Volete che i vostri testi parlino come un madrelingua': {'en': 'Want your texts to sound like a native speaker wrote them', 'ru': 'Хотите, чтобы ваши тексты звучали как у носителя языка'},
    'Dal 2001 traduciamo e adattiamo siti per i mercati esteri con redattori madrelingua — non un plugin, un deliverable con nome e cognome. Prezzo chiuso, consegna a data fissa.': {'en': 'Since 2001 we’ve translated and adapted websites for foreign markets with native-speaking editors — not a plugin, a deliverable with a name and a face. Fixed price, delivery on a fixed date.', 'ru': 'С 2001 года мы переводим и адаптируем сайты для зарубежных рынков силами редакторов-носителей языка — не плагин, а результат работы конкретного человека. Фиксированная цена, точный срок сдачи.'},
    'Generatore di llms.txt': {'en': 'llms.txt generator', 'ru': 'Генератор llms.txt'},
    'Il file che spiega il vostro sito agli assistenti AI, pronto da scaricare. Rispondete a tre domande — o incollate solo l’indirizzo e i dati li raccogliamo noi — e un’intelligenza artificiale scrive il vostro llms.txt: struttura corretta, pagine chiave, descrizione chiara. Da copiare, scaricare e mettere online. Gratis, senza registrazione.': {'en': 'The file that explains your site to AI assistants, ready to download. Answer three questions — or just paste your address and we’ll gather the data — and an artificial intelligence writes your llms.txt: correct structure, key pages, a clear description. Copy it, download it, put it online. Free, no sign-up.', 'ru': 'Файл, который объясняет ваш сайт ИИ-ассистентам, готовый к скачиванию. Ответьте на три вопроса — или просто вставьте адрес, а данные мы соберём сами — и искусственный интеллект напишет ваш llms.txt: правильная структура, ключевые страницы, понятное описание. Скопируйте, скачайте и разместите на сайте. Бесплатно, без регистрации.'},
    'Il vostro llms.txt, scritto e pronto da scaricare.': {'en': 'Your llms.txt, written and ready to download.', 'ru': 'Ваш llms.txt — написан и готов к скачиванию.'},
    'Dateci l’essenziale': {'en': 'Give us the essentials', 'ru': 'Дайте нам самое главное'},
    'Nome, di cosa vi occupate, le pagine che contano. Oppure incollate solo l’indirizzo del sito: leggiamo noi la home e ricaviamo i dati.': {'en': 'Your name, what you do, the pages that matter. Or just paste your site’s address: we’ll read the homepage and work out the details ourselves.', 'ru': 'Название, чем вы занимаетесь, важные страницы. Или просто вставьте адрес сайта: мы сами прочитаем главную и извлечём данные.'},
    'L’AI scrive il file': {'en': 'The AI writes the file', 'ru': 'ИИ пишет файл'},
    'Un modello di intelligenza artificiale compone l’llms.txt nel formato che i crawler AI si aspettano: un’intestazione con il nome, una descrizione sintetica, l’elenco delle pagine importanti con una riga ciascuna.': {'en': 'An AI model composes the llms.txt in the format AI crawlers expect: a heading with your name, a concise description, the list of important pages with one line each.', 'ru': 'Модель искусственного интеллекта составляет llms.txt в формате, которого ожидают ИИ-краулеры: заголовок с названием, краткое описание, список важных страниц с одной строкой на каждую.'},
    'Copiate, scaricate, pubblicate': {'en': 'Copy, download, publish', 'ru': 'Скопируйте, скачайте, опубликуйте'},
    'Il file è pronto: lo copiate con un clic o lo scaricate come llms.txt. Va caricato nella cartella principale del sito, accanto al robots.txt.': {'en': 'The file is ready: copy it with one click or download it as llms.txt. Upload it to your site’s root folder, next to robots.txt.', 'ru': 'Файл готов: скопируйте его в один клик или скачайте как llms.txt. Загрузите его в корневую папку сайта, рядом с robots.txt.'},
    'Devo per forza avere un llms.txt?': {'en': 'Do I really need an llms.txt?', 'ru': 'Обязательно ли иметь llms.txt?'},
    'Non è obbligatorio come il robots.txt, ma è un segnale in crescita: da maggio 2026 Google lo considera nell’audit «Agentic Browsing» di Lighthouse. A costo zero, è tra le cose più facili da fare per farsi leggere meglio dagli assistenti AI.': {'en': 'It isn’t mandatory like robots.txt, but it’s a growing signal: since May 2026 Google factors it into Lighthouse’s «Agentic Browsing» audit. At zero cost, it’s one of the easiest things you can do to be read better by AI assistants.', 'ru': 'Он не обязателен, как robots.txt, но это растущий сигнал: с мая 2026 года Google учитывает его в аудите Lighthouse «Agentic Browsing». Бесплатно, а это одна из самых простых вещей, которые можно сделать, чтобы вас лучше читали ИИ-ассистенты.'},
    'Conservate i dati che inserisco?': {'en': 'Do you store the data I enter?', 'ru': 'Вы сохраняете введённые данные?'},
    'No. Usiamo i dati (o il testo della home, se date solo l’indirizzo) una volta per generare il file e non li salviamo. In cache resta solo il risultato per 24 ore.': {'en': 'No. We use the data (or the homepage text, if you only give the address) once to generate the file and don’t save it. Only the result stays cached, for 24 hours.', 'ru': 'Нет. Мы используем данные (или текст главной, если вы дали только адрес) один раз для генерации файла и не сохраняем их. В кэше остаётся только результат — на 24 часа.'},
    'Basta l’llms.txt per farsi trovare da ChatGPT?': {'en': 'Is llms.txt enough to be found by ChatGPT?', 'ru': 'Достаточно ли llms.txt, чтобы вас нашёл ChatGPT?'},
    'No, è un pezzo del puzzle. Farsi citare dagli assistenti AI dipende anche da contenuti chiari, dati strutturati e autorevolezza. L’llms.txt aiuta a spiegarsi; il resto è SEO tecnica e contenuti.': {'en': 'No, it’s one piece of the puzzle. Being cited by AI assistants also depends on clear content, structured data and authority. llms.txt helps you explain yourself; the rest is technical SEO and content.', 'ru': 'Нет, это только часть головоломки. То, будут ли вас цитировать ИИ-ассистенты, зависит ещё от понятного контента, структурированных данных и авторитетности. llms.txt помогает объясниться; остальное — техническое SEO и контент.'},
    'Che cos’è l’llms.txt e cosa ci mettiamo dentro': {'en': 'What llms.txt is, and what we put in it', 'ru': 'Что такое llms.txt и что мы в него вкладываем'},
    'L’llms.txt è un file di testo, in formato Markdown, che vive nella radice del sito e riassume — per gli assistenti AI — chi siete e quali sono le vostre pagine importanti. È al mondo dei modelli AI quello che il robots.txt è a Google: una mappa breve e leggibile, che i crawler di ChatGPT, Perplexity o Claude leggono più volentieri dell’HTML. Noi generiamo l’intestazione con il nome, una descrizione onesta del business e la lista delle pagine chiave, ognuna con la sua riga di contesto.': {'en': 'llms.txt is a plain-text file, in Markdown format, that lives at the root of your site and sums up — for AI assistants — who you are and which pages of yours matter. It’s to the world of AI models what robots.txt is to Google: a short, readable map that ChatGPT’s, Perplexity’s or Claude’s crawlers read more willingly than raw HTML. We generate the heading with your name, an honest description of the business, and the list of key pages, each with its own line of context.', 'ru': 'llms.txt — это текстовый файл в формате Markdown, который лежит в корне сайта и кратко описывает для ИИ-ассистентов, кто вы и какие ваши страницы важны. Для мира ИИ-моделей это то же самое, чем для Google является robots.txt: короткая, понятная карта, которую краулеры ChatGPT, Perplexity или Claude читают охотнее, чем HTML. Мы генерируем заголовок с названием, честное описание бизнеса и список ключевых страниц, у каждой — своя строка контекста.'},
    'Cosa non è. L’llms.txt non è una bacchetta magica: non garantisce di essere citati e, da solo, non fa SEO. È un pezzo — utile e a costo zero — di un lavoro più ampio di visibilità sugli assistenti AI. Il file che generiamo è un ottimo punto di partenza: rileggetelo, sistemate la descrizione se serve, e verificate che le pagine elencate siano davvero quelle giuste.': {'en': 'What it isn’t. llms.txt isn’t a magic wand: it doesn’t guarantee you’ll be cited and, on its own, it isn’t SEO. It’s one piece — useful and free — of a bigger job of visibility with AI assistants. The file we generate is a great starting point: re-read it, tweak the description if needed, and check the pages listed are really the right ones.', 'ru': 'Чего это не даёт. llms.txt — не волшебная палочка: он не гарантирует, что вас процитируют, и сам по себе не является SEO. Это один элемент — полезный и бесплатный — более широкой работы по видимости для ИИ-ассистентов. Файл, который мы генерируем, — отличная отправная точка: перечитайте его, поправьте описание, если нужно, и проверьте, что перечисленные страницы действительно те, что нужно.'},
    'Come usare il file che avete generato': {'en': 'How to use the file you generated', 'ru': 'Как использовать сгенерированный файл'},
    'Il risultato è il file completo, pronto. Copiatelo o scaricatelo, poi caricatelo nella cartella principale del sito — la stessa dove vive il robots.txt — così l’indirizzo finale è iltuosito.it/llms.txt. Da lì i crawler AI lo trovano da soli. Sotto al file trovate una nota: di solito è un dettaglio da controllare a mano, come una descrizione da personalizzare o una pagina da aggiungere.': {'en': 'The result is the complete, ready file. Copy or download it, then upload it to your site’s root folder — the same one where robots.txt lives — so the final address is yoursite.com/llms.txt. From there AI crawlers find it on their own. Below the file you’ll find a note: usually a detail worth checking by hand, like a description to personalise or a page to add.', 'ru': 'Результат — это полный, готовый файл. Скопируйте его или скачайте, затем загрузите в корневую папку сайта — ту же, где лежит robots.txt, — чтобы итоговый адрес был вашсайт.рф/llms.txt. Оттуда ИИ-краулеры найдут его сами. Под файлом вы найдёте примечание: обычно это деталь, которую стоит проверить вручную, например описание, которое нужно доработать, или страницу, которую стоит добавить.'},
    'Un consiglio. Rileggete sempre la descrizione prima di pubblicare: l’AI la scrive dai dati che le date, ma nessuno conosce il vostro business meglio di voi. Due minuti di rilettura valgono più di dieci righe generate al volo. E aggiornatelo quando aggiungete pagine importanti: un llms.txt vecchio racconta un sito che non c’è più.': {'en': 'One tip. Always re-read the description before publishing: the AI writes it from the data you give it, but nobody knows your business better than you. Two minutes of proofreading are worth more than ten lines generated on the fly. And update it whenever you add important pages: an outdated llms.txt describes a site that no longer exists.', 'ru': 'Один совет. Всегда перечитывайте описание перед публикацией: ИИ пишет его на основе данных, которые вы дали, но никто не знает ваш бизнес лучше вас. Две минуты вычитки стоят больше, чем десять строк, сгенерированных на лету. И обновляйте файл, когда добавляете важные страницы: устаревший llms.txt описывает сайт, которого уже не существует.'},
    'Volete essere trovati e citati dagli assistenti AI': {'en': 'Want to be found and cited by AI assistants', 'ru': 'Хотите, чтобы вас находили и цитировали ИИ-ассистенты'},
    'L’llms.txt è il primo passo. Il resto — dati strutturati, contenuti leggibili dalle AI, SEO tecnica — lo costruiamo noi, a prezzo chiuso e con PageSpeed 90+ garantito da contratto.': {'en': 'llms.txt is the first step. The rest — structured data, AI-readable content, technical SEO — we build for you, at a fixed price and with PageSpeed 90+ guaranteed by contract.', 'ru': 'llms.txt — это первый шаг. Остальное — структурированные данные, контент, понятный ИИ, техническое SEO — делаем мы, по фиксированной цене и с PageSpeed 90+ по договору.'},
    'Analizza': {'en': 'Analyze', 'ru': 'Проверить'},
    'Valuta il testo': {'en': 'Check the text', 'ru': 'Оценить текст'},
    'L’AI sta leggendo il vostro sito…': {'en': 'The AI is reading your site…', 'ru': 'ИИ читает ваш сайт…'},
    'L’AI sta valutando il testo…': {'en': 'The AI is checking the text…', 'ru': 'ИИ оценивает текст…'},
    'L’AI sta scrivendo il vostro llms.txt…': {'en': 'The AI is writing your llms.txt…', 'ru': 'ИИ пишет ваш llms.txt…'},
    'Lo strumento non è disponibile in questo momento. Riprovate tra poco.': {'en': 'The tool isn’t available right now. Please try again shortly.', 'ru': 'Инструмент сейчас недоступен. Попробуйте чуть позже.'},
    'Strumento in manutenzione.': {'en': 'Tool under maintenance.', 'ru': 'Инструмент на обслуживании.'},
    'Avete raggiunto il limite di prove per oggi. Riprovate domani.': {'en': 'You’ve reached today’s limit. Please try again tomorrow.', 'ru': 'Достигнут лимит проверок на сегодня. Попробуйте завтра.'},
    'Non salviamo il contenuto: è una lettura dell’AI, non un audit certificato.': {'en': 'We don’t store the content: it’s an AI reading, not a certified audit.', 'ru': 'Мы не сохраняем контент: это чтение ИИ, не сертифицированный аудит.'},
    'Non salviamo il testo: è una lettura dell’AI, non un audit certificato.': {'en': 'We don’t store the text: it’s an AI reading, not a certified audit.', 'ru': 'Мы не сохраняем текст: это чтение ИИ, не сертифицированный аудит.'},
    'Non salviamo i dati: è una lettura dell’AI, non un audit certificato.': {'en': 'We don’t store the data: it’s an AI reading, not a certified audit.', 'ru': 'Мы не сохраняем данные: это чтение ИИ, не сертифицированный аудит.'},
    'Citabilità AI': {'en': 'AI citability', 'ru': 'Цитируемость для ИИ'},
    'Le 3 mosse': {'en': 'The 3 moves', 'ru': '3 шага'},
    'Ricevete l’analisi completa via e-mail': {'en': 'Get the full analysis by e-mail', 'ru': 'Получите полный разбор на e-mail'},
    'La vostra e-mail': {'en': 'Your e-mail', 'ru': 'Ваш e-mail'},
    'Acconsento a essere ricontattato da Studio Remarka.': {'en': 'I agree to be contacted by Studio Remarka.', 'ru': 'Согласен(на) на связь со Studio Remarka.'},
    'Ricevi l’analisi completa': {'en': 'Send me the full analysis', 'ru': 'Отправить полный разбор'},
    'Fatto: controllate la posta.': {'en': 'Done — check your inbox.', 'ru': 'Готово — проверьте почту.'},
    'Incollate qui il testo da valutare (max ~2.000 caratteri)…': {'en': 'Paste the text to check here (max ~2,000 characters)…', 'ru': 'Вставьте текст для проверки (макс. ~2000 знаков)…'},
    'Lingua del testo:': {'en': 'Text language:', 'ru': 'Язык текста:'},
    'Suona nativo': {'en': 'Sounds native', 'ru': 'Звучит как у носителя'},
    'Si sente la traduzione': {'en': 'Sounds translated', 'ru': 'Слышен перевод'},
    'Naturalezza': {'en': 'Naturalness', 'ru': 'Естественность'},
    'Registro': {'en': 'Tone', 'ru': 'Тон'},
    '3 correzioni': {'en': '3 fixes', 'ru': '3 правки'},
    'Prima': {'en': 'Before', 'ru': 'Было'},
    'Dopo': {'en': 'After', 'ru': 'Стало'},
    'Incollate almeno una frase.': {'en': 'Paste at least one sentence.', 'ru': 'Вставьте хотя бы одно предложение.'},
    'Compila i campi': {'en': 'Fill in the fields', 'ru': 'Заполнить поля'},
    'Ho solo l’indirizzo': {'en': 'I only have the URL', 'ru': 'Только адрес'},
    'Nome del sito / attività': {'en': 'Site / business name', 'ru': 'Название сайта / бизнеса'},
    'Di cosa vi occupate': {'en': 'What you do', 'ru': 'Чем вы занимаетесь'},
    'Pagine chiave (una per riga)': {'en': 'Key pages (one per line)', 'ru': 'Ключевые страницы (по одной в строке)'},
    'Copia': {'en': 'Copy', 'ru': 'Копировать'},
    'Copiato': {'en': 'Copied', 'ru': 'Скопировано'},
    'Scarica llms.txt': {'en': 'Download llms.txt', 'ru': 'Скачать llms.txt'},
    'Manca l’llms.txt? Createlo qui in un minuto': {'en': 'Missing an llms.txt? Create one here in a minute', 'ru': 'Нет llms.txt? Создайте его здесь за минуту'},
    'Volete sapere come l’AI legge davvero il vostro sito?': {'en': 'Want to know how AI actually reads your site?', 'ru': 'Хотите узнать, как ИИ на самом деле читает ваш сайт?'},
    'Scoprite come l’AI legge davvero il vostro sito': {'en': 'See how AI actually reads your site', 'ru': 'Узнайте, как ИИ на самом деле читает ваш сайт'},
    'Createvi un llms.txt in un minuto': {'en': 'Create your llms.txt in a minute', 'ru': 'Создайте llms.txt за минуту'},
    'Provate se i vostri testi suonano madrelingua': {'en': 'Test whether your texts sound native', 'ru': 'Проверьте, звучат ли ваши тексты как у носителя'},
    'Create il vostro llms.txt in un minuto: generatore gratuito': {'en': 'Create your llms.txt in a minute: free generator', 'ru': 'Создайте llms.txt за минуту: бесплатный генератор'},
    'Scoprite come l’AI legge davvero il vostro sito — gratis': {'en': 'See how AI actually reads your site — free', 'ru': 'Узнайте, как ИИ на самом деле читает ваш сайт — бесплатно'},
    'Tre strumenti AI, nuovi. «Il vostro sito, letto dall’AI» vi mostra cosa capisce un assistente artificiale quando incontra la vostra home. «Suona madrelingua?» dice se i vostri testi in inglese o russo suonano nativi o sanno di traduzione — il nostro mestiere dal 2001. Il «Generatore di llms.txt» scrive per voi il file che spiega il sito agli assistenti AI, pronto da scaricare. Gratis, senza registrazione: è l’intelligenza artificiale al servizio del vostro sito, non del contrario.': {'en': 'Three new AI tools. «Your website, read by AI» shows you what an artificial assistant understands when it comes across your homepage. «Does it sound native?» tells you if your English or Russian texts sound native or feel translated — our trade since 2001. The «llms.txt generator» writes, for you, the file that explains your site to AI assistants, ready to download. Free, no sign-up: it’s artificial intelligence at the service of your site, not the other way round.', 'ru': 'Три новых ИИ-инструмента. «Ваш сайт, прочитанный ИИ» показывает, что понимает искусственный ассистент, когда встречает вашу главную страницу. «Звучит как у носителя?» говорит, звучат ли ваши тексты на английском или русском как у носителя языка или чувствуется перевод — наше ремесло с 2001 года. «Генератор llms.txt» пишет для вас файл, который объясняет сайт ИИ-ассистентам, готовый к скачиванию. Бесплатно, без регистрации: искусственный интеллект на службе у вашего сайта, а не наоборот.'},
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
    'Analisi SEO — gratis': {'en': 'SEO analysis — free', 'ru': 'SEO-анализ — бесплатно'},
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
    'Misura la velocità — gratis': {'en': 'Measure your speed — free', 'ru': 'Измерить скорость — бесплатно'},
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

    # ---- link "Approfondisci" per card (data-more-label + testo statico) ----
    'Approfondisci →': {'en': 'See the full test →'},

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

# CHROME_BLOG — Blog · Batch 1 (5 articoli IT → EN). Copre ogni nodo di testo
# visibile generato da build_blog_post: titolo (H1 + indice), estratto, corpo,
# titoli H2, paragrafi, voci di lista, alt e didascalie delle illustrazioni,
# etichette dei link contestuali e delle CTA (con « →» finale). Solo EN: la
# versione RU del blog è un batch a parte, non una traduzione (translate_pages
# ru resta vietato). Redazione EN madrelingua; numeri in formato US.
CHROME_BLOG = {
    '15 LUG 2026': {'en': '15 JUL 2026'},
    # ---------- Articolo 1 — EAA e-commerce ----------
    'EAA 2026: cosa rischia davvero il vostro e-commerce':
        {'en': 'EAA 2026: what your e-commerce site really risks'},
    'Dal 28 giugno 2025 l’accessibilità è un obbligo di legge, con sanzioni fino al 5% del fatturato. Chi è coinvolto, chi resta fuori e da dove partire, senza allarmismi.':
        {'en': 'Since 28 June 2025 accessibility is a legal requirement, with fines up to 5% of revenue. Who’s covered, who’s exempt, and where to start — without the scaremongering.'},
    'European Accessibility Act e-commerce: la scadenza del 28 giugno 2025, lo standard WCAG 2.1 AA e la sanzione fino al 5% del fatturato':
        {'en': 'European Accessibility Act e-commerce: the 28 June 2025 deadline, the WCAG 2.1 AA standard, and fines up to 5% of revenue'},
    'Il 28 giugno 2025 è passato in sordina, e proprio per questo fa più danni. Da quella data l’European Accessibility Act è una legge applicata anche in Italia, e tocca molti più e-commerce di quanti se ne siano accorti: se vendete online a dei consumatori, con ogni probabilità il vostro negozio deve essere usabile anche dalle persone con disabilità — non come cortesia, ma per obbligo, con sanzioni che il recepimento italiano fissa fino al 5% del fatturato. Niente panico e niente finta indifferenza: vediamo cosa rischia davvero il vostro e-commerce, chi resta fuori e cosa conviene fare adesso.':
        {'en': '28 June 2025 came and went quietly, and that’s exactly why it does more damage. Since that date the European Accessibility Act has been enforced law in Italy too, and it affects far more e-commerce sites than have noticed: if you sell online to consumers, your store most likely has to be usable by people with disabilities as well — not as a courtesy, but by law, with fines the Italian transposition sets at up to 5% of revenue. No panic, and no pretending it isn’t happening: let’s look at what your e-commerce site really risks, who’s left out, and what’s worth doing now.'},
    'Che cos’è l’European Accessibility Act, in parole vostre':
        {'en': 'What the European Accessibility Act is, in plain terms'},
    'L’European Accessibility Act (EAA) nasce dalla direttiva europea 2019/882, e l’idea è persino ovvia una volta detta. Un negozio fisico con tre gradini all’ingresso e nessuna rampa lascia fuori una parte dei clienti; un e-commerce con contrasti illeggibili, immagini senza descrizione e un checkout che non si completa da tastiera fa esattamente la stessa cosa, solo che non si vede. La norma chiede che i servizi digitali venduti ai consumatori siano usabili anche da chi ha una disabilità visiva, motoria o cognitiva.':
        {'en': 'The European Accessibility Act (EAA) comes from EU Directive 2019/882, and the idea is almost obvious once you say it out loud. A physical shop with three steps at the door and no ramp shuts out some of its customers; an e-commerce site with unreadable contrast, images without descriptions and a checkout you can’t complete from the keyboard does exactly the same thing — you just can’t see it. The law requires that digital services sold to consumers be usable by people with a visual, motor or cognitive disability too.'},
    'In Italia la direttiva è stata recepita e si applica dal 28 giugno 2025. Lo standard di riferimento non è un’opinione: sono le WCAG 2.1 di livello AA, le stesse linee guida internazionali che i tecnici usano da anni. Non è una moda partita ieri, è un percorso cominciato nel 2019 e arrivato a scadenza adesso.':
        {'en': 'In Italy the directive has been transposed and applies from 28 June 2025. The reference standard isn’t a matter of opinion: it’s WCAG 2.1 level AA, the same international guidelines developers have used for years. This isn’t a fad that started yesterday — it’s a path that began in 2019 and has just reached its deadline.'},
    'Cronologia dell’European Accessibility Act: direttiva UE 2019/882, recepimento in Italia, entrata in vigore il 28 giugno 2025 e sanzione massima del 5%':
        {'en': 'Timeline of the European Accessibility Act: EU Directive 2019/882, transposition in Italy, entry into force on 28 June 2025, and a maximum fine of 5%'},
    'Dalla direttiva UE 2019/882 all’entrata in vigore in Italia il 28 giugno 2025. Le microimprese di servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato — hanno un’esenzione. Fonti: AccessibleEU (Commissione europea) e la guida di Bird & Bird.':
        {'en': 'From EU Directive 2019/882 to entry into force in Italy on 28 June 2025. Service micro-enterprises — fewer than 10 people and under € 2M in revenue — are exempt. Sources: AccessibleEU (European Commission) and the Bird & Bird guide.'},
    'Cosa rischia davvero il vostro e-commerce con l’European Accessibility Act':
        {'en': 'What your e-commerce site really risks under the European Accessibility Act'},
    'Partiamo dai soldi, perché è la domanda vera. Il recepimento italiano prevede sanzioni fino al 5% del fatturato per i servizi non conformi: su un negozio che fattura 800.000 euro l’anno sono fino a 40.000 euro, più di quanto costi rifare il sito da zero. Non è un rischio teorico. In Francia, dove l’applicazione è partita prima, le prime cause verso i grandi rivenditori online sono già arrivate; in Italia la vigilanza è appena cominciata, e le prime segnalazioni sono una questione di mesi, non di anni.':
        {'en': 'Let’s start with the money, because that’s the real question. The Italian transposition provides for fines of up to 5% of revenue for non-compliant services: for a store turning over € 800,000 a year that’s up to € 40,000 — more than rebuilding the site from scratch would cost. This isn’t a theoretical risk. In France, where enforcement started earlier, the first cases against large online retailers have already landed; in Italy oversight has only just begun, and the first complaints are a matter of months, not years.'},
    'Ma la sanzione è la parte che spaventa di più, non quella che pesa di più. Un e-commerce inaccessibile perde clienti ogni giorno, in silenzio, molto prima che arrivi un controllo. Pensate a chi ci vede poco e non riesce a leggere un grigio chiaro elegante, a chi naviga da telefono con una mano sola, a chi compila l’ordine da tastiera perché il mouse gli è scomodo: ogni barriera è un carrello abbandonato che nei vostri report non comparirà mai come «problema di accessibilità». Lo leggerete come «tasso di conversione basso», e darete la colpa al prezzo.':
        {'en': 'But the fine is the part that scares you most, not the part that costs you most. An inaccessible e-commerce site loses customers every day, quietly, long before any inspection. Think of the person who sees poorly and can’t read an elegant light gray, the one browsing one-handed on a phone, the one filling in the order from the keyboard because the mouse is awkward for them: every barrier is an abandoned cart that will never show up in your reports as an “accessibility problem.” You’ll read it as a “low conversion rate,” and you’ll blame the price.'},
    'Siete obbligati? La regola delle microimprese':
        {'en': 'Are you covered? The micro-enterprise rule'},
    'La domanda che ci fanno tutti è «vale anche per me?». La risposta onesta è «quasi sempre sì, ma verificate». La norma guarda a chi vende beni o servizi ai consumatori a distanza. Esiste però un’esenzione per le microimprese che erogano servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato annuo. L’esenzione è pensata per i servizi e il perimetro esatto va guardato caso per caso, non a occhio: nel dubbio, meglio una verifica di mezz’ora che una sanzione.':
        {'en': 'Everyone asks us the same thing: “does this apply to me too?” The honest answer is “almost always yes, but check.” The law looks at anyone selling goods or services to consumers at a distance. There is, however, an exemption for service micro-enterprises — fewer than 10 people and under € 2 million in annual revenue. The exemption is built for services, and the exact scope has to be looked at case by case, not by gut feeling: when in doubt, a half-hour check beats a fine.'},
    'E-commerce e servizi digitali che vendono a consumatori nell’Unione Europea: è il caso più comune, e il più esposto.':
        {'en': 'E-commerce and digital services selling to consumers in the European Union: the most common case, and the most exposed.'},
    'Banche, assicurazioni, trasporti, biglietterie e sistemi di prenotazione online.':
        {'en': 'Banks, insurers, transport, ticketing and online booking systems.'},
    'Aziende che non sono microimprese e che finora hanno trattato l’accessibilità come un dettaglio estetico.':
        {'en': 'Companies that aren’t micro-enterprises and have treated accessibility as a cosmetic detail until now.'},
    'Verifica gratis le barriere del vostro sito →':
        {'en': 'Check your site’s barriers for free →'},
    'Da dove si comincia: le quattro parole che contano':
        {'en': 'Where to start: the four words that matter'},
    'Le WCAG 2.1 AA sembrano un muro di sigle, ma poggiano su quattro princìpi semplici, riassunti nell’acronimo POUR: un sito accessibile è percepibile, utilizzabile, comprensibile e robusto. Tradotto in pratica: testo che si legge anche con poca vista, tutto raggiungibile da tastiera, moduli con etichette chiare e messaggi d’errore che spiegano cosa fare, codice pulito che gli screen reader sanno leggere.':
        {'en': 'WCAG 2.1 AA looks like a wall of acronyms, but it rests on four simple principles, summed up as POUR: an accessible site is perceivable, operable, understandable and robust. In practice: text you can read even with poor eyesight, everything reachable from the keyboard, forms with clear labels and error messages that explain what to do, and clean code that screen readers can read.'},
    'I quattro princìpi delle WCAG 2.1 AA: percepibile, utilizzabile, comprensibile, robusto':
        {'en': 'The four principles of WCAG 2.1 AA: perceivable, operable, understandable, robust'},
    'I quattro princìpi delle WCAG 2.1 AA (POUR). Un audit automatico intercetta circa un terzo di questi criteri; il resto — tastiera, screen reader, contenuti — si verifica a mano.':
        {'en': 'The four principles of WCAG 2.1 AA (POUR). An automated audit catches about a third of these criteria; the rest — keyboard, screen reader, content — is checked by hand.'},
    'Tre settimane, dall’audit alla dichiarazione':
        {'en': 'Three weeks, from audit to statement'},
    'Un controllo automatico gratuito è il primo gradino: in un minuto vi dice se il sito ha già i problemi più evidenti — contrasti, etichette, struttura. Ma la conformità piena non si certifica con un punteggio: serve la verifica manuale (tastiera, screen reader, contenuti) e una dichiarazione di accessibilità pubblicata sul sito, il documento che la norma pretende. Senza dichiarazione, un sito tecnicamente accessibile resta comunque non a norma.':
        {'en': 'A free automated check is the first step: in a minute it tells you whether the site already has the most obvious problems — contrast, labels, structure. But full compliance isn’t certified by a score: it takes a manual review (keyboard, screen reader, content) and an accessibility statement published on the site, the document the law requires. Without the statement, a technically accessible site is still not compliant.'},
    'La buona notizia è che non è un lavoro infinito. Per un e-commerce di taglia media, dall’audit alle correzioni fino alla dichiarazione, sono in genere tre settimane. L’obbligo, preso per tempo, non è un costo a fondo perduto: è un sito che vende a più persone e che non teme la prima lettera del controllo.':
        {'en': 'The good news is that it isn’t an endless job. For a mid-sized e-commerce site, from audit to fixes to statement it’s usually three weeks. Taken in time, the obligation isn’t money down the drain: it’s a site that sells to more people and doesn’t fear the first enforcement letter.'},
    'Vogliamo sistemarlo noi: il servizio Adeguamento EAA, a prezzo chiuso →':
        {'en': 'Want us to fix it? The EAA compliance service, at a fixed price →'},
    'Adeguamento EAA: audit, correzioni e dichiarazione in 3 settimane →':
        {'en': 'EAA compliance: audit, fixes and statement in 3 weeks →'},

    # ---------- Articolo 2 — llms.txt ----------
    'llms.txt: cos’è e serve davvero al vostro sito?':
        {'en': 'llms.txt: what it is, and does your site actually need it?'},
    'Un file di testo che spiega il vostro sito ai modelli AI, come robots.txt fa con Google. Cos’è, come si scrive e quanto conta davvero, senza esagerazioni.':
        {'en': 'A text file that explains your site to AI models, the way robots.txt does for Google. What it is, how to write it, and how much it really matters — no hype.'},
    'llms.txt: cos’è, il file Markdown nella radice del sito che riassume i contenuti per i modelli AI':
        {'en': 'llms.txt: what it is — the Markdown file in the site root that summarizes your content for AI models'},
    'Nel giro di un anno è comparso un nuovo file di cui tutti parlano e che quasi nessuno ha: llms.txt. La promessa è semplice — un foglietto di istruzioni che spiega il vostro sito ai modelli di intelligenza artificiale, come robots.txt fa da vent’anni con i motori di ricerca. Ma serve davvero, o è l’ennesima sigla che qualcuno vi venderà a caro prezzo? Vediamo cos’è llms.txt, come si scrive in mezz’ora e quanto conta oggi, senza gonfiarne l’importanza e senza liquidarlo con un’alzata di spalle.':
        {'en': 'Within a year a new file everyone talks about and almost nobody has appeared: llms.txt. The promise is simple — a little instruction sheet that explains your site to AI models, the way robots.txt has done for search engines for twenty years. But does it actually help, or is it just one more acronym someone will sell you at a premium? Let’s look at what llms.txt is, how to write it in half an hour, and how much it matters today — without inflating it and without waving it off.'},
    'llms.txt, cos’è in una frase':
        {'en': 'llms.txt, in one sentence'},
    'llms.txt è un file di testo in formato Markdown che mettete nella radice del sito (sito.it/llms.txt) e che riassume, in modo leggibile da una macchina, chi siete, cosa fate e dove trovare le pagine importanti. Nasce come proposta di standard nel 2024 e ha un obiettivo preciso: dare ai modelli linguistici — quelli dietro ChatGPT, Claude, Perplexity — una mappa pulita del sito, senza costringerli a indovinare tra menù, banner e codice.':
        {'en': 'llms.txt is a Markdown text file you place in your site root (yoursite.com/llms.txt) that summarizes, in a machine-readable way, who you are, what you do, and where to find the important pages. It emerged as a proposed standard in 2024 with a clear goal: to give language models — the ones behind ChatGPT, Claude, Perplexity — a clean map of the site, without forcing them to guess among menus, banners and code.'},
    'L’analogia con robots.txt aiuta, ma non è perfetta. robots.txt dice ai crawler dove possono andare; llms.txt dice loro cosa contano le vostre pagine e come raccontarvi. È la differenza tra un cartello «vietato l’ingresso» e una guida che spiega il museo.':
        {'en': 'The robots.txt analogy helps, but it isn’t perfect. robots.txt tells crawlers where they may go; llms.txt tells them what your pages are about and how to describe you. It’s the difference between a “no entry” sign and a guide that explains the museum.'},
    'Come è fatto un file llms.txt':
        {'en': 'What an llms.txt file looks like'},
    'La parte bella è che si legge e si scrive senza essere programmatori. La struttura è quella di un documento Markdown ordinato: un titolo con il nome dell’azienda, una riga di sintesi, e poi sezioni con link alle pagine che volete far leggere per prime — servizi, chi siamo, contatti, documentazione.':
        {'en': 'The nice part is that you can read and write it without being a programmer. The structure is that of a tidy Markdown document: a title with the company name, a one-line summary, then sections with links to the pages you want read first — services, about, contacts, documentation.'},
    'Anatomia di un file llms.txt: titolo H1 obbligatorio, una riga di sintesi, sezioni con link e un blocco opzionale':
        {'en': 'Anatomy of an llms.txt file: a required H1 title, a one-line summary, sections with links, and an optional block'},
    'L’anatomia di un file llms.txt: un titolo (1, obbligatorio), una sintesi in una riga (2), le sezioni con i link alle pagine chiave (3) e un blocco opzionale per il resto (4). Nient’altro: la forza sta nella sobrietà.':
        {'en': 'The anatomy of an llms.txt file: a title (1, required), a one-line summary (2), sections with links to the key pages (3), and an optional block for the rest (4). Nothing more — its strength is in the restraint.'},
    'Serve davvero? La risposta onesta':
        {'en': 'Does it actually help? The honest answer'},
    'Qui evitiamo due bugie speculari. La prima: «llms.txt è indispensabile, senza sei invisibile». Falso. È uno standard giovane, non tutti i modelli lo leggono ancora, e la sua assenza oggi non è un errore grave. La seconda: «è una moda inutile». Anche questa è falsa. Costa mezz’ora, non fa danni, e vi mette dalla parte giusta di un cambiamento che sta accelerando.':
        {'en': 'Here we steer clear of two mirror-image lies. The first: “llms.txt is essential, without it you’re invisible.” False. It’s a young standard, not every model reads it yet, and its absence today isn’t a serious error. The second: “it’s a pointless fad.” Also false. It costs half an hour, does no harm, and puts you on the right side of a change that’s speeding up.'},
    'Il modo giusto di leggerlo è questo: llms.txt non vi porta clienti da solo, ma toglie ambiguità. Se un modello prova a raccontare cosa fate, preferite che legga una mappa scritta da voi o che ricostruisca tutto da un menù e da tre banner cookie? La risposta è ovvia, e il costo dell’assicurazione è ridicolo rispetto al rischio di essere descritti male.':
        {'en': 'Here’s the right way to read it: llms.txt won’t bring you customers on its own, but it removes ambiguity. If a model tries to describe what you do, would you rather it read a map you wrote or piece everything together from a menu and three cookie banners? The answer is obvious, and the cost of the insurance is trivial next to the risk of being described badly.'},
    'llms.txt è un pezzo, non tutta la SEO tecnica':
        {'en': 'llms.txt is one piece, not the whole of technical SEO'},
    'Un errore comune è trattare llms.txt come una bacchetta magica. In realtà è l’ultimo arrivato in una famiglia di segnali che esistono da tempo: dati strutturati in JSON-LD, una sitemap aggiornata, contenuti in testo leggibile e non solo in immagini, un robots.txt che non chiude la porta ai crawler giusti. llms.txt è la ciliegina; la torta è la SEO tecnica fatta bene.':
        {'en': 'A common mistake is treating llms.txt as a magic wand. In reality it’s the newest arrival in a family of signals that have been around for a while: JSON-LD structured data, an up-to-date sitemap, content in readable text rather than only in images, and a robots.txt that doesn’t shut the door on the right crawlers. llms.txt is the cherry; the cake is technical SEO done well.'},
    'Se non sapete da dove cominciare, cominciate misurando. In un minuto potete verificare se il vostro sito espone già i quattro segnali che i modelli cercano — file llms.txt, accesso dei crawler AI, dati strutturati e sitemap — e capire cosa manca prima di scrivere una sola riga.':
        {'en': 'If you don’t know where to begin, begin by measuring. In a minute you can check whether your site already exposes the four signals models look for — an llms.txt file, AI-crawler access, structured data and a sitemap — and see what’s missing before you write a single line.'},
    'Fa parte della SEO tecnica che consegniamo →':
        {'en': 'It’s part of the technical SEO we deliver →'},
    'Leggi anche: come farsi trovare e citare da ChatGPT →':
        {'en': 'Read also: how to get found and cited by ChatGPT →'},
    'Verifica gratis se il vostro sito è pronto per l’AI →':
        {'en': 'Check for free whether your site is AI-ready →'},

    # ---------- Articolo 3 — GEO / ChatGPT ----------
    'Come farsi trovare (e citare) da ChatGPT: guida alla GEO':
        {'en': 'How to get found (and cited) by ChatGPT: a GEO guide'},
    'Sempre più persone chiedono a ChatGPT invece che a Google. La GEO è l’arte di farsi citare nelle risposte generate: cosa cambia rispetto alla SEO e cosa fare.':
        {'en': 'More and more people ask ChatGPT instead of Google. GEO is the craft of getting cited in generated answers: what changes from SEO, and what to do about it.'},
    'Sito visibile su ChatGPT: la GEO (Generative Engine Optimization) e una risposta AI che cita la vostra pagina come fonte':
        {'en': 'A site visible on ChatGPT: GEO (Generative Engine Optimization) and an AI answer that cites your page as a source'},
    'C’è una domanda che un anno fa era da nerd e oggi la fa anche vostro cugino: «l’hai chiesto a ChatGPT?». Sempre più persone cercano una risposta parlando con un assistente AI invece di sfogliare dieci link blu, e questo apre una partita nuova: non basta più essere primi su Google, bisogna essere citati nelle risposte generate. Farsi trovare su ChatGPT, Perplexity e simili ha persino un nome — GEO, Generative Engine Optimization. Vediamo cos’è, in cosa somiglia alla SEO e in cosa se ne allontana, e soprattutto cosa potete fare concretamente.':
        {'en': 'There’s a question that a year ago was for nerds and today even your cousin asks: “did you ask ChatGPT?” More and more people look for an answer by talking to an AI assistant instead of scrolling ten blue links, and that opens a new game: being first on Google is no longer enough — you have to be cited in the generated answers. Getting found on ChatGPT, Perplexity and the like even has a name: GEO, Generative Engine Optimization. Let’s look at what it is, where it resembles SEO and where it parts ways, and above all what you can concretely do.'},
    'Perché volete un sito visibile su ChatGPT':
        {'en': 'Why you want a site visible on ChatGPT'},
    'Quando un modello AI risponde a una domanda, spesso non inventa: legge il web e sintetizza, e nelle risposte migliori indica le fonti con dei rimandi cliccabili. Essere una di quelle fonti significa due cose. La prima, immediata: qualcuno vi legge nel momento esatto in cui sta decidendo. La seconda, più sottile: comparire in una risposta di ChatGPT o Perplexity è un segnale di autorevolezza che si trascina dietro fiducia, anche offline.':
        {'en': 'When an AI model answers a question, it often isn’t making things up: it reads the web and synthesizes, and in the best answers it points to sources with clickable references. Being one of those sources means two things. The first, immediate: someone reads you at the exact moment they’re deciding. The second, subtler: appearing in a ChatGPT or Perplexity answer is a signal of authority that carries trust with it, offline too.'},
    'L’errore da evitare è pensare che sia una moda passeggera o roba «da grandi marchi». Il meccanismo premia chi si spiega bene, non chi ha il budget più grosso — ed è esattamente il terreno su cui una PMI ben fatta può battere un concorrente più grande e più pigro.':
        {'en': 'The mistake to avoid is thinking it’s a passing fad or something “for big brands.” The mechanism rewards whoever explains themselves clearly, not whoever has the biggest budget — and that’s exactly the ground on which a well-run small business can beat a bigger, lazier competitor.'},
    'Come un modello arriva a citare la vostra pagina':
        {'en': 'How a model ends up citing your page'},
    'Il percorso è più semplice di quanto sembri, e capirlo aiuta a lavorarci. Il vostro sito viene letto da crawler specializzati — GPTBot di OpenAI, ClaudeBot, PerplexityBot; questi contenuti alimentano il modello; e quando qualcuno fa una domanda pertinente, il modello costruisce la risposta e, se il vostro testo è chiaro e affidabile, vi cita come fonte.':
        {'en': 'The path is simpler than it looks, and understanding it helps you work on it. Your site is read by specialized crawlers — OpenAI’s GPTBot, ClaudeBot, PerplexityBot; that content feeds the model; and when someone asks a relevant question, the model builds the answer and, if your text is clear and trustworthy, cites you as a source.'},
    'Il flusso della GEO: dal vostro sito ai crawler AI (GPTBot, ClaudeBot, PerplexityBot), al modello, fino alla risposta con la citazione':
        {'en': 'The GEO flow: from your site to the AI crawlers (GPTBot, ClaudeBot, PerplexityBot), to the model, to the answer with the citation'},
    'Il percorso, in quattro passi: il vostro sito (1) viene letto dai crawler AI (2), alimenta il modello (3) e, se il contenuto è chiaro, finisce citato nella risposta (4). Ogni passo ha un modo per andare storto — o per funzionare.':
        {'en': 'The path, in four steps: your site (1) is read by AI crawlers (2), feeds the model (3) and, if the content is clear, ends up cited in the answer (4). Every step has a way to go wrong — or to work.'},
    'GEO e SEO: cosa cambia (e cosa no)':
        {'en': 'GEO and SEO: what changes (and what doesn’t)'},
    'Buona parte del lavoro è la stessa di sempre: contenuti chiari, struttura tecnica pulita, velocità, dati strutturati. Chi ha già una SEO tecnica solida parte con mezzo lavoro fatto. Ma tre cose diventano più importanti del solito.':
        {'en': 'Much of the work is the same as always: clear content, a clean technical structure, speed, structured data. Anyone with solid technical SEO already starts half done. But three things become more important than usual.'},
    'Aprire la porta ai crawler giusti: nel robots.txt non bloccate GPTBot, ClaudeBot, PerplexityBot e Google-Extended se volete comparire nelle risposte generate.':
        {'en': 'Open the door to the right crawlers: in robots.txt, don’t block GPTBot, ClaudeBot, PerplexityBot and Google-Extended if you want to appear in generated answers.'},
    'Scrivere fatti espliciti: i modelli citano ciò che capiscono senza ambiguità. «Realizziamo e-commerce a Milano, consegna in 6 settimane, prezzo chiuso» vale più di «soluzioni digitali su misura per il vostro business».':
        {'en': 'Write explicit facts: models cite what they understand without ambiguity. “We build e-commerce sites in Milan, delivery in 6 weeks, fixed price” is worth more than “tailored digital solutions for your business.”'},
    'Farsi leggere in testo, non in immagini: un dato prezioso dentro una locandina JPG, per un modello, non esiste.':
        {'en': 'Be readable as text, not as images: a valuable fact inside a JPG poster, to a model, simply doesn’t exist.'},
    'Da dove partire, senza perdersi':
        {'en': 'Where to start, without getting lost'},
    'La GEO non è un servizio a parte da comprare in fretta: è la buona SEO tecnica di sempre, orientata a un lettore nuovo. Il primo passo concreto è verificare se il vostro sito è già leggibile dalle macchine — se espone i dati strutturati, se non sta bloccando i crawler AI, se ha una sitemap in ordine. Da lì si vede subito cosa manca.':
        {'en': 'GEO isn’t a separate service to buy in a hurry: it’s the same good technical SEO as always, aimed at a new kind of reader. The first concrete step is to check whether your site is already machine-readable — whether it exposes structured data, whether it’s blocking the AI crawlers, whether its sitemap is in order. From there you see at once what’s missing.'},
    'E se volete capire il tassello più discusso di questo mondo — il famoso file llms.txt — l’abbiamo raccontato a parte, senza fumo: cos’è, come si scrive e quanto conta davvero.':
        {'en': 'And if you want to understand the most talked-about piece of this world — the famous llms.txt file — we’ve covered it separately, no smoke: what it is, how to write it, and how much it really matters.'},
    'Lo prepariamo noi: fa parte della SEO tecnica →':
        {'en': 'We set it up: it’s part of technical SEO →'},
    'Leggi anche: llms.txt, cos’è e serve davvero al vostro sito →':
        {'en': 'Read also: llms.txt, what it is and whether your site needs it →'},
    'Verifica gratis se il vostro sito è leggibile dai modelli AI →':
        {'en': 'Check for free whether AI models can read your site →'},

    # ---------- Articolo 4 — Check-up ----------
    'Check-up del sito web: le 7 misure che contano':
        {'en': 'Website check-up: the 7 metrics that matter'},
    'Un sito «va bene» o «va male» non si decide a sensazione. Ci sono sette misure che ne raccontano la salute — e un modo per leggerle in un minuto, gratis.':
        {'en': 'Whether a site is “doing well” or “doing badly” isn’t decided by gut feeling. There are seven metrics that tell its health — and a way to read them in a minute, for free.'},
    'Check-up del sito web: sette misure in un solo punteggio di salute da 0 a 100':
        {'en': 'Website check-up: seven metrics in a single health score from 0 to 100'},
    '«Secondo voi il nostro sito è messo bene?» È la domanda con cui inizia metà delle nostre chiamate, e la risposta seria non è «sì» o «no»: è «dipende da cosa misurate». Un sito bellissimo può essere lentissimo; uno velocissimo può essere invisibile a Google; uno perfetto per Google può respingere una persona su dieci per un problema di accessibilità. Fare il check-up di un sito web significa guardarlo su più fronti insieme, con dei numeri, non a occhio. Ecco le sette misure che contano davvero, e come leggerle senza diventare tecnici.':
        {'en': '“Do you think our site is in good shape?” It’s the question half our calls start with, and the serious answer isn’t “yes” or “no”: it’s “depends what you measure.” A beautiful site can be painfully slow; a lightning-fast one can be invisible to Google; one that’s perfect for Google can turn away one person in ten over an accessibility problem. Running a website check-up means looking at it on several fronts at once, with numbers, not by eye. Here are the seven metrics that really matter, and how to read them without becoming a technician.'},
    'Perché un solo numero non basta (e sette sì)':
        {'en': 'Why a single number isn’t enough (and seven are)'},
    'Il voto unico rassicura, ma inganna. «PageSpeed 92» dice qualcosa sulla velocità e niente su privacy, accessibilità o prontezza AI. Per questo un check-up serio non guarda una cosa sola: mette in fila sette dimensioni e le pesa, così vedete in un colpo d’occhio dove il sito è solido e dove perde punti — e quali problemi valgono la pena di sistemare per primi.':
        {'en': 'A single score reassures, but it misleads. “PageSpeed 92” says something about speed and nothing about privacy, accessibility or AI readiness. That’s why a serious check-up doesn’t look at one thing: it lines up seven dimensions and weights them, so you see at a glance where the site is solid and where it loses points — and which problems are worth fixing first.'},
    'Le sette misure del check-up — prestazioni, SEO, accessibilità, best practice, privacy, prontezza AI, CO₂ — e le fasce di punteggio di salute':
        {'en': 'The seven check-up metrics — performance, SEO, accessibility, best practices, privacy, AI readiness, CO₂ — and the health-score bands'},
    'Le sette misure e le fasce del punteggio di salute (0–49 critico, 50–74 con margine, 75–89 buono, 90+ eccellente). Quattro dimensioni arrivano dall’API Google PageSpeed; tre — privacy, prontezza AI e CO₂ — sono verifiche nostre. Le prestazioni pesano di più (25), la CO₂ di meno (5).':
        {'en': 'The seven metrics and the health-score bands (0–49 critical, 50–74 room to improve, 75–89 good, 90+ excellent). Four dimensions come from the Google PageSpeed API; three — privacy, AI readiness and CO₂ — are our own checks. Performance weighs the most (25), CO₂ the least (5).'},
    'Le quattro misure che arrivano da Google':
        {'en': 'The four metrics that come from Google'},
    'Quattro delle sette misure non sono una nostra opinione: arrivano dall’API di Google PageSpeed, la stessa che alimenta pagespeed.web.dev, interrogata in versione mobile perché è quella con cui Google vi posiziona.':
        {'en': 'Four of the seven metrics aren’t our opinion: they come from the Google PageSpeed API, the same one that powers pagespeed.web.dev, queried in mobile mode because that’s the version Google ranks you by.'},
    'Prestazioni: quanto in fretta la pagina diventa utilizzabile su un telefono. È la voce che pesa di più, ed è quella che decide se le visite restano o scappano.':
        {'en': 'Performance: how fast the page becomes usable on a phone. It’s the metric that weighs the most, and the one that decides whether visits stay or bolt.'},
    'SEO tecnica: se titoli, struttura e dati mancanti mettono i bastoni tra le ruote all’indicizzazione.':
        {'en': 'Technical SEO: whether titles, structure and missing data are getting in the way of indexing.'},
    'Accessibilità: contrasti, etichette, struttura dei titoli — le barriere che dal 2025 sono anche un obbligo di legge.':
        {'en': 'Accessibility: contrast, labels, heading structure — the barriers that since 2025 are also a legal requirement.'},
    'Best practice: uso corretto di HTTPS, immagini, console pulita e piccoli segnali di igiene tecnica.':
        {'en': 'Best practices: correct use of HTTPS, images, a clean console and the small signs of technical hygiene.'},
    'Le tre misure che aggiungiamo noi':
        {'en': 'The three metrics we add ourselves'},
    'Le altre tre le calcoliamo direttamente, leggendo il sito come farebbe un visitatore. La conformità privacy la ricaviamo dall’HTML (banner, informative, tracker prima del consenso); la prontezza AI da quattro segnali — llms.txt, accesso dei crawler AI, dati strutturati, sitemap; l’impronta di CO₂ dal peso reale della pagina, con il modello Sustainable Web Design. Sono verifiche indicative, e lo diciamo: il check-up privacy non è un parere legale, e il punteggio non promette una posizione su Google. È una fotografia tecnica precisa, non una promessa di vendita.':
        {'en': 'The other three we calculate directly, reading the site as a visitor would. Privacy compliance we read from the HTML (banner, notices, trackers firing before consent); AI readiness from four signals — llms.txt, AI-crawler access, structured data, sitemap; the CO₂ footprint from the page’s real weight, using the Sustainable Web Design model. These are indicative checks, and we say so: the privacy check isn’t legal advice, and the score doesn’t promise a position on Google. It’s a precise technical snapshot, not a sales promise.'},
    'Come si legge il voto di salute':
        {'en': 'How to read the health score'},
    'Il punteggio di salute è la media pesata delle sette misure, e si legge come un semaforo: da 90 in su siete in fascia verde, tra 75 e 89 è buono, tra 50 e 74 c’è margine concreto, sotto 50 è critico e diventa la priorità. Due avvertenze: un voto alto non significa «primi su Google» — significa fondamenta tecniche sane; e se una misura risulta «N/D», di solito non è un guasto vostro, ma un server saturo o una lettura automatica rifiutata.':
        {'en': 'The health score is the weighted average of the seven metrics, and it reads like a traffic light: 90 and up you’re in the green band, 75 to 89 is good, 50 to 74 there’s real room to improve, below 50 is critical and becomes the priority. Two caveats: a high score doesn’t mean “first on Google” — it means sound technical foundations; and if a metric comes back “N/A,” it’s usually not a fault on your side, but a saturated server or an automated read that was refused.'},
    'La cosa migliore è che tutto questo lo potete misurare da soli, gratis e in meno di un minuto, incollando l’indirizzo del sito. Il report completo, pagina per pagina, arriva in PDF; e se dal check-up esce che vale la pena rifare la base tecnica, il restyling parte da lì — dai numeri, non dalle sensazioni.':
        {'en': 'The best part is that you can measure all this yourself, free and in under a minute, by pasting in the site’s address. The full report, page by page, comes as a PDF; and if the check-up shows the technical foundation is worth rebuilding, the redesign starts there — from the numbers, not from a hunch.'},
    'Fai il check-up completo, gratis e senza registrazione →':
        {'en': 'Run the full check-up, free and with no sign-up →'},
    'Se serve rifare la base: restyling e migrazione →':
        {'en': 'If the foundation needs rebuilding: redesign and migration →'},
    'Fai ora il check-up completo del tuo sito — gratis →':
        {'en': 'Run your site’s full check-up now — free →'},

    # ---------- Articolo 5 — E-E-A-T ----------
    'E-E-A-T: come Google giudica la vostra credibilità':
        {'en': 'E-E-A-T: how Google judges your credibility'},
    'Esperienza, competenza, autorevolezza, affidabilità: la cornice con cui Google valuta di chi fidarsi. Cos’è l’E-E-A-T e come rafforzarla, senza trucchi.':
        {'en': 'Experience, expertise, authoritativeness, trust: the framework Google uses to judge who to rely on. What E-E-A-T is and how to strengthen it, no tricks.'},
    'E-E-A-T cos’è: esperienza, competenza, autorevolezza e affidabilità, i quattro pilastri delle Search Quality Rater Guidelines di Google':
        {'en': 'What E-E-A-T is: experience, expertise, authoritativeness and trust — the four pillars of Google’s Search Quality Rater Guidelines'},
    'Se avete letto qualcosa di SEO nell’ultimo anno vi sarà rimbalzato addosso un acronimo dall’aria misteriosa: E-E-A-T. Suona come una password, ed è invece il modo in cui Google prova a rispondere a una domanda molto umana: di questo sito, ci si può fidare? Non è un punteggio segreto e non si compra. È una cornice fatta di quattro parole — esperienza, competenza, autorevolezza, affidabilità — che vale la pena capire, perché tocca da vicino chiunque venda servizi o consigli online. Vediamo cos’è l’E-E-A-T e, soprattutto, cosa potete fare per rafforzarla senza scorciatoie.':
        {'en': 'If you’ve read anything about SEO in the past year, a mysterious-looking acronym has probably bounced off you: E-E-A-T. It sounds like a password, and it’s actually the way Google tries to answer a very human question: can this site be trusted? It’s not a secret score and it can’t be bought. It’s a framework made of four words — experience, expertise, authoritativeness, trust — worth understanding, because it directly affects anyone who sells services or advice online. Let’s look at what E-E-A-T is and, above all, what you can do to strengthen it without shortcuts.'},
    'E-E-A-T, cos’è (e cosa non è)':
        {'en': 'E-E-A-T, what it is (and what it isn’t)'},
    'E-E-A-T sta per Experience, Expertise, Authoritativeness, Trust: esperienza, competenza, autorevolezza e affidabilità. Non è un’invenzione dei SEO: è scritto nero su bianco nelle Search Quality Rater Guidelines, il manuale con cui Google istruisce le persone in carne e ossa che valutano la qualità dei risultati. Serve a stimare quanto ci si può fidare di una pagina, soprattutto sui temi che incidono su salute, denaro e sicurezza.':
        {'en': 'E-E-A-T stands for Experience, Expertise, Authoritativeness, Trust. It isn’t an invention of the SEO crowd: it’s written in black and white in the Search Quality Rater Guidelines, the manual Google uses to instruct the flesh-and-blood people who assess the quality of its results. It’s there to estimate how far a page can be trusted, especially on topics that affect health, money and safety.'},
    'Attenzione a un equivoco diffuso: l’E-E-A-T non è un fattore di ranking diretto, né un numero che Google vi assegna. È una cornice di qualità che i valutatori umani usano per addestrare gli algoritmi. Rafforzare i segnali di fiducia aiuta indirettamente; ma nessuno strumento — nemmeno il nostro — misura l’E-E-A-T «reale» del vostro sito. Diffidate di chi ve lo promette.':
        {'en': 'Beware a widespread misunderstanding: E-E-A-T is not a direct ranking factor, nor a number Google assigns you. It’s a quality framework the human raters use to train the algorithms. Strengthening trust signals helps indirectly; but no tool — not even ours — measures your site’s “real” E-E-A-T. Be wary of anyone who promises it.'},
    'I quattro pilastri, con Trust al centro':
        {'en': 'The four pillars, with Trust at the center'},
    'Le quattro parole non pesano tutte uguale. Nelle linee guida di Google il pilastro centrale è la fiducia (Trust): esperienza, competenza e autorevolezza servono soprattutto a sostenerla. Ha senso: un contenuto può essere scritto da un vero esperto, ma se il sito non è sicuro o non si capisce chi c’è dietro, la fiducia crolla lo stesso.':
        {'en': 'The four words don’t all carry equal weight. In Google’s guidelines the central pillar is Trust: experience, expertise and authoritativeness mostly serve to support it. It makes sense: content can be written by a genuine expert, but if the site isn’t secure or it’s unclear who’s behind it, trust collapses anyway.'},
    'I quattro pilastri E-E-A-T — esperienza, competenza, autorevolezza, affidabilità — con gli otto segnali di fiducia leggibili nel codice della pagina':
        {'en': 'The four E-E-A-T pillars — experience, expertise, authoritativeness, trust — with the eight trust signals readable in the page code'},
    'I quattro pilastri E-E-A-T e alcuni segnali concreti che vi finiscono dentro: portfolio e casi studio, pagina «chi siamo», dati strutturati e profili esterni, HTTPS, contatti, P.IVA, privacy. La fiducia (Trust) è il pilastro centrale.':
        {'en': 'The four E-E-A-T pillars and some concrete signals that fall under them: portfolio and case studies, an “about” page, structured data and external profiles, HTTPS, contacts, VAT number, privacy. Trust is the central pillar.'},
    'I segnali che potete davvero controllare':
        {'en': 'The signals you can actually control'},
    'La parte buona dell’E-E-A-T è che una fetta è alla vostra portata, subito. Google e i lettori cercano, nella pagina, dei segnali di fiducia leggibili: una connessione sicura in HTTPS, contatti verificabili, l’identità legale (P.IVA e ragione sociale), i link a privacy e cookie policy, una pagina «chi siamo» vera con nomi e volti, un portfolio o dei casi studio, i dati strutturati in JSON-LD e i profili esterni. Sono aggiunte tecniche precise, quasi tutte veloci e a basso costo.':
        {'en': 'The good part of E-E-A-T is that a slice of it is within your reach right away. Google and readers look, on the page, for readable trust signals: a secure HTTPS connection, verifiable contacts, legal identity (VAT number and registered name), links to privacy and cookie policies, a real “about” page with names and faces, a portfolio or case studies, JSON-LD structured data and external profiles. These are precise technical additions, almost all of them quick and low-cost.'},
    'Quello che nessuna scorciatoia vi darà è l’altra metà: la reputazione, le menzioni, la qualità reale dei contenuti, l’esperienza vissuta di chi scrive. Quella si costruisce con il tempo — ed è esattamente perché non si può falsificare che Google le dà tanto peso.':
        {'en': 'What no shortcut will give you is the other half: reputation, mentions, the real quality of the content, the lived experience of whoever writes it. That’s built over time — and it’s precisely because it can’t be faked that Google gives it so much weight.'},
    'Da dove partire: misurare, poi sistemare':
        {'en': 'Where to start: measure, then fix'},
    'Il modo più rapido per capire come siete messi non è leggere altra teoria, ma guardare cosa espone davvero la vostra home. In un minuto potete misurare gli otto segnali di fiducia leggibili nel codice e vedere su quale dei quattro pilastri conviene intervenire per primo. Da lì, un pomeriggio di lavoro tecnico — una pagina «chi siamo» vera, i contatti nel footer, un blocco di dati strutturati — sposta il punteggio più di quanto immaginate.':
        {'en': 'The fastest way to see where you stand isn’t to read more theory, but to look at what your homepage actually exposes. In a minute you can measure the eight trust signals readable in the code and see which of the four pillars is worth tackling first. From there, an afternoon of technical work — a real “about” page, contacts in the footer, a block of structured data — moves the score more than you’d expect.'},
    'E ricordate la regola che vale per tutto l’E-E-A-T: un sito può dichiarare bene chi è, ma la fiducia vera la costruiscono i contenuti, il tempo e le persone. Gli strumenti misurano i segnali; la credibilità la meritate voi.':
        {'en': 'And remember the rule that holds for all of E-E-A-T: a site can state well who it is, but real trust is built by content, time and people. Tools measure the signals; the credibility, you earn.'},
    'Misura gratis gli otto segnali E-E-A-T della tua home →':
        {'en': 'Measure your homepage’s eight E-E-A-T signals for free →'},
    'Chi siamo, contatti e dati strutturati sono di serie nella SEO tecnica →':
        {'en': 'An about page, contacts and structured data come standard in technical SEO →'},
    'Misura gratis i segnali E-E-A-T del tuo sito →':
        {'en': 'Measure your site’s E-E-A-T signals for free →'},

    # ---------- Link contestuali aggiunti nelle pagine strumento (migliorare) ----------
    'Approfondisci: EAA 2026, cosa rischia davvero il vostro e-commerce →':
        {'en': 'Read more: EAA 2026, what your e-commerce site really risks →'},
    'Approfondisci: llms.txt, cos’è e serve davvero al vostro sito →':
        {'en': 'Read more: llms.txt, what it is and whether your site needs it →'},
    'Guida: come farsi trovare e citare da ChatGPT (GEO) →':
        {'en': 'Guide: how to get found and cited by ChatGPT (GEO) →'},
}
CHROME.update(CHROME_BLOG)

# CHROME_BLOG_RETROFIT — Blog · ретрофит 15.07 (piano-blog rule 4): EN-пары
# для всех новых IT-узлов ретрофита (обогащение + блоки «Fonti» + внешние
# контекстные ссылки), все 13 статей. Только EN (RU блога — руками).
# Редакция EN уровня носителя; числа в формате US.
CHROME_BLOG_RETROFIT = {
    "Web Vitals, la definizione di Google →":
        {'en': "Web Vitals, Google’s definition →"},
    "Le cifre e le affermazioni di questo articolo vengono da qui. Sono prime fonti, non riassunti: apritele e verificate.":
        {'en': "The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself."},
    "La definizione delle metriche di velocità ed esperienza che pesano di più nel check-up.":
        {'en': "The definition of the speed and experience metrics that weigh most in the check-up."},
    "La guida ufficiale a cosa Google considera qualità: è lo sfondo della dimensione SEO.":
        {'en': "The official guide to what Google considers quality: it’s the backdrop to the SEO dimension."},
    "Lo standard dietro la misura di accessibilità, oggi anche obbligo di legge nell’UE.":
        {'en': "The standard behind the accessibility measure, now also a legal requirement in the EU."},
    "Sustainable Web Design — stima delle emissioni":
        {'en': "Sustainable Web Design — emissions estimate"},
    "Il modello con cui calcoliamo l’impronta di CO₂ dal peso reale della pagina.":
        {'en': "The model we use to calculate the CO₂ footprint from the real page weight."},
    "I dati di campo di Google sugli utenti reali, alla base delle metriche di velocità.":
        {'en': "Google’s field data on real users, the basis of the speed metrics."},
    "Aprite dieci siti italiani a caso e contate: in almeno sette il pulsante «Rifiuta» è nascosto, minuscolo o non c’è proprio. È esattamente il punto su cui il Garante Privacy ha smesso di chiudere un occhio. La regola è semplice — «Rifiuta» deve pesare quanto «Accetta», il consenso dev’essere documentabile — ma è ignorata dalla maggioranza dei banner che analizziamo. Ecco la checklist punto per punto che usiamo per verificare un sito, e come costruiamo i nostri banner perché siano a norma dal primo giorno.":
        {'en': "Open ten Italian websites at random and count: on at least seven the “Reject” button is hidden, tiny, or missing altogether. This is exactly the point on which the Garante Privacy has stopped turning a blind eye. The rule is simple — “Reject” must carry the same weight as “Accept”, and consent must be documentable — but it’s ignored by most of the banners we analyze. Here’s the point-by-point checklist we use to vet a site, and how we build our banners so they’re compliant from day one."},
    "Le regole del Garante, in chiaro":
        {'en': "The Garante’s rules, in plain terms"},
    "Il principio è uno solo: il consenso ai cookie non necessari dev’essere una scelta libera. Da qui discendono le regole pratiche del Garante e delle linee guida europee. «Rifiuta» deve avere lo stesso peso visivo di «Accetta»: stesso colore, stesse dimensioni, stessa distanza dal dito. Chiudere il banner con la X equivale a rifiutare, non ad accettare. Nessun cookie di profilazione può partire prima che la persona abbia detto sì. E il consenso va conservato, così da poterlo dimostrare se qualcuno lo chiede.":
        {'en': "There’s just one principle: consent to non-essential cookies must be a free choice. From this follow the practical rules of the Garante and the European guidelines. “Reject” must have the same visual weight as “Accept”: same color, same size, same distance from your finger. Closing the banner with the X counts as rejecting, not accepting. No profiling cookie can fire before the person has said yes. And consent must be stored, so you can prove it if anyone asks."},
    "La checklist, punto per punto":
        {'en': "The checklist, point by point"},
    "Questi sono i controlli che facciamo su ogni sito prima di dire se il banner è a norma. Passateli sul vostro: bastano cinque minuti.":
        {'en': "These are the checks we run on every site before saying whether the banner is compliant. Run them on yours: five minutes is enough."},
    "Il pulsante «Rifiuta» è visibile al primo colpo, con lo stesso peso di «Accetta».":
        {'en': "The “Reject” button is visible at first glance, with the same weight as “Accept”."},
    "Nessuno script di tracciamento (Google Analytics, pixel, mappe) parte prima del consenso.":
        {'en': "No tracking script (Google Analytics, pixels, maps) fires before consent."},
    "Chiudere il banner o navigare senza scegliere non vale come consenso.":
        {'en': "Closing the banner or browsing without choosing does not count as consent."},
    "Esiste un modo semplice per cambiare idea dopo: un link «preferenze cookie» sempre raggiungibile.":
        {'en': "There’s an easy way to change your mind later: a “cookie preferences” link that’s always reachable."},
    "C’è una cookie policy chiara, che elenca i cookie e le loro finalità.":
        {'en': "There’s a clear cookie policy that lists the cookies and what they’re for."},
    "Il consenso viene registrato e resta documentabile nel tempo.":
        {'en': "Consent is recorded and stays documentable over time."},
    "Gli errori che troviamo più spesso":
        {'en': "The mistakes we find most often"},
    "Tre errori tornano quasi sempre. Il primo: il banner con solo «Accetta» ben visibile e il rifiuto sepolto in un sottomenu — è la violazione più comune e la più facile da contestare. Il secondo: gli analytics che partono al caricamento, prima di qualunque clic, perché installati «al volo» anni fa e mai più toccati. Il terzo: il cookie wall, cioè «accetta o non entri», che salvo casi rari non è una scelta libera e quindi non è un consenso valido.":
        {'en': "Three mistakes come up almost every time. The first: a banner with only “Accept” clearly visible and rejection buried in a submenu — it’s the most common violation and the easiest to challenge. The second: analytics that fire on load, before any click, because they were installed “on the fly” years ago and never touched again. The third: the cookie wall, i.e. “accept or you don’t get in”, which apart from rare cases is not a free choice and therefore not valid consent."},
    "C’è poi un quarto errore, più sottile: il banner «finto conforme», con i due pulsanti di pari peso ma i cookie di profilazione che partono comunque al caricamento, sotto il cofano. A occhio sembra a posto; basta aprire gli strumenti per sviluppatori del browser per vedere i tracker attivi prima di ogni clic. È il caso che il nostro controllo indicativo intercetta più spesso.":
        {'en': "Then there’s a fourth mistake, subtler: the “fake-compliant” banner, with two equal-weight buttons but the profiling cookies firing on load anyway, under the hood. At a glance it looks fine; just open the browser’s developer tools to see the trackers active before any click. It’s the case our indicative check catches most often."},
    "Come costruiamo un banner a norma":
        {'en': "How we build a compliant banner"},
    "Nei nostri siti il banner nasce già conforme: due pulsanti di pari peso, nessuno script prima del consenso, preferenze modificabili in ogni momento e registro dei consensi. Non è un plugin incollato all’ultimo, è parte del progetto. E se avete già un sito, la verifica è il primo passo: il nostro controllo indicativo vi dice in un minuto se banner, policy e tracker sono a posto — poi, se serve, si sistema.":
        {'en': "In our sites the banner is compliant from the start: two equal-weight buttons, no scripts before consent, preferences you can change at any time, and a consent log. It’s not a plugin stuck on at the last minute, it’s part of the project. And if you already have a site, the check is the first step: our indicative check tells you in a minute whether the banner, policy, and trackers are in order — then, if needed, we fix it."},
    "Cosa fare in mezz’ora, oggi: aprite il sito in una finestra anonima, guardate se «Rifiuta» è visibile quanto «Accetta», e con gli strumenti per sviluppatori controllate se partono script di tracciamento prima di qualsiasi scelta. Se una delle due cose non torna, avete già trovato la priorità. Non risolve tutto, ma vi dice se siete nella maggioranza a rischio o nella minoranza a posto.":
        {'en': "What to do in half an hour, today: open the site in an incognito window, check whether “Reject” is as visible as “Accept”, and with the developer tools check whether any tracking scripts fire before you make any choice. If either one is off, you’ve already found your priority. It won’t solve everything, but it tells you whether you’re in the at-risk majority or the compliant minority."},
    "Controlla gratis cookie e tracker del tuo sito →":
        {'en': "Check your site’s cookies and trackers for free →"},
    "Privacy e conformità sono parte della SEO tecnica →":
        {'en': "Privacy and compliance are part of technical SEO →"},
    "Le regole italiane su banner e consenso: la fonte diretta della checklist.":
        {'en': "The Italian rules on banners and consent: the direct source of the checklist."},
    "EDPB — report della cookie banner taskforce":
        {'en': "EDPB — cookie banner taskforce report"},
    "Il documento europeo che uniforma cosa è lecito e cosa no in un banner.":
        {'en': "The European document that standardizes what is and isn’t allowed in a banner."},
    "Il testo del GDPR: la base giuridica di consenso libero, specifico e documentabile.":
        {'en': "The text of the GDPR: the legal basis for free, specific, and documentable consent."},
    "Controlla gratis il tuo cookie banner →":
        {'en': "Check your cookie banner for free →"},
    "Il titolare di un’officina apre il sito dal telefono, in pausa pranzo, sotto rete mobile: conta i secondi, sbuffa, chiude. Non era un cliente vero, era lui — ma il gesto è identico a quello di chi vi cercava sul serio e se n’è andato. LCP, INP e CLS sono le tre sigle con cui Google misura proprio quel momento, e con cui decide chi mostrare per primo nella ricerca da mobile. Le spieghiamo senza gergo, con esempi di negozi e officine e non di startup, e vi diciamo perché il punteggio desktop — su cui molte agenzie insistono ancora — non conta quasi più nulla.":
        {'en': "The owner of a garage opens the site from his phone, on his lunch break, on mobile data: he counts the seconds, huffs, closes it. It wasn’t a real customer, it was him — but the gesture is identical to that of someone who was genuinely looking for you and left. LCP, INP, and CLS are the three acronyms Google uses to measure exactly that moment, and with which it decides who to show first in mobile search. We explain them without jargon, with examples from shops and garages rather than startups, and we tell you why the desktop score — which many agencies still insist on — counts for almost nothing anymore."},
    "LCP, INP e CLS: le tre sigle, tradotte":
        {'en': "LCP, INP, and CLS: the three acronyms, translated"},
    "LCP (Largest Contentful Paint) misura quanto tempo passa prima che compaia il contenuto più grande della pagina — di solito la foto di apertura o il titolo. È la domanda «quanto devo aspettare per vedere qualcosa di utile?». Sotto i 2,5 secondi è considerato buono; sopra i 4, la maggior parte delle persone ha già valutato se restare. Per un negozio di mobili, l’LCP è la prima fotografia del divano; per un’officina, il numero di telefono in alto.":
        {'en': "LCP (Largest Contentful Paint) measures how long it takes for the largest content on the page to appear — usually the opening photo or the headline. It’s the question “how long do I have to wait to see something useful?”. Under 2.5 seconds is considered good; over 4, most people have already decided whether to stay. For a furniture shop, the LCP is the first photo of the sofa; for a garage, the phone number at the top."},
    "INP (Interaction to Next Paint) misura la reattività: tocco un pulsante, quanto ci mette il sito a rispondere? Dal 2024 ha sostituito il vecchio FID come metrica ufficiale, ed è la più sottovalutata. CLS (Cumulative Layout Shift) misura invece la stabilità: quante volte, mentre la pagina carica, gli elementi «saltano» e vi fanno cliccare la cosa sbagliata. Chi ha provato a premere «Aggiungi al carrello» e ha comprato un altro prodotto perché la pagina si è mossa sa esattamente di cosa parliamo.":
        {'en': "INP (Interaction to Next Paint) measures responsiveness: I tap a button, how long does the site take to respond? Since 2024 it has replaced the old FID as the official metric, and it’s the most underrated one. CLS (Cumulative Layout Shift) instead measures stability: how many times, while the page loads, the elements “jump” and make you click the wrong thing. Anyone who has tried to press “Add to cart” and bought a different product because the page shifted knows exactly what we mean."},
    "Perché il punteggio mobile è l’unico che conta":
        {'en': "Why the mobile score is the only one that counts"},
    "Molte agenzie mostrano ancora con orgoglio il punteggio desktop: 98, verde brillante, complimenti. Peccato che Google indicizzi e posizioni i siti in versione mobile da anni, e che i vostri clienti vi cerchino dal telefono, spesso sotto rete lenta e con dieci schede aperte. Il punteggio che conta è quello mobile, misurato in quelle condizioni — non quello desktop preso in ufficio con la fibra.":
        {'en': "Many agencies still proudly show the desktop score: 98, bright green, congratulations. Too bad Google has been indexing and ranking sites in their mobile version for years, and your customers look for you from their phones, often on a slow connection with ten tabs open. The score that counts is the mobile one, measured in those conditions — not the desktop one taken in the office on fiber."},
    "Ecco perché nei nostri contratti la soglia è una sola e chiara: PageSpeed 90+ su mobile, garantito per iscritto. Non «faremo il possibile»: un numero, verificabile da chiunque con lo stesso strumento pubblico di Google.":
        {'en': "That’s why in our contracts there’s a single, clear threshold: PageSpeed 90+ on mobile, guaranteed in writing. Not “we’ll do our best”: a number, verifiable by anyone with the same public tool from Google."},
    "Un errore che vediamo spesso: il sito «leggero» che diventa pesante dopo il lancio, perché nel tempo si aggiungono uno slider, un chat-widget, tre pixel di tracciamento e un font in più. Ognuno sembra innocuo; insieme affondano l’INP e l’LCP. La velocità non è un traguardo che si taglia una volta: è una manutenzione. Per questo la rimisuriamo, non la diamo per scontata.":
        {'en': "A mistake we often see: the “light” site that becomes heavy after launch, because over time a slider, a chat widget, three tracking pixels, and one more font get added. Each seems harmless; together they sink the INP and LCP. Speed isn’t a finish line you cross once: it’s maintenance. That’s why we re-measure it, we don’t take it for granted."},
    "Dati di laboratorio o dati reali: la differenza che cambia tutto":
        {'en': "Lab data or real data: the difference that changes everything"},
    "C’è un equivoco che rovina metà delle discussioni sui Core Web Vitals. Esistono due tipi di misura: i dati di laboratorio (Lighthouse simula un caricamento in condizioni controllate) e i dati di campo (il Chrome UX Report raccoglie i tempi reali degli utenti veri, con i loro telefoni e le loro reti). Google, per posizionarvi, guarda i dati di campo. Un sito può segnare 95 in laboratorio e arrancare sul campo, perché i vostri clienti non hanno tutti l’iPhone nuovo e la fibra.":
        {'en': "There’s a misunderstanding that ruins half the discussions about Core Web Vitals. There are two kinds of measurement: lab data (Lighthouse simulates a load under controlled conditions) and field data (the Chrome UX Report gathers the real times of real users, with their phones and their networks). To rank you, Google looks at field data. A site can score 95 in the lab and struggle in the field, because your customers don’t all have the newest iPhone and fiber."},
    "Misurate su mobile, non su desktop: è la versione che Google usa per posizionarvi.":
        {'en': "Measure on mobile, not desktop: it’s the version Google uses to rank you."},
    "Guardate i dati di campo (CrUX), non solo il punteggio istantaneo di laboratorio.":
        {'en': "Look at the field data (CrUX), not just the instant lab score."},
    "Trattate LCP, INP e CLS come tre problemi diversi: si risolvono con interventi diversi.":
        {'en': "Treat LCP, INP, and CLS as three different problems: they’re solved with different fixes."},
    "Ricontrollate dopo ogni modifica pesante: un plugin o uno slider nuovo possono buttare giù tutto.":
        {'en': "Re-check after every major change: a new plugin or slider can bring everything down."},
    "Non serve un progetto per iniziare a capire come siete messi. Incollate l’indirizzo nel nostro test di velocità e leggete i tre valori: se l’LCP è alto, quasi sempre il colpevole sono immagini pesanti o un hosting lento; se salta il CLS, mancano le dimensioni fissate su immagini e banner; se l’INP è alto, c’è troppo codice di terze parti che blocca il telefono. Da lì sapete se basta una giornata di ottimizzazione o se conviene rifare la base — e in entrambi i casi partite da un numero, non da una sensazione.":
        {'en': "You don’t need a project to start understanding where you stand. Paste the address into our speed test and read the three values: if the LCP is high, the culprit is almost always heavy images or slow hosting; if the CLS is off, the fixed dimensions on images and banners are missing; if the INP is high, there’s too much third-party code blocking the phone. From there you know whether a day of optimization is enough or whether it’s better to rebuild the foundation — and in both cases you start from a number, not a feeling."},
    "Misura ora i Core Web Vitals del tuo sito — gratis →":
        {'en': "Measure your site’s Core Web Vitals now — for free →"},
    "Sito lento? Le 7 cause reali e quanto costa sistemarle →":
        {'en': "Slow site? The 7 real causes and what it costs to fix them →"},
    "La pagina di Google che introduce e definisce i Core Web Vitals.":
        {'en': "The Google page that introduces and defines the Core Web Vitals."},
    "La metrica di caricamento: soglia buona sotto 2,5 secondi.":
        {'en': "The loading metric: good threshold under 2.5 seconds."},
    "La metrica di reattività che dal 2024 ha sostituito il vecchio FID.":
        {'en': "The responsiveness metric that replaced the old FID in 2024."},
    "La metrica di stabilità visiva: soglia buona sotto 0,1.":
        {'en': "The visual stability metric: good threshold under 0.1."},
    "I dati di campo su utenti reali, quelli che Google usa davvero per posizionarvi.":
        {'en': "The field data on real users, the ones Google actually uses to rank you."},
    "Misura i Core Web Vitals del tuo sito — gratis →":
        {'en': "Measure your site’s Core Web Vitals — for free →"},
    "E-E-A-T, la definizione ufficiale di Google →":
        {'en': "E-E-A-T, Google’s official definition →"},
    "La pagina dove Google definisce l’E-E-A-T e spiega cosa valuta nella qualità.":
        {'en': "The page where Google defines E-E-A-T and explains what it assesses as quality."},
    "I dati strutturati JSON-LD sono uno dei segnali di identità più facili da aggiungere.":
        {'en': "JSON-LD structured data is one of the easiest identity signals to add."},
    "Google — le funzionalità AI e il vostro sito":
        {'en': "Google — AI features and your site"},
    "Perché credibilità e chiarezza contano anche nelle risposte generate dall’AI.":
        {'en': "Why credibility and clarity matter in AI-generated answers too."},
    "Direttiva (UE) 2019/882, il testo ufficiale su EUR-Lex →":
        {'en': "Directive (EU) 2019/882, the official text on EUR-Lex →"},
    "WCAG 2.1 AA, i criteri ufficiali del W3C →":
        {'en': "WCAG 2.1 AA, the official W3C criteria →"},
    "Il testo ufficiale dell’European Accessibility Act: da qui nasce l’obbligo.":
        {'en': "The official text of the European Accessibility Act: this is where the obligation comes from."},
    "Il centro di competenza UE sull’accessibilità conferma l’entrata in vigore del 28 giugno 2025.":
        {'en': "The EU accessibility competence center confirms the entry into force on 28 June 2025."},
    "Lo standard tecnico di riferimento (livello AA): i criteri con cui si misura la conformità.":
        {'en': "The reference technical standard (level AA): the criteria by which compliance is measured."},
    "Guida EAA per il commercio online — Bird & Bird":
        {'en': "EAA guide for online commerce — Bird & Bird"},
    "Uno studio legale internazionale spiega perimetro, esenzioni e sanzioni per chi vende online.":
        {'en': "An international law firm explains the scope, exemptions, and penalties for those selling online."},
    "Come Google usa i contenuti nelle risposte AI →":
        {'en': "How Google uses content in AI answers →"},
    "Come Google usa i contenuti del web nelle risposte generative e cosa possono fare i siti.":
        {'en': "How Google uses web content in generative answers and what sites can do."},
    "OpenAI — panoramica dei crawler":
        {'en': "OpenAI — crawler overview"},
    "Se GPTBot non può leggervi, ChatGPT non può citarvi: qui le regole di accesso.":
        {'en': "If GPTBot can’t read you, ChatGPT can’t cite you: here are the access rules."},
    "Anthropic — ClaudeBot e come gestirlo":
        {'en': "Anthropic — ClaudeBot and how to manage it"},
    "La stessa logica per Claude: l’accesso del crawler è il presupposto della citabilità.":
        {'en': "The same logic for Claude: crawler access is the prerequisite for being citable."},
    "La specifica llms.txt su llmstxt.org →":
        {'en': "The llms.txt specification on llmstxt.org →"},
    "La proposta llms.txt (llmstxt.org)":
        {'en': "The llms.txt proposal (llmstxt.org)"},
    "La specifica originale del formato: cosa contiene un file llms.txt e a cosa serve.":
        {'en': "The original specification of the format: what an llms.txt file contains and what it’s for."},
    "La documentazione ufficiale su GPTBot e sugli altri bot di OpenAI, con le regole robots.txt.":
        {'en': "The official documentation on GPTBot and the other OpenAI bots, with the robots.txt rules."},
    "Anthropic — ClaudeBot e come bloccarlo":
        {'en': "Anthropic — ClaudeBot and how to block it"},
    "Come Anthropic dichiara il proprio crawler e come i siti possono consentirlo o escluderlo.":
        {'en': "How Anthropic declares its crawler and how sites can allow or exclude it."},
    "Google — panoramica dei crawler (Google-Extended)":
        {'en': "Google — crawler overview (Google-Extended)"},
    "L’elenco ufficiale degli user-agent Google, incluso Google-Extended per gli usi AI.":
        {'en': "The official list of Google user-agents, including Google-Extended for AI uses."},
    "C’è un momento, in ogni rifacimento, in cui il sito nuovo va online e quello vecchio sparisce. Se qualcuno ha sbagliato i redirect, in quel momento spariscono anche anni di posizionamento su Google — e ve ne accorgete due settimane dopo, quando le richieste calano e nessuno sa perché. Migrare da WordPress senza perdere le posizioni non è fortuna: è un protocollo. Vi mostriamo l’audit, la mappa degli URL e i redirect 301 che applichiamo prima di ogni migrazione, cosa monitoriamo nelle prime sei settimane e un caso in cui il traffico non si è mosso di un punto.":
        {'en': "There’s a moment, in every rebuild, when the new site goes live and the old one disappears. If someone got the redirects wrong, in that moment years of Google ranking disappear too — and you notice two weeks later, when inquiries drop and no one knows why. Migrating from WordPress without losing your rankings isn’t luck: it’s a protocol. We show you the audit, the URL map, and the 301 redirects we apply before every migration, what we monitor in the first six weeks, and a case where traffic didn’t move by a single point."},
    "Cosa si rischia davvero in una migrazione":
        {'en': "What you really risk in a migration"},
    "Google conosce le vostre pagine con i loro indirizzi attuali. Cambiate struttura, dominio o piattaforma senza dirglielo nel modo giusto, e per Google metà del sito «è sparita»: le vecchie pagine restituiscono errore, le posizioni guadagnate in anni evaporano, e il traffico organico cala proprio mentre festeggiate il sito nuovo. Non è una maledizione tecnica: è quasi sempre la conseguenza di redirect mancanti o sbagliati.":
        {'en': "Google knows your pages by their current addresses. Change structure, domain, or platform without telling it the right way, and to Google half the site “has vanished”: the old pages return errors, the positions earned over years evaporate, and organic traffic drops right as you’re celebrating the new site. It’s not a technical curse: it’s almost always the result of missing or wrong redirects."},
    "L’errore più comune e più costoso ha un nome: il redirect «tutto alla home». Per fretta o pigrizia, si fa puntare ogni vecchio indirizzo alla pagina iniziale del sito nuovo. Per Google è quasi come cancellare quelle pagine: il valore accumulato non si trasferisce, e le posizioni scivolano. Ogni vecchia pagina deve rimandare alla sua nuova equivalente, una per una.":
        {'en': "The most common and most costly mistake has a name: the “everything to the homepage” redirect. Out of haste or laziness, every old address is pointed to the new site’s homepage. To Google this is almost like deleting those pages: the accumulated value isn’t transferred, and the rankings slip. Every old page must point to its new equivalent, one by one."},
    "Il protocollo prima del cambio":
        {'en': "The protocol before the switch"},
    "Una migrazione sicura si prepara prima di toccare qualsiasi cosa. Il lavoro vero è qui, non il giorno del lancio.":
        {'en': "A safe migration is prepared before touching anything. The real work is here, not on launch day."},
    "Audit del sito attuale: quali pagine portano traffico e posizioni, quali link puntano al sito.":
        {'en': "Audit of the current site: which pages bring traffic and rankings, which links point to the site."},
    "Mappa degli URL: ogni vecchio indirizzo abbinato al suo nuovo, senza lasciare pagine orfane.":
        {'en': "URL map: every old address matched to its new one, without leaving orphan pages."},
    "Redirect 301 uno-a-uno: ogni vecchia pagina rimanda a quella nuova equivalente, non tutte alla home.":
        {'en': "One-to-one 301 redirects: every old page points to its new equivalent, not all to the homepage."},
    "Controllo di sitemap, canonical e dati strutturati sul sito nuovo, prima di pubblicare.":
        {'en': "Check of the sitemap, canonicals, and structured data on the new site, before publishing."},
    "Piano di rollback: se qualcosa va storto, si torna indietro in minuti, non in giorni.":
        {'en': "Rollback plan: if something goes wrong, you roll back in minutes, not days."},
    "Le prime sei settimane dopo":
        {'en': "The first six weeks after"},
    "Il lancio non è la fine, è l’inizio del monitoraggio. Nelle prime sei settimane Google riscansiona il sito e ricalcola le posizioni: è normale un piccolo assestamento, non è normale un crollo. Teniamo d’occhio gli errori di scansione, le pagine che perdono posizioni, i redirect che non funzionano, e correggiamo in giornata. È la differenza tra un calo di tre giorni e un problema che si trascina per mesi.":
        {'en': "Launch isn’t the end, it’s the start of monitoring. In the first six weeks Google recrawls the site and recalculates rankings: a small settling is normal, a collapse is not. We keep an eye on crawl errors, pages losing rankings, redirects that don’t work, and we fix them the same day. It’s the difference between a three-day dip and a problem that drags on for months."},
    "Un caso reale":
        {'en': "A real case"},
    "Su un sito con anni di posizionamento locale, la migrazione a una base tecnica nuova è passata con il traffico organico invariato: stesse posizioni, stessi contatti, più velocità. Nessun miracolo — solo il protocollo, applicato con pazienza. Se state pensando a un rifacimento o a un cambio di piattaforma, il momento per parlarne è prima, non dopo il primo calo.":
        {'en': "On a site with years of local ranking, the migration to a new technical foundation went through with organic traffic unchanged: same rankings, same leads, more speed. No miracle — just the protocol, applied with patience. If you’re thinking about a rebuild or a platform change, the time to talk about it is before, not after the first drop."},
    "Cosa fare prima di dire sì a una migrazione: chiedete a chi la propone se prepara una mappa URL uno-a-uno e un piano di redirect 301 prima del lancio, e se monitora le posizioni nelle settimane dopo. Se la risposta è vaga, il rischio è vostro, non suo. Una migrazione ben fatta non si vede — ed è esattamente questo il punto: il traffico continua come se niente fosse.":
        {'en': "What to do before saying yes to a migration: ask whoever proposes it whether they prepare a one-to-one URL map and a 301 redirect plan before launch, and whether they monitor rankings in the weeks after. If the answer is vague, the risk is yours, not theirs. A well-done migration is invisible — and that’s exactly the point: traffic carries on as if nothing happened."},
    "Restyling e migrazione senza perdere posizioni →":
        {'en': "Restyling and migration without losing rankings →"},
    "Fai il check-up del sito prima di migrare →":
        {'en': "Get your site’s check-up before migrating →"},
    "Google — spostamenti del sito con cambio di URL":
        {'en': "Google — site moves with URL changes"},
    "La procedura ufficiale per una migrazione che non perde posizioni.":
        {'en': "The official procedure for a migration that doesn’t lose rankings."},
    "Come impostare i redirect 301 perché Google trasferisca il valore delle vecchie pagine.":
        {'en': "How to set up 301 redirects so Google transfers the value of the old pages."},
    "Dopo la migrazione la velocità va rimisurata: sono le metriche che Google guarda.":
        {'en': "After the migration, speed has to be re-measured: these are the metrics Google looks at."},
    "Parliamo della tua migrazione: restyling e migrazione →":
        {'en': "Let’s talk about your migration: restyling and migration →"},
    "«Ci serve un’app.» Nove volte su dieci, quando ce lo sentiamo dire, la risposta onesta è: forse no. Un’app nativa costa in media 15.000–30.000 euro, va mantenuta due volte — iOS e Android — e ogni aggiornamento passa dalla revisione degli store. Una PWA, cioè un sito «progressivo», si installa sul telefono, funziona offline e manda notifiche a una frazione di quel costo. Vediamo i tre casi in cui a una PMI conviene davvero, e i due in cui invece un’app nativa serve ancora.":
        {'en': "“We need an app.” Nine times out of ten, when we hear this, the honest answer is: maybe not. A native app costs on average € 15,000–30,000, has to be maintained twice — iOS and Android — and every update goes through the stores’ review. A PWA, i.e. a “progressive” site, installs on the phone, works offline, and sends notifications at a fraction of that cost. Let’s look at the three cases where it’s genuinely worth it for an SME, and the two where a native app is still needed."},
    "Cos’è una PWA, senza gergo":
        {'en': "What a PWA is, without the jargon"},
    "PWA sta per Progressive Web App: è un sito web normale, che si apre nel browser, ma costruito in modo da comportarsi come un’app. La persona che lo visita può «installarlo» sullo schermo del telefono con un tocco, senza passare dallo store; da lì si apre a tutto schermo, funziona anche con rete debole o assente, e — dove serve — manda notifiche. Niente download da 80 MB, niente recensione di Apple o Google da aspettare: è il vostro sito, con i superpoteri giusti.":
        {'en': "PWA stands for Progressive Web App: it’s an ordinary website, opening in the browser, but built to behave like an app. The person visiting it can “install” it on their phone’s screen with a tap, without going through the store; from there it opens full-screen, works even with a weak or absent connection, and — where needed — sends notifications. No 80 MB download, no Apple or Google review to wait for: it’s your site, with the right superpowers."},
    "Una PWA non è la risposta a tutto. Ma in questi tre casi, per una PMI, è quasi sempre la scelta giusta — più economica e più veloce da mantenere di un’app nativa.":
        {'en': "A PWA isn’t the answer to everything. But in these three cases, for an SME, it’s almost always the right choice — cheaper and faster to maintain than a native app."},
    "Un caso tipico dal nostro registro: un’officina che riceve prenotazioni. Con una PWA, il cliente abituale «installa» il sito sul telefono, lo apre con un tocco come un’app, prenota anche dal parcheggio dove la rete balla — e all’officina non è costato un secondo progetto da mantenere. La stessa cosa con un’app nativa avrebbe richiesto due sviluppi, due pubblicazioni e un canone che quella officina non avrebbe mai ripagato.":
        {'en': "A typical case from our records: a garage that takes bookings. With a PWA, the regular customer “installs” the site on their phone, opens it with a tap like an app, books even from the parking lot where the signal is shaky — and it didn’t cost the garage a second project to maintain. The same thing with a native app would have required two builds, two publications, and a fee that garage would never have recouped."},
    "Serve una scorciatoia sul telefono del cliente abituale: un ristorante che prende prenotazioni, un negozio con un catalogo che si consulta spesso.":
        {'en': "You need a shortcut on the regular customer’s phone: a restaurant that takes reservations, a shop with a catalog that gets browsed often."},
    "I clienti usano il sito anche dove la rete è ballerina: fiere, magazzini, cantieri, zone di campagna.":
        {'en': "Customers use the site even where the signal is shaky: trade fairs, warehouses, building sites, rural areas."},
    "Il budget non regge due app separate per iOS e Android più la loro manutenzione: la PWA è una sola, e vive dove vive il sito.":
        {'en': "The budget can’t sustain two separate apps for iOS and Android plus their maintenance: the PWA is a single one, and it lives where the site lives."},
    "I due casi in cui serve ancora un’app nativa":
        {'en': "The two cases where a native app is still needed"},
    "Onestà prima di tutto: a volte l’app nativa serve davvero. Il primo caso è quando il prodotto vive di funzioni profonde del telefono — fotocamera avanzata, sensori, elaborazione pesante offline, giochi. Il secondo è quando la presenza nello store è essa stessa un canale di vendita e di fiducia, e i clienti si aspettano di trovarvi lì. Fuori da questi due casi, un’app nativa è spesso un costo di prestigio che una PWA copre con meno soldi e meno grattacapi.":
        {'en': "Honesty first: sometimes a native app really is needed. The first case is when the product lives on deep phone functions — advanced camera, sensors, heavy offline processing, games. The second is when the store presence is itself a sales and trust channel, and customers expect to find you there. Outside these two cases, a native app is often a prestige cost that a PWA covers with less money and fewer headaches."},
    "Un’app nativa richiede due basi di codice, due pubblicazioni, due cicli di aggiornamento e le commissioni degli store: è per questo che parte da 15.000 euro e non smette più di costare. Una PWA parte dallo stesso sito che già vi serve, aggiunge le funzioni progressive e vive di un solo aggiornamento per tutti. Il consiglio pratico: prima di firmare per un’app, chiedetevi quali funzioni «da app» vi servono davvero. Spesso la risposta sta comodamente dentro una PWA — e i soldi risparmiati diventano contenuti e pubblicità.":
        {'en': "A native app requires two codebases, two publications, two update cycles, and the store commissions: that’s why it starts at € 15,000 and never stops costing. A PWA starts from the same site you already need, adds the progressive functions, and lives on a single update for everyone. The practical advice: before signing for an app, ask yourself which “app-like” functions you really need. Often the answer sits comfortably inside a PWA — and the money saved becomes content and advertising."},
    "Un test pratico prima di decidere: elencate le tre cose che l’app «dovrebbe fare». Se sono aprirsi in fretta, funzionare offline, stare sullo schermo e mandare una notifica, siete in territorio PWA. Se invece serve la fotocamera con riconoscimenti, i pagamenti dentro lo store o funzioni hardware profonde, allora l’app nativa ha senso. Il costo di sbagliare questa scelta si conta in decine di migliaia di euro.":
        {'en': "A practical test before deciding: list the three things the app “should do”. If they’re opening quickly, working offline, sitting on the screen, and sending a notification, you’re in PWA territory. If instead you need the camera with recognition, in-store payments, or deep hardware functions, then a native app makes sense. The cost of getting this choice wrong is counted in tens of thousands of euros."},
    "Come realizziamo i siti PWA →":
        {'en': "How we build PWA sites →"},
    "Quando invece serve una web app su misura →":
        {'en': "When you need a custom web app instead →"},
    "Cos’è una PWA e cosa la distingue da un sito normale e da un’app nativa.":
        {'en': "What a PWA is and what sets it apart from an ordinary site and a native app."},
    "La documentazione tecnica di riferimento su installabilità, offline e notifiche.":
        {'en': "The reference technical documentation on installability, offline, and notifications."},
    "Il corso di Google che spiega, passo per passo, come funziona una PWA.":
        {'en': "The Google course that explains, step by step, how a PWA works."},
    "Scopri i siti PWA di Studio Remarka →":
        {'en': "Discover Studio Remarka’s PWA sites →"},
    "Un errore da 5.000 euro: sottovalutare i contenuti":
        {'en': "A € 5,000 mistake: underestimating content"},
    "C’è una voce che quasi ogni preventivo e-commerce tiene bassa per sembrare competitivo: i contenuti. Schede prodotto scritte bene, foto vere, testi che vendono e — se esportate — traduzioni da madrelingua. Sembra la parte «facile», ed è invece quella che decide se il negozio converte o resta una vetrina silenziosa. Chi vi vende un e-commerce a poco spesso vi lascia questo conto per dopo, quando scoprite che 300 schede non si scrivono da sole.":
        {'en': "There’s one line item that almost every e-commerce quote keeps low to look competitive: content. Well-written product pages, real photos, copy that sells, and — if you export — native-speaker translations. It seems like the “easy” part, and it’s actually the one that decides whether the shop converts or stays a silent shop window. Whoever sells you a cheap e-commerce site often leaves you this bill for later, when you discover that 300 product pages don’t write themselves."},
    "Dati reali su peso, tecnologie e prestazioni dei siti, e-commerce compresi.":
        {'en': "Real data on the weight, technologies, and performance of sites, e-commerce included."},
    "Quanto vende online l’Europa: il contesto di mercato dietro le cifre di un negozio.":
        {'en': "How much Europe sells online: the market context behind a shop’s figures."},
    "La velocità mobile che difendiamo per contratto e che incide sulle vendite.":
        {'en': "The mobile speed we defend by contract and that affects sales."},
    "Dal 2025 l’accessibilità è un costo-obbligo anche per l’e-commerce: va messo nel preventivo.":
        {'en': "Since 2025 accessibility is a mandatory cost for e-commerce too: it has to go in the quote."},
    "«Mi hanno chiesto 900 euro e mi hanno chiesto 12.000 per la stessa cosa. Chi mi sta prendendo in giro?» Nessuno dei due, quasi sempre: è che «un sito aziendale» in Italia vuol dire dieci prodotti diversi con lo stesso nome. Il mercato va dagli 800 euro dei costruttori fai-da-te ai 50.000 delle grandi agenzie, e nessuno vi spiega davvero cosa cambia in mezzo. In questo articolo mettiamo una mappa onesta sotto ogni fascia di prezzo — incluso il nostro — e le domande da fare prima di firmare qualunque preventivo.":
        {'en': "“One quoted me € 900 and another quoted me € 12,000 for the same thing. Who’s pulling my leg?” Neither, almost always: it’s that “a company website” in Italy means ten different products with the same name. The market ranges from the € 800 of DIY builders to the € 50,000 of the big agencies, and no one really explains what changes in between. In this article we put an honest map under every price bracket — including ours — and the questions to ask before signing any quote."},
    "Le fasce di prezzo, senza giri di parole":
        {'en': "The price brackets, without beating around the bush"},
    "Sotto i 1.000 euro si comprano quasi sempre template montati in fretta: un costruttore fai-da-te o un conoscente «che sa fare i siti». Funzionano finché non vi serve modificarli, posizionarli o farli caricare in fretta su mobile. Nella fascia 2.500–8.000 euro sta il grosso del mercato professionale italiano: design su misura, CMS per aggiornare da soli, SEO tecnica, più lingue. Sopra i 15.000 si va verso strutture complesse, integrazioni con gestionali e progetti multi-sede.":
        {'en': "Under € 1,000 you almost always buy hastily assembled templates: a DIY builder or an acquaintance “who knows how to make websites”. They work until you need to modify them, rank them, or make them load fast on mobile. In the € 2,500–8,000 bracket sits the bulk of the Italian professional market: custom design, a CMS to update on your own, technical SEO, multiple languages. Above € 15,000 you move toward complex structures, integrations with management software, and multi-site projects."},
    "Il nostro listino per il sito aziendale sta nella fascia centrale — € 3.900–5.800, prezzo chiuso nel preventivo — con due voci che altrove raramente trovate nero su bianco: PageSpeed 90+ garantito e data di consegna con penale dell’1% per ogni giorno lavorativo di ritardo.":
        {'en': "Our price list for the company website sits in the central bracket — € 3,900–5,800, a fixed price in the quote — with two items you rarely find in black and white elsewhere: PageSpeed 90+ guaranteed and a delivery date with a 1% penalty for every working day of delay."},
    "Cosa cambia davvero tra una fascia e l’altra":
        {'en': "What really changes from one bracket to the next"},
    "Il prezzo non lo fa il numero di pagine: lo fanno tre cose. La prima è il design — un tema comprato e riempito costa un decimo di un’interfaccia disegnata sui vostri contenuti, e si vede. La seconda è la base tecnica: un sito che carica in un secondo su mobile richiede lavoro che un template non fa da solo. La terza sono i contenuti veri — testi scritti, foto fatte, traduzioni da madrelingua — che sono spesso la parte che manca nei preventivi troppo bassi, e che poi vi ritrovate a pagare a parte.":
        {'en': "The price isn’t set by the number of pages: three things set it. The first is design — a bought theme filled in costs a tenth of an interface designed around your content, and it shows. The second is the technical foundation: a site that loads in one second on mobile takes work a template doesn’t do on its own. The third is real content — written copy, photos taken, native-speaker translations — which is often the part missing from quotes that are too low, and that you then end up paying for separately."},
    "Un esempio concreto di cosa si nasconde nella parola «pagine». Due preventivi dicono entrambi «sito da 15 pagine»: uno intende 15 pagine con testi già pronti da impaginare, l’altro 15 pagine da progettare, scrivere e fotografare. Il secondo costa il doppio e vale il triplo, ma sul foglio sembrano identici. È qui che nasce metà dei «mi hanno chiesto il doppio per la stessa cosa».":
        {'en': "A concrete example of what hides inside the word “pages”. Two quotes both say “a 15-page site”: one means 15 pages with copy already ready to lay out, the other 15 pages to design, write, and photograph. The second costs twice as much and is worth three times as much, but on paper they look identical. This is where half of the “they quoted me double for the same thing” comes from."},
    "Un preventivo onesto risponde a queste domande senza esitare. Se chi avete davanti si innervosisce, avete già un’informazione.":
        {'en': "An honest quote answers these questions without hesitation. If the person in front of you gets flustered, you already have some information."},
    "Il prezzo è chiuso o «indicativo»? Cosa succede se in corso d’opera emergono lavori aggiuntivi?":
        {'en': "Is the price fixed or “indicative”? What happens if additional work comes up along the way?"},
    "La data di consegna è scritta nel contratto? Con quale penale in caso di ritardo?":
        {'en': "Is the delivery date written in the contract? With what penalty in case of delay?"},
    "Chi possiede dominio, codice e contenuti dopo la consegna: io o voi?":
        {'en': "Who owns the domain, code, and content after delivery: me or you?"},
    "La velocità su mobile è garantita con un numero, o è solo una promessa a voce?":
        {'en': "Is the mobile speed guaranteed with a number, or is it just a spoken promise?"},
    "L’assistenza dopo il lancio è inclusa, per quanto tempo, e cosa copre esattamente?":
        {'en': "Is post-launch support included, for how long, and what exactly does it cover?"},
    "Un requisito nuovo che nessuno mette a preventivo":
        {'en': "A new requirement no one puts in the quote"},
    "Dal 28 giugno 2025 l’accessibilità dei siti che vendono ai consumatori è un obbligo di legge europeo, non un abbellimento. Un preventivo che non ne parla o è vecchio, o vi lascia il conto per dopo. Nel nostro caso lo standard WCAG 2.1 AA è parte del lavoro, non un extra a sorpresa: preferiamo dirlo prima, in cifre, che scoprirlo insieme davanti a una segnalazione.":
        {'en': "Since 28 June 2025, accessibility for sites that sell to consumers is a European legal obligation, not a decoration. A quote that doesn’t mention it is either outdated or leaving you the bill for later. In our case the WCAG 2.1 AA standard is part of the work, not a surprise extra: we prefer to say it up front, in figures, than to discover it together in the face of a complaint."},
    "La differenza tra fasce, alla fine, è tutta qui: cosa è garantito per iscritto e cosa è lasciato alla buona volontà. Un template a 800 euro non vi promette una velocità, una data, un obbligo di legge rispettato; un progetto serio sì. Non comprate pagine, comprate promesse mantenibili: ed è su quelle che va letto il prezzo.":
        {'en': "The difference between brackets, in the end, is all here: what is guaranteed in writing and what is left to good will. An € 800 template doesn’t promise you a speed, a date, a legal obligation met; a serious project does. You’re not buying pages, you’re buying promises that can be kept: and it’s against those that the price should be read."},
    "Cosa include davvero un sito aziendale →":
        {'en': "What a company website really includes →"},
    "Dati reali su come è fatto il web oggi: utile per capire cosa si paga davvero.":
        {'en': "Real data on how the web is built today: useful for understanding what you’re really paying for."},
    "Il contesto europeo in cui un sito aziendale deve rendere.":
        {'en': "The European context in which a company website has to perform."},
    "La velocità mobile che garantiamo per contratto: la differenza tra le fasce di prezzo.":
        {'en': "The mobile speed we guarantee by contract: the difference between the price brackets."},
    "Dal 2025 l’accessibilità è un requisito, non un extra: va considerata nel budget.":
        {'en': "Since 2025 accessibility is a requirement, not an extra: it has to be factored into the budget."},
    "Vedi il nostro listino, a prezzo chiuso →":
        {'en': "See our price list, at a fixed price →"},
    "Perché la velocità mobile conta: Web Vitals →":
        {'en': "Why mobile speed matters: Web Vitals →"},
    "Prima di spendere un euro, misurate. Incollate l’indirizzo nel nostro test di velocità e guardate due cose: il punteggio mobile e quali risorse pesano di più. Nove volte su dieci il colpevole è già lì, in cima alla lista: una manciata di immagini enormi, un tema che carica megabyte di codice inutile, o un hosting che risponde piano. Sapere quale delle sette cause vi riguarda cambia tutto: alcune si risolvono in una giornata, altre chiedono di rifare la base.":
        {'en': "Before spending a single euro, measure. Paste the address into our speed test and look at two things: the mobile score and which resources weigh the most. Nine times out of ten the culprit is already there, at the top of the list: a handful of enormous images, a theme that loads megabytes of useless code, or hosting that responds slowly. Knowing which of the seven causes affects you changes everything: some are solved in a day, others call for rebuilding the foundation."},
    "La regola che ripetiamo sempre: non fidatevi del «mi sembra più veloce». Misurate prima, cambiate una cosa, misurate dopo. Un numero che passa da 41 a 92 convince il titolare più di qualsiasi relazione — e vi dice, nero su bianco, che i soldi spesi hanno reso.":
        {'en': "The rule we always repeat: don’t trust “it feels faster”. Measure before, change one thing, measure after. A number that goes from 41 to 92 convinces the owner more than any report — and it tells you, in black and white, that the money spent paid off."},
    "Misura ora la velocità del tuo sito — gratis →":
        {'en': "Measure your site’s speed now — for free →"},
    "Se la base è vecchia: restyling tecnico →":
        {'en': "If the foundation is old: technical restyling →"},
    "Le metriche con cui Google misura la velocità percepita di una pagina.":
        {'en': "The metrics Google uses to measure the perceived speed of a page."},
    "Cos’è l’LCP e perché immagini e hosting lo spostano più di ogni altra cosa.":
        {'en': "What the LCP is and why images and hosting move it more than anything else."},
    "Dati aggregati sul peso delle pagine: dove si concentra davvero la lentezza del web.":
        {'en': "Aggregate data on page weight: where the web’s slowness really concentrates."},
    "I dati di campo che distinguono un sito «che sembra veloce» da uno veloce davvero.":
        {'en': "The field data that tells a site that “seems fast” apart from one that’s truly fast."},
    "Un cliente tedesco apre la vostra scheda prodotto tradotta con l’automatico, legge una frase che nella sua lingua suona goffa, e chiude: non ha pensato «traduzione sbagliata», ha pensato «azienda poco seria». È così che un errore di registro costa un ordine prima ancora di una mail. La traduzione automatica basta per un menù o un orario; non basta dove si vende. In questo articolo: quando conviene l’automatico, quando serve un madrelingua, e cosa cambia davvero nei costi e nei tempi per lingua, con un caso reale di export verso la Germania.":
        {'en': "A German customer opens your machine-translated product page, reads a sentence that in their language sounds clumsy, and closes it: they didn’t think “bad translation”, they thought “unprofessional company”. That’s how a register error costs an order before even an email. Machine translation is enough for a menu or opening hours; it’s not enough where you sell. In this article: when machine translation is worth it, when you need a native speaker, and what really changes in costs and timelines per language, with a real case of exporting to Germany."},
    "Un cliente tedesco apre la vostra scheda prodotto tradotta con l’automatico, legge una frase che nella sua lingua suona goffa, e chiude: non ha pensato «traduzione sbagliata», ha pensato «azienda poco seria». È così che un errore di registro costa un ordine prima ancora di una mail. La traduzione automatica basta per un menù o un orario; non basta dove si vende. In questo articolo: quando conviene l’automatico, quando serve un madrelingua, e cosa cambia davvero nei costi e nei tempi per lingua, con un caso reale del gruppo Remarka.":
        {'en': "A German customer opens your machine-translated product page, reads a sentence that in their language sounds clumsy, and closes it: they didn’t think “bad translation”, they thought “unprofessional company”. That’s how a register error costs an order before even an email. Machine translation is enough for a menu or opening hours; it’s not enough where you sell. In this article: when machine translation is worth it, when you need a native speaker, and what really changes in costs and timelines per language, with a real case from the Remarka group."},
    "Quando la traduzione automatica basta (e quando no)":
        {'en': "When machine translation is enough (and when it isn’t)"},
    "La traduzione automatica di oggi è ottima per capire e farsi capire su cose semplici: un orario, un indirizzo, la descrizione neutra di un servizio. Se il vostro obiettivo è che un turista trovi il numero di telefono, va benissimo. Il problema nasce dove le parole vendono: una scheda prodotto tecnica, una pagina che deve convincere, un testo dove il tono conta quanto il contenuto. Lì l’automatico produce frasi «giuste ma spente», e a volte errori di registro che, nella lingua del cliente, suonano goffi o poco professionali.":
        {'en': "Today’s machine translation is excellent for understanding and being understood on simple things: opening hours, an address, the neutral description of a service. If your goal is for a tourist to find the phone number, it works fine. The problem arises where words sell: a technical product page, a page that has to persuade, a text where tone counts as much as content. There, machine translation produces sentences that are “correct but flat”, and sometimes register errors that, in the customer’s language, sound clumsy or unprofessional."},
    "Un modo semplice per decidere: chiedetevi se quella pagina informa o vende. Le pagine che informano — orari, contatti, descrizioni neutre — reggono bene l’automatico, magari con una rilettura. Le pagine che vendono — schede prodotto, landing, testi che devono convincere — vanno affidate a un madrelingua, perché lì un errore di tono non fa sorridere: fa chiudere la scheda.":
        {'en': "A simple way to decide: ask yourself whether that page informs or sells. Pages that inform — hours, contacts, neutral descriptions — hold up fine with machine translation, perhaps with a proofread. Pages that sell — product pages, landing pages, texts that have to persuade — should be entrusted to a native speaker, because there a tone error doesn’t raise a smile: it closes the page."},
    "Cosa cambia nei costi e nei tempi, per lingua":
        {'en': "What changes in costs and timelines, per language"},
    "Aggiungere una lingua non è schiacciare un pulsante «traduci». È tradurre i testi con un madrelingua, adattare quelli di vendita, tradurre anche ciò che non si vede — titoli, descrizioni per Google, messaggi di errore — e impostare i segnali tecnici (hreflang) che dicono al motore quale versione mostrare a chi. Il costo cresce con le parole reali da lavorare, non con il numero di bandierine; i tempi, con il numero di pagine che devono davvero convincere, non solo informare.":
        {'en': "Adding a language isn’t hitting a “translate” button. It’s translating the texts with a native speaker, adapting the sales ones, translating even what you don’t see — titles, descriptions for Google, error messages — and setting up the technical signals (hreflang) that tell the engine which version to show to whom. The cost grows with the real words to work on, not with the number of little flags; the timelines, with the number of pages that really have to persuade, not just inform."},
    "In pratica, per un sito aziendale medio, aggiungere una lingua ben fatta significa qualche giorno di lavoro per la traduzione e l’adattamento, più l’impostazione tecnica. Molto meno di quanto si teme, se si parte dai testi giusti; molto di più di «zero», che è quanto promette chi vi vende un plugin di traduzione automatica come se fosse una versione estera del sito.":
        {'en': "In practice, for an average company website, adding a well-done language means a few days of work for translation and adaptation, plus the technical setup. Much less than feared, if you start from the right texts; much more than “zero”, which is what those selling you a machine-translation plugin as if it were a foreign version of the site promise."},
    "L’errore che costa clienti: tradurre senza localizzare":
        {'en': "The mistake that costs customers: translating without localizing"},
    "Tradurre è cambiare le parole; localizzare è cambiare ciò che serve perché il messaggio funzioni in quel mercato. Un prezzo con la valuta giusta, una data nel formato locale, un esempio che in Germania si capisce e in Italia no, un tono più diretto o più formale a seconda del Paese. Uno studio classico di CSA Research lo dice da anni con un titolo che è già una tesi: «Can’t Read, Won’t Buy» — se non lo leggo nella mia lingua, non lo compro. Vale ancora, e vale soprattutto dove c’è un carrello.":
        {'en': "Translating is changing the words; localizing is changing whatever it takes for the message to work in that market. A price in the right currency, a date in the local format, an example that’s understood in Germany but not in Italy, a more direct or more formal tone depending on the country. A classic CSA Research study has said it for years with a title that’s already a thesis: “Can’t Read, Won’t Buy” — if I can’t read it in my language, I won’t buy it. It still holds, and it holds above all where there’s a cart."},
    "Un catalogo tradotto da madrelingua e un checkout ridotto a un solo passaggio sono le due leve che spostano più vendite dirette in un e-commerce che vende all'estero: lo applichiamo agli stessi progetti multilingue che il gruppo Remarka costruisce per sé — casi reali, con link al progetto vivo, in /casi-studio/.":
        {'en': "A catalog translated by native speakers and a checkout cut down to one step are the two levers that move the most direct sales in an e-commerce site selling abroad: we apply them to the same multilingual projects the Remarka group builds for itself — real cases, with a link to the live project, at /en/case-studies/."},
    "Le prime due cause — immagini e hosting — si risolvono spesso in giornata e da sole possono dimezzare i tempi di caricamento. La compressione moderna (AVIF/WebP con caricamento progressivo) taglia il peso delle fotografie dell’80% a parità di qualità visibile: è spesso, da sola, l’ottimizzazione con il rapporto costo/beneficio più alto in un audit.":
        {'en': "The first two causes — images and hosting — can often be fixed within a day and can halve load times on their own. Modern compression (AVIF/WebP with progressive loading) cuts photo weight by 80% with no visible loss of quality: on its own, it's often the single optimisation with the highest cost-to-benefit ratio in an audit."},
    "Un caso reale: la localizzazione che genera ordini":
        {'en': "A real case: localisation that generates orders"},
    "Il sito di ATT (traduzione.tech), online dal 2022, porta all'agenzia circa 20 ordini al mese su oltre 40 combinazioni e direzioni linguistiche — un caso reale del gruppo Remarka, non un cliente terzo, con link al progetto vivo in /casi-studio/. Non è la traduzione da sola: è la traduzione fatta da chi vende, unita a un sito veloce e a una struttura pensata per il cliente B2B. È esattamente il modello del nostro servizio Export Ready — il sito e la sua versione estera sotto un unico contratto, con redattori madrelingua.":
        {'en': "The site of ATT (traduzione.tech), live since 2022, brings the agency around 20 orders a month across more than 40 language pairs and directions — a real case from the Remarka group, not a third-party client, with a link to the live project at /en/case-studies/. It isn’t the translation alone: it’s the translation done by people who sell, combined with a fast site and a structure built for the B2B client. It’s exactly the model of our Export Ready service — the site and its foreign version under a single contract, with native-speaking editors."},
    "Siti multilingue con redattori madrelingua →":
        {'en': "Multilingual websites with native-speaking editors →"},
    "Calcola il ROI di una versione estera del sito →":
        {'en': "Calculate the ROI of a foreign version of the site →"},
    "Lo studio classico: la maggioranza dei consumatori compra solo nella propria lingua.":
        {'en': "The classic study: the majority of consumers buy only in their own language."},
    "Google — siti multi-regionali e multilingue":
        {'en': "Google — multi-regional and multilingual sites"},
    "La guida ufficiale a come strutturare un sito per più Paesi e più lingue.":
        {'en': "The official guide to how to structure a site for multiple countries and multiple languages."},
    "Come dire a Google quale versione linguistica mostrare a chi: dettaglio tecnico che conta.":
        {'en': "How to tell Google which language version to show to whom: a technical detail that matters."},
    "Il peso dell’e-commerce transfrontaliero in Europa, il mercato che una versione estera apre.":
        {'en': "The weight of cross-border e-commerce in Europe, the market a foreign version opens up."},
    "Scopri i siti multilingue di Studio Remarka →":
        {'en': "Discover Studio Remarka’s multilingual websites →"},
}
CHROME.update(CHROME_BLOG_RETROFIT)

# CHROME_BLOG_RETROFIT2 — этикетки «Fonti», названия источников и заголовки/
# подписи ретрофита, которые не срабатывают на эвристику ITALIAN_HINT конвейера
# (короткие/с брендами): явные EN-пары, чтобы в EN не осталось IT. Нейтральные
# (бренды web.dev/MDN/CrUX) — идентичны, добавлены для полноты.
CHROME_BLOG_RETROFIT2 = {
    "Fonti":
        {'en': "Sources"},
    "web.dev — Web Vitals":
        {'en': "web.dev — Web Vitals"},
    "Google — contenuti utili e affidabili (E-E-A-T)":
        {'en': "Google — helpful, reliable content (E-E-A-T)"},
    "WCAG 2 — panoramica W3C/WAI":
        {'en': "WCAG 2 — W3C/WAI overview"},
    "Chrome UX Report (CrUX)":
        {'en': "Chrome UX Report (CrUX)"},
    "Garante Privacy — linee guida sui cookie":
        {'en': "Garante Privacy — cookie guidelines"},
    "Regolamento (UE) 2016/679 — GDPR (EUR-Lex)":
        {'en': "Regulation (EU) 2016/679 — GDPR (EUR-Lex)"},
    "Cosa fare oggi, in mezz’ora":
        {'en': "What to do today, in half an hour"},
    "web.dev — Largest Contentful Paint (LCP)":
        {'en': "web.dev — Largest Contentful Paint (LCP)"},
    "web.dev — Interaction to Next Paint (INP)":
        {'en': "web.dev — Interaction to Next Paint (INP)"},
    "web.dev — Cumulative Layout Shift (CLS)":
        {'en': "web.dev — Cumulative Layout Shift (CLS)"},
    "Google — creare contenuti utili e affidabili":
        {'en': "Google — create helpful, reliable content"},
    "Google — introduzione ai dati strutturati":
        {'en': "Google — intro to structured data"},
    "Direttiva (UE) 2019/882 (EUR-Lex)":
        {'en': "Directive (EU) 2019/882 (EUR-Lex)"},
    "AccessibleEU — Commissione europea":
        {'en': "AccessibleEU — European Commission"},
    "WCAG 2.1 — W3C":
        {'en': "WCAG 2.1 — W3C"},
    "I dati strutturati JSON-LD aiutano macchine e modelli a capire chi siete e cosa offrite.":
        {'en': "JSON-LD structured data helps machines and models understand who you are and what you offer."},
    "Google — redirect e ricerca Google":
        {'en': "Google — redirects and Google Search"},
    "I tre casi in cui conviene davvero":
        {'en': "The three cases where it’s really worth it"},
    "Quanto si risparmia, in numeri":
        {'en': "How much you save, in numbers"},
    "web.dev — Progressive Web Apps":
        {'en': "web.dev — Progressive Web Apps"},
    "MDN — Progressive Web Apps":
        {'en': "MDN — Progressive Web Apps"},
    "web.dev — Learn PWA":
        {'en': "web.dev — Learn PWA"},
    "Dati di mercato reali: Web Almanac 2024 di HTTP Archive →":
        {'en': "Real market data: HTTP Archive’s Web Almanac 2024 →"},
    "HTTP Archive — Web Almanac 2024":
        {'en': "HTTP Archive — Web Almanac 2024"},
    "Eurostat — statistiche sull’e-commerce":
        {'en': "Eurostat — e-commerce statistics"},
    "Confronta prezzi e tempi, accanto a quelli di mercato →":
        {'en': "Compare prices and timelines, side by side with the market →"},
    "Eurostat — statistiche sull’economia digitale":
        {'en': "Eurostat — digital economy statistics"},
    "CSA Research — «Can’t Read, Won’t Buy»":
        {'en': "CSA Research — “Can’t Read, Won’t Buy”"},
    "Google — versioni localizzate e hreflang":
        {'en': "Google — localized versions and hreflang"},
}
CHROME.update(CHROME_BLOG_RETROFIT2)

# CHROME_BLOG_RETRO_ILLUS — иллюстрации 8 старых статей (обложки + схемы):
# EN-пары ТОЛЬКО для новых текстовых узлов (alt обложек, alt и caption схем).
# Метки внутри SVG нейтральны/двуязычны и не переводятся (файл общий IT/EN/RU).
# Числа — в формате US (как в CHROME_BLOG): us_numbers конвейера их сохраняет.
CHROME_BLOG_RETRO_ILLUS = {
    # ---- Cover alt ----
    'Un sito in quattro lingue: costi, tempi e la differenza tra tradurre e localizzare':
        {'en': 'A four-language website: costs, timelines, and the difference between translating and localizing'},
    'Cookie banner a norma nel 2026: «Rifiuta» con lo stesso peso di «Accetta» e consenso documentabile secondo il Garante Privacy':
        {'en': 'A compliant cookie banner in 2026: “Reject” with the same weight as “Accept” and documentable consent, per the Italian Garante Privacy'},
    'Migrare da WordPress senza perdere la SEO: redirect 301, mappa degli URL e sei settimane di monitoraggio':
        {'en': 'Migrating from WordPress without losing SEO: 301 redirects, a URL map, and six weeks of monitoring'},
    'PWA per le PMI: quando l’app nativa non serve, con installabilità, uso offline e notifiche':
        {'en': 'PWA for SMBs: when a native app isn’t needed — installable, offline, with notifications'},
    'Quanto costa un sito aziendale in Italia: le fasce di prezzo dagli 800 ai 50.000 euro':
        {'en': 'How much a business website costs in Italy: the price bands from € 800 to € 50,000'},
    'Core Web Vitals nel 2026: LCP, INP e CLS, le tre metriche che Google misura sul mobile':
        {'en': 'Core Web Vitals in 2026: LCP, INP and CLS, the three metrics Google measures on mobile'},
    'Quanto costa un e-commerce in Italia nel 2026: le fasce di prezzo dai 6.000 ai 25.000 euro e oltre':
        {'en': 'How much an e-commerce site costs in Italy in 2026: the price bands from € 6,000 to € 25,000 and up'},
    'Sito lento: le sette cause reali e quanto costa sistemarle':
        {'en': 'A slow website: the seven real causes and what it costs to fix them'},
    # ---- Figure alt ----
    'Tradurre contro localizzare: cambiare le parole rispetto ad adattare valuta, formato data, tono ed esempi al mercato':
        {'en': 'Translating versus localizing: changing the words compared with adapting currency, date format, tone and examples to the market'},
    'La checklist del cookie banner a norma in sei punti e gli errori più comuni':
        {'en': 'The compliant cookie-banner checklist in six points and the most common mistakes'},
    'Redirect 301 uno-a-uno che trasferisce il valore SEO contro il redirect «tutto alla home» che lo perde':
        {'en': 'A one-to-one 301 redirect that transfers SEO value versus the “all to home” redirect that loses it'},
    'Confronto tra sito, PWA e app nativa per installabilità, uso offline, notifiche, store e costo di partenza':
        {'en': 'A comparison of website, PWA and native app for installability, offline use, notifications, store and starting cost'},
    'Le tre fasce di prezzo di un sito aziendale in Italia: fai-da-te sotto i 1.000 euro, professionale tra 2.500 e 8.000, complesso oltre i 15.000':
        {'en': 'The three price bands of a business website in Italy: DIY under € 1,000, professional between € 2,500 and € 8,000, complex above € 15,000'},
    'Le soglie «buono», «da migliorare» e «scarso» di LCP, INP e CLS':
        {'en': 'The “good”, “needs improvement” and “poor” thresholds of LCP, INP and CLS'},
    'Le tre fasce di prezzo di un e-commerce in Italia e i costi ricorrenti spesso fuori dal preventivo':
        {'en': 'The three price bands of an e-commerce site in Italy and the recurring costs often left out of the quote'},
    'Le sette cause di un sito lento, dalla più frequente, con il costo dell’intervento basso, medio o alto':
        {'en': 'The seven causes of a slow website, from the most frequent, with a low, medium or high fix cost'},
    # ---- Figure caption ----
    'Tradurre cambia le parole; localizzare adatta il messaggio al mercato — valuta, formato data, tono, hreflang. Fonte: CSA Research, «Can’t Read, Won’t Buy».':
        {'en': 'Translating changes the words; localizing adapts the message to the market — currency, date format, tone, hreflang. Source: CSA Research, “Can’t Read, Won’t Buy”.'},
    'I sei controlli di un cookie banner a norma e i tre errori che troviamo più spesso. Fonte: Garante Privacy, linee guida sui cookie.':
        {'en': 'The six checks for a compliant cookie banner and the three mistakes we see most often. Source: Garante Privacy, cookie guidelines.'},
    'Ogni vecchia pagina va rimandata alla sua nuova equivalente (1→1): il redirect «tutto alla home» disperde le posizioni. Fonte: Google Search Central, spostamenti del sito e redirect.':
        {'en': 'Every old page must point to its new equivalent (1→1): the “all to home” redirect scatters your rankings. Source: Google Search Central, site moves and redirects.'},
    'Sito, PWA e app nativa a confronto: la PWA aggiunge installabilità, offline e notifiche partendo dallo stesso sito, mentre un’app nativa parte da € 15.000. Fonti: web.dev e MDN sulle Progressive Web App.':
        {'en': 'Website, PWA and native app compared: a PWA adds installability, offline use and notifications starting from the same site, while a native app starts at € 15,000. Sources: web.dev and MDN on Progressive Web Apps.'},
    'Le fasce del mercato italiano 2026: fai-da-te (sotto € 1.000), professionale (€ 2.500–8.000, dove sta il nostro listino € 3.900–5.800) e complesso (oltre € 15.000). Fonte: listini pubblici delle web agency italiane, 2026.':
        {'en': 'The Italian market bands, 2026: DIY (under € 1,000), professional (€ 2,500–8,000, where our list price € 3,900–5,800 sits) and complex (over € 15,000). Source: public price lists of Italian web agencies, 2026.'},
    'Le soglie dei tre Core Web Vitals. LCP sotto 2,5 secondi e CLS sotto 0,1 sono i valori citati nell’articolo; l’INP sotto 200 ms è la soglia «buono» ufficiale. Fonte: web.dev (Google), Web Vitals.':
        {'en': 'The thresholds of the three Core Web Vitals. LCP under 2.5 seconds and CLS under 0.1 are the values cited in the article; INP under 200 ms is the official “good” threshold. Source: web.dev (Google), Web Vitals.'},
    'Le fasce del mercato italiano 2026: template (sotto € 3.000), professionale su misura (€ 6.000–15.000, dove sta il nostro listino € 7.500–14.000) e complesso (oltre € 15.000). Ai costi di costruzione si aggiungono manutenzione (€ 500–2.000 l’anno) e commissioni sui pagamenti (1,5–3%). Fonte: listini pubblici delle web agency italiane, 2026.':
        {'en': 'The Italian market bands, 2026: template (under € 3,000), professional custom-built (€ 6,000–15,000, where our list price € 7,500–14,000 sits) and complex (over € 15,000). On top of the build cost come maintenance (€ 500–2,000 a year) and payment fees (1.5–3%). Source: public price lists of Italian web agencies, 2026.'},
    'Le sette cause più frequenti di un sito lento e il costo dell’intervento: quasi tutte si risolvono a costo basso, solo la base tecnica vecchia richiede un lavoro più profondo. Fonte: decine di audit su siti di PMI italiane (Studio Remarka).':
        {'en': 'The seven most frequent causes of a slow website and the cost to fix them: nearly all are low-cost, only an old technical base needs deeper work. Source: dozens of audits on Italian SMB websites (Studio Remarka).'},
}
CHROME.update(CHROME_BLOG_RETRO_ILLUS)

# CHROME_BLOG_BATCH2 — Blog · Batch 2 (5 articoli IT → EN) + i due backlink
# aggiunti nei tool impatto-co2 / verifica-accessibilita. Copre ogni nodo
# di testo generato da build_blog_post non gia' coperto (titoli, lead, corpo,
# liste, alt/didascalie SVG, link contestuali e CTA con « →», etichette e note
# del blocco «Fonti»). Solo EN: il blog RU e' un batch a se'. Numeri in US.
CHROME_BLOG_BATCH2 = {
    '16 LUG 2026': {'en': '16 JUL 2026'},
    # arricchimenti (paragrafi/sezioni aggiunti per densità)
    "Cosa non comprimiamo: mai la qualità":
        {'en': "What we never compress: quality"},
    "Tagliamo l’attesa, non i controlli. Le tre settimane non nascono da un lavoro fatto di corsa, ma da un lavoro senza pause morte: mentre voi rileggete una bozza, noi non restiamo fermi, prepariamo la fase successiva. Quello che non salta mai è la parte che protegge voi — i test di velocità e accessibilità, la prova su telefoni veri, il controllo dei moduli e dei link. Se una di queste verifiche non passa, non andiamo online: la data si difende con il metodo, non sacrificando il collaudo.":
        {'en': "We cut the waiting, not the checks. The three weeks don’t come from work done in a rush, but from work with no dead pauses: while you review a draft, we don’t sit idle, we prepare the next phase. What never gets skipped is the part that protects you — the speed and accessibility tests, the trial on real phones, the check of forms and links. If one of these checks fails, we don’t go live: the date is defended with method, not by sacrificing the testing."},
    "C’è un caso in cui tre settimane non bastano, e lo diciamo prima: un progetto con un catalogo grande, molte integrazioni o più lingue richiede più tempo. Non lo nascondiamo per far firmare — lo scriviamo nel preventivo, con la stessa data fissa e la stessa penale. È per questo che le tre settimane valgono per il sito aziendale: la vetrina ne chiede due, l’e-commerce sei. Un numero onesto vale più di un numero piccolo.":
        {'en': "There’s a case where three weeks aren’t enough, and we say so up front: a project with a large catalog, many integrations or several languages takes longer. We don’t hide it to get a signature — we write it in the quote, with the same fixed date and the same penalty. That’s why three weeks is the business-website figure: a brochure site asks for two, e-commerce for six. An honest number is worth more than a small one."},
    "Un dettaglio che fa la differenza: la mappa non si improvvisa il giorno del lancio. Si prepara prima, pagina per pagina, e si prova su un ambiente di test. Quando è fatta bene, il passaggio è invisibile ai visitatori e a Google — nessun errore 404, nessuna pagina orfana, nessun calo. Il rifacimento smette di essere un salto nel buio e diventa un trasloco ordinato, con le scatole etichettate.":
        {'en': "A detail that makes the difference: the map isn’t improvised on launch day. It’s prepared beforehand, page by page, and tested on a staging environment. When it’s done well, the switch is invisible to visitors and to Google — no 404 errors, no orphan pages, no drop. The rebuild stops being a leap in the dark and becomes an orderly move, with the boxes labeled."},
    "Un esempio tipico da un audit: una home da 6 megabyte, quasi tutti in fotografie non compresse, portata a poco più di 1 megabyte senza togliere una sola immagine — solo formati moderni e caricamento differito. Il risultato è triplo: pagina più veloce di alcuni secondi su telefono, banda risparmiata ogni mese e un’impronta di CO₂ per visita più che dimezzata. Un solo intervento, tre benefici — ambiente, velocità e costi — che vanno sempre nella stessa direzione.":
        {'en': "A typical example from an audit: a homepage of 6 megabytes, almost all in uncompressed photos, brought down to just over 1 megabyte without removing a single image — just modern formats and lazy loading. The result is threefold: a page several seconds faster on a phone, bandwidth saved every month, and a CO₂ footprint per visit more than halved. One intervention, three benefits — environment, speed and cost — that always pull in the same direction."},
    # estratti (indice blog)
    "Tre preventivi per lo stesso sito, tre cifre che non c’entrano niente. La griglia per leggerli riga per riga e le domande da fare prima di firmare.":
        {'en': "Three quotes for the same site, three figures that don’t add up. The grid to read them line by line and the questions to ask before signing."},
    "Il mercato ci mette 6–10 settimane, noi tre. Non è magia né lavoro fatto a metà: è metodo. Ecco cosa succede in ognuna delle tre settimane, e la penale se sforiamo.":
        {'en': "The market takes 6–10 weeks, we take three. It isn’t magic or half-done work: it’s method. Here’s what happens in each of the three weeks, and the penalty if we overrun."},
    "Rifare tutto o ritoccare? Cinque domande per capire, con i numeri e non a sensazione, se al vostro sito basta un restyling o serve ripartire da zero.":
        {'en': "Redo everything or touch it up? Five questions to work out, with numbers and not by feel, whether your site needs a redesign or a fresh start."},
    "Ogni visita consuma energia e produce CO₂. Come si misura l’impatto ambientale di un sito web, perché leggero vuol dire anche veloce ed economico, e cosa c’entra la CSRD.":
        {'en': "Every visit consumes energy and produces CO₂. How to measure a website’s environmental impact, why light also means fast and cheap, and what the CSRD has to do with it."},
    "È il documento che la legge pretende, e che un sito accessibile senza non è a norma. Cos’è la dichiarazione di accessibilità, cosa deve contenere e gli errori da evitare.":
        {'en': "It’s the document the law requires, and without which an accessible site isn’t compliant. What the accessibility statement is, what it must contain and the mistakes to avoid."},
    "Preventivo sito web: come leggerlo senza sorprese":
        {'en': "Website quote: how to read it without surprises"},
    "Avete chiesto tre preventivi per lo stesso sito e vi tornano tre cifre che sembrano parlare di progetti diversi: 2.400, 6.900, 14.000 euro. Vi pare di confrontare mele con biciclette, e in un certo senso è vero. Un preventivo sito web non è il listino del pane: dentro la stessa parola — «sito da dieci pagine» — ci stanno lavori che valgono il triplo l’uno dell’altro. In questo articolo vi diamo la griglia per leggere un preventivo riga per riga, capire dove si nasconde il prezzo vero e quali domande fare prima di firmare, così le sorprese non arrivano in fattura.":
        {'en': "You asked for three quotes for the same website and back come three figures that seem to describe different projects: € 2,400, € 6,900, € 14,000. It feels like comparing apples with bicycles, and in a sense that’s true. A website quote isn’t a bakery price list: inside the same words — “a ten-page site” — sit jobs worth three times one another. In this article we hand you the grid to read a quote line by line, see where the real price hides, and which questions to ask before signing, so the surprises don’t arrive on the invoice."},
    "Perché due preventivi «uguali» costano il doppio":
        {'en': "Why two “identical” quotes cost double"},
    "Il malinteso nasce quasi sempre da una parola sola: «pagina». Due preventivi dicono entrambi «sito da dieci pagine», ma uno intende dieci pagine con i vostri testi già pronti da impaginare su un template, l’altro dieci pagine da progettare, scrivere e fotografare su misura. Il secondo costa il doppio e vale il triplo, eppure sul foglio le due righe sembrano identiche. È qui che nasce metà dei «mi hanno chiesto una cifra assurda per la stessa cosa».":
        {'en': "The misunderstanding almost always starts from a single word: “page.” Two quotes both say “a ten-page site,” but one means ten pages with your texts already written, to lay out on a template; the other means ten pages to design, write and photograph from scratch. The second costs double and is worth triple, yet on paper the two lines look identical. This is where half of the “they quoted me an absurd amount for the same thing” comes from."},
    "Il prezzo di un sito non lo fanno le pagine, lo fanno tre cose che spesso restano implicite: quanto è su misura il design, quanto lavoro c’è sui contenuti, e cosa viene garantito per iscritto. Un preventivo onesto rende esplicite tutte e tre. Un preventivo furbo le lascia nel vago, così può essere il più basso della pila — e recuperare dopo, quando scoprite che le foto, i testi e la seconda lingua «non erano compresi».":
        {'en': "A site’s price isn’t made by the pages, it’s made by three things that often stay implicit: how bespoke the design is, how much work goes into the content, and what is guaranteed in writing. An honest quote makes all three explicit. A crafty quote leaves them vague, so it can be the lowest of the pile — and make it up later, when you find that the photos, the texts and the second language “weren’t included.”"},
    "Le sei voci che compongono un preventivo sito web. Design e contenuti sono quelle che spostano di più il prezzo; assistenza e accessibilità sono quelle che spesso «spariscono» dalle offerte più basse. Fonte: listini pubblici delle web agency italiane, 2026.":
        {'en': "The six items that make up a website quote. Design and content are the ones that move the price the most; support and accessibility are the ones that often “vanish” from the cheapest offers. Source: public price lists of Italian web agencies, 2026."},
    "Le voci che un preventivo sito web deve avere":
        {'en': "The items a website quote must include"},
    "Prima di guardare la cifra in fondo, guardate se ci sono tutte le voci. Un progetto serio si scompone più o meno sempre nello stesso modo, e ogni voce mancante è un costo che tornerà, di solito a lavoro iniziato, quando trattare è più difficile.":
        {'en': "Before looking at the figure at the bottom, check that all the items are there. A serious project breaks down more or less the same way every time, and every missing item is a cost that will come back — usually once the work has started, when negotiating is harder."},
    "Design e struttura: quanto è su misura e quanto è template. Un tema comprato e adattato è legittimo, ma deve costare come tale, non come un progetto originale.":
        {'en': "Design and structure: how much is bespoke and how much is template. A bought and adapted theme is legitimate, but it should cost as such, not as an original project."},
    "Sviluppo e messa online: CMS, moduli, integrazioni, configurazione dell’hosting. Chiedete cosa è incluso e cosa è «a parte».":
        {'en': "Development and go-live: CMS, modules, integrations, hosting setup. Ask what’s included and what’s “separate.”"},
    "Contenuti: testi, foto, eventuali traduzioni. È la voce che i preventivi bassi tengono più bassa, ed è quella che decide se il sito converte o resta una vetrina muta.":
        {'en': "Content: texts, photos, any translations. It’s the item the cheapest quotes keep lowest, and it’s the one that decides whether the site converts or stays a mute shop window."},
    "SEO tecnica e velocità: struttura, dati strutturati, PageSpeed. Se non c’è una riga, non è gratis: è che non c’è.":
        {'en': "Technical SEO and speed: structure, structured data, PageSpeed. If there isn’t a line, it isn’t free: it isn’t there."},
    "Accessibilità: dal 28 giugno 2025 è un obbligo di legge per molti siti, non un abbellimento. Un preventivo che non la nomina è vecchio o vi lascia il conto per dopo.":
        {'en': "Accessibility: since 28 June 2025 it’s a legal requirement for many sites, not an embellishment. A quote that doesn’t mention it is either old or leaving you the bill for later."},
    "Assistenza e proprietà: chi possiede dominio, codice e dati dopo la consegna, e cosa copre l’assistenza — per quanto tempo e a quali condizioni.":
        {'en': "Support and ownership: who owns the domain, code and data after delivery, and what the support covers — for how long and on what terms."},
    "Prezzo chiuso o «indicativo»? La riga che cambia tutto":
        {'en': "Fixed price or “indicative”? The line that changes everything"},
    "C’è una differenza sostanziale tra un preventivo «chiuso» e uno «indicativo», e vale più di qualsiasi sconto. Il prezzo chiuso è quello che pagherete: se emergono lavori aggiuntivi, si concordano per iscritto prima, o restano a carico di chi ha fatto il preventivo. Il prezzo indicativo è un punto di partenza che sale in corsa, quando ormai avete investito tempo e non potete tornare indietro.":
        {'en': "There’s a substantial difference between a “fixed” quote and an “indicative” one, and it’s worth more than any discount. The fixed price is what you’ll pay: if extra work comes up, it’s agreed in writing first, or it’s on whoever made the quote. The indicative price is a starting point that climbs as you go, once you’ve already invested time and can’t turn back."},
    "La stessa logica vale per i tempi. «Consegna in primavera» non è una data; «consegna il 30, con l’1% di sconto per ogni giorno lavorativo di ritardo» lo è. Chiedete sempre se la data è nel contratto e con quale penale: la risposta, più delle cifre, vi dice con chi avete a che fare. Nel nostro caso il prezzo è bloccato alla firma e la data è scritta con la penale — non per generosità, ma perché è l’unico modo per cui «senza sorprese» significhi qualcosa.":
        {'en': "The same logic applies to timing. “Delivery in spring” isn’t a date; “delivery on the 30th, with 1% off for every working day of delay” is. Always ask whether the date is in the contract and with what penalty: the answer, more than the figures, tells you who you’re dealing with. In our case the price is locked at signing and the date is written with the penalty — not out of generosity, but because it’s the only way “no surprises” means anything."},
    "Le sorprese che arrivano dopo: i costi ricorrenti":
        {'en': "The surprises that come later: the recurring costs"},
    "Il prezzo di costruzione è metà della storia. Un sito vivo costa ogni anno, e un preventivo onesto ve lo dice prima. Hosting adeguato, aggiornamenti di sicurezza, manutenzione: sul mercato la manutenzione professionale viaggia tra i 500 e i 2.000 euro l’anno, e cambia molto cosa comprende. Se vendete online si aggiungono le commissioni sui pagamenti e la fatturazione elettronica, che in Italia passa obbligatoriamente dal Sistema di Interscambio dell’Agenzia delle Entrate: assicuratevi che sia inclusa o messa a preventivo, non scoperta a negozio aperto.":
        {'en': "The build price is half the story. A living site costs every year, and an honest quote tells you so up front. Adequate hosting, security updates, maintenance: on the market professional maintenance runs between € 500 and € 2,000 a year, and what it covers varies a lot. If you sell online, add payment fees and e-invoicing, which in Italy must pass through the Agenzia delle Entrate’s Sistema di Interscambio: make sure it’s included or quoted, not discovered once the shop is open."},
    "C’è poi un costo che quasi nessun preventivo nomina ancora, ed è un obbligo: l’adeguamento all’European Accessibility Act, in vigore in Italia dal 28 giugno 2025 per i siti che vendono ai consumatori. Non è una voce facoltativa da «vedere più avanti»: è un requisito di legge, con sanzioni. Un preventivo che lo ignora non vi sta facendo risparmiare, vi sta rimandando il conto.":
        {'en': "Then there’s a cost almost no quote names yet, and it’s an obligation: compliance with the European Accessibility Act, in force in Italy since 28 June 2025 for sites that sell to consumers. It isn’t an optional item to “look at later”: it’s a legal requirement, with fines. A quote that ignores it isn’t saving you money, it’s postponing the bill."},
    "Come leggerlo in pratica: le cinque domande":
        {'en': "How to read it in practice: the five questions"},
    "Non serve diventare tecnici. Bastano cinque domande, e il modo in cui vi rispondono conta quanto le risposte: se chi avete davanti si innervosisce, avete già un’informazione.":
        {'en': "You don’t need to become technical. Five questions are enough, and the way they answer counts as much as the answers: if the person opposite gets nervous, you already have some information."},
    "Il prezzo è chiuso o indicativo? Cosa succede se in corso d’opera emergono lavori aggiuntivi?":
        {'en': "Is the price fixed or indicative? What happens if extra work comes up along the way?"},
    "La data di consegna è nel contratto, e con quale penale in caso di ritardo?":
        {'en': "Is the delivery date in the contract, and with what penalty for delay?"},
    "Contenuti, foto e traduzioni sono inclusi, o sono «a parte»?":
        {'en': "Are content, photos and translations included, or are they “separate”?"},
    "Chi possiede dominio, codice e dati dopo la consegna — io o voi?":
        {'en': "Who owns the domain, code and data after delivery — me or you?"},
    "Accessibilità e velocità su mobile sono garantite con un numero, o sono promesse a voce?":
        {'en': "Are accessibility and mobile speed guaranteed with a number, or promised verbally?"},
    "Prima di rifare: misura la salute del sito attuale →":
        {'en': "Before rebuilding: measure the health of your current site →"},
    "Leggi anche: sito web in 3 settimane, com’è possibile davvero →":
        {'en': "Read also: a website in 3 weeks, how it’s really possible →"},
    "Agenzia delle Entrate — fatturazione elettronica (SDI)":
        {'en': "Agenzia delle Entrate — e-invoicing (SDI)"},
    "La pagina ufficiale sul Sistema di Interscambio: un costo che ogni e-commerce deve mettere a preventivo.":
        {'en': "The official page on the Sistema di Interscambio: a cost every e-commerce site must put in the quote."},
    "Dal 28 giugno 2025 l’accessibilità è un obbligo, non un extra: va considerata nel preventivo.":
        {'en': "Since 28 June 2025 accessibility is an obligation, not an extra: it belongs in the quote."},
    "Dati reali su com’è fatto il web oggi: utile per capire cosa si paga davvero dietro un sito.":
        {'en': "Real data on how the web is actually built today: useful to understand what you’re really paying for behind a site."},
    "La velocità mobile che va garantita con un numero: la differenza tra un preventivo serio e uno vago.":
        {'en': "The mobile speed that must be guaranteed with a number: the difference between a serious quote and a vague one."},
    "Preventivo sito web: come leggerlo riga per riga, le voci che spostano il prezzo e le sorprese da evitare in fattura":
        {'en': "Website quote: how to read it line by line, the items that move the price, and the surprises to avoid on the invoice"},
    "Le voci di un preventivo sito web: design, sviluppo, contenuti, SEO tecnica, accessibilità e assistenza, e quali fanno oscillare di più il prezzo":
        {'en': "The items of a website quote: design, development, content, technical SEO, accessibility and support, and which ones swing the price the most"},
    "Sito web in 3 settimane: com’è possibile (davvero)":
        {'en': "A website in 3 weeks: how it’s (really) possible"},
    "«Un sito web in 3 settimane? O è una fregatura, o è un template riempito in fretta.» È la reazione più comune, ed è sana: sul mercato italiano un sito aziendale richiede in media 6–10 settimane, quindi promettere tre suona come promettere di dimagrire dormendo. Eppure lo facciamo, con la data scritta in contratto e una penale se sforiamo. Non c’è nessun trucco e nessun lavoro fatto a metà: c’è un metodo che toglie i tempi morti, non la qualità. Vediamo, giorno per giorno, com’è possibile un sito web in 3 settimane — e cosa serve da parte vostra perché funzioni.":
        {'en': "“A website in 3 weeks? Either it’s a scam, or it’s a template filled in a hurry.” It’s the most common reaction, and a healthy one: on the Italian market a business website takes 6–10 weeks on average, so promising three sounds like promising to lose weight while sleeping. Yet we do it, with the date written in the contract and a penalty if we overrun. There’s no trick and no half-done work: there’s a method that removes the dead time, not the quality. Let’s see, day by day, how a website in 3 weeks is possible — and what we need from you to make it work."},
    "Tre settimane non è magia: è togliere i tempi morti":
        {'en': "Three weeks isn’t magic: it’s removing the dead time"},
    "Le 6–10 settimane del mercato non sono quasi mai lavoro: sono attesa. Il preventivo che resta indeciso per giorni, i contenuti che arrivano a rate, il design che va avanti e indietro cinque volte perché nessuno ha fissato lo scopo all’inizio. Il tempo se ne va nel ping-pong, non nel produrre. Noi comprimiamo le tre settimane aggredendo proprio quel ping-pong: scopo chiuso alla firma, un solo giro di revisione per fase, contenuti raccolti con voi in un incontro invece che inseguiti per email.":
        {'en': "The market’s 6–10 weeks are hardly ever work: they’re waiting. The quote that stays undecided for days, content arriving in dribs and drabs, a design going back and forth five times because nobody set the scope at the start. Time goes in the ping-pong, not in producing. We compress the three weeks by attacking exactly that ping-pong: scope fixed at signing, a single round of revisions per phase, content gathered with you in one meeting rather than chased by email."},
    "La seconda leva è banale ma decisiva: partiamo da fondamenta nostre, collaudate su decine di progetti, non da un foglio bianco ogni volta. Questo non vuol dire «tutti i siti uguali»: vuol dire che l’impalcatura tecnica — velocità, accessibilità, struttura SEO — è già solida, e le tre settimane le spendiamo su ciò che è vostro, non a reinventare la ruota.":
        {'en': "The second lever is banal but decisive: we start from our own foundations, proven across dozens of projects, not from a blank page every time. That doesn’t mean “all sites the same”: it means the technical scaffolding — speed, accessibility, SEO structure — is already solid, and we spend the three weeks on what’s yours, not on reinventing the wheel."},
    "Settimana 1: analisi, preventivo chiuso, design":
        {'en': "Week 1: analysis, fixed quote, design"},
    "La prima settimana decide le altre due. Facciamo l’analisi — chi siete, chi volete raggiungere, cosa deve fare il sito — e da lì esce un preventivo chiuso, con prezzo bloccato e data. Poi il design: non venti bozze, ma una direzione condivisa e approvata, così la settimana dopo si sviluppa senza ripensamenti. È la settimana che richiede più presenza da parte vostra, ed è tempo ben speso: ogni decisione presa adesso è un ritardo evitato dopo.":
        {'en': "The first week decides the other two. We do the analysis — who you are, who you want to reach, what the site has to do — and out of it comes a fixed quote, with locked price and date. Then the design: not twenty drafts, but one shared, approved direction, so the following week develops with no second thoughts. It’s the week that asks the most of you, and it’s time well spent: every decision taken now is a delay avoided later."},
    "Dalla firma all’online in 21 giorni: analisi e design (settimana 1), sviluppo (settimana 2), contenuti, test e pubblicazione (settimana 3). La data è in contratto: ogni giorno lavorativo di ritardo vale l’1% di sconto. Tempi del sito aziendale; la vetrina è 2 settimane, l’e-commerce 6.":
        {'en': "From signing to online in 21 days: analysis and design (week 1), development (week 2), content, testing and publishing (week 3). The date is in the contract: every working day of delay is 1% off. Business-website timing; a brochure site is 2 weeks, e-commerce 6."},
    "Settimana 2: sviluppo, con la velocità già dentro":
        {'en': "Week 2: development, with speed already built in"},
    "Nella seconda settimana il design approvato diventa un sito che funziona. Qui la scelta di partire da fondamenta collaudate paga tutto il suo prezzo: la struttura tecnica che regge la velocità e l’accessibilità è già al suo posto, e lo sviluppo si concentra sulle vostre pagine, non sull’impalcatura. Non rincorriamo il PageSpeed 90+ alla fine come una toppa: lo costruiamo mentre sviluppiamo, perché la velocità non è un ritocco finale ma il modo in cui il sito è fatto.":
        {'en': "In the second week the approved design becomes a site that works. Here the choice to start from proven foundations pays for itself in full: the technical structure that carries speed and accessibility is already in place, and development focuses on your pages, not the scaffolding. We don’t chase PageSpeed 90+ at the end like a patch: we build it as we develop, because speed isn’t a final touch-up but the way the site is made."},
    "La terza settimana è quella dei dettagli che si vedono e di quelli che non si vedono. Impaginiamo i contenuti definitivi, poi testiamo: velocità reale su telefono, accessibilità secondo lo standard WCAG 2.1 AA — oggi anche un obbligo di legge — moduli, link, comportamento su schermi diversi. Solo quando i numeri tornano si va online. Un sito veloce che rispetta le persone non è un vezzo: è ciò che Google misura per posizionarvi e ciò che tiene le visite invece di farle scappare.":
        {'en': "The third week is the one of the details you see and the ones you don’t. We lay out the final content, then test: real speed on a phone, accessibility to the WCAG 2.1 AA standard — today also a legal requirement — forms, links, behavior on different screens. Only when the numbers add up do we go live. A fast site that respects people isn’t a frill: it’s what Google measures to rank you and what keeps visits instead of sending them away."},
    "Verifica la salute di un sito con il check-up completo →":
        {'en': "Check a site’s health with the full check-up →"},
    "E se sforiamo? La penale, e cosa serve da parte vostra":
        {'en': "And if we overrun? The penalty, and what we need from you"},
    "La data in contratto vale solo se ha un prezzo: ogni giorno lavorativo di ritardo è l’1% di sconto sul totale. È la ragione per cui prendiamo sul serio le tre settimane, ed è anche la ragione per cui vi chiediamo una cosa in cambio. Il rispetto della data dipende da due mani: perché tre settimane bastino, i contenuti e le decisioni devono arrivare quando li chiediamo, non a lavoro iniziato. La settimana 1 serve proprio a questo — a raccogliere tutto insieme, così le settimane 2 e 3 corrono.":
        {'en': "The date in the contract only counts if it has a price: every working day of delay is 1% off the total. It’s the reason we take the three weeks seriously, and it’s also the reason we ask one thing in return. Meeting the date depends on two hands: for three weeks to be enough, content and decisions have to arrive when we ask for them, not once the work has started. Week 1 exists precisely for this — to gather everything together, so weeks 2 and 3 can run."},
    "Chi promette «un sito in una settimana» senza chiedervi niente sta vendendo un template svuotato. Chi vi promette «quando sarà pronto» sta lasciando aperta una porta che costa cara. Tre settimane, con una data e una penale, è il punto onesto tra le due cose: veloce sul serio, ma senza scorciatoie sulla qualità.":
        {'en': "Whoever promises “a site in a week” without asking you for anything is selling a hollowed-out template. Whoever promises you “whenever it’s ready” is leaving open a door that costs dearly. Three weeks, with a date and a penalty, is the honest point between the two: genuinely fast, but with no shortcuts on quality."},
    "Cosa include un sito aziendale, a prezzo chiuso →":
        {'en': "What a business website includes, at a fixed price →"},
    "Prima di firmare: come leggere un preventivo sito web →":
        {'en': "Before signing: how to read a website quote →"},
    "Sito già online? Restyling o sito nuovo: il test delle 5 domande →":
        {'en': "Already online? Redesign or new site: the test of 5 questions →"},
    "La velocità mobile che garantiamo per contratto: il PageSpeed 90+ non è uno slogan, è una soglia misurabile.":
        {'en': "The mobile speed we guarantee by contract: PageSpeed 90+ isn’t a slogan, it’s a measurable threshold."},
    "Dal 2025 l’accessibilità è parte dello scopo di ogni sito nuovo, non un lavoro rimandabile.":
        {'en': "Since 2025 accessibility is part of the scope of every new site, not a job to postpone."},
    "Cosa Google considera qualità: lo sfondo del perché testiamo prima di andare online.":
        {'en': "What Google considers quality: the backdrop to why we test before going live."},
    "I dati strutturati fanno parte dell’impalcatura tecnica che è già pronta in partenza.":
        {'en': "Structured data is part of the technical scaffolding that’s ready from the start."},
    "Sito aziendale in 3 settimane, prezzo chiuso →":
        {'en': "A business website in 3 weeks, fixed price →"},
    "Sito web in 3 settimane: le tre settimane dalla firma all’online, analisi, sviluppo e messa online con data in contratto":
        {'en': "A website in 3 weeks: the three weeks from signing to online, analysis, development and go-live with the date in the contract"},
    "Le tre settimane dalla firma all’online: settimana 1 analisi e design, settimana 2 sviluppo, settimana 3 contenuti, test e messa online":
        {'en': "The three weeks from signing to online: week 1 analysis and design, week 2 development, week 3 content, testing and go-live"},
    "Restyling o sito nuovo? Il test delle 5 domande":
        {'en': "Redesign or new website? The test of 5 questions"},
    "C’è un momento in cui aprite il vostro sito dal telefono e qualcosa stona: carica piano, sembra vecchio, i contatti arrivano col contagocce. La domanda che segue è sempre la stessa — «lo ritocchiamo o lo rifacciamo da capo?» — e la risposta sbagliata costa in entrambe le direzioni: si può buttare via un sito ancora buono, o accanirsi a rattoppare una base ormai fusa. Non è una scelta da fare a sensazione. Bastano cinque domande per capire se al vostro sito serve un restyling o un rifacimento vero — e questo articolo ve le mette in mano.":
        {'en': "There’s a moment when you open your site on your phone and something jars: it loads slowly, it looks old, the enquiries trickle in. The question that follows is always the same — “do we touch it up or rebuild it from scratch?” — and the wrong answer costs in both directions: you can throw away a site that’s still good, or keep patching a base that’s already burnt out. It isn’t a choice to make by feel. Five questions are enough to tell whether your site needs a redesign or a real rebuild — and this article puts them in your hands."},
    "Restyling o rifacimento: non è la stessa spesa":
        {'en': "Redesign or rebuild: not the same spend"},
    "Prima di decidere, mettiamo d’accordo le parole. Un restyling lavora sopra una base che tiene: rinnova l’aspetto, riscrive dei contenuti, sistema la velocità e l’accessibilità, ma non demolisce le fondamenta. Un rifacimento rifà la base tecnica da zero — tema, struttura, spesso la piattaforma — e ci riporta sopra i contenuti che meritano di restare. Il primo costa meno e dura meno a farsi; il secondo costa di più ma risolve problemi che nessun ritocco può toccare.":
        {'en': "Before deciding, let’s agree on the words. A redesign works on top of a base that holds: it refreshes the look, rewrites some content, fixes speed and accessibility, but doesn’t demolish the foundations. A rebuild redoes the technical base from scratch — theme, structure, often the platform — and carries back onto it the content that deserves to stay. The first costs less and takes less time; the second costs more but solves problems no touch-up can reach."},
    "Sbagliare la diagnosi è la spesa più stupida di tutte. Fare un rifacimento completo quando bastava un restyling è buttare soldi; fare un restyling su una base marcia è come cambiare le gomme a un motore fuso — ogni intervento costa e il risultato resta mediocre. Le cinque domande servono esattamente a non sbagliare questa diagnosi.":
        {'en': "Getting the diagnosis wrong is the dumbest spend of all. Doing a full rebuild when a redesign would have done is throwing money away; doing a redesign on a rotten base is like putting new tires on a blown engine — every fix costs and the result stays mediocre. The five questions exist precisely to avoid getting this diagnosis wrong."},
    "Il test delle 5 domande":
        {'en': "The test of 5 questions"},
    "Rispondete con onestà. Più «sì» collezionate, più l’ago si sposta dal restyling verso il sito nuovo. Non è una formula magica, è un modo per guardare in faccia le cose che di solito si evitano.":
        {'en': "Answer honestly. The more “yeses” you collect, the more the needle moves from redesign toward new site. It isn’t a magic formula, it’s a way to look in the face the things you usually avoid."},
    "1. Il sito è lento su telefono anche dopo aver alleggerito le immagini? Se la lentezza sta nella base — tema pesante, plugin stratificati, PHP vecchio — ritoccare non basta.":
        {'en': "1. Is the site slow on a phone even after you’ve lightened the images? If the slowness is in the base — heavy theme, layered plugins, old PHP — touching up isn’t enough."},
    "2. Ogni modifica è una battaglia? Se aggiungere una pagina o cambiare un testo richiede un tecnico e mezza giornata, la struttura sta remando contro di voi.":
        {'en': "2. Is every change a battle? If adding a page or changing a text needs a developer and half a day, the structure is rowing against you."},
    "3. È inutilizzabile o inaccessibile da mobile? Se una persona su due arriva da telefono e fatica, non è un ritocco estetico: è un problema di fondamenta.":
        {'en': "3. Is it unusable or inaccessible on mobile? If one person in two arrives by phone and struggles, it isn’t a cosmetic touch-up: it’s a foundations problem."},
    "4. La piattaforma è ferma o insicura? Versioni obsolete, aggiornamenti impossibili, avvisi di sicurezza: sono crepe strutturali, non macchie da coprire.":
        {'en': "4. Is the platform stuck or insecure? Obsolete versions, impossible updates, security warnings: these are structural cracks, not stains to cover."},
    "5. Il sito non dice più cosa siete diventati? Se posizionamento, offerta e pubblico sono cambiati e il sito è rimasto indietro, il problema è la sostanza, non la vernice.":
        {'en': "5. Does the site no longer say what you’ve become? If your positioning, offer and audience have changed and the site has stayed behind, the problem is substance, not paint."},
    "Le cinque domande e dove portano: pochi «sì», e concentrati sull’aspetto, indicano un restyling; molti «sì», e sulle fondamenta (velocità, piattaforma, mobile), indicano un sito nuovo. La soglia non è matematica: conta quali domande.":
        {'en': "The five questions and where they lead: few “yeses,” concentrated on appearance, point to a redesign; many “yeses,” on the foundations (speed, platform, mobile), point to a new site. The threshold isn’t mathematical: it’s which questions."},
    "Quando basta un restyling":
        {'en': "When a redesign is enough"},
    "Se i «sì» sono pochi e riguardano l’aspetto — il sito invecchiato ma ancora rapido, facile da aggiornare, solido sotto il cofano — il restyling è la scelta giusta e la più intelligente. Rinnovate l’immagine, riscrivete i contenuti che vendono, sistemate accessibilità e velocità, e tenete tutto il valore che il sito ha già accumulato su Google. Prima di decidere, però, guardate i numeri e non l’impressione: un check-up del sito misura in un minuto velocità, SEO, accessibilità e privacy, e vi dice se la base regge davvero o se vi sta solo sembrando.":
        {'en': "If the “yeses” are few and about appearance — the site aged but still fast, easy to update, solid under the hood — the redesign is the right and smartest choice. Refresh the image, rewrite the content that sells, fix accessibility and speed, and keep all the value the site has already built on Google. Before deciding, though, look at the numbers and not the impression: a site check-up measures speed, SEO, accessibility and privacy in a minute, and tells you whether the base really holds or only seems to."},
    "Misura la salute del sito prima di scegliere: check-up completo →":
        {'en': "Measure the site’s health before choosing: full check-up →"},
    "Quando conviene il sito nuovo (e come non perdere Google)":
        {'en': "When a new site is worth it (and how not to lose Google)"},
    "Se i «sì» si accumulano sulle fondamenta — lentezza strutturale, piattaforma insicura, mobile inutilizzabile — il rifacimento non è uno spreco, è la fine di uno spreco. La paura giusta, a quel punto, è una sola: perdere le posizioni guadagnate in anni. È una paura legittima e gestibile. Con una mappa degli URL uno-a-uno e i redirect 301 fatti prima del lancio, il valore delle vecchie pagine si trasferisce alle nuove e il traffico continua come se niente fosse. Il crollo dopo un rifacimento non è una maledizione tecnica: è quasi sempre la conseguenza di redirect mancanti o fatti «tutti alla home».":
        {'en': "If the “yeses” pile up on the foundations — structural slowness, an insecure platform, unusable mobile — the rebuild isn’t a waste, it’s the end of a waste. The right fear, at that point, is only one: losing the rankings earned over years. It’s a legitimate and manageable fear. With a one-to-one URL map and 301 redirects done before launch, the value of the old pages transfers to the new ones and traffic carries on as if nothing happened. The collapse after a rebuild isn’t a technical curse: it’s almost always the consequence of missing redirects, or ones done “all to the homepage.”"},
    "Come funzionano i redirect quando si cambia sito (Google) →":
        {'en': "How redirects work when you change site (Google) →"},
    "Decidere con i numeri, non a sensazione":
        {'en': "Deciding with numbers, not by feel"},
    "La regola che ripetiamo sempre: prima si misura, poi si decide. Un check-up onesto trasforma «mi sembra vecchio» in una lista di problemi con una priorità, e da lì la scelta tra restyling e sito nuovo diventa quasi ovvia. Se dai numeri esce che la base regge, si ritocca; se esce che è finita, si rifà — e in entrambi i casi si parte da un dato, non da una sensazione o da un venditore che ha già deciso per voi.":
        {'en': "The rule we always repeat: measure first, then decide. An honest check-up turns “it feels old” into a list of problems with a priority, and from there the choice between redesign and new site becomes almost obvious. If the numbers show the base holds, you touch it up; if they show it’s finished, you rebuild — and in both cases you start from a fact, not a feeling or a salesperson who has already decided for you."},
    "Un ultimo criterio che quasi nessuno considera: il peso. Un sito vecchio è spesso anche un sito pesante, e un sito pesante è lento, costoso da servire e più inquinante. Rifare la base, quando serve, è anche l’occasione per alleggerire — e la velocità che ne esce si vede subito, sul telefono e nei contatti.":
        {'en': "One last criterion almost nobody considers: weight. An old site is often also a heavy site, and a heavy site is slow, expensive to serve and more polluting. Rebuilding the base, when needed, is also the chance to lighten it — and the speed that comes out shows immediately, on the phone and in the enquiries."},
    "Restyling e migrazione, senza perdere posizioni →":
        {'en': "Redesign and migration, without losing rankings →"},
    "Leggi anche: quanto pesa il vostro sito sull’ambiente (e sul portafoglio) →":
        {'en': "Read also: how much your site weighs on the environment (and on your wallet) →"},
    "La procedura ufficiale per rifare un sito senza perdere il posizionamento su Google.":
        {'en': "The official procedure for rebuilding a site without losing your Google rankings."},
    "Come impostare i redirect 301 perché Google trasferisca il valore delle vecchie pagine alle nuove.":
        {'en': "How to set up 301 redirects so Google transfers the value of the old pages to the new ones."},
    "Le metriche di velocità con cui distinguere un sito ancora buono da uno da rifare.":
        {'en': "The speed metrics to tell a site that’s still good from one to rebuild."},
    "Il modello che lega il peso della pagina al consumo: un sito vecchio è spesso anche pesante.":
        {'en': "The model linking a page’s weight to its consumption: an old site is often also a heavy one."},
    "Restyling sito web o sito nuovo: il test delle cinque domande per decidere con i numeri se ritoccare o ripartire da zero":
        {'en': "Redesign or new website: the test of five questions to decide with numbers whether to touch up or start over"},
    "Il test delle cinque domande su velocità, facilità di modifica, mobile, piattaforma e messaggio, con l’esito restyling o sito nuovo":
        {'en': "The test of five questions on speed, ease of editing, mobile, platform and message, with the outcome redesign or new site"},
    "Quanto pesa il vostro sito sull’ambiente (e sul portafoglio)":
        {'en': "How much your site weighs on the environment (and on your wallet)"},
    "Un sito web sembra immateriale, ma non lo è: ogni volta che qualcuno lo apre, dei byte viaggiano da un data center alla sua schermata, e quel viaggio consuma energia. Moltiplicate per decine di migliaia di visite al mese e l’«immateriale» diventa una bolletta e un po’ di anidride carbonica. La buona notizia è che l’impatto ambientale di un sito web si può stimare, e che ridurlo coincide quasi sempre con renderlo più veloce e meno costoso. Vediamo come si misura, cosa c’entrano i vostri conti e la nuova rendicontazione europea, e cosa potete fare in un pomeriggio.":
        {'en': "A website seems immaterial, but it isn’t: every time someone opens it, bytes travel from a data center to their screen, and that journey consumes energy. Multiply by tens of thousands of visits a month and the “immaterial” becomes a bill and a bit of carbon dioxide. The good news is that a website’s environmental impact can be estimated, and that reducing it almost always coincides with making it faster and cheaper. Let’s see how it’s measured, what it has to do with your accounts and the new European reporting rules, and what you can do in an afternoon."},
    "Un sito ha un peso, e il peso ha un costo":
        {'en': "A site has a weight, and the weight has a cost"},
    "Il peso di una pagina è la somma di tutto ciò che il browser deve scaricare per mostrarla: immagini, caratteri, script, video. Più è pesante, più energia serve per trasferirla e visualizzarla — nel data center, lungo la rete, sul dispositivo di chi guarda. Quell’energia ha due prezzi paralleli: uno ambientale, in grammi di CO₂, e uno economico, in server più cari, campagne che portano visite che scappano, e clienti che se ne vanno prima di vedere la prima riga perché il telefono arranca.":
        {'en': "A page’s weight is the sum of everything the browser has to download to show it: images, fonts, scripts, video. The heavier it is, the more energy it takes to transfer and display — in the data center, along the network, on the viewer’s device. That energy has two parallel prices: an environmental one, in grams of CO₂, and an economic one, in more expensive servers, campaigns that bring visits that flee, and customers who leave before seeing the first line because the phone is struggling."},
    "È il motivo per cui parliamo di ambiente e portafoglio nello stesso respiro: non sono due discorsi, è lo stesso discorso. La pagina che inquina di più è, quasi sempre, la stessa che carica più lentamente e costa di più mantenere.":
        {'en': "That’s why we talk about the environment and the wallet in the same breath: they aren’t two conversations, it’s the same conversation. The page that pollutes most is, almost always, the same one that loads more slowly and costs more to maintain."},
    "Come si stima l’impatto ambientale di un sito web":
        {'en': "How to estimate a website’s environmental impact"},
    "Non è una sensazione, è un calcolo. Si parte da un dato misurabile — il peso della pagina in byte — e gli si applica un modello che traduce i byte trasferiti in energia e poi in grammi di CO₂ equivalente. Il modello più usato è il Sustainable Web Design, reso disponibile dalla Green Web Foundation nella libreria open source co2.js: gli stessi strumenti che stanno dietro ai calcolatori di emissioni del web. Il riferimento comodo è la media: una pagina web produce intorno agli 0,8 grammi di CO₂ per visita. Sotto quella soglia siete leggeri; sensibilmente sopra, c’è margine per alleggerire.":
        {'en': "It isn’t a feeling, it’s a calculation. You start from a measurable figure — the page weight in bytes — and apply a model that turns the transferred bytes into energy and then into grams of CO₂ equivalent. The most widely used model is Sustainable Web Design, made available by the Green Web Foundation in the open-source library co2.js: the same tools behind the web’s emission calculators. The handy reference is the average: a web page produces around 0.8 grams of CO₂ per visit. Below that threshold you’re light; noticeably above, there’s room to lighten."},
    "Serve onestà sui limiti, perché qui è facile vendere fumo. È una stima con coefficienti medi mondiali: non conosce l’energia reale del vostro hosting né il comportamento di ogni visitatore. Non è un’impronta certificata, è un ordine di grandezza affidabile e confrontabile — e il suo pregio è proprio che si aggancia a un fatto tecnico su cui potete davvero intervenire: il peso.":
        {'en': "Some honesty about the limits is in order, because it’s easy to sell smoke here. It’s an estimate with global average coefficients: it doesn’t know your hosting’s real energy or every visitor’s behavior. It isn’t a certified footprint, it’s a reliable, comparable order of magnitude — and its merit is precisely that it hangs on a technical fact you can actually act on: weight."},
    "Dal peso ai grammi: i byte trasferiti diventano energia e poi CO₂ per visita, moltiplicata per il traffico dà la stima annua. Riferimento: media del web ≈ 0,8 g per visita. Modello: Sustainable Web Design (co2.js, Green Web Foundation).":
        {'en': "From weight to grams: the transferred bytes become energy and then CO₂ per visit, which multiplied by traffic gives the yearly estimate. Reference: web average ≈ 0.8 g per visit. Model: Sustainable Web Design (co2.js, Green Web Foundation)."},
    "Perché leggero vuol dire veloce e più economico":
        {'en': "Why light means fast and cheaper"},
    "Alleggerire una pagina e velocizzarla sono la stessa operazione, vista da due lati. Ogni byte tolto è meno energia trasferita — quindi meno CO₂ — e insieme meno tempo di caricamento, quindi più visite che restano. Le fotografie non ottimizzate sono quasi sempre la voce più pesante: convertirle nei formati moderni può tagliarne l’80% a parità di qualità visibile, e con esse taglia emissioni, costi di banda e secondi di attesa. Non dovete scegliere tra fare bene al pianeta e fare bene ai conti: è la stessa leva.":
        {'en': "Lightening a page and speeding it up are the same operation seen from two sides. Every byte removed is less energy transferred — so less CO₂ — and at the same time less loading time, so more visits that stay. Unoptimized photos are almost always the heaviest item: converting them to modern formats can cut them by 80% at the same visible quality, and with them cuts emissions, bandwidth costs and seconds of waiting. You don’t have to choose between doing right by the planet and doing right by the accounts: it’s the same lever."},
    "La CO₂ entra anche nei bilanci: la CSRD":
        {'en': "CO₂ enters the balance sheets too: the CSRD"},
    "Fino a ieri l’impatto ambientale di un sito era una questione di sensibilità. Da poco è anche una voce che può finire in un bilancio. La direttiva europea sulla rendicontazione di sostenibilità — la CSRD — allarga di molto la platea delle aziende che devono rendicontare i propri impatti ambientali, e chi ha questo obbligo lo estende ai fornitori. Se lavorate con o dentro aziende soggette alla CSRD, un sito misurabile e leggero smette di essere un vezzo e diventa un dato che qualcuno vi chiederà. Meglio arrivarci con un numero in mano che con un’alzata di spalle.":
        {'en': "Until yesterday a site’s environmental impact was a matter of sensibility. Recently it’s also an item that can end up in a balance sheet. The European directive on sustainability reporting — the CSRD — greatly widens the pool of companies that must report their environmental impacts, and those under the obligation extend it to their suppliers. If you work with or inside companies subject to the CSRD, a measurable, light site stops being a nicety and becomes a figure someone will ask you for. Better to get there with a number in hand than with a shrug."},
    "Diciamolo con onestà, come sempre: il nostro strumento dà una stima indicativa, non un audit certificato per una rendicontazione ufficiale. Ma è il primo passo giusto — vi dice dove siete e quanto margine avete, prima ancora di parlare con un consulente.":
        {'en': "Let’s say it honestly, as always: our tool gives an indicative estimate, not a certified audit for official reporting. But it’s the right first step — it tells you where you are and how much room you have, even before you talk to a consultant."},
    "La direttiva CSRD sulla rendicontazione di sostenibilità (EUR-Lex) →":
        {'en': "The CSRD directive on sustainability reporting (EUR-Lex) →"},
    "Cosa potete fare in un pomeriggio":
        {'en': "What you can do in an afternoon"},
    "Non serve rifare tutto per vedere il numero scendere. Le prime mosse sono semplici e rendono subito.":
        {'en': "You don’t have to redo everything to see the number drop. The first moves are simple and pay off right away."},
    "Alleggerite le immagini: convertitele in WebP o AVIF con caricamento differito. È quasi sempre l’intervento con il rapporto costo/beneficio più alto.":
        {'en': "Lighten the images: convert them to WebP or AVIF with lazy loading. It’s almost always the intervention with the highest cost/benefit ratio."},
    "Tagliate script e font superflui: ogni libreria di terze parti e ogni famiglia di caratteri in più è energia trasferita a ogni visita.":
        {'en': "Trim superfluous scripts and fonts: every third-party library and every extra font family is energy transferred on every visit."},
    "Sfruttate cache e CDN: evitano di ritrasferire gli stessi contenuti mille volte, meno traffico ripetuto e meno consumo.":
        {'en': "Use cache and a CDN: they avoid re-transferring the same content a thousand times — less repeated traffic and less consumption."},
    "Scegliete un hosting alimentato da rinnovabili: abbassa l’intensità di carbonio di ogni byte servito, con effetto immediato.":
        {'en': "Choose hosting powered by renewables: it lowers the carbon intensity of every byte served, with immediate effect."},
    "Misura gratis l’impronta di CO₂ del tuo sito →":
        {'en': "Measure your site’s CO₂ footprint for free →"},
    "Leggi anche: sito lento, le 7 cause reali (e quanto costa sistemarle) →":
        {'en': "Read also: a slow site, the 7 real causes (and what it costs to fix them) →"},
    "Il modello con cui si calcola l’impronta di CO₂ dal peso reale della pagina.":
        {'en': "The model used to calculate the CO₂ footprint from the page’s real weight."},
    "La libreria open source che traduce i byte trasferiti in grammi di CO₂ equivalente.":
        {'en': "The open-source library that turns transferred bytes into grams of CO₂ equivalent."},
    "Il testo ufficiale della rendicontazione di sostenibilità che allarga gli obblighi ambientali alle imprese.":
        {'en': "The official text of the sustainability reporting rules that extend environmental obligations to businesses."},
    "Dati reali sul peso delle pagine: dove si concentra davvero il consumo del web.":
        {'en': "Real data on page weights: where the web’s consumption really concentrates."},
    "Perché un sito leggero è anche veloce: le metriche che legano peso, velocità ed esperienza.":
        {'en': "Why a light site is also a fast one: the metrics that link weight, speed and experience."},
    "Misura ora l’impronta di CO₂ del tuo sito — gratis →":
        {'en': "Measure your site’s CO₂ footprint now — free →"},
    "Impatto ambientale sito web: dal peso della pagina in byte all’energia consumata e ai grammi di CO₂ per visita":
        {'en': "Website environmental impact: from page weight in bytes to energy consumed and grams of CO₂ per visit"},
    "Dal peso della pagina ai grammi di CO₂: byte trasferiti, energia consumata, emissioni per visita e stima annua col modello Sustainable Web Design":
        {'en': "From page weight to grams of CO₂: transferred bytes, energy consumed, emissions per visit and yearly estimate with the Sustainable Web Design model"},
    "C’è un documento di cui pochi parlano e che, dal 2025, molti siti devono avere: la dichiarazione di accessibilità. È la parte meno appariscente dell’adeguamento all’European Accessibility Act, e proprio per questo la più dimenticata — con una beffa dentro: un sito tecnicamente accessibile, ma senza dichiarazione pubblicata, resta comunque non a norma. In questa guida pratica vediamo cos’è la dichiarazione di accessibilità, cosa deve contenere per essere seria e non un copia-incolla, gli errori più comuni, e come si arriva a pubblicarla senza affidarsi a un punteggio automatico.":
        {'en': "There’s a document few talk about and that, since 2025, many sites must have: the accessibility statement. It’s the least conspicuous part of European Accessibility Act compliance, and for that very reason the most forgotten — with a twist inside: a technically accessible site, but without a published statement, is still not compliant. In this practical guide we look at what the accessibility statement is, what it must contain to be serious and not a copy-paste, the most common mistakes, and how you get to publishing it without relying on an automated score."},
    "Cos’è la dichiarazione di accessibilità (e perché è obbligatoria)":
        {'en': "What the accessibility statement is (and why it’s mandatory)"},
    "La dichiarazione di accessibilità è un documento pubblico in cui il sito dichiara, in chiaro, quanto è accessibile: quale standard applica, cosa funziona, cosa non è ancora a posto e a chi scrivere per segnalare un problema. Non è un attestato che vi date da soli per bellezza: è il modo in cui la norma vi chiede di prendere una posizione verificabile davanti a chi usa il sito, comprese le persone con disabilità.":
        {'en': "The accessibility statement is a public document in which the site states, plainly, how accessible it is: which standard it applies, what works, what isn’t right yet, and who to write to in order to report a problem. It isn’t a certificate you award yourself for show: it’s the way the law asks you to take a verifiable stance before those who use the site, including people with disabilities."},
    "L’obbligo nasce dall’European Accessibility Act — la direttiva europea 2019/882 — applicato in Italia dal 28 giugno 2025 per molti siti che vendono beni o servizi ai consumatori. Lo standard tecnico di riferimento sono le WCAG 2.1 di livello AA. E qui sta il punto che sorprende di più: la conformità non si esaurisce nel rendere il sito accessibile, chiede anche di dichiararlo. Senza il documento, il lavoro tecnico non basta.":
        {'en': "The obligation comes from the European Accessibility Act — EU Directive 2019/882 — applied in Italy since 28 June 2025 for many sites that sell goods or services to consumers. The technical reference standard is WCAG 2.1 level AA. And here’s the point that surprises most: compliance doesn’t end with making the site accessible, it also asks you to declare it. Without the document, the technical work isn’t enough."},
    "L’European Accessibility Act, il testo ufficiale (EUR-Lex) →":
        {'en': "The European Accessibility Act, the official text (EUR-Lex) →"},
    "Cosa deve contenere: l’anatomia di una dichiarazione seria":
        {'en': "What it must contain: the anatomy of a serious statement"},
    "Il World Wide Web Consortium, l’ente che scrive gli standard del web, indica cosa una dichiarazione dovrebbe sempre avere — e mette a disposizione perfino un generatore gratuito. Tradotto in pratica, gli elementi che non possono mancare sono pochi e chiari.":
        {'en': "The World Wide Web Consortium, the body that writes the web’s standards, sets out what a statement should always have — and even provides a free generator. Put into practice, the elements that can’t be missing are few and clear."},
    "L’impegno all’accessibilità: una frase che dichiara che vi rivolgete anche alle persone con disabilità, non un preambolo di circostanza.":
        {'en': "The commitment to accessibility: a sentence stating that you address people with disabilities too, not a token preamble."},
    "Lo standard applicato: quale livello WCAG (di norma 2.1 AA) avete preso come riferimento.":
        {'en': "The standard applied: which WCAG level (usually 2.1 AA) you took as your reference."},
    "Lo stato di conformità: cosa è accessibile e — onestà — quali parti non lo sono ancora, senza nascondere i limiti.":
        {'en': "The conformance status: what is accessible and — honesty — which parts aren’t yet, without hiding the limits."},
    "Un contatto per le segnalazioni: un indirizzo vero a cui una persona può scrivere se trova una barriera, con l’impegno a rispondere.":
        {'en': "A contact for reports: a real address a person can write to if they hit a barrier, with a commitment to reply."},
    "La data e l’aggiornamento: quando è stata redatta e revisionata, perché un sito cambia e la dichiarazione deve seguirlo.":
        {'en': "The date and updates: when it was drafted and reviewed, because a site changes and the statement has to follow it."},
    "I cinque elementi che una dichiarazione di accessibilità dovrebbe sempre avere: impegno, standard applicato, stato di conformità, parti non ancora accessibili e contatto per le segnalazioni, con data di redazione. Fonte: W3C/WAI, «Developing an Accessibility Statement».":
        {'en': "The five elements an accessibility statement should always have: commitment, standard applied, conformance status, parts not yet accessible, and a contact for reports, with the drafting date. Source: W3C/WAI, “Developing an Accessibility Statement.”"},
    "La guida e il generatore gratuito del W3C/WAI →":
        {'en': "The W3C/WAI guide and free generator →"},
    "Gli errori più comuni":
        {'en': "The most common mistakes"},
    "Le dichiarazioni che vediamo sbagliano quasi sempre negli stessi modi. Il primo: il copia-incolla scaricato da un altro sito, con dati che non c’entrano nulla — vale meno di niente, e in caso di controllo si nota subito. Il secondo: la dichiarazione «perfetta» che giura conformità totale mentre il sito è pieno di barriere, cioè una promessa che smentisce sé stessa alla prima prova. Il terzo: il gergo da avvocati e da tecnici, illeggibile per la persona a cui dovrebbe servire — «non soddisfa il criterio 1.2.2» invece di «i video non hanno i sottotitoli». Il quarto: nasconderla, così ben sepolta nel footer che nessuno la trova. Una dichiarazione onesta e imperfetta vale più di una perfetta e falsa.":
        {'en': "The statements we see go wrong almost always in the same ways. The first: the copy-paste downloaded from another site, with data that has nothing to do with it — worth less than nothing, and in an inspection it shows at once. The second: the “perfect” statement that swears total conformance while the site is full of barriers, that is, a promise that contradicts itself at the first test. The third: lawyer-and-technician jargon, unreadable for the person it should serve — “does not meet Success Criterion 1.2.2” instead of “the videos have no captions.” The fourth: hiding it, buried so deep in the footer that no one finds it. An honest, imperfect statement is worth more than a perfect, false one."},
    "Non basta un punteggio: la dichiarazione viene dopo l’audit":
        {'en': "A score isn’t enough: the statement comes after the audit"},
    "C’è un equivoco da smontare: «ho passato il test automatico, sono a posto». No. Un controllo automatico gratuito è un ottimo primo gradino — in un minuto scova contrasti, etichette e struttura — ma intercetta circa un terzo dei criteri WCAG: quello che una macchina sa misurare. Il resto — navigazione da tastiera, esperienza con uno screen reader, chiarezza dei contenuti — si verifica solo a mano. Una dichiarazione seria si scrive dopo un audit vero, non incollando il numero di uno strumento.":
        {'en': "There’s a misconception to dismantle: “I passed the automated test, I’m fine.” No. A free automated check is an excellent first step — in a minute it flags contrast, labels and structure — but it catches about a third of the WCAG criteria: what a machine can measure. The rest — keyboard navigation, screen-reader experience, content clarity — can only be checked by hand. A serious statement is written after a real audit, not by pasting a tool’s number."},
    "Per questo l’ordine giusto è preciso: prima l’audit, automatico e manuale; poi le correzioni; poi la dichiarazione che racconta con onestà il risultato; infine una verifica finale. Chi vi vende la dichiarazione senza l’audit vi sta vendendo una cornice senza il quadro.":
        {'en': "That’s why the right order is precise: first the audit, automated and manual; then the fixes; then the statement that honestly reports the result; finally a final verification. Whoever sells you the statement without the audit is selling you a frame without the picture."},
    "Guida EAA per il commercio online (Bird & Bird) →":
        {'en': "EAA guide for online retail (Bird & Bird) →"},
    "Come la prepariamo noi, in tre settimane":
        {'en': "How we prepare it, in three weeks"},
    "Nel nostro servizio la dichiarazione non è un foglio a parte, è l’ultimo passo di un percorso. Settimana 1: audit automatico e manuale, con il perimetro esatto delle barriere. Settimana 2: correzioni — contrasti, etichette dei moduli, gerarchia dei titoli, navigazione da tastiera. Settimana 3: redazione e pubblicazione della dichiarazione di accessibilità, e un audit di verifica che conferma lo standard WCAG 2.1 AA a correzioni fatte. Prezzo chiuso dopo l’audit, data in contratto con penale, come per ogni nostro lavoro.":
        {'en': "In our service the statement isn’t a separate sheet, it’s the last step of a path. Week 1: automated and manual audit, with the exact scope of the barriers. Week 2: fixes — contrast, form labels, heading hierarchy, keyboard navigation. Week 3: drafting and publishing the accessibility statement, and a verification audit confirming the WCAG 2.1 AA standard once fixes are done. Fixed price after the audit, date in the contract with a penalty, as with all our work."},
    "Se avete un e-commerce e volete capire prima cosa rischiate davvero — chi è obbligato, chi resta fuori, quali sanzioni — l’abbiamo raccontato a parte, senza allarmismi. La dichiarazione è il traguardo; ma il viaggio comincia dal sapere se, e quanto, l’obbligo vi riguarda.":
        {'en': "If you run an e-commerce and want to understand first what you really risk — who’s covered, who’s left out, what fines — we told it separately, without scaremongering. The statement is the finish line; but the journey starts from knowing whether, and how much, the obligation concerns you."},
    "Leggi anche: EAA 2026, cosa rischia davvero il vostro e-commerce →":
        {'en': "Read also: EAA 2026, what your e-commerce site really risks →"},
    "La guida ufficiale del W3C, con un generatore gratuito: cosa una dichiarazione deve contenere.":
        {'en': "The official W3C guide, with a free generator: what a statement must contain."},
    "Il testo dell’European Accessibility Act: da qui nasce l’obbligo, dichiarazione compresa.":
        {'en': "The text of the European Accessibility Act: the source of the obligation, the statement included."},
    "Lo standard tecnico di riferimento (livello AA) che la dichiarazione deve citare.":
        {'en': "The technical reference standard (level AA) the statement must cite."},
    "Il centro di competenza UE sull’accessibilità: conferma l’entrata in vigore del 28 giugno 2025.":
        {'en': "The EU accessibility competence center: it confirms the entry into force on 28 June 2025."},
    "Uno studio legale internazionale spiega perimetro, esenzioni e obblighi per chi vende online.":
        {'en': "An international law firm explains scope, exemptions and obligations for those who sell online."},
    "Dichiarazione di accessibilità: il documento richiesto dall’European Accessibility Act, cosa deve contenere e dove pubblicarlo":
        {'en': "Accessibility statement: the document required by the European Accessibility Act, what it must contain and where to publish it"},
    "L’anatomia di una dichiarazione di accessibilità: impegno, standard WCAG 2.1 AA, stato di conformità, parti non accessibili, contatto e data":
        {'en': "The anatomy of an accessibility statement: commitment, WCAG 2.1 AA standard, conformance status, parts not accessible, contact and date"},
    "Guida: quanto pesa il vostro sito sull’ambiente (e sul portafoglio) →":
        {'en': "Guide: how much your site weighs on the environment (and on your wallet) →"},
    "Guida pratica: la dichiarazione di accessibilità nel 2026 →":
        {'en': "Practical guide: the accessibility statement in 2026 →"},
    # Fix (17.07): titolo dell'articolo (H1 + riga in blog-index) senza
    # parola in ITALIAN_HINT — non intercettato dal report del conveyor,
    # stesso tipo di falso negativo già corretto per altri titoli in
    # "Batch 3 — fix" più sotto.
    "Dichiarazione di accessibilità: guida pratica 2026":
        {'en': "Accessibility statement: a practical 2026 guide"},
}
CHROME.update(CHROME_BLOG_BATCH2)


# Prezzo lancio — promo sui primi 5 progetti (titolare, 15.07.2026). Solo
# 'en': il RU si scrive a mano (translate_pages.py ru è vietato). I prezzi
# stessi (es. "€ 1.900–2.800") non servono qui: sono nodi di testo puramente
# numerici, il traduttore li lascia intatti e la conversione al formato
# US (virgola/punto) avviene comunque nel passo us_numbers() a valle.
CHROME_LANCIO = {
    'PREZZO LANCIO — PRIMI 5 PROGETTI': {'en': 'LAUNCH PRICE — FIRST 5 PROJECTS'},
    'Prezzo lancio sui primi 5 progetti: stesso contratto, stesse garanzie. Listino pieno dal 2027.': {
        'en': 'Launch price on our first 5 projects: same contract, same guarantees. Full price list from 2027.'},
    'Ne restano {{lancio_slots}} su 5.': {'en': '{{lancio_slots}} of 5 slots still open.'},
}
CHROME.update(CHROME_LANCIO)

# Catalogo casi studio reali (docs/copy-casi-studio.md, generate_pages.py
# build_casi_studio_index()): microcopy del template — intro, filtro a chip,
# CTA delle 11 schede, blocco finale. I testi delle singole carte (titolo/
# problema/soluzione/risultato/alt/didascalie shot) sono nel corpus CASES,
# non qui — questo è solo lo scheletro riutilizzabile della pagina.
CHROME_CASI_STUDIO = {
    'Non un portfolio di clienti. I sistemi che abbiamo costruito per noi': {
        'en': 'Not a client portfolio. The systems we built for ourselves'},
    "Molte web agency mostrano loghi di clienti. Il gruppo Remarka lavora con le lingue dal 2001 — e dallo stesso anno costruisce siti: già nel 2002–2003 ne realizzava per aziende terze, e alcuni sono online ancora oggi (directindustry.com.ru · ivextrans.eu · beltran.by). Da allora abbiamo realizzato oltre 160 progetti; 28 sono oggi in manutenzione continua presso di noi. Studio Remarka è la vetrina nuova di questo lavoro, non il suo inizio.": {
        'en': "Most web agencies show off client logos. The Remarka group has worked with languages since 2001 — and has been building websites since that same year: as early as 2002–2003 it was delivering sites for outside companies, some still online today (directindustry.com.ru · ivextrans.eu · beltran.by). Since then: over 160 projects delivered, 28 currently under our continuous maintenance. Studio Remarka is this work's new storefront, not its beginning."},
    'Qui sotto trovate i sistemi che il gruppo ha costruito per sé: per gestire il proprio lavoro, portare i propri servizi su Google, vendere in più lingue. Li usiamo ogni giorno, con i nostri soldi e la nostra reputazione in gioco — e quando lavorate con noi ricevete la stessa ingegneria. Ogni caso ha un link al progetto vivo: potete aprirlo, provarlo, misurarlo da soli. Nessun cliente inventato, nessun numero non verificabile.': {
        'en': "Below are the systems the group built for itself: to run our own operations, rank our own services on Google, sell in several languages. We use them every day, with our own money and reputation on the line — and when you work with us you get the same engineering. Every case links to the live project: open it, test it, measure it yourself. No invented clients, no numbers you can't check."},
    'Ogni scheda porta al progetto online. I punteggi e le metriche sono verificabili sul posto.': {
        'en': 'Every card opens the live project. Scores and metrics are verifiable on the spot.'},
    'Tutti i progetti': {'en': 'All projects'},
    'Siti aziendali e vetrina': {'en': 'Business & brochure sites'},
    'Web app e prodotti': {'en': 'Web apps & products'},
    'SEO tecnica e contenuti': {'en': 'Technical SEO & content'},
    'Restyling e marketing': {'en': 'Redesign & marketing'},
    '11 progetti del gruppo · filtra per tipo di lavoro': {'en': '11 group projects · filter by type of work'},
    'Un sito aziendale come questo →': {'en': 'A business website like this one →'},
    'Una web app su misura per la vostra azienda →': {'en': 'A custom web app for your company →'},
    'Una Mini App o PWA per il vostro pubblico →': {'en': 'A Mini App or PWA for your audience →'},
    'SEO tecnica e siti multilingue →': {'en': 'Technical SEO and multilingual sites →'},
    'SEO tecnica per progetti di contenuto →': {'en': 'Technical SEO for content projects →'},
    'Restyling e idee di marketing per il vostro sito →': {'en': 'Redesign and marketing ideas for your site →'},
    'SEO tecnica che porta risultati →': {'en': 'Technical SEO that delivers →'},
    'Un sito vetrina per la vostra attività →': {'en': 'A brochure site for your business →'},
    'Restyling e nuovo design per il vostro sito →': {'en': 'Redesign and new design for your site →'},
    'Una web app su misura per il vostro processo →': {'en': 'A custom web app for your process →'},
    'Contenuti nativi in più lingue per il vostro sito →': {'en': 'Native content in several languages for your site →'},
    'Il prossimo sistema possiamo costruirlo per voi': {'en': 'The next system, we can build for you'},
    'Prima misuriamo cosa avete oggi, poi vi diciamo — con numeri e con una data in contratto — cosa possiamo fare.': {
        'en': 'First we measure what you have today, then we tell you — with numbers and a date in the contract — what we can do.'},
    'Richiedi un preventivo in 24 ore': {'en': 'Get a quote in 24 hours'},
    'Guarda tutti i servizi': {'en': 'See all services'},
    'Dal nostro catalogo': {'en': 'From our own catalogue'},
}
CHROME.update(CHROME_CASI_STUDIO)

# CHROME_BLOG_BATCH3 — Blog · Batch 3 (5 articoli IT → EN) + i due backlink
# aggiunti nei tool test-velocita / segnali-eeat. Copre ogni nodo di testo
# generato da build_blog_post (titoli, lead, corpo, liste, alt/didascalie SVG,
# link contestuali e CTA con « →», etichette e note del blocco «Fonti»).
# Solo EN: il blog RU e' un batch a se'. Numeri in formato US.
CHROME_BLOG_BATCH3 = {
    "17 LUG 2026": {"en": "17 JUL 2026"},

    # ---- Articolo 11 · Telegram Mini App ----
    "Telegram Mini App per il business: il canale che l’Italia ignora":
        {"en": "Telegram Mini Apps for business: the channel Italy is ignoring"},
    "Un’app dentro Telegram, senza scaricare niente: ordini, prenotazioni e assistenza dove i clienti già scrivono. Cos’è una Telegram Mini App, quando conviene e perché in Italia quasi nessuno la usa.":
        {"en": "An app inside Telegram, with nothing to download: orders, bookings and support where your customers already write. What a Telegram Mini App is, when it pays off, and why almost nobody in Italy uses one."},
    "Un cliente vi scrive su Telegram per prenotare, come fa ogni settimana. Stavolta però, invece dei soliti quattro messaggi per mettersi d’accordo sull’orario, tocca un pulsante dentro la chat: si apre una piccola schermata, sceglie il giorno, conferma e ha chiuso — senza uscire da Telegram, senza installare nessuna app. Quella schermata è una Telegram Mini App, e per un’azienda è un canale che in Italia quasi nessuno usa ancora. Vediamo cos’è, quando conviene davvero al vostro business e perché il gruppo Remarka ne ha costruita una per il proprio lavoro, con numeri veri e non promesse.":
        {"en": "A customer messages you on Telegram to book, like every week. This time, though, instead of the usual four messages to settle on a time, they tap a button inside the chat: a small screen opens, they pick the day, confirm, and they’re done — without leaving Telegram, without installing any app. That screen is a Telegram Mini App, and for a business it’s a channel almost nobody in Italy uses yet. Let’s see what it is, when it really pays off for your business, and why the Remarka group built one for its own work — with real numbers, not promises."},
    "Che cos’è una Telegram Mini App (e cosa non è)":
        {"en": "What a Telegram Mini App is (and what it isn’t)"},
    "Una Telegram Mini App è, in una riga, un’app web che si apre dentro Telegram. Tecnicamente è un sito — fatto delle stesse cose di qualsiasi sito, pagine e codice — che Telegram mostra a tutto schermo dentro la chat quando l’utente tocca un pulsante. Non si scarica dallo store, non occupa memoria, non chiede aggiornamenti: vive a un tocco di distanza dalla conversazione. La documentazione ufficiale di Telegram la descrive proprio così, come un’interfaccia web che può sostituire del tutto un sito, ma dentro l’app di messaggistica.":
        {"en": "A Telegram Mini App is, in one line, a web app that opens inside Telegram. Technically it’s a website — made of the same things as any site, pages and code — that Telegram shows full-screen inside the chat when the user taps a button. There’s nothing to download from a store, it takes no memory, it asks for no updates: it lives one tap away from the conversation. Telegram’s official documentation describes it exactly this way, as a web interface that can completely replace a website, but inside the messaging app."},
    "Serve distinguerla da due cose che le somigliano. Un bot Telegram risponde a comandi e messaggi di testo: utile, ma resta una conversazione a domande e risposte. Un’app nativa, quella dello store, è potente ma costa cara, va scaricata e mantenuta due volte per iOS e Android. La Mini App sta nel mezzo e prende il meglio: l’interfaccia ricca di un’app, ma dentro Telegram e senza installare niente. È il posto giusto quando l’interazione deve essere più di un messaggio, ma non merita un’app da scaricare.":
        {"en": "It helps to tell it apart from two things it resembles. A Telegram bot replies to commands and text messages: useful, but it stays a question-and-answer conversation. A native app, the kind from the store, is powerful but expensive, has to be downloaded and maintained twice for iOS and Android. The Mini App sits in the middle and takes the best of both: the rich interface of an app, but inside Telegram and with nothing to install. It’s the right place when the interaction has to be more than a message, yet doesn’t deserve an app to download."},
    "Quattro modi di stare online: il sito nel browser, l’app nativa nello store, il bot come chat di testo e la Mini App — un’app vera dentro Telegram, senza installare niente. Fonte: documentazione ufficiale Telegram, Mini Apps.":
        {"en": "Four ways to be online: the website in the browser, the native app in the store, the bot as a text chat, and the Mini App — a real app inside Telegram, with nothing to install. Source: Telegram official documentation, Mini Apps."},
    "La forza di una Mini App non è tecnica, è di posizione: sta dove le persone già sono. Telegram ha superato il miliardo di utenti attivi al mese nel 2025, e per molte attività — soprattutto quelle che parlano con clienti abituali — la chat è già il canale dove arrivano richieste e prenotazioni. Portare lì dentro un’interfaccia vera significa togliere l’attrito peggiore: quello di far uscire il cliente dalla conversazione per aprire un sito, cercare la pagina, fare login.":
        {"en": "A Mini App’s strength isn’t technical, it’s about position: it sits where people already are. Telegram passed one billion monthly active users in 2025, and for many businesses — especially those that talk to regular customers — the chat is already the channel where requests and bookings come in. Bringing a real interface in there removes the worst friction of all: pushing the customer out of the conversation to open a website, find the page, log in."},
    "C’è di più della sola comodità. La piattaforma di Telegram dà alle Mini App strumenti da vero prodotto: pagamenti integrati, notifiche mirate, autenticazione dell’utente senza moduli da compilare. Sono i mattoni con cui si costruisce un canale che non solo informa, ma vende e fa restare. Ed è qui che si apre lo spazio che il titolo chiama «il canale che l’Italia ignora»: tra le PMI italiane le Mini App sono ancora rarissime — non per un limite tecnico, ma perché quasi nessuno le propone. Chi arriva prima trova un terreno quasi vuoto.":
        {"en": "There’s more than convenience. Telegram’s platform gives Mini Apps real-product tools: built-in payments, targeted notifications, user authentication with no forms to fill in. These are the bricks for a channel that doesn’t just inform, but sells and keeps people. And this is where the space the title calls “the channel Italy is ignoring” opens up: among Italian SMBs Mini Apps are still extremely rare — not for a technical limit, but because almost nobody offers them. Whoever gets there first finds an almost empty field."},
    "Un caso reale: il nostro gestionale, dentro Telegram":
        {"en": "A real case: our management system, inside Telegram"},
    "Non lo diciamo in teoria: una Mini App l’abbiamo costruita per noi. Il gruppo Remarka gestisce le traduzioni con un sistema interno (un TMS), e traduttori e project manager vivono nelle chat più che alle scrivanie. Aprire il gestionale dal browser solo per controllare lo stato di un ordine era troppo, ogni volta. Così abbiamo portato le funzioni chiave del sistema dentro una Telegram Mini App: ordini, stati e notifiche direttamente in chat, con la stessa logica del pannello web.":
        {"en": "We don’t say it in theory: we built a Mini App for ourselves. The Remarka group runs its translations on an internal system (a TMS), and translators and project managers live in chats more than at desks. Opening the management system in a browser just to check an order’s status was too much, every time. So we brought the system’s key functions into a Telegram Mini App: orders, statuses and notifications right in the chat, with the same logic as the web dashboard."},
    "I numeri sono piccoli e veri, e li diamo così come sono: la Mini App è stata sviluppata in due settimane e oggi gestisce oltre dieci utenti e ordini al giorno. Il gestionale entra in tasca — niente app da installare, niente login da browser — e sta dove il team già lavora. È esattamente il tipo di prodotto che sappiamo costruire quando l’interfaccia deve stare dove sono già le persone, e la stessa ingegneria che mettiamo in una web app su misura per voi.":
        {"en": "The numbers are small and real, and we give them as they are: the Mini App was built in two weeks and today handles over ten users and orders a day. The management system fits in your pocket — no app to install, no browser login — and lives where the team already works. It’s exactly the kind of product we know how to build when the interface has to be where people already are, and the same engineering we put into a custom web app for you."},
    "Il caso completo, con il link al progetto vivo →":
        {"en": "The full case, with a link to the live project →"},
    "Una web app o Mini App su misura per la vostra azienda →":
        {"en": "A custom web app or Mini App for your company →"},
    "Quando conviene al vostro business (e quando no)":
        {"en": "When it pays off for your business (and when it doesn’t)"},
    "Onestà prima dell’entusiasmo: una Mini App non serve a tutti. Conviene quando ricorrono certe condizioni, e in quei casi è spesso la scelta più intelligente — più economica e più rapida di un’app nativa.":
        {"en": "Honesty before enthusiasm: a Mini App isn’t for everyone. It pays off when certain conditions recur, and in those cases it’s often the smartest choice — cheaper and faster than a native app."},
    "I vostri clienti sono già su Telegram e vi scrivono lì: un ristorante che prende prenotazioni, uno studio che fissa appuntamenti, un negozio con clienti abituali.":
        {"en": "Your customers are already on Telegram and write to you there: a restaurant taking bookings, a practice setting appointments, a shop with regular customers."},
    "L’interazione è ricorrente e va oltre il testo: scegliere una data, sfogliare un catalogo, controllare lo stato di un ordine, pagare.":
        {"en": "The interaction is recurring and goes beyond text: picking a date, browsing a catalogue, checking an order’s status, paying."},
    "Non c’è budget per un’app nativa da mantenere su due store: la Mini App è una sola, e vive dove vive Telegram.":
        {"en": "There’s no budget for a native app to maintain on two stores: the Mini App is a single one, and lives where Telegram lives."},
    "E quando non conviene? Se il vostro pubblico non usa Telegram, la porta si apre su una stanza vuota: il canale giusto è un altro. Se il prodotto ha bisogno di funzioni profonde del telefono — fotocamera avanzata, sensori, elaborazione pesante offline — o se la presenza nello store è essa stessa parte del marchio, allora l’app nativa ha un senso che una Mini App non copre. Fuori da questi casi, però, si finisce spesso a pagare un’app da migliaia di euro per fare ciò che una Mini App farebbe con una frazione della spesa.":
        {"en": "And when doesn’t it pay off? If your audience doesn’t use Telegram, the door opens onto an empty room: the right channel is another one. If the product needs deep phone functions — advanced camera, sensors, heavy offline processing — or if the store presence is itself part of the brand, then the native app makes a sense a Mini App doesn’t cover. Outside these cases, though, you often end up paying for an app worth thousands of euros to do what a Mini App would do for a fraction of the cost."},
    "Il primo passo non è tecnico, è una domanda: dove sono già i vostri clienti, e cosa vorrebbero fare senza dover cambiare app? Da lì si disegna l’interazione essenziale — poche schermate, un’azione chiara — e la si collega ai sistemi che già usate. Una Mini App resta comunque web, e sul web la velocità conta: vale la pena misurarne le prestazioni fin dall’inizio, come per qualsiasi sito. E se volete capire prima se il vostro pubblico è pronto anche per un’app installabile senza store, il confronto tra PWA e app nativa lo abbiamo raccontato a parte.":
        {"en": "The first step isn’t technical, it’s a question: where are your customers already, and what would they like to do without switching apps? From there you design the essential interaction — a few screens, one clear action — and connect it to the systems you already use. A Mini App is still web, and on the web speed matters: it’s worth measuring its performance from the start, as with any site. And if you first want to understand whether your audience is ready for an installable app without a store too, we’ve covered the PWA versus native app comparison separately."},
    "Progettiamo la vostra web app o Mini App su misura →":
        {"en": "We design your custom web app or Mini App →"},
    "Misura gratis la velocità del vostro sito →":
        {"en": "Measure your site’s speed for free →"},
    "Leggi anche: PWA per le PMI, quando l’app non serve →":
        {"en": "Read also: PWAs for SMBs, when the app isn’t needed →"},
    "Telegram — Mini Apps per sviluppatori":
        {"en": "Telegram — Mini Apps for developers"},
    "La documentazione ufficiale: cos’è una Mini App e come si costruisce dentro Telegram.":
        {"en": "The official documentation: what a Mini App is and how to build one inside Telegram."},
    "Telegram — la piattaforma delle Mini App":
        {"en": "Telegram — the Mini Apps platform"},
    "Come le Mini App si integrano in Telegram: avvio, autorizzazione, notifiche e pagamenti.":
        {"en": "How Mini Apps integrate into Telegram: launch, authorisation, notifications and payments."},
    "Telegram — la piattaforma dei bot":
        {"en": "Telegram — the bot platform"},
    "Le fondamenta su cui poggiano bot e Mini App: cosa un’azienda può automatizzare in chat.":
        {"en": "The foundations bots and Mini Apps rest on: what a business can automate in chat."},
    "TechCrunch — Telegram supera il miliardo di utenti (2025)":
        {"en": "TechCrunch — Telegram passes one billion users (2025)"},
    "Il dato sulla scala del canale: oltre un miliardo di utenti attivi al mese.":
        {"en": "The figure on the channel’s scale: over one billion monthly active users."},
    "Progettiamo la vostra web app su misura, a prezzo chiuso →":
        {"en": "We design your custom web app, at a fixed price →"},
    "Telegram Mini App per il business: un’app che si apre dentro la chat, senza installare niente":
        {"en": "Telegram Mini App for business: an app that opens inside the chat, with nothing to install"},
    "Telegram Mini App per il business a confronto con bot, sito web e app nativa: dove vive e cosa serve per usarla":
        {"en": "Telegram Mini App for business compared with bot, website and native app: where it lives and what it takes to use it"},

    # ---- Articolo 12 · Gestionale su misura vs Excel ----
    "Gestionale su misura vs Excel: quando conviene il salto":
        {"en": "Custom management software vs Excel: when the leap pays off"},
    "Excel regge finché non vi frena: ordini persi tra fogli ed email, errori che nessuno vede, dati che non tornano. Quando conviene passare a un gestionale su misura, con un caso reale e i numeri.":
        {"en": "Excel holds up until it holds you back: orders lost between sheets and email, errors nobody sees, figures that don’t add up. When it pays to move to custom management software, with a real case and the numbers."},
    "«Con Excel ce la caviamo.» È vero, fino a un certo punto. Il foglio di calcolo è geniale finché l’attività è piccola: costa zero, lo sanno usare tutti, si piega a qualsiasi esigenza. Poi cresce il numero di ordini, di clienti, di persone che mettono mano allo stesso file — e quello che era una comodità diventa un collo di bottiglia: la versione giusta che non si trova, la riga sovrascritta per sbaglio, l’ordine sparito tra un foglio e una mail. A quel punto la domanda non è più «Excel o no», ma quando conviene passare a un gestionale su misura. In questo articolo proviamo a rispondere con onestà — e con un caso reale del gruppo Remarka, numeri compresi.":
        {"en": "“We get by with Excel.” True, up to a point. The spreadsheet is brilliant while the business is small: it costs nothing, everyone knows how to use it, it bends to any need. Then the number of orders, of clients, of people touching the same file grows — and what was a convenience becomes a bottleneck: the right version that can’t be found, the row overwritten by mistake, the order vanished between a sheet and an email. At that point the question is no longer “Excel or not,” but when it pays to move to custom management software. In this article we try to answer honestly — and with a real case from the Remarka group, numbers included."},
    "Perché Excel regge — finché non vi frena":
        {"en": "Why Excel holds up — until it holds you back"},
    "Il foglio di calcolo non è il nemico: è il punto di partenza giusto per quasi tutti. Un’attività che segue venti ordini al mese non ha bisogno di un sistema, ha bisogno di una tabella — ed Excel, o un foglio condiviso, la fa benissimo. Il problema non è lo strumento, è la soglia oltre la quale lo strumento smette di aiutare e comincia a rallentare. Quella soglia arriva quasi sempre insieme a tre segnali: più persone lavorano sullo stesso file, i dati diventano tanti, e le stesse informazioni vanno ricopiate da un foglio all’altro.":
        {"en": "The spreadsheet isn’t the enemy: it’s the right starting point for almost everyone. A business handling twenty orders a month doesn’t need a system, it needs a table — and Excel, or a shared sheet, does it perfectly. The problem isn’t the tool, it’s the threshold past which the tool stops helping and starts slowing you down. That threshold almost always arrives with three signs: more people working on the same file, the data growing large, and the same information having to be copied from one sheet to another."},
    "Ed è qui che nasce il rischio silenzioso. Il gruppo di ricerca europeo che studia i rischi dei fogli di calcolo — l’EuSpRIG — stima che oltre il 90% dei fogli usati in azienda contenga errori, e che circa la metà di quelli operativi abbia difetti concreti. Non perché chi li compila sia sbadato, ma perché un foglio non avvisa quando una formula si rompe o una riga viene sovrascritta: l’errore resta lì, invisibile, finché non costa qualcosa.":
        {"en": "And this is where the silent risk begins. The European research group that studies spreadsheet risks — EuSpRIG — estimates that over 90% of spreadsheets used in business contain errors, and that around half of those used operationally have real defects. Not because whoever fills them in is careless, but because a spreadsheet doesn’t warn you when a formula breaks or a row is overwritten: the error stays there, invisible, until it costs something."},
    "I costi nascosti dei fogli di calcolo":
        {"en": "The hidden costs of spreadsheets"},
    "Il prezzo di Excel non è nella licenza, è nel tempo e negli errori. Prendiamo i sintomi più comuni, quelli che ogni azienda cresciuta con i fogli riconosce al volo.":
        {"en": "Excel’s price isn’t in the licence, it’s in time and errors. Take the most common symptoms, the ones every company grown on spreadsheets recognises at a glance."},
    "La versione giusta che non si trova: «ordini_finale_v3_DEF_buono.xlsx» è una barzelletta che tutti hanno vissuto — e ogni copia è un dato che diverge dagli altri.":
        {"en": "The right version that can’t be found: “orders_final_v3_DEF_good.xlsx” is a joke everyone has lived — and every copy is data that drifts from the rest."},
    "Il lavoro perso tra fogli ed email: un ordine confermato in una chat, un preventivo in un altro file, una scadenza nella testa di una persona sola. Basta che quella persona sia in ferie.":
        {"en": "Work lost between sheets and email: an order confirmed in a chat, a quote in another file, a deadline in one person’s head alone. All it takes is for that person to be on holiday."},
    "Gli errori che nessuno vede: una formula trascinata male, un incolla sulla cella sbagliata, un totale che non torna e che nessuno controlla perché «è sempre andato bene».":
        {"en": "The errors nobody sees: a formula dragged wrong, a paste into the wrong cell, a total that doesn’t add up and that nobody checks because “it’s always been fine.”"},
    "L’assenza di ruoli: tutti possono cambiare tutto, senza traccia di chi ha modificato cosa e quando.":
        {"en": "The absence of roles: everyone can change everything, with no trace of who changed what, and when."},
    "A sinistra il lavoro sparso tra fogli, email e teste delle persone; a destra un gestionale su misura dove ordini, clienti, scadenze e ruoli vivono in un solo sistema. Fonte del dato sugli errori: EuSpRIG, ricerca sui fogli di calcolo.":
        {"en": "On the left, work scattered across sheets, email and people’s heads; on the right, custom management software where orders, clients, deadlines and roles live in a single system. Source for the error figure: EuSpRIG, spreadsheet research."},
    "Quando conviene il salto a un gestionale su misura":
        {"en": "When the leap to custom management software pays off"},
    "Nessuno di questi problemi è drammatico da solo. Insieme, però, formano una tassa quotidiana sul tempo del team — e ogni tanto un errore che finisce in fattura o in una consegna saltata. Le cronache raccolte dall’EuSpRIG sono piene di casi in cui un singolo sbaglio di foglio è costato bilanci da rifare e numeri sbagliati presi per buoni. Il momento giusto per il salto non è una dimensione, è un insieme di sintomi: se ne riconoscete tre o più, il foglio ha finito di aiutarvi.":
        {"en": "None of these problems is dramatic on its own. Together, though, they form a daily tax on the team’s time — and every so often an error that ends up on an invoice or in a missed delivery. The records collected by EuSpRIG are full of cases where a single spreadsheet mistake cost restated accounts and wrong numbers taken as true. The right moment for the leap isn’t a size, it’s a set of symptoms: if you recognise three or more, the spreadsheet has finished helping you."},
    "Più persone lavorano sugli stessi dati contemporaneamente, e vi trovate a fondere versioni a mano.":
        {"en": "Several people work on the same data at the same time, and you find yourselves merging versions by hand."},
    "Le stesse informazioni vanno ricopiate da un posto all’altro — dal preventivo all’ordine, dall’ordine alla fattura — con il rischio di errore a ogni passaggio.":
        {"en": "The same information has to be copied from one place to another — from quote to order, from order to invoice — with the risk of error at every step."},
    "Vi servono ruoli diversi: chi vede tutto, chi solo la propria parte, chi non deve toccare i prezzi.":
        {"en": "You need different roles: who sees everything, who only their own part, who mustn’t touch the prices."},
    "Volete sapere in ogni momento lo stato di ogni pratica, senza aprire cinque file e chiedere a tre persone.":
        {"en": "You want to know the status of every case at any moment, without opening five files and asking three people."},
    "State perdendo ordini o scadenze perché l’informazione vive nella testa di qualcuno, non in un sistema.":
        {"en": "You’re losing orders or deadlines because the information lives in someone’s head, not in a system."},
    "Un caso reale: il sistema che manda avanti un’agenzia":
        {"en": "A real case: the system that runs an agency"},
    "Attenzione: «gestionale su misura» non vuol dire per forza un progetto enorme. Vuol dire un sistema costruito sul vostro modo di lavorare, invece di piegare il lavoro a un software preconfezionato che fa il 70% di ciò che serve e vi obbliga al restante 30% a mano. Anche qui parliamo di ciò che abbiamo costruito per noi. Gestire centinaia di ordini di traduzione — clienti, traduttori, scadenze, preventivi, fatture — con fogli ed email era diventato il collo di bottiglia che rompeva le consegne.":
        {"en": "Careful: “custom management software” doesn’t necessarily mean a huge project. It means a system built around your way of working, instead of bending the work to off-the-shelf software that does 70% of what you need and forces you to do the remaining 30% by hand. Here too we’re talking about what we built for ourselves. Running hundreds of translation orders — clients, translators, deadlines, quotes, invoices — on sheets and email had become the bottleneck that broke deliveries."},
    "Così il gruppo Remarka ha costruito un TMS, un gestionale su misura dove ogni ordine ha uno stato, ogni cliente una scheda, ogni traduttore un carico e ogni lavoro la sua fattura: bacheca degli ordini, anagrafiche, preventivi e contabilità in un’unica web app. I numeri, reali: il sistema è in produzione da due anni e gestisce 180 ordini al mese, oltre 2.000 l’anno. Dentro ci lavorano 2 amministratori, 8 project manager e 4 agenzie partner con la propria base clienti — e gli ordini non si perdono più tra le email. È la stessa ingegneria che mettiamo in una web app su misura per la vostra azienda.":
        {"en": "So the Remarka group built a TMS, custom management software where every order has a status, every client a record, every translator a workload, and every job its invoice: order board, contacts, quotes and accounting in a single web app. The numbers, real: the system has been in production for two years and handles 180 orders a month, over 2,000 a year. Inside it work 2 administrators, 8 project managers and 4 partner agencies with their own client base — and orders no longer get lost in email. It’s the same engineering we put into custom web software for your company."},
    "Una web app gestionale su misura per voi →":
        {"en": "A custom management web app for you →"},
    "Prima di decidere: due domande e un numero":
        {"en": "Before deciding: two questions and one number"},
    "Non serve rifare tutto domani. Prima di parlare di un gestionale, fatevi due domande oneste: quante ore alla settimana il team spende a sistemare, cercare e ricopiare dati tra fogli ed email? E quante volte, nell’ultimo anno, un errore o un’informazione persa vi è costato un cliente, una consegna o una figuraccia? Se le risposte vi mettono a disagio, il conto del «gratis» di Excel è più salato di quanto sembri.":
        {"en": "You don’t need to redo everything tomorrow. Before talking about a management system, ask yourselves two honest questions: how many hours a week does the team spend fixing, searching and re-copying data between sheets and email? And how many times, in the past year, has an error or a lost piece of information cost you a client, a delivery or an embarrassment? If the answers make you uncomfortable, the bill for Excel’s “free” is steeper than it looks."},
    "Il passo successivo è mappare il flusso reale — come nasce un ordine, chi lo tocca, dove si incaglia — e capire quali passaggi un sistema su misura può togliere. Da lì esce un progetto con un prezzo chiuso, non un salto nel buio. E se il vostro lavoro vive già dentro le chat, val la pena sapere che quel gestionale può entrare anche dentro Telegram, in tasca al team.":
        {"en": "The next step is to map the real flow — how an order is born, who touches it, where it gets stuck — and work out which steps a custom system can remove. Out of that comes a project with a fixed price, not a leap in the dark. And if your work already lives inside chats, it’s worth knowing that management system can go inside Telegram too, in the team’s pocket."},
    "Progettiamo il vostro gestionale su misura, a prezzo chiuso →":
        {"en": "We design your custom management software, at a fixed price →"},
    "Misura la salute tecnica del vostro sito attuale →":
        {"en": "Measure the technical health of your current site →"},
    "Leggi anche: la Telegram Mini App, il gestionale in tasca →":
        {"en": "Read also: the Telegram Mini App, the management system in your pocket →"},
    "EuSpRIG — ricerca sui rischi dei fogli di calcolo":
        {"en": "EuSpRIG — research on spreadsheet risks"},
    "Il gruppo europeo che studia gli errori nei fogli: oltre il 90% ne contiene, metà di quelli operativi ha difetti.":
        {"en": "The European group that studies spreadsheet errors: over 90% contain them, half of those used operationally have defects."},
    "EuSpRIG — le «horror stories» dei fogli di calcolo":
        {"en": "EuSpRIG — the spreadsheet “horror stories”"},
    "Casi reali in cui un errore di Excel è costato bilanci sbagliati e decisioni prese su numeri falsi.":
        {"en": "Real cases where an Excel error cost wrong accounts and decisions made on false numbers."},
    "Gestire dati di clienti sparsi tra fogli ed email è anche un rischio di protezione dei dati: un sistema con ruoli lo riduce.":
        {"en": "Managing client data scattered across sheets and email is also a data-protection risk: a system with roles reduces it."},
    "Gestionale su misura contro Excel: da fogli di calcolo sparsi a un unico sistema con ordini, clienti e ruoli":
        {"en": "Custom management software versus Excel: from scattered spreadsheets to a single system with orders, clients and roles"},
    "Da Excel e email sparsi a un gestionale su misura: ordini, clienti, scadenze e ruoli in un unico sistema":
        {"en": "From scattered Excel and email to custom management software: orders, clients, deadlines and roles in a single system"},

    # ---- Articolo 13 · Dati strutturati schema.org ----
    "Schema.org per le PMI: i dati strutturati che Google premia":
        {"en": "Schema.org for SMEs: the structured data Google rewards"},
    "I dati strutturati raccontano il vostro sito a Google in una lingua che capisce: prezzi, orari, recensioni, eventi. Cosa sono, come funziona schema.org e quali risultati ricchi potete ottenere.":
        {"en": "Structured data tells Google about your site in a language it understands: prices, opening hours, reviews, events. What it is, how schema.org works, and which rich results you can get."},
    "Cercate su Google il nome di un ristorante e, prima ancora di aprire il sito, vedete già le stelline delle recensioni, l’orario di apertura, la fascia di prezzo. Cercate una ricetta e compaiono i tempi di cottura e la foto. Non è magia né fortuna: quei siti hanno detto a Google, in modo esplicito, cosa contengono — usando i dati strutturati di schema.org. È uno degli strumenti più sottovalutati dalle PMI italiane, eppure è tra i pochi che potete aggiungere senza riscrivere il sito e con un effetto visibile nei risultati. Vediamo cosa sono i dati strutturati schema.org, come funzionano e cosa Google ci fa davvero.":
        {"en": "Search Google for a restaurant’s name and, before you even open the site, you already see the review stars, the opening hours, the price range. Search for a recipe and the cooking times and the photo appear. It isn’t magic or luck: those sites told Google, explicitly, what they contain — using schema.org structured data. It’s one of the most underrated tools among Italian SMEs, yet one of the few you can add without rewriting the site and with a visible effect in the results. Let’s see what schema.org structured data is, how it works, and what Google actually does with it."},
    "Cosa sono i dati strutturati (in parole vostre)":
        {"en": "What structured data is (in your words)"},
    "Una pagina web, per un motore di ricerca, è un muro di testo da interpretare. «€ 25» è un prezzo, un codice postale o una taglia? «Chiuso» si riferisce a un negozio, a una strada o a un commento? Gli esseri umani lo capiscono dal contesto; una macchina deve indovinare. I dati strutturati servono esattamente a togliere di mezzo l’indovinello: sono un blocco di codice, invisibile al visitatore, che etichetta le informazioni una per una — «questo è il nome dell’attività, questo l’orario, questo il prezzo, queste le recensioni».":
        {"en": "A web page, to a search engine, is a wall of text to interpret. Is “€ 25” a price, a postcode or a size? Does “Closed” refer to a shop, a road or a comment? Humans work it out from context; a machine has to guess. Structured data exists precisely to take the guesswork out: it’s a block of code, invisible to the visitor, that labels the information one item at a time — “this is the business name, this the opening hours, this the price, these the reviews.”"},
    "Il vocabolario con cui si scrivono queste etichette si chiama schema.org: un dizionario condiviso, nato da un accordo tra Google, Microsoft e altri motori, che definisce come descrivere un’azienda, un prodotto, un evento, un articolo. Google raccomanda di scriverlo in un formato preciso, il JSON-LD: un piccolo blocco che si mette nel codice della pagina senza toccarne l’aspetto. Il visitatore non lo vede; il motore lo legge e capisce.":
        {"en": "The vocabulary these labels are written in is called schema.org: a shared dictionary, born of an agreement between Google, Microsoft and other engines, that defines how to describe a business, a product, an event, an article. Google recommends writing it in a specific format, JSON-LD: a small block placed in the page’s code without touching its appearance. The visitor doesn’t see it; the engine reads it and understands."},
    "Un blocco JSON-LD etichetta le informazioni — tipo, nome, indirizzo, orari, prezzo, recensioni — e Google le trasforma in un risultato ricco: stelline, orari e mappa. Fonte: Google, introduzione ai dati strutturati; vocabolario schema.org.":
        {"en": "A JSON-LD block labels the information — type, name, address, hours, price, reviews — and Google turns it into a rich result: stars, hours and map. Source: Google, intro to structured data; schema.org vocabulary."},
    "I dati strutturati non sono un vezzo tecnico: servono a ottenere i risultati ricchi (rich results), cioè quelle schede più grandi e complete che superano il classico link blu. Google li mostra proprio a partire dalle informazioni etichettate con schema.org — le stelline di una recensione, le briciole di navigazione, le FAQ che si aprono sotto il risultato, la foto e i tempi di una ricetta, la data di un evento. La galleria ufficiale di Google elenca decine di questi formati, e cresce di continuo.":
        {"en": "Structured data isn’t a technical affectation: it exists to earn rich results, those larger, fuller listings that go beyond the classic blue link. Google shows them precisely from the information labelled with schema.org — a review’s stars, breadcrumbs, the FAQs that open under the result, a recipe’s photo and times, an event’s date. Google’s official gallery lists dozens of these formats, and it keeps growing."},
    "Il vantaggio è doppio e concreto. Il primo: un risultato ricco occupa più spazio e attira più clic, a parità di posizione. Il secondo, più sottile: le stesse etichette che Google legge le leggono anche gli assistenti AI, che pescano dai dati strutturati per capire chi siete e cosa offrite. Diciamolo con onestà, però: i dati strutturati non fanno salire il sito nella classifica di per sé — Google lo dice chiaramente. Rendono il risultato più bello e più leggibile, non più in alto. Sono un moltiplicatore di clic, non una scorciatoia di posizione.":
        {"en": "The advantage is twofold and concrete. First: a rich result takes up more space and attracts more clicks, at the same position. Second, subtler: the same labels Google reads are read by AI assistants too, which draw on structured data to understand who you are and what you offer. Let’s be honest, though: structured data doesn’t lift the site up the rankings by itself — Google says so plainly. It makes the result nicer and more readable, not higher. It’s a click multiplier, not a ranking shortcut."},
    "Quali dati strutturati servono davvero a una PMI":
        {"en": "Which structured data an SME really needs"},
    "Non serve etichettare tutto: servono i tipi giusti per la vostra attività. Ecco quelli che, per una piccola o media impresa italiana, rendono di più con meno sforzo.":
        {"en": "You don’t need to label everything: you need the right types for your business. Here are the ones that, for a small or medium Italian business, give the most for the least effort."},
    "Organization o LocalBusiness: nome, logo, indirizzo, telefono, orari. È la carta d’identità del sito, e per un’attività locale quella che alimenta la scheda con orari e mappa.":
        {"en": "Organization or LocalBusiness: name, logo, address, phone, opening hours. It’s the site’s ID card, and for a local business the one that feeds the listing with hours and a map."},
    "Product e Offer: per chi vende, prezzo, disponibilità e valuta, così Google può mostrarli direttamente nel risultato.":
        {"en": "Product and Offer: for sellers, price, availability and currency, so Google can show them directly in the result."},
    "Review e AggregateRating: le recensioni reali, con le stelline — ma solo se sono vere e verificabili, mai inventate.":
        {"en": "Review and AggregateRating: real reviews, with the stars — but only if they’re genuine and verifiable, never invented."},
    "FAQPage: le domande frequenti, che possono comparire già aperte sotto il risultato.":
        {"en": "FAQPage: the frequently asked questions, which can appear already open under the result."},
    "BlogPosting e Article: autore, data e immagine di un articolo — gli stessi dati strutturati che mettiamo di serie su ogni pezzo di questo blog.":
        {"en": "BlogPosting and Article: an article’s author, date and image — the same structured data we put as standard on every piece of this blog."},
    "Google — la galleria dei risultati ricchi →":
        {"en": "Google — the rich results gallery →"},
    "Come aggiungerli senza rifare il sito":
        {"en": "How to add them without rebuilding the site"},
    "Una regola d’oro sopra tutte, ed è anche una regola di Google: i dati strutturati devono corrispondere a ciò che l’utente vede sulla pagina. Etichettare recensioni che non esistono, prezzi finti o orari sbagliati non è furbizia, è una violazione delle linee guida che può portare a una penalizzazione manuale. Il markup premia l’onestà, non i trucchi.":
        {"en": "One golden rule above all, and it’s a Google rule too: structured data must match what the user sees on the page. Labelling reviews that don’t exist, fake prices or wrong hours isn’t cleverness, it’s a guideline violation that can lead to a manual penalty. Structured data rewards honesty, not tricks."},
    "La buona notizia è che i dati strutturati si aggiungono sopra il sito che avete, senza rifarlo. Sono un blocco JSON-LD nel codice della pagina: su WordPress lo si genera con un plugin SEO ben configurato o, meglio, con markup su misura che riflette davvero i vostri contenuti. Prima di pubblicare si prova: lo strumento gratuito di Google (il Rich Results Test) legge la pagina e vi dice quali risultati ricchi può generare e dove ci sono errori. È un controllo di mezz’ora che evita di scoprire il problema quando ormai è online. I dati strutturati sono parte della SEO tecnica che consegniamo di serie — non un extra da vedere «più avanti».":
        {"en": "The good news is that structured data is added on top of the site you have, without rebuilding it. It’s a JSON-LD block in the page’s code: on WordPress it’s generated with a well-configured SEO plugin or, better, with bespoke markup that truly reflects your content. Before publishing you test it: Google’s free tool (the Rich Results Test) reads the page and tells you which rich results it can generate and where the errors are. It’s a half-hour check that saves you from finding the problem once it’s already online. Structured data is part of the technical SEO we deliver as standard — not an extra to look at “later.”"},
    "Fanno parte della SEO tecnica che consegniamo →":
        {"en": "They’re part of the technical SEO we deliver →"},
    "Dati strutturati, un pezzo del quadro più grande":
        {"en": "Structured data, one piece of a bigger picture"},
    "Un errore comune è trattare i dati strutturati come una bacchetta magica. In realtà sono un tassello: dicono a Google e agli assistenti AI chi siete, ma valgono davvero solo se il resto regge — contenuti chiari, un sito veloce, segnali di fiducia in ordine. Le stesse etichette che descrivono la vostra azienda sono, non a caso, uno dei segnali E-E-A-T che i motori leggono per capire quanto siete affidabili.":
        {"en": "A common mistake is treating structured data as a magic wand. In reality it’s one piece: it tells Google and AI assistants who you are, but it really counts only if the rest holds up — clear content, a fast site, trust signals in order. The same labels that describe your business are, not by chance, one of the E-E-A-T signals engines read to gauge how trustworthy you are."},
    "Il modo giusto di iniziare è misurare cosa c’è già. In un minuto potete verificare se la vostra home espone i dati strutturati — insieme agli altri segnali di fiducia — e capire cosa manca prima di aggiungere una sola riga di codice. Da lì, i risultati ricchi diventano un obiettivo concreto, non una speranza.":
        {"en": "The right way to start is to measure what’s already there. In a minute you can check whether your homepage exposes structured data — along with the other trust signals — and see what’s missing before adding a single line of code. From there, rich results become a concrete goal, not a hope."},
    "Misura gratis i segnali E-E-A-T e i dati strutturati della tua home →":
        {"en": "Measure your homepage’s E-E-A-T signals and structured data for free →"},
    "Fa parte della SEO tecnica a prezzo chiuso →":
        {"en": "It’s part of technical SEO at a fixed price →"},
    "Leggi anche: E-E-A-T, come Google giudica la vostra credibilità →":
        {"en": "Read also: E-E-A-T, how Google judges your credibility →"},
    "schema.org — il vocabolario dei dati strutturati":
        {"en": "schema.org — the structured data vocabulary"},
    "Il dizionario condiviso da Google e Microsoft con cui si descrivono aziende, prodotti ed eventi.":
        {"en": "The dictionary shared by Google and Microsoft used to describe businesses, products and events."},
    "Google — introduzione ai dati strutturati":
        {"en": "Google — intro to structured data"},
    "Come funziona il markup, perché JSON-LD è il formato consigliato e cosa Google ne fa.":
        {"en": "How the markup works, why JSON-LD is the recommended format, and what Google does with it."},
    "Google — galleria dei risultati ricchi":
        {"en": "Google — rich results gallery"},
    "L’elenco ufficiale dei formati di risultato ricco che i dati strutturati possono attivare.":
        {"en": "The official list of rich result formats that structured data can unlock."},
    "Google — linee guida generali sui dati strutturati":
        {"en": "Google — general structured data guidelines"},
    "Le regole da rispettare: i dati devono corrispondere ai contenuti visibili, o scatta la penalizzazione.":
        {"en": "The rules to follow: the data must match the visible content, or the penalty kicks in."},
    "Dati strutturati e SEO tecnica, di serie in ogni sito →":
        {"en": "Structured data and technical SEO, standard in every site →"},
    "Dati strutturati schema.org: un blocco JSON-LD invisibile che diventa un risultato ricco su Google":
        {"en": "Schema.org structured data: an invisible JSON-LD block that becomes a rich result on Google"},
    "Anatomia dei dati strutturati schema.org in JSON-LD: tipo, nome, orari e prezzo che diventano un risultato ricco su Google":
        {"en": "Anatomy of schema.org structured data in JSON-LD: type, name, hours and price that become a rich result on Google"},

    # ---- Articolo 14 · Gamification B2B ----
    "Gamification nel B2B: quando un gioco vende servizi seri":
        {"en": "Gamification in B2B: when a game sells serious services"},
    "Un servizio B2B «serio» fatica a farsi ricordare. La gamification può tenere le persone sul sito e raccontare cosa fate — se è strumento di marketing, non gadget. Come funziona, con un caso reale.":
        {"en": "A “serious” B2B service struggles to be remembered. Gamification can keep people on the site and tell them what you do — if it’s a marketing tool, not a gadget. How it works, with a real case."},
    "Un servizio B2B serio — una consulenza, una traduzione tecnica, un software gestionale — ha un problema che nessuno confessa volentieri: è noioso da raccontare. La brochure la legge chi già vi conosce; il sito lo si apre, si scorre e si chiude in trenta secondi. La gamification, cioè usare meccaniche da gioco fuori dal gioco, promette di rompere questa noia: tenere le persone sulla pagina, farle interagire, lasciare un ricordo. Ma funziona davvero nel marketing B2B, o è un gadget costoso? In questo articolo vediamo quando un gioco vende servizi seri, con un caso reale del gruppo Remarka e i suoi numeri.":
        {"en": "A serious B2B service — a consultancy, a technical translation, a management software — has a problem nobody likes to admit: it’s boring to tell. The brochure is read by those who already know you; the site is opened, scrolled and closed in thirty seconds. Gamification, that is using game mechanics outside a game, promises to break this boredom: keep people on the page, get them interacting, leave a memory. But does it really work in B2B marketing, or is it an expensive gadget? In this article we see when a game sells serious services, with a real case from the Remarka group and its numbers."},
    "Cos’è la gamification (e cosa non è)":
        {"en": "What gamification is (and what it isn’t)"},
    "Gamification non vuol dire «trasformare l’azienda in un videogioco». Vuol dire prendere alcune meccaniche che rendono i giochi coinvolgenti — un obiettivo chiaro, un progresso visibile, una piccola sfida, una ricompensa — e usarle in un contesto che gioco non è: un sito, un percorso di prova, un modulo. Il Nielsen Norman Group, autorità nel campo dell’esperienza utente, la definisce proprio così: l’uso di meccaniche di gioco in contesti non di gioco.":
        {"en": "Gamification doesn’t mean “turning the company into a video game.” It means taking some of the mechanics that make games engaging — a clear goal, visible progress, a small challenge, a reward — and using them in a context that isn’t a game: a site, a trial journey, a form. The Nielsen Norman Group, an authority in user experience, defines it exactly that way: the use of game mechanics in non-game contexts."},
    "E chiariamo subito cosa non è, perché è qui che si sbaglia. Non è appiccicare un punteggio a caso o una barra di progresso finta: quella è decorazione, e si vede. La gamification funziona quando tocca leve psicologiche reali. Sempre il Nielsen Norman Group le riconduce a tre bisogni fondamentali — autonomia, competenza, senso di relazione: le persone si coinvolgono quando possono scegliere, quando sentono di migliorare, quando quello che fanno ha un significato. Un gioco che ignora questi bisogni è solo un fastidio in più.":
        {"en": "And let’s be clear at once about what it isn’t, because this is where people go wrong. It isn’t slapping on a random score or a fake progress bar: that’s decoration, and it shows. Gamification works when it touches real psychological levers. Again the Nielsen Norman Group traces them to three fundamental needs — autonomy, competence, a sense of relatedness: people engage when they can choose, when they feel they’re improving, when what they do has meaning. A game that ignores these needs is just one more annoyance."},
    "Perché nel B2B è più difficile (e più prezioso)":
        {"en": "Why in B2B it’s harder (and more valuable)"},
    "Nel B2C la gamification è ovunque: raccolte punti, badge, classifiche. Nel B2B l’istinto è opposto — «siamo un’azienda seria, non un luna park» — e proprio per questo l’occasione è più grande. In un settore dove tutti i siti si somigliano, con gli stessi claim e le stesse foto stock, un contenuto che coinvolge davvero è una rarità che si nota e si ricorda. Il punto non è divertire per divertire: è dare al visitatore un motivo per restare, e al marchio qualcosa da raccontare.":
        {"en": "In B2C, gamification is everywhere: points schemes, badges, leaderboards. In B2B the instinct is the opposite — “we’re a serious company, not a funfair” — and precisely for that the opportunity is bigger. In a sector where all the sites look alike, with the same claims and the same stock photos, content that genuinely engages is a rarity that gets noticed and remembered. The point isn’t to entertain for entertainment’s sake: it’s to give the visitor a reason to stay, and the brand something to talk about."},
    "C’è anche un ritorno tecnico spesso ignorato. Il tempo che le persone passano sul sito e il modo in cui interagiscono sono segnali di qualità dei contenuti — Google premia le pagine che rispondono davvero e trattengono, non quelle che si abbandonano in due secondi. Un contenuto che intrattiene mentre spiega chi siete lavora quindi su due fronti insieme: la memoria di chi lo vive e la salute del sito agli occhi dei motori.":
        {"en": "There’s also a technical return that’s often ignored. The time people spend on the site and the way they interact are signals of content quality — Google rewards pages that genuinely answer and hold attention, not those abandoned in two seconds. Content that entertains while it explains who you are therefore works on two fronts at once: the memory of those who experience it and the site’s health in the eyes of the engines."},
    "Il ciclo che rende coinvolgente un’esperienza: un obiettivo chiaro, un’azione, un progresso visibile, una ricompensa — poggiato sui tre bisogni di autonomia, competenza e relazione. Fonte: Nielsen Norman Group.":
        {"en": "The loop that makes an experience engaging: a clear goal, an action, visible progress, a reward — resting on the three needs of autonomy, competence and relatedness. Source: Nielsen Norman Group."},
    "Un caso reale: un gioco per raccontare le traduzioni":
        {"en": "A real case: a game to tell the story of translation"},
    "Anche qui, prima di venderlo a voi l’abbiamo fatto per noi. Un servizio B2B «serio» come la traduzione fatica a farsi ricordare: volevamo un modo per far restare le persone sul sito dell’agenzia e raccontare il nostro mondo senza una brochure noiosa. Così abbiamo creato «L’Impero delle Traduzioni», un gioco browser in italiano dentro il sito: gamification al servizio del marketing, un contenuto che intrattiene e allo stesso tempo racconta cosa facciamo.":
        {"en": "Here too, before selling it to you we did it for ourselves. A “serious” B2B service like translation struggles to be remembered: we wanted a way to keep people on the agency’s site and tell our world without a boring brochure. So we created “Translation Empire,” a browser game in Italian inside the site: gamification in the service of marketing, content that entertains while it tells what we do."},
    "I numeri, così come sono: 984 partite giocate e oltre 200 ore complessive passate sul sito dell’agenzia — 12.086 minuti — grazie al gioco. Per un servizio che «non si può raccontare», è tempo di attenzione reale, non un dato gonfiato. È il lato creativo dello stesso team che vi fa il restyling: quando serve far restare l’utente, sappiamo anche divertirlo.":
        {"en": "The numbers, as they are: 984 games played and over 200 hours in total spent on the agency’s site — 12,086 minutes — thanks to the game. For a service that “can’t be told,” that’s real attention time, not an inflated figure. It’s the creative side of the same team that handles your redesign: when the job is to keep the user around, we know how to entertain them too."},
    "Quando un gioco vende (e quando è solo un costo)":
        {"en": "When a game sells (and when it’s just a cost)"},
    "La gamification non è la risposta a ogni problema di marketing. Conviene quando ci sono le condizioni giuste, ed è uno spreco quando le si forza.":
        {"en": "Gamification isn’t the answer to every marketing problem. It pays off when the right conditions are there, and it’s a waste when you force them."},
    "Avete qualcosa da spiegare che a parole annoia: un processo, un mestiere, un concetto tecnico che un’esperienza rende chiaro in un modo che il testo non può.":
        {"en": "You have something to explain that bores in words: a process, a craft, a technical concept that an experience makes clear in a way text can’t."},
    "Il vostro pubblico torna sul sito o ci passa del tempo: un gioco ha senso dove c’è attenzione da coltivare, non dove si cerca un numero di telefono e via.":
        {"en": "Your audience comes back to the site or spends time on it: a game makes sense where there’s attention to cultivate, not where people look up a phone number and leave."},
    "Volete distinguervi in un settore uniforme: dove i concorrenti si somigliano tutti, un contenuto vivo è un vantaggio di memoria.":
        {"en": "You want to stand out in a uniform sector: where competitors all look alike, living content is an advantage in memory."},
    "Da dove partire, senza buttare budget":
        {"en": "Where to start, without wasting budget"},
    "E quando è solo un costo? Quando il gioco non c’entra niente con ciò che vendete, quando è messo lì per moda e non risolve un problema reale del visitatore, quando complica il percorso invece di arricchirlo. Un gioco che allontana la persona dall’azione che conta — chiedere un preventivo, capire un servizio — è un gadget che avete pagato per rallentarvi. La domanda giusta, sempre, è: questo gioco fa restare e capire, o solo fare scena?":
        {"en": "And when is it just a cost? When the game has nothing to do with what you sell, when it’s there for fashion and solves no real problem for the visitor, when it complicates the journey instead of enriching it. A game that pulls the person away from the action that matters — asking for a quote, understanding a service — is a gadget you paid to slow yourself down. The right question, always, is: does this game make people stay and understand, or just put on a show?"},
    "Non si comincia dal gioco, si comincia dal messaggio. Cosa volete che una persona ricordi dopo essere passata dal vostro sito? Se quella cosa si spiega meglio facendola che leggendola, allora la gamification ha un senso — e va disegnata attorno a quel messaggio, non attorno al divertimento fine a sé stesso. È il tipo di idea che nasce quando restyling e marketing lavorano insieme: se state ripensando il sito e cercate un modo per farlo ricordare, questo è il momento giusto per valutarlo, con i piedi per terra e un occhio ai numeri.":
        {"en": "You don’t start from the game, you start from the message. What do you want a person to remember after passing through your site? If that thing is explained better by doing it than by reading it, then gamification makes sense — and it should be designed around that message, not around fun for its own sake. It’s the kind of idea that comes up when redesign and marketing work together: if you’re rethinking the site and looking for a way to make it memorable, this is the right time to weigh it up, feet on the ground and an eye on the numbers."},
    "Restyling e marketing per un sito che si ricorda →":
        {"en": "Redesign and marketing for a site that gets remembered →"},
    "Misura la salute del tuo sito attuale, gratis →":
        {"en": "Measure the health of your current site, free →"},
    "Leggi anche: check-up del sito web, le 7 misure che contano →":
        {"en": "Read also: website check-up, the 7 metrics that matter →"},
    "Nielsen Norman Group — la gamification nell’esperienza utente":
        {"en": "Nielsen Norman Group — gamification in the user experience"},
    "L’autorità mondiale della UX definisce cos’è la gamification e quando funziona davvero.":
        {"en": "The world authority on UX defines what gamification is and when it really works."},
    "Nielsen Norman Group — autonomia, competenza e relazione":
        {"en": "Nielsen Norman Group — autonomy, competence and relatedness"},
    "I tre bisogni psicologici che rendono un’esperienza coinvolgente, base di ogni buona gamification.":
        {"en": "The three psychological needs that make an experience engaging, the basis of any good gamification."},
    "Perché un contenuto che coinvolge e trattiene è anche un segnale di qualità per la ricerca.":
        {"en": "Why content that engages and holds attention is also a quality signal for search."},
    "Gamification nel marketing B2B: meccaniche di gioco che tengono le persone sul sito e raccontano un servizio serio":
        {"en": "Gamification in B2B marketing: game mechanics that keep people on the site and tell a serious service’s story"},
    "Il ciclo della gamification nel marketing B2B: obiettivo, azione, progresso e ricompensa, sui bisogni di autonomia, competenza e relazione":
        {"en": "The gamification loop in B2B marketing: goal, action, progress and reward, on the needs of autonomy, competence and relatedness"},

    # ---- Articolo 15 · Hosting Italia o cloud ----
    "Hosting in Italia o in cloud: cosa cambia per velocità e GDPR":
        {"en": "Website hosting in Italy or the cloud: what changes for speed and GDPR"},
    "Dove vive il vostro sito conta più di quanto pensiate: cambia la velocità di caricamento e la conformità al GDPR. Hosting in Italia, cloud europeo o extra-UE: cosa scegliere e perché.":
        {"en": "Where your site lives matters more than you think: it changes load speed and GDPR compliance. Hosting in Italy, European cloud or outside the EU: what to choose and why."},
    "«Tanto l’hosting è tutto uguale, prendo il più economico.» È l’idea con cui si firmano contratti che poi costano cari in due valute diverse: secondi di attesa e grattacapi legali. Dove vivono fisicamente i vostri file — un server in Italia, un cloud europeo, un data center oltreoceano — cambia due cose che pesano davvero: quanto in fretta la pagina si apre a un visitatore italiano, e quanto è semplice restare in regola con il GDPR sui dati dei clienti. In questo articolo vediamo cosa cambia per l’hosting di un sito web in Italia rispetto al cloud, senza tecnicismi inutili e con le domande giuste da fare prima di scegliere.":
        {"en": "“Hosting is all the same anyway, I’ll take the cheapest.” It’s the idea behind contracts that then cost dearly in two different currencies: seconds of waiting and legal headaches. Where your files physically live — a server in Italy, a European cloud, a data center overseas — changes two things that really weigh: how fast the page opens for an Italian visitor, and how simple it is to stay compliant with the GDPR on your customers’ data. In this article we see what changes for website hosting in Italy versus the cloud, without needless jargon and with the right questions to ask before choosing."},
    "Cosa cambia per la velocità: la distanza conta":
        {"en": "What changes for speed: distance matters"},
    "Ogni volta che qualcuno apre il vostro sito, il suo browser deve dialogare con il server dove vivono i file. La prima risposta del server ha un nome tecnico — Time to First Byte, il tempo fino al primo byte — ed è la base su cui si costruisce tutta la velocità percepita. Su questo tempo pesano due cose: quanto è veloce il server a rispondere, e quanto è lontano da chi lo interroga. La documentazione di Google su questa metrica è netta: la scelta dell’hosting è determinante, e i server condivisi e sovraffollati sono generalmente più lenti.":
        {"en": "Every time someone opens your site, their browser has to talk to the server where the files live. The server’s first response has a technical name — Time to First Byte, the time to the first byte — and it’s the base on which all perceived speed is built. Two things weigh on this time: how fast the server responds, and how far it is from whoever queries it. Google’s documentation on this metric is blunt: the choice of hosting is decisive, and shared, overcrowded servers are generally slower."},
    "La distanza fisica non è un dettaglio. Un server lontano dai vostri visitatori aggiunge latenza a ogni richiesta — millisecondi che, sommati, diventano secondi di attesa in più su una connessione mobile. Se il vostro pubblico è italiano, un hosting vicino (in Italia o comunque in Europa) parte avvantaggiato. La soluzione che scavalca il problema si chiama CDN, una rete di server che tiene copie del sito vicino agli utenti ovunque siano: con una buona CDN davanti, anche un’origine lontana può servire in fretta un visitatore italiano.":
        {"en": "Physical distance isn’t a detail. A server far from your visitors adds latency to every request — milliseconds that, added up, become extra seconds of waiting on a mobile connection. If your audience is Italian, hosting that’s close (in Italy or at least in Europe) starts with an advantage. The solution that gets around the problem is called a CDN, a network of servers that keeps copies of the site near users wherever they are: with a good CDN in front, even a distant origin can serve an Italian visitor quickly."},
    "Dal visitatore italiano al server: vicino (Italia o UE) significa tempo di risposta basso e dati che restano nell’Unione; lontano (extra-UE) significa più latenza e, per il GDPR, misure supplementari. Una CDN avvicina i contenuti. Fonti: web.dev (TTFB), EDPB (trasferimenti dati).":
        {"en": "From the Italian visitor to the server: close (Italy or EU) means low response time and data that stays in the Union; far (outside the EU) means more latency and, for the GDPR, supplementary measures. A CDN brings the content closer. Sources: web.dev (TTFB), EDPB (data transfers)."},
    "Cosa cambia per il GDPR: dove finiscono i dati":
        {"en": "What changes for the GDPR: where the data ends up"},
    "Qui il discorso si sposta dalla velocità alla legge, e diventa serio. Il vostro sito, quasi sempre, raccoglie dati personali: un modulo contatti, un e-commerce, persino i log del server con gli indirizzi IP. Il GDPR — il regolamento europeo sulla protezione dei dati — stabilisce che questi dati godono di una tutela precisa, e pone regole stringenti quando escono dall’Unione Europea. Non è un divieto di usare fornitori extra-UE, ma un obbligo di garantire che, ovunque vadano, i dati mantengano lo stesso livello di protezione.":
        {"en": "Here the talk shifts from speed to law, and gets serious. Your site, almost always, collects personal data: a contact form, an e-commerce, even server logs with IP addresses. The GDPR — the European data protection regulation — establishes that this data enjoys a precise protection, and sets strict rules when it leaves the European Union. It isn’t a ban on using non-EU providers, but an obligation to ensure that, wherever it goes, the data keeps the same level of protection."},
    "La differenza pratica è questa. Se ospitate il sito in Italia o in un data center europeo, i dati restano nell’UE e il capitolo dei trasferimenti internazionali, semplicemente, non si apre: una complicazione in meno. Se invece scegliete un fornitore che archivia o elabora i dati fuori dall’Unione — molti grandi cloud hanno server in tutto il mondo — dovete verificare le garanzie previste dal GDPR. Il Comitato europeo per la protezione dei dati (EDPB), dopo la sentenza «Schrems II», ha chiarito che in questi casi servono valutazioni e, spesso, misure supplementari. Tradotto: più burocrazia e più responsabilità sulle vostre spalle.":
        {"en": "The practical difference is this. If you host the site in Italy or in a European data center, the data stays in the EU and the chapter on international transfers simply doesn’t open: one complication fewer. If instead you choose a provider that stores or processes data outside the Union — many large clouds have servers all over the world — you have to verify the safeguards required by the GDPR. The European Data Protection Board (EDPB), after the “Schrems II” ruling, clarified that in these cases assessments and, often, supplementary measures are needed. Translated: more bureaucracy and more responsibility on your shoulders."},
    "Italia, Europa o extra-UE: come scegliere":
        {"en": "Italy, Europe or outside the EU: how to choose"},
    "Non esiste una risposta unica valida per tutti, ma esistono criteri chiari. Ecco come ragionare, senza farsi guidare solo dal prezzo mensile.":
        {"en": "There’s no single answer for everyone, but there are clear criteria. Here’s how to reason, without being guided by the monthly price alone."},
    "Se il vostro pubblico è italiano o europeo: un hosting in Italia o nell’UE è la scelta più semplice — vicino per la velocità, dentro l’UE per il GDPR.":
        {"en": "If your audience is Italian or European: hosting in Italy or the EU is the simplest choice — close for speed, inside the EU for the GDPR."},
    "Se avete traffico o clienti in più continenti: conta la copertura, e una CDN europea davanti a un’origine ben scelta risolve la velocità senza portare i dati fuori dall’UE.":
        {"en": "If you have traffic or clients across continents: coverage matters, and a European CDN in front of a well-chosen origin solves the speed without moving the data outside the EU."},
    "Se guardate un grande cloud extra-UE: verificate dove risiedono davvero i dati — molti offrono regioni europee — e mettete a bilancio la conformità, non solo il canone.":
        {"en": "If you’re looking at a large non-EU cloud: check where the data really resides — many offer European regions — and budget for compliance, not just the fee."},
    "In ogni caso: chiedete un server non sovraffollato e una CDN inclusa, sono le due leve che spostano di più il tempo di risposta.":
        {"en": "In any case: ask for a server that isn’t overcrowded and a CDN included, they’re the two levers that move response time the most."},
    "Come sapere dove siete oggi (e se vi frena)":
        {"en": "How to know where you are today (and whether it’s holding you back)"},
    "Un dettaglio che vale doppio: un hosting adeguato migliora insieme velocità e sostenibilità. Un server efficiente, vicino e alimentato da energia rinnovabile serve i vostri byte con meno attesa e meno emissioni — la stessa leva, letta da due lati. Ma prima di cambiare hosting, misurate quello che avete.":
        {"en": "A detail that counts double: adequate hosting improves speed and sustainability together. An efficient server, close and powered by renewable energy, serves your bytes with less waiting and fewer emissions — the same lever, read from two sides. But before changing hosting, measure what you have."},
    "Il tempo di risposta del server si vede in qualsiasi test di velocità: se la pagina impiega più di un secondo a dare il primo segno di vita, l’hosting è quasi sempre tra gli indiziati principali. È un numero, non una sensazione. Sul fronte dati, la domanda da fare al fornitore è secca: dove sono fisicamente archiviati i dati del mio sito e dei miei utenti? Se la risposta è vaga, è già un segnale. Nei siti che consegniamo l’hosting è scelto perché i dati restino nell’Unione Europea, come parte del progetto e non come dettaglio da sistemare dopo.":
        {"en": "The server’s response time shows up in any speed test: if the page takes more than a second to give its first sign of life, hosting is almost always among the prime suspects. It’s a number, not a feeling. On the data front, the question to ask the provider is blunt: where is my site’s and my users’ data physically stored? If the answer is vague, that’s already a signal. In the sites we deliver, hosting is chosen so the data stays in the European Union, as part of the project and not a detail to sort out later."},
    "Cosa include un sito aziendale, hosting e GDPR compresi →":
        {"en": "What a business website includes, hosting and GDPR included →"},
    "Misura gratis la velocità e il tempo di risposta del server →":
        {"en": "Measure your server’s speed and response time for free →"},
    "La metrica del tempo di risposta del server: perché l’hosting decide la velocità di partenza.":
        {"en": "The server response-time metric: why hosting decides your starting speed."},
    "web.dev — ottimizzare il TTFB":
        {"en": "web.dev — optimize TTFB"},
    "Come hosting, prossimità e CDN incidono sul tempo di risposta, con i rimedi concreti.":
        {"en": "How hosting, proximity and CDN affect response time, with concrete fixes."},
    "Il testo del GDPR: la tutela dei dati personali e le regole sui trasferimenti fuori dall’UE.":
        {"en": "The GDPR text: the protection of personal data and the rules on transfers outside the EU."},
    "EDPB — trasferimenti internazionali di dati":
        {"en": "EDPB — international data transfers"},
    "La guida del Comitato europeo: cosa serve quando i dati escono dall’Unione Europea (post Schrems II).":
        {"en": "The European Board’s guide: what’s needed when data leaves the European Union (post Schrems II)."},
    "Un sito aziendale con hosting e GDPR inclusi, a prezzo chiuso →":
        {"en": "A business website with hosting and GDPR included, at a fixed price →"},
    "Hosting di un sito web in Italia o in cloud: distanza dal visitatore, velocità e dove finiscono i dati secondo il GDPR":
        {"en": "Website hosting in Italy or the cloud: distance from the visitor, speed and where the data ends up under the GDPR"},
    "Hosting di un sito web in Italia o in cloud: distanza dal visitatore, tempo di risposta e dove risiedono i dati secondo il GDPR":
        {"en": "Website hosting in Italy or the cloud: distance from the visitor, response time and where the data resides under the GDPR"},

    # ---- Backlink aggiunti nei tool (test-velocita, segnali-eeat) ----
    "Guida: hosting in Italia o in cloud, cosa cambia per velocità e GDPR →":
        {"en": "Guide: website hosting in Italy or the cloud, what changes for speed and GDPR →"},
    "Guida: i dati strutturati schema.org che Google premia →":
        {"en": "Guide: the schema.org structured data Google rewards →"},
}
CHROME.update(CHROME_BLOG_BATCH3)

# Batch 3 — fix: etichetta link inline esterno (art. dati strutturati, sez. 4)
CHROME.update({
    "Google — linee guida sui dati strutturati →":
        {"en": "Google — structured data guidelines →"},
})

# Batch 3 — fix: titoli H2 senza parole in ITALIAN_HINT (non intercettati dal report)
CHROME.update({
    "Perché proprio dentro Telegram": {"en": "Why inside Telegram, of all places"},
    "Da dove partire": {"en": "Where to start"},
    "Cosa ci fa Google: i risultati ricchi": {"en": "What Google does with it: rich results"},
})

# CHROME_BLOG_BATCH4 — Blog · Batch 4 (5 articoli IT → EN): SEO locale a Milano,
# Google Business Profile, hreflang, sito per l'export, manutenzione WordPress.
# Copre ogni nodo di testo generato da build_blog_post. Solo EN (il blog RU è un
# batch a sé). Numeri in formato US (li normalizza il conveyor).
CHROME_BLOG_BATCH4 = {
    "18 LUG 2026": {"en": "18 JUL 2026"},

    # ================= Articolo 16 · SEO locale a Milano =================
    "SEO locale a Milano: come emergere nella città più competitiva":
        {"en": "Local SEO in Milan: how to stand out in Italy’s most competitive city"},
    "A Milano si cerca «vicino a me» e si sceglie chi appare per primo nella mappa. Come funziona la SEO locale, cosa pesa davvero nel ranking e da dove partire — con il nostro ufficio in città come banco di prova.":
        {"en": "In Milan people search “near me” and pick whoever shows up first on the map. How local SEO works, what really weighs in the ranking and where to start — with our own office in the city as a test bed."},
    "Un artigiano ai Navigli, un fisioterapista in Città Studi, un ristorante a Porta Romana: a Milano ognuno di loro compete con altri venti nel raggio di un chilometro. E quando un cliente cerca «fisioterapista vicino a me» dal telefono, non scorre dieci pagine di risultati — guarda i primi tre nella mappa e sceglie lì. La SEO locale a Milano è la disciplina che decide chi finisce in quei tre posti. Non è una questione di magia né di budget: è un lavoro fatto di segnali precisi, che quasi nessuno cura fino in fondo. Vediamo come funziona davvero, cosa pesa nel ranking e da dove partire — con il nostro ufficio in città come esempio concreto.":
        {"en": "A tradesperson on the Navigli, a physiotherapist in Città Studi, a restaurant in Porta Romana: in Milan each of them competes with twenty others within a kilometre. And when a customer searches “physiotherapist near me” on their phone, they don’t scroll through ten pages of results — they look at the top three on the map and choose there. Local SEO in Milan is the discipline that decides who lands in those three spots. It’s not a matter of magic or budget: it’s work made of precise signals that almost nobody sees all the way through. Let’s look at how it really works, what weighs in the ranking, and where to start — with our own office in the city as a concrete example."},
    "SEO locale a Milano: la mappa con i primi tre risultati che un cliente vede cercando «vicino a me»":
        {"en": "Local SEO in Milan: the map with the top three results a customer sees when searching “near me”"},
    "Perché a Milano la SEO locale è una gara diversa":
        {"en": "Why local SEO in Milan is a different race"},
    "Milano è il mercato più affollato d’Italia per quasi ogni servizio: per lo stesso mestiere convivono in città centinaia di attività, e la concorrenza non è nazionale, è a isolati di distanza. Questo cambia le regole. Farsi trovare per «commercialista Milano» non serve a niente se non si compare quando qualcuno, a due fermate di metro, cerca proprio in quel momento. La SEO locale non punta al primo posto nazionale: punta a essere il più rilevante per chi è vicino, adesso.":
        {"en": "Milan is Italy’s most crowded market for almost every service: hundreds of businesses in the same trade coexist in the city, and the competition isn’t national, it’s a few blocks away. That changes the rules. Getting found for “accountant Milan” is useless if you don’t show up when someone two metro stops away is searching right at that moment. Local SEO doesn’t aim for the top national spot: it aims to be the most relevant to whoever is nearby, now."},
    "Il campo di battaglia ha un nome preciso: il «local pack», quel blocco con la mappa e tre attività che Google mostra in cima ai risultati di ricerca a intento locale. Sotto ci sono i link classici, ma l’occhio — soprattutto da mobile — cade lì. Entrare in quei tre riquadri vale più di dieci posizioni organiche: è la vetrina che il cliente vede prima di tutto il resto. E a Milano, dove i concorrenti sono tanti, la differenza tra esserci e non esserci è la differenza tra squillare e restare muti.":
        {"en": "The battlefield has a precise name: the “local pack,” that block with the map and three businesses Google shows at the top of local-intent search results. The classic links sit below it, but the eye — especially on mobile — lands there. Making it into those three boxes is worth more than ten organic positions: it’s the storefront the customer sees before anything else. And in Milan, where competitors are many, the difference between being there and not is the difference between your phone ringing and staying silent."},
    "I tre fattori che decidono la mappa":
        {"en": "The three factors that decide the map"},
    "Google è insolitamente esplicito su come sceglie chi mostrare nel local pack. Nella sua guida ufficiale al ranking locale indica tre fattori, e vale la pena conoscerli perché su tutti e tre si può lavorare.":
        {"en": "Google is unusually explicit about how it picks who to show in the local pack. In its official guide to local ranking it names three factors, and they’re worth knowing because you can work on all three."},
    "Rilevanza: quanto la vostra scheda corrisponde a ciò che la persona cerca. Più le informazioni sono complete e precise — categoria giusta, servizi, descrizione — più Google vi abbina alle ricerche pertinenti.":
        {"en": "Relevance: how well your profile matches what the person is searching for. The more complete and precise the information — right category, services, description — the more Google matches you to relevant searches."},
    "Distanza: quanto siete lontani da chi cerca. Non la controllate, ma la potete assecondare: un indirizzo esatto e una zona di servizio dichiarata dicono a Google dove operate davvero.":
        {"en": "Distance: how far you are from the person searching. You don’t control it, but you can play to it: an exact address and a declared service area tell Google where you actually operate."},
    "Prominenza: quanto siete conosciuti. Pesano le recensioni, le citazioni del nome e dell’indirizzo su altri siti, e — sì — anche quanti siti autorevoli parlano di voi. Qui la SEO locale incontra quella «classica».":
        {"en": "Prominence: how well known you are. Reviews count, so do mentions of your name and address on other sites, and — yes — how many authoritative sites talk about you. Here local SEO meets the “classic” kind."},
    "I tre fattori della SEO locale a Milano secondo Google: rilevanza, distanza e prominenza, che decidono il local pack":
        {"en": "The three factors of local SEO in Milan according to Google: relevance, distance and prominence, which decide the local pack"},
    "I tre fattori con cui Google decide il local pack: rilevanza (quanto la scheda corrisponde alla ricerca), distanza (quanto siete vicini a chi cerca) e prominenza (quanto siete conosciuti, recensioni comprese). Su tutti e tre si lavora. Fonte: Google, guida ufficiale al ranking locale.":
        {"en": "The three factors Google uses to decide the local pack: relevance (how well the profile matches the search), distance (how close you are to the searcher) and prominence (how well known you are, reviews included). You can work on all three. Source: Google, official guide to local ranking."},
    "La scheda Google: il vostro negozio prima del negozio":
        {"en": "Your Google profile: the shop before the shop"},
    "Il motore della SEO locale è la scheda Google (Google Business Profile): è lei a comparire nella mappa, con nome, orari, foto, telefono e recensioni. Per molte ricerche locali il cliente decide guardando solo quella, senza aprire il sito. Curarla non è un dettaglio, è la base: una scheda incompleta o con orari sbagliati vi taglia fuori dai risultati pertinenti prima ancora della concorrenza.":
        {"en": "The engine of local SEO is your Google profile (Google Business Profile): it’s what appears on the map, with name, hours, photos, phone and reviews. For many local searches the customer decides looking at that alone, without ever opening the site. Looking after it isn’t a detail, it’s the foundation: an incomplete profile or one with wrong hours cuts you out of the relevant results before the competition even does."},
    "E poi ci sono le recensioni, che pesano su fiducia e ranking insieme. Secondo l’indagine annuale di BrightLocal sui consumatori, la quasi totalità delle persone legge le recensioni prima di scegliere un’attività locale. Non significa inventarle — sarebbe un boomerang, oltre che una violazione — ma chiederle con metodo a chi è stato bene. Alla scheda Google e a come si cura senza trucchi abbiamo dedicato un articolo a parte, perché merita una guida sua.":
        {"en": "And then there are reviews, which weigh on trust and ranking at once. According to BrightLocal’s annual consumer survey, almost everyone reads reviews before choosing a local business. That doesn’t mean inventing them — it would be a boomerang, and a violation too — but asking for them methodically from people who had a good experience. We’ve devoted a separate article to the Google profile and how to look after it without tricks, because it deserves a guide of its own."},
    "Google — guida al ranking locale →":
        {"en": "Google — guide to local ranking →"},
    "Leggi anche: Google Business Profile, la vetrina che nessuno cura →":
        {"en": "Read also: Google Business Profile, the storefront nobody tends →"},
    "Il sito conta ancora: dati strutturati e contenuti locali":
        {"en": "The site still matters: structured data and local content"},
    "La scheda Google non vive da sola: si appoggia al vostro sito, e un sito curato rafforza tutto il resto. Il primo mattone sono i dati strutturati — quel blocco di codice, invisibile al visitatore, che dice a Google «questa è un’attività locale, ecco nome, indirizzo, orari e zona». È il tipo LocalBusiness di schema.org, e Google lo legge per capire e mostrare meglio la vostra scheda. Il secondo mattone è la coerenza: nome, indirizzo e telefono devono essere identici ovunque compaiano, sul sito e sulle directory.":
        {"en": "The Google profile doesn’t live alone: it leans on your site, and a well-kept site strengthens everything else. The first brick is structured data — that block of code, invisible to the visitor, that tells Google “this is a local business, here’s the name, address, hours and area.” It’s schema.org’s LocalBusiness type, and Google reads it to understand and show your profile better. The second brick is consistency: name, address and phone must be identical everywhere they appear, on the site and in directories."},
    "Poi vengono i contenuti che parlano davvero del territorio. Non «keyword Milano» ripetute a forza, ma pagine e testi che rispondono a domande locali reali: le zone che servite, i casi seguiti in città, i tempi di intervento in provincia. È lavoro di SEO tecnica e di contenuto insieme, ed è esattamente quello che consegniamo di serie — non un extra da vedere «più avanti». Prima di aggiungere una riga, però, conviene misurare i segnali che il vostro sito già manda a Google.":
        {"en": "Then come the contents that really speak about the area. Not “Milan keyword” hammered in, but pages and copy that answer real local questions: the zones you serve, the jobs you’ve handled in the city, response times across the province. It’s technical SEO and content work together, and it’s exactly what we deliver as standard — not an extra to look at “later on.” Before adding a single line, though, it’s worth measuring the signals your site already sends Google."},
    "Dati strutturati e SEO tecnica in ogni sito →":
        {"en": "Structured data and technical SEO in every site →"},
    "Misura gratis i segnali E-E-A-T e i dati strutturati della vostra home →":
        {"en": "Measure your home page’s E-E-A-T signals and structured data for free →"},
    "Google — dati strutturati e LocalBusiness →":
        {"en": "Google — structured data and LocalBusiness →"},
    "Da dove partire, a Milano e oltre":
        {"en": "Where to start, in Milan and beyond"},
    "L’ordine giusto è controintuitivo: prima la scheda Google (completa, verificata, con recensioni vere), poi il sito (dati strutturati, NAP coerente, contenuti locali), infine la prominenza (citazioni e link autorevoli, che arrivano col tempo). Saltare il primo passo per rincorrere il terzo è l’errore più comune, e il più costoso. A Milano, dove i concorrenti curano già almeno la scheda, la partita si gioca sui dettagli che gli altri trascurano.":
        {"en": "The right order is counterintuitive: first the Google profile (complete, verified, with real reviews), then the site (structured data, consistent NAP, local content), and finally prominence (citations and authoritative links, which come with time). Skipping the first step to chase the third is the most common mistake, and the most expensive. In Milan, where competitors at least tend to their profile, the game is won on the details the others neglect."},
    "Questo lavoro lo facciamo dove i clienti sono, non solo online: a Milano abbiamo un ufficio vero, in Vicolo Privato Lavandai, e il primo incontro — da voi o da noi — non si paga. Ma il metodo è lo stesso in tutta Italia: analizziamo la scheda e il sito attuali, vi diciamo cosa manca nero su bianco, e lavoriamo per farvi entrare in quella mappa. Il nostro biglietto da visita, del resto, è un sito che abbiamo costruito per un’agenzia del gruppo con la stessa cura che mettiamo per voi.":
        {"en": "We do this work where the customers are, not only online: in Milan we have a real office, on Vicolo Privato Lavandai, and the first meeting — at your place or ours — is free. But the method is the same across Italy: we analyse your current profile and site, tell you what’s missing in black and white, and work to get you onto that map. Our calling card, after all, is a site we built for a group agency with the same care we put into yours."},
    "Realizzazione siti web a Milano: come lavoriamo in città →":
        {"en": "Websites in Milan: how we work in the city →"},
    "Dove lavoriamo, in tutta Italia →":
        {"en": "Where we work, across Italy →"},
    "Il caso ATT, il sito dell’agenzia di traduzioni →":
        {"en": "The ATT case, the translation agency’s website →"},
    "SEO tecnica e locale, di serie in ogni sito, a prezzo chiuso →":
        {"en": "Technical and local SEO, standard in every site, at a fixed price →"},
    "Google — migliorare il ranking locale su Google":
        {"en": "Google — improve your local ranking on Google"},
    "La guida ufficiale: i tre fattori (rilevanza, distanza, prominenza) e come Google sceglie il local pack.":
        {"en": "The official guide: the three factors (relevance, distance, prominence) and how Google picks the local pack."},
    "Google — dati strutturati e LocalBusiness":
        {"en": "Google — structured data and LocalBusiness"},
    "Come il markup LocalBusiness aiuta Google a capire e mostrare un’attività locale.":
        {"en": "How LocalBusiness markup helps Google understand and display a local business."},
    "BrightLocal — Local Consumer Review Survey":
        {"en": "BrightLocal — Local Consumer Review Survey"},
    "L’indagine annuale sui consumatori: quasi tutti leggono le recensioni prima di scegliere un’attività locale.":
        {"en": "The annual consumer survey: almost everyone reads reviews before choosing a local business."},

    # ============= Articolo 17 · Google Business Profile =============
    "Google Business Profile: la vetrina gratuita che nessuno cura":
        {"en": "Google Business Profile: the free storefront nobody tends"},
    "È gratis, la vede più gente della vostra home e decide se vi scelgono o passano oltre. Cos’è un Google Business Profile, come si cura sul serio e gli errori che vi tagliano fuori dai risultati.":
        {"en": "It’s free, more people see it than your home page, and it decides whether they pick you or move on. What a Google Business Profile is, how to tend it properly and the mistakes that cut you out of the results."},
    "C’è una pagina che, per molte ricerche, la gente vede prima del vostro sito: la scheda che compare a destra quando cercano il vostro nome, o nella mappa quando cercano un servizio «vicino a me». È il vostro Google Business Profile, ed è gratuito. Eppure è la cosa peggio curata del marketing di quasi ogni PMI italiana: orari vecchi, foto sfocate, una descrizione scritta di fretta anni fa e mai più toccata. Chi la cura sul serio si prende un vantaggio che i concorrenti gli regalano ogni giorno. Vediamo cos’è davvero un Google Business Profile, come si tiene in ordine senza trucchi, e quali errori vi tagliano fuori dai risultati.":
        {"en": "There’s a page that, for many searches, people see before your site: the panel that appears on the right when they search your name, or on the map when they search a service “near me.” It’s your Google Business Profile, and it’s free. Yet it’s the worst-tended piece of marketing at almost every Italian SMB: old hours, blurry photos, a description dashed off years ago and never touched since. Whoever tends it properly gains an edge their competitors hand them every day. Let’s see what a Google Business Profile really is, how to keep it in order without tricks, and which mistakes cut you out of the results."},
    "Google Business Profile: la scheda gratuita con nome, orari, foto e recensioni che i clienti vedono prima del sito":
        {"en": "Google Business Profile: the free listing with name, hours, photos and reviews that customers see before the site"},
    "Cos’è (e perché la vede più gente della vostra home)":
        {"en": "What it is (and why more people see it than your home page)"},
    "Un Google Business Profile è la scheda gratuita che rappresenta la vostra attività su Google Search e Google Maps. Contiene nome, categoria, indirizzo o zona di servizio, orari, telefono, sito, foto e recensioni. Non è il vostro sito e non lo sostituisce: è ciò che Google mostra di voi quando qualcuno vi cerca, spesso senza che quel qualcuno arrivi mai alla vostra home. Per un’attività locale è, di fatto, la prima pagina — quella su cui si decide se chiamarvi o passare al prossimo.":
        {"en": "A Google Business Profile is the free listing that represents your business on Google Search and Google Maps. It holds name, category, address or service area, hours, phone, website, photos and reviews. It isn’t your site and doesn’t replace it: it’s what Google shows of you when someone searches for you, often without that someone ever reaching your home page. For a local business it is, in effect, the first page — the one where they decide whether to call you or move on to the next."},
    "Il paradosso è che questa vetrina costa zero e la vede tantissima gente, e proprio per questo viene trascurata: è gratis, quindi sembra meno importante di una campagna a pagamento. È l’opposto. Una scheda completa e aggiornata è tra gli investimenti a più alto ritorno che esistano, perché lavora su ogni ricerca del vostro nome e su quelle a intento locale, tutti i giorni, senza costo per clic.":
        {"en": "The paradox is that this storefront costs nothing and huge numbers of people see it, and precisely for that reason it gets neglected: it’s free, so it seems less important than a paid campaign. It’s the opposite. A complete, up-to-date profile is among the highest-return investments there are, because it works on every search of your name and every local-intent search, every day, at no cost per click."},
    "Come si cura sul serio: completezza, recensioni, coerenza":
        {"en": "How to tend it properly: completeness, reviews, consistency"},
    "La cura di una scheda non è un gesto una tantum, è manutenzione. Tre leve contano più delle altre, e sono le stesse che Google indica nella sua guida al ranking locale.":
        {"en": "Tending a profile isn’t a one-off gesture, it’s maintenance. Three levers count more than the rest, and they’re the same ones Google names in its guide to local ranking."},
    "Completezza: compilate ogni campo — categoria principale corretta, servizi, descrizione onesta, orari veri (festivi compresi), foto reali e recenti. Una scheda completa è più probabile che compaia per le ricerche pertinenti.":
        {"en": "Completeness: fill in every field — correct primary category, services, an honest description, real hours (holidays included), real and recent photos. A complete profile is more likely to appear for relevant searches."},
    "Recensioni: chiedetele con metodo a chi è stato bene, rispondete a tutte con educazione, anche alle critiche. Contano per la fiducia e per il ranking — ma solo se sono vere.":
        {"en": "Reviews: ask for them methodically from people who had a good experience, reply to all of them politely, criticism included. They count for trust and for ranking — but only if they’re genuine."},
    "Coerenza (NAP): nome, indirizzo e telefono devono essere identici sulla scheda, sul sito e su ogni directory. Le incoerenze confondono Google e vi fanno perdere posizioni.":
        {"en": "Consistency (NAP): name, address and phone must be identical on the profile, on the site and in every directory. Inconsistencies confuse Google and cost you positions."},
    "Anatomia di un Google Business Profile curato: nome, categoria, orari veri, foto reali, recensioni con risposte e NAP coerente":
        {"en": "Anatomy of a well-tended Google Business Profile: name, category, real hours, real photos, reviews with replies and consistent NAP"},
    "Una scheda Google curata, campo per campo: categoria corretta, orari veri, foto reali, recensioni con risposte e un NAP (nome, indirizzo, telefono) identico ovunque. La completezza è ciò che la fa comparire nelle ricerche pertinenti. Fonte: Google, guida al ranking locale e linee guida di rappresentazione.":
        {"en": "A well-tended Google profile, field by field: correct category, real hours, real photos, reviews with replies and a NAP (name, address, phone) identical everywhere. Completeness is what makes it appear in relevant searches. Source: Google, guide to local ranking and representation guidelines."},
    "Gli errori che vi tagliano fuori dai risultati":
        {"en": "The mistakes that cut you out of the results"},
    "Google ha regole precise su come un’attività va rappresentata, e violarle non è furbizia: porta a sospensioni della scheda, cioè a sparire dai risultati. Le linee guida ufficiali sono chiare, e gli errori più comuni sono anche i più facili da evitare.":
        {"en": "Google has precise rules on how a business should be represented, and breaking them isn’t clever: it leads to profile suspensions, meaning you vanish from the results. The official guidelines are clear, and the most common mistakes are also the easiest to avoid."},
    "Nome «arricchito» con parole chiave: «Mario Rossi Idraulico Milano Pronto Intervento 24h» viola le regole. Il nome deve essere quello reale dell’attività, punto.":
        {"en": "A name “stuffed” with keywords: “Mario Rossi Plumber Milan 24h Emergency Call-Out” breaks the rules. The name must be the business’s real one, full stop."},
    "Indirizzo finto o casella postale per simulare una sede che non c’è: è tra le violazioni prese più sul serio.":
        {"en": "A fake address or a PO box to fake a location that doesn’t exist: it’s among the violations taken most seriously."},
    "Categorie a raffica: sceglietene poche e pertinenti, non tutte quelle possibili. La precisione batte la quantità.":
        {"en": "Categories by the fistful: pick a few relevant ones, not every possible one. Precision beats quantity."},
    "Promozioni e prezzi nella descrizione, o link vietati: la descrizione racconta chi siete, non «tutto al -50%».":
        {"en": "Promotions and prices in the description, or forbidden links: the description tells who you are, not “everything 50% off.”"},
    "Google — linee guida per rappresentare la vostra attività →":
        {"en": "Google — guidelines for representing your business →"},
    "Google — panoramica delle policy del Business Profile →":
        {"en": "Google — overview of Business Profile policies →"},
    "Una nota onesta sul nostro caso":
        {"en": "An honest note on our own case"},
    "Qui serve trasparenza, perché è facile spacciare la propria situazione per modello. La presenza su Google del nostro gruppo è storicamente registrata sotto il marchio dell’agenzia di traduzioni (ATT), non sotto Studio Remarka: non vi mostriamo «la nostra scheda perfetta» come esempio, perché non sarebbe onesto. Quello che vi diamo sono le regole che valgono per tutti, applicate come si deve — e il fatto, questo sì reale, che a Milano abbiamo un ufficio vero su cui una scheda locale poggia su un indirizzo che esiste.":
        {"en": "Here transparency matters, because it’s easy to pass your own situation off as a model. Our group’s presence on Google is historically registered under the translation agency’s brand (ATT), not under Studio Remarka: we don’t show you “our perfect profile” as an example, because that wouldn’t be honest. What we give you are the rules that apply to everyone, applied properly — plus the fact, and this one is real, that in Milan we have a real office on which a local listing rests on an address that exists."},
    "Il punto è proprio questo: una scheda Google funziona quando dietro c’è qualcosa di vero — un indirizzo, degli orari, un servizio reso davvero. Nessun trucco regge a lungo, e Google è sempre più bravo a smascherarli. La buona notizia è che la maggior parte dei vostri concorrenti la scheda non la cura affatto: bastano completezza, onestà e costanza per stare davanti.":
        {"en": "That’s exactly the point: a Google profile works when there’s something real behind it — an address, real hours, a service genuinely provided. No trick holds up for long, and Google keeps getting better at unmasking them. The good news is that most of your competitors don’t tend their profile at all: completeness, honesty and consistency are enough to stay ahead."},
    "La scheda è metà del lavoro: l’altra metà è il sito":
        {"en": "The profile is half the job: the other half is the site"},
    "Una scheda curata porta la persona a un passo dalla scelta; poi, spesso, quella persona clicca sul sito per confermare la decisione. Se il sito è lento, vecchio o poco chiaro, il lavoro fatto sulla scheda si perde all’ultimo metro. Scheda Google e sito lavorano in coppia: dati strutturati LocalBusiness, NAP coerente, contenuti locali e velocità sono ciò che tiene insieme le due metà. È SEO tecnica, ed è quella che mettiamo di serie.":
        {"en": "A well-tended profile brings the person a step from the choice; then, often, that person clicks through to the site to confirm the decision. If the site is slow, old or unclear, the work done on the profile is lost at the last metre. The Google profile and the site work as a pair: LocalBusiness structured data, a consistent NAP, local content and speed are what holds the two halves together. That’s technical SEO, and it’s what we deliver as standard."},
    "Da dove cominciare, in pratica? Rivendicate e verificate la scheda, completatela campo per campo, avviate una raccolta onesta di recensioni. In parallelo, misurate cosa dice di voi il sito oggi. E se volete il quadro completo del perché a Milano — e in ogni città competitiva — questa partita conti così tanto, l’abbiamo raccontato nell’articolo sulla SEO locale.":
        {"en": "Where to begin, in practice? Claim and verify the profile, complete it field by field, start an honest push for reviews. In parallel, measure what your site says about you today. And if you want the full picture of why in Milan — and in every competitive city — this game matters so much, we’ve told it in the article on local SEO."},
    "SEO tecnica e locale, a prezzo chiuso →":
        {"en": "Technical and local SEO, at a fixed price →"},
    "Analizza gratis la SEO on-page della vostra pagina →":
        {"en": "Analyse your page’s on-page SEO for free →"},
    "Leggi anche: SEO locale a Milano, come emergere →":
        {"en": "Read also: local SEO in Milan, how to stand out →"},
    "Che siate a Milano, Roma o Torino: dove lavoriamo →":
        {"en": "Whether you’re in Milan, Rome or Turin: where we work →"},
    "SEO tecnica e locale che lavora insieme alla scheda Google →":
        {"en": "Technical and local SEO that works alongside your Google profile →"},
    "Google — migliorare il ranking locale su Google":
        {"en": "Google — improve your local ranking on Google"},
    "La guida ufficiale: perché completezza, recensioni e verifica della scheda aiutano a comparire.":
        {"en": "The official guide: why completeness, reviews and profile verification help you appear."},
    "Google — linee guida per rappresentare la vostra attività":
        {"en": "Google — guidelines for representing your business"},
    "Le regole su nome, indirizzo e categorie: cosa è ammesso e cosa porta alla sospensione della scheda.":
        {"en": "The rules on name, address and categories: what’s allowed and what leads to profile suspension."},
    "Google — panoramica delle policy del Business Profile":
        {"en": "Google — overview of Business Profile policies"},
    "Le policy generali del profilo: contenuti proibiti e limitati, e come Google le applica.":
        {"en": "The profile’s general policies: prohibited and restricted content, and how Google enforces them."},
    "L’indagine annuale: quanto le recensioni pesano nella scelta di un’attività locale.":
        {"en": "The annual survey: how much reviews weigh in the choice of a local business."},

    # ============= Articolo 18 · Hreflang sito multilingue =============
    "Sito multilingue: hreflang senza mal di testa":
        {"en": "Multilingual website: hreflang without the headache"},
    "Un sito in più lingue mal collegato manda l’inglese a chi cerca in italiano e si fa concorrenza da solo. Cos’è l’hreflang, come si imposta senza errori e perché è ingegneria, non un plugin.":
        {"en": "A poorly linked multilingual site sends English to people searching in Italian and competes with itself. What hreflang is, how to set it up without errors and why it’s engineering, not a plugin."},
    "Avete tradotto il sito in inglese e tedesco, giustamente. Ma ora un cliente italiano cerca su Google e si ritrova la pagina inglese; un tedesco atterra sulla versione italiana; e le vostre due pagine — stesso contenuto, lingue diverse — si fanno concorrenza a vicenda nei risultati. Il colpevole è quasi sempre lo stesso: manca, o è sbagliato, l’hreflang. È l’attributo con cui si dice a Google «questa pagina è la versione italiana, quest’altra l’inglese, servile alla persona giusta». Si sente parlare di hreflang per un sito multilingue come di qualcosa di ostico: lo è, se lo si tratta come un plugin da attivare. Vediamo cos’è davvero, come si imposta senza errori e perché è ingegneria, non fortuna.":
        {"en": "You’ve translated the site into English and German, rightly so. But now an Italian customer searches Google and ends up on the English page; a German lands on the Italian version; and your two pages — same content, different languages — compete with each other in the results. The culprit is almost always the same: hreflang is missing or wrong. It’s the attribute that tells Google “this page is the Italian version, that one is English, serve each to the right person.” People talk about hreflang for a multilingual website as something forbidding: it is, if you treat it as a plugin to switch on. Let’s see what it really is, how to set it up without errors and why it’s engineering, not luck."},
    "Hreflang per un sito multilingue: le versioni italiana, inglese e tedesca collegate così che Google serva la lingua giusta":
        {"en": "Hreflang for a multilingual website: the Italian, English and German versions linked so Google serves the right language"},
    "Cos’è l’hreflang (in parole vostre)":
        {"en": "What hreflang is (in plain terms)"},
    "Immaginate di avere la stessa pagina in tre lingue: italiano, inglese, tedesco. Per un motore di ricerca sono tre indirizzi diversi con contenuti che si somigliano molto — e senza un’indicazione esplicita, Google deve indovinare quale mostrare a chi, rischiando di sbagliare o di considerarle contenuti duplicati. L’hreflang è quell’indicazione esplicita: un piccolo segnale, presente su ogni versione, che dice «esisto in queste lingue, ecco gli indirizzi di tutte, e io sono quella per l’italiano».":
        {"en": "Imagine you have the same page in three languages: Italian, English, German. To a search engine they’re three different addresses with contents that look very much alike — and without an explicit signal, Google has to guess which to show to whom, risking mistakes or treating them as duplicate content. Hreflang is that explicit signal: a small marker, present on every version, that says “I exist in these languages, here are the addresses of all of them, and I’m the one for Italian.”"},
    "La regola d’oro è la reciprocità: se la pagina italiana punta all’inglese, l’inglese deve puntare all’italiano, e ogni versione deve elencare tutte le altre — sé stessa compresa. Google, nella sua documentazione ufficiale sulle versioni localizzate, insiste proprio su questo: i riferimenti devono essere bidirezionali e completi, altrimenti li ignora. È qui che nascono la maggior parte dei mal di testa: non nel concetto, ma nella coerenza da mantenere su decine di pagine.":
        {"en": "The golden rule is reciprocity: if the Italian page points to the English one, the English must point back to the Italian, and every version must list all the others — itself included. Google, in its official documentation on localised versions, insists on exactly this: the references must be bidirectional and complete, or it ignores them. This is where most of the headaches come from: not in the concept, but in the consistency to maintain across dozens of pages."},
    "Come funziona l’hreflang in un sito multilingue: le versioni italiana, inglese e tedesca si citano a vicenda in modo reciproco":
        {"en": "How hreflang works in a multilingual website: the Italian, English and German versions cite each other reciprocally"},
    "L’hreflang collega le versioni di una pagina: ognuna dichiara sé stessa e tutte le altre, in modo reciproco (se IT punta a EN, EN deve puntare a IT). Così Google serve la lingua giusta e non le tratta come contenuti duplicati. Fonte: Google Search Central, versioni localizzate.":
        {"en": "Hreflang links the versions of a page: each declares itself and all the others, reciprocally (if IT points to EN, EN must point to IT). This way Google serves the right language and doesn’t treat them as duplicate content. Source: Google Search Central, localised versions."},
    "Gli errori che rompono un sito multilingue":
        {"en": "The mistakes that break a multilingual website"},
    "Quasi tutti i problemi di hreflang nascono da pochi errori ricorrenti. Conoscerli è metà del lavoro, perché sono quasi sempre gli stessi.":
        {"en": "Almost every hreflang problem comes from a few recurring mistakes. Knowing them is half the job, because they’re almost always the same ones."},
    "Riferimenti non reciproci: la pagina IT cita la EN, ma la EN non ricambia. Google scarta l’intera coppia e torna a indovinare.":
        {"en": "Non-reciprocal references: the IT page cites the EN one, but the EN doesn’t reciprocate. Google discards the whole pair and goes back to guessing."},
    "Codici lingua sbagliati: «en-UK» non esiste (è «en-GB»), e un codice inventato viene ignorato in silenzio.":
        {"en": "Wrong language codes: “en-UK” doesn’t exist (it’s “en-GB”), and a made-up code is silently ignored."},
    "URL relativi o pagine che rimandano a versioni in «noindex»: l’hreflang deve puntare a indirizzi assoluti e indicizzabili, o non serve a nulla.":
        {"en": "Relative URLs or pages pointing to “noindex” versions: hreflang must point to absolute, indexable addresses, or it’s useless."},
    "Manca l’autoreferenza: ogni versione deve elencare anche sé stessa. Dimenticarlo è l’errore più comune e più silenzioso.":
        {"en": "The self-reference is missing: every version must also list itself. Forgetting it is the most common and most silent mistake."},
    "Google — dire a Google le versioni localizzate (hreflang) →":
        {"en": "Google — tell Google about localised versions (hreflang) →"},
    "Hreflang non è tutto: la lingua deve suonare vera":
        {"en": "Hreflang isn’t everything: the language has to ring true"},
    "C’è un equivoco da smontare: l’hreflang risolve il «quale versione mostrare», non il «la versione è buona». Potete avere l’hreflang perfetto e perdere comunque il cliente, se la traduzione suona finta. Una scheda prodotto tradotta a macchina, con un registro sbagliato, allontana chi la legge nella propria lingua — e nessun attributo tecnico lo compensa. La ricerca di CSA («Can’t Read, Won’t Buy») lo dice da anni: le persone comprano molto più volentieri nella propria lingua, e diffidano dei testi che suonano stranieri.":
        {"en": "There’s a misconception to dismantle: hreflang solves “which version to show,” not “the version is any good.” You can have perfect hreflang and still lose the customer if the translation sounds fake. A machine-translated product page with the wrong register drives away the person reading it in their own language — and no technical attribute makes up for that. CSA’s research (“Can’t Read, Won’t Buy”) has said it for years: people buy far more willingly in their own language, and distrust text that sounds foreign."},
    "Per questo, da noi, il multilingue è due mestieri in uno: l’ingegneria che collega le versioni (hreflang, sitemap, struttura degli URL) e i redattori madrelingua che scrivono, non traducono a macchina. Le lingue le curano madrelingua del gruppo Remarka, nel settore dal 2001, selezionati da una piattaforma di test interna che scarta la stragrande maggioranza dei candidati — la stessa che tiene la qualità di ogni nostro progetto multilingue. E se un mercato ha regole proprie — per la Germania, l’Austria — la parte tecnica va oltre l’hreflang: è la gestione dei siti multi-regionali.":
        {"en": "That’s why, for us, multilingual is two crafts in one: the engineering that links the versions (hreflang, sitemap, URL structure) and the native-speaking editors who write, rather than machine-translate. The languages are handled by native speakers of the Remarka group, in the field since 2001, selected by an internal testing platform that rejects the vast majority of candidates — the same one that holds the quality of every multilingual project of ours. And if a market has its own rules — for Germany, Austria — the technical part goes beyond hreflang: it’s the handling of multi-regional sites."},
    "Google — gestire i siti multi-regionali e multilingue →":
        {"en": "Google — managing multi-regional and multilingual sites →"},
    "La piattaforma che seleziona chi traduce (solo l’8% passa) →":
        {"en": "The platform that selects who translates (only 8% pass) →"},
    "Come si tiene in ordine, senza impazzire":
        {"en": "How to keep it in order, without losing your mind"},
    "Il segreto per non impazzire con l’hreflang è non gestirlo a mano. Su decine di pagine e tre lingue, mantenere a mano i riferimenti reciproci è una fonte inesauribile di errori. La soluzione è generare l’hreflang da un’unica mappa delle corrispondenze — una fonte di verità sola, da cui ogni pagina eredita i propri collegamenti — così che aggiungere una pagina non significhi aggiornarne trenta. È esattamente l’approccio con cui è costruito questo sito: italiano alla radice, inglese e russo come alberi coerenti, collegati da una mappa che non si tocca a mano.":
        {"en": "The secret to not losing your mind over hreflang is not managing it by hand. Across dozens of pages and three languages, keeping reciprocal references by hand is an endless source of errors. The solution is to generate hreflang from a single map of correspondences — one source of truth, from which every page inherits its own links — so that adding a page doesn’t mean updating thirty. It’s exactly the approach this site is built on: Italian at the root, English and Russian as coherent trees, linked by a map that’s never touched by hand."},
    "In pratica, prima di aggiungere lingue conviene verificare come Google legge già il vostro sito: se le versioni esistenti si citano correttamente, se ci sono codici sbagliati, se qualcosa finisce fuori indice. Un’analisi SEO on-page fa emergere questi problemi prima che costino posizioni. E se state pensando non solo a tradurre ma ad aprire un mercato estero per davvero, l’hreflang è solo il primo pezzo di un discorso più grande: quello dell’export digitale.":
        {"en": "In practice, before adding languages it’s worth checking how Google already reads your site: whether the existing versions cite each other correctly, whether there are wrong codes, whether something ends up out of the index. An on-page SEO analysis surfaces these problems before they cost you positions. And if you’re thinking not just of translating but of opening a foreign market for real, hreflang is only the first piece of a bigger picture: digital export."},
    "Analizza gratis la SEO on-page della vostra pagina →":
        {"en": "Analyse your page’s on-page SEO for free →"},
    "Progettiamo il vostro sito multilingue a prezzo chiuso →":
        {"en": "We design your multilingual site at a fixed price →"},
    "Leggi anche: export digitale, il sito che apre mercati esteri →":
        {"en": "Read also: digital export, the site that opens foreign markets →"},
    "Siti multilingue con hreflang e madrelingua, a prezzo chiuso →":
        {"en": "Multilingual sites with hreflang and native speakers, at a fixed price →"},
    "Google Search Central — versioni localizzate (hreflang)":
        {"en": "Google Search Central — localised versions (hreflang)"},
    "La documentazione ufficiale: come dichiarare le versioni per lingua, con riferimenti reciproci e completi.":
        {"en": "The official documentation: how to declare versions by language, with reciprocal and complete references."},
    "Google Search Central — siti multi-regionali e multilingue":
        {"en": "Google Search Central — multi-regional and multilingual sites"},
    "Come gestire lingua e Paese insieme: struttura degli URL, targeting e insidie da evitare.":
        {"en": "How to handle language and country together: URL structure, targeting and pitfalls to avoid."},
    "CSA Research — «Can’t Read, Won’t Buy»":
        {"en": "CSA Research — “Can’t Read, Won’t Buy”"},
    "La ricerca sul comportamento d’acquisto: le persone comprano molto più volentieri nella propria lingua.":
        {"en": "The research on buying behaviour: people buy far more willingly in their own language."},

    # ============= Articolo 19 · Sito per l’export =============
    "Export digitale: il sito che apre mercati esteri":
        {"en": "Digital export: the website that opens foreign markets"},
    "Vendere all’estero non è tradurre la home. Cosa serve davvero a un sito per l’export — lingue native, SEO internazionale, pagamenti e fiducia — e i casi reali che l’hanno fatto.":
        {"en": "Selling abroad isn’t translating the home page. What a website for export really needs — native languages, international SEO, payments and trust — and the real cases that did it."},
    "Un’azienda manifatturiera bresciana fa il 40% del fatturato in Germania, ma il suo sito è solo in italiano — e i clienti tedeschi ordinano per telefono, quando va bene. Una guest house sul lago di Como riempie le stanze con ospiti stranieri, ma online si presenta in una lingua sola. È lo spreco silenzioso di tantissime PMI italiane: il prodotto è pronto per l’estero, il sito no. Un sito per l’export non è la home tradotta con un plugin: è uno strumento pensato per farsi trovare, capire e scegliere da chi vive in un altro mercato. Vediamo cosa serve davvero, e i casi reali del gruppo Remarka che l’hanno fatto — con numeri, non promesse.":
        {"en": "A manufacturer near Brescia makes 40% of its revenue in Germany, but its site is only in Italian — and German customers order by phone, when things go well. A guest house on Lake Como fills its rooms with foreign guests, yet online it shows up in a single language. It’s the silent waste of so many Italian SMBs: the product is ready for abroad, the site isn’t. A website for export isn’t the home page translated with a plugin: it’s a tool built to be found, understood and chosen by people who live in another market. Let’s see what it really needs, and the real Remarka group cases that did it — with numbers, not promises."},
    "Un sito per l’export che apre mercati esteri: lingue native, SEO internazionale, pagamenti e fiducia oltre confine":
        {"en": "A website for export that opens foreign markets: native languages, international SEO, payments and trust across borders"},
    "Perché «tradurre la home» non è export":
        {"en": "Why “translating the home page” isn’t export"},
    "L’errore di partenza è pensare all’export come a un problema di traduzione. Tradurre è l’ultimo strato, non il primo. Un sito per l’export deve rispondere a domande che la versione italiana non si pone: la persona in Germania trova il sito quando cerca nella sua lingua? Capisce come comprare, con quali pagamenti, in quale valuta? Si fida di un’azienda straniera che non conosce? Se anche una sola di queste risposte è «no», la traduzione più bella del mondo non porta un ordine.":
        {"en": "The starting mistake is to think of export as a translation problem. Translation is the last layer, not the first. A website for export has to answer questions the Italian version never asks: does the person in Germany find the site when they search in their own language? Do they understand how to buy, with which payments, in which currency? Do they trust a foreign company they don’t know? If even one of these answers is “no,” the finest translation in the world won’t bring an order."},
    "La statistica di fondo è impietosa. La ricerca di CSA Research («Can’t Read, Won’t Buy») mostra che la stragrande maggioranza dei consumatori compra molto più volentieri nella propria lingua, e molti evitano del tutto i siti che non la parlano. E l’e-commerce transfrontaliero, dicono i dati Eurostat, è una fetta in crescita ma ancora frenata proprio da lingua, fiducia e logistica. L’export digitale è colmare quel divario, non solo aprire il traduttore automatico.":
        {"en": "The underlying statistic is unforgiving. CSA Research’s study (“Can’t Read, Won’t Buy”) shows that the vast majority of consumers buy far more willingly in their own language, and many avoid altogether the sites that don’t speak it. And cross-border e-commerce, Eurostat data says, is a growing slice still held back by exactly this: language, trust and logistics. Digital export is about closing that gap, not just firing up the machine translator."},
    "Cosa serve davvero a un sito per l’export":
        {"en": "What a website for export really needs"},
    "Un sito che vende all’estero poggia su quattro pilastri, e la traduzione è solo uno dei quattro. Toglietene uno e il mercato resta chiuso.":
        {"en": "A site that sells abroad rests on four pillars, and translation is only one of the four. Remove one and the market stays shut."},
    "Lingue native, non automatiche: testi scritti da chi la lingua la vive, con il registro giusto per quel mercato. È il pilastro della fiducia.":
        {"en": "Native, not automatic languages: copy written by people who live the language, with the right register for that market. It’s the pillar of trust."},
    "SEO internazionale: hreflang corretto, struttura per lingua e Paese, contenuti pensati per come si cerca là. Se non vi trovano, non esistete.":
        {"en": "International SEO: correct hreflang, a structure by language and country, content built for how people search there. If they don’t find you, you don’t exist."},
    "Pagamenti e valute locali: i metodi che quel mercato usa davvero, non solo la carta. In Germania, per dire, contano mezzi diversi dai nostri.":
        {"en": "Local payments and currencies: the methods that market actually uses, not just cards. In Germany, for instance, different means matter than ours."},
    "Fiducia oltre confine: informazioni chiare su spedizioni, resi, tempi e assistenza nella lingua del cliente. La fiducia si costruisce sui dettagli.":
        {"en": "Trust across borders: clear information on shipping, returns, timings and support in the customer’s language. Trust is built on details."},
    "I quattro pilastri di un sito per l’export: lingue native, SEO internazionale, pagamenti locali e fiducia oltre confine":
        {"en": "The four pillars of a website for export: native languages, international SEO, local payments and trust across borders"},
    "Un sito per l’export poggia su quattro pilastri: lingue native (non automatiche), SEO internazionale (hreflang e struttura per mercato), pagamenti e valute locali, fiducia oltre confine (spedizioni, resi, assistenza nella lingua del cliente). La traduzione è uno dei quattro, non il tutto. Fonti: CSA Research, Eurostat.":
        {"en": "A website for export rests on four pillars: native languages (not automatic), international SEO (hreflang and a structure by market), local payments and currencies, trust across borders (shipping, returns, support in the customer’s language). Translation is one of the four, not the whole. Sources: CSA Research, Eurostat."},
    "I casi reali: chi ha aperto un mercato per davvero":
        {"en": "The real cases: who opened a market for real"},
    "Non parliamo in teoria. Una guest house sul lago di Como, ukrinitsy.ru, dopo un sito vetrina veloce e in più lingue ha visto le prenotazioni dirette crescere di oltre il 450% in una stagione: gli ospiti stranieri prenotano dal sito, senza passare dai portali. Un’agenzia del gruppo, con пере.рф, è arrivata al primo posto su Yandex per le query di settore con la sola SEO tecnica su un dominio-caso-limite — la prova che il posizionamento in un mercato estero lo fa l’ingegneria, non la fortuna del nome.":
        {"en": "We’re not talking in theory. A guest house on Lake Como, ukrinitsy.ru, after a fast, multilingual brochure site saw direct bookings grow by over 450% in a season: foreign guests book from the site, without going through portals. A group agency, with пере.рф, reached the top spot on Yandex for its industry queries with technical SEO alone on an edge-case domain — proof that ranking in a foreign market is made by engineering, not by a lucky name."},
    "E c’è il caso che conosciamo meglio, perché è il nostro biglietto da visita: ATT (traduzione.tech) lavora su oltre 40 combinazioni e direzioni linguistiche, con un sito costruito per parlare la lingua del cliente B2B in ogni mercato. La stessa ingegneria — lingue native, SEO internazionale, struttura pulita — è quella che mettiamo in un sito export-ready per voi. I casi, con il link al progetto vivo, sono tutti aperti e verificabili.":
        {"en": "And there’s the case we know best, because it’s our calling card: ATT (traduzione.tech) works across more than 40 language pairs and directions, with a site built to speak the B2B customer’s language in every market. The same engineering — native languages, international SEO, a clean structure — is what we put into an export-ready site for you. The cases, each with a link to the live project, are all open and verifiable."},
    "Sito export-ready: cosa include e per quali mercati →":
        {"en": "Export-ready website: what it includes and for which markets →"},
    "I casi reali del gruppo, con link al progetto vivo →":
        {"en": "The group’s real cases, with a link to the live project →"},
    "Quanto rende: misurare prima di partire":
        {"en": "How much it returns: measuring before you start"},
    "Aprire un mercato costa, ed è giusto chiedersi se rende prima di partire. La domanda non è «quanto costa tradurre», ma «quanto vale un cliente in più in quel mercato, e quanti ne servono per ripagare il lavoro». Un catalogo tradotto da madrelingua e un checkout ridotto all’osso sono le due leve che spostano più vendite dirette all’estero — ma vanno dimensionate sul ritorno atteso, non sull’entusiasmo. Meglio partire da un mercato solo, fatto bene, che da cinque fatti a metà.":
        {"en": "Opening a market costs money, and it’s right to ask whether it pays before you start. The question isn’t “how much does translation cost,” but “how much is one more customer worth in that market, and how many do we need to pay back the work.” A catalogue translated by native speakers and a checkout stripped to the bone are the two levers that shift the most direct sales abroad — but they must be sized against the expected return, not against enthusiasm. Better to start with one market done well than five done by halves."},
    "Uno strumento per iniziare a ragionare c’è: un calcolo del ritorno della localizzazione, che mette in fila costo del lavoro linguistico e vendite potenziali per capire da quale lingua conviene partire. E se il primo mercato è dietro l’angolo — la Germania, l’Austria, la Svizzera per chi esporta manifattura — il pezzo tecnico da non sbagliare resta quello dell’hreflang, che abbiamo raccontato a parte.":
        {"en": "There’s a tool to start reasoning with: a localisation-return calculation that lines up the cost of the language work and the potential sales to work out which language to start from. And if the first market is right next door — Germany, Austria, Switzerland for those exporting manufacturing — the technical piece not to get wrong is still hreflang, which we’ve covered separately."},
    "Leggi anche: sito multilingue, hreflang senza mal di testa →":
        {"en": "Read also: multilingual website, hreflang without the headache →"},
    "Sito export-ready per i vostri mercati esteri, a prezzo chiuso →":
        {"en": "An export-ready site for your foreign markets, at a fixed price →"},
    "La ricerca sul comportamento d’acquisto: la maggioranza compra nella propria lingua ed evita i siti che non la parlano.":
        {"en": "The research on buying behaviour: the majority buy in their own language and avoid sites that don’t speak it."},
    "Eurostat — statistiche sull’e-commerce":
        {"en": "Eurostat — e-commerce statistics"},
    "I dati europei: quanto pesa l’e-commerce transfrontaliero e cosa ancora lo frena.":
        {"en": "The European data: how much cross-border e-commerce weighs and what still holds it back."},
    "Google Search Central — siti multi-regionali e multilingue":
        {"en": "Google Search Central — multi-regional and multilingual sites"},
    "Come impostare lingua e Paese per farsi trovare correttamente nei mercati esteri.":
        {"en": "How to set up language and country to get found correctly in foreign markets."},

    # ============= Articolo 20 · Manutenzione WordPress =============
    "Manutenzione WordPress: cosa succede se non la fate":
        {"en": "WordPress maintenance: what happens if you skip it"},
    "Un WordPress non aggiornato non «resta com’è»: invecchia, si buca e un giorno non si apre più. Cosa comporta la manutenzione, cosa rischia chi la salta e perché non è un costo ma un’assicurazione.":
        {"en": "An un-updated WordPress doesn’t “stay as it is”: it ages, it gets breached and one day it stops opening. What maintenance involves, what those who skip it risk, and why it’s not a cost but insurance."},
    "«Il sito funziona, perché pagare la manutenzione?» È la domanda con cui si risparmiano cento euro l’anno e se ne perdono mille in una notte. Un sito WordPress non è un quadro appeso al muro: è un software vivo, fatto di un core, di plugin e di un tema che il mondo intorno — browser, PHP, standard di sicurezza — continua a cambiare. Non aggiornarlo non vuol dire «lasciarlo com’è»: vuol dire lasciarlo invecchiare finché un giorno non si apre più, o peggio, finché qualcuno ci entra. Vediamo cosa comporta davvero la manutenzione di un sito WordPress, cosa rischia chi la salta, e perché non è un costo ma un’assicurazione.":
        {"en": "“The site works, why pay for maintenance?” It’s the question that saves you a hundred euros a year and loses you a thousand in one night. A WordPress site isn’t a painting on the wall: it’s living software, made of a core, of plugins and of a theme that the world around it — browsers, PHP, security standards — keeps changing. Not updating it doesn’t mean “leaving it as it is”: it means letting it age until one day it stops opening, or worse, until someone gets in. Let’s see what maintaining a WordPress site really involves, what those who skip it risk, and why it’s not a cost but insurance."},
    "Manutenzione WordPress: backup, aggiornamenti, test e monitoraggio che tengono un sito sicuro e in piedi nel tempo":
        {"en": "WordPress maintenance: backups, updates, testing and monitoring that keep a site secure and standing over time"},
    "Perché un WordPress non «resta com’è»":
        {"en": "Why a WordPress doesn’t “stay as it is”"},
    "WordPress fa girare una fetta enorme del web, e questa diffusione ha un rovescio: è anche il bersaglio preferito di chi cerca falle da sfruttare. Il core è mantenuto bene e riceve aggiornamenti di sicurezza in continuazione — spesso automatici — ma il sito non è solo il core: è il core più i plugin più il tema. Ed è lì che si apre il problema. Secondo il report annuale di Patchstack sulla sicurezza di WordPress, la quasi totalità delle vulnerabilità scoperte non sta nel core, ma nei plugin e nei temi di terze parti.":
        {"en": "WordPress runs a huge slice of the web, and that reach has a flip side: it’s also the favourite target of those hunting for exploitable holes. The core is well maintained and gets security updates constantly — often automatic — but the site isn’t just the core: it’s the core plus the plugins plus the theme. And that’s where the problem opens up. According to Patchstack’s annual WordPress security report, almost all discovered vulnerabilities are not in the core, but in third-party plugins and themes."},
    "Il dato è netto: nel 2024 sono state trovate quasi ottomila nuove vulnerabilità nell’ecosistema WordPress, e circa il 96% riguardava i plugin. Ogni plugin non aggiornato è una porta che qualcuno, prima o poi, prova ad aprire. Non aggiornare non congela il sito in uno stato sicuro: lo lascia esposto a falle che diventano pubbliche e sfruttabili col passare dei mesi. Il «resta com’è» è un’illusione — quello che resta è solo il rischio, che cresce.":
        {"en": "The figure is stark: in 2024 almost eight thousand new vulnerabilities were found in the WordPress ecosystem, and around 96% concerned plugins. Every un-updated plugin is a door someone, sooner or later, tries to open. Not updating doesn’t freeze the site in a secure state: it leaves it exposed to holes that become public and exploitable as the months pass. “Staying as it is” is an illusion — what stays is only the risk, and it grows."},
    "Cosa comporta la manutenzione (fatta bene)":
        {"en": "What maintenance involves (done right)"},
    "Manutenzione non vuol dire «cliccare aggiorna a caso». Vuol dire un ciclo ordinato che tiene il sito sicuro, veloce e recuperabile. Sono poche cose, ma vanno fatte con metodo — la documentazione ufficiale di WordPress.org insiste su ognuna di esse.":
        {"en": "Maintenance doesn’t mean “clicking update at random.” It means an orderly cycle that keeps the site secure, fast and recoverable. It’s a few things, but they must be done methodically — the official WordPress.org documentation insists on every one of them."},
    "Backup prima di ogni intervento: database e file, completi e verificati. Senza un backup che funziona, un aggiornamento andato male è un disastro; con quello, è un contrattempo di dieci minuti.":
        {"en": "Backup before every intervention: database and files, complete and verified. Without a working backup, an update gone wrong is a disaster; with one, it’s a ten-minute setback."},
    "Aggiornamenti controllati: core, plugin e tema aggiornati con criterio, testati prima su un ambiente di prova quando l’aggiornamento è delicato — non alla cieca sul sito vivo.":
        {"en": "Controlled updates: core, plugins and theme updated with judgment, tested first on a staging environment when the update is delicate — not blindly on the live site."},
    "Sicurezza e hardening: password forti, accessi limitati, plugin inutilizzati rimossi (un plugin disattivato ma presente può ancora essere sfruttato).":
        {"en": "Security and hardening: strong passwords, limited access, unused plugins removed (a deactivated but still-present plugin can still be exploited)."},
    "Monitoraggio: uptime, velocità e integrità controllati nel tempo, così un problema si vede prima che lo veda un cliente.":
        {"en": "Monitoring: uptime, speed and integrity checked over time, so a problem is spotted before a customer spots it."},
    "Il ciclo di manutenzione di un sito WordPress: backup, aggiornamenti controllati, test, hardening e monitoraggio":
        {"en": "The maintenance cycle of a WordPress site: backup, controlled updates, testing, hardening and monitoring"},
    "Il ciclo della manutenzione WordPress fatta bene: backup completo, aggiornamenti controllati (core, plugin, tema), test su ambiente di prova, hardening e monitoraggio continuo. Il 96% delle vulnerabilità sta nei plugin: aggiornarli con metodo è la difesa principale. Fonti: WordPress.org, Patchstack.":
        {"en": "The cycle of WordPress maintenance done right: full backup, controlled updates (core, plugins, theme), testing on a staging environment, hardening and continuous monitoring. 96% of vulnerabilities are in plugins: updating them methodically is the main defence. Sources: WordPress.org, Patchstack."},
    "Cosa rischia chi la salta":
        {"en": "What those who skip it risk"},
    "I rischi non sono ipotesi da manuale, sono le telefonate che riceviamo. Il sito bucato che rimanda a pagine di spam o distribuisce malware — e Google lo segnala come «pericoloso» ai visitatori, bruciando in un giorno anni di reputazione. Il sito che dopo un aggiornamento di PHP del server smette semplicemente di aprirsi, perché un plugin fermo a tre anni fa non è più compatibile. La schermata bianca senza backup, con l’unica copia «da qualche parte» che nessuno trova.":
        {"en": "The risks aren’t textbook hypotheses, they’re the phone calls we get. The breached site that redirects to spam pages or serves malware — and Google flags it as “dangerous” to visitors, burning years of reputation in a day. The site that, after a server PHP update, simply stops opening, because a plugin frozen three years ago is no longer compatible. The white screen with no backup, the only copy “somewhere” that nobody can find."},
    "E poi c’è il costo silenzioso, quello che non fa rumore: il modulo contatti che ha smesso di inviare email da mesi e nessuno se n’è accorto, le richieste dei clienti finite nel vuoto. La manutenzione non è la voce di spesa che sembra: è ciò che tiene lontani questi disastri, e quasi sempre costa una frazione di quello che costa rimediare dopo. Un check-up periodico è il modo più economico per sapere in che stato è davvero il vostro sito, prima che ve lo dica un cliente.":
        {"en": "And then there’s the silent cost, the one that makes no noise: the contact form that stopped sending emails months ago and nobody noticed, customer enquiries fallen into the void. Maintenance isn’t the expense line it seems: it’s what keeps these disasters away, and it almost always costs a fraction of what fixing them afterwards costs. A periodic check-up is the cheapest way to know what state your site is really in, before a customer tells you."},
    "WordPress.org — aggiornare WordPress →":
        {"en": "WordPress.org — updating WordPress →"},
    "Misura gratis la salute tecnica del vostro sito →":
        {"en": "Measure your site’s technical health for free →"},
    "Il nostro approccio: inclusa, poi facoltativa":
        {"en": "Our approach: included, then optional"},
    "Sappiamo che «manutenzione» suona come un abbonamento imposto, e non ci piace nemmeno a noi. Per questo nei siti che consegniamo i primi 12 mesi di assistenza, aggiornamenti e misurazioni sono inclusi nel prezzo di costruzione, senza sorprese. Dopo, il canone è facoltativo — oppure il sito resta a voi così com’è: codice e dati sono vostri dal primo giorno. Nessun ricatto tecnico, nessuna dipendenza forzata.":
        {"en": "We know “maintenance” sounds like an imposed subscription, and we don’t like it either. That’s why, on the sites we deliver, the first 12 months of support, updates and measurements are included in the build price, no surprises. After that, the fee is optional — or the site stays with you as it is: code and data are yours from day one. No technical blackmail, no forced dependency."},
    "E non lo diciamo in astratto: teniamo in manutenzione continua 28 progetti, e mandiamo avanti da due anni un gestionale interno — il TMS del gruppo — che gestisce oltre 2.000 ordini l’anno e non può permettersi di fermarsi un’ora. La manutenzione la facciamo prima di tutto sui nostri sistemi, con i nostri soldi e la nostra reputazione in gioco. È la stessa cura, e la stessa ingegneria, che mettiamo in un sito aziendale per voi.":
        {"en": "And we don’t say it in the abstract: we keep 28 projects under continuous maintenance, and for two years we’ve been running an internal management system — the group’s TMS — that handles over 2,000 orders a year and can’t afford to be down for an hour. We do maintenance first of all on our own systems, with our own money and reputation on the line. It’s the same care, and the same engineering, we put into a business website for you."},
    "Un sito aziendale con manutenzione inclusa i primi 12 mesi →":
        {"en": "A business website with maintenance included for the first 12 months →"},
    "Fate il check-up del vostro sito attuale, gratis →":
        {"en": "Run a check-up on your current site, for free →"},
    "Leggi anche: hosting in Italia o in cloud, velocità e GDPR →":
        {"en": "Read also: hosting in Italy or the cloud, speed and GDPR →"},
    "Un sito aziendale con 12 mesi di manutenzione inclusa, a prezzo chiuso →":
        {"en": "A business website with 12 months of maintenance included, at a fixed price →"},
    "WordPress.org — aggiornare WordPress":
        {"en": "WordPress.org — updating WordPress"},
    "La documentazione ufficiale: perché il backup prima di ogni aggiornamento è il passo che non si salta.":
        {"en": "The official documentation: why a backup before every update is the step you never skip."},
    "WordPress.org — hardening (mettere in sicurezza WordPress)":
        {"en": "WordPress.org — hardening (securing WordPress)"},
    "Le misure ufficiali per ridurre la superficie d’attacco: accessi, plugin, permessi.":
        {"en": "The official measures to reduce the attack surface: access, plugins, permissions."},
    "Patchstack — State of WordPress Security 2024":
        {"en": "Patchstack — State of WordPress Security 2024"},
    "Il report annuale: quasi 8.000 vulnerabilità nel 2024, circa il 96% nei plugin, pochissime nel core.":
        {"en": "The annual report: almost 8,000 vulnerabilities in 2024, around 96% in plugins, very few in the core."},
}
CHROME.update(CHROME_BLOG_BATCH4)

# Batch 4 — blocco ufficio + mappa click-to-load, indirizzi pubblici owner
# 17.07.2026 (piano-geo-citta.md, batch U1). Usato su Milano/Torino/Roma;
# solo Milano ha una pagina EN (/en/milan/), quindi solo le stringhe che
# compaiono lì hanno bisogno di una traduzione EN (le altre restano inerti,
# non tradotte, ed è corretto così — nessuna pagina EN le legge).
CHROME.update({
    "Ci incontriamo di persona": {"en": "We meet in person", "ru": "Встречаемся лично"},
    "Un ufficio vero a Milano, su appuntamento": {"en": "A real office in Milan, by appointment", "ru": "Настоящий офис в Милане, по предварительной записи"},
    "L’indirizzo è pubblico e l’ufficio è vero: ci veniamo a incontrare di persona, su appuntamento, per analizzare insieme il sito attuale e uscire con le priorità scritte nero su bianco. Il primo incontro non si paga.": {
        "en": "The address is public and the office is real: we meet here in person, by appointment, to review your current site together and walk away with priorities written down in black and white. The first meeting is free.",
        "ru": "Адрес открыт, а офис настоящий: мы встречаемся здесь лично, по предварительной записи, разбираем ваш нынешний сайт и уходите вы с приоритетами, зафиксированными чёрным по белому. Первая встреча бесплатна.",
    },
    "L’ufficio è quello del gruppo Remarka, condiviso con ATT · Agenzia di Traduzione Tecnica, la nostra agenzia di traduzioni dal 2001: su Google Maps la sede è registrata con quel nome — non stupitevi cliccando la mappa, siamo sempre noi.": {
        "en": "The office belongs to the Remarka group and is shared with ATT · Agenzia di Traduzione Tecnica, our translation agency since 2001: on Google Maps the listing is registered under that name — don’t be surprised when you click the map, it’s still us.",
        "ru": "Офис принадлежит группе Remarka и используется совместно с ATT · Agenzia di Traduzione Tecnica — нашим переводческим бюро, работающим с 2001 года: на Google Maps карточка зарегистрирована под этим названием — не удивляйтесь, кликнув по карте, это по-прежнему мы.",
    },
    "Solo su appuntamento": {"en": "By appointment only", "ru": "Только по предварительной записи"},
    "Apri la mappa": {"en": "Open the map", "ru": "Открыть карту"},
    "Il pulsante carica una mappa di Google: nessuna richiesta a Google finché non lo attivate.": {
        "en": "The button loads a Google map: no request is sent to Google until you activate it.",
        "ru": "Кнопка загружает карту Google: запрос к Google не отправляется, пока вы её не активируете.",
    },
    "Apri in Google Maps →": {"en": "Open in Google Maps →", "ru": "Открыть в Google Maps →"},
    "Fissa un appuntamento →": {"en": "Book an appointment →", "ru": "Записаться на встречу →"},
    "Milano, 20144, Vicolo Privato Lavandai, 2a": {"en": "Milan, 20144, Vicolo Privato Lavandai, 2a", "ru": "Милан, 20144, Vicolo Privato Lavandai, 2a"},
    "Realizzazione siti web a Milano: Studio Remarka, ufficio in città": {
        "en": "Website development in Milan: Studio Remarka, our office in the city",
        "ru": "Разработка сайтов в Милане: Studio Remarka, наш офис в городе",
    },
    "Non è obbligatorio: analisi, preventivo e avanzamento lavori passano da videochiamate e da un ambiente di prova online. Ma se siete a Milano, il caffè lo offriamo noi: il nostro ufficio è in Vicolo Privato Lavandai, 2a, 20144 Milano, solo su appuntamento.": {
        "en": "It’s not required: analysis, quote and progress reviews all run through video calls and an online staging environment. But if you’re in Milan, the coffee is on us: our office is at Vicolo Privato Lavandai, 2a, 20144 Milan, by appointment only.",
        "ru": "Это не обязательно: анализ, смета и ход работ идут через видеозвонки и онлайн-среду для проверки. Но если вы в Милане, кофе — за наш счёт: наш офис находится по адресу Vicolo Privato Lavandai, 2a, 20144 Милан, только по предварительной записи.",
    },
    # Fix owner U1: rimosso il riferimento a "zona Solari" (indirizzo
    # placeholder mai reale, sostituito dal vero indirizzo pubblico).
    "No: Milano e tutta la provincia, più Monza e Brianza. Il primo incontro non si paga, da voi o nel nostro ufficio a Milano.": {
        "en": "No: Milan and the whole province, plus Monza and Brianza. The first meeting is free, at your office or at ours in Milan.",
        "ru": "Нет: Милан и вся провинция, плюс Монца и Брианца. Первая встреча бесплатна — у вас или в нашем офисе в Милане.",
    },
})

# CHROME_BLOG_INDEX — redesign dell'indice blog (richiesta del titolare
# 17.07): eyebrow «In evidenza» delle 2 card di copertina e le etichette del
# filtro a chip per rubrica (generate_pages.py:BLOG_RUBRICHE). Solo EN: il
# blog RU resta un batch a sé (ru-blog-index.php non passa dal conveyor).
CHROME_BLOG_INDEX = {
    "In evidenza": {"en": "Featured"},
    "Tutti": {"en": "All"},
    "SEO e visibilità AI": {"en": "SEO & AI visibility"},
    "Norme e accessibilità": {"en": "Rules & accessibility"},
    "Prezzi e decisioni": {"en": "Pricing & decisions"},
    "Tecnologie che vendono": {"en": "Tech that sells"},
    "Velocità e sostenibilità": {"en": "Speed & sustainability"},
}
CHROME.update(CHROME_BLOG_INDEX)

# Alt-text delle grafiche ritagliate dal mockup owner sull'indice strumenti
# (18.07.2026, docs pilota: nessun redisegno SVG, PNG sorgente ritagliato in
# assets/img/tools/). Solo EN: RU si scrive a mano nel proprio file
# (translate_pages.py ru è vietato).
CHROME_TOOLS_IMG_ALT = {
    "Dashboard del check-up con punteggio di salute 87 su 100 e grafico delle prestazioni":
        {"en": "Check-up dashboard showing an 87/100 health score and a performance chart"},
    "Grafico dell’andamento di velocità e tachimetro del punteggio PageSpeed":
        {"en": "Speed trend chart and gauge showing the PageSpeed score"},
    "Checklist SEO on-page e grafico di crescita della visibilità in ricerca":
        {"en": "On-page SEO checklist and a rising search visibility chart"},
    "Icone di verifica cookie, informative privacy e badge di conformità GDPR":
        {"en": "Icons for cookie check, privacy notices and a GDPR compliance badge"},
    "Grafico a barre crescenti con icona di ritorno economico della localizzazione":
        {"en": "Rising bar chart with a return-on-investment icon for localization"},
    "Icona di accessibilità con indicatori di conformità verificati":
        {"en": "Accessibility icon with verified compliance indicators"},
    "Diagramma di segnali tecnici collegati e checklist di prontezza per l’AI":
        {"en": "Diagram of connected technical signals and an AI-readiness checklist"},
    "Grafico dell’impronta di CO₂ generata dalle visite al sito":
        {"en": "Chart of the CO₂ footprint generated by site visits"},
    "Quattro icone dei pilastri E-E-A-T: esperienza, autorevolezza, verifica e affidabilità":
        {"en": "Four icons for the E-E-A-T pillars: experience, authoritativeness, verification and trust"},
    "Blocchi di testo della pagina analizzati e icona a forma di occhio dell’AI":
        {"en": "Analyzed page text blocks next to an AI eye icon"},
    "Forma d’onda audio del testo con punteggio di naturalezza 92":
        {"en": "Audio waveform of the text with a 92 naturalness score"},
    "Anteprima del file llms.txt generato automaticamente":
        {"en": "Preview of the automatically generated llms.txt file"},
}
CHROME.update(CHROME_TOOLS_IMG_ALT)

# Area clienti (cab.remarka.biz) + sezione Gratis/Monitor del Lab
# (docs/piano-promo-cabinet-lab.md). Solo 'en': le pagine RU sono scritte a
# mano (translate_pages.py ru è vietato — piano-strumenti-lab.md).
CHROME_AREA_CLIENTI = {
    # Pagina /area-clienti/
    'Area clienti': {'en': 'Client area'},
    'Il progetto, nero su bianco': {'en': 'The project, in black and white'},
    'Ogni progetto Remarka include l’accesso all’area clienti: la fase del lavoro visibile ogni giorno, approvazioni e file in un unico posto — in italiano, inglese o russo.':
        {'en': 'Every Remarka project includes access to the client area: the current stage visible every day, approvals and files in one place — in Italian, English or Russian.'},
    'Accedi all’area clienti': {'en': 'Log in to the client area'},
    'Non siete ancora clienti? Parliamone': {'en': 'Not a client yet? Let’s talk'},
    'fasi del progetto, visibili in ogni momento — dal brief al lancio':
        {'en': 'project stages, visible at any moment — from brief to launch'},
    'Tre passaggi, zero password': {'en': 'Three steps, zero passwords'},
    'Passo 1': {'en': 'Step 1'},
    'Passo 2': {'en': 'Step 2'},
    'Passo 3': {'en': 'Step 3'},
    'Entrate senza password': {'en': 'Log in without a password'},
    'Inserite la vostra e-mail: vi mandiamo un link di accesso monouso, valido 15 minuti. Niente password da ricordare, niente password da rubare.':
        {'en': 'Enter your e-mail: we send you a single-use login link, valid for 15 minutes. No passwords to remember, no passwords to steal.'},
    'Vedete a che punto siamo': {'en': 'See where we are'},
    'Il progetto avanza su 8 fasi, dal brief al lancio: quella corrente è sempre evidenziata. Non serve chiedere «a che punto siamo?» — si vede.':
        {'en': 'The project moves through 8 stages, from brief to launch: the current one is always highlighted. No need to ask “where are we?” — you can see it.'},
    'Approvate e scaricate': {'en': 'Approve and download'},
    'Bozze e testi si approvano con un click, con data e nome; file e fatture restano archiviati. Ogni domanda ha un filo tracciato, non una e-mail persa.':
        {'en': 'Drafts and copy are approved in one click, with date and name; files and invoices stay on record. Every question has a tracked thread, not a lost e-mail.'},
    'Cosa trovate dentro': {'en': 'What you find inside'},
    'Tutto il progetto, in un posto solo': {'en': 'The whole project, in one place'},
    'Fasi del progetto': {'en': 'Project stages'},
    'Dal brief al lancio, 8 fasi con la corrente evidenziata: l’avanzamento si vede a colpo d’occhio, ogni giorno.':
        {'en': 'From brief to launch, 8 stages with the current one highlighted: progress is visible at a glance, every day.'},
    'Approvazioni con storico': {'en': 'Approvals with history'},
    'Bozze e testi da approvare o rimandare con un commento. Ogni decisione resta agli atti: chi, cosa, quando.':
        {'en': 'Drafts and copy to approve, or send back with a comment. Every decision stays on record: who, what, when.'},
    'File in un unico posto': {'en': 'Files in one place'},
    'I materiali del progetto — bozze, consegne, documenti — sempre scaricabili. E potete caricare i vostri: loghi, testi, foto.':
        {'en': 'Project materials — drafts, deliverables, documents — always available to download. And you can upload yours: logos, copy, photos.'},
    'Fatture e stato dei pagamenti': {'en': 'Invoices and payment status'},
    'Numero, data, importo e stato di ogni fattura, con il PDF scaricabile. Niente da chiedere, niente da cercare.':
        {'en': 'Number, date, amount and status of every invoice, with the PDF ready to download. Nothing to ask for, nothing to dig up.'},
    'Richieste tracciate': {'en': 'Tracked requests'},
    'Ogni domanda apre un filo con storico e risposta: niente e-mail perse tra le caselle di tre persone.':
        {'en': 'Every question opens a thread with its history and answer: no e-mails lost across three inboxes.'},
    'Tre lingue': {'en': 'Three languages'},
    'Interfaccia e notifiche in italiano, inglese o russo: ognuno del vostro team la usa nella propria lingua.':
        {'en': 'Interface and notifications in Italian, English or Russian: everyone on your team uses it in their own language.'},
    'Perché l’abbiamo costruita': {'en': 'Why we built it'},
    'Costruita da noi, come i siti che vendiamo': {'en': 'Built by us, like the websites we sell'},
    'Sviluppiamo web app per i clienti — e l’area clienti è la nostra: stessa piattaforma, stessi standard, stesso design. Nessun gestionale di terzi: i dati restano su server nell’Unione Europea e ne raccogliamo solo il minimo necessario per lavorare insieme.':
        {'en': 'We build web apps for clients — and the client area is ours: same platform, same standards, same design. No third-party tools: data stays on servers in the European Union, and we only collect the minimum needed to work together.'},
    'Sicurezza e privacy': {'en': 'Security and privacy'},
    'Accesso senza password: link monouso via e-mail, valido 15 minuti':
        {'en': 'Passwordless access: a single-use link by e-mail, valid for 15 minutes'},
    'Sessioni revocabili e registro degli accessi': {'en': 'Revocable sessions and an access log'},
    'Dati su server nell’Unione Europea (Germania), GDPR by design':
        {'en': 'Data on servers in the European Union (Germany), GDPR by design'},
    'Solo i dati necessari: e-mail, nome, lingua — nient’altro':
        {'en': 'Only the data we need: e-mail, name, language — nothing else'},
    'Quanto costa l’area clienti?': {'en': 'How much does the client area cost?'},
    'Niente: è inclusa in ogni progetto Remarka, dal sito vetrina all’e-commerce.':
        {'en': 'Nothing: it’s included in every Remarka project, from a brochure site to an e-commerce store.'},
    'Serve installare qualcosa?': {'en': 'Do I need to install anything?'},
    'No. Funziona dal browser, anche dal telefono. Entrate con la vostra e-mail: niente password, niente app da installare.':
        {'en': 'No. It works in the browser, on your phone too. You log in with your e-mail: no passwords, no apps to install.'},
    'In che lingua è l’interfaccia?': {'en': 'What language is the interface in?'},
    'Italiano, inglese o russo: la scegliete voi, e ogni membro del vostro team può usarne una diversa.':
        {'en': 'Italian, English or Russian: you choose, and each member of your team can use a different one.'},
    'Chi vede i vostri dati?': {'en': 'Who sees your data?'},
    'Solo voi e noi. Ogni cliente vede esclusivamente i propri progetti; i dati stanno su server nell’Unione Europea e non li cediamo a terzi.':
        {'en': 'Only you and us. Each client sees exclusively their own projects; data lives on servers in the European Union and we never pass it to third parties.'},

    # Riga area clienti nelle pagine servizio / riga prezzi / chi-siamo
    'Ogni progetto include l’area clienti: fasi, approvazioni e file in un unico posto →':
        {'en': 'Every project includes the client area: stages, approvals and files in one place →'},
    'Area clienti: fasi, approvazioni, fatture': {'en': 'Client area: stages, approvals, invoices'},
    'Costruiamo anche i nostri strumenti: Remarka Lab, con 12 check gratuiti e il monitoraggio continuo dei siti che seguiamo, e l’area clienti dove ogni progetto è visibile fase per fase. La stessa tecnologia che vendiamo, usata ogni giorno da noi.':
        {'en': 'We also build our own tools: Remarka Lab, with 12 free checks and continuous monitoring of the websites we look after, and the client area where every project is visible stage by stage. The same technology we sell, used by us every day.'},
    'Gli strumenti gratuiti del Lab →': {'en': 'The Lab’s free tools →'},
    'Com’è fatta l’area clienti →': {'en': 'Inside the client area →'},

    # Indice strumenti: brand Lab + sezione Gratis/Monitor (#monitor)
    'Remarka Lab · Strumenti gratuiti': {'en': 'Remarka Lab · Free tools'},
    # Tre livelli (aggiornato 20.07 — lab aperto: vetrina /showcase + free self-serve)
    'Gratis · senza registrazione': {'en': 'Free · no sign-up'},
    'Strumenti una tantum': {'en': 'One-off checks'},
    '12 check gratuiti: velocità, SEO, accessibilità, GDPR, AI, E-E-A-T, CO₂, ROI':
        {'en': '12 free checks: speed, SEO, accessibility, GDPR, AI, E-E-A-T, CO₂, ROI'},
    'Risultato in circa un minuto, senza registrazione': {'en': 'Result in about a minute, no sign-up'},
    'Ogni strumento indica cosa correggere': {'en': 'Every tool shows what to fix'},
    'Gratis · con accesso': {'en': 'Free · with an account'},
    'Remarka Lab · Monitor': {'en': 'Remarka Lab · Monitor'},
    'Un sito sotto controllo, gratis': {'en': 'One site under watch, for free'},
    'Accesso con link via e-mail, senza password': {'en': 'Sign in with an email link, no password'},
    'Punteggio di salute, errori e problemi, andamento nel tempo':
        {'en': 'Health score, errors and issues, trend over time'},
    'Provate Remarka Lab, gratis →': {'en': 'Try Remarka Lab, free →'},
    'Pro · con l’assistenza': {'en': 'Pro · with a maintenance plan'},
    'Con noi accanto': {'en': 'With us alongside'},
    'Il sito osservato in continuo dopo il lancio':
        {'en': 'Your site watched continuously after launch'},
    'Se un valore peggiora, lo vediamo noi e interveniamo':
        {'en': 'If a metric slips, we see it and step in'},
    'Incluso nei progetti con assistenza attiva':
        {'en': 'Included in projects with an active maintenance plan'},
    'Cosa misurare ogni mese: la guida →': {'en': 'What to measure each month: the guide →'},
    'Parliamone →': {'en': 'Let’s talk →'},
    'Gratis oggi. Sotto controllo domani': {'en': 'Free today. Under watch tomorrow'},
    'Un punteggio si misura gratis una volta. Tenerlo alto nel tempo è un lavoro. Con Remarka Lab tenete un sito sotto controllo gratis — e per i clienti con assistenza attiva ce ne occupiamo noi.':
        {'en': 'A score is measured for free once. Keeping it high over time is work. With Remarka Lab you keep one site under watch for free — and for clients with an active maintenance plan we take care of it.'},
    'Volete vederlo dal vivo? Lo stato del nostro sito, in diretta →':
        {'en': 'Want to see it live? Our site’s status, in real time →'},
}
CHROME.update(CHROME_AREA_CLIENTI)

# CHROME_BLOG_CABLAB — sputnik area clienti + monitoraggio (2 articoli IT → EN,
# piano-promo-cabinet-lab.md §3.9). Solo 'en': il blog RU è un batch a sé.
CHROME_BLOG_CABLAB = {
    '19 LUG 2026': {'en': '19 JUL 2026'},

    # ---- Articolo 1: area clienti di un'agenzia web ----
    'Area clienti di un’agenzia web: cosa dovete pretendere':
        {'en': 'A web agency’s client portal: what you should demand'},
    '«A che punto siamo con il sito?» non dovrebbe essere una domanda: dovrebbe essere una schermata. I sei segni di un fornitore trasparente, le tre domande di sicurezza e perché non deve costarvi un euro in più.':
        {'en': '“Where are we with the website?” shouldn’t be a question: it should be a screen. The six signs of a transparent vendor, the three security questions, and why it shouldn’t cost you an extra euro.'},
    '«A che punto siamo con il sito?» Se per rispondere dovete scavare tra tre catene di e-mail, uno screenshot su WhatsApp e un PDF chiamato definitivo-v3-BIS, il problema non siete voi: è il fornitore che vi ha lasciato senza strumenti. Nel 2026 un’area clienti — un posto dove il progetto si vede: la fase in corso, chi deve approvare cosa, i file, le fatture — non è un lusso da grande agenzia web, è il minimo sindacale della trasparenza. In questo articolo: i sei segni che distinguono un’area clienti vera da una vetrina, le tre domande di sicurezza da fare prima di firmare, e perché tutto questo non dovrebbe costarvi un euro in più.':
        {'en': '“Where are we with the website?” If answering that means digging through three e-mail threads, a WhatsApp screenshot and a PDF called final-v3-REV, the problem isn’t you: it’s the vendor who left you without tools. In 2026 a client portal — one place where the project is visible: the current stage, who needs to approve what, the files, the invoices — isn’t a big-agency luxury; it’s the bare minimum of transparency a web agency owes you. In this article: the six signs that tell a real client portal from a shop window, the three security questions to ask before signing, and why none of this should cost you an extra euro.'},
    'Area clienti di un’agenzia web: le fasi del progetto, le approvazioni con storico e i sei segni di un fornitore trasparente':
        {'en': 'A web agency client portal: project stages, approvals with history and the six signs of a transparent vendor'},
    'Il progetto invisibile (e i litigi che produce)':
        {'en': 'The invisible project (and the disputes it breeds)'},
    'La maggior parte dei conflitti tra cliente e agenzia non nasce dalla qualità del lavoro: nasce dalla memoria. «Il logo grande l’avevate approvato voi» — «no, avevamo chiesto di ridurlo». Senza un registro, ogni decisione vive nella testa di qualcuno, e la versione più sicura di sé vince sulla versione vera. Non è un difetto di carattere, è un difetto di struttura: e-mail e chat sono canali di conversazione, non archivi di decisioni. Il Project Management Institute lo ripete da anni nei suoi rapporti: la comunicazione inefficace è tra le prime cause di fallimento dei progetti — e un progetto web da tre settimane non fa eccezione.':
        {'en': 'Most conflicts between client and agency aren’t born from the quality of the work: they’re born from memory. “You approved the big logo” — “no, we asked to make it smaller”. Without a record, every decision lives in someone’s head, and the most confident version wins over the true one. It’s not a character flaw, it’s a structural one: e-mail and chat are conversation channels, not archives of decisions. The Project Management Institute has been repeating it for years in its reports: ineffective communication is among the top causes of project failure — and a three-week web project is no exception.'},
    'C’è anche un costo più silenzioso: l’attesa. Ogni «a che punto siamo?» è un’interruzione per chi lavora e un’incertezza per chi aspetta; su un progetto di un mese sono decine di messaggi che non producono nulla. La trasparenza non è cortesia — è infrastruttura: se lo stato del progetto è visibile, la domanda scompare da sola.':
        {'en': 'There’s a quieter cost too: waiting. Every “where are we?” is an interruption for the people working and uncertainty for the people waiting; over a one-month project that’s dozens of messages that produce nothing. Transparency isn’t courtesy — it’s infrastructure: when the project’s status is visible, the question disappears on its own.'},
    'I sei segni di un’area clienti di agenzia web fatta sul serio':
        {'en': 'The six signs of a web agency client portal built for real'},
    'Fasi visibili: il progetto ha stadi espliciti — brief, design, sviluppo, contenuti, revisione, lancio — e vedete in quale si trova oggi, non nell’ultima telefonata.':
        {'en': 'Visible stages: the project has explicit stages — brief, design, development, content, review, launch — and you can see which one it’s in today, not as of the last phone call.'},
    'Approvazioni con storico: bozze e testi si approvano o si rimandano con un commento, e resta scritto chi, cosa e quando.':
        {'en': 'Approvals with history: drafts and copy get approved or sent back with a comment, and it stays on record — who, what, when.'},
    'File in un posto solo: bozze, consegne e materiali non viaggiano in allegati da 20 MB, ma stanno dove li ritroverete tra un anno.':
        {'en': 'Files in one place: drafts, deliverables and materials don’t travel as 20 MB attachments — they live where you’ll find them a year from now.'},
    'Fatture con stato: numero, importo, scadenza e stato di pagamento — senza dover chiedere «me la rimanda?».':
        {'en': 'Invoices with status: number, amount, due date and payment status — without having to ask “could you resend it?”.'},
    'Richieste tracciate: ogni domanda apre un filo con la sua risposta, non un thread che muore nella casella di un collega in ferie.':
        {'en': 'Tracked requests: every question opens a thread with its answer, not a chain that dies in the inbox of a colleague on holiday.'},
    'La vostra lingua: se il team lavora tra più paesi, l’interfaccia deve seguirvi — non costringervi all’italiano tecnico.':
        {'en': 'Your language: if your team works across countries, the interface should follow you — not force everyone into technical Italian.'},
    'I sei segni di un’area clienti seria: fasi visibili, approvazioni con storico, file, fatture, richieste tracciate e interfaccia multilingue':
        {'en': 'The six signs of a serious client portal: visible stages, approvals with history, files, invoices, tracked requests and a multilingual interface'},
    'I sei segni, in ordine di importanza: fasi visibili, approvazioni con storico, file in un posto solo, fatture con stato, richieste tracciate, interfaccia nella vostra lingua. Nessuno dei sei è tecnologia esotica: è disciplina resa visibile.':
        {'en': 'The six signs, in order of importance: visible stages, approvals with history, files in one place, invoices with status, tracked requests, an interface in your language. None of the six is exotic technology: it’s discipline made visible.'},
    'Eccoli, in ordine di importanza. Nessuno dei sei è tecnologia esotica: sono pratiche note da vent’anni a chiunque gestisca progetti. La differenza sta in chi porta l’onere: un fornitore serio ve le mette a disposizione di serie, non ve le vende a parte come «modulo premium». E se al primo appuntamento vi mostrano l’area clienti prima ancora che glielo chiediate, è un buon segno: non hanno niente da nascondere sul modo in cui lavorano.':
        {'en': 'Here they are, in order of importance. None of the six is exotic technology: they’ve been standard practice for anyone running projects for twenty years. The difference is who carries the burden: a serious vendor gives them to you as standard, not as a paid “premium module”. And if they show you the client portal at the first meeting, before you even ask, that’s a good sign: they have nothing to hide about how they work.'},
    'Le tre domande di sicurezza, prima di firmare':
        {'en': 'The three security questions, before you sign'},
    'Prima domanda: come si entra? La risposta migliore è «senza password»: un link monouso via e-mail, che scade in pochi minuti. Le linee guida NIST sull’identità digitale dicono da anni quello che l’esperienza di tutti conferma — le password si dimenticano, si riusano e si rubano. Un accesso monouso elimina il problema alla radice, invece di scaricarlo su di voi.':
        {'en': 'First question: how do you get in? The best answer is “without a password”: a single-use link by e-mail that expires in minutes. NIST’s digital identity guidelines have been saying for years what everyone’s experience confirms — passwords get forgotten, reused and stolen. A single-use login removes the problem at the root instead of offloading it onto you.'},
    'Seconda: dove vivono i dati? Nomi, e-mail, fatture e bozze del vostro sito sono dati aziendali. Il GDPR chiede minimizzazione — si raccoglie solo il necessario — e voi avete tutto l’interesse che restino su server nell’Unione Europea, dove il regolamento si applica senza acrobazie contrattuali.':
        {'en': 'Second: where does the data live? Names, e-mails, invoices and drafts of your website are business data. The GDPR requires minimisation — collecting only what’s necessary — and it’s squarely in your interest that it stays on servers in the European Union, where the regulation applies without contractual acrobatics.'},
    'Terza: chi vede cosa? In un portale con più clienti, la separazione dei dati non è un dettaglio: chiedete esplicitamente se ogni cliente vede solo i propri progetti e se gli accessi vengono registrati. Un fornitore serio risponde in trenta secondi; uno improvvisato cambia discorso.':
        {'en': 'Third: who sees what? In a portal serving several clients, data separation isn’t a detail: ask explicitly whether each client sees only their own projects and whether logins are recorded. A serious vendor answers in thirty seconds; an improvised one changes the subject.'},
    'Bonus, prima ancora di parlare con l’agenzia: guardate il suo sito con lo stesso metro che userebbe Google. I segnali di fiducia — chi c’è dietro, contatti veri, politiche pubblicate — si misurano in un minuto.':
        {'en': 'Bonus, before you even talk to the agency: look at their own website with the same yardstick Google would use. Trust signals — who’s behind it, real contact details, published policies — take one minute to measure.'},
    'Misura i segnali di fiducia di un sito: lo strumento E-E-A-T gratuito →':
        {'en': 'Measure a website’s trust signals: the free E-E-A-T tool →'},
    'Un’area clienti non sostituisce il contratto (lo completa)':
        {'en': 'A client portal doesn’t replace the contract (it completes it)'},
    'Attenzione all’equivoco opposto: un portale elegante non è una garanzia. La data di consegna sta nel contratto, non nell’interfaccia; il prezzo chiuso pure. L’area clienti è il posto dove vedete che il contratto viene rispettato — fase dopo fase, approvazione dopo approvazione. Le due cose lavorano insieme: nero su bianco negli accordi, tutto alla luce nell’esecuzione. Diffidate di chi vi offre solo una delle due.':
        {'en': 'Beware of the opposite misunderstanding: an elegant portal is not a guarantee. The delivery date lives in the contract, not in the interface; so does the fixed price. The client portal is where you see the contract being honoured — stage after stage, approval after approval. The two work together: everything in writing in the agreement, everything in the open in the execution. Be wary of anyone offering only one of the two.'},
    'Se in questi giorni state confrontando preventivi, abbiamo scritto una guida su come leggerli senza sorprese: le voci che devono esserci, quelle che mancano sempre e le domande da fare prima di firmare.':
        {'en': 'If you’re comparing quotes these days, we’ve written a guide on how to read them without surprises: the line items that must be there, the ones that are always missing, and the questions to ask before signing.'},
    'Preventivo sito web: come leggerlo senza sorprese →':
        {'en': 'Website quotes: how to read one without surprises →'},
    'Come lo facciamo noi (e perché non costa un euro in più)':
        {'en': 'How we do it (and why it doesn’t cost an extra euro)'},
    'Dichiarazione di interesse: questa guida non è neutrale, perché un’area clienti l’abbiamo costruita — per noi. Sviluppiamo web app per i clienti e il nostro portale gira sulla stessa piattaforma: 8 fasi del progetto sempre visibili, approvazioni con storico, file, fatture e richieste, interfaccia in italiano, inglese o russo, accesso senza password, dati su server in Germania. È inclusa in ogni progetto, dal sito vetrina all’e-commerce, perché per noi la trasparenza non è un optional a listino: è il modo più economico di lavorare bene.':
        {'en': 'Declaration of interest: this guide isn’t neutral, because we’ve built a client portal — for ourselves. We build web apps for clients and our portal runs on the same platform: 8 project stages always visible, approvals with history, files, invoices and requests, interface in Italian, English or Russian, passwordless access, data on servers in Germany. It’s included in every project, from a brochure site to an e-commerce store, because for us transparency isn’t a paid extra on a price list: it’s the cheapest way to work well.'},
    'Il criterio resta valido anche se sceglierete un’altra agenzia: pretendete di vedere il vostro progetto. Se la risposta è «vi teniamo aggiornati via e-mail», sapete già come andrà a finire.':
        {'en': 'The criterion holds even if you choose another agency: demand to see your project. If the answer is “we’ll keep you posted by e-mail”, you already know how it ends.'},
    'Com’è fatta la nostra area clienti, schermata per schermata →':
        {'en': 'Inside our client area, screen by screen →'},
    'Siti aziendali: cosa include un progetto →':
        {'en': 'Business websites: what a project includes →'},
    'Com’è fatta la nostra area clienti →': {'en': 'Inside our client area →'},
    'NIST SP 800-63B — Digital Identity Guidelines':
        {'en': 'NIST SP 800-63B — Digital Identity Guidelines'},
    'Le linee guida del National Institute of Standards and Technology su autenticazione e credenziali: la base tecnica dell’accesso senza password.':
        {'en': 'The National Institute of Standards and Technology guidelines on authentication and credentials: the technical basis of passwordless access.'},
    'Regolamento (UE) 2016/679 — GDPR, testo ufficiale':
        {'en': 'Regulation (EU) 2016/679 — GDPR, official text'},
    'L’articolo 5 fissa i princìpi di minimizzazione dei dati e di limitazione della conservazione citati nell’articolo.':
        {'en': 'Article 5 sets out the data-minimisation and storage-limitation principles cited in this article.'},
    'PMI — Pulse of the Profession': {'en': 'PMI — Pulse of the Profession'},
    'La serie di rapporti del Project Management Institute che indica da anni la comunicazione inefficace tra le prime cause di fallimento dei progetti.':
        {'en': 'The Project Management Institute’s report series, which for years has ranked ineffective communication among the top causes of project failure.'},

    # ---- Articolo 2: monitoraggio dopo il lancio ----
    'Monitoraggio del sito dopo il lancio: cosa misurare ogni mese':
        {'en': 'Website monitoring after launch: what to measure every month'},
    'Il giorno della consegna il punteggio era 94. Un anno dopo il sito carica in cinque secondi e nessuno se n’è accorto. Le quattro misure che contano, il rituale mensile in venti minuti e quando delegare.':
        {'en': 'On delivery day the score was 94. A year later the site takes five seconds to load and nobody noticed. The four measures that matter, the twenty-minute monthly ritual, and when to delegate.'},
    'Il giorno della consegna il vostro sito era una scheda perfetta: PageSpeed 94, tutto verde, strette di mano. Dodici mesi dopo carica in cinque secondi, un modulo non invia più nulla e nessuno se n’è accorto — perché nessuno stava guardando. I siti non si rompono con un boato: si logorano in silenzio, un plugin aggiornato alla volta, una foto da 8 MB alla volta. Il monitoraggio del sito web è il mestiere di accorgersene prima dei vostri clienti. Ecco cosa misurare ogni mese, con quali strumenti, e quando ha senso delegare.':
        {'en': 'On delivery day your website was a perfect scorecard: PageSpeed 94, all green, handshakes. Twelve months later it takes five seconds to load, one form no longer sends anything, and nobody noticed — because nobody was watching. Websites don’t break with a bang: they wear out in silence, one plugin update at a time, one 8 MB photo at a time. Website monitoring is the craft of noticing before your customers do. Here’s what to measure every month, with which tools, and when it makes sense to delegate.'},
    'Monitoraggio del sito web dopo il lancio: il punteggio che si logora in dodici mesi senza controlli e le soglie dei Core Web Vitals':
        {'en': 'Website monitoring after launch: a score wearing down over twelve unwatched months, and the Core Web Vitals thresholds'},
    'Perché un sito veloce smette di esserlo':
        {'en': 'Why a fast website stops being fast'},
    'Un sito è un sistema vivo: il CMS e i plugin si aggiornano, il team carica le immagini come escono dal telefono, il marketing aggiunge uno script di tracciamento «solo per una campagna» che resta lì per sempre, l’hosting condiviso si affolla di vicini. Ogni cambiamento è piccolo; la somma no. È lo stesso motivo per cui l’auto fa il tagliando: non perché si sia rotta, ma perché è stata usata.':
        {'en': 'A website is a living system: the CMS and plugins update themselves, the team uploads photos straight off the phone, marketing adds a tracking script “just for one campaign” that stays forever, the shared hosting fills up with neighbours. Each change is small; the sum is not. It’s the same reason a car gets serviced: not because it broke, but because it’s been used.'},
    'C’è poi un secondo orologio che gira: quello di Google. Le metriche cambiano — nel 2024 INP ha sostituito FID tra i Core Web Vitals — e un sito fermo agli standard di due anni fa scivola indietro anche senza che nessuno tocchi nulla. Il punteggio del giorno della consegna non è un attestato appeso al muro: è una fotografia, e le fotografie invecchiano.':
        {'en': 'And a second clock is ticking: Google’s. The metrics change — in 2024 INP replaced FID among the Core Web Vitals — and a site frozen at two-year-old standards slides backwards even if nobody touches a thing. The delivery-day score isn’t a diploma on the wall: it’s a photograph, and photographs age.'},
    'Le quattro misure di un monitoraggio del sito web serio':
        {'en': 'The four measures of serious website monitoring'},
    'Uptime: il sito risponde? Sembra banale, finché non scoprite che era giù proprio la notte della campagna. Serve un controllo automatico ogni pochi minuti, con un avviso immediato.':
        {'en': 'Uptime: does the site respond? Sounds trivial, until you find out it was down on the very night of your campaign. You need an automatic check every few minutes, with an immediate alert.'},
    'Core Web Vitals sul campo: LCP sotto 2,5 secondi, INP sotto 200 millisecondi, CLS sotto 0,1 — misurati sugli utenti reali (dati CrUX aggregati su 28 giorni), non solo in laboratorio.':
        {'en': 'Core Web Vitals in the field: LCP under 2.5 seconds, INP under 200 milliseconds, CLS under 0.1 — measured on real users (CrUX data aggregated over 28 days), not just in the lab.'},
    'Funzioni critiche: moduli, carrello, prenotazioni. Il danno vero non è «il sito è lento», è «il modulo non invia da tre settimane».':
        {'en': 'Critical functions: forms, cart, bookings. The real damage isn’t “the site is slow” — it’s “the form hasn’t been sending for three weeks”.'},
    'Visibilità: le pagine indicizzate, gli errori segnalati da Search Console, le posizioni sulle ricerche che vi portano clienti.':
        {'en': 'Visibility: the pages in the index, the errors flagged by Search Console, your positions on the searches that bring you customers.'},
    'Le quattro misure del monitoraggio di un sito web: uptime, Core Web Vitals reali, funzioni critiche e visibilità su Google':
        {'en': 'The four measures of website monitoring: uptime, real-user Core Web Vitals, critical functions and visibility on Google'},
    'Le quattro misure, in ordine: prima «esiste?» (uptime), poi «funziona per gli utenti veri?» (Core Web Vitals sul campo, CrUX su 28 giorni), poi «vende?» (moduli e carrello), infine «si trova?» (indice e posizioni). Fonti: web.dev e documentazione CrUX (Google).':
        {'en': 'The four measures, in order: first “does it exist?” (uptime), then “does it work for real users?” (field Core Web Vitals, CrUX over 28 days), then “does it sell?” (forms and cart), finally “can it be found?” (index and rankings). Sources: web.dev and the CrUX documentation (Google).'},
    'Quattro misure, in quest’ordine: prima «esiste?», poi «funziona per le persone vere?», poi «vende?», infine «si trova?». Un monitoraggio che guarda solo il punteggio di velocità è un cruscotto con la sola spia della benzina: utile, ma non vi dice che si è staccata una ruota.':
        {'en': 'Four measures, in this order: first “does it exist?”, then “does it work for real people?”, then “does it sell?”, finally “can it be found?”. Monitoring that watches only the speed score is a dashboard with just the fuel light: useful, but it won’t tell you a wheel has come off.'},
    'Laboratorio e mondo reale: perché i due numeri non coincidono':
        {'en': 'Lab and real world: why the two numbers don’t match'},
    'Lighthouse — il motore dietro PageSpeed Insights — misura il sito in condizioni controllate: stessa rete simulata, stesso dispositivo. È prezioso per diagnosticare, ma resta un laboratorio. I Core Web Vitals «sul campo» arrivano invece dal Chrome UX Report: utenti veri, reti vere, telefoni veri, aggregati su 28 giorni. I due numeri possono divergere — il laboratorio promosso e il campo bocciato, o viceversa — e quando divergono, ha ragione il campo: è lì che stanno i vostri clienti.':
        {'en': 'Lighthouse — the engine behind PageSpeed Insights — measures the site under controlled conditions: same simulated network, same device. It’s invaluable for diagnosing, but it’s still a lab. Field Core Web Vitals come instead from the Chrome UX Report: real users, real networks, real phones, aggregated over 28 days. The two numbers can diverge — the lab passing and the field failing, or the other way round — and when they diverge, the field is right: that’s where your customers are.'},
    'La conseguenza pratica: un check una tantum vi dice come sta il sito oggi, in laboratorio. Solo una serie mensile vi dice se sta migliorando o peggiorando per le persone che lo usano davvero. È la differenza tra una foto e un elettrocardiogramma.':
        {'en': 'The practical consequence: a one-off check tells you how the site is doing today, in the lab. Only a monthly series tells you whether it’s getting better or worse for the people who actually use it. It’s the difference between a photo and an electrocardiogram.'},
    'Il rituale mensile, in venti minuti':
        {'en': 'The monthly ritual, in twenty minutes'},
    'Lanciate un check-up completo e salvate il punteggio accanto a quello del mese scorso: conta la direzione, non il numero del giorno.':
        {'en': 'Run a full check-up and save the score next to last month’s: what counts is the direction, not the number of the day.'},
    'Aprite Search Console: copertura dell’indice, errori nuovi, ricerche che portano clic.':
        {'en': 'Open Search Console: index coverage, new errors, the searches that bring clicks.'},
    'Guardate il report di uptime del mese: quanti minuti di assenza, e in quali orari.':
        {'en': 'Look at the month’s uptime report: how many minutes of downtime, and at what hours.'},
    'Percorrete a mano la strada che vi porta soldi — modulo, richiesta di preventivo, carrello — dal telefono, non dalla scrivania.':
        {'en': 'Walk the path that brings you money by hand — form, quote request, cart — from a phone, not from your desk.'},
    'Verificate che l’ultimo backup esista e si apra: un backup mai testato è una speranza, non un backup.':
        {'en': 'Check that the latest backup exists and opens: a backup never tested is a hope, not a backup.'},
    'Check-up completo del sito: 7 misure in un minuto, gratis →':
        {'en': 'Full site check-up: 7 measures in one minute, free →'},
    'Quando delegare (e cosa pretendere da chi lo fa per voi)':
        {'en': 'When to delegate (and what to demand from whoever does it for you)'},
    'Il rituale dei venti minuti funziona — finché qualcuno lo fa davvero. L’esperienza dice che dopo il terzo mese l’appuntamento scivola, e il sito torna a logorarsi non visto. L’ingegneria dell’affidabilità di Google ha formalizzato un principio che vale anche in piccolo: i sistemi si presidiano con controlli automatici e allarmi, non con la buona volontà.':
        {'en': 'The twenty-minute ritual works — as long as someone actually does it. Experience says that after the third month the appointment slips, and the site goes back to wearing out unseen. Google’s reliability engineering formalised a principle that holds at small scale too: systems are kept safe by automatic checks and alerts, not by good intentions.'},
    'È il motivo per cui nei nostri progetti con assistenza il monitoraggio è incluso: la nostra piattaforma tiene d’occhio uptime, controlli periodici e Core Web Vitals reali dei siti che seguiamo, e quando un valore scivola lo vediamo noi — prima che ve ne accorgiate dai clienti. Il report arriva ogni mese, in linguaggio umano. Se invece preferite il fai-da-te, il rituale qui sopra è vostro: l’importante è che qualcuno guardi.':
        {'en': 'That’s why monitoring is included in our projects with a maintenance plan: our platform keeps an eye on uptime, periodic checks and the real-user Core Web Vitals of the sites we look after, and when a value slips we see it — before you hear about it from customers. The report arrives every month, in human language. If you prefer DIY, the ritual above is yours: what matters is that someone is watching.'},
    'Il nostro Monitor in diretta — e provatelo su un vostro sito, gratis →':
        {'en': 'Our Monitor live — and try it on a site of yours, free →'},
    'Gratis oggi, sotto controllo domani: il monitoraggio per i clienti →':
        {'en': 'Free today, under watch tomorrow: monitoring for clients →'},
    'Restyling tecnico: quando i numeri dicono che serve →':
        {'en': 'Technical redesign: when the numbers say it’s time →'},
    'Cosa misurare ogni mese: la guida al monitoraggio →':
        {'en': 'What to measure every month: the monitoring guide →'},
    'Core Web Vitals nel 2026: cosa misura davvero Google →':
        {'en': 'Core Web Vitals in 2026: what Google actually measures →'},
    'Cosa pretendere dall’area clienti di qualunque agenzia: la guida →':
        {'en': 'What to demand from any agency’s client portal: the guide →'},
    'Fate il check-up completo del vostro sito — gratis →':
        {'en': 'Run the full check-up of your website — free →'},
    'web.dev — Core Web Vitals (Google)': {'en': 'web.dev — Core Web Vitals (Google)'},
    'Definizioni e soglie ufficiali di LCP, INP e CLS citate nell’articolo, incluso il passaggio da FID a INP nel 2024.':
        {'en': 'The official definitions and thresholds of LCP, INP and CLS cited in this article, including the switch from FID to INP in 2024.'},
    'Chrome UX Report (CrUX) — documentazione': {'en': 'Chrome UX Report (CrUX) — documentation'},
    'La fonte dei dati «sul campo»: utenti reali di Chrome, aggregati su una finestra mobile di 28 giorni.':
        {'en': 'The source of field data: real Chrome users, aggregated over a rolling 28-day window.'},
    'Google SRE — Monitoring Distributed Systems': {'en': 'Google SRE — Monitoring Distributed Systems'},
    'Il capitolo del libro Site Reliability Engineering sul presidiare i sistemi: controlli automatici e allarmi, non buona volontà.':
        {'en': 'The Site Reliability Engineering book’s chapter on keeping systems safe: automatic checks and alerts, not good intentions.'},
}
CHROME.update(CHROME_BLOG_CABLAB)

# CHROME_SERVIZI_VISUALS — polosa dei progetti reali + visual di direzione su
# /servizi/ e schema editoriale su Export Ready (manifest images/chatgpt).
CHROME_SERVIZI_VISUALS = {
    'Dai progetti del gruppo': {'en': 'From the group’s projects'},
    'Interfacce vere, in produzione': {'en': 'Real interfaces, in production'},
    'Tre schermate dai progetti che il gruppo Remarka usa e mantiene ogni giorno — non mockup. I casi completi, con i link ai siti vivi, sono nel catalogo.':
        {'en': 'Three screens from projects the Remarka group uses and maintains every day — not mockups. The full write-ups, with links to the live sites, are in the catalog.'},
    'Tutti i progetti, con i link vivi →': {'en': 'All the projects, with live links →'},
    'Schermata reale del sito techperevod.com': {'en': 'Actual screenshot of the techperevod.com website'},
    'Schermata reale del catalogo perevod4.ru': {'en': 'Actual screenshot of the perevod4.ru catalog'},
    'Schermata reale del TMS interno del gruppo': {'en': 'Actual screenshot of the group’s internal TMS'},
    'TMS · interno': {'en': 'TMS · internal'},
    'Schema del percorso editoriale: sorgente, revisione, versioni locali':
        {'en': 'Editorial workflow diagram: source, review, local versions'},
}
CHROME.update(CHROME_SERVIZI_VISUALS)

# CHROME_RECENSIONI — sezione recensioni Product Hunt + priorità del check-up
# (le citazioni restano in originale inglese: nessuna coppia per i testi).
CHROME_RECENSIONI = {
    'Dalla community': {'en': 'From the community'},
    'Cosa dice chi li ha provati': {'en': 'What people who tried them say'},
    'Le prime recensioni dal lancio su Product Hunt — citate in originale, con il permesso degli autori.':
        {'en': 'The first reviews from our Product Hunt launch — quoted verbatim, with the authors’ permission.'},
    'Da dove partire': {'en': 'Where to start'},
    # Download diretto del PDF (senza e-mail) — bottone nel form report.
    'oppure': {'en': 'or'},
    'Scaricate il PDF adesso — senza e-mail': {'en': 'Download the PDF now — no e-mail needed'},
    'Prepariamo il PDF…': {'en': 'Preparing your PDF…'},
}
CHROME.update(CHROME_RECENSIONI)
