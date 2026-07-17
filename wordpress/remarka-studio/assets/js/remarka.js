/**
 * Remarka Studio — фронтовый движок (~5 КБ, без зависимостей).
 *
 * 1. sr-reveal / sr-cascade — появление блоков (порт из прототипа).
 * 2. .sr-barra[data-sr-target] — la barra dei cento: заливка до целевого %.
 * 3. .sr-counter[data-sr-to] — счётчик числа (0 → цель, ease-out cubic).
 * 4. Фолбэк для анимаций Prespa: если JS родительской темы не добавил
 *    .animated элементам .p-animation-*, добавляем сами по тому же контракту.
 * 5. Demo-виджеты (hero, test velocità) — детерминированный fake-скоринг
 *    по хешу URL, как в дизайн-прототипе. В продакшене заменить на реальный
 *    вызов PageSpeed Insights API (см. TODO в конце файла).
 * 6. Cookie-banner + WhatsApp FAB — сайтвайд, инжектятся в футер через
 *    functions.php (remarka_inject_footer_widgets), логика здесь.
 *
 * prefers-reduced-motion: всё видимо сразу, ничего не движется (см. CSS).
 */
(function () {
	'use strict';

	var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	function onReady(fn) {
		if (document.readyState === 'loading') {
			document.addEventListener('DOMContentLoaded', fn);
		} else {
			fn();
		}
	}

	/* ---------- 1. Reveal ---------- */

	function initReveal() {
		var targets = document.querySelectorAll('.sr-reveal, .sr-cascade');
		if (!targets.length) {
			return;
		}
		if (reduced || !('IntersectionObserver' in window)) {
			targets.forEach(function (el) { el.classList.add('sr-visible'); });
			return;
		}

		document.querySelectorAll('.sr-cascade').forEach(function (container) {
			Array.prototype.forEach.call(container.children, function (child, i) {
				child.style.transitionDelay = (i * 80) + 'ms';
			});
		});

		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (entry.isIntersecting) {
					entry.target.classList.add('sr-visible');
					io.unobserve(entry.target);
				}
			});
		}, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

		targets.forEach(function (el) { io.observe(el); });
	}

	/* ---------- 2. Barra ---------- */

	function initBarre() {
		var bars = document.querySelectorAll('.sr-barra[data-sr-target]');
		if (!bars.length) {
			return;
		}

		bars.forEach(function (bar) {
			bar.style.setProperty('--sr-barra-target', bar.getAttribute('data-sr-target'));
		});

		if (reduced || !('IntersectionObserver' in window)) {
			bars.forEach(function (bar) { bar.setAttribute('data-barra-ready', ''); });
			return;
		}

		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (!entry.isIntersecting) {
					return;
				}
				var bar = entry.target;
				var delay = parseInt(bar.getAttribute('data-sr-delay') || '0', 10);
				window.setTimeout(function () {
					bar.setAttribute('data-barra-ready', '');
				}, delay);
				io.unobserve(bar);
			});
		}, { threshold: 0.4 });

		bars.forEach(function (bar) { io.observe(bar); });
	}

	/* ---------- 3. Счётчики ---------- */

	function easeOutCubic(t) {
		return 1 - Math.pow(1 - t, 3);
	}

	function formatIt(value, decimals) {
		return value.toFixed(decimals).replace('.', ',');
	}

	/**
	 * Цель счётчика: data-sr-to, а если атрибута нет — текст самого элемента
	 * (редактор меняет число прямо в абзаце). Анимируются только «чистые»
	 * числа (например «97» или «4,9»); всё остальное («−38%», «12 mesi»)
	 * остаётся статичным.
	 */
	function counterTarget(el) {
		var attr = el.getAttribute('data-sr-to');
		var raw = (attr !== null ? attr : el.textContent).trim();
		if (!/^\d+(?:[.,]\d+)?$/.test(raw)) {
			return null;
		}
		return {
			to: parseFloat(raw.replace(',', '.')),
			decimals: (raw.split(/[.,]/)[1] || '').length
		};
	}

	function initCounters() {
		var counters = document.querySelectorAll('.sr-counter');
		if (!counters.length) {
			return;
		}

		if (reduced || !('IntersectionObserver' in window)) {
			return; // текст уже содержит финальное значение
		}

		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (!entry.isIntersecting) {
					return;
				}
				var el = entry.target;
				io.unobserve(el);
				var t = counterTarget(el);
				if (!t) {
					return;
				}
				var start = performance.now();
				var dur = 1200;

				function tick(now) {
					var p = Math.min(1, (now - start) / dur);
					el.textContent = formatIt(t.to * easeOutCubic(p), t.decimals);
					if (p < 1) {
						window.requestAnimationFrame(tick);
					}
				}

				window.requestAnimationFrame(tick);
			});
		}, { threshold: 0.4 });

		counters.forEach(function (el) {
			if (counterTarget(el)) {
				io.observe(el);
			}
		});
	}

	/* ---------- 4. Фолбэк для .p-animation-* (движок Prespa) ---------- */

	function initPrespaFallback() {
		if (reduced) {
			return;
		}
		window.setTimeout(function () {
			var pending = document.querySelectorAll('[class*="p-animation-"]:not(.animated)');
			var done = document.querySelector('[class*="p-animation-"].animated');
			if (!pending.length || done) {
				return; // родительский JS работает — не вмешиваемся
			}
			if (!('IntersectionObserver' in window)) {
				pending.forEach(function (el) { el.classList.add('animated'); });
				return;
			}
			var io = new IntersectionObserver(function (entries) {
				entries.forEach(function (entry) {
					if (entry.isIntersecting) {
						entry.target.classList.add('animated');
						io.unobserve(entry.target);
					}
				});
			}, { threshold: 0.2 });
			pending.forEach(function (el) { io.observe(el); });
		}, 1500);
	}

	/* ---------- 5. Виджеты скорости: реальный PageSpeed Insights API ----------
	   Vera Google PSI API (v5, CORS-abilitata, chiamabile dal browser).
	   Chiave API opzionale via Customizer (window.remarkaPSI.key) — senza
	   chiave la quota anonima è bassa ma sufficiente per traffico iniziale.
	   In caso di errore/quota: messaggio onesto, MAI numeri simulati. */

	function itNumber(value, decimals, locale) {
		var s = value.toFixed(decimals);
		return locale === 'en' ? s : s.replace('.', ',');
	}

	function normalizeUrl(raw) {
		var url = (raw || '').trim();
		if (!url) {
			return null;
		}
		if (!/^https?:\/\//i.test(url)) {
			url = 'https://' + url;
		}
		try {
			return new URL(url).href;
		} catch (err) {
			return null;
		}
	}

	/**
	 * Estrae fino a 3 risorse concrete (url + valore leggibile) dai
	 * `details.items` di un audit Lighthouse, per i "rilievi" del check-up
	 * (M5, docs/piano-checkup-sito.md). Non tutti gli audit hanno un url per
	 * item (es. audit di accessibilità basati su nodo DOM): in quel caso la
	 * lista resta vuota, il chiamante mostra solo il titolo dell'audit.
	 */
	function auditItemValue(item) {
		if (typeof item.wastedMs === 'number') return Math.round(item.wastedMs) + ' ms';
		if (typeof item.wastedBytes === 'number') return Math.round(item.wastedBytes / 1024) + ' KB';
		if (typeof item.totalBytes === 'number') return Math.round(item.totalBytes / 1024) + ' KB';
		if (typeof item.transferSize === 'number') return Math.round(item.transferSize / 1024) + ' KB';
		return '';
	}
	function auditResources(audit) {
		var items = (audit && audit.details && Array.isArray(audit.details.items)) ? audit.details.items : [];
		var out = [];
		for (var i = 0; i < items.length && out.length < 3; i++) {
			var it = items[i];
			var url = it && typeof it.url === 'string' ? it.url : null;
			if (!url) continue;
			out.push({ u: url.slice(0, 300), v: auditItemValue(it).slice(0, 200) });
		}
		return out;
	}

	/**
	 * Chiamata unica a PageSpeed Insights su quattro categorie (performance,
	 * accessibility, seo, best-practices) + estrazione byte-weight e audit
	 * falliti localizzati. `locale` (it|en|ru) fa restituire a Google i titoli
	 * degli audit tradotti. La 4ª categoria (BEST_PRACTICES) serve al check-up
	 * completo (docs/copy-checkup.md §1.1): un'unica chiamata PSI copre 4 delle
	 * 7 dimensioni, più il byte-weight per il modulo CO₂.
	 * Ritorna:
	 *   scores: {perf, a11y, seo, bp}   (0–100 o null)
	 *   byteWeight: numericValue di total-byte-weight (byte) o null
	 *   byteWeightItems: fino a 3 risorse più pesanti {u,v} (M5, per i rilievi CO₂)
	 *   lcpSec / inpMs / cls        (metriche Core Web Vitals)
	 *   audits: {perf/a11y/seo/bp:[{id,title,score,items:[{u,v}]}]}  (falliti score<0.9, peggiori prima)
	 */
	function psiFetch(url, locale, categories) {
		locale = locale || 'it';
		var cats = categories && categories.length ? categories : ['PERFORMANCE', 'ACCESSIBILITY', 'SEO', 'BEST_PRACTICES'];
		var endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed' +
			'?url=' + encodeURIComponent(url) +
			'&strategy=mobile' +
			cats.map(function (c) { return '&category=' + c; }).join('') +
			'&locale=' + encodeURIComponent(locale);
		var key = (window.remarkaPSI && window.remarkaPSI.key) || '';
		if (key) {
			endpoint += '&key=' + encodeURIComponent(key);
		}
		/* Se la chiamata diretta a googleapis.com fallisce (CSP dell'hosting,
		   estensioni del browser, chiave con restrizioni), ripieghiamo sul
		   proxy del nostro server: stessa risposta JSON, chiave lato PHP. */
		function viaProxy() {
			var cfg = window.remarkaPSI || {};
			if (!cfg.ajaxUrl) {
				throw new Error('PSI proxy non disponibile');
			}
			var pu = cfg.ajaxUrl + '?action=remarka_tool_psi' +
				'&nonce=' + encodeURIComponent(cfg.toolsNonce || '') +
				'&url=' + encodeURIComponent(url) +
				'&categories=' + encodeURIComponent(cats.join(',')) +
				'&locale=' + encodeURIComponent(locale);
			return window.fetch(pu).then(function (resp) {
				if (!resp.ok) {
					throw new Error('PSI proxy HTTP ' + resp.status);
				}
				return resp.json();
			});
		}
		return window.fetch(endpoint).then(function (resp) {
			if (!resp.ok) {
				throw new Error('PSI HTTP ' + resp.status);
			}
			return resp.json();
		}).catch(function () {
			return viaProxy();
		}).then(function (data) {
			var lh = data.lighthouseResult;
			if (!lh || !lh.categories) {
				throw new Error('PSI: risposta senza punteggio');
			}
			var cats = lh.categories;
			var audits = lh.audits || {};

			function catScore(c) {
				return c && typeof c.score === 'number' ? Math.round(c.score * 100) : null;
			}

			function topAudits(cat) {
				var out = [];
				if (!cat || !cat.auditRefs) {
					return out;
				}
				cat.auditRefs.forEach(function (ref) {
					var a = audits[ref.id];
					if (!a || typeof a.score !== 'number' || a.score >= 0.9) {
						return;
					}
					var mode = a.scoreDisplayMode;
					if (mode === 'notApplicable' || mode === 'informative' || mode === 'manual') {
						return;
					}
					out.push({ id: ref.id, title: a.title || ref.id, score: a.score, items: auditResources(a) });
				});
				out.sort(function (a, b) { return a.score - b.score; });
				return out;
			}

			var field = (data.loadingExperience && data.loadingExperience.metrics) || {};
			var lcpAudit = audits['largest-contentful-paint'];
			var clsAudit = audits['cumulative-layout-shift'];
			var inpField = field.INTERACTION_TO_NEXT_PAINT;
			var byteAudit = audits['total-byte-weight'];

			return {
				scores: {
					perf: catScore(cats.performance),
					a11y: catScore(cats.accessibility),
					seo: catScore(cats.seo),
					bp: catScore(cats['best-practices'])
				},
				byteWeight: byteAudit && typeof byteAudit.numericValue === 'number' ? byteAudit.numericValue : null,
				byteWeightItems: auditResources(byteAudit),
				lcpSec: lcpAudit && typeof lcpAudit.numericValue === 'number' ? lcpAudit.numericValue / 1000 : null,
				cls: clsAudit && typeof clsAudit.numericValue === 'number' ? clsAudit.numericValue : null,
				inpMs: inpField && typeof inpField.percentile === 'number' ? inpField.percentile : null,
				audits: {
					perf: topAudits(cats.performance),
					a11y: topAudits(cats.accessibility),
					seo: topAudits(cats.seo),
					bp: topAudits(cats['best-practices'])
				}
			};
		});
	}

	var PSI_ERROR_MSG = 'Non siamo riusciti a completare il test (il servizio Google potrebbe essere momentaneamente saturo). Riprovate tra qualche minuto — oppure scriveteci: lo facciamo noi e vi mandiamo il report.';

	/** Виджет в hero: собственный балл студии + форма «а у вас?». */
	function initHeroWidgets() {
		document.querySelectorAll('[data-sr-hero-form]').forEach(function (form) {
			var pending = form.querySelector('[data-sr-hero-pending]');
			var result = form.querySelector('[data-sr-hero-result]');
			var urlOut = form.querySelector('[data-sr-hero-url]');
			var scoreOut = form.querySelector('[data-sr-hero-score]');
			var fill = form.querySelector('[data-sr-hero-fill]');
			var running = false;

			form.addEventListener('submit', function (e) {
				e.preventDefault();
				if (running) {
					return;
				}
				var input = form.querySelector('input[type="text"]');
				var url = normalizeUrl(input && input.value);
				if (!url) {
					if (input) input.focus();
					return;
				}
				running = true;
				if (pending) pending.hidden = false;
				if (result) result.hidden = true;
				if (fill) fill.style.width = '0%';

				psiFetch(url, toolLocale(form), ['PERFORMANCE']).then(function (m) {
					var score = m.scores.perf;
					if (urlOut) urlOut.textContent = url.replace(/^https?:\/\//, '');
					if (scoreOut) scoreOut.textContent = score === null ? '—' : String(score);
					if (result) result.hidden = false;
					if (fill && score !== null) {
						window.requestAnimationFrame(function () {
							window.requestAnimationFrame(function () {
								fill.style.width = score + '%';
							});
						});
					}
				}).catch(function () {
					if (urlOut) urlOut.textContent = PSI_ERROR_MSG;
					if (scoreOut) scoreOut.textContent = '—';
					if (result) result.hidden = false;
				}).finally(function () {
					if (pending) pending.hidden = true;
					running = false;
				});
			});
		});
	}

	/* ============================================================================
	 * Remarka Lab — motore degli 8 strumenti gratuiti (+ il check-up completo,
	 * l'orchestratore che li riassume).
	 *
	 * DISPATCHER: initToolWidgets() cerca ogni contenitore [data-sr-tool="…"] e
	 * inizializza il modulo giusto (speed|seo|a11y|co2|gdpr|ai|roi|checkup). Retro-
	 * compatibilità: un <form data-sr-tool-form> senza wrapper [data-sr-tool] è
	 * trattato come 'speed' (la pagina test-velocità esistente non si rompe).
	 *
	 * ─────────────────────────────────────────────────────────────────────────
	 * CONTRATTO DATA-ATTRIBUTI (API tra questo JS e le pagine — per T2)
	 * ─────────────────────────────────────────────────────────────────────────
	 * Tutte le stringhe visibili nei risultati si LEGGONO dai data-* del
	 * contenitore-widget (ogni pagina per-lingua porta le proprie): se assenti,
	 * fallback in italiano qui sotto. Il tipo si sceglie con data-sr-tool.
	 *
	 * COMUNE a tutti:
	 *   data-sr-tool="speed|seo|a11y|co2|gdpr|ai|roi|checkup|eeat"   (obbligatorio sul wrapper)
	 *   data-sr-locale="it|en|ru"        locale PSI (default: window.remarkaPSI.locale|it)
	 *   [data-sr-tool-form]              il <form> (input url + submit)
	 *   input[type=text]                 campo URL
	 *   [data-sr-tool-pending]           messaggio "in corso" (hidden di default)
	 *   [data-sr-tool-result]            contenitore risultato (hidden di default)
	 *   data-err                         messaggio d'errore fetch (fallback PSI_ERROR_MSG)
	 *
	 * SCORE-BASED (speed, seo, a11y): barra 0–100 + verdetto.
	 *   [data-sr-tool-url]     riga sopra il punteggio (etichetta url)
	 *   [data-sr-tool-score]   numero 0–100
	 *   [data-sr-tool-fill]    .sr-barra__fill (larghezza = score%)
	 *   [data-sr-tool-verdict] testo del verdetto
	 *   data-verdict-good / data-verdict-mid / data-verdict-poor  (soglie 90 / 50)
	 *   data-label-suffix      suffisso della riga url (es. " — PageSpeed mobile")
	 *   speed extra: [data-sr-tool-lcp] [data-sr-tool-inp] [data-sr-tool-cls]
	 *   seo/a11y extra: [data-sr-tool-audits] <ul> dove elenca gli audit falliti (≤6)
	 *     data-audits-empty  testo se non ci sono audit falliti
	 *
	 * CO2 (data-sr-tool="co2"):
	 *   [data-sr-tool-grams]    g CO₂e / visita
	 *   [data-sr-tool-weight]   peso pagina (MB)
	 *   [data-sr-tool-year]     kg CO₂e / anno (su data-co2-visits, default 10000/mese)
	 *   [data-sr-tool-verdict]  verdetto vs media
	 *   [data-sr-tool-fill]     barra (grammi vs 2× media = 100%)
	 *   data-co2-average        media di confronto in g (default 0.8)
	 *   data-co2-visits         visite/mese per la stima annua (default 10000)
	 *   data-verdict-good/-mid/-poor  (sotto media / vicino / sopra)
	 *   data-label-unit-year    etichetta unità annua (default "kg CO₂e / anno")
	 *
	 * GDPR (data-sr-tool="gdpr"): semaforo a 4 punti (euristica, non parere legale).
	 *   [data-sr-tool-cmp]      esito CMP           [data-sr-tool-policy]  esito policy
	 *   [data-sr-tool-trackers] esito tracker       [data-sr-tool-external] n. domini esterni
	 *   ogni riga può avere un [data-sr-flag] impostato a good|warn|bad (per CSS)
	 *   data-label-cmp-yes / data-label-cmp-no
	 *   data-label-policy-yes / data-label-policy-no
	 *   data-label-trackers-clean / data-label-trackers-flag / data-label-trackers-ok
	 *   data-label-external      template (usa {n})
	 *   [data-sr-tool-disclaimer] (statico nella pagina, non toccato dal JS)
	 *
	 * AI (data-sr-tool="ai"): punteggio N/4.
	 *   [data-sr-tool-score]    "N/4"
	 *   [data-sr-tool-llms] [data-sr-tool-robots] [data-sr-tool-jsonld] [data-sr-tool-sitemap]
	 *   ogni riga [data-sr-flag]=good|warn|bad
	 *   data-label-yes / data-label-no / data-label-partial
	 *
	 * ROI (data-sr-tool="roi"): calcolatore puro, nessuna rete.
	 *   input[data-sr-roi-visits] [data-sr-roi-foreign] [data-sr-roi-conv]
	 *        [data-sr-roi-order] [data-sr-roi-boost]
	 *   [data-sr-tool-result]   (mostrato sempre)
	 *   [data-sr-roi-annual]    ricavo/anno stimato
	 *   [data-sr-roi-monthly]   ricavo/mese stimato
	 *   data-roi-currency       simbolo (default "€")
	 *
	 * EEAT (data-sr-tool="eeat"): punteggio 0–100 su 8 segnali di fiducia
	 * on-page, raggruppati in 4 assi E-E-A-T (docs/copy-eeat.md).
	 *   [data-sr-tool-url] [data-sr-tool-score] [data-sr-tool-fill] [data-sr-tool-verdict]
	 *   data-verdict-good (≥90) / data-verdict-buono (75–89) / data-verdict-mid (50–74) /
	 *     data-verdict-poor (<50)
	 *   4 assi, valore 0–100 + [data-sr-flag]=good|warn|bad (soglie 75/50):
	 *     [data-sr-tool-axis-esperienza] [data-sr-tool-axis-competenza]
	 *     [data-sr-tool-axis-autorevolezza] [data-sr-tool-axis-affidabilita]
	 *   8 segnali, ognuno [data-sr-flag]=good|warn|bad:
	 *     [data-sr-tool-https] [data-sr-tool-contatti] [data-sr-tool-legale]
	 *     [data-sr-tool-policy] [data-sr-tool-chisiamo] [data-sr-tool-portfolio]
	 *     [data-sr-tool-schema] [data-sr-tool-profili]
	 *   data-label-{signal}-{good|warn|bad}   testo per ogni segnale/esito
	 *     (segnali binari: solo -good/-bad). Chiavi: https, contatti, legale,
	 *     policy, chisiamo, portfolio, schema, profili.
	 *   [data-sr-tool-notice]   avviso «analisi parziale» SPA (hidden di default)
	 *   data-notice             testo dell'avviso
	 *   data-label-nd           suffisso annotato sui segnali "bad" quando l'avviso è attivo
	 *   [data-sr-tool-disclaimer] (statico nella pagina, non toccato dal JS)
	 * ========================================================================== */

	function toolLocale(el) {
		var attr = el && el.getAttribute && el.getAttribute('data-sr-locale');
		return attr || (window.remarkaPSI && window.remarkaPSI.locale) || 'it';
	}

	function txt(root, name, fallback) {
		var v = root && root.getAttribute ? root.getAttribute(name) : null;
		return (v === null || v === '') ? fallback : v;
	}

	function q(root, sel) { return root.querySelector(sel); }

	function setText(root, sel, text) {
		var el = root.querySelector(sel);
		if (el) el.textContent = text;
	}

	function animateFill(root, sel, pct) {
		var fill = root.querySelector(sel);
		if (!fill) return;
		fill.style.width = '0%';
		window.requestAnimationFrame(function () {
			window.requestAnimationFrame(function () {
				fill.style.width = Math.max(0, Math.min(100, pct)) + '%';
			});
		});
	}

	function scoreVerdict(root, score) {
		if (score === null) return '';
		if (score < 50) return txt(root, 'data-verdict-poor', 'Punteggio basso: è la priorità da sistemare.');
		if (score < 90) return txt(root, 'data-verdict-mid', 'Nella media, ma lontano dagli standard consigliati: ci sono margini concreti.');
		return txt(root, 'data-verdict-good', 'Ottimo: il sito rispetta gli standard consigliati.');
	}

	/** Ricava il form e prepara pending/result/running per i moduli con rete. */
	function toolShell(root) {
		var form = root.matches && root.matches('[data-sr-tool-form]') ? root : (root.querySelector('[data-sr-tool-form]') || root);
		return {
			root: root,
			form: form,
			pending: root.querySelector('[data-sr-tool-pending]'),
			result: root.querySelector('[data-sr-tool-result]'),
			errMsg: txt(root, 'data-err', PSI_ERROR_MSG)
		};
	}

	/** Precompila e avvia da `?url=…&autostart=1`: usato dal redirect del
	 * blocco home check-up (initCheckupHomeForm) e dai link "Approfondisci →"
	 * delle card check-up (renderCheckupResults). Generico: agganciato da
	 * onUrlSubmit() a ogni widget [data-sr-tool] con un form URL, non solo
	 * al check-up. */
	function toolMaybeAutostart(shell) {
		var params;
		try {
			params = new URLSearchParams(window.location.search);
		} catch (e) {
			return;
		}
		var urlParam = params.get('url');
		if (!urlParam) return;
		var input = shell.form.querySelector('input[type="text"], input[type="url"]');
		if (input) input.value = urlParam;
		if (params.get('autostart') === '1') {
			window.setTimeout(function () {
				if (shell.form.requestSubmit) {
					shell.form.requestSubmit();
					return;
				}
				var ev = null;
				try { ev = new Event('submit', { cancelable: true }); } catch (e2) { /* ambienti molto vecchi */ }
				if (ev) shell.form.dispatchEvent(ev);
			}, 0);
		}
	}

	function onUrlSubmit(shell, handler) {
		var running = false;
		shell.form.addEventListener('submit', function (e) {
			e.preventDefault();
			if (running) return;
			var input = shell.form.querySelector('input[type="text"], input[type="url"]');
			var url = normalizeUrl(input && input.value);
			if (!url) { if (input) input.focus(); return; }
			running = true;
			if (shell.pending) shell.pending.hidden = false;
			if (shell.result) shell.result.hidden = true;
			Promise.resolve()
				.then(function () { return handler(url); })
				.then(function () { if (shell.result) shell.result.hidden = false; })
				.catch(function () { showToolError(shell); })
				.then(function () {
					if (shell.pending) shell.pending.hidden = true;
					running = false;
				});
		});
		toolMaybeAutostart(shell);
	}

	function showToolError(shell) {
		setText(shell.root, '[data-sr-tool-verdict]', shell.errMsg);
		setText(shell.root, '[data-sr-tool-url]', '');
		if (shell.result) shell.result.hidden = false;
	}

	/* ---------- Modulo: velocità (PageSpeed performance) ---------- */
	function speedVerdict(root, score) {
		// Fallback identici alla copy live di /strumenti/test-velocita/.
		if (score === null) return '';
		if (score < 50) return txt(root, 'data-verdict-poor', 'Il sito è lento su mobile: la maggior parte dei visitatori abbandona prima del caricamento completo. Un restyling tecnico è la priorità.');
		if (score < 90) return txt(root, 'data-verdict-mid', 'Il sito è nella media, ma lontano dagli standard consigliati da Google. Ci sono margini di miglioramento concreti e misurabili.');
		return txt(root, 'data-verdict-good', 'Ottimo punteggio: il sito rispetta gli standard Google per l’esperienza mobile.');
	}

	function initSpeedTool(root) {
		var shell = toolShell(root);
		onUrlSubmit(shell, function (url) {
			var locale = toolLocale(root);
			return psiFetch(url, locale, ['PERFORMANCE']).then(function (m) {
				var score = m.scores.perf;
				setText(root, '[data-sr-tool-url]', url.replace(/^https?:\/\//, '') + txt(root, 'data-label-suffix', ' — PageSpeed mobile'));
				setText(root, '[data-sr-tool-score]', score === null ? '—' : String(score));
				setText(root, '[data-sr-tool-verdict]', speedVerdict(root, score));
				setText(root, '[data-sr-tool-lcp]', m.lcpSec !== null ? itNumber(m.lcpSec, 1, locale) + ' s' : '—');
				setText(root, '[data-sr-tool-inp]', m.inpMs !== null ? Math.round(m.inpMs) + ' ms' : '—');
				setText(root, '[data-sr-tool-cls]', m.cls !== null ? itNumber(m.cls, 2, locale) : '—');
				if (score !== null) animateFill(root, '[data-sr-tool-fill]', score);
			});
		});
	}

	/* ---------- Modulo: SEO / accessibilità (PSI category + lista audit) ---------- */
	function initLighthouseTool(root, kind) {
		var shell = toolShell(root);
		var scoreKey = kind === 'seo' ? 'seo' : 'a11y';
		onUrlSubmit(shell, function (url) {
			return psiFetch(url, toolLocale(root), [kind === 'seo' ? 'SEO' : 'ACCESSIBILITY']).then(function (m) {
				var score = m.scores[scoreKey];
				setText(root, '[data-sr-tool-url]', url.replace(/^https?:\/\//, '') + txt(root, 'data-label-suffix', ''));
				setText(root, '[data-sr-tool-score]', score === null ? '—' : String(score));
				setText(root, '[data-sr-tool-verdict]', scoreVerdict(root, score));
				if (score !== null) animateFill(root, '[data-sr-tool-fill]', score);

				var list = q(root, '[data-sr-tool-audits]');
				if (list) {
					list.innerHTML = '';
					var items = (m.audits[scoreKey] || []).slice(0, 6);
					if (!items.length) {
						var li0 = document.createElement('li');
						li0.textContent = txt(root, 'data-audits-empty', 'Nessun problema rilevante rilevato.');
						list.appendChild(li0);
					} else {
						items.forEach(function (a) {
							var li = document.createElement('li');
							li.textContent = a.title;
							list.appendChild(li);
						});
					}
				}
			});
		});
	}

	/* ---------- Modulo: impatto CO₂ ----------
	 * Modello Sustainable Web Design (co2.js, The Green Web Foundation,
	 * Apache-2.0). Coefficienti SWD:
	 *   KWH_PER_GB = 0,81 ; ripartizione device/network/datacenter/production
	 *   0,52/0,14/0,15/0,19 (somma 1,0) ; cache first/return 0,75 e 0,25×0,02.
	 * Intensità di rete globale (media WORLD) = 472,94 gCO₂e/kWh
	 * (data/output/average-intensities.js). Host "grey" (caso peggiore):
	 * i quattro segmenti condividono la stessa intensità → il calcolo si
	 * riduce a energia×intensità. Fonte: github.com/thegreenwebfoundation/co2.js */
	var CO2_KWH_PER_GB = 0.81;
	var CO2_GRID_INTENSITY = 472.94; // gCO₂e/kWh (media WORLD, co2.js)
	var CO2_CACHE_FACTOR = 0.75 + 0.25 * 0.02; // = 0,755 (per-visita)

	function co2PerVisitGrams(bytes) {
		var energyKwh = (bytes / 1e9) * CO2_KWH_PER_GB * CO2_CACHE_FACTOR;
		return energyKwh * CO2_GRID_INTENSITY; // segmenti sommano a 1,0 (grey)
	}
	function co2PerByteGrams(bytes) { // caricamento pieno, senza cache
		return (bytes / 1e9) * CO2_KWH_PER_GB * CO2_GRID_INTENSITY;
	}

	function initCo2Tool(root) {
		var shell = toolShell(root);
		onUrlSubmit(shell, function (url) {
			var locale = toolLocale(root);
			return psiFetch(url, locale, ['PERFORMANCE']).then(function (m) {
				if (m.byteWeight === null) { throw new Error('CO2: peso non disponibile'); }
				var grams = co2PerVisitGrams(m.byteWeight);
				var mb = m.byteWeight / (1024 * 1024);
				var avg = parseFloat(txt(root, 'data-co2-average', '0.8')) || 0.8;
				var visits = parseFloat(txt(root, 'data-co2-visits', '10000')) || 10000;
				var yearKg = grams * visits * 12 / 1000;

				setText(root, '[data-sr-tool-url]', url.replace(/^https?:\/\//, ''));
				setText(root, '[data-sr-tool-grams]', itNumber(grams, 2, locale) + ' g');
				setText(root, '[data-sr-tool-weight]', itNumber(mb, 2, locale) + ' MB');
				setText(root, '[data-sr-tool-year]', itNumber(yearKg, 0, locale) + ' ' + txt(root, 'data-label-unit-year', 'kg CO₂e / anno'));

				var verdict;
				if (grams <= avg) verdict = txt(root, 'data-verdict-good', 'Sotto la media del web: buon lavoro.');
				else if (grams <= avg * 1.5) verdict = txt(root, 'data-verdict-mid', 'Vicino alla media del web: c’è margine per alleggerire.');
				else verdict = txt(root, 'data-verdict-poor', 'Sopra la media del web: la pagina è pesante, conviene ottimizzare.');
				setText(root, '[data-sr-tool-verdict]', verdict);

				animateFill(root, '[data-sr-tool-fill]', grams / (avg * 2) * 100);
			});
		});
	}

	/* ---------- Modulo: GDPR (euristica onesta, non parere legale) ---------- */
	var GDPR_CMPS = ['iubenda', 'cookiebot', 'complianz', 'onetrust', 'cookieyes', 'borlabs', 'klaro'];
	var GDPR_TRACKERS = [
		{ re: /gtag\(|googletagmanager\.com|google-analytics\.com|gtag\/js|\bga\(/i, name: 'Google Analytics / gtag' },
		{ re: /connect\.facebook\.net|fbevents\.js|fbq\(/i, name: 'Meta Pixel' },
		{ re: /clarity\.ms|clarity\("|window\.clarity/i, name: 'Microsoft Clarity' },
		{ re: /static\.hotjar\.com|hotjar\.com|hj\(/i, name: 'Hotjar' }
	];

	function setFlag(root, sel, flag) {
		var el = q(root, sel);
		if (el) el.setAttribute('data-sr-flag', flag);
	}

	/**
	 * Funzione pura (nessun accesso al DOM): legge l'HTML grezzo della pagina
	 * (via remarka_tool_fetch) e ne estrae i 4 segnali GDPR. Riutilizzata da
	 * initGdprTool (rendering pagina strumento) e dall'orchestratore check-up
	 * (docs/copy-checkup.md §1.2 — stessi 4 segnali, pesi diversi).
	 * Ritorna: { cmp: string|null, hasPolicy: bool, trackersFound: string[], externalCount: int, domains: string[] }
	 * `domains` (M5): gli hostname di terze parti effettivamente trovati negli
	 * src degli script — usati per i rilievi del check-up (link cliccabili).
	 */
	function runGdprCheck(url) {
		return toolFetch(url, 'html').then(function (data) {
			var html = data.body || '';
			var lower = html.toLowerCase();

			var cmp = null;
			GDPR_CMPS.forEach(function (name) { if (!cmp && lower.indexOf(name) !== -1) cmp = name; });

			var hasPolicy = /href=["'][^"']*(privacy|cookie|informativa)[^"']*["']/i.test(html) ||
				/(privacy policy|cookie policy|informativa (sulla )?privacy)/i.test(html);

			var trackersFound = [];
			GDPR_TRACKERS.forEach(function (t) { if (t.re.test(html)) trackersFound.push(t.name); });

			var domains = {};
			var re = /<script[^>]+src=["']https?:\/\/([^\/"']+)/gi, mm;
			while ((mm = re.exec(html)) !== null) { domains[mm[1].toLowerCase()] = true; }

			return { cmp: cmp, hasPolicy: hasPolicy, trackersFound: trackersFound, externalCount: Object.keys(domains).length, domains: Object.keys(domains) };
		});
	}

	/** Deriva i 4 flag good|warn|bad dai segnali grezzi (stessa logica per pagina strumento e check-up). */
	function gdprSignalFlags(sig) {
		var trackFlag;
		if (sig.trackersFound.length && !sig.cmp) {
			trackFlag = 'bad';
		} else if (sig.trackersFound.length) {
			trackFlag = 'warn';
		} else {
			trackFlag = 'good';
		}
		return {
			cmpFlag: sig.cmp ? 'good' : 'bad',
			policyFlag: sig.hasPolicy ? 'good' : 'bad',
			trackFlag: trackFlag,
			externalFlag: sig.externalCount === 0 ? 'good' : (sig.externalCount <= 5 ? 'warn' : 'bad')
		};
	}

	function initGdprTool(root) {
		var shell = toolShell(root);
		onUrlSubmit(shell, function (url) {
			return runGdprCheck(url).then(function (sig) {
				var flags = gdprSignalFlags(sig);

				setText(root, '[data-sr-tool-cmp]', sig.cmp
					? txt(root, 'data-label-cmp-yes', 'Cookie banner rilevato') + ' (' + sig.cmp + ')'
					: txt(root, 'data-label-cmp-no', 'Nessun cookie banner rilevato'));
				setFlag(root, '[data-sr-tool-cmp]', flags.cmpFlag);

				setText(root, '[data-sr-tool-policy]', sig.hasPolicy
					? txt(root, 'data-label-policy-yes', 'Link a privacy/cookie policy presente')
					: txt(root, 'data-label-policy-no', 'Nessun link a privacy/cookie policy'));
				setFlag(root, '[data-sr-tool-policy]', flags.policyFlag);

				var trackText;
				if (flags.trackFlag === 'bad') {
					trackText = txt(root, 'data-label-trackers-flag', 'Tracker attivi senza banner') + ': ' + sig.trackersFound.join(', ');
				} else if (flags.trackFlag === 'warn') {
					trackText = txt(root, 'data-label-trackers-ok', 'Tracker presenti (con banner)') + ': ' + sig.trackersFound.join(', ');
				} else {
					trackText = txt(root, 'data-label-trackers-clean', 'Nessun tracker nell’HTML iniziale');
				}
				setText(root, '[data-sr-tool-trackers]', trackText);
				setFlag(root, '[data-sr-tool-trackers]', flags.trackFlag);

				var tmpl = txt(root, 'data-label-external', '{n} domini esterni caricano script');
				setText(root, '[data-sr-tool-external]', tmpl.replace('{n}', String(sig.externalCount)));
				setFlag(root, '[data-sr-tool-external]', flags.externalFlag);
			});
		});
	}

	/* ---------- Modulo: pronto per l'AI (llms.txt / robots / JSON-LD / sitemap) ---------- */
	var AI_CRAWLERS = ['GPTBot', 'ClaudeBot', 'PerplexityBot', 'Google-Extended'];

	function robotsAllows(robots, agent) {
		// Ritorna 'blocked' | 'allowed' | 'unmentioned' per uno user-agent.
		var lines = robots.split(/\r?\n/);
		var inBlock = false, disallowAll = false, mentioned = false;
		for (var i = 0; i < lines.length; i++) {
			var line = lines[i].replace(/#.*$/, '').trim();
			if (!line) continue;
			var ua = line.match(/^user-agent:\s*(.+)$/i);
			if (ua) {
				var val = ua[1].trim();
				if (val.toLowerCase() === agent.toLowerCase()) { inBlock = true; mentioned = true; }
				else { inBlock = false; }
				continue;
			}
			if (inBlock) {
				var dis = line.match(/^disallow:\s*(.*)$/i);
				if (dis) { if (dis[1].trim() === '/') disallowAll = true; }
			}
		}
		if (!mentioned) return 'unmentioned';
		return disallowAll ? 'blocked' : 'allowed';
	}

	/**
	 * Parser JSON-LD condiviso (puro, nessun accesso al DOM): estrae ogni
	 * blocco <script type="application/ld+json">, i valori @type (anche dentro
	 * @graph) e sameAs. Un blocco malformato conta comunque come "presente"
	 * (coerente con l'euristica storica di initAiTool) e alza `malformed`.
	 * Riutilizzato da runAiCheck e da runEeatCheck (segnale "Dati strutturati").
	 * Ritorna: { present: bool, malformed: bool, types: string[], sameAs: string[] }
	 */
	function extractJsonLd(html) {
		var out = { present: false, malformed: false, types: [], sameAs: [] };
		var collect = function (o) {
			if (!o) return;
			if (o['@type']) out.types.push(String(o['@type']));
			if (o.sameAs) {
				(Array.isArray(o.sameAs) ? o.sameAs : [o.sameAs]).forEach(function (s) {
					if (s) out.sameAs.push(String(s));
				});
			}
			if (Array.isArray(o['@graph'])) { o['@graph'].forEach(collect); }
		};
		var re = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi, mm;
		while ((mm = re.exec(html)) !== null) {
			out.present = true;
			try {
				var json = JSON.parse(mm[1].trim());
				(Array.isArray(json) ? json : [json]).forEach(collect);
			} catch (e) {
				out.malformed = true;
				out.types.push('?');
			}
		}
		return out;
	}

	/**
	 * Funzione pura: le 4 verifiche di prontezza AI (llms.txt, robots, JSON-LD,
	 * sitemap), senza toccare il DOM. Riutilizzata da initAiTool e
	 * dall'orchestratore check-up (docs/copy-checkup.md §1.2 — stessi 4
	 * segnali, pesi diversi: JSON-LD 30 · sitemap 25 · robots 25 · llms 20).
	 * Ritorna: { llms: bool, robots: 'blocked'|'allowed'|'unmentioned', jsonld: bool, jsonldTypes: string[], sitemap: bool }
	 */
	function runAiCheck(url) {
		var checks = { llms: false, robotsRaw: '', jsonld: false, jsonldTypes: [], sitemap: false };
		var jobs = [
			toolFetch(url, 'path:llms.txt').then(function (d) {
				checks.llms = d.status === 200 && /#/.test(d.body || '');
			}, function () {}),
			toolFetch(url, 'path:robots.txt').then(function (d) {
				checks.robotsRaw = d.status === 200 ? (d.body || '') : '';
			}, function () { checks.robotsRaw = ''; }),
			toolFetch(url, 'html').then(function (d) {
				var body = d.body || '';
				var jsonld = extractJsonLd(body);
				checks.jsonld = jsonld.present;
				checks.jsonldTypes = jsonld.types;
			}, function () {}),
			toolFetch(url, 'path:sitemap.xml').then(function (d) {
				checks.sitemap = d.status === 200 && /<(urlset|sitemapindex)/i.test(d.body || '');
			}, function () {})
		];
		return Promise.all(jobs).then(function () {
			var robots = checks.robotsRaw
				? (function () {
					var anyBlocked = false, anyMentioned = false;
					AI_CRAWLERS.forEach(function (c) {
						var s = robotsAllows(checks.robotsRaw, c);
						if (s !== 'unmentioned') anyMentioned = true;
						if (s === 'blocked') anyBlocked = true;
					});
					return anyBlocked ? 'blocked' : (anyMentioned ? 'allowed' : 'unmentioned');
				})()
				: 'unmentioned';
			return { llms: checks.llms, robots: robots, jsonld: checks.jsonld, jsonldTypes: checks.jsonldTypes, sitemap: checks.sitemap };
		});
	}

	function initAiTool(root) {
		var shell = toolShell(root);
		onUrlSubmit(shell, function (url) {
			return runAiCheck(url).then(function (checks) {
				var yes = txt(root, 'data-label-yes', 'Sì');
				var no = txt(root, 'data-label-no', 'No');
				var partial = txt(root, 'data-label-partial', 'Parziale');

				setText(root, '[data-sr-tool-llms]', checks.llms ? yes : no);
				setFlag(root, '[data-sr-tool-llms]', checks.llms ? 'good' : 'bad');

				// robots "buono" = crawler AI non bloccati
				var robotsGood = checks.robots !== 'blocked';
				setText(root, '[data-sr-tool-robots]', checks.robots === 'blocked' ? no : (checks.robots === 'allowed' ? yes : partial));
				setFlag(root, '[data-sr-tool-robots]', checks.robots === 'blocked' ? 'bad' : (checks.robots === 'allowed' ? 'good' : 'warn'));

				var jsonldTxt = checks.jsonld ? (yes + (checks.jsonldTypes && checks.jsonldTypes.length ? ' (' + checks.jsonldTypes.slice(0, 4).join(', ') + ')' : '')) : no;
				setText(root, '[data-sr-tool-jsonld]', jsonldTxt);
				setFlag(root, '[data-sr-tool-jsonld]', checks.jsonld ? 'good' : 'bad');

				setText(root, '[data-sr-tool-sitemap]', checks.sitemap ? yes : no);
				setFlag(root, '[data-sr-tool-sitemap]', checks.sitemap ? 'good' : 'bad');

				var n = (checks.llms ? 1 : 0) + (robotsGood ? 1 : 0) + (checks.jsonld ? 1 : 0) + (checks.sitemap ? 1 : 0);
				setText(root, '[data-sr-tool-score]', n + '/4');
			});
		});
	}

	/* ============================================================================
	 * Modulo: segnali E-E-A-T (docs/copy-eeat.md) — 8° strumento Lab.
	 *
	 * Un solo fetch `toolFetch(url, 'html')`: leggiamo la home come farebbe un
	 * visitatore, senza passare da Google. Otto segnali on-page (regex/DOM sul
	 * primo HTML, nessun JavaScript eseguito) raggruppati in 4 assi E-E-A-T.
	 * L'HTTPS si legge dallo schema dell'URL normalizzato dall'utente (il
	 * fetch server-side non espone l'URL finale dopo eventuali redirect).
	 * ========================================================================== */

	// peso di ogni segnale (somma 100) — docs/copy-eeat.md §1.1/§1.2.
	var EEAT_WEIGHTS = {
		https: 8, contatti: 12, legale: 12, policy: 10,
		chisiamo: 12, portfolio: 10, schema: 20, profili: 16
	};
	// composizione dei 4 assi (§1.3) — le chiavi corrispondono a EEAT_WEIGHTS.
	var EEAT_AXES = {
		affidabilita: ['https', 'contatti', 'legale', 'policy'],
		esperienza: ['chisiamo', 'portfolio'],
		competenza: ['schema'],
		autorevolezza: ['profili']
	};
	var EEAT_AXIS_MAX = { affidabilita: 42, esperienza: 22, competenza: 20, autorevolezza: 16 };

	// Fallback IT (usati solo se la pagina non porta il data-label-* corrispondente).
	var EEAT_FALLBACK = {
		https: { good: 'Connessione sicura (HTTPS)', bad: 'Nessun HTTPS: connessione non sicura' },
		contatti: {
			good: 'Contatti verificabili presenti',
			warn: 'Solo un’email, nessun telefono o indirizzo',
			bad: 'Nessun contatto verificabile'
		},
		legale: { good: 'P.IVA / dati fiscali presenti', bad: 'Nessuna P.IVA o identità legale' },
		policy: {
			good: 'Privacy e cookie policy presenti',
			warn: 'Presente solo una delle due policy',
			bad: 'Nessuna privacy o cookie policy'
		},
		chisiamo: { good: 'Pagina «Chi siamo» presente', bad: 'Nessuna pagina «Chi siamo»' },
		portfolio: { good: 'Portfolio o casi studio presenti', bad: 'Nessun portfolio o caso studio' },
		schema: {
			good: 'Dati strutturati d’identità presenti',
			warn: 'JSON-LD presente ma solo generico',
			bad: 'Nessun dato strutturato JSON-LD'
		},
		profili: {
			good: 'Profili esterni collegati',
			warn: 'Un solo profilo esterno',
			bad: 'Nessun profilo esterno collegato'
		}
	};

	/** true se `href="…"` contiene la regex, oppure se il testo visibile di un <a> la contiene. */
	function eeatLinkOrTextMatch(html, re) {
		var hrefRe = new RegExp('href=["\'][^"\']*(?:' + re.source + ')[^"\']*["\']', 'i');
		if (hrefRe.test(html)) { return true; }
		var anchorRe = /<a\b[^>]*>([\s\S]*?)<\/a>/gi, m;
		while ((m = anchorRe.exec(html)) !== null) {
			if (re.test(m[1])) { return true; }
		}
		return false;
	}

	/** Lunghezza del testo visibile nel <body> (script/style/commenti/tag rimossi). */
	function eeatVisibleTextLength(html) {
		var bodyMatch = /<body[^>]*>([\s\S]*)<\/body>/i.exec(html);
		var body = bodyMatch ? bodyMatch[1] : html;
		var stripped = body
			.replace(/<script[\s\S]*?<\/script>/gi, ' ')
			.replace(/<style[\s\S]*?<\/style>/gi, ' ')
			.replace(/<!--[\s\S]*?-->/g, ' ')
			.replace(/<[^>]+>/g, ' ')
			.replace(/\s+/g, ' ')
			.trim();
		return stripped.length;
	}

	/** Euristica SPA/HTML scarno (§1.4): marker id="root"/"app" vuoto, o testo visibile < ~2 KB. */
	function eeatLooksThin(html) {
		if (/<div[^>]*\bid=["'](root|app)["'][^>]*>\s*<\/div>/i.test(html)) { return true; }
		return eeatVisibleTextLength(html) < 2000;
	}

	/** Domini social distinti collegati da un href= (linkedin/facebook/instagram/youtube/x/twitter/t.me). */
	function eeatSocialDomains(html) {
		var socialRe = /(linkedin\.com|facebook\.com|instagram\.com|youtube\.com|x\.com|twitter\.com|t\.me)/i;
		var hrefRe = /href=["'](https?:\/\/[^"']+)["']/gi, m, domains = {};
		while ((m = hrefRe.exec(html)) !== null) {
			var mm = socialRe.exec(m[1]);
			if (mm) { domains[mm[1].toLowerCase()] = true; }
		}
		return Object.keys(domains);
	}

	/**
	 * Funzione pura (nessun accesso al DOM/rete): gli 8 segnali E-E-A-T
	 * (docs/copy-eeat.md §1.1) letti da un HTML già scaricato + schema
	 * dell'URL normalizzato. Separata da runEeatCheck per essere testabile
	 * senza stub di rete (vedi scratchpad test unitari dello scoring).
	 * Ritorna: { flags: {https,contatti,legale,policy,chisiamo,portfolio,schema,profili: 'good'|'warn'|'bad'}, partial: bool }
	 */
	function eeatComputeFlags(html, scheme) {
		html = html || '';
		var jsonld = extractJsonLd(html);

		// 1. HTTPS — binario, dallo schema dell'URL (nessun downgrade rilevabile lato client).
		var httpsFlag = scheme === 'https' ? 'good' : 'bad';

		// 2. Contatti verificabili.
		var hasTel = /href=["']tel:/i.test(html);
		var hasMailto = /href=["']mailto:/i.test(html) || /[\w.+-]+@[\w-]+\.[a-z]{2,}/i.test(html);
		var hasAddressCap = /(via|viale|piazza|corso|str\.)\s+[^,<]{2,}?\b\d{5}\b/i.test(html);
		var contattiFlag = (hasTel || hasAddressCap) ? 'good' : (hasMailto ? 'warn' : 'bad');

		// 3. Identità legale — binario.
		var legaleRe = /(p\.?\s?iva|partita\s+iva|\bvat\b|\brea\b|c\.?f\.?|cod(?:ice)?\s+fisc)/i;
		var legaleFlag = (legaleRe.test(html) || /\b\d{11}\b/.test(html)) ? 'good' : 'bad';

		// 4. Privacy & cookie policy — buone entrambe, warn una sola.
		var hasPrivacy = eeatLinkOrTextMatch(html, /privacy|informativa/i);
		var hasCookiePolicy = eeatLinkOrTextMatch(html, /cookie/i);
		var policyFlag = (hasPrivacy && hasCookiePolicy) ? 'good' : ((hasPrivacy || hasCookiePolicy) ? 'warn' : 'bad');

		// 5. Pagina «Chi siamo» — binario.
		var chisiamoFlag = eeatLinkOrTextMatch(html, /chi[-\s]siamo|about(?:-us)?|su-di-noi|azienda|team|storia/i) ? 'good' : 'bad';

		// 6. Portfolio / casi studio — binario.
		var portfolioFlag = eeatLinkOrTextMatch(html, /casi[-\s]studio|case[-\s]stud|portfolio|referenze|lavori|progetti|testimonial/i) ? 'good' : 'bad';

		// 7. Dati strutturati JSON-LD — good un @type d'identità, warn generico/malformato, bad assente.
		var schemaFlag;
		if (!jsonld.present) {
			schemaFlag = 'bad';
		} else if (jsonld.malformed) {
			schemaFlag = 'warn';
		} else if (jsonld.types.some(function (t) { return /organization|localbusiness|person/i.test(t); })) {
			schemaFlag = 'good';
		} else {
			schemaFlag = 'warn';
		}

		// 8. Profili esterni — good ≥2 profili o sameAs presente, warn 1 profilo.
		var socialDomains = eeatSocialDomains(html);
		var profiliFlag;
		if (jsonld.sameAs.length > 0 || socialDomains.length >= 2) {
			profiliFlag = 'good';
		} else if (socialDomains.length === 1) {
			profiliFlag = 'warn';
		} else {
			profiliFlag = 'bad';
		}

		return {
			flags: {
				https: httpsFlag, contatti: contattiFlag, legale: legaleFlag, policy: policyFlag,
				chisiamo: chisiamoFlag, portfolio: portfolioFlag, schema: schemaFlag, profili: profiliFlag
			},
			partial: eeatLooksThin(html)
		};
	}

	/** Wrapper di rete: un solo `toolFetch(url,'html')` + eeatComputeFlags sul body ricevuto. */
	function runEeatCheck(url) {
		var scheme = /^http:\/\//i.test(url) ? 'http' : 'https';
		return toolFetch(url, 'html').then(function (data) {
			return eeatComputeFlags(data.body || '', scheme);
		});
	}

	/** punteggio_segnale (§1.2): peso se good, round(peso/2) se warn, 0 se bad. */
	function eeatSignalScore(flag, weight) {
		if (flag === 'good') { return weight; }
		if (flag === 'warn') { return Math.round(weight / 2); }
		return 0;
	}

	/** Dai flag agli 8 segnali: punti per segnale, punteggio totale 0–100, percentuale per asse. */
	function eeatScoreFromFlags(flags) {
		var points = {}, total = 0;
		Object.keys(EEAT_WEIGHTS).forEach(function (key) {
			var p = eeatSignalScore(flags[key], EEAT_WEIGHTS[key]);
			points[key] = p;
			total += p;
		});
		var axes = {};
		Object.keys(EEAT_AXES).forEach(function (axis) {
			var sum = EEAT_AXES[axis].reduce(function (s, key) { return s + points[key]; }, 0);
			axes[axis] = Math.round(sum / EEAT_AXIS_MAX[axis] * 100);
		});
		return { total: total, points: points, axes: axes };
	}

	/** Flag CSS per asse (§1.3): ≥75 good, 50–74 warn, <50 bad. */
	function eeatAxisFlag(pct) {
		if (pct >= 75) { return 'good'; }
		if (pct >= 50) { return 'warn'; }
		return 'bad';
	}

	var EEAT_VERDICT_FALLBACK = {
		good: 'Ottimo: i segnali di fiducia E-E-A-T sono presenti e leggibili nel codice. Ricordate che parliamo di segnali on-page, non del vostro E-E-A-T reale.',
		buono: 'Buona base: la maggior parte dei segnali di fiducia c’è. Sistemate i pochi punti in giallo o rosso per completare il quadro.',
		mid: 'A metà strada: diversi segnali di fiducia mancano o non sono leggibili. La lista qui sotto indica da dove partire.',
		poor: 'Segnali deboli: la pagina espone pochi elementi di fiducia verificabili — che sono anche i più facili da aggiungere.'
	};

	/** Verdetto generale a 4 fasce (§1.3): 90/75/50. */
	function eeatVerdict(root, score) {
		if (score >= 90) { return txt(root, 'data-verdict-good', EEAT_VERDICT_FALLBACK.good); }
		if (score >= 75) { return txt(root, 'data-verdict-buono', EEAT_VERDICT_FALLBACK.buono); }
		if (score >= 50) { return txt(root, 'data-verdict-mid', EEAT_VERDICT_FALLBACK.mid); }
		return txt(root, 'data-verdict-poor', EEAT_VERDICT_FALLBACK.poor);
	}

	function initEeatTool(root) {
		var shell = toolShell(root);
		onUrlSubmit(shell, function (url) {
			return runEeatCheck(url).then(function (res) {
				var scored = eeatScoreFromFlags(res.flags);

				setText(root, '[data-sr-tool-url]', url.replace(/^https?:\/\//, ''));
				setText(root, '[data-sr-tool-score]', String(scored.total));
				animateFill(root, '[data-sr-tool-fill]', scored.total);
				setText(root, '[data-sr-tool-verdict]', eeatVerdict(root, scored.total));

				['esperienza', 'competenza', 'autorevolezza', 'affidabilita'].forEach(function (axis) {
					var sel = '[data-sr-tool-axis-' + axis + ']';
					setText(root, sel, scored.axes[axis] + '%');
					setFlag(root, sel, eeatAxisFlag(scored.axes[axis]));
				});

				var ndText = txt(root, 'data-label-nd', 'non rilevato (possibile rendering JavaScript)');
				Object.keys(EEAT_WEIGHTS).forEach(function (key) {
					var flag = res.flags[key];
					var label = txt(root, 'data-label-' + key + '-' + flag, EEAT_FALLBACK[key][flag]);
					if (res.partial && flag === 'bad') { label += ' (' + ndText + ')'; }
					setText(root, '[data-sr-tool-' + key + ']', label);
					setFlag(root, '[data-sr-tool-' + key + ']', flag);
				});

				var notice = q(root, '[data-sr-tool-notice]');
				if (notice) {
					notice.hidden = !res.partial;
					if (res.partial) {
						notice.textContent = txt(root, 'data-notice',
							'Il sito rende i contenuti via JavaScript: alcuni segnali potrebbero esistere ma non essere leggibili nell’HTML iniziale. Il punteggio è indicativo.');
					}
				}
			});
		});
	}

	/* ---------- Modulo: ROI localizzazione (calcolatore, nessuna rete) ---------- */
	function initRoiTool(root) {
		var form = root.matches && root.matches('[data-sr-tool-form]') ? root : (root.querySelector('[data-sr-tool-form]') || root);
		var result = root.querySelector('[data-sr-tool-result]');
		var currency = txt(root, 'data-roi-currency', '€');
		var locale = toolLocale(root);
		var numLocale = locale === 'en' ? 'en-US' : (locale === 'ru' ? 'ru-RU' : 'it-IT');

		function num(sel) {
			var el = form.querySelector(sel);
			var v = el ? parseFloat(String(el.value).replace(',', '.')) : 0;
			return isNaN(v) ? 0 : v;
		}
		function money(v) {
			return currency + ' ' + Math.round(v).toLocaleString(numLocale);
		}
		function recalc() {
			var visits = num('[data-sr-roi-visits]');
			var foreign = num('[data-sr-roi-foreign]') / 100;
			var conv = num('[data-sr-roi-conv]') / 100;
			var order = num('[data-sr-roi-order]');
			var boost = num('[data-sr-roi-boost]') / 100;
			var foreignVisitors = visits * foreign;
			var extraMonthly = foreignVisitors * conv * boost * order;
			setText(root, '[data-sr-roi-monthly]', money(extraMonthly));
			setText(root, '[data-sr-roi-annual]', money(extraMonthly * 12));
			if (result) result.hidden = false;
		}
		if (form) {
			form.addEventListener('submit', function (e) { e.preventDefault(); recalc(); });
			form.addEventListener('input', recalc);
			recalc();
		}
	}

	/* ============================================================================
	 * Modulo: check-up completo (orchestratore) — docs/copy-checkup.md §1/§2.3.
	 *
	 * Esegue in parallelo le misure delle altre 7 dimensioni (1 chiamata PSI
	 * copre prestazioni/SEO/accessibilità/best-practice + byte-weight per la
	 * CO₂; GDPR e AI via remarka_tool_fetch), applica il modello di scoring del
	 * copy deck (pesi 25/20/15/15/10/10/5, normalizzazione GDPR/AI/CO₂,
	 * soglie 90/75/50, degrado con rinormalizzazione, guardia di validità
	 * ≥4/7 e almeno Prestazioni|SEO) e disegna lo schermo dei risultati.
	 *
	 * CONTRATTO DATA-ATTRIBUTI (estensione al contratto generale sopra):
	 *   [data-sr-tool="checkup"]     wrapper (data-sr-locale come gli altri)
	 *   [data-sr-dim="perf|seo|a11y|gdpr|bp|ai|co2"]  una per le 7 card;
	 *     dentro ciascuna: .sr-eyebrow (etichetta, letta anche per le
	 *     priorità), [data-sr-tool-score], [data-sr-tool-fill],
	 *     [data-sr-dim-word] (verdetto, riceve data-sr-flag),
	 *     [data-sr-tool-verdict] (rilievo 1 riga), [data-sr-dim-extra]
	 *     (opzionale, solo AI: "N / 4 segnali").
	 *   data-verdict-0..3            sui singoli [data-sr-dim] — le 4 frasi di
	 *                                 rilievo (Eccellente/Buono/Da migliorare/
	 *                                 Critico), fallback IT in CHECKUP_FINDINGS.
	 *   data-word-0..3               sul wrapper — le 4 etichette di verdetto.
	 *   data-composite-0..3          sul wrapper — le 4 etichette del composito.
	 *   [data-sr-checkup-incomplete] banner «check-up incompleto» (guardia).
	 *   [data-sr-checkup-retry]      bottone «Riprova» dentro il banner.
	 *   [data-sr-checkup-composite] [data-sr-checkup-priorities-wrap]
	 *   [data-sr-checkup-form-wrap]  sezioni nascoste quando la guardia fallisce.
	 *   [data-sr-gauge] [data-sr-gauge-num] [data-sr-checkup-label]
	 *   [data-sr-checkup-url] [data-sr-checkup-calc] [data-sr-checkup-priorities]
	 *   [data-sr-checkup-report-form] [data-sr-checkup-consent]
	 *   [data-sr-checkup-consent-monthly] [data-sr-checkup-success] [data-sr-checkup-error]
	 *   input[name=sr_checkup_hp] (honeypot, .sr-hp-field — invisibile via CSS)
	 * ========================================================================== */

	var CHECKUP_WEIGHTS = { perf: 25, seo: 20, a11y: 15, gdpr: 15, bp: 10, ai: 10, co2: 5 };
	var CHECKUP_ORDER = ['perf', 'seo', 'a11y', 'gdpr', 'bp', 'ai', 'co2'];
	var CHECKUP_WORDS = ['Eccellente', 'Buono', 'Da migliorare', 'Critico'];
	var CHECKUP_COMPOSITE_LABELS = ['Sito in salute eccellente', 'Sito in buona salute', 'Sito da migliorare', 'Sito a rischio'];
	// Fallback IT verbatim da docs/copy-checkup.md §2.3 (usato solo se la pagina
	// non porta i data-verdict-0..3 sulla card — le pagine EN/RU di M4 li avranno propri).
	var CHECKUP_FINDINGS = {
		perf: ['Il sito è rapido su mobile: rispetta gli standard Google.',
			'Velocità buona; restano margini misurabili su qualche pagina.',
			'Nella media del web, ma lontano dagli standard consigliati.',
			'Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.'],
		seo: ['Basi tecniche on-page in ordine: nessun ostacolo all’indicizzazione.',
			'Struttura solida; poche correzioni per completare le basi.',
			'Alcuni elementi on-page mancano o sono duplicati.',
			'Qualcosa ostacola l’indicizzazione: da sistemare prima di tutto.'],
		a11y: ['Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA.',
			'Buon livello; restano barriere minori da rimuovere.',
			'Diverse barriere rilevate: contrasti, etichette, navigazione.',
			'Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).'],
		gdpr: ['Banner, informative e tracker in ordine nell’HTML iniziale.',
			'Impianto presente; un paio di punti da verificare a mano.',
			'Mancano elementi o alcuni tracker vanno governati meglio.',
			'Tracker attivi senza banner o policy assenti: rischio concreto col Garante.'],
		bp: ['Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate.',
			'Buon livello tecnico; qualche avviso da chiudere.',
			'Diversi avvisi tecnici: sicurezza, errori console, immagini.',
			'Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.'],
		ai: ['4 segnali su 4: il sito è leggibile e citabile dai modelli AI.',
			'3 segnali su 4: manca poco alla piena prontezza AI.',
			'2 segnali su 4: dati strutturati o sitemap da completare.',
			'0–1 segnali: i modelli AI faticano a leggere e citare il sito.'],
		co2: ['Pagina leggera: emissioni sotto la media del web.',
			'Vicino alla media; c’è margine per alleggerire.',
			'Sopra la media: la pagina è pesante da caricare.',
			'Molto sopra la media: pagina pesante, costo ambientale e di velocità.']
	};
	var CHECKUP_NA_TEXT = 'Non siamo riusciti a misurare questo aspetto: il sito ha rifiutato la lettura o il servizio Google era saturo.';
	var CHECKUP_GAUGE_COLORS = { good: '#1a8f4a', warn: '#c98a00', bad: '#cc3333', na: '#DDDBD4' };

	/** Percorsi per lingua degli strumenti dedicati (inc/lang-map.php),
	 *  per il link "Approfondisci →" di ogni card check-up. 'bp' non ha uno
	 *  strumento dedicato (generate_pages.py::_checkup_dim_card la esclude). */
	var CHECKUP_DIM_TOOL_PATH = {
		perf: { it: '/strumenti/test-velocita/', en: '/en/tools/speed-test/', ru: '/ru/instrumenty/test-skorosti/' },
		seo: { it: '/strumenti/analisi-seo/', en: '/en/tools/seo-audit/', ru: '/ru/instrumenty/seo-audit/' },
		a11y: { it: '/strumenti/verifica-accessibilita/', en: '/en/tools/accessibility-check/', ru: '/ru/instrumenty/proverka-dostupnosti/' },
		gdpr: { it: '/strumenti/check-gdpr/', en: '/en/tools/gdpr-check/', ru: '/ru/instrumenty/proverka-gdpr/' },
		ai: { it: '/strumenti/sito-pronto-ai/', en: '/en/tools/ai-readiness/', ru: '/ru/instrumenty/gotovnost-k-ii/' },
		co2: { it: '/strumenti/impatto-co2/', en: '/en/tools/website-carbon/', ru: '/ru/instrumenty/uglerodnyj-sled/' }
	};

	/** Href del link "Approfondisci →" di una card: percorso dello strumento
	 *  dedicato (per lingua) + `?url=…&autostart=1`, sullo stesso schema del
	 *  redirect del blocco home (CHECKUP_PAGE_PATH più sotto). null se la
	 *  dimensione non ha uno strumento dedicato (bp). */
	function checkupDimMoreHref(dim, locale, url) {
		var byLocale = CHECKUP_DIM_TOOL_PATH[dim];
		if (!byLocale) return null;
		var path = byLocale[locale] || byLocale.it;
		return path + '?url=' + encodeURIComponent(url) + '&autostart=1';
	}

	function checkupLevel(score) {
		if (score >= 90) return 0;
		if (score >= 75) return 1;
		if (score >= 50) return 2;
		return 3;
	}
	function checkupFlagForLevel(level) {
		return level <= 1 ? 'good' : (level === 2 ? 'warn' : 'bad');
	}

	/** GDPR: punti 0/0,5/1 per flag, pesati come da docs/copy-checkup.md §1.2. */
	function gdprScoreFromFlags(flags) {
		function f(flag) { return flag === 'good' ? 1 : (flag === 'warn' ? 0.5 : 0); }
		return Math.round(35 * f(flags.cmpFlag) + 30 * f(flags.trackFlag) + 20 * f(flags.policyFlag) + 15 * f(flags.externalFlag));
	}

	/** AI: somma dei pesi dei segnali positivi (JSON-LD 30 · sitemap 25 · robots 25 · llms 20). */
	function aiScoreFromSignals(sig) {
		var s = 0;
		if (sig.jsonld) s += 30;
		if (sig.sitemap) s += 25;
		if (sig.robots !== 'blocked') s += 25;
		if (sig.llms) s += 20;
		return s;
	}

	/** CO₂: rampa lineare 0,4g→100 · 0,8g→67 · 1,6g→0 (clamp 0–100). */
	function co2ScoreFromGrams(g) {
		return Math.max(0, Math.min(100, Math.round(100 * (1.6 - g) / 1.2)));
	}

	/** Composito pesato sulle sole dimensioni disponibili + guardia di validità (§1.5). */
	function checkupComposite(scores) {
		var sumW = 0, sumWS = 0, n = 0, hasPerfOrSeo = false;
		CHECKUP_ORDER.forEach(function (k) {
			var s = scores[k];
			if (s === null || s === undefined) return;
			sumW += CHECKUP_WEIGHTS[k];
			sumWS += CHECKUP_WEIGHTS[k] * s;
			n++;
			if (k === 'perf' || k === 'seo') hasPerfOrSeo = true;
		});
		var valid = n >= 4 && hasPerfOrSeo;
		return { composite: (valid && sumW > 0) ? Math.round(sumWS / sumW) : null, measured: n, valid: valid };
	}

	/**
	 * Rilievi individuali per il report PDF (M5, docs/piano-checkup-sito.md).
	 * Etichette brevi nelle 3 lingue per le 3 dimensioni "nostre" (gdpr/ai/co2):
	 * i 4 audit Google arrivano già localizzati da PSI (parametro `locale` in
	 * psiFetch). Nessun testo lungo qui: sono titoli di gruppo, il copy deck
	 * del PDF (checkup-report-pdf.php) resta la fonte del tono/contenuto.
	 */
	var CHECKUP_FINDING_LABELS = {
		it: {
			gdprTrackers: 'Domini di terze parti che caricano script',
			aiFiles: 'File assenti agli indirizzi attesi',
			aiFileMissing: 'File assente',
			aiJsonldFound: 'Dati strutturati JSON-LD rilevati',
			aiJsonldMissing: 'Nessun dato strutturato JSON-LD nella pagina',
			co2Weight: 'Peso totale della pagina',
			co2Heavy: 'Risorse più pesanti'
		},
		en: {
			gdprTrackers: 'Third-party domains loading scripts',
			aiFiles: 'Files missing at the expected address',
			aiFileMissing: 'File missing',
			aiJsonldFound: 'Structured data (JSON-LD) found',
			aiJsonldMissing: 'No structured data (JSON-LD) on the page',
			co2Weight: 'Total page weight',
			co2Heavy: 'Heaviest resources'
		},
		ru: {
			gdprTrackers: 'Домены третьих лиц, загружающие скрипты',
			aiFiles: 'Файлы отсутствуют по ожидаемому адресу',
			aiFileMissing: 'Файл отсутствует',
			aiJsonldFound: 'Обнаружены структурированные данные (JSON-LD)',
			aiJsonldMissing: 'На странице нет структурированных данных (JSON-LD)',
			co2Weight: 'Общий вес страницы',
			co2Heavy: 'Самые тяжёлые ресурсы'
		}
	};

	function checkupFindingLabels(locale) {
		return CHECKUP_FINDING_LABELS[locale] || CHECKUP_FINDING_LABELS.it;
	}

	/** PSI (perf/seo/a11y/bp): fino a 4 audit peggiori, già ordinati, con le loro risorse. */
	function auditsToFindings(list) {
		return (list || []).slice(0, 4).map(function (a) {
			return { t: String(a.title || '').slice(0, 200), items: (a.items || []).slice(0, 3) };
		});
	}

	function checkupOrigin(url) {
		try { return new URL(url).origin; } catch (e) { return url.replace(/\/$/, ''); }
	}

	function buildGdprFindings(sig, locale) {
		var lbl = checkupFindingLabels(locale);
		var groups = [];
		var domains = (sig && sig.domains) || [];
		if (domains.length) {
			groups.push({
				t: lbl.gdprTrackers,
				items: domains.slice(0, 3).map(function (d) { return { u: 'https://' + String(d).slice(0, 290), v: '' }; })
			});
		}
		return groups;
	}

	function buildAiFindings(sig, url, locale) {
		var lbl = checkupFindingLabels(locale);
		var origin = checkupOrigin(url);
		var groups = [];
		var missing = [];
		if (sig) {
			if (!sig.llms) missing.push({ u: origin + '/llms.txt', v: lbl.aiFileMissing });
			if (sig.robots === 'blocked') missing.push({ u: origin + '/robots.txt', v: lbl.aiFileMissing });
			if (!sig.sitemap) missing.push({ u: origin + '/sitemap.xml', v: lbl.aiFileMissing });
		}
		if (missing.length) {
			groups.push({ t: lbl.aiFiles, items: missing.slice(0, 3) });
		}
		if (sig) {
			groups.push({ t: sig.jsonld ? lbl.aiJsonldFound : lbl.aiJsonldMissing, items: [] });
		}
		return groups.slice(0, 4);
	}

	function formatBytesShort(bytes) {
		if (bytes >= 1024 * 1024) return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
		return Math.round(bytes / 1024) + ' KB';
	}

	function buildCo2Findings(m, url, locale) {
		var lbl = checkupFindingLabels(locale);
		var groups = [];
		if (!m || m.byteWeight === null || m.byteWeight === undefined) {
			return groups;
		}
		groups.push({ t: lbl.co2Weight, items: [{ u: url, v: formatBytesShort(m.byteWeight) }] });
		if (m.byteWeightItems && m.byteWeightItems.length) {
			groups.push({ t: lbl.co2Heavy, items: m.byteWeightItems.slice(0, 3) });
		}
		return groups;
	}

	/** Ricapa i findings se, nonostante i limiti per-audit/per-item, il totale resta troppo grande. */
	function capFindingsSize(findings, maxBytes) {
		function size(f) { return JSON.stringify(f).length; }
		if (size(findings) <= maxBytes) return findings;
		Object.keys(findings).forEach(function (k) {
			findings[k].forEach(function (group) { group.items = group.items.slice(0, 1); });
		});
		if (size(findings) <= maxBytes) return findings;
		Object.keys(findings).forEach(function (k) { findings[k] = findings[k].slice(0, 2); });
		if (size(findings) <= maxBytes) return findings;
		return {};
	}

	/** Assembla i rilievi individuali delle 7 dimensioni (M5) — tollerante ai fallimenti parziali come lo scoring. */
	function buildCheckupFindings(url, locale, m, gdprSig, aiSig) {
		var findings = {
			perf: m ? auditsToFindings(m.audits.perf) : [],
			seo: m ? auditsToFindings(m.audits.seo) : [],
			a11y: m ? auditsToFindings(m.audits.a11y) : [],
			bp: m ? auditsToFindings(m.audits.bp) : [],
			gdpr: buildGdprFindings(gdprSig, locale),
			ai: buildAiFindings(aiSig, url, locale),
			co2: buildCo2Findings(m, url, locale)
		};
		return capFindingsSize(findings, 40000);
	}

	/** Orchestratore: 1 psiFetch (4 categorie + byte-weight) + GDPR + AI, in parallelo, tollerante ai fallimenti parziali. */
	/*
	 * PSI con 4 categorie su siti pesanti fallisce spesso lato Google (timeout
	 * interno Lighthouse). Strategia: 2 tentativi completi, poi fallback alla
	 * sola categoria PERFORMANCE (meglio perf+CO2 misurati che 5 N/D).
	 */
	function psiFetchResilient(url, locale) {
		function delay(ms) {
			return new Promise(function (resolve) { window.setTimeout(resolve, ms); });
		}
		return psiFetch(url, locale).catch(function () {
			return delay(1500).then(function () { return psiFetch(url, locale); });
		}).catch(function () {
			return delay(1500).then(function () { return psiFetch(url, locale, ['PERFORMANCE']); });
		}).catch(function () { return null; });
	}

	function runCheckup(url, locale) {
		var jobs = [
			psiFetchResilient(url, locale),
			runGdprCheck(url).catch(function () { return null; }),
			runAiCheck(url).catch(function () { return null; })
		];
		return Promise.all(jobs).then(function (res) {
			var m = res[0], gdprSig = res[1], aiSig = res[2];
			var scores = { perf: null, seo: null, a11y: null, bp: null, gdpr: null, ai: null, co2: null };
			var extra = {};
			if (m) {
				scores.perf = m.scores.perf;
				scores.seo = m.scores.seo;
				scores.a11y = m.scores.a11y;
				scores.bp = m.scores.bp;
				if (m.byteWeight !== null) {
					extra.co2Grams = co2PerVisitGrams(m.byteWeight);
					scores.co2 = co2ScoreFromGrams(extra.co2Grams);
				}
			}
			if (gdprSig) {
				extra.gdprFlags = gdprSignalFlags(gdprSig);
				scores.gdpr = gdprScoreFromFlags(extra.gdprFlags);
			}
			if (aiSig) {
				extra.aiCount = (aiSig.llms ? 1 : 0) + (aiSig.robots !== 'blocked' ? 1 : 0) + (aiSig.jsonld ? 1 : 0) + (aiSig.sitemap ? 1 : 0);
				scores.ai = aiScoreFromSignals(aiSig);
			}
			var comp = checkupComposite(scores);
			var findings = buildCheckupFindings(url, locale, m, gdprSig, aiSig);
			return { url: url, scores: scores, extra: extra, composite: comp.composite, measured: comp.measured, valid: comp.valid, findings: findings };
		});
	}

	function renderCheckupPriorities(root, dims) {
		var container = q(root, '[data-sr-checkup-priorities]');
		if (!container) return;
		container.innerHTML = '';
		var candidates = dims.filter(function (d) { return d.score !== null; });
		candidates.sort(function (a, b) { return (b.weight * (100 - b.score)) - (a.weight * (100 - a.score)); });
		candidates.slice(0, 3).forEach(function (d, i) {
			var row = document.createElement('div');
			row.className = 'sr-priorities__row';
			var idxEl = document.createElement('span');
			idxEl.className = 'sr-mono sr-priorities__idx';
			idxEl.textContent = '0' + (i + 1);
			var body = document.createElement('div');
			var title = document.createElement('p');
			title.className = 'sr-priorities__title';
			title.setAttribute('data-sr-flag', d.flag);
			title.textContent = d.label + ' · ' + d.word;
			var desc = document.createElement('p');
			desc.className = 'sr-priorities__desc';
			desc.textContent = d.finding;
			body.appendChild(title);
			body.appendChild(desc);
			row.appendChild(idxEl);
			row.appendChild(body);
			container.appendChild(row);
		});
	}

	function renderCheckupResults(root, result) {
		var dims = [];
		var locale = toolLocale(root);
		root.querySelectorAll('[data-sr-dim]').forEach(function (card) {
			var key = card.getAttribute('data-sr-dim');
			var score = result.scores[key];
			var eyebrowEl = card.querySelector('.sr-eyebrow');
			var label = eyebrowEl ? eyebrowEl.textContent : key;
			var scoreEl = card.querySelector('[data-sr-tool-score]');
			var fillEl = card.querySelector('[data-sr-tool-fill]');
			var wordEl = card.querySelector('[data-sr-dim-word]');
			var findingEl = card.querySelector('[data-sr-tool-verdict]');
			var extraEl = card.querySelector('[data-sr-dim-extra]');

			/* Link "Approfondisci →" verso lo strumento dedicato: mostrato anche
			   quando la misura è N/D, perché la pagina dello strumento rifà la
			   misurazione da sola (può riuscire dove la chiamata combinata del
			   check-up ha fallito). Assente su 'bp' (nessuno strumento dedicato). */
			var moreEl = card.querySelector('[data-sr-dim-more]');
			if (moreEl) {
				var moreHref = checkupDimMoreHref(key, locale, result.url);
				if (moreHref) {
					moreEl.href = moreHref;
					moreEl.textContent = txt(root, 'data-more-label', 'Approfondisci →');
					moreEl.hidden = false;
				}
			}

			if (score === null || score === undefined) {
				if (scoreEl) scoreEl.textContent = '—';
				if (fillEl) fillEl.style.width = '0%';
				if (wordEl) { wordEl.textContent = 'N/D'; wordEl.removeAttribute('data-sr-flag'); }
				if (findingEl) findingEl.textContent = txt(root, 'data-na-text', CHECKUP_NA_TEXT);
				if (extraEl) extraEl.textContent = '';
				dims.push({ key: key, label: label, score: null, weight: CHECKUP_WEIGHTS[key] });
				return;
			}

			var level = checkupLevel(score);
			var flag = checkupFlagForLevel(level);
			var word = txt(root, 'data-word-' + level, CHECKUP_WORDS[level]);
			/* I testi-verdetto della card AI parlano di "N segnali su 4": vanno
			   scelti dal conteggio reale, non dalla fascia del punteggio pesato
			   (2 segnali "leggeri" = 45 punti, ma il testo deve dire 2, non 0-1). */
			var textLevel = level;
			if (key === 'ai' && result.extra && typeof result.extra.aiCount === 'number') {
				var n = result.extra.aiCount;
				textLevel = n >= 4 ? 0 : n === 3 ? 1 : n === 2 ? 2 : 3;
			}
			var finding = txt(card, 'data-verdict-' + textLevel, CHECKUP_FINDINGS[key][textLevel]);

			if (scoreEl) scoreEl.textContent = String(score);
			if (fillEl) animateFill(card, '[data-sr-tool-fill]', score);
			if (wordEl) { wordEl.textContent = word; wordEl.setAttribute('data-sr-flag', flag); }
			if (findingEl) findingEl.textContent = finding;
			if (extraEl) {
				if (key === 'ai') {
					extraEl.textContent = (result.extra.aiCount || 0) + txt(root, 'data-ai-suffix', ' / 4 segnali');
				} else {
					extraEl.textContent = '';
				}
			}
			dims.push({ key: key, label: label, score: score, weight: CHECKUP_WEIGHTS[key], flag: flag, word: word, finding: finding });
		});

		renderCheckupPriorities(root, dims);

		var incompleteEl = q(root, '[data-sr-checkup-incomplete]');
		var compositeEl = q(root, '[data-sr-checkup-composite]');
		var prioritiesWrap = q(root, '[data-sr-checkup-priorities-wrap]');
		var formWrap = q(root, '[data-sr-checkup-form-wrap]');

		if (!result.valid) {
			if (incompleteEl) incompleteEl.hidden = false;
			if (compositeEl) compositeEl.hidden = true;
			if (prioritiesWrap) prioritiesWrap.hidden = true;
			if (formWrap) formWrap.hidden = true;
			return;
		}

		if (incompleteEl) incompleteEl.hidden = true;
		if (compositeEl) compositeEl.hidden = false;
		if (prioritiesWrap) prioritiesWrap.hidden = false;
		if (formWrap) formWrap.hidden = false;

		var compLevel = checkupLevel(result.composite);
		var compFlag = checkupFlagForLevel(compLevel);
		var gaugeNum = q(root, '[data-sr-gauge-num]');
		if (gaugeNum) gaugeNum.textContent = String(result.composite);
		var gauge = q(root, '[data-sr-gauge]');
		if (gauge) {
			var color = CHECKUP_GAUGE_COLORS[compFlag] || CHECKUP_GAUGE_COLORS.na;
			gauge.style.background = 'conic-gradient(' + color + ' 0 ' + result.composite + '%, var(--sr-traccia) ' + result.composite + '% 100%)';
		}
		var labelEl = q(root, '[data-sr-checkup-label]');
		if (labelEl) labelEl.textContent = txt(root, 'data-composite-' + compLevel, CHECKUP_COMPOSITE_LABELS[compLevel]);

		var urlEl = q(root, '[data-sr-checkup-url]');
		if (urlEl) {
			var domain = result.url.replace(/^https?:\/\//, '').replace(/\/$/, '');
			var now = new Date();
			var day = String(now.getDate()).padStart(2, '0'), month = String(now.getMonth() + 1).padStart(2, '0');
			urlEl.textContent = domain + txt(root, 'data-label-suffix', ' — analisi mobile') + ' · ' + day + '.' + month + '.' + now.getFullYear();
		}

		var calcEl = q(root, '[data-sr-checkup-calc]');
		if (calcEl) {
			var tmpl = txt(root, 'data-calc-note', 'Calcolato su {n} misurazioni su 7.');
			calcEl.textContent = tmpl.replace('{n}', String(result.measured));
		}
	}

	/** Form richiesta report PDF: valida lato client, assembla il payload JSON e
	 * lo invia all'azione AJAX `remarka_tool_report` (handler server-side in
	 * functions.php: nonce + honeypot + rate-limit + dompdf + wp_mail + CPT
	 * sr_lead, M3). */
	function initCheckupReportForm(root, getLastResult) {
		var form = q(root, '[data-sr-checkup-report-form]');
		if (!form) return;
		var successEl = q(root, '[data-sr-checkup-success]');
		var errorEl = q(root, '[data-sr-checkup-error]');

		form.addEventListener('submit', function (e) {
			e.preventDefault();
			if (successEl) successEl.hidden = true;
			if (errorEl) errorEl.hidden = true;

			var result = getLastResult();
			var emailInput = form.querySelector('input[type="email"]');
			var consentInput = q(root, '[data-sr-checkup-consent]');
			if (!result || !emailInput || !emailInput.checkValidity() || !consentInput || !consentInput.checked) {
				if (emailInput && emailInput.reportValidity) emailInput.reportValidity();
				return;
			}

			var monthlyInput = q(root, '[data-sr-checkup-consent-monthly]');
			var payload = {
				url: result.url,
				locale: toolLocale(root),
				composite: result.composite,
				measured: result.measured,
				scores: result.scores,
				findings: result.findings || {},
				ts: new Date().toISOString()
			};

			var cfg = window.remarkaPSI || {};
			if (!cfg.ajaxUrl || !window.fetch) {
				if (errorEl) errorEl.hidden = false;
				return;
			}
			var btn = form.querySelector('button[type="submit"]');
			if (btn) btn.disabled = true;

			var hpInput = form.querySelector('[name="sr_checkup_hp"]');
			var data = new FormData();
			data.set('action', 'remarka_tool_report');
			data.set('nonce', cfg.toolsNonce || '');
			data.set('email', emailInput.value);
			data.set('consent', '1');
			data.set('consent_monthly', monthlyInput && monthlyInput.checked ? '1' : '0');
			data.set('sr_checkup_hp', hpInput ? hpInput.value : '');
			data.set('payload', JSON.stringify(payload).slice(0, 65536));

			window.fetch(cfg.ajaxUrl, { method: 'POST', body: data, credentials: 'same-origin' })
				.then(function (r) { return r.json(); })
				.then(function (json) {
					if (json && json.success) {
						form.hidden = true;
						if (successEl) successEl.hidden = false;
					} else if (errorEl) {
						errorEl.hidden = false;
					}
				})
				.catch(function () { if (errorEl) errorEl.hidden = false; })
				.finally(function () { if (btn) btn.disabled = false; });
		});
	}

	function initCheckupTool(root) {
		var shell = toolShell(root);
		var lastResult = null;

		function run(url) {
			return runCheckup(url, toolLocale(root)).then(function (result) {
				lastResult = result;
				renderCheckupResults(root, result);
			});
		}

		onUrlSubmit(shell, run);
		initCheckupReportForm(root, function () { return lastResult; });

		var retryBtn = q(root, '[data-sr-checkup-retry]');
		if (retryBtn) {
			retryBtn.addEventListener('click', function () {
				var input = shell.form.querySelector('input[type="text"]');
				var url = normalizeUrl(input && input.value);
				if (!url) return;
				if (shell.pending) shell.pending.hidden = false;
				run(url).finally(function () { if (shell.pending) shell.pending.hidden = true; });
			});
		}
	}

	/** POST server-side fetch (endpoint remarka_tool_fetch) → {ok,status,body}. */
	function toolFetch(url, mode) {
		var cfg = window.remarkaPSI || {};
		if (!cfg.ajaxUrl || !window.fetch) {
			return Promise.reject(new Error('toolFetch non disponibile'));
		}
		var data = new FormData();
		data.set('action', 'remarka_tool_fetch');
		data.set('nonce', cfg.toolsNonce || '');
		data.set('url', url);
		data.set('mode', mode || 'html');
		return window.fetch(cfg.ajaxUrl, { method: 'POST', body: data, credentials: 'same-origin' })
			.then(function (r) { return r.json(); })
			.then(function (json) {
				if (json && json.success && json.data) { return json.data; }
				throw new Error((json && json.data && json.data.message) || 'fetch_failed');
			});
	}

	/* ==========================================================================
	 * Remarka Lab — 3 strumenti AI (Anthropic Messages API), docs/piano-ai-tools.md §6.
	 *
	 * Endpoint comune `remarka_tool_ai` (POST, admin-ajax.php), risposta sempre
	 * { ok, code, data } incapsulata nella busta WP { success, data:{...} }.
	 * Stati: idle → loading ([data-sr-tool-pending]) → result/error
	 * ([data-sr-tool-result], errore scritto in [data-sr-tool-verdict]).
	 *
	 * CONTRATTO DATA-ATTRIBUTI (oltre a quello generale sopra):
	 *   data-sr-tool="ai-read|ai-suona|ai-llms"    data-sr-locale come gli altri.
	 *   data-ai-loading       testo "in corso" (specifico per strumento).
	 *   data-ai-maintenance   strumento in manutenzione (code=maintenance).
	 *   data-ai-limit         limite raggiunto (code=rate_limit|daily_cap).
	 *   data-ai-err           errore generico (fallback per ogni altro code).
	 *
	 * ai-read: [data-ai-verdetto] [data-ai-citabilita] [data-ai-citabilita-fill]
	 *   [data-ai-azioni] (contenitore, 3 righe renderizzate da JS con
	 *   [data-ai-azione-tpl] <template> dentro: .ai-azione-fai/.ai-azione-effetto)
	 *   [data-ai-lead-form] [data-ai-lead-email] [data-ai-lead-consent]
	 *   [data-ai-lead-success] [data-ai-lead-error] [name=sr_ai_hp] honeypot.
	 *
	 * ai-suona: input[name=text_lang] radio ×2 (data-lang-name-it/en/ru per le
	 *   etichette, nella lingua della pagina) + textarea[data-ai-suona-text] +
	 *   [data-ai-counter]. Risultato: [data-ai-badge] (data-sr-flag good/bad),
	 *   [data-ai-punteggio] [data-ai-punteggio-fill] [data-ai-registro]
	 *   [data-ai-verdetto] [data-ai-correzioni] con <template data-ai-correzione-tpl>.
	 *
	 * ai-llms: due modalità via input[name=ai_llms_mode] radio (form|url),
	 *   [data-ai-llms-form] [data-ai-llms-url] (i due blocchi campi, toggle
	 *   hidden). Risultato: textarea[readonly][data-ai-llms-output]
	 *   [data-ai-llms-note] [data-ai-copy] [data-ai-download].
	 * ========================================================================== */

	function aiErrorMessage(root, code) {
		if ('maintenance' === code) return txt(root, 'data-ai-maintenance', 'Strumento in manutenzione.');
		if ('rate_limit' === code || 'daily_cap' === code) return txt(root, 'data-ai-limit', 'Avete raggiunto il limite di prove per oggi. Riprovate domani.');
		return txt(root, 'data-ai-err', 'Lo strumento non è disponibile in questo momento. Riprovate tra poco.');
	}

	/** POST generico verso un'azione admin-ajax (nonce 'remarka_tools' incluso). */
	function aiPost(action, payload) {
		var cfg = window.remarkaPSI || {};
		if (!cfg.ajaxUrl || !window.fetch) {
			return Promise.reject(new Error('strumento non disponibile'));
		}
		var data = new FormData();
		data.set('action', action);
		data.set('nonce', cfg.toolsNonce || '');
		Object.keys(payload).forEach(function (k) {
			data.set(k, payload[k] === null || payload[k] === undefined ? '' : String(payload[k]));
		});
		return window.fetch(cfg.ajaxUrl, { method: 'POST', body: data, credentials: 'same-origin' })
			.then(function (r) { return r.json(); });
	}

	/**
	 * Aggancia il submit del form: guardia "running", pending/result, dispatch
	 * su onResult(data) se ok, altrimenti scrive il messaggio d'errore in
	 * [data-sr-tool-verdict]. `buildPayload()` può restare null e occuparsi da
	 * sé della UI (es. validazione locale) per abortire senza chiamata di rete.
	 */
	function aiSubmit(root, form, buildPayload, onResult) {
		var running = false;
		var pending = root.querySelector('[data-sr-tool-pending]');
		var result = root.querySelector('[data-sr-tool-result]');
		form.addEventListener('submit', function (e) {
			e.preventDefault();
			if (running) return;
			var payload = buildPayload();
			if (!payload) return;
			running = true;
			if (pending) pending.hidden = false;
			if (result) result.hidden = true;
			aiPost('remarka_tool_ai', payload)
				.then(function (json) {
					var envelope = json && json.data;
					var code = envelope && envelope.code;
					if (json && json.success && envelope && envelope.ok && envelope.data) {
						onResult(envelope.data);
					} else {
						setText(root, '[data-sr-tool-verdict]', aiErrorMessage(root, code));
					}
					if (result) result.hidden = false;
				})
				.catch(function () {
					setText(root, '[data-sr-tool-verdict]', aiErrorMessage(root, null));
					if (result) result.hidden = false;
				})
				.finally(function () {
					if (pending) pending.hidden = true;
					running = false;
				});
		});
	}

	/* ---------- ai-read: «Il vostro sito, letto dall'AI» ---------- */

	function renderAiAzioni(root, azioni) {
		var wrap = q(root, '[data-ai-azioni]');
		if (!wrap) return;
		var tpl = wrap.querySelector('template');
		wrap.querySelectorAll('.ai-azione').forEach(function (n) { n.remove(); });
		(azioni || []).forEach(function (a) {
			var node;
			if (tpl && tpl.content) {
				node = tpl.content.firstElementChild.cloneNode(true);
				var fai = node.querySelector('.ai-azione-fai');
				var eff = node.querySelector('.ai-azione-effetto');
				if (fai) fai.textContent = a.fai;
				if (eff) eff.textContent = a.effetto;
			} else {
				node = document.createElement('div');
				node.className = 'ai-azione sr-card';
				node.textContent = a.fai + ' → ' + a.effetto;
			}
			node.classList.add('ai-azione');
			wrap.appendChild(node);
		});
	}

	function initAiReadTool(root) {
		var form = q(root, '[data-sr-tool-form]');
		if (!form) return;
		var lastResult = null;
		var lastUrl = null;

		aiSubmit(root, form, function () {
			var input = form.querySelector('input[type="text"], input[type="url"]');
			var url = normalizeUrl(input && input.value);
			if (!url) {
				if (input) input.focus();
				return null;
			}
			lastUrl = url;
			return { tool: 'read-site', url: url, locale: toolLocale(root) };
		}, function (data) {
			lastResult = data;
			setText(root, '[data-sr-tool-verdict]', data.verdetto);
			setText(root, '[data-ai-citabilita]', String(data.citabilita));
			animateFill(root, '[data-ai-citabilita-fill]', data.citabilita);
			renderAiAzioni(root, data.azioni);
		});

		var leadForm = q(root, '[data-ai-lead-form]');
		if (!leadForm) return;
		leadForm.addEventListener('submit', function (e) {
			e.preventDefault();
			var successEl = q(root, '[data-ai-lead-success]');
			var errorEl = q(root, '[data-ai-lead-error]');
			if (successEl) successEl.hidden = true;
			if (errorEl) errorEl.hidden = true;

			var emailInput = leadForm.querySelector('input[type="email"]');
			var consentInput = q(root, '[data-ai-lead-consent]');
			if (!lastResult || !lastUrl || !emailInput || !emailInput.checkValidity() || !consentInput || !consentInput.checked) {
				if (emailInput && emailInput.reportValidity) emailInput.reportValidity();
				return;
			}
			var btn = leadForm.querySelector('button[type="submit"]');
			if (btn) btn.disabled = true;
			var hpInput = leadForm.querySelector('[name="sr_ai_hp"]');

			aiPost('remarka_tool_ai_lead', {
				url: lastUrl,
				email: emailInput.value,
				consent: '1',
				locale: toolLocale(root),
				sr_ai_hp: hpInput ? hpInput.value : ''
			}).then(function (json) {
				if (json && json.success) {
					leadForm.hidden = true;
					if (successEl) successEl.hidden = false;
				} else if (errorEl) {
					errorEl.hidden = false;
				}
			}).catch(function () {
				if (errorEl) errorEl.hidden = false;
			}).finally(function () {
				if (btn) btn.disabled = false;
			});
		});
	}

	/* ---------- ai-suona: «Suona madrelingua?» (verifica lingue estere) ---------- */

	/** Le due lingue "altre" rispetto a quella della pagina, in ordine fisso
	 *  it→en→ru: la prima è il default (docs/piano-ai-tools.md, correzione
	 *  proprietario 16.07). Il selettore mostra i nomi nella lingua della pagina. */
	function aiSuonaOtherLangs(locale) {
		return ['it', 'en', 'ru'].filter(function (c) { return c !== locale; });
	}

	function initAiSuonaTool(root) {
		var form = q(root, '[data-sr-tool-form]');
		if (!form) return;
		var textarea = form.querySelector('textarea[data-ai-suona-text]');
		var counter = q(root, '[data-ai-counter]');
		var LIMIT = 2000;

		function updateCounter() {
			if (counter && textarea) counter.textContent = String(textarea.value.length) + ' / ' + LIMIT;
		}
		if (textarea) {
			textarea.addEventListener('input', updateCounter);
			updateCounter();
		}

		// Selettore lingua: due radio già presenti nel markup (per-pagina) —
		// impostiamo solo il default (primo) se nessuno è checked.
		var langInputs = form.querySelectorAll('input[name="text_lang"]');
		if (langInputs.length && !form.querySelector('input[name="text_lang"]:checked')) {
			langInputs[0].checked = true;
		}

		aiSubmit(root, form, function () {
			var text = (textarea && textarea.value || '').trim();
			if (!text) {
				setText(root, '[data-sr-tool-verdict]', txt(root, 'data-ai-err-short', 'Incollate almeno una frase.'));
				var result = q(root, '[data-sr-tool-result]');
				if (result) result.hidden = false;
				return null;
			}
			var checked = form.querySelector('input[name="text_lang"]:checked');
			return {
				tool: 'suona',
				text: text.slice(0, LIMIT),
				text_lang: checked ? checked.value : aiSuonaOtherLangs(toolLocale(root))[0],
				locale: toolLocale(root)
			};
		}, function (data) {
			var badge = q(root, '[data-ai-badge]');
			if (badge) {
				badge.textContent = data.suona
					? txt(root, 'data-ai-badge-yes', 'Suona nativo')
					: txt(root, 'data-ai-badge-no', 'Si sente la traduzione');
				badge.setAttribute('data-sr-flag', data.suona ? 'good' : 'bad');
			}
			setText(root, '[data-ai-punteggio]', String(data.punteggio));
			animateFill(root, '[data-ai-punteggio-fill]', data.punteggio);
			setText(root, '[data-ai-registro]', data.registro);
			setText(root, '[data-sr-tool-verdict]', data.verdetto);

			var wrap = q(root, '[data-ai-correzioni]');
			if (wrap) {
				var tpl = wrap.querySelector('template');
				wrap.querySelectorAll('.ai-correzione').forEach(function (n) { n.remove(); });
				(data.correzioni || []).forEach(function (c) {
					var node;
					if (tpl && tpl.content) {
						node = tpl.content.firstElementChild.cloneNode(true);
						var prima = node.querySelector('.ai-correzione-prima');
						var dopo = node.querySelector('.ai-correzione-dopo');
						var perche = node.querySelector('.ai-correzione-perche');
						if (prima) prima.textContent = c.prima;
						if (dopo) dopo.textContent = c.dopo;
						if (perche) perche.textContent = c.perche;
					} else {
						node = document.createElement('div');
						node.className = 'ai-correzione sr-card';
						node.textContent = c.prima + ' → ' + c.dopo + ' (' + c.perche + ')';
					}
					node.classList.add('ai-correzione');
					wrap.appendChild(node);
				});
			}
		});
	}

	/* ---------- ai-llms: «Generatore llms.txt» ---------- */

	function initAiLlmsTool(root) {
		var form = q(root, '[data-sr-tool-form]');
		if (!form) return;
		var formBlock = q(root, '[data-ai-llms-form]');
		var urlBlock = q(root, '[data-ai-llms-url]');
		var modeInputs = form.querySelectorAll('input[name="ai_llms_mode"]');

		function syncMode() {
			var checked = form.querySelector('input[name="ai_llms_mode"]:checked');
			var mode = checked ? checked.value : 'form';
			if (formBlock) formBlock.hidden = 'form' !== mode;
			if (urlBlock) urlBlock.hidden = 'url' !== mode;
		}
		modeInputs.forEach(function (i) { i.addEventListener('change', syncMode); });
		syncMode();

		aiSubmit(root, form, function () {
			var checked = form.querySelector('input[name="ai_llms_mode"]:checked');
			var mode = checked ? checked.value : 'form';
			if ('url' === mode) {
				var urlInput = form.querySelector('input[name="ai_llms_url"]');
				var url = normalizeUrl(urlInput && urlInput.value);
				if (!url) {
					if (urlInput) urlInput.focus();
					return null;
				}
				return { tool: 'llms-txt', mode: 'url', url: url, locale: toolLocale(root) };
			}
			var nome = form.querySelector('[name="ai_llms_nome"]');
			var cosa = form.querySelector('[name="ai_llms_cosa"]');
			var pagine = form.querySelector('[name="ai_llms_pagine"]');
			if (!nome || !nome.value.trim() || !cosa || !cosa.value.trim()) {
				if (nome && !nome.value.trim()) nome.focus();
				return null;
			}
			return {
				tool: 'llms-txt',
				mode: 'form',
				nome: nome.value.trim(),
				cosa: cosa.value.trim(),
				pagine: pagine ? pagine.value.trim() : '',
				locale: toolLocale(root)
			};
		}, function (data) {
			var out = q(root, '[data-ai-llms-output]');
			if (out) out.value = data.llms_txt;
			setText(root, '[data-ai-llms-note]', data.note || '');

			var copyBtn = q(root, '[data-ai-copy]');
			if (copyBtn && !copyBtn.dataset.aiBound) {
				copyBtn.dataset.aiBound = '1';
				copyBtn.addEventListener('click', function () {
					if (!out || !navigator.clipboard) return;
					navigator.clipboard.writeText(out.value).then(function () {
						var original = copyBtn.textContent;
						copyBtn.textContent = txt(root, 'data-ai-copy-done', 'Copiato');
						window.setTimeout(function () { copyBtn.textContent = original; }, 2000);
					}).catch(function () { /* clipboard non disponibile: nessun crash */ });
				});
			}
			var downloadBtn = q(root, '[data-ai-download]');
			if (downloadBtn && !downloadBtn.dataset.aiBound) {
				downloadBtn.dataset.aiBound = '1';
				downloadBtn.addEventListener('click', function () {
					if (!out || !window.Blob) return;
					var blob = new Blob([out.value], { type: 'text/plain;charset=utf-8' });
					var a = document.createElement('a');
					a.href = URL.createObjectURL(blob);
					a.download = 'llms.txt';
					document.body.appendChild(a);
					a.click();
					document.body.removeChild(a);
					window.setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
				});
			}
		});
	}

	/* ---------- Бегущая строка прогресса для всех тестов ----------
	   Все виджеты (speed/seo/a11y/co2/gdpr/ai/eeat/checkup + 3 AI-инструмента
	   + hero) показывают проверку одинаково: контейнер [data-sr-tool-pending]
	   (или [data-sr-hero-pending]) переключается через hidden. Вставляем в
	   каждый такой контейнер один раз ленту прогресса в фирменном стиле:
	   контейнер скрыт по умолчанию, поэтому CSS-анимация идёт только пока
	   тест выполняется. Так пользователю видно, что тест не завис. */
	function initPendingBars() {
		document.querySelectorAll('[data-sr-tool-pending], [data-sr-hero-pending]').forEach(function (el) {
			if (el.querySelector('.sr-progress')) {
				return;
			}
			var track = document.createElement('span');
			track.className = 'sr-progress';
			track.setAttribute('aria-hidden', 'true');
			var bar = document.createElement('span');
			bar.className = 'sr-progress__bar';
			track.appendChild(bar);
			el.appendChild(track);
		});
	}

	/** Dispatcher: inizializza ogni widget in base a data-sr-tool. */
	function initToolWidgets() {
		document.querySelectorAll('[data-sr-tool]').forEach(function (root) {
			switch (root.getAttribute('data-sr-tool')) {
				case 'speed': initSpeedTool(root); break;
				case 'seo': initLighthouseTool(root, 'seo'); break;
				case 'a11y': initLighthouseTool(root, 'a11y'); break;
				case 'co2': initCo2Tool(root); break;
				case 'gdpr': initGdprTool(root); break;
				case 'ai': initAiTool(root); break;
				case 'roi': initRoiTool(root); break;
				case 'checkup': initCheckupTool(root); break;
				case 'eeat': initEeatTool(root); break;
				case 'ai-read': initAiReadTool(root); break;
				case 'ai-suona': initAiSuonaTool(root); break;
				case 'ai-llms': initAiLlmsTool(root); break;
			}
		});
		// Retro-compatibilità: form velocità senza wrapper [data-sr-tool].
		document.querySelectorAll('[data-sr-tool-form]').forEach(function (form) {
			if (!form.closest('[data-sr-tool]')) { initSpeedTool(form); }
		});
	}

	/* ---------- 6. Cookie banner + WhatsApp FAB ---------- */

	function initCookieBanner() {
		var banner = document.querySelector('[data-sr-cookie-banner]');
		if (!banner) {
			return;
		}
		var KEY = 'sr-cookie-choice';
		try {
			if (!window.localStorage.getItem(KEY)) {
				banner.hidden = false;
			}
		} catch (err) {
			banner.hidden = false;
		}
		banner.querySelectorAll('[data-sr-cookie-choice]').forEach(function (btn) {
			btn.addEventListener('click', function () {
				try {
					window.localStorage.setItem(KEY, btn.getAttribute('data-sr-cookie-choice'));
				} catch (err) { /* privacy mode: la scelta vale solo per la sessione */ }
				banner.hidden = true;
			});
		});
	}

	function initWaFab() {
		var fab = document.querySelector('[data-sr-wa-fab]');
		if (!fab) {
			return;
		}
		var check = function () {
			var scrolled = window.scrollY + window.innerHeight;
			var threshold = document.documentElement.scrollHeight * 0.6;
			fab.classList.toggle('sr-visible', scrolled > threshold);
		};
		check();
		window.addEventListener('scroll', check, { passive: true });
		window.addEventListener('resize', check);
	}

	/* ---------- 7. Переключатель языка (IT/EN/RU) ----------
	   Ссылки на реальные переводы текущей страницы: конфиг приходит из
	   PHP (window.remarkaLang, см. inc/multilang.php). Вставляется JS-ом
	   в #primary-menu, чтобы не трогать header.php Prespa. */
	function initLangSwitch() {
		var menu = document.getElementById('primary-menu');
		var cfg = window.remarkaLang;
		if (!menu || !cfg || !cfg.urls || menu.querySelector('.sr-lang-switch')) {
			return;
		}

		var li = document.createElement('li');
		li.className = 'sr-lang-switch';
		li.innerHTML = '<span class="sr-lang-switch__divider" aria-hidden="true"></span>' +
			['it', 'en', 'ru'].map(function (code) {
				var active = code === cfg.current ? ' sr-lang-switch__btn--active' : '';
				return '<a class="sr-lang-switch__btn' + active + '" href="' + cfg.urls[code] + '" hreflang="' + code + '">' +
					code.toUpperCase() + '</a>';
			}).join('');

		var searchItem = menu.querySelector('.search-icon');
		if (searchItem) {
			menu.insertBefore(li, searchItem);
		} else {
			menu.appendChild(li);
		}
	}

	/* ---------- 8. Modulo contatti ----------
	   Progressive enhancement: без JS форма шлёт обычный POST на
	   admin-post.php; здесь перехватываем и шлём через fetch на
	   admin-ajax, показывая успех/ошибку без перезагрузки. */
	/* Многошаговость формы: показываем один fieldset[data-sr-step] за раз,
	   валидируем шаг перед переходом, ведём полоску прогресса. Без JS все
	   шаги видны и форма шлётся одним POST — фолбэк не ломается. */
	function initStepForm(form, i18n, errorEl) {
		var steps = form.querySelectorAll('[data-sr-step]');
		var submitBtn = form.querySelector('[data-sr-submit]');
		var progress = form.querySelector('[data-sr-progress]');
		var pFill = form.querySelector('[data-sr-progress-fill]');
		var pLabel = form.querySelector('[data-sr-progress-label]');
		if (steps.length < 2 || !submitBtn) return;

		var cur = 0;
		var nav = document.createElement('div');
		nav.className = 'sr-form-nav';
		var back = document.createElement('button');
		back.type = 'button';
		back.className = 'sr-form-back';
		back.textContent = i18n.back || '← Indietro';
		var next = document.createElement('button');
		next.type = 'button';
		next.className = 'wp-block-button__link';
		next.textContent = i18n.next || 'Continua →';
		nav.appendChild(back);
		nav.appendChild(next);
		form.insertBefore(nav, errorEl);

		function showErr(msg) { if (errorEl) { errorEl.textContent = msg; errorEl.hidden = false; } }
		function hideErr() { if (errorEl) errorEl.hidden = true; }

		function validStep(step) {
			var groups = {};
			step.querySelectorAll('input[type="radio"]').forEach(function (r) {
				if (!(r.name in groups)) groups[r.name] = false;
				if (r.checked) groups[r.name] = true;
			});
			for (var g in groups) { if (!groups[g]) { showErr(i18n.choose || 'Seleziona un’opzione.'); return false; } }
			var invalid = null;
			step.querySelectorAll('input:not([type="radio"]), textarea, select').forEach(function (f) {
				if (!invalid && !f.checkValidity()) invalid = f;
			});
			if (invalid) { if (invalid.reportValidity) invalid.reportValidity(); return false; }
			return true;
		}

		function show(n) {
			steps.forEach(function (s, idx) { s.hidden = idx !== n; });
			var last = n === steps.length - 1;
			back.style.visibility = n === 0 ? 'hidden' : 'visible';
			next.hidden = last;
			submitBtn.hidden = !last;
			if (progress) {
				progress.hidden = false;
				if (pFill) pFill.style.width = ((n + 1) / steps.length * 100) + '%';
				if (pLabel) pLabel.textContent = (i18n.step || 'Passo') + ' ' + (n + 1) + ' ' + (i18n.of || 'di') + ' ' + steps.length;
			}
			var focusable = steps[n].querySelector('input, textarea, select');
			if (focusable && n > 0) { try { focusable.focus({ preventScroll: true }); } catch (err) {} }
		}

		next.addEventListener('click', function () { if (validStep(steps[cur])) { hideErr(); cur++; show(cur); } });
		back.addEventListener('click', function () { if (cur > 0) { hideErr(); cur--; show(cur); } });
		show(0);
	}

	function initContactForm() {
		document.querySelectorAll('[data-sr-contact-form]').forEach(function (form) {
			var success = form.parentElement.querySelector('[data-sr-form-success]');
			var errorEl = form.querySelector('[data-sr-form-error]');
			var btn = form.querySelector('button[type="submit"]');
			var cfg = window.remarkaPSI || {};
			var i18n = window.remarkaForm || {};

			// Отражаем имя выбранного файла в зоне загрузки.
			var fileInput = form.querySelector('.sr-upload__input');
			var uploadText = form.querySelector('[data-sr-upload-text]');
			if (fileInput && uploadText) {
				var uploadOrig = uploadText.innerHTML;
				fileInput.addEventListener('change', function () {
					if (fileInput.files && fileInput.files.length) {
						uploadText.textContent = fileInput.files[0].name;
					} else {
						uploadText.innerHTML = uploadOrig;
					}
				});
			}

			if (!cfg.ajaxUrl || !window.fetch) {
				return; // остаётся нативный POST-фолбэк (все шаги видны)
			}

			initStepForm(form, i18n, errorEl);

			form.addEventListener('submit', function (e) {
				e.preventDefault();
				if (errorEl) errorEl.hidden = true;
				if (btn) {
					btn.disabled = true;
					btn.dataset.srLabel = btn.textContent;
					btn.textContent = i18n.sending || 'Invio in corso…';
				}

				var data = new FormData(form);
				data.set('action', 'remarka_contact');
				if (cfg.formNonce) data.set('remarka_nonce', cfg.formNonce);

				window.fetch(cfg.ajaxUrl, { method: 'POST', body: data, credentials: 'same-origin' })
					.then(function (resp) { return resp.json(); })
					.then(function (json) {
						if (json && json.success) {
							form.hidden = true;
							if (success) success.hidden = false;
						} else {
							var msg = (json && json.data && json.data.message) ||
								'Invio non riuscito. Riprovate o scriveteci su WhatsApp.';
							if (errorEl) {
								errorEl.textContent = msg;
								errorEl.hidden = false;
							}
						}
					})
					.catch(function () {
						if (errorEl) {
							errorEl.textContent = 'Problema di rete: riprovate tra qualche istante.';
							errorEl.hidden = false;
						}
					})
					.finally(function () {
						if (btn) {
							btn.disabled = false;
							btn.textContent = btn.dataset.srLabel || 'Invia la richiesta';
						}
					});
			});
		});
	}

	/* ---------- 9. Blocco home check-up completo ----------
	   Non è un widget [data-sr-tool]: non misura nulla in home, si limita a
	   normalizzare l'URL e mandare alla pagina check-up con ?url=…&autostart=1
	   (patterns/checkup-home.php + lang-en/lang-ru). L'analisi vera parte lì
	   (initCheckupTool). Lang-aware (M4): il percorso di destinazione dipende
	   da data-sr-locale sul form (come i widget strumenti, via toolLocale()),
	   così ogni blocco home (IT/EN/RU) manda alla pagina check-up della
	   propria lingua. */
	var CHECKUP_PAGE_PATH = {
		it: '/strumenti/check-up-completo/',
		en: '/en/tools/full-site-checkup/',
		ru: '/ru/instrumenty/polnaya-proverka-sajta/',
	};
	function initCheckupHomeForm() {
		document.querySelectorAll('[data-sr-checkup-home]').forEach(function (form) {
			form.addEventListener('submit', function (e) {
				e.preventDefault();
				var input = form.querySelector('input[type="text"]');
				var url = normalizeUrl(input && input.value);
				if (!url) {
					if (input) input.focus();
					return;
				}
				var locale = toolLocale(form);
				var path = CHECKUP_PAGE_PATH[locale] || CHECKUP_PAGE_PATH.it;
				window.location.href = path + '?url=' + encodeURIComponent(url) + '&autostart=1';
			});
		});
	}

	/* ---------- 10. Filtro a chip del catalogo casi studio ----------
	   patterns/pages/casi-studio-index.php (+ en-): righe di pulsanti
	   [data-sr-case-filter="all|siti|webapp|seo|restyling"] sopra la
	   griglia di sezioni [data-cat] .sr-case-card. Nessuna dipendenza da
	   framework: solo hidden/show, coerente con lo stile del resto del file. */
	function initCaseFilter() {
		var bars = document.querySelectorAll('[data-sr-case-filter-bar]');
		if (!bars.length) return;

		bars.forEach(function (bar) {
			var scope = bar.closest('[data-sr-case-scope]') || document;
			var btns = bar.querySelectorAll('[data-sr-case-filter]');
			var cards = scope.querySelectorAll('.sr-case-card[data-cat]');

			function apply(key) {
				cards.forEach(function (card) {
					var show = key === 'all' || card.getAttribute('data-cat') === key;
					card.hidden = !show;
				});
				btns.forEach(function (b) {
					b.classList.toggle('is-active', b.getAttribute('data-sr-case-filter') === key);
					b.setAttribute('aria-pressed', b.getAttribute('data-sr-case-filter') === key ? 'true' : 'false');
				});
			}

			btns.forEach(function (btn) {
				btn.addEventListener('click', function () {
					apply(btn.getAttribute('data-sr-case-filter'));
				});
			});
		});
	}

	onReady(function () {
		initReveal();
		initBarre();
		initCounters();
		initPrespaFallback();
		initHeroWidgets();
		initPendingBars();
		initToolWidgets();
		initCheckupHomeForm();
		initCookieBanner();
		initWaFab();
		initLangSwitch();
		initContactForm();
		initCaseFilter();
	});
})();
