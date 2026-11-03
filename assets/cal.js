/* Cal.com popup for every [data-cal-open] link. Only the public booking link
   belongs here, never an API key. Without JS the link opens the Cal page. */
(function () {
  var NS = '30min', LINK = 'parth-khanna-1/30min';
  var CONFIG = { layout: 'month_view', theme: 'light' };
  function track(name, props) { try { (window._hsq = window._hsq || []).push(['trackEvent', { id: name, value: (props && props.location) || '' }]); } catch (e) {} }

  /* Official Cal.com embed loader */
  (function (C, A, L) { var p = function (a, ar) { a.q.push(ar); }; var d = C.document; C.Cal = C.Cal || function () { var cal = C.Cal; var ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement('script')).src = A; cal.loaded = true; } if (ar[0] === L) { var api = function () { p(api, arguments); }; var namespace = ar[1]; api.q = api.q || []; if (typeof namespace === 'string') { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ['initNamespace', namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, 'https://app.cal.com/embed/embed.js', 'init');

  Cal('init', NS, { origin: 'https://app.cal.com' });
  Cal.ns[NS]('ui', { theme: 'light', hideEventTypeDetails: false, layout: 'month_view', cssVarsPerTheme: { light: { 'cal-brand': '#0f2a24' } } });
  /* Load the booking page ahead of the click so the popup feels instant */
  Cal.ns[NS]('preload', { calLink: LINK });
  Cal.ns[NS]('on', { action: 'bookingSuccessful', callback: function () { track('cal_booking_success', { page: location.pathname }); } });

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-cal-open]');
    if (!a || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    track('cal_popup_open', { location: a.getAttribute('data-cal-open') });
    Cal.ns[NS]('modal', { calLink: LINK, config: CONFIG });
  });
})();
