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
  var targets = $$('.prose > .viz, .prose > .stats, .prose > .callout, .prose > .takeaways, .cta, .rel, .cluster-head, .card, .start');
  if ('IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .08, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (el, i) {
      if (el.getBoundingClientRect().top < innerHeight) return;
      el.classList.add('reveal'); el.style.transitionDelay = (el.classList.contains('card') ? (i % 3) * 70 : 0) + 'ms'; io.observe(el);
    });
  }

  // library filters: topic pills, level, search (combined)
  var q = document.getElementById('lib-q'), topic = 'all', lvl = 'all';
  function apply() {
    var term = q ? q.value.trim().toLowerCase() : '', any = false;
    $$('.cluster').forEach(function (c) {
      var shown = 0;
      $$('.card', c).forEach(function (k) {
        var ok = (topic === 'all' || k.dataset.cluster === topic) && (lvl === 'all' || k.dataset.level === lvl) &&
          (!term || term.split(/\s+/).every(function (w) { return k.dataset.search.indexOf(w) > -1; }));
        k.hidden = !ok; if (ok) { shown++; k.classList.add('in'); }
      });
      c.hidden = !shown; if (shown) any = true;
    });
    var nr = document.querySelector('.no-results'); if (nr) nr.hidden = any;
  }
  $$('.pill[data-filter]').forEach(function (t) {
    t.addEventListener('click', function () {
      topic = t.dataset.filter;
      $$('.pill[data-filter]').forEach(function (x) { x.classList.toggle('on', x === t); x.setAttribute('aria-pressed', x === t); });
      apply();
    });
  });
  $$('.lv').forEach(function (t) {
    t.addEventListener('click', function () { lvl = t.dataset.level; $$('.lv').forEach(function (x) { x.classList.toggle('on', x === t); }); apply(); });
  });
  if (q) q.addEventListener('input', apply);

  // mobile menu
  var nav = document.querySelector('.nav'), btn = document.querySelector('.nav-toggle');
  if (btn) btn.addEventListener('click', function () { var o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', o); });
})();
