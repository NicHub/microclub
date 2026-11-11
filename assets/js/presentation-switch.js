/* Bascule rapide entre l’article et sa vue présentation. */
(function () {
  'use strict';

  var link = document.querySelector('[data-presentation-url]');
  if (!link) {
    return;
  }

  document.addEventListener('keydown', function (event) {
    if (event.altKey || event.ctrlKey || event.metaKey) {
      return;
    }

    /* V comme « vue » : F reste réservé au plein écran dans la présentation. */
    if (event.key === 'v' || event.key === 'V') {
      var target = event.target;
      if (target && /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName)) {
        return;
      }
      event.preventDefault();
      window.location.href = link.href;
    }
  });
})();
