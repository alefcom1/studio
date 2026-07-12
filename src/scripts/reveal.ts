const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function initCascades() {
  document.querySelectorAll<HTMLElement>('[data-reveal-cascade]').forEach((container) => {
    Array.from(container.children).forEach((child, i) => {
      if (child instanceof HTMLElement && !child.hasAttribute('data-reveal')) {
        child.setAttribute('data-reveal', '');
        child.style.transitionDelay = `${i * 80}ms`;
      }
    });
  });
}

function initReveal() {
  const targets = document.querySelectorAll<HTMLElement>('[data-reveal]');
  if (prefersReducedMotion) {
    targets.forEach((el) => el.classList.add('is-visible'));
    return;
  }
  targets.forEach((el) => {
    const delay = el.getAttribute('data-reveal-delay');
    if (delay) el.style.transitionDelay = `${delay}ms`;
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );
  targets.forEach((el) => observer.observe(el));
}

function initBarre() {
  const bars = document.querySelectorAll<HTMLElement>('[data-barra]');
  if (prefersReducedMotion) {
    bars.forEach((el) => el.setAttribute('data-barra-ready', ''));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target as HTMLElement;
          const delay = Number(el.getAttribute('data-barra-delay') || 0);
          window.setTimeout(() => el.setAttribute('data-barra-ready', ''), delay);
          observer.unobserve(el);
        }
      });
    },
    { threshold: 0.4 }
  );
  bars.forEach((el) => observer.observe(el));
}

function easeOutCubic(t: number) {
  return 1 - Math.pow(1 - t, 3);
}

function initCounters() {
  const counters = document.querySelectorAll<HTMLElement>('[data-counter-to]');
  const format = (el: HTMLElement, value: number) => {
    const decimals = Number(el.getAttribute('data-counter-decimals') || 0);
    return value.toFixed(decimals).replace('.', ',');
  };

  if (prefersReducedMotion) {
    counters.forEach((el) => {
      const to = Number(el.getAttribute('data-counter-to'));
      el.textContent = format(el, to);
    });
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target as HTMLElement;
        const to = Number(el.getAttribute('data-counter-to'));
        const duration = 1200;
        const start = performance.now();
        function tick(now: number) {
          const progress = Math.min(1, (now - start) / duration);
          const value = to * easeOutCubic(progress);
          el.textContent = format(el, value);
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        observer.unobserve(el);
      });
    },
    { threshold: 0.4 }
  );
  counters.forEach((el) => observer.observe(el));
}

function init() {
  initCascades();
  initReveal();
  initBarre();
  initCounters();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
