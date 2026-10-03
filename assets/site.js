/* Shared behaviour for the Goldfib research library: reading progress, TOC highlight,
   scroll-reveal, topic filter tabs and the mobile menu. */
(function () {
  var $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };

  // reading progress + active TOC entry
  var p = document.getElementById('progress'), toc = $$('.toc a[href^="#"]');
  function onScroll() {
    var h = document.documentElement;
    if (p) p.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + '%';
    var cur;
    toc.forEach(function (a) { var t = document.getElementById(a.getAttribute('href').slice(1)); if (t && t.getBoundingClientRect().top < 140) cur = a; });
    toc.forEach(function (a) { a.classList.toggle('on', a === cur); });
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // scroll-reveal (content stays visible without JS or with reduced motion)
  var targets = $$('.prose > .viz, .prose > .stats, .prose > .callout, .prose > .takeaways, .cta, .rel, .cluster > h2, .map, .featured');
  if ('IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .08, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (el, i) {
      if (el.getBoundingClientRect().top < innerHeight) return;
      el.classList.add('reveal'); el.style.transitionDelay = (el.classList.contains('rel') ? (i % 3) * 70 : 0) + 'ms'; io.observe(el);
    });
  }

  // topic filter tabs on the library index
  var tabs = $$('.tab[data-filter]');
  tabs.forEach(function (t) {
    t.addEventListener('click', function () {
      var f = t.dataset.filter;
      tabs.forEach(function (x) { x.classList.toggle('on', x === t); x.setAttribute('aria-pressed', x === t); });
      $$('.cluster').forEach(function (c) { c.hidden = f !== 'all' && c.id !== f; });
      $$('[data-hide-filtered]').forEach(function (c) { c.hidden = f !== 'all'; });
      $$('.rel.reveal').forEach(function (c) { c.classList.add('in'); });
    });
  });

  // mobile menu
  var nav = document.querySelector('.nav'), btn = document.querySelector('.nav-toggle');
  if (btn) btn.addEventListener('click', function () { var o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', o); });
})();
