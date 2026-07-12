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

	/* ---------- 5. Demo-виджеты скорости ---------- */

	function hashScore(url, min, range) {
		var h = 0;
		for (var i = 0; i < url.length; i++) {
			h = (h * 31 + url.charCodeAt(i)) >>> 0;
		}
		return min + (h % range);
	}

	function itNumber(value, decimals) {
		return value.toFixed(decimals).replace('.', ',');
	}

	/** Виджет в hero: собственный балл студии (97) + форма «а у вас?». */
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
				var url = (input.value || '').trim() || 'www.tuosito.it';
				running = true;
				if (pending) pending.hidden = false;
				if (result) result.hidden = true;
				if (fill) fill.style.width = '0%';

				window.setTimeout(function () {
					var score = hashScore(url, 31, 28);
					if (pending) pending.hidden = true;
					if (result) result.hidden = false;
					if (urlOut) urlOut.textContent = url;
					if (scoreOut) scoreOut.textContent = String(score);
					if (fill) {
						window.requestAnimationFrame(function () {
							window.requestAnimationFrame(function () {
								fill.style.width = score + '%';
							});
						});
					}
					running = false;
				}, 1400);
			});
		});
	}

	/** Виджet strumento «Test velocità»: punteggio + LCP/INP/CLS. */
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

			form.addEventListener('submit', function (e) {
				e.preventDefault();
				if (running) {
					return;
				}
				var input = form.querySelector('input[type="text"]');
				var url = (input.value || '').trim() || 'www.tuosito.it';
				running = true;
				if (pending) pending.hidden = false;
				if (result) result.hidden = true;

				window.setTimeout(function () {
					var score = hashScore(url, 28, 37);
					var lcp = Math.max(1.2, 6.2 - score * 0.05);
					var inp = Math.max(120, 640 - score * 6);
					var cls = Math.max(0.02, 0.42 - score * 0.004);

					var set = function (sel, text) {
						var el = form.querySelector(sel);
						if (el) el.textContent = text;
					};
					set('[data-sr-tool-url]', url);
					set('[data-sr-tool-score]', String(score));
					set('[data-sr-tool-verdict]', verdictFor(score));
					set('[data-sr-tool-lcp]', itNumber(lcp, 1) + ' s');
					set('[data-sr-tool-inp]', Math.round(inp) + ' ms');
					set('[data-sr-tool-cls]', itNumber(cls, 2));

					if (pending) pending.hidden = true;
					if (result) result.hidden = false;

					var fill = form.querySelector('[data-sr-tool-fill]');
					if (fill) {
						fill.style.width = '0%';
						window.requestAnimationFrame(function () {
							window.requestAnimationFrame(function () {
								fill.style.width = score + '%';
							});
						});
					}
					running = false;
				}, 1800);
			});
		});
	}
	/* TODO produzione: sostituire hashScore()/verdictFor() con una chiamata
	   server-side alla PageSpeed Insights API (mediana di 3 rilevazioni),
	   mantenendo lo stesso stato pending 1.4–1.8s e la stessa struttura dati. */

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

	onReady(function () {
		initReveal();
		initBarre();
		initCounters();
		initPrespaFallback();
		initHeroWidgets();
		initToolWidgets();
		initCookieBanner();
		initWaFab();
	});
})();
