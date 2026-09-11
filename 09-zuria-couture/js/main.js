// ZURIA — sparse, deliberate interactions only

(function () {
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }
})();

function wireForm(formId, noteId, successMessage, invalidMessage) {
  var form = document.getElementById(formId);
  if (!form) return;
  var note = document.getElementById(noteId);

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!form.checkValidity()) {
      note.textContent = invalidMessage;
      note.hidden = false;
      return;
    }
    note.textContent = successMessage;
    note.hidden = false;
    form.reset();
  });
}

wireForm('newsletter-form', 'newsletter-note', 'Subscribed — atelier updates will land in your inbox.', 'Enter a valid email address to subscribe.');
wireForm('order-form-el', 'order-note', "Request received — we'll email you within one business day with next steps.", 'Please fill in your name and email so we can reach you.');
wireForm('contact-form', 'contact-note', "Message sent — we'll reply within one business day.", 'Please fill in your name and email before sending.');
