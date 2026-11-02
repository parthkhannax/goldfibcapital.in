/* ==========================================================================
   Goldfib Capital · Interaction & Micro-Interaction Engine
   - Easing: Decisive spring curves
   - Live High-Speed Search with live result counts
   - Grid vs Institutional Ledger View Switcher
   - Dynamic Scroll-Spy Table of Contents
   - Accessible keyboard focus and mobile navigation
   ========================================================================== */

(function () {
  'use strict';

  var $$ = function (sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  };

  // 1. Reading Progress Bar & Scroll Spy for Table of Contents
  var progressBar = document.getElementById('progress');
  var tocLinks = $$('.toc a[href^="#"]');
  var headings = tocLinks.map(function (a) {
    var id = a.getAttribute('href').slice(1);
    return document.getElementById(id);
  }).filter(Boolean);

  function handleScroll() {
    var docEl = document.documentElement;
    var totalHeight = docEl.scrollHeight - docEl.clientHeight;
    if (progressBar && totalHeight > 0) {
      progressBar.style.width = ((docEl.scrollTop / totalHeight) * 100) + '%';
    }

    if (!tocLinks.length || !headings.length) return;

    var scrollY = window.pageYOffset || docEl.scrollTop;
    var currentActive = null;

    for (var i = 0; i < headings.length; i++) {
      var top = headings[i].getBoundingClientRect().top;
      if (top <= 160) {
        currentActive = tocLinks[i];
      }
    }

    tocLinks.forEach(function (link) {
      link.classList.toggle('on', link === currentActive);
    });
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // 2. Library Instant Search, Topic & Level Filtering
  var searchInput = document.getElementById('lib-q');
  var pillButtons = $$('.pill[data-filter]');
  var levelButtons = $$('.lv[data-level]');
  var clusters = $$('.cluster');
  var allCards = $$('.card');
  var noResults = document.querySelector('.no-results');
  var resultsCounter = document.getElementById('results-count');

  var currentTopic = 'all';
  var currentLevel = 'all';

  function filterLibrary() {
    var query = searchInput ? searchInput.value.trim().toLowerCase() : '';
    var tokens = query ? query.split(/\s+/) : [];
    var visibleTotal = 0;

    clusters.forEach(function (cluster) {
      var clusterCards = $$('.card', cluster);
      var clusterVisible = 0;

      clusterCards.forEach(function (card) {
        var cardTopic = card.getAttribute('data-cluster') || '';
        var cardLevel = card.getAttribute('data-level') || '';
        var searchIndex = (card.getAttribute('data-search') || '').toLowerCase();

        var matchesTopic = (currentTopic === 'all' || cardTopic === currentTopic);
        var matchesLevel = (currentLevel === 'all' || cardLevel === currentLevel);
        var matchesQuery = !tokens.length || tokens.every(function (token) {
          return searchIndex.indexOf(token) !== -1;
        });

        var isVisible = matchesTopic && matchesLevel && matchesQuery;
        card.style.display = isVisible ? '' : 'none';

        if (isVisible) {
          clusterVisible++;
          visibleTotal++;
        }
      });

      cluster.style.display = clusterVisible > 0 ? '' : 'none';
    });

    if (noResults) {
      noResults.hidden = visibleTotal > 0;
    }

    if (resultsCounter) {
      resultsCounter.textContent = visibleTotal;
    }
  }

  pillButtons.forEach(function (pill) {
    pill.addEventListener('click', function () {
      currentTopic = pill.getAttribute('data-filter') || 'all';
      pillButtons.forEach(function (btn) {
        var isTarget = btn === pill;
        btn.classList.toggle('on', isTarget);
        btn.setAttribute('aria-pressed', isTarget ? 'true' : 'false');
      });
      filterLibrary();
    });
  });

  levelButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      currentLevel = btn.getAttribute('data-level') || 'all';
      levelButtons.forEach(function (b) {
        b.classList.toggle('on', b === btn);
      });
      filterLibrary();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', filterLibrary);
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.activeElement === searchInput) {
        searchInput.value = '';
        filterLibrary();
        searchInput.blur();
      }
    });
  }

  // 3. View Switcher (Grid vs Institutional Ledger View)
  var viewGridBtn = document.getElementById('view-grid');
  var viewLedgerBtn = document.getElementById('view-ledger');
  var libraryContainer = document.querySelector('.library-container');

  function setView(mode) {
    if (!libraryContainer) return;
    if (mode === 'ledger') {
      libraryContainer.classList.add('mode-ledger');
      if (viewLedgerBtn) viewLedgerBtn.classList.add('on');
      if (viewGridBtn) viewGridBtn.classList.remove('on');
      try { localStorage.setItem('goldfib_lib_view', 'ledger'); } catch (e) {}
    } else {
      libraryContainer.classList.remove('mode-ledger');
      if (viewGridBtn) viewGridBtn.classList.add('on');
      if (viewLedgerBtn) viewLedgerBtn.classList.remove('on');
      try { localStorage.setItem('goldfib_lib_view', 'grid'); } catch (e) {}
    }
  }

  if (viewGridBtn && viewLedgerBtn) {
    viewGridBtn.addEventListener('click', function () { setView('grid'); });
    viewLedgerBtn.addEventListener('click', function () { setView('ledger'); });
    try {
      var savedView = localStorage.getItem('goldfib_lib_view');
      if (savedView === 'ledger') setView('ledger');
    } catch (e) {}
  }

  // 4. Mobile Navigation Toggle
  var nav = document.querySelector('.nav');
  var navToggle = document.querySelector('.nav-toggle');
  if (nav && navToggle) {
    navToggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // 5. Operations Command Hub (WOW Factor Telemetry & Interactions)
  var opsHub = document.getElementById('opsHub');
  if (opsHub) {
    // A. Real-Time IST Digital Clock
    var clockDigits = document.getElementById('clockDigits');
    function tickClock() {
      try {
        var now = new Date();
        var ist = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Kolkata' }));
        var hh = String(ist.getHours()).padStart(2, '0');
        var mm = String(ist.getMinutes()).padStart(2, '0');
        var ss = String(ist.getSeconds()).padStart(2, '0');
        if (clockDigits) clockDigits.textContent = hh + ':' + mm + ':' + ss + ' IST';
      } catch (err) {}
    }
    tickClock();
    setInterval(tickClock, 1000);

    // B. Interactive Tab Controller (Stream vs Waveform vs Pipeline)
    var tabs = $$('.ops-tab', opsHub);
    var panels = $$('.ops-panel', opsHub);
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var targetId = 'panel-' + tab.getAttribute('data-tab');
        tabs.forEach(function (t) { t.classList.toggle('active', t === tab); });
        panels.forEach(function (p) { p.classList.toggle('active', p.id === targetId); });
      });
    });

    // C. Live Transaction Ingestion Stream (THE ANIMATED WOW FACTOR)
    var streamFeed = document.getElementById('streamFeed');
    var transactionLedger = [
      { inst: 'kotak', name: 'Kotak Custody', desc: 'NSE:TCS · 1,200 sh (₹4.20 Cr)', status: 'AUTO-MATCHED ✓' },
      { inst: 'julius', name: 'Julius Baer (DIFC)', desc: 'US Tech Co-Investment ($850K)', status: 'DTAA RECONCILED ✓' },
      { inst: 'hdfc', name: 'HDFC Bank Custody', desc: '7.38% GS 2027 Coupon (₹18.45 L)', status: 'CREDITED ✓' },
      { inst: 'ibkr', name: 'Interactive Brokers', desc: 'SPX Collar Hedge Roll ($120K)', status: 'MARGIN SYNCED ✓' },
      { inst: 'icici', name: 'ICICI Securities', desc: 'Contract Note #88412 Parsed', status: '0 DISCREPANCIES ✓' },
      { inst: 'julius', name: 'Julius Baer (UAE)', desc: 'Gulf PE Distribution ($420K)', status: 'TAX-LOT BOOKED ✓' },
      { inst: 'kotak', name: 'Kotak Private', desc: 'Pre-IPO Chemical Co-Inv (₹15 Cr)', status: 'SHADOW NAV BOOKED ✓' }
    ];

    var txIndex = 0;
    var maxVisibleRows = 3;
    var isPaused = false;

    function renderInitialFeed() {
      if (!streamFeed) return;
      streamFeed.innerHTML = '';
      for (var i = 0; i < maxVisibleRows; i++) {
        addTransactionRow(transactionLedger[i], false);
      }
      txIndex = maxVisibleRows;
    }

    function addTransactionRow(tx, animate) {
      if (!streamFeed) return;
      var row = document.createElement('div');
      row.className = 'stream-row';
      if (animate) row.style.animation = 'streamSlideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1)';
      row.innerHTML = '<span class="st-inst ' + tx.inst + '">' + tx.name + '</span>' +
                      '<span class="st-desc">' + tx.desc + '</span>' +
                      '<span class="st-status">' + tx.status + '</span>';
      
      streamFeed.insertBefore(row, streamFeed.firstChild);
      if (streamFeed.children.length > maxVisibleRows) {
        streamFeed.removeChild(streamFeed.lastChild);
      }
    }

    renderInitialFeed();

    var streamInterval = setInterval(function () {
      if (isPaused) return;
      var tx = transactionLedger[txIndex % transactionLedger.length];
      txIndex++;
      addTransactionRow(tx, true);
    }, 2800);

    opsHub.addEventListener('mouseenter', function () { isPaused = true; });
    opsHub.addEventListener('mouseleave', function () { isPaused = false; });

    // D. Interactive SVG Waveform Scrubber
    var wfWrap = document.getElementById('waveformWrap');
    var crosshair = document.getElementById('wfCrosshair');
    var point = document.getElementById('wfPoint');
    var tooltip = document.getElementById('wfTooltip');

    if (wfWrap && crosshair && point && tooltip) {
      var dataPoints = [
        { x: 40, y: 118, date: 'Q1 2024', val: '₹284.10 Cr' },
        { x: 120, y: 95, date: 'Q3 2024', val: '₹316.50 Cr' },
        { x: 210, y: 75, date: 'Q1 2025', val: '₹352.80 Cr' },
        { x: 310, y: 50, date: 'Q3 2025', val: '₹388.20 Cr' },
        { x: 400, y: 24, date: 'Q1 2026', val: '₹408.40 Cr' },
        { x: 450, y: 18, date: 'Q3 2026 (Live)', val: '₹412.60 Cr' }
      ];

      wfWrap.addEventListener('mousemove', function (e) {
        var rect = wfWrap.getBoundingClientRect();
        var mouseX = e.clientX - rect.left;
        var svgX = (mouseX / rect.width) * 460;

        // Find nearest point
        var closest = dataPoints.reduce(function (prev, curr) {
          return Math.abs(curr.x - svgX) < Math.abs(prev.x - svgX) ? curr : prev;
        });

        crosshair.setAttribute('x1', closest.x);
        crosshair.setAttribute('x2', closest.x);
        crosshair.setAttribute('opacity', '0.7');

        point.setAttribute('cx', closest.x);
        point.setAttribute('cy', closest.y);
        point.setAttribute('opacity', '1');

        tooltip.innerHTML = '<div class="tt-date">' + closest.date + '</div><div class="tt-val">' + closest.val + '</div>';
        var tooltipLeft = Math.max(10, Math.min(rect.width - 120, (closest.x / 460) * rect.width - 45));
        tooltip.style.left = tooltipLeft + 'px';
        tooltip.classList.add('visible');
      });

      wfWrap.addEventListener('mouseleave', function () {
        crosshair.setAttribute('opacity', '0');
        point.setAttribute('opacity', '0');
        tooltip.classList.remove('visible');
      });
    }

    // E. 3D Magnetic Perspective Tilt (genjutsu style)
    if (window.matchMedia('(pointer: fine)').matches) {
      opsHub.addEventListener('mousemove', function (e) {
        var rect = opsHub.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var centerX = rect.width / 2;
        var centerY = rect.height / 2;
        var rotateX = ((y - centerY) / centerY) * -3;
        var rotateY = ((x - centerX) / centerX) * 3;
        opsHub.style.transform = 'perspective(1200px) rotateX(' + rotateX.toFixed(2) + 'deg) rotateY(' + rotateY.toFixed(2) + 'deg) translateY(-2px)';
        opsHub.style.setProperty('--mouse-x', x + 'px');
        opsHub.style.setProperty('--mouse-y', y + 'px');
      });

      opsHub.addEventListener('mouseleave', function () {
        opsHub.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) translateY(0px)';
      });
    }
  }
})();
