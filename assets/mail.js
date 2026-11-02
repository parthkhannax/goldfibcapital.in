// Goldfib Capital · Direct Enquiry & HubSpot Lead Capture Engine
// Links all email CTAs across the site to HubSpot form fill + persistent lead ledger.
(function () {
  'use strict';

  var desktop = window.matchMedia && matchMedia('(hover:hover) and (pointer:fine)').matches;

  function parseMailto(href) {
    var parts = href.replace(/^mailto:/i, '').split('?');
    var to = decodeURIComponent(parts[0] || 'partners@goldfibcapital.in');
    var q = new URLSearchParams(parts[1] || '');
    return {
      to: to,
      subject: q.get('subject') || '',
      body: q.get('body') || ''
    };
  }

  function gmailUrl(href) {
    var m = parseMailto(href);
    var u = new URLSearchParams({ view: 'cm', fs: '1', to: m.to });
    if (m.subject) u.set('su', m.subject);
    if (m.body) u.set('body', m.body);
    return 'https://mail.google.com/mail/?' + u.toString();
  }

  window.gfMailRaw = function (href) {
    if (desktop) window.open(gmailUrl(href), '_blank', 'noopener');
    else location.href = href;
  };

  var modalHtml =
    '<div id="gf-contact-modal" class="gf-modal" aria-hidden="true" role="dialog" aria-modal="true">' +
      '<div class="gf-modal-backdrop" data-gf-close></div>' +
      '<div class="gf-modal-card">' +
        '<div class="gf-modal-head">' +
          '<span class="eyebrow">TALK TO US · GOLDFIB RESEARCH DESK</span>' +
          '<button class="gf-modal-close" data-gf-close aria-label="Close dialog">&times;</button>' +
        '</div>' +
        '<h3 id="gf-modal-heading">Start a research discussion</h3>' +
        '<p class="gf-modal-sub" id="gf-modal-desc">Share your portfolio coverage list or bespoke diligence requirement. A research analyst responds within one working day.</p>' +
        '<form id="gf-enquiry-form" class="gf-form" method="POST" action="#">' +
          '<input type="hidden" name="form_name" value="Goldfib Research Enquiry">' +
          '<input type="hidden" name="page_url" id="gf-hs-url" value="">' +
          '<input type="hidden" name="page_title" id="gf-hs-title" value="">' +
          '<input type="hidden" name="inquiry_topic" id="gf-hs-topic" value="">' +
          '<div class="gf-form-row">' +
            '<label><span>Work Email <b style="color:var(--gold)">*</b></span>' +
              '<input type="email" name="email" required autocomplete="email" placeholder="name@familyoffice.in">' +
            '</label>' +
          '</div>' +
          '<div class="gf-form-cols">' +
            '<label><span>Full Name <b style="color:var(--gold)">*</b></span>' +
              '<input type="text" name="firstname" required autocomplete="name" placeholder="Rajesh Singhania">' +
            '</label>' +
            '<label><span>Family Office / Firm</span>' +
              '<input type="text" name="company" autocomplete="organization" placeholder="Singhania Family Office">' +
            '</label>' +
          '</div>' +
          '<div class="gf-form-row">' +
            '<label><span>Research Scope or Query</span>' +
              '<textarea name="message" id="gf-hs-message" rows="3" placeholder="Tell us about the companies you cover or the research work you need done..."></textarea>' +
            '</label>' +
          '</div>' +
          '<button type="submit" class="btn gf-submit-btn">Submit Enquiry to Desk →</button>' +
          '<div class="gf-form-foot">' +
            '<span>Direct buy-side analyst dialogue. No sales sequences or spam.</span>' +
            '<a href="#" id="gf-direct-mail" class="gf-direct-mail">Prefer direct email? Launch mail app →</a>' +
          '</div>' +
        '</form>' +
        '<div id="gf-form-success" class="gf-success" hidden>' +
          '<div class="gf-check">&#10003;</div>' +
          '<h4>Enquiry Received</h4>' +
          '<p>Thank you for reaching out. A research partner from our desk will review your requirement and follow up within one working day.</p>' +
          '<button type="button" class="btn ghost small" data-gf-close>Close</button>' +
        '</div>' +
      '</div>' +
    '</div>';

  var modal, form, successCard, currentMailtoHref = '';

  function ensureModal() {
    if (modal) return;
    var div = document.createElement('div');
    div.innerHTML = modalHtml;
    modal = div.firstElementChild;
    document.body.appendChild(modal);

    form = modal.querySelector('#gf-enquiry-form');
    successCard = modal.querySelector('#gf-form-success');

    modal.addEventListener('click', function (e) {
      if (e.target.closest('[data-gf-close]')) {
        closeModal();
      }
    });

    modal.querySelector('#gf-direct-mail').addEventListener('click', function (e) {
      e.preventDefault();
      closeModal();
      window.gfMailRaw(currentMailtoHref || 'mailto:partners@goldfibcapital.in');
    });

    form.addEventListener('submit', handleFormSubmit);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  function openModal(href) {
    ensureModal();
    currentMailtoHref = href || 'mailto:partners@goldfibcapital.in';
    var parsed = parseMailto(currentMailtoHref);

    form.reset();
    form.hidden = false;
    successCard.hidden = true;

    modal.querySelector('#gf-hs-url').value = location.href;
    modal.querySelector('#gf-hs-title').value = document.title;
    modal.querySelector('#gf-hs-topic').value = parsed.subject;

    if (parsed.subject) {
      modal.querySelector('#gf-modal-heading').textContent = parsed.subject.length > 50
        ? parsed.subject.slice(0, 48) + '...'
        : parsed.subject;
    } else {
      modal.querySelector('#gf-modal-heading').textContent = 'Start a research discussion';
    }

    var msgBox = modal.querySelector('#gf-hs-message');
    if (parsed.subject && !msgBox.value) {
      msgBox.placeholder = 'Inquiry: ' + parsed.subject;
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    var emailInput = form.querySelector('input[name="email"]');
    if (emailInput) setTimeout(function () { emailInput.focus(); }, 120);
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function handleFormSubmit(e) {
    e.preventDefault();
    var email = form.email.value.trim();
    var name = form.firstname.value.trim();
    var company = form.company.value.trim();
    var msg = form.message.value.trim();
    var topic = modal.querySelector('#gf-hs-topic').value;

    if (!email) return;

    var lead = {
      source: 'goldfib_contact_modal',
      email: email,
      firstname: name,
      company: company,
      message: msg,
      topic: topic,
      page_url: location.href,
      page_title: document.title,
      timestamp: new Date().toISOString()
    };

    // 1. Save to client-side lead ledger
    try {
      var leads = JSON.parse(localStorage.getItem('goldfib_leads') || '[]');
      leads.push(lead);
      localStorage.setItem('goldfib_leads', JSON.stringify(leads));
    } catch (err) {}

    // 2. Dispatch submission so HubSpot tracking code captures the form fill
    try {
      if (window._hsq) {
        window._hsq.push(['identify', {
          email: email,
          firstname: name,
          company: company
        }]);
        window._hsq.push(['trackEvent', {
          id: 'Goldfib Research Enquiry Submitted',
          value: topic
        }]);
      }
    } catch (hsqErr) {}

    // 3. Display confirmation
    form.hidden = true;
    successCard.hidden = false;
  }

  window.gfOpenModal = openModal;
  window.gfCloseModal = closeModal;
  window.gfMail = openModal;

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    openModal(a.getAttribute('href'));
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureModal);
  } else {
    ensureModal();
  }
})();
