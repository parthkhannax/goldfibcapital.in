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

  // 5. Memo Automation Engine (AI Prompt ➔ Team Analysing ➔ Done)
  var memoEngine = document.getElementById('memoEngine');
  if (memoEngine) {
    var stepBtns = [
      document.getElementById('stepBtn1'),
      document.getElementById('stepBtn2'),
      document.getElementById('stepBtn3')
    ];
    var stepPanels = [
      document.getElementById('panelStep1'),
      document.getElementById('panelStep2'),
      document.getElementById('panelStep3')
    ];
    var conn1 = document.getElementById('stepConn1');
    var conn2 = document.getElementById('stepConn2');
    var statusText = document.getElementById('stepStatusText');
    var anPct = document.getElementById('anPct');
    var btnNext = document.getElementById('btnNextToAnalysis');

    var currentStep = 2; // Start on Step 2 (Analysing with charts)
    var isUserInteracting = false;
    var autoTimer = null;

    var stepDescriptions = [
      'FO PROMPT',
      'TEAM ANALYSING',
      'IC APPROVED'
    ];

    function setStep(stepNum, userTriggered) {
      currentStep = stepNum;
      if (userTriggered) {
        isUserInteracting = true;
        clearTimeout(autoTimer);
        setTimeout(function () { isUserInteracting = false; }, 9000);
      }

      stepBtns.forEach(function (btn, idx) {
        if (!btn) return;
        var s = idx + 1;
        btn.classList.toggle('active', s === stepNum);
        btn.classList.toggle('done', s < stepNum);
      });

      stepPanels.forEach(function (panel, idx) {
        if (!panel) return;
        panel.classList.toggle('active', (idx + 1) === stepNum);
      });

      if (conn1) conn1.classList.toggle('active', stepNum >= 2);
      if (conn2) conn2.classList.toggle('active', stepNum >= 3);

      if (statusText) statusText.textContent = stepDescriptions[stepNum - 1] || 'PROCESSING';

      if (stepNum === 2 && anPct) {
        anPct.textContent = '88% SYNTHESIZED';
        setTimeout(function () { if (currentStep === 2) anPct.textContent = '94% SYNTHESIZED'; }, 1100);
        setTimeout(function () { if (currentStep === 2) anPct.textContent = '100% VERIFIED'; }, 2200);
      }
    }

    window.setMemoStep = function (s) { setStep(s, true); };

    stepBtns.forEach(function (btn, idx) {
      if (btn) {
        btn.addEventListener('click', function () {
          setStep(idx + 1, true);
        });
      }
    });

    if (btnNext) {
      btnNext.addEventListener('click', function () {
        setStep(2, true);
      });
    }

    // Auto-Cycle: 1 ➔ 2 ➔ 3 ➔ 1 every 4.2 seconds
    function startAutoCycle() {
      autoTimer = setInterval(function () {
        if (isUserInteracting) return;
        var next = currentStep >= 3 ? 1 : currentStep + 1;
        setStep(next, false);
      }, 4200);
    }

    startAutoCycle();

    memoEngine.addEventListener('mouseenter', function () { isUserInteracting = true; });
    memoEngine.addEventListener('mouseleave', function () { isUserInteracting = false; });

    // 3D Magnetic Perspective Tilt (genjutsu style)
    if (window.matchMedia('(pointer: fine)').matches) {
      memoEngine.addEventListener('mousemove', function (e) {
        var rect = memoEngine.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var centerX = rect.width / 2;
        var centerY = rect.height / 2;
        var rotateX = ((y - centerY) / centerY) * -3;
        var rotateY = ((x - centerX) / centerX) * 3;
        memoEngine.style.transform = 'perspective(1200px) rotateX(' + rotateX.toFixed(2) + 'deg) rotateY(' + rotateY.toFixed(2) + 'deg) translateY(-2px)';
        memoEngine.style.setProperty('--mouse-x', x + 'px');
        memoEngine.style.setProperty('--mouse-y', y + 'px');
      });

      memoEngine.addEventListener('mouseleave', function () {
        memoEngine.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) translateY(0px)';
      });
    }
  }
})();
