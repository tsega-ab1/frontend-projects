// KORA Coffee — sparse, deliberate interactions only

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

(function () {
  var form = document.getElementById('newsletter-form');
  if (!form) return;

  var note = document.getElementById('newsletter-note');
  var input = document.getElementById('newsletter-email');

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!input.checkValidity()) {
      note.textContent = 'Enter a valid email address to subscribe.';
      note.hidden = false;
      input.focus();
      return;
    }

    note.textContent = 'Subscribed — new-crop notes will land in your inbox.';
    note.hidden = false;
    form.reset();
  });
})();
