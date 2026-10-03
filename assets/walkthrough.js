/* Goldfib 5-step research walkthrough. Opens as a modal from any [data-walkthrough-open] element,
   or mounts inline inside [data-walkthrough-inline]. Figures follow the illustrative defaults used in
   "What a research desk really costs" and "AI & research automation". */
(function () {
  var GOLD = '#b8965a', BLUE = '#60a5fa', GREEN = '#34d399', PINK = '#f472b6', SUB = '#8b919e', INK = '#132338';
  var SEAT = { salary: 22, data: 6, over: 6.6 }, REVIEW = 12, TOOLS = 4, MANUAL = 12, AUTO = 24;
  var FOCUS = {
    large: ['Large caps', '/blog/institutional-grade-equity-research-india/', "What 'institutional-grade' really means"],
    small: ['Small & mid caps', '/blog/coverage-gap-indian-small-caps/', 'The small-cap coverage gap'],
    unlisted: ['Unlisted & pre-IPO', '/blog/pre-ipo-unlisted-shares-due-diligence-india/', 'Pre-IPO & unlisted share diligence']
  };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var inr = function (l) { return l >= 100 ? '₹' + (l / 100).toFixed(2) + ' cr' : '₹' + l.toFixed(1) + ' L'; };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  var CSS =
    '#wt-modal{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:12px;background:rgba(6,12,22,.78);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);opacity:0;pointer-events:none;transition:opacity .3s}' +
    '#wt-modal.on{opacity:1;pointer-events:auto}' +
    '.wt-card{position:relative;width:100%;max-width:680px;background:var(--bg-elevated,#1a2c45);border:1px solid rgba(184,150,90,.32);border-radius:18px;color:var(--text-primary,#e8e4dc);box-shadow:0 30px 90px rgba(0,0,0,.45);font-family:Outfit,system-ui,sans-serif;line-height:1.6}' +
    '#wt-modal .wt-card{max-height:92vh;overflow-y:auto;transform:translateY(24px) scale(.97);transition:transform .45s cubic-bezier(.2,.8,.2,1)}#wt-modal.on .wt-card{transform:none}' +
    '.wt-in{padding:30px 34px}.wt-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}' +
    '.wt-x{width:36px;height:36px;border-radius:50%;border:0;background:transparent;color:var(--text-secondary,#a3a9b5);font-size:26px;line-height:1;cursor:pointer}.wt-x:hover{background:rgba(255,255,255,.08);color:#fff}' +
    '[data-walkthrough-inline] .wt-x{display:none}' +
    '.wt-dots{display:flex;gap:6px;margin-bottom:26px}.wt-dot{height:4px;flex:1;border-radius:4px;background:rgba(255,255,255,.12);transition:background .4s}.wt-dot.on{background:' + GOLD + '}' +
    '.wt-step{display:none}.wt-step.on{display:block;animation:wtIn .45s ease-out}@keyframes wtIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}' +
    '.wt-k{font-family:"JetBrains Mono",monospace;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--text-muted,#6c7586);margin-bottom:6px}' +
    '.wt-step h3{font-family:"Space Grotesk",sans-serif;font-size:clamp(1.5rem,4vw,2rem);line-height:1.2;letter-spacing:-.02em;margin-bottom:10px}' +
    '.wt-step>p{color:var(--text-secondary,#a3a9b5);font-weight:300;font-size:.95rem;margin-bottom:18px}.wt-step b{color:var(--text-primary,#e8e4dc);font-weight:600}' +
    '.wt-chart{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:10px}.wt-chart svg{width:100%;height:auto;display:block}' +
    '.wt-nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-top:16px}' +
    '.wt-num{padding:14px;border-radius:10px;background:rgba(255,255,255,.04)}.wt-num.hl{background:rgba(184,150,90,.1);border:1px solid rgba(184,150,90,.32)}' +
    '.wt-num span{display:block;font-family:"JetBrains Mono",monospace;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--text-muted,#6c7586);margin-bottom:4px}.wt-num.hl span{color:' + GOLD + '}' +
    '.wt-num b{font-family:"Space Grotesk",sans-serif;font-size:1.5rem;font-variant-numeric:tabular-nums}.wt-num.hl b{color:' + GOLD + '}' +
    '.wt-note{margin-top:14px;font-size:.9rem;color:var(--text-secondary,#a3a9b5)}.wt-note b{color:' + GOLD + '}' +
    '.wt-field{display:block;font-size:.8rem;color:var(--text-secondary,#a3a9b5);margin-bottom:16px}.wt-field output{float:right;font-family:"JetBrains Mono",monospace;color:#fff}' +
    '.wt-field input[type=range]{width:100%;accent-color:' + GOLD + ';margin-top:8px}' +
    '.wt-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}.wt-chip{border:1px solid rgba(255,255,255,.14);background:transparent;color:var(--text-primary,#e8e4dc);padding:8px 14px;border-radius:999px;font:inherit;font-size:.82rem;cursor:pointer;transition:all .2s}' +
    '.wt-chip:hover{border-color:' + GOLD + '}.wt-chip.on{background:' + GOLD + ';border-color:' + GOLD + ';color:#0c1220;font-weight:600}' +
    '.wt-text{width:100%;padding:12px 14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);border-radius:8px;color:#fff;font:inherit;margin-bottom:10px}.wt-text:focus{outline:none;border-color:' + GOLD + '}' +
    '.wt-go{width:100%;margin-top:6px;background:' + GOLD + ';color:#0c1220;border:0;border-radius:8px;padding:15px;font:inherit;font-size:.78rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;cursor:pointer;transition:background .2s}.wt-go:hover{background:#d4b47a}' +
    '.wt-nav{display:none;justify-content:space-between;align-items:center;margin-top:24px}.wt-nav.on{display:flex}' +
    '.wt-back{background:none;border:0;color:var(--text-secondary,#a3a9b5);font:inherit;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;cursor:pointer}.wt-back:hover{color:#fff}' +
    '.wt-next{background:' + GOLD + ';color:#0c1220;border:0;border-radius:8px;padding:12px 22px;font:inherit;font-size:.74rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;cursor:pointer}' +
    '.wt-fine{font-size:.68rem;color:var(--text-muted,#6c7586);line-height:1.6;margin-top:22px}' +
    '.wt-done{display:none}.wt-done.on{display:block}.wt-done a{display:block;padding:10px 0;border-top:1px solid rgba(255,255,255,.07);color:' + GOLD + ';font-size:.9rem}' +
    '.wt-draw{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:wtDraw 1.4s cubic-bezier(.2,.8,.2,1) forwards;animation-delay:var(--d,0s)}@keyframes wtDraw{to{stroke-dashoffset:0}}' +
    '.wt-fade{opacity:0;animation:wtFade .6s ease-out forwards;animation-delay:var(--d,1s)}@keyframes wtFade{to{opacity:1}}' +
    '.wt-grow{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation:wtGrow .9s cubic-bezier(.2,.8,.2,1) forwards;animation-delay:var(--d,0s)}@keyframes wtGrow{to{transform:scaleX(1)}}' +
    '.wt-pulse{animation:wtPulse 2.4s ease-in-out infinite;animation-delay:var(--d,0s)}@keyframes wtPulse{0%,100%{opacity:.35}50%{opacity:1}}' +
    '#wt-nudge{position:fixed;right:20px;bottom:20px;z-index:9997;max-width:300px;background:var(--bg-elevated,#1a2c45);border:1px solid rgba(184,150,90,.4);border-radius:14px;padding:18px 20px;box-shadow:0 20px 60px rgba(0,0,0,.45);color:var(--text-primary,#e8e4dc);font-family:Outfit,sans-serif;transform:translateY(20px);opacity:0;transition:all .4s}' +
    '#wt-nudge.on{transform:none;opacity:1}#wt-nudge p{font-size:.88rem;margin:6px 0 14px;line-height:1.5}#wt-nudge .wt-x{position:absolute;top:6px;right:6px;width:28px;height:28px;font-size:20px}' +
    '#wt-nudge button.wt-next{padding:10px 16px}' +
    '@media(max-width:600px){.wt-in{padding:22px 18px}#wt-nudge{left:16px;right:16px;max-width:none}}' +
    '@media(prefers-reduced-motion:reduce){.wt-draw,.wt-fade,.wt-grow,.wt-step.on,.wt-pulse{animation:none!important;opacity:1;transform:none;stroke-dashoffset:0}}';

  var HTML =
    '<div class="wt-in"><div class="wt-top"><span class="eyebrow">Goldfib · 5-step research walkthrough</span><button class="wt-x" data-wt-close aria-label="Close">&times;</button></div>' +
    '<div class="wt-dots">' + '<span class="wt-dot"></span>'.repeat(5) + '</div>' +

    '<section class="wt-step" data-s="1"><p class="wt-k">Step 1 of 5 · Your coverage</p><h3>How many companies do you want covered properly?</h3>' +
    '<p>We\'ll price an in-house research desk for that list, show where analyst hours go, and what changes when the mechanical work is automated.</p>' +
    '<label class="wt-field">Companies to cover <output id="wt-n-o"></output><input id="wt-n" type="range" min="4" max="60" step="1" value="20"></label>' +
    '<div class="wt-field">Where they sit<div class="wt-chips" id="wt-focus"><button type="button" class="wt-chip" data-v="large">Large caps</button><button type="button" class="wt-chip on" data-v="small">Small &amp; mid caps</button><button type="button" class="wt-chip" data-v="unlisted">Unlisted &amp; pre-IPO</button></div></div>' +
    '<button class="wt-go" data-wt-start>Start the walkthrough</button></section>' +

    '<section class="wt-step" data-s="2"><p class="wt-k">Step 2 of 5 · The in-house desk</p><h3>What it costs to cover <span class="wt-N"></span> companies yourself</h3>' +
    '<p>At about 12 full reports per analyst a year, you need <b class="wt-man"></b>. Salaries are only part of the bill: data seats, overheads and a senior reviewer\'s time come with every desk.</p>' +
    '<div class="wt-chart" data-chart="cost"></div>' +
    '<div class="wt-nums"><div class="wt-num"><span>Desk cost / year</span><b data-count="desk"></b></div><div class="wt-num hl"><span>Cost per report</span><b data-count="cprM"></b></div></div></section>' +

    '<section class="wt-step" data-s="3"><p class="wt-k">Step 3 of 5 · Where the hours go</p><h3>Half the analyst\'s week is mechanical</h3>' +
    '<p>Collecting filings, extracting tables and updating models take about 27 of 50 hours. Automate that layer and analysis time rises from 8 to 20 hours, with 6 hours of verification added.</p>' +
    '<div class="wt-chart" data-chart="hours"></div>' +
    '<div class="wt-nums"><div class="wt-num"><span>Analysts, manual</span><b data-count="nM"></b></div><div class="wt-num hl"><span>Analysts, automated</span><b data-count="nA"></b></div></div></section>' +

    '<section class="wt-step" data-s="4"><p class="wt-k">Step 4 of 5 · Cost per report</p><h3>Throughput is the biggest cost lever</h3>' +
    '<p>Fixed costs dominate small desks. The gold line is the same coverage with automation doing collection and extraction, so each analyst finishes about twice as many reports.</p>' +
    '<div class="wt-chart" data-chart="curve"></div>' +
    '<div class="wt-nums"><div class="wt-num"><span>Manual desk</span><b data-count="cprM"></b></div><div class="wt-num hl"><span>Automated desk</span><b data-count="cprA"></b></div></div>' +
    '<p class="wt-note">For your <span class="wt-N"></span> companies that is <b class="wt-save"></b> less per report, before any change in quality.</p></section>' +

    '<section class="wt-step" data-s="5"><p class="wt-k">Step 5 of 5 · Your research plan</p><h3>What a year of coverage looks like</h3>' +
    '<p>Every filing flows through the same pipeline. Machines do the volume work; a person signs off wherever a number becomes a decision.</p>' +
    '<div class="wt-chart" data-chart="pipe"></div>' +
    '<div class="wt-nums"><div class="wt-num hl"><span>Initiation reports</span><b data-count="N"></b></div><div class="wt-num"><span>Quarterly result notes</span><b data-count="q"></b></div><div class="wt-num"><span>Pledge &amp; holding checks</span><b data-count="q"></b></div></div>' +
    '<form id="wt-form" style="margin-top:20px"><input class="wt-text" name="name" placeholder="Your name"><input class="wt-text" name="org" placeholder="Family office / fund / organisation">' +
    '<button type="submit" class="wt-go">Email this plan to Goldfib</button></form>' +
    '<div class="wt-done"><p class="wt-note">Your email app should have opened with the plan filled in. If it didn\'t, write to <b>partners@goldfibcapital.in</b>. Meanwhile, read more:</p>' +
    '<a class="wt-focus-link" href="#"></a><a href="/blog/research-desk-cost-india/">What a research desk really costs →</a><a href="/blog/ai-investment-research-automation-india/">AI &amp; research automation: what works →</a></div></section>' +

    '<div class="wt-nav"><button class="wt-back" data-wt-back>← Back</button><button class="wt-next" data-wt-next>Next →</button></div>' +
    '<p class="wt-fine">Illustrative model, not a quote or a benchmark. Assumes ₹22 L CTC, ₹6 L data and 30% overheads per analyst seat, 15% of an ₹80 L portfolio manager\'s time for review, 12 full reports per analyst a year manually and 24 with automation, plus ₹4 L a year of tooling for the automated desk. Replace the inputs with your own.</p></div>';

  var card, wrap, step = 1, d = {}, inline = false;

  function model() {
    var N = +$('#wt-n', card).value, focus = ($('.wt-chip.on', card) || {}).dataset.v || 'small';
    var desk = function (n, tools) { return n * (SEAT.salary + SEAT.data + SEAT.over) + REVIEW + (tools ? TOOLS : 0); };
    var nM = Math.ceil(N / MANUAL), nA = Math.ceil(N / AUTO);
    d = { N: N, focus: focus, nM: nM, nA: nA, desk: desk(nM), deskA: desk(nA, 1), q: N * 4, deskFn: desk };
    d.cprM = d.desk / N; d.cprA = d.deskA / N;
  }

  function count(el, to, f) {
    if (reduce) { el.textContent = f(to); return; }
    var t0 = performance.now();
    (function tick(t) { var k = Math.min(1, (t - t0) / 1100); el.textContent = f(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(tick); })(t0);
  }

  // charts
  var W = 600, H = 250, NARROW = false;
  function svg(inner, h) { return '<svg viewBox="0 0 ' + W + ' ' + (h || H) + '" font-family="Outfit,sans-serif">' + inner + '</svg>'; }
  function txt(x, y, s, c, o) { o = o || {}; return '<text x="' + x + '" y="' + y + '" fill="' + c + '" font-size="' + (o.size || 12) + '"' + (o.anchor ? ' text-anchor="' + o.anchor + '"' : '') + (o.cls ? ' class="' + o.cls + '" style="--d:' + o.d + 's"' : '') + '>' + s + '</text>'; }

  function chartCost() {
    var segs = [['Salaries', SEAT.salary * d.nM, GOLD], ['Data & tools', SEAT.data * d.nM, BLUE], ['Overheads', SEAT.over * d.nM, PINK], ['Senior review', REVIEW, GREEN]];
    var x = 20, full = W - 40, s = '', lx = 20;
    segs.forEach(function (g, i) {
      var w = full * g[1] / d.desk;
      s += '<rect class="wt-grow" style="--d:' + (i * .25) + 's" x="' + x + '" y="40" width="' + Math.max(1, w - 2) + '" height="56" rx="4" fill="' + g[2] + '"/>';
      if (w > 60) s += txt(x + 10, 74, inr(g[1]), INK, { size: 13, cls: 'wt-fade', d: .4 + i * .25 });
      x += w;
    });
    s += txt(20, 26, 'Annual cost of a ' + d.nM + '-analyst desk', SUB);
    s += txt(W - 20, 26, inr(d.desk) + ' / yr', '#fff', { anchor: 'end', size: 13, cls: 'wt-fade', d: 1.2 });
    segs.forEach(function (g, i) {
      var col = i % 2, row = Math.floor(i / 2), xx = 20 + col * (W / 2 - 10), yy = 136 + row * 32;
      s += '<g class="wt-fade" style="--d:' + (.6 + i * .15) + 's"><rect x="' + xx + '" y="' + (yy - 11) + '" width="12" height="12" rx="3" fill="' + g[2] + '"/>' + txt(xx + 20, yy, g[0] + ' · ' + Math.round(g[1] / d.desk * 100) + '%', '#d3d0c9', { size: 13 }) + '</g>';
    });
    s += txt(20, 222, 'Salaries are only ' + Math.round(SEAT.salary * d.nM / d.desk * 100) + '% of the bill.' + (NARROW ? '' : ' The rest is easy to leave out of a budget.'), SUB, { cls: 'wt-fade', d: 1.4 });
    return svg(s, 236);
  }

  function chartHours() {
    var series = [['Collection & extraction', GOLD], ['Model updating', BLUE], ['Reading', SUB], ['Analysis & thesis', GREEN], ['Writing', PINK], ['Verification', '#a78bfa']];
    var rows = [['Before', [20, 7, 9, 8, 6, 0]], ['After', [4, 2, 10, 20, 8, 6]]], L = 70, full = W - L - 20, s = '';
    rows.forEach(function (r, ri) {
      var x = L, y = 22 + ri * 64;
      s += txt(0, y + 28, r[0], '#d3d0c9', { size: 13 });
      r[1].forEach(function (v, i) {
        if (!v) return;
        var w = full * v / 50;
        s += '<rect class="wt-grow" style="--d:' + (ri * .6 + i * .12) + 's" x="' + x + '" y="' + y + '" width="' + Math.max(1, w - 2) + '" height="40" rx="4" fill="' + series[i][1] + '"/>';
        if (w > 30) s += txt(x + w / 2 - 1, y + 25, v + 'h', INK, { size: 12, anchor: 'middle', cls: 'wt-fade', d: .5 + ri * .6 + i * .12 });
        x += w;
      });
    });
    var cols = NARROW ? 2 : 3;
    series.forEach(function (g, i) {
      var col = i % cols, row = Math.floor(i / cols), xx = col * (W / cols), yy = 176 + row * 26;
      s += '<g class="wt-fade" style="--d:' + (1 + i * .1) + 's"><rect x="' + xx + '" y="' + (yy - 10) + '" width="11" height="11" rx="3" fill="' + g[1] + '"/>' + txt(xx + 18, yy, g[0], '#d3d0c9', { size: 12 }) + '</g>';
    });
    return svg(s, 176 + Math.ceil(6 / cols) * 26 + 4);
  }

  function chartCurve() {
    var L = 58, R = 18, T = 20, B = 36, a = 4, b = 60, lo = 0, hi = 0, xs = [];
    for (var n = a; n <= b; n++) { xs.push(n); hi = Math.max(hi, d.deskFn(Math.ceil(n / MANUAL)) / n); }
    hi = Math.ceil(hi / 2) * 2;
    var sx = function (v) { return L + (v - a) / (b - a) * (W - L - R); }, sy = function (v) { return H - B - (v - lo) / (hi - lo) * (H - T - B); };
    var path = function (per, tools) { return 'M' + xs.map(function (n) { return sx(n).toFixed(1) + ',' + sy(d.deskFn(Math.ceil(n / per), tools) / n).toFixed(1); }).join('L'); };
    var s = '';
    for (var i = 0; i <= 4; i++) { var v = lo + (hi - lo) * i / 4, y = sy(v); s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y + '" y2="' + y + '" stroke="rgba(255,255,255,.06)"/>' + txt(L - 8, y + 4, '₹' + v.toFixed(0) + 'L', SUB, { size: 11, anchor: 'end' }); }
    [4, 12, 24, 36, 48, 60].forEach(function (n) { s += txt(sx(n), H - B + 18, n, SUB, { size: 11, anchor: 'middle' }); });
    s += txt(W - R, H - 4, 'companies covered →', SUB, { size: 11, anchor: 'end' });
    s += '<path class="wt-draw" style="--l:2400" d="' + path(MANUAL) + '" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="2" stroke-linejoin="round"/>';
    s += '<path class="wt-draw" style="--l:2400;--d:.35s" d="' + path(AUTO, 1) + '" fill="none" stroke="' + GOLD + '" stroke-width="3" stroke-linejoin="round"/>';
    var mx = sx(d.N);
    s += '<g class="wt-fade" style="--d:1.2s"><line x1="' + mx + '" x2="' + mx + '" y1="' + T + '" y2="' + (H - B) + '" stroke="' + GREEN + '" stroke-dasharray="3 4"/>' + txt(mx, T - 4, 'You · ' + d.N, GREEN, { anchor: mx > W - 80 ? 'end' : 'middle' }) + '</g>';
    [[d.cprM, '#fff'], [d.cprA, GOLD]].forEach(function (p, i) { s += '<circle class="wt-fade" style="--d:' + (1.5 + i * .15) + 's" cx="' + mx + '" cy="' + sy(p[0]) + '" r="5.5" fill="' + p[1] + '" stroke="' + INK + '" stroke-width="2"/>'; });
    s += '<g class="wt-fade" style="--d:1.6s">' + txt(W - R, T + 14, '— Manual desk', 'rgba(255,255,255,.7)', { anchor: 'end', size: 12 }) + txt(W - R, T + 32, '— With automation', GOLD, { anchor: 'end', size: 12 }) + '</g>';
    return svg(s);
  }

  function chartPipe() {
    var nodes = [['Filings', 'NSE · BSE · AR'], ['Extract', 'tables, notes'], ['Model', 'drivers, history'], ['Analyst', 'thesis, memo'], ['Review', 'sign-off']];
    var y = 80, gap = (W - 80) / 4, s = '<path id="wt-pipe" d="M40,' + y + ' L' + (W - 40) + ',' + y + '" stroke="rgba(255,255,255,.12)" stroke-width="2"/>';
    s += '<path class="wt-draw" style="--l:600" d="M40,' + y + ' L' + (W - 40) + ',' + y + '" stroke="' + GOLD + '" stroke-width="2"/>';
    nodes.forEach(function (n, i) {
      var x = 40 + i * gap, human = i >= 3;
      s += '<g class="wt-fade" style="--d:' + (.2 + i * .22) + 's"><circle cx="' + x + '" cy="' + y + '" r="22" fill="' + INK + '" stroke="' + (human ? GREEN : GOLD) + '" stroke-width="2"/>' +
        txt(x, y + 5, i + 1, human ? GREEN : GOLD, { size: 14, anchor: 'middle' }) + txt(x, y + 46, n[0], '#fff', { size: 13, anchor: 'middle' }) + (NARROW ? '' : txt(x, y + 63, n[1], SUB, { size: 11, anchor: 'middle' })) + '</g>';
    });
    if (!reduce) for (var k = 0; k < 3; k++) s += '<circle r="4" fill="' + GOLD + '" opacity="0"><set attributeName="opacity" to="1" begin="' + (1.2 + k * 1.2) + 's"/><animateMotion dur="3.6s" begin="' + (1.2 + k * 1.2) + 's" repeatCount="indefinite"><mpath href="#wt-pipe"/></animateMotion></circle>';
    s += '<g class="wt-fade" style="--d:1.4s"><rect x="40" y="16" width="' + (gap * 2 + 22) + '" height="22" rx="11" fill="rgba(184,150,90,.12)"/>' + txt(50 + gap, 31, 'Automated · ' + d.q + (NARROW ? ' filings' : ' filings a year'), GOLD, { size: 11, anchor: 'middle' }) +
      '<rect x="' + (40 + gap * 3 - 22) + '" y="16" width="' + (gap + 44) + '" height="22" rx="11" fill="rgba(52,211,153,.12)"/>' + txt(40 + gap * 3.5, 31, 'Human checkpoints', GREEN, { size: 11, anchor: 'middle' }) + '</g>';
    return svg(s, NARROW ? 150 : 170);
  }

  var CH = { cost: chartCost, hours: chartHours, curve: chartCurve, pipe: chartPipe };
  var FMT = { desk: inr, cprM: inr, cprA: inr, nM: function (v) { return Math.round(v) + ''; }, nA: function (v) { return Math.round(v) + ''; }, N: function (v) { return Math.round(v) + ''; }, q: function (v) { return Math.round(v) + ''; } };

  function fill() {
    $$('.wt-N', card).forEach(function (e) { e.textContent = d.N; });
    $('.wt-man', card).textContent = d.nM + (d.nM === 1 ? ' analyst' : ' analysts');
    $('.wt-save', card).textContent = inr(d.cprM - d.cprA) + ' (' + Math.round((1 - d.cprA / d.cprM) * 100) + '%)';
    var f = FOCUS[d.focus], l = $('.wt-focus-link', card); l.href = f[1]; l.textContent = f[2] + ' →';
  }

  function go(s) {
    step = s;
    $$('.wt-step', card).forEach(function (e) { e.classList.toggle('on', +e.dataset.s === s); });
    $$('.wt-dot', card).forEach(function (e, i) { e.classList.toggle('on', i < s); });
    $('.wt-nav', card).classList.toggle('on', s > 1);
    $('.wt-next', card).style.visibility = s < 5 ? 'visible' : 'hidden';
    var box = $('.wt-step[data-s="' + s + '"]', card), c = $('.wt-chart', box);
    NARROW = card.clientWidth < 520; W = NARROW ? 360 : 600;
    if (c) c.innerHTML = CH[c.dataset.chart]();
    $$('[data-count]', box).forEach(function (e) { var k = e.dataset.count; count(e, d[k], FMT[k]); });
    if (inline) { var top = wrap.getBoundingClientRect().top; if (top < 0 || top > innerHeight * .6) wrap.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }
    else card.scrollTop = 0;
  }

  function open() {
    if (inline) { wrap.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); return; }
    wrap.classList.add('on'); document.body.style.overflow = 'hidden'; hideNudge();
  }
  function close() { if (inline) return; wrap.classList.remove('on'); document.body.style.overflow = ''; }

  var nudge;
  function hideNudge() { if (nudge) nudge.classList.remove('on'); }

  function init() {
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    var host = $('[data-walkthrough-inline]');
    card = document.createElement('div'); card.className = 'wt-card'; card.innerHTML = HTML;
    if (host) { inline = true; wrap = host; host.appendChild(card); }
    else {
      wrap = document.createElement('div'); wrap.id = 'wt-modal'; wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true');
      wrap.setAttribute('aria-label', 'Goldfib research walkthrough'); wrap.appendChild(card); document.body.appendChild(wrap);
    }
    var n = $('#wt-n', card), no = $('#wt-n-o', card), upd = function () { no.textContent = n.value + ' companies'; };
    n.addEventListener('input', upd); upd();
    go(1);

    document.addEventListener('click', function (e) {
      var o = e.target.closest('[data-walkthrough-open]'); if (o) { e.preventDefault(); open(); return; }
      if (e.target.closest('[data-wt-nudge-x]')) { hideNudge(); return; }
      if (!card.contains(e.target)) { if (e.target === wrap) close(); return; }
      var chip = e.target.closest('.wt-chip');
      if (chip) { $$('.wt-chip', card).forEach(function (c) { c.classList.toggle('on', c === chip); }); return; }
      if (e.target.closest('[data-wt-close]')) return close();
      if (e.target.closest('[data-wt-start]')) { model(); fill(); return go(2); }
      if (e.target.closest('[data-wt-next]')) return go(Math.min(5, step + 1));
      if (e.target.closest('[data-wt-back]')) return go(Math.max(1, step - 1));
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

    $('#wt-form', card).addEventListener('submit', function (e) {
      e.preventDefault();
      var f = e.target, who = [f.name.value.trim(), f.org.value.trim()].filter(Boolean).join(', ');
      var body = 'Hi Goldfib team,\n\nI went through the research walkthrough. My numbers:\n\n' +
        '- Companies to cover: ' + d.N + ' (' + FOCUS[d.focus][0] + ')\n' +
        '- In-house desk estimate: ' + d.nM + ' analyst(s), ' + inr(d.desk) + ' a year, ' + inr(d.cprM) + ' per report\n' +
        '- With automation: ' + d.nA + ' analyst(s), ' + inr(d.cprA) + ' per report\n' +
        '- Plan: ' + d.N + ' initiation reports, ' + d.q + ' quarterly result notes, ' + d.q + ' pledge & shareholding checks\n\n' +
        'I would like to talk about a research plan for this list.\n\n' + (who ? who + '\n' : 'Name / organisation:\n');
      location.href = 'mailto:partners@goldfibcapital.in?subject=' + encodeURIComponent('Research plan: ' + d.N + ' companies (' + FOCUS[d.focus][0] + ')') + '&body=' + encodeURIComponent(body);
      f.style.display = 'none'; $('.wt-done', card).classList.add('on');
    });

    if (!inline && /[?&]walkthrough=1/.test(location.search)) setTimeout(open, 400);
    if (!inline) {
      try {
        if (!sessionStorage.getItem('gf_wt_nudge')) {
          nudge = document.createElement('div'); nudge.id = 'wt-nudge';
          nudge.innerHTML = '<button class="wt-x" data-wt-nudge-x aria-label="Close">&times;</button><span class="eyebrow">Interactive guide</span><p>Price a research desk for your coverage list and see what automation changes, in 5 steps.</p><button class="wt-next" data-walkthrough-open>Start the 5 steps</button>';
          document.body.appendChild(nudge);
          setTimeout(function () { if (!wrap.classList.contains('on')) nudge.classList.add('on'); try { sessionStorage.setItem('gf_wt_nudge', '1'); } catch (x) {} }, 90000);
        }
      } catch (x) {}
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
