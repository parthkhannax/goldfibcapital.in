/* Interactive calculators for Goldfib articles. Each <figure data-widget="name"> gets wired up here. */
(function () {
  var GOLD = '#b8965a', BLUE = '#60a5fa', GREEN = '#34d399', PINK = '#f472b6', SUB = '#8b919e';
  var inr = function (lakh) { return lakh >= 100 ? '₹' + (lakh / 100).toFixed(2) + ' cr' : '₹' + lakh.toFixed(1) + ' L'; };

  function sliders(el, defs, onChange) {
    var box = document.createElement('div'); box.className = 'w-inputs';
    var vals = {};
    defs.forEach(function (d) {
      var l = document.createElement('label');
      l.innerHTML = d.label + ' <b></b><input type="range" min="' + d.min + '" max="' + d.max + '" step="' + (d.step || 1) + '" value="' + d.value + '">';
      var inp = l.querySelector('input'), out = l.querySelector('b');
      var upd = function () { vals[d.key] = +inp.value; out.textContent = d.fmt ? d.fmt(+inp.value) : inp.value; };
      inp.addEventListener('input', function () { upd(); onChange(vals); });
      upd(); box.appendChild(l);
    });
    el.appendChild(box);
    return vals;
  }

  function hbars(items, max) {
    var h = items.length * 38 + 6, s = '<svg viewBox="0 0 400 ' + h + '">';
    items.forEach(function (it, i) {
      var w = Math.max(2, 200 * it.v / max), y = i * 38 + 4;
      s += '<text x="0" y="' + (y + 19) + '" font-size="12" fill="' + SUB + '" font-family="Outfit">' + it.label + '</text>' +
        '<rect x="110" y="' + (y + 5) + '" width="' + w + '" height="22" rx="4" fill="' + it.c + '"/>' +
        '<text x="' + (116 + w) + '" y="' + (y + 21) + '" font-size="12" fill="#e8e4dc" font-family="JetBrains Mono">' + it.t + '</text>';
    });
    return s + '</svg>';
  }

  var W = {};

  /* In-house research desk: what one report really costs */
  W['desk-cost'] = function (el) {
    var out = document.createElement('div'); out.className = 'w-out';
    var v = sliders(el, [
      { key: 'n', label: 'Analysts on the desk', min: 1, max: 6, value: 2 },
      { key: 'ctc', label: 'CTC per analyst (₹ lakh/yr)', min: 8, max: 60, value: 22 },
      { key: 'data', label: 'Data &amp; tools per seat (₹ lakh/yr)', min: 0, max: 30, value: 6 },
      { key: 'ovh', label: 'Office, hiring &amp; attrition (% of CTC)', min: 0, max: 60, value: 30, fmt: function (x) { return x + '%'; } },
      { key: 'rev', label: 'Senior review time (% of a PM at ₹80L)', min: 0, max: 50, value: 15, fmt: function (x) { return x + '%'; } },
      { key: 'rpt', label: 'Full reports per analyst per year', min: 4, max: 40, value: 12 }
    ], draw);
    el.appendChild(out);
    function draw() {
      var sal = v.n * v.ctc, dat = v.n * v.data, ovh = sal * v.ovh / 100, rev = 80 * v.rev / 100;
      var tot = sal + dat + ovh + rev, per = tot / (v.n * v.rpt);
      out.innerHTML = '<span class="eyebrow">Cost per finished report</span><div class="big">' + inr(per) + '</div>' +
        '<div class="row"><span>Annual desk cost</span><span>' + inr(tot) + '</span></div>' +
        '<div class="row"><span>Reports per year</span><span>' + v.n * v.rpt + '</span></div>' +
        hbars([{ label: 'Salaries', v: sal, t: inr(sal), c: GOLD }, { label: 'Data & tools', v: dat, t: inr(dat), c: BLUE },
               { label: 'Overheads', v: ovh, t: inr(ovh), c: GREEN }, { label: 'Senior review', v: rev, t: inr(rev), c: PINK }], Math.max(sal, dat, ovh, rev));
    }
    draw();
  };

  /* Two-stage DCF: how much of the value sits in the terminal year */
  W['dcf-explorer'] = function (el) {
    var out = document.createElement('div'); out.className = 'w-out';
    var pct = function (x) { return x + '%'; };
    var v = sliders(el, [
      { key: 'g1', label: 'FCF growth, years 1–10', min: 0, max: 30, value: 15, fmt: pct },
      { key: 'g2', label: 'Terminal growth (nominal)', min: 2, max: 8, step: 0.5, value: 5, fmt: pct },
      { key: 'r', label: 'Cost of capital (WACC)', min: 9, max: 16, step: 0.5, value: 12, fmt: pct }
    ], draw);
    el.appendChild(out);
    function draw() {
      var r = v.r / 100, g1 = v.g1 / 100, g2 = v.g2 / 100, f = 100, pv1 = 0;
      for (var t = 1; t <= 10; t++) { f *= (1 + g1); pv1 += f / Math.pow(1 + r, t); }
      if (r <= g2) { out.innerHTML = '<div class="big">∞</div><p class="muted">WACC must exceed terminal growth, or the model breaks.</p>'; return; }
      var tv = f * (1 + g2) / (r - g2), pvtv = tv / Math.pow(1 + r, 10), ev = pv1 + pvtv;
      out.innerHTML = '<span class="eyebrow">Value from the terminal year</span><div class="big">' + (100 * pvtv / ev).toFixed(0) + '%</div>' +
        '<div class="row"><span>Value / today\'s FCF</span><span>' + (ev / 100).toFixed(1) + '×</span></div>' +
        '<div class="row"><span>Implied exit multiple (TV / yr-10 FCF)</span><span>' + (tv / f).toFixed(1) + '×</span></div>' +
        hbars([{ label: 'PV years 1–10', v: pv1, t: (pv1 / 100).toFixed(1) + '×', c: BLUE }, { label: 'PV terminal', v: pvtv, t: (pvtv / 100).toFixed(1) + '×', c: GOLD }], Math.max(pv1, pvtv));
    }
    draw();
  };

  /* Fee drag: direct vs fixed-fee vs fixed + performance fee */
  W['fee-drag'] = function (el) {
    var out = document.createElement('div'); out.className = 'w-out';
    var pct = function (x) { return x + '%'; };
    var v = sliders(el, [
      { key: 'c', label: 'Starting corpus (₹ crore)', min: 1, max: 100, value: 10 },
      { key: 'r', label: 'Gross return per year', min: 6, max: 22, step: 0.5, value: 14, fmt: pct },
      { key: 'y', label: 'Years', min: 3, max: 20, value: 10 },
      { key: 'd', label: 'Direct: research + execution cost', min: 0, max: 1.5, step: 0.05, value: 0.3, fmt: pct },
      { key: 'f', label: 'Manager: fixed fee', min: 0, max: 3, step: 0.1, value: 2, fmt: pct },
      { key: 'p', label: 'Manager: performance fee', min: 0, max: 25, value: 20, fmt: pct },
      { key: 'h', label: 'Hurdle for performance fee', min: 0, max: 12, value: 10, fmt: pct }
    ], draw);
    el.appendChild(out);
    function draw() {
      var a = v.c, b = v.c, c = v.c, A = [a], B = [b], C = [c], r = v.r / 100;
      for (var t = 0; t < v.y; t++) {
        a *= 1 + r - v.d / 100; b *= 1 + r - v.f / 100;
        var g = c * (r - v.f / 100), hurdle = c * v.h / 100;
        c += g - Math.max(0, g - hurdle) * v.p / 100;
        A.push(a); B.push(b); C.push(c);
      }
      var mx = Math.max(a, b, c), s = '<svg viewBox="0 0 400 190">';
      [[A, BLUE, 'Direct'], [B, GREEN, 'Fixed fee'], [C, GOLD, 'Fixed + perf']].forEach(function (S) {
        s += '<path fill="none" stroke-width="2.4" stroke="' + S[1] + '" d="' + S[0].map(function (x, i) {
          return (i ? 'L' : 'M') + (10 + 300 * i / v.y).toFixed(1) + ',' + (180 - 165 * x / mx).toFixed(1); }).join(' ') + '"/>';
      });
      s += '<text x="318" y="' + (184 - 165 * a / mx) + '" font-size="11" fill="' + BLUE + '">Direct</text>' +
           '<text x="318" y="' + (184 - 165 * c / mx + (Math.abs(c - b) / mx < .06 ? 12 : 0)) + '" font-size="11" fill="' + GOLD + '">Fixed+perf</text></svg>';
      var cr = function (x) { return '₹' + x.toFixed(2) + ' cr'; };
      out.innerHTML = '<span class="eyebrow">Gap vs direct after ' + v.y + ' years</span><div class="big">' + cr(a - c) + '</div>' +
        '<div class="row"><span>Direct</span><span>' + cr(a) + '</span></div>' +
        '<div class="row"><span>Fixed fee only</span><span>' + cr(b) + '</span></div>' +
        '<div class="row"><span>Fixed + performance</span><span>' + cr(c) + '</span></div>' + s;
    }
    draw();
  };

  document.querySelectorAll('[data-widget]').forEach(function (fig) {
    var fn = W[fig.getAttribute('data-widget')];
    if (fn) fn(fig.querySelector('.widget-body'));
  });
})();
