// SmileLife Dental Hospital — sparse, deliberate interactions only

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
  var form = document.getElementById('contact-form');
  if (!form) return;

  var note = document.getElementById('form-note');

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!form.checkValidity()) {
      note.textContent = 'Please fill in your name, phone and email so we can confirm your appointment.';
      note.hidden = false;
      return;
    }

    note.textContent = "Request received — we'll call or email you within one business day to confirm.";
    note.hidden = false;
    form.reset();
  });
})();
