// Email CTAs open Gmail compose on desktop. Phones keep mailto: so the Gmail app (or default mail app) opens.
(function () {
  function gmail(href) {
    var parts = href.replace(/^mailto:/i, '').split('?'), q = new URLSearchParams(parts[1] || '');
    var u = new URLSearchParams({ view: 'cm', fs: '1', to: decodeURIComponent(parts[0]) });
    if (q.get('subject')) u.set('su', q.get('subject'));
    if (q.get('body')) u.set('body', q.get('body'));
    return 'https://mail.google.com/mail/?' + u.toString();
  }
  var desktop = window.matchMedia && matchMedia('(hover:hover) and (pointer:fine)').matches;
  window.gfMail = function (href) {
    if (desktop) window.open(gmail(href), '_blank', 'noopener'); else location.href = href;
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a || !desktop || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    window.gfMail(a.getAttribute('href'));
  });
})();
