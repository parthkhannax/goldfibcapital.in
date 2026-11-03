/* Goldfib homepage motion. Uses GSAP, ScrollTrigger and SplitText (assets/vendor). */
(function () {
  'use strict';
  var root = document.documentElement;
  var unhide = function () { root.classList.remove('motion-wait'); };
  if (!window.gsap || !window.ScrollTrigger || !window.SplitText) { unhide(); return; }
  gsap.registerPlugin(ScrollTrigger, SplitText);
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return gsap.utils.toArray((c || document).querySelectorAll(s)); };
  var EASE = 'power3.out';

  /* ---------- Desk demo ---------- */
  var PROMPT = 'Find co-investors for our ₹25 Cr specialty chemicals deal and take it from sourcing to closing.';
  var STAGES = [
    ['Source', 'Sourcing', 'screening companies against your mandate'],
    ['Network', 'Network', 'mapping warm paths to aligned co-investors'],
    ['Diligence', 'Diligence', 'checking filings, financials and red flags'],
    ['IC', 'Investment committee', 'preparing the IC pack and decision log'],
    ['Close', 'Closing', 'tracking documents, signatures and funds flow']
  ];
  var FUNNEL = [['Sourced', 148], ['Screened', 36], ['Warm intros', 12], ['Diligence', 5], ['Closing', 1]];
  var KPIS = [[25, '₹', ' Cr', 'round size'], [6, '', '', 'co-investors matched'], [31, '', ' days', 'sourcing to close']];
  var NS = 'http://www.w3.org/2000/svg';

  function el(tag, cls, text, parent) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    if (parent) parent.appendChild(n);
    return n;
  }
  function svgEl(tag, attrs, parent) {
    var n = document.createElementNS(NS, tag);
    Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (parent) parent.appendChild(n);
    return n;
  }
  function svgText(str, x, y, cls, parent, anchor) {
    var t = svgEl('text', { x: x, y: y, class: cls, 'text-anchor': anchor || 'middle' }, parent);
    t.textContent = str;
    return t;
  }

  function buildDesk(demo) {
    var thread = $('#ddThread', demo);
    var refs = { thread: thread };
    refs.bubble = el('div', 'dd-bubble', PROMPT, thread);
    var slot = el('div', 'dd-slot', null, thread);

    var work = refs.work = el('div', 'dd-work', null, slot);
    var rail = el('div', 'dd-rail', null, work);
    refs.railFill = el('i', 'dd-rail-fill', null, rail);
    refs.railItems = STAGES.map(function (s) { return el('span', '', s[0], el('div', 'dd-stop', null, rail)).parentNode; });

    var svg = refs.viz = svgEl('svg', { class: 'dd-viz', viewBox: '0 0 400 210' }, work);
    refs.count = svgText('', 200, 18, 'v-count', svg);

    // Scene 1: 148 companies, 36 pass the screen
    var dotsG = svgEl('g', {}, svg), dots = [], cols = 19, rows = 8;
    for (var i = 0; i < 148; i++) {
      dots.push(svgEl('circle', { cx: 22 + (i % cols) * 19.9, cy: 48 + Math.floor(i / cols) * 21, r: 4.2, fill: '#1a2f4a' }, dotsG));
    }
    // Fixed scatter, so exactly 36 pass on every loop with no visible pattern
    var picks = dots.map(function (d, k) { return { d: d, h: (k + 1) * 2654435761 % 4294967296 }; })
      .sort(function (a, b) { return a.h - b.h; }).slice(0, 36).map(function (o) { return o.d; });
    refs.dots = dots;
    refs.pass = picks;
    refs.fail = dots.filter(function (d) { return picks.indexOf(d) < 0; });
    refs.scan = svgEl('rect', { x: 0, y: 34, width: 3, height: 164, rx: 1.5, fill: '#c9a961' }, svg);

    // Scene 2: the office connects to six co-investors
    var net = refs.net = svgEl('g', {}, svg);
    var cx = 200, cy = 118;
    refs.lines = []; refs.nodes = [];
    [[-150, -52], [-168, 30], [-96, 74], [96, 74], [168, 30], [150, -52]].forEach(function (p, n) {
      refs.lines.push(svgEl('line', { x1: cx, y1: cy, x2: cx + p[0], y2: cy + p[1], stroke: '#c9a961', 'stroke-width': 1.6, pathLength: 1, 'stroke-dasharray': 1, 'stroke-dashoffset': 1 }, net));
      var g = svgEl('g', {}, net);
      svgEl('circle', { cx: cx + p[0], cy: cy + p[1], r: 15, fill: '#fff', stroke: '#1a2f4a', 'stroke-width': 1.5 }, g);
      svgText('CI' + (n + 1), cx + p[0], cy + p[1] + 4, 'v-node', g);
      refs.nodes.push(g);
    });
    refs.hub = svgEl('g', {}, net);
    svgEl('circle', { cx: cx, cy: cy, r: 27, fill: '#1a2f4a' }, refs.hub);
    svgText('Your', cx, cy - 2, 'v-hub', refs.hub);
    svgText('office', cx, cy + 11, 'v-hub', refs.hub);

    // Scene 3: three diligence checks
    var dil = refs.dil = svgEl('g', {}, svg);
    refs.checks = ['Filings', 'Financials', 'Red flags'].map(function (label, n) {
      var y = 58 + n * 50;
      svgText(label, 32, y + 13, 'v-label', dil, 'start');
      svgEl('rect', { x: 118, y: y, width: 216, height: 18, rx: 4, fill: '#eef1f4' }, dil);
      var fill = svgEl('rect', { x: 118, y: y, width: 216, height: 18, rx: 4, fill: '#1a2f4a' }, dil);
      var tick = svgEl('path', { d: 'M348 ' + (y + 9) + 'l6 6 11-13', fill: 'none', stroke: '#a68a3e', 'stroke-width': 3, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', pathLength: 1, 'stroke-dasharray': 1, 'stroke-dashoffset': 1 }, dil);
      return { fill: fill, tick: tick };
    });

    // Scene 4: the IC pack assembles
    var ic = refs.ic = svgEl('g', {}, svg);
    refs.pages = [[-44, -6], [-22, -3], [0, 0]].map(function (o) {
      var g = svgEl('g', {}, ic);
      svgEl('rect', { x: 140 + o[0] + 30, y: 44 + o[1], width: 112, height: 150, rx: 6, fill: '#fff', stroke: '#1a2f4a', 'stroke-width': 1.4 }, g);
      return g;
    });
    var top = refs.pages[2];
    svgText('IC PACK', 226, 68, 'v-doc', top);
    refs.docLines = [82, 96, 110, 124, 138, 152, 166].map(function (y, n) {
      return svgEl('rect', { x: 184, y: y, width: n % 3 === 2 ? 56 : 84, height: 5, rx: 2, fill: n === 0 ? '#c9a961' : '#c4ccd6' }, top);
    });

    // Scene 5: documents, signatures, funds flow
    var close = refs.close = svgEl('g', {}, svg);
    svgEl('line', { x1: 70, y1: 112, x2: 330, y2: 112, stroke: '#e2e8f0', 'stroke-width': 4 }, close);
    refs.closeLine = svgEl('line', { x1: 70, y1: 112, x2: 330, y2: 112, stroke: '#c9a961', 'stroke-width': 4, pathLength: 1, 'stroke-dasharray': 1, 'stroke-dashoffset': 1 }, close);
    refs.closeNodes = [[70, 'Documents'], [200, 'Signatures'], [330, 'Funds flow']].map(function (c) {
      var g = svgEl('g', {}, close);
      svgEl('circle', { cx: c[0], cy: 112, r: 15, fill: '#1a2f4a' }, g);
      svgEl('path', { d: 'M' + (c[0] - 6) + ' 112l4 5 8-10', fill: 'none', stroke: '#fff', 'stroke-width': 2.4, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, g);
      svgText(c[1], c[0], 150, 'v-label', g);
      return g;
    });

    var cap = el('div', 'dd-caption', null, work);
    refs.capB = el('b', '', '', cap);
    refs.capT = el('span', '', '', cap);

    // Report
    var result = refs.result = el('div', 'dd-result', null, slot);
    refs.summary = el('div', 'dd-summary', 'Worked through 5 stages', result);
    var r = refs.report = el('div', 'dd-report', null, result);
    var head = el('div', 'dd-report-head', null, r);
    el('strong', '', 'Deal report: specialty chemicals', head);
    el('span', '', 'Illustrative', head);
    var kp = el('div', 'dd-kpis', null, r);
    refs.kpis = KPIS.map(function (k) {
      var d = el('div', '', null, kp);
      var b = el('b', '', k[1] + k[0] + k[2], d);
      el('span', '', k[3], d);
      return { box: d, b: b, v: k[0], pre: k[1], suf: k[2] };
    });
    el('span', 'dd-chart-title', 'Pipeline, companies at each stage', r);
    var f = el('div', 'dd-funnel', null, r);
    refs.rows = FUNNEL.map(function (s) {
      var row = el('div', 'dd-row', null, f);
      el('span', '', s[0], row);
      var bar = el('span', 'dd-bar', null, el('div', 'dd-track', null, row));
      bar.style.width = Math.max(s[1] / FUNNEL[0][1] * 100, 3).toFixed(1) + '%';
      var num = el('em', '', String(s[1]), row);
      return { bar: bar, num: num, v: s[1] };
    });
    return refs;
  }

  function counter(tl, target, from, to, write, dur, at) {
    var o = { n: from };
    tl.to(o, { n: to, duration: dur, ease: 'power2.out', onUpdate: function () { write(Math.round(o.n)); } }, at);
  }

  function animateDesk(demo, r) {
    var greet = $('.dd-greeting', demo), composer = $('.dd-composer', demo);
    var input = $('#ddInput', demo), send = $('#ddSend', demo);
    var caret = el('span', 'dd-caret'), typed = document.createTextNode('');

    function renderTyping(n) {
      if (n <= 0) {
        input.className = 'dd-input empty';
        input.textContent = 'Ask the desk...';
        send.classList.remove('ready');
        return;
      }
      if (input.firstChild !== typed) {
        input.className = 'dd-input';
        input.textContent = '';
        input.appendChild(typed);
        input.appendChild(caret);
        send.classList.add('ready');
      }
      typed.nodeValue = PROMPT.slice(0, n);
    }
    function setStage(i) {
      r.railItems.forEach(function (s, n) {
        s.classList.toggle('on', n === i);
        s.classList.toggle('done', n < i);
      });
      if (i >= 0) { r.capB.textContent = STAGES[i][1] + ': '; r.capT.textContent = STAGES[i][2]; }
    }
    function writeCount(n, word) { r.count.textContent = n + ' ' + word; }
    function reply() { input.className = 'dd-input empty'; input.textContent = 'Reply to the desk...'; send.classList.remove('ready'); }

    var scenes = [r.net, r.dil, r.ic, r.close];
    var byScan = function (i, d) { return (+d.getAttribute('cx') - 8) / 392 * .85; };
    renderTyping(0);
    gsap.set(composer, { y: -176 });
    gsap.set(input, { minHeight: 64 });
    gsap.set([r.bubble, r.work, r.result], { autoAlpha: 0 });
    gsap.set(r.bubble, { y: 26, scale: .96, transformOrigin: '100% 100%' });
    gsap.set(r.railFill, { scaleX: 0, transformOrigin: '0 50%' });
    gsap.set(r.dots, { scale: 0, transformOrigin: '50% 50%' });
    gsap.set(r.scan, { autoAlpha: 0, x: 8 });
    gsap.set(scenes, { autoAlpha: 0 });
    gsap.set(r.nodes.concat([r.hub]), { scale: 0, transformOrigin: '50% 50%' });
    r.checks.forEach(function (c) { gsap.set(c.fill, { scaleX: 0, transformOrigin: '0 50%' }); });
    gsap.set(r.pages, { y: 30, autoAlpha: 0 });
    gsap.set(r.docLines, { scaleX: 0, transformOrigin: '0 50%' });
    gsap.set(r.closeNodes, { autoAlpha: .22 });
    gsap.set(r.report, { y: 24, scale: .97 });
    gsap.set(r.kpis.map(function (k) { return k.box; }), { y: 12, autoAlpha: 0 });
    gsap.set(r.rows.map(function (x) { return x.bar; }), { scaleX: 0, transformOrigin: '0 50%' });
    gsap.set(r.summary, { autoAlpha: 0, x: -8 });

    var tl = gsap.timeline({ repeat: -1, paused: true, onRepeat: function () { renderTyping(0); setStage(-1); r.count.textContent = ''; } });
    var t = { n: 0 };
    tl.to(t, { n: PROMPT.length, duration: 2.9, ease: 'none', onUpdate: function () { renderTyping(Math.round(t.n)); } }, .8);
    tl.to(send, { scale: .82, duration: .1, ease: 'power2.in' }, '+=.35').to(send, { scale: 1, duration: .32, ease: 'back.out(3)' });
    tl.call(reply);
    tl.to(greet, { autoAlpha: 0, y: -24, duration: .4, ease: 'power2.in' }, '<');
    tl.to(composer, { y: 0, duration: .75, ease: 'expo.inOut' }, '<');
    tl.to(input, { minHeight: 21, duration: .75, ease: 'expo.inOut' }, '<');
    tl.to(r.bubble, { autoAlpha: 1, y: 0, scale: 1, duration: .6, ease: 'back.out(1.5)' }, '-=.35');
    tl.to(r.work, { autoAlpha: 1, duration: .3 }, '-=.15');

    function stage(i) { tl.call(setStage, [i]); tl.to(r.railFill, { scaleX: i / 4, duration: .45, ease: 'power2.inOut' }, '<'); }

    // Sourcing
    stage(0);
    tl.to(r.dots, { scale: 1, duration: .35, ease: 'back.out(3)', stagger: { amount: .55, from: 'random' } }, '<');
    counter(tl, null, 0, 148, function (n) { writeCount(n, 'companies'); }, .7, '<');
    tl.to(r.scan, { autoAlpha: 1, duration: .1 });
    tl.to(r.scan, { x: 392, duration: .85, ease: 'sine.inOut' }, '<');
    tl.to(r.fail, { attr: { fill: '#dbe0e6' }, scale: .55, duration: .22, stagger: byScan }, '<');
    tl.to(r.pass, { attr: { fill: '#c9a961' }, scale: 1.25, duration: .3, stagger: byScan }, '<');
    counter(tl, null, 148, 36, function (n) { writeCount(n, 'screened'); }, .85, '<');
    tl.to(r.scan, { autoAlpha: 0, duration: .15 }, '-=.05');

    // Network
    tl.to(r.fail, { autoAlpha: 0, duration: .25 }, '+=.3');
    tl.to(r.pass, { attr: { cx: 200, cy: 118 }, autoAlpha: 0, duration: .55, ease: 'power3.in', stagger: .006 }, '<');
    stage(1);
    tl.to(r.net, { autoAlpha: 1, duration: .05 }, '<+.3');
    tl.to(r.hub, { scale: 1, duration: .5, ease: 'back.out(2.2)' }, '<');
    counter(tl, null, 36, 12, function (n) { writeCount(n, 'warm intros'); }, .9, '<');
    tl.to(r.lines, { attr: { 'stroke-dashoffset': 0 }, duration: .4, ease: 'power2.out', stagger: .1 }, '-=.35');
    tl.to(r.nodes, { scale: 1, duration: .4, ease: 'back.out(2.6)', stagger: .1 }, '<+.2');
    tl.to(r.lines, { attr: { 'stroke-width': 2.6 }, duration: .25, yoyo: true, repeat: 1, stagger: .03 }, '+=.05');

    // Diligence
    tl.to(r.net, { autoAlpha: 0, scale: .94, transformOrigin: '50% 50%', duration: .3, ease: 'power2.in' }, '+=.3');
    stage(2);
    tl.to(r.dil, { autoAlpha: 1, duration: .25 }, '>-.05');
    counter(tl, null, 12, 5, function (n) { writeCount(n, 'in diligence'); }, 1.5, '<');
    r.checks.forEach(function (c, i) {
      tl.to(c.fill, { scaleX: 1, duration: .45, ease: 'power2.inOut' }, i ? '>-.05' : '<');
      tl.to(c.tick, { attr: { 'stroke-dashoffset': 0 }, duration: .18 }, '>-.03');
    });

    // Investment committee
    tl.to(r.dil, { autoAlpha: 0, y: -12, duration: .28, ease: 'power2.in' }, '+=.3');
    stage(3);
    tl.call(function () { r.count.textContent = 'Decision log open'; });
    tl.to(r.ic, { autoAlpha: 1, duration: .05 }, '>');
    tl.to(r.pages, { y: 0, autoAlpha: 1, duration: .45, ease: 'back.out(1.5)', stagger: .12 }, '<');
    tl.to(r.docLines, { scaleX: 1, duration: .2, ease: 'power2.out', stagger: .07 }, '-=.15');

    // Closing
    tl.to(r.ic, { autoAlpha: 0, y: -12, duration: .28, ease: 'power2.in' }, '+=.35');
    stage(4);
    tl.call(function () { r.count.textContent = '1 deal closing'; });
    tl.to(r.close, { autoAlpha: 1, duration: .2 }, '>');
    tl.to(r.closeLine, { attr: { 'stroke-dashoffset': 0 }, duration: 1.05, ease: 'none' }, '<');
    tl.to(r.closeNodes, { autoAlpha: 1, duration: .25, stagger: .42 }, '<');
    tl.to(r.closeNodes, { scale: 1.08, transformOrigin: '50% 50%', duration: .16, yoyo: true, repeat: 1, stagger: .42 }, '<');

    // Report
    tl.to(r.work, { autoAlpha: 0, y: -16, duration: .35, ease: 'power2.in' }, '+=.3');
    tl.to(r.result, { autoAlpha: 1, duration: .05 });
    tl.to(r.summary, { autoAlpha: 1, x: 0, duration: .3, ease: EASE }, '<');
    tl.to(r.report, { y: 0, scale: 1, duration: .6, ease: 'expo.out' }, '<');
    tl.to(r.kpis.map(function (k) { return k.box; }), { y: 0, autoAlpha: 1, duration: .4, ease: EASE, stagger: .09 }, '<+.1');
    r.kpis.forEach(function (k, i) {
      counter(tl, null, 0, k.v, function (n) { k.b.textContent = k.pre + n + k.suf; }, .8, i ? '<+.08' : '<');
    });
    tl.to(r.rows.map(function (x) { return x.bar; }), { scaleX: 1, duration: .75, ease: 'expo.out', stagger: .09 }, '<');
    r.rows.forEach(function (x, i) {
      counter(tl, null, 0, x.v, function (n) { x.num.textContent = n; }, .55, i ? '<+.09' : '<');
    });
    tl.to({}, { duration: 7.5 });
    tl.to(demo.querySelector('.dd-stage'), { autoAlpha: 0, duration: .4, ease: 'power1.in' });
    tl.set(demo.querySelector('.dd-stage'), { autoAlpha: 1 });
    return tl;
  }

  function staticDesk(demo, r) {
    demo.classList.remove('is-idle');
    gsap.set($('.dd-greeting', demo), { autoAlpha: 0 });
    gsap.set(r.work, { display: 'none' });
    $('#ddInput', demo).textContent = 'Reply to the desk...';
  }

  /* ---------- Page ---------- */
  function heroConstellation(hero) {
    var svg = svgEl('svg', { class: 'hero-net', viewBox: '0 0 1400 760', preserveAspectRatio: 'xMidYMid slice', 'aria-hidden': 'true' });
    hero.insertBefore(svg, hero.firstChild);
    var pts = [[70, 120], [230, 60], [420, 110], [120, 330], [300, 620], [90, 640], [600, 45], [800, 80], [1010, 45], [1230, 110], [1345, 300], [1290, 560], [1120, 700], [840, 725], [560, 710]];
    var lines = [], dots = [];
    pts.forEach(function (p, i) {
      var q = pts[(i + 1) % pts.length];
      lines.push(svgEl('line', { x1: p[0], y1: p[1], x2: q[0], y2: q[1], stroke: '#a68a3e', 'stroke-width': 1, pathLength: 1, 'stroke-dasharray': 1, 'stroke-dashoffset': 1 }, svg));
    });
    pts.forEach(function (p, i) { dots.push(svgEl('circle', { cx: p[0], cy: p[1], r: i % 3 ? 3 : 5, fill: i % 3 ? '#c9a961' : '#1a2f4a' }, svg)); });
    gsap.set(dots, { scale: 0, transformOrigin: '50% 50%' });
    gsap.to(lines, { attr: { 'stroke-dashoffset': 0 }, duration: .9, ease: 'power1.inOut', stagger: .1, delay: .3 });
    gsap.to(dots, { scale: 1, duration: .5, ease: 'back.out(3)', stagger: .1, delay: .25 });
    dots.forEach(function (d, i) {
      gsap.to(d, { y: i % 2 ? 7 : -7, duration: 2.6 + (i % 4) * .4, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: 2 });
    });
    gsap.to(svg, { yPercent: 16, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
    return svg;
  }

  function heroIntro(onDone) {
    var h1 = $('.hero h1'), flourish = $('.hero-flourish path');
    flourish.style.animation = 'none';
    gsap.set(flourish, { strokeDashoffset: 260 });
    unhide();
    var tl = gsap.timeline({ onComplete: onDone });
    tl.fromTo(h1, { clipPath: 'inset(0% 0% 100% 0%)', y: 34 }, { clipPath: 'inset(-8% -2% -14% -2%)', y: 0, duration: 1.25, ease: 'power4.inOut', clearProps: 'clipPath,transform' }, .05)
      .to(flourish, { strokeDashoffset: 0, duration: .8, ease: 'power2.inOut' }, '-=.25');
    gsap.from('.hero .lead', { y: 22, autoAlpha: 0, duration: .8, ease: EASE, delay: .55 });
    gsap.from('.hero .cta-row > *', { y: 18, autoAlpha: 0, duration: .65, ease: EASE, stagger: .1, delay: .72 });
    gsap.from('.desk-demo', { y: 48, autoAlpha: 0, scale: .97, duration: 1.1, ease: 'expo.out', delay: .4 });
  }

  function revealHeadings() {
    $$('.head h2, #study h2, .final h2, .founder h3').forEach(function (h) {
      SplitText.create(h, {
        type: 'lines', mask: 'lines', autoSplit: true,
        onSplit: function (self) {
          return gsap.from(self.lines, { yPercent: 110, duration: .95, ease: 'power4.out', stagger: .09, scrollTrigger: { trigger: h, start: 'top 88%', once: true } });
        }
      });
    });
    $$('.kicker, .head p, .final p').forEach(function (n) {
      gsap.from(n, { y: 16, autoAlpha: 0, duration: .7, ease: EASE, scrollTrigger: { trigger: n, start: 'top 90%', once: true } });
    });
  }

  function marquees() {
    $$('.marquee').forEach(function (m) {
      var track = $('.marquee-track', m), rev = m.classList.contains('rev');
      track.style.animation = 'none';
      var loop = gsap.fromTo(track, { xPercent: rev ? -50 : 0 }, { xPercent: rev ? 0 : -50, duration: 34, ease: 'none', repeat: -1 });
      var boost = gsap.quickTo(loop, 'timeScale', { duration: .6, ease: 'power2.out' });
      ScrollTrigger.create({
        trigger: m, start: 'top bottom', end: 'bottom top',
        onUpdate: function (self) { boost(1 + Math.min(Math.abs(self.getVelocity()) / 300, 5)); gsap.delayedCall(.15, function () { boost(1); }); }
      });
    });
  }

  function cards() {
    gsap.set('.pcard', { y: 56, autoAlpha: 0 });
    ScrollTrigger.batch('.pcard', { start: 'top 88%', once: true, onEnter: function (b) {
      gsap.to(b, { y: 0, autoAlpha: 1, duration: .95, ease: 'expo.out', stagger: .14 });
      b.forEach(function (c) { gsap.from(c.querySelectorAll('.nums > div'), { y: 18, autoAlpha: 0, duration: .55, ease: EASE, stagger: .08, delay: .25 }); });
    } });

    $$('.ps article').forEach(function (a, i) {
      var tl = gsap.timeline({ scrollTrigger: { trigger: a, start: 'top 84%', once: true } });
      tl.from(a, { y: 60, autoAlpha: 0, duration: .9, ease: 'expo.out', delay: i * .1 })
        .from(a.querySelector('.pain'), { x: -18, autoAlpha: 0, duration: .5, ease: EASE }, '-=.55')
        .from(a.querySelector('.gain'), { x: -18, autoAlpha: 0, duration: .5, ease: EASE }, '-=.2');
    });
  }

  function study() {
    var chart = $('.chart svg');
    if (chart) {
      var rects = gsap.utils.toArray(chart.querySelectorAll('rect'));
      var texts = gsap.utils.toArray(chart.querySelectorAll('text'));
      var tl = gsap.timeline({ scrollTrigger: { trigger: chart, start: 'top 78%', once: true } });
      tl.from(texts.slice(0, 2), { autoAlpha: 0, duration: .4 })
        .from(rects.slice(0, 3), { scaleX: 0, transformOrigin: '0 50%', duration: .55, ease: 'power3.inOut', stagger: .12 }, '-=.1')
        .from(texts.slice(2, 5), { autoAlpha: 0, duration: .3, stagger: .05 }, '-=.15')
        .from(texts[5], { autoAlpha: 0, duration: .3 })
        .from(rects.slice(3, 6), { scaleX: 0, transformOrigin: '0 50%', duration: .55, ease: 'power3.inOut', stagger: .12 }, '-=.1')
        .from(texts.slice(6, 9), { autoAlpha: 0, duration: .3, stagger: .05 }, '-=.15')
        .from([chart.querySelector('line')].concat(rects.slice(6), texts.slice(9)), { autoAlpha: 0, duration: .4 });
    }
    $$('.facts b').forEach(function (b) {
      var original = b.textContent, m = original.match(/^(\d+)h → (\d+)h$/), o;
      gsap.from(b.parentNode, { y: 18, autoAlpha: 0, duration: .6, ease: EASE, scrollTrigger: { trigger: b, start: 'top 90%', once: true } });
      if (m) {
        o = { n: +m[1] };
        gsap.to(o, { n: +m[2], duration: 1.3, ease: 'power2.inOut', scrollTrigger: { trigger: b, start: 'top 90%', once: true },
          onUpdate: function () { b.textContent = m[1] + 'h → ' + Math.round(o.n) + 'h'; }, onComplete: function () { b.textContent = original; } });
      }
    });
  }

  function processSection() {
    var steps = $('.steps'), items = $$('.steps > div');
    if (!steps) return;
    var mm = gsap.matchMedia();
    mm.add('(min-width: 981px) and (min-height: 620px)', function () {
      var line = el('i', 'steps-line', null, steps);
      gsap.set(line, { scaleX: 0, transformOrigin: '0 50%' });
      gsap.set(items, { autoAlpha: .22, y: 28 });
      var tl = gsap.timeline({ scrollTrigger: { trigger: '#process', start: 'top top+=70', end: '+=110%', pin: true, scrub: .6, anticipatePin: 1 } });
      tl.to(line, { scaleX: 1, duration: 4, ease: 'none' }, 0);
      items.forEach(function (it, i) { tl.to(it, { autoAlpha: 1, y: 0, duration: .7, ease: 'power2.out' }, i * .95 + .1); });
      return function () { line.remove(); };
    });
    mm.add('(max-width: 980px), (max-height: 619px)', function () {
      items.forEach(function (it) { gsap.from(it, { y: 34, autoAlpha: 0, duration: .75, ease: EASE, scrollTrigger: { trigger: it, start: 'top 88%', once: true } }); });
    });
  }

  function founder() {
    var img = $('.founder img');
    if (!img) return;
    gsap.fromTo(img, { clipPath: 'inset(100% 0 0 0)', scale: 1.08 }, { clipPath: 'inset(0% 0 0 0)', scale: 1, duration: 1.15, ease: 'expo.inOut', scrollTrigger: { trigger: img, start: 'top 85%', once: true } });
    gsap.from('.founder .role, .founder p, .founder .cta-row > *', { y: 18, autoAlpha: 0, duration: .65, ease: EASE, stagger: .08, scrollTrigger: { trigger: '.founder', start: 'top 72%', once: true } });
  }

  function finalSection() {
    var f = $('.final');
    if (!f) return;
    gsap.fromTo(f, { clipPath: 'inset(0% 7% 0% 7% round 28px)' }, { clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'none', scrollTrigger: { trigger: f, start: 'top bottom', end: 'top 45%', scrub: true } });
    gsap.from('.final .cta-row > *', { y: 20, autoAlpha: 0, duration: .65, ease: EASE, stagger: .1, scrollTrigger: { trigger: '.final .cta-row', start: 'top 92%', once: true } });
  }

  function chrome() {
    var bar = $('.nav .accent-bar');
    if (bar) {
      var fill = el('i', 'scroll-progress', null, bar);
      gsap.set(fill, { scaleX: 0, transformOrigin: '0 50%' });
      gsap.to(fill, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .25 } });
    }
    var nav = $('.nav');
    if (nav) ScrollTrigger.create({ start: 80, end: 'max', toggleClass: { targets: nav, className: 'is-scrolled' } });
  }

  function pointerMotion() {
    gsap.matchMedia().add('(hover: hover) and (pointer: fine) and (min-width: 981px)', function () {
      $$('.hero .btn, .final .btn').forEach(function (b) {
        var x = gsap.quickTo(b, 'x', { duration: .45, ease: 'power3' }), y = gsap.quickTo(b, 'y', { duration: .45, ease: 'power3' });
        b.addEventListener('pointermove', function (e) { var c = b.getBoundingClientRect(); x((e.clientX - c.left - c.width / 2) * .16); y((e.clientY - c.top - c.height / 2) * .28); });
        b.addEventListener('pointerleave', function () { x(0); y(0); });
      });
      $$('.pcard, .ps article').forEach(function (c) {
        var rx = gsap.quickTo(c, 'rotationX', { duration: .5, ease: 'power3' }), ry = gsap.quickTo(c, 'rotationY', { duration: .5, ease: 'power3' });
        gsap.set(c, { transformPerspective: 1100 });
        c.addEventListener('pointermove', function (e) { var b = c.getBoundingClientRect(); ry(((e.clientX - b.left) / b.width - .5) * 4); rx(((e.clientY - b.top) / b.height - .5) * -4); });
        c.addEventListener('pointerleave', function () { rx(0); ry(0); });
      });
      var hero = $('.hero'), net = $('.hero-net');
      if (hero && net) {
        var nx = gsap.quickTo(net, 'x', { duration: 1.1, ease: 'power3' });
        hero.addEventListener('pointermove', function (e) { nx((e.clientX / window.innerWidth - .5) * -18); });
      }
    });
  }

  /* ---------- Boot ---------- */
  var demo = $('#deskDemo'), refs = demo ? buildDesk(demo) : null;
  var mm = gsap.matchMedia();
  mm.add('(prefers-reduced-motion: reduce)', function () {
    unhide();
    if (refs) staticDesk(demo, refs);
  });
  mm.add('(prefers-reduced-motion: no-preference)', function () {
    demo.classList.remove('is-idle');
    var desk = refs ? animateDesk(demo, refs) : null;
    var started = false;
    var start = function () { started = true; desk.play(); };
    heroConstellation($('.hero'));
    heroIntro(function () {});
    if (desk) {
      gsap.delayedCall(1, start);
      ScrollTrigger.create({ trigger: demo, start: 'top bottom', end: 'bottom top', onToggle: function (s) { if (started) { if (s.isActive) desk.play(); else desk.pause(); } } });
    }
    chrome(); revealHeadings(); marquees(); cards(); study(); processSection(); founder(); finalSection(); pointerMotion();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  });
})();
