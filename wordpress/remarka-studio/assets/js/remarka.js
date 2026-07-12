/**
 * Remarka Studio — фронтовый движок (~3 КБ, без зависимостей).
 *
 * 1. sr-reveal / sr-cascade — появление блоков (порт из прототипа).
 * 2. .sr-barra[data-sr-target] — la barra dei cento: заливка до целевого %.
 * 3. .sr-counter[data-sr-to] — счётчик числа (0 → цель, ease-out cubic).
 * 4. Фолбэк для анимаций Prespa: если JS родительской темы не добавил
 *    .animated элементам .p-animation-*, добавляем сами по тому же контракту.
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

	onReady(function () {
		initReveal();
		initBarre();
		initCounters();
		initPrespaFallback();
	});
})();
