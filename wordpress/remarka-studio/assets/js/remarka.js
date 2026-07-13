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

	function itNumber(value, decimals) {
		return value.toFixed(decimals).replace('.', ',');
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

	function psiFetch(url) {
		var endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed' +
			'?url=' + encodeURIComponent(url) +
			'&strategy=mobile&category=performance&locale=it';
		var key = (window.remarkaPSI && window.remarkaPSI.key) || '';
		if (key) {
			endpoint += '&key=' + encodeURIComponent(key);
		}
		return window.fetch(endpoint).then(function (resp) {
			if (!resp.ok) {
				throw new Error('PSI HTTP ' + resp.status);
			}
			return resp.json();
		}).then(function (data) {
			var lh = data.lighthouseResult;
			if (!lh || !lh.categories || !lh.categories.performance) {
				throw new Error('PSI: risposta senza punteggio');
			}
			var audits = lh.audits || {};
			var field = (data.loadingExperience && data.loadingExperience.metrics) || {};
			var lcpAudit = audits['largest-contentful-paint'];
			var clsAudit = audits['cumulative-layout-shift'];
			var inpField = field.INTERACTION_TO_NEXT_PAINT;
			return {
				score: Math.round(lh.categories.performance.score * 100),
				lcpSec: lcpAudit && typeof lcpAudit.numericValue === 'number' ? lcpAudit.numericValue / 1000 : null,
				cls: clsAudit && typeof clsAudit.numericValue === 'number' ? clsAudit.numericValue : null,
				inpMs: inpField && typeof inpField.percentile === 'number' ? inpField.percentile : null
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

				psiFetch(url).then(function (m) {
					if (urlOut) urlOut.textContent = url.replace(/^https?:\/\//, '');
					if (scoreOut) scoreOut.textContent = String(m.score);
					if (result) result.hidden = false;
					if (fill) {
						window.requestAnimationFrame(function () {
							window.requestAnimationFrame(function () {
								fill.style.width = m.score + '%';
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

	/** Виджет strumento «Test velocità»: punteggio reale + LCP/INP/CLS. */
	function initToolWidgets() {
		document.querySelectorAll('[data-sr-tool-form]').forEach(function (form) {
			var pending = form.querySelector('[data-sr-tool-pending]');
			var result = form.querySelector('[data-sr-tool-result]');
			var running = false;

			function verdictFor(score) {
				if (score < 50) {
					return 'Il sito è lento su mobile: la maggior parte dei visitatori abbandona prima del caricamento completo. Un restyling tecnico è la priorità.';
				}
				if (score < 90) {
					return 'Il sito è nella media, ma lontano dagli standard consigliati da Google. Ci sono margini di miglioramento concreti e misurabili.';
				}
				return 'Ottimo punteggio: il sito rispetta gli standard Google per l’esperienza mobile.';
			}

			var set = function (sel, text) {
				var el = form.querySelector(sel);
				if (el) el.textContent = text;
			};

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

				psiFetch(url).then(function (m) {
					set('[data-sr-tool-url]', url.replace(/^https?:\/\//, '') + ' — PageSpeed mobile');
					set('[data-sr-tool-score]', String(m.score));
					set('[data-sr-tool-verdict]', verdictFor(m.score));
					set('[data-sr-tool-lcp]', m.lcpSec !== null ? itNumber(m.lcpSec, 1) + ' s' : '—');
					set('[data-sr-tool-inp]', m.inpMs !== null ? Math.round(m.inpMs) + ' ms' : '—');
					set('[data-sr-tool-cls]', m.cls !== null ? itNumber(m.cls, 2) : '—');

					if (result) result.hidden = false;

					var fill = form.querySelector('[data-sr-tool-fill]');
					if (fill) {
						fill.style.width = '0%';
						window.requestAnimationFrame(function () {
							window.requestAnimationFrame(function () {
								fill.style.width = m.score + '%';
							});
						});
					}
				}).catch(function () {
					set('[data-sr-tool-url]', '');
					set('[data-sr-tool-score]', '—');
					set('[data-sr-tool-verdict]', PSI_ERROR_MSG);
					set('[data-sr-tool-lcp]', '—');
					set('[data-sr-tool-inp]', '—');
					set('[data-sr-tool-cls]', '—');
					if (result) result.hidden = false;
				}).finally(function () {
					if (pending) pending.hidden = true;
					running = false;
				});
			});
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
	   Per il design brief: solo stato UI, persistito in localStorage,
	   traduzione contenuti non implementata (TODO — vedi README handoff).
	   Iniettato via JS invece che in header.php: non tocchiamo markup/JS
	   di Prespa di cui non abbiamo il sorgente completo (ricerca, menu
	   mobile) — stesso approccio già usato per il footer proprietario. */
	function initLangSwitch() {
		var menu = document.getElementById('primary-menu');
		if (!menu || menu.querySelector('.sr-lang-switch')) {
			return;
		}
		var langs = ['IT', 'EN', 'RU'];
		var stored = window.localStorage.getItem('sr-lang') || 'IT';

		var li = document.createElement('li');
		li.className = 'sr-lang-switch';
		li.innerHTML = '<span class="sr-lang-switch__divider" aria-hidden="true"></span>' +
			langs.map(function (code) {
				return '<button type="button" class="sr-lang-switch__btn" data-sr-lang="' + code + '">' + code + '</button>';
			}).join('');

		var searchItem = menu.querySelector('.search-icon');
		if (searchItem) {
			menu.insertBefore(li, searchItem);
		} else {
			menu.appendChild(li);
		}

		function setActive(code) {
			li.querySelectorAll('[data-sr-lang]').forEach(function (btn) {
				btn.classList.toggle('sr-lang-switch__btn--active', btn.getAttribute('data-sr-lang') === code);
			});
		}

		li.addEventListener('click', function (e) {
			var btn = e.target.closest('[data-sr-lang]');
			if (!btn) {
				return;
			}
			var code = btn.getAttribute('data-sr-lang');
			window.localStorage.setItem('sr-lang', code);
			setActive(code);
		});

		setActive(stored);
	}

	/* ---------- 8. Modulo contatti ----------
	   Progressive enhancement: без JS форма шлёт обычный POST на
	   admin-post.php; здесь перехватываем и шлём через fetch на
	   admin-ajax, показывая успех/ошибку без перезагрузки. */
	function initContactForm() {
		document.querySelectorAll('[data-sr-contact-form]').forEach(function (form) {
			var success = form.parentElement.querySelector('[data-sr-form-success]');
			var errorEl = form.querySelector('[data-sr-form-error]');
			var btn = form.querySelector('button[type="submit"]');
			var cfg = window.remarkaPSI || {};
			if (!cfg.ajaxUrl || !window.fetch) {
				return; // остаётся нативный POST-фолбэк
			}

			form.addEventListener('submit', function (e) {
				e.preventDefault();
				if (errorEl) errorEl.hidden = true;
				if (btn) {
					btn.disabled = true;
					btn.dataset.srLabel = btn.textContent;
					btn.textContent = 'Invio in corso…';
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

	onReady(function () {
		initReveal();
		initBarre();
		initCounters();
		initPrespaFallback();
		initHeroWidgets();
		initToolWidgets();
		initCookieBanner();
		initWaFab();
		initLangSwitch();
		initContactForm();
	});
})();
