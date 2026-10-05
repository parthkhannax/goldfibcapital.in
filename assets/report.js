// === Goldfib personalised research plan (ebook) ===
//
// Turns a finished walkthrough into a print-ready A4 e-book: cover, contents and
// introduction, five short chapters on the reader's own numbers, a plan, and
// method + disclosures. Self-contained: logo and charts are inline SVG drawn for
// paper (ink on white, gold = the automated desk), so nothing depends on the page.
//
// Entry points: window.gfReportHTML(d) -> html string, window.gfReport(d) -> print
//   d = { N, org, fteM, fteA, desk, deskA, cprM, cprA, seat:{salary,data,over}, review, tools, manual, auto }
(function () {
  'use strict';
  var INK = '#111418', BODY = '#3a3f47', MUTE = '#6b7079', RULE = '#e4e1da', WASH = '#f6f4ef', GOLD = '#a8843f', GOLDL = '#efe5d0';
  var G = ['#2b2f36', '#5d636c', '#9aa0a8', '#cfd2d6'];

  var esc = function (t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var inr = function (l) { return l >= 100 ? '₹' + (l / 100).toFixed(2) + ' cr' : '₹' + l.toFixed(1) + ' L'; };
  var one = function (v) { return (Math.round(v * 10) / 10).toFixed(1); };
  var W = 640;
  function svg(h, inner, alt) { return '<svg viewBox="0 0 ' + W + ' ' + h + '" role="img" aria-label="' + esc(alt) + '" xmlns="http://www.w3.org/2000/svg" font-family="Inter,Arial,sans-serif">' + inner + '</svg>'; }
  function t(x, y, s, o) { o = o || {}; return '<text x="' + x + '" y="' + y + '" fill="' + (o.c || BODY) + '" font-size="' + (o.s || 12) + '"' + (o.w ? ' font-weight="' + o.w + '"' : '') + (o.a ? ' text-anchor="' + o.a + '"' : '') + '>' + s + '</text>'; }

  // Monochrome mark: paths only, so it can never fall back to a missing font.
  function mark(size, col) {
    return '<svg width="' + size + '" height="' + size + '" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="' + col + '" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="2" y="2" width="60" height="60" rx="10"/><path d="M14 26V20L32 10L50 20V26"/><path d="M22 24v-6M32 24V15M42 24v-6"/><path d="M14 32h36M18 32v16M32 32v16M46 32v16M12 50h40"/></svg>';
  }
  function logo(col, sz) { return '<div class="logo" style="color:' + col + '">' + mark(sz || 30, col) + '<div><b>GOLDFIB</b><span>CAPITAL</span></div></div>'; }

  // ── Model ──────────────────────────────────────────────────────────────
  function build(d) {
    var seat = d.seat.salary + d.seat.data + d.seat.over;
    var m = Object.create(d);
    m.seatCost = seat;
    m.saveYr = d.desk - d.deskA;
    m.savePct = Math.round(m.saveYr / d.desk * 100);
    // Same budget as the in-house desk, spent on the automated desk
    m.nBudget = Math.floor((d.desk - d.review - d.tools) / seat * d.auto);
    m.thesisM = Math.round(d.fteM * 8 * 48); m.thesisA = Math.round(d.fteA * 20 * 48);
    m.mechM = Math.round(d.fteM * 27 * 48); m.mechA = Math.round(d.fteA * 6 * 48);
    return m;
  }

  // ── Charts ─────────────────────────────────────────────────────────────
  function chartCost(m) {
    var rows = [
      ['In-house desk', [m.fteM * m.seat.salary, m.fteM * m.seat.data, m.fteM * m.seat.over, m.review, 0], m.desk, INK],
      ['Automated desk', [m.fteA * m.seat.salary, m.fteA * m.seat.data, m.fteA * m.seat.over, m.review, m.tools], m.deskA, GOLD]];
    var cols = G.concat([GOLD]), names = ['Analyst salaries', 'Data seats', 'Overheads', 'Senior review', 'Automation stack'];
    var L = 120, full = W - L - 92, s = '';
    rows.forEach(function (r, i) {
      var x = L, y = 20 + i * 70;
      s += t(0, y + 22, r[0], { c: INK, w: 600, s: 13 }) + t(0, y + 38, one(i ? m.fteA : m.fteM) + ' analyst FTE', { c: MUTE, s: 11 });
      r[1].forEach(function (v, k) {
        if (v <= 0) return; var w = full * v / m.desk;
        s += '<rect x="' + x + '" y="' + y + '" width="' + Math.max(1, w - 1.5) + '" height="40" fill="' + cols[k] + '"/>';
        if (w > 52) s += t(x + 7, y + 25, inr(v), { c: k < 2 ? '#fff' : INK, s: 11 });
        x += w;
      });
      s += t(x + 8, y + 25, inr(r[2]), { c: r[3], w: 700, s: 14 });
    });
    var x2 = L + full * m.deskA / m.desk;
    s += '<path d="M' + x2 + ' 152 V160 H' + (L + full) + ' V152" stroke="' + GOLD + '" fill="none"/>' +
      t((x2 + L + full) / 2, 176, 'You keep ' + inr(m.saveYr) + ' a year (' + m.savePct + '%)', { c: GOLD, w: 700, s: 12, a: 'middle' });
    names.forEach(function (n, k) { var xx = (k % 3) * 210, yy = 206 + Math.floor(k / 3) * 22; s += '<rect x="' + xx + '" y="' + (yy - 10) + '" width="11" height="11" fill="' + cols[k] + '"/>' + t(xx + 18, yy, n, { s: 11 }); });
    return svg(240, s, 'Annual cost, in-house vs automated desk');
  }

  function chartHours() {
    var rows = [['Collecting & extracting', 20, 4], ['Updating models', 7, 2], ['Reading', 9, 10], ['Analysis & thesis', 8, 20], ['Writing', 6, 8], ['Verification', 0, 6]];
    var L = 168, R = 30, max = 22, sx = function (v) { return L + v / max * (W - L - R); }, s = '';
    [0, 5, 10, 15, 20].forEach(function (v) { s += '<line x1="' + sx(v) + '" x2="' + sx(v) + '" y1="14" y2="226" stroke="' + RULE + '"/>' + t(sx(v), 244, v + 'h', { c: MUTE, s: 10, a: 'middle' }); });
    rows.forEach(function (r, i) {
      var y = 30 + i * 36, up = r[2] > r[1];
      s += t(0, y + 4, r[0], { c: INK, s: 12, w: up ? 600 : 400 });
      s += '<line x1="' + sx(r[1]) + '" x2="' + sx(r[2]) + '" y1="' + y + '" y2="' + y + '" stroke="' + (up ? GOLD : G[2]) + '" stroke-width="3"/>';
      s += '<circle cx="' + sx(r[1]) + '" cy="' + y + '" r="6" fill="#fff" stroke="' + G[1] + '" stroke-width="2"/><circle cx="' + sx(r[2]) + '" cy="' + y + '" r="6.5" fill="' + GOLD + '"/>';
      s += t(sx(r[2]) + (r[2] >= r[1] ? 12 : -12), y + 4, r[2] + 'h', { c: GOLD, w: 700, s: 11, a: r[2] >= r[1] ? 'start' : 'end' });
    });
    s += '<circle cx="' + (L) + '" cy="266" r="5" fill="#fff" stroke="' + G[1] + '" stroke-width="2"/>' + t(L + 10, 270, 'Manual week', { s: 11 }) +
      '<circle cx="' + (L + 120) + '" cy="266" r="5.5" fill="' + GOLD + '"/>' + t(L + 130, 270, 'Automated week', { s: 11 });
    return svg(280, s, 'Hours per task in a 50-hour week, manual vs automated');
  }

  function chartCurve(m) {
    var L = 54, R = 20, T = 16, B = 40, H = 270, a = 4, b = 60, xs = [], hi = 0;
    var cm = function (n) { return (n / m.manual * m.seatCost + m.review) / n; }, ca = function (n) { return (n / m.auto * m.seatCost + m.review + m.tools) / n; };
    for (var n = a; n <= b; n++) { xs.push(n); hi = Math.max(hi, cm(n)); }
    hi = Math.ceil(hi);
    var sx = function (v) { return L + (v - a) / (b - a) * (W - L - R); }, sy = function (v) { return H - B - v / hi * (H - T - B); };
    var line = function (f) { return xs.map(function (n) { return sx(n).toFixed(1) + ',' + sy(f(n)).toFixed(1); }); };
    var pm = line(cm), pa = line(ca), s = '';
    for (var i = 0; i <= 4; i++) { var v = hi * i / 4; s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + sy(v) + '" y2="' + sy(v) + '" stroke="' + RULE + '"/>' + t(L - 8, sy(v) + 4, '₹' + one(v) + 'L', { c: MUTE, s: 10, a: 'end' }); }
    [4, 12, 24, 36, 48, 60].forEach(function (n) { s += t(sx(n), H - B + 18, n, { c: MUTE, s: 10, a: 'middle' }); });
    s += t(W - R, H - 4, 'companies covered', { c: MUTE, s: 10, a: 'end' });
    s += '<path d="M' + pm.join('L') + 'L' + pa.slice().reverse().join('L') + 'Z" fill="' + GOLDL + '"/>';
    s += '<path d="M' + pm.join('L') + '" fill="none" stroke="' + G[1] + '" stroke-width="2" stroke-dasharray="5 4"/>';
    s += '<path d="M' + pa.join('L') + '" fill="none" stroke="' + GOLD + '" stroke-width="3"/>';
    var mx = sx(m.N);
    s += '<line x1="' + mx + '" x2="' + mx + '" y1="' + T + '" y2="' + (H - B) + '" stroke="' + INK + '" stroke-dasharray="2 3"/>';
    s += '<circle cx="' + mx + '" cy="' + sy(m.cprM) + '" r="5" fill="#fff" stroke="' + G[1] + '" stroke-width="2"/><circle cx="' + mx + '" cy="' + sy(m.cprA) + '" r="6" fill="' + GOLD + '"/>';
    var right = mx > W - 190, ax = right ? mx - 10 : mx + 10, an = right ? 'end' : 'start';
    s += t(ax, sy(m.cprM) - 8, 'In-house ' + inr(m.cprM), { c: G[1], s: 11, a: an }) + t(ax, sy(m.cprA) + 18, 'Automated ' + inr(m.cprA), { c: GOLD, w: 700, s: 11, a: an });
    s += t(mx, T - 4 + 0, '', {});
    return svg(H, s, 'Cost per full report by coverage size');
  }

  function chartBudget(m) {
    var panels = [['Full reports a year', m.N, m.nBudget], ['Analyst hours on thesis work', m.thesisM, Math.round(m.thesisA * m.nBudget / m.N)], ['Quarterly result notes', m.N * 4, m.nBudget * 4]];
    var pw = W / 3, s = '';
    panels.forEach(function (p, i) {
      var x = i * pw, max = Math.max(p[1], p[2]), base = 190, hmax = 130;
      var h1 = hmax * p[1] / max, h2 = hmax * p[2] / max;
      s += '<rect x="' + (x + 30) + '" y="' + (base - h1) + '" width="58" height="' + h1 + '" fill="' + G[2] + '"/>' + t(x + 59, base - h1 - 8, p[1], { c: G[1], s: 13, w: 600, a: 'middle' });
      s += '<rect x="' + (x + 100) + '" y="' + (base - h2) + '" width="58" height="' + h2 + '" fill="' + GOLD + '"/>' + t(x + 129, base - h2 - 8, p[2], { c: GOLD, s: 14, w: 700, a: 'middle' });
      s += '<line x1="' + (x + 20) + '" x2="' + (x + pw - 20) + '" y1="' + base + '" y2="' + base + '" stroke="' + INK + '"/>';
      s += t(x + pw / 2 - 12, base + 22, p[0], { c: INK, s: 11.5, w: 600, a: 'middle' }) + t(x + pw / 2 - 12, base + 38, '+' + Math.round((p[2] / p[1] - 1) * 100) + '% with automation', { c: GOLD, s: 11, a: 'middle' });
    });
    s += '<rect x="0" y="252" width="11" height="11" fill="' + G[2] + '"/>' + t(18, 262, 'In-house desk', { s: 11 }) + '<rect x="130" y="252" width="11" height="11" fill="' + GOLD + '"/>' + t(148, 262, 'Automated desk, same budget', { s: 11 });
    return svg(272, s, 'What the same budget buys');
  }

  function chartCumulative(m) {
    var L = 10, s = '', max = m.saveYr * 5, bw = 84, gap = (W - L * 2 - bw * 5) / 4, base = 170;
    for (var y = 1; y <= 5; y++) {
      var v = m.saveYr * y, h = 130 * v / max, x = L + (y - 1) * (bw + gap);
      s += '<rect x="' + x + '" y="' + (base - h) + '" width="' + bw + '" height="' + h + '" fill="' + (y === 5 ? GOLD : GOLDL) + '" stroke="' + GOLD + '"/>';
      s += t(x + bw / 2, base - h - 8, inr(v), { c: y === 5 ? GOLD : INK, w: 700, s: 12, a: 'middle' }) + t(x + bw / 2, base + 18, 'Year ' + y, { c: MUTE, s: 11, a: 'middle' });
    }
    s += '<line x1="0" x2="' + W + '" y1="' + base + '" y2="' + base + '" stroke="' + INK + '"/>';
    return svg(196, s, 'Cumulative savings over five years');
  }

  function chartPipe(m) {
    var nodes = [['Filings', 'NSE · BSE · ARs', 'auto'], ['Extract', 'tables, notes', 'auto'], ['Model', 'drivers, history', 'auto'], ['Verify', 'tie-outs, flags', 'human'], ['Analyst', 'thesis, memo', 'human'], ['Review', 'PM sign-off', 'human']];
    var gap = (W - 80) / 5, y = 64, s = '';
    s += '<rect x="10" y="10" width="' + (gap * 2 + 60) + '" height="22" rx="11" fill="' + GOLDL + '"/>' + t(40 + gap, 25, 'Automated · ' + m.N * 4 + ' filings a year', { c: GOLD, w: 600, s: 11, a: 'middle' });
    s += '<rect x="' + (40 + gap * 3 - 30) + '" y="10" width="' + (gap * 2 + 60) + '" height="22" rx="11" fill="' + WASH + '" stroke="' + RULE + '"/>' + t(40 + gap * 4, 25, 'Human checkpoints', { c: INK, w: 600, s: 11, a: 'middle' });
    s += '<line x1="40" x2="' + (W - 40) + '" y1="' + y + '" y2="' + y + '" stroke="' + RULE + '" stroke-width="2"/>';
    nodes.forEach(function (n, i) {
      var x = 40 + i * gap, auto = n[2] === 'auto';
      s += '<circle cx="' + x + '" cy="' + y + '" r="20" fill="' + (auto ? GOLD : '#fff') + '" stroke="' + (auto ? GOLD : INK) + '" stroke-width="2"/>' + t(x, y + 5, i + 1, { c: auto ? '#fff' : INK, w: 700, s: 13, a: 'middle' });
      s += t(x, y + 42, n[0], { c: INK, w: 600, s: 12, a: 'middle' }) + t(x, y + 58, n[1], { c: MUTE, s: 10, a: 'middle' });
    });
    return svg(136, s, 'The automated research pipeline');
  }

  // ── Book ───────────────────────────────────────────────────────────────
  function html(d) {
    var m = build(d), org = esc(d.org), date = new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' });
    var total = 9, pg = 0;
    var stat = function (k, v, hl) { return '<div class="st' + (hl ? ' hl' : '') + '"><span>' + k + '</span><b>' + v + '</b></div>'; };
    var page = function (body, cls) {
      pg++;
      return '<section class="pg ' + (cls || '') + '">' + (pg > 1 ? '<header>' + logo(INK, 18) + '<span>Research plan · ' + org + '</span><span>' + pg + ' / ' + total + '</span></header>' : '') + body + '</section>';
    };
    var ch = function (n, title, lede) { return '<p class="k">Chapter ' + n + '</p><h1>' + title + '</h1><p class="lede">' + lede + '</p>'; };
    var fig = function (svgs, cap) { return '<figure>' + svgs + '<figcaption>' + cap + '</figcaption></figure>'; };
    var take = function (items) { return '<div class="take"><p class="k">Key takeaways</p><ul>' + items.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul></div>'; };

    var body = '';
    // 1 Cover
    body += page(
      '<div class="cv-top">' + logo(INK, 40) + '<span>' + date + '</span></div>' +
      '<div class="cv-mid"><p class="k">A personalised research plan</p><h1 class="cv-title">Cover ' + m.N + ' companies for ' + m.savePct + '% less.</h1>' +
      '<p class="cv-sub">What an in-house research desk really costs ' + org + ', where the analyst\'s week goes, and how an automated desk delivers more research for less money.</p>' +
      '<div class="cv-rule"></div><p class="cv-for">Prepared for <b>' + org + '</b></p></div>' +
      '<div class="sts cv-sts">' + stat('Saved every year', inr(m.saveYr), 1) + stat('Cost per report', inr(m.cprM) + ' → ' + inr(m.cprA)) + stat('Thesis hours per analyst', '8h → 20h / week') + '</div>' +
      '<p class="cv-foot">Goldfib Capital · goldfibcapital.in</p>', 'cover');

    // 2 Contents + introduction
    body += page(
      '<p class="k">Contents</p><ol class="toc">' +
      ['Introduction', 'The real cost of your research desk', 'Where the analyst\'s week goes', 'Cost per report: the lever that matters', 'What the same budget buys', 'How the automated desk works', 'Your plan and next steps', 'Method, assumptions and disclosures'].map(function (x, i) { return '<li><span>' + x + '</span><i>' + (i + 2) + '</i></li>'; }).join('') + '</ol>' +
      '<p class="k" style="margin-top:9mm">Introduction</p><h1>Most research budgets pay for typing, not thinking.</h1>' +
      '<p>' + org + ' wants ' + m.N + ' Indian companies covered properly: initiation work, a note every quarter, and a watch on promoter pledges and shareholding. The usual answer is to hire analysts. The problem is what those analysts spend their week on.</p>' +
      '<p>We timed a 50-hour analyst week on Indian listed companies. About <b>27 hours</b> go to collecting filings, extracting tables and rolling models forward. Only <b>8 hours</b> go to the thesis, the part you are actually paying for.</p>' +
      '<p>This plan applies that study to your list. Each chapter answers one question, on your numbers: what the desk costs, where the time goes, what each report costs, what the same budget could buy, and how the work gets done with a person signing off every number that matters.</p>' +
      '<div class="call"><b>How to read this plan.</b> Grey is the in-house desk. Gold is the automated desk. Every figure is built from the assumptions on the last page, so you can swap in your own.</div>');

    // 3 Cost
    body += page(ch(1, 'The real cost of your research desk', 'Salaries are the visible part of the bill. Data seats, overheads and a senior reviewer\'s time come with every analyst you hire.') +
      '<p>At about ' + m.manual + ' full reports per analyst a year, covering ' + m.N + ' companies takes <b>' + one(m.fteM) + ' analyst FTE</b>, about <b>' + inr(m.desk) + '</b> a year. Automate the mechanical layer and each analyst completes ' + m.auto + ' reports, so the same list needs <b>' + one(m.fteA) + ' FTE</b>. Even after adding ' + inr(m.tools) + ' a year for the automation stack, the desk costs <b>' + inr(m.deskA) + '</b>.</p>' +
      fig(chartCost(m), 'Annual cost of covering ' + m.N + ' companies. Same review budget on both desks; the automated desk also pays for its tooling.') +
      '<div class="sts">' + stat('In-house desk / year', inr(m.desk)) + stat('Automated desk / year', inr(m.deskA), 1) + stat('Saved / year', inr(m.saveYr) + ' · ' + m.savePct + '%', 1) + '</div>' +
      take(['Analyst seats drive the bill, so analyst throughput drives the saving.', 'The automated desk is cheaper even after paying for its own tooling.', 'The saving grows with every company you add to the list.']));

    // 4 Hours
    body += page(ch(2, 'Where the analyst\'s week goes', 'Half of a manual week is mechanical. Automation hands that time back to analysis, and adds a verification step the manual desk usually skips.') +
      fig(chartHours(), 'One 50-hour analyst week, hours by task. Grey dots: manual. Gold dots: automated.') +
      '<p>Collecting and extracting falls from <b>20 hours to 4</b>, model updates from 7 to 2. Analysis and thesis work rises from <b>8 to 20 hours</b>, and 6 hours of explicit verification are added: tie-outs to the filing, flagged anomalies, a second look before anything reaches the PM.</p>' +
      '<div class="sts">' + stat('Mechanical hours / yr, your desk', m.mechM.toLocaleString('en-IN') + ' → ' + m.mechA.toLocaleString('en-IN'), 1) + stat('Thesis hours per analyst', '2.5× more', 1) + stat('Reports / analyst / yr', m.manual + ' → ' + m.auto, 1) + '</div>' +
      take(['The analyst stops being a data clerk and becomes the decision-maker.', 'Verification is built into the week, not squeezed in at the end.', 'Better research per hour, not just cheaper research.']));

    // 5 Curve
    body += page(ch(3, 'Cost per report: the lever that matters', 'A small desk carries a fixed review cost over few reports. Doubling throughput spreads every rupee over twice the output.') +
      fig(chartCurve(m), 'Cost per full report by coverage size. Dashed grey: in-house. Gold: automated. The shaded gap is the saving at every list size.') +
      '<p>At your ' + m.N + ' companies a full report costs <b>' + inr(m.cprM) + '</b> in-house and <b>' + inr(m.cprA) + '</b> on the automated desk. The gold line sits below the grey one across the whole range, from a 4-company watch-list to a 60-company universe.</p>' +
      '<div class="sts">' + stat('In-house / report', inr(m.cprM)) + stat('Automated / report', inr(m.cprA), 1) + stat('Saved / report', inr(m.cprM - m.cprA), 1) + '</div>' +
      take(['Automation wins at every coverage size on the chart.', 'Per-report cost is the fairest way to compare research options.', 'Use it to benchmark any broker, vendor or hire you consider.']));

    // 6 Budget
    body += page(ch(4, 'What the same budget buys', 'Instead of saving the money, spend the same ' + inr(m.desk) + ' on the automated desk and see how much more research ' + org + ' gets.') +
      fig(chartBudget(m), 'Same annual budget, two desks. Thesis hours scale with analyst FTE at 8h vs 20h a week over 48 weeks.') +
      '<p>The same budget covers <b>' + m.nBudget + ' companies instead of ' + m.N + '</b>. Or keep the list and bank the saving: over five years it adds up to <b>' + inr(m.saveYr * 5) + '</b>.</p>' +
      fig(chartCumulative(m), 'Cumulative saving if ' + org + ' keeps its ' + m.N + '-company list on the automated desk.') +
      take(['Choose: wider coverage, or the same coverage for less.', 'Either way the automated desk produces more research per rupee.']));

    // 7 How it works
    body += page(ch(5, 'How the automated desk works', 'Machines do the volume work. A person signs off wherever a number becomes a decision.') +
      fig(chartPipe(m), 'Every filing for your list flows through the same six steps.') +
      '<div class="two"><div><h3>What is automated</h3><ul><li>Pulling results, annual reports, shareholding and pledge disclosures from NSE and BSE.</li><li>Extracting statements, notes and segment tables into a consistent schema.</li><li>Rolling models forward and flagging changes against your thesis.</li></ul></div>' +
      '<div><h3>What stays human</h3><ul><li>Verification: every extracted number ties out to its source page.</li><li>The thesis, valuation judgement and the memo itself.</li><li>Portfolio manager sign-off before anything is acted on.</li></ul></div></div>' +
      '<div class="call"><b>For ' + org + ' each year:</b> ' + m.N + ' initiation reports, ' + m.N * 4 + ' quarterly result notes and ' + m.N * 4 + ' pledge and shareholding checks, all through this pipeline.</div>');

    // 8 Plan + CTA
    body += page('<p class="k">Chapter 6</p><h1>Your plan and next steps</h1><p class="lede">A short, low-risk way for ' + org + ' to test this on real work before committing.</p>' +
      '<ol class="steps"><li><b>Week 1 · Scoping call.</b> 30 minutes on your ' + m.N + '-company list, live deals and the gaps that matter most.</li>' +
      '<li><b>Weeks 2–3 · Pilot memo.</b> One full report on a company you choose, with every number tied to its filing.</li>' +
      '<li><b>Week 4 · Review.</b> Judge the work against your current research. Compare cost per report on your own numbers.</li>' +
      '<li><b>Month 2 onward · Full coverage.</b> Initiations, quarterly notes and pledge monitoring across the list.</li></ol>' +
      '<div class="cta">' + logo('#fff', 34) + '<h2>Run this on ' + org + '\'s real list.</h2><p>Book a 30-minute scoping call. We will bring this plan and a sample memo.</p>' +
      '<p class="big">partners@goldfibcapital.in<br>goldfibcapital.in</p></div>' +
      '<p class="k" style="margin-top:9mm">Further reading</p><ul class="read"><li>What a research desk really costs — goldfibcapital.in/blog/research-desk-cost-india/</li><li>AI and research automation: what works — goldfibcapital.in/blog/ai-investment-research-automation-india/</li><li>Building a family-office research function — goldfibcapital.in/blog/family-office-research-function-india/</li></ul>');

    // 9 Method
    body += page('<p class="k">Appendix</p><h1>Method, assumptions and disclosures</h1>' +
      '<table><tr><th>Assumption</th><th>Value used</th></tr>' +
      '<tr><td>Analyst CTC</td><td>₹' + m.seat.salary + ' L a year</td></tr><tr><td>Data seats per analyst</td><td>₹' + m.seat.data + ' L a year</td></tr>' +
      '<tr><td>Overheads per analyst (30%)</td><td>₹' + m.seat.over + ' L a year</td></tr><tr><td>Senior review (15% of an ₹80 L PM)</td><td>₹' + m.review + ' L a year, both desks</td></tr>' +
      '<tr><td>Automation stack</td><td>₹' + m.tools + ' L a year, automated desk only</td></tr><tr><td>Full reports per analyst a year</td><td>' + m.manual + ' manual · ' + m.auto + ' automated</td></tr>' +
      '<tr><td>Analyst week</td><td>50 hours, 48 working weeks</td></tr><tr><td>Coverage modelled</td><td>' + m.N + ' companies</td></tr></table>' +
      '<h3>How the numbers are built</h3><p>Analyst need is measured in full-time equivalents (coverage ÷ reports per analyst), so a desk can use part of an analyst\'s time. Desk cost = FTE × seat cost + senior review (+ tooling for the automated desk). Cost per report = desk cost ÷ companies covered.</p>' +
      '<h3>About Goldfib Capital</h3><p>Goldfib Capital builds institutional-grade equity research on Indian listed and unlisted companies for family offices, PMS and AIF managers. Our desk pairs automated filing extraction with analyst judgement and explicit verification.</p>' +
      '<p class="fine">This document is an illustrative model built from stated assumptions. It is not a quote, a benchmark survey, investment advice or an offer of any security. Actual costs depend on scope, coverage and data requirements. Prepared for ' + org + ' on ' + date + '.</p>');

    var css = '@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}body{font:11.5px/1.65 Inter,Arial,sans-serif;color:' + BODY + ';-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#fff}' +
      '.pg{width:210mm;height:297mm;padding:15mm 18mm 14mm;position:relative;page-break-after:always;overflow:hidden}.pg:last-child{page-break-after:auto}' +
      'header{display:flex;align-items:center;gap:12px;font:500 8.5px "JetBrains Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:' + MUTE + ';border-bottom:1px solid ' + RULE + ';padding-bottom:7px;margin-bottom:9mm}header span:last-child{margin-left:auto}header .logo b{font-size:10px}header .logo span{display:none}' +
      '.logo{display:flex;align-items:center;gap:9px}.logo div{display:flex;flex-direction:column;line-height:1}.logo b{font:700 15px "Space Grotesk",Arial,sans-serif;letter-spacing:.06em}.logo span{font:600 7.5px "Space Grotesk",Arial,sans-serif;letter-spacing:.45em;margin-top:3px}' +
      '.k{font:500 9px "JetBrains Mono",monospace;letter-spacing:.18em;text-transform:uppercase;color:' + GOLD + ';margin-bottom:5px}' +
      'h1{font:700 25px/1.18 "Playfair Display",Georgia,serif;color:' + INK + ';margin-bottom:8px}h2{font:700 20px/1.2 "Playfair Display",Georgia,serif;margin:10px 0 6px}h3{font:600 12px "Space Grotesk",Arial,sans-serif;color:' + INK + ';text-transform:uppercase;letter-spacing:.06em;margin:12px 0 5px}' +
      'p{margin-bottom:9px}b{color:' + INK + '}.lede{font:italic 13px/1.6 Georgia,serif;color:' + MUTE + ';border-left:3px solid ' + GOLD + ';padding-left:12px;margin-bottom:12px}' +
      'figure{margin:10px 0 12px;padding:12px 14px 10px;border:1px solid ' + RULE + ';border-radius:6px}figure svg{width:100%;height:auto;display:block}figcaption{font-size:9.5px;color:' + MUTE + ';margin-top:6px;border-top:1px solid ' + RULE + ';padding-top:6px}' +
      '.sts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:10px 0}.st{border:1px solid ' + RULE + ';border-radius:6px;padding:9px 11px}.st.hl{background:' + GOLDL + ';border-color:' + GOLD + '}' +
      '.st span{display:block;font:500 8px "JetBrains Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:' + MUTE + ';margin-bottom:3px}.st b{font:600 15px "Space Grotesk",Arial,sans-serif;color:' + INK + '}.st.hl b{color:#7a5d24}' +
      '.take{background:' + WASH + ';border-left:3px solid ' + INK + ';padding:10px 14px;margin-top:10px}.take ul{list-style:none}.take li{padding-left:16px;position:relative;margin:3px 0}.take li:before{content:"→";position:absolute;left:0;color:' + GOLD + ';font-weight:700}' +
      '.call{background:' + GOLDL + ';border-radius:6px;padding:11px 14px;margin:10px 0}' +
      'ul,ol{margin:4px 0 8px 16px}li{margin:3px 0}.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}' +
      '.toc{list-style:none;margin:6px 0 0}.toc li{display:flex;justify-content:space-between;border-bottom:1px dotted #c9c5bc;padding:6px 0;font:500 12.5px "Space Grotesk",Arial,sans-serif;color:' + INK + '}.toc i{font-style:normal;color:' + GOLD + '}' +
      '.steps li{margin:8px 0;padding-left:4px}.cta{background:' + INK + ';color:#d8d4cc;border-radius:8px;padding:12mm;margin-top:8mm}.cta h2{color:#fff;margin-top:14px}.cta .big{font:600 16px/1.6 "Space Grotesk",Arial,sans-serif;color:#e2c88f;margin:10px 0 0}' +
      '.read{list-style:none;margin-left:0;font-size:10.5px}table{width:100%;border-collapse:collapse;margin:10px 0 6px;font-size:11px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid ' + RULE + '}th{font:500 8.5px "JetBrains Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:' + MUTE + '}' +
      '.fine{font-size:9px;color:' + MUTE + ';border-top:1px solid ' + RULE + ';padding-top:8px;margin-top:10px}' +
      '.cover{display:flex;flex-direction:column;padding:18mm 20mm}.cv-top{display:flex;justify-content:space-between;align-items:center;font:500 9px "JetBrains Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:' + MUTE + ';border-bottom:1px solid ' + INK + ';padding-bottom:10px}' +
      '.cv-mid{margin-top:42mm}.cv-title{font-size:44px;line-height:1.08;margin:8px 0 14px}.cv-sub{font:15px/1.6 Georgia,serif;color:' + BODY + ';max-width:150mm}.cv-rule{width:44px;height:3px;background:' + GOLD + ';margin:16px 0}.cv-for{font:500 13px "Space Grotesk",Arial,sans-serif}' +
      '.cv-sts{margin-top:auto}.cv-sts .st b{font-size:17px}.cv-foot{font:500 9px "JetBrains Mono",monospace;letter-spacing:.14em;text-transform:uppercase;color:' + MUTE + ';margin-top:8mm;border-top:1px solid ' + RULE + ';padding-top:8px}';
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Goldfib Capital - Research plan for ' + org + '</title>' +
      '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">' +
      '<style>' + css + '</style></head><body>' + body + '</body></html>';
  }

  function print(d) {
    var page = html(d);
    var old = document.getElementById('wt-print'); if (old) old.remove();
    var f = document.createElement('iframe'); f.id = 'wt-print'; f.setAttribute('aria-hidden', 'true');
    f.style.cssText = 'position:fixed;right:0;bottom:0;width:0;height:0;border:0;visibility:hidden';
    document.body.appendChild(f);
    var doc = f.contentWindow.document; doc.open(); doc.write(page); doc.close();
    var done = false, go = function () {
      if (done) return; done = true; var t0 = document.title; document.title = 'Goldfib Capital - Research plan for ' + d.org;
      f.contentWindow.focus(); f.contentWindow.print(); setTimeout(function () { document.title = t0; }, 1000);
    };
    (doc.fonts && doc.fonts.ready ? doc.fonts.ready : Promise.resolve()).then(function () { setTimeout(go, 300); });
    setTimeout(go, 3000);
  }
  window.gfReportHTML = html;
  window.gfReport = print;
})();
