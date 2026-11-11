/* Navigation de la vue « présentation ».
   Flèches, espace, PageUp/PageDown, Home/End, F pour le plein écran, P pour
   l’impression. Le numéro de diapositive est reflété dans le fragment d’URL. */

(function () {
  'use strict';

  var deck = document.getElementById('deck');
  if (!deck) {
    return;
  }

  var slides = Array.prototype.slice.call(deck.querySelectorAll('.slide'));
  var total = slides.length;
  if (total === 0) {
    return;
  }

  var current = 0;
  var counter = document.querySelector('.deck-current');
  var progress = document.querySelector('.deck-progress-bar');

  function clamp(index) {
    return Math.max(0, Math.min(total - 1, index));
  }

  function readHash() {
    var match = /^#(\d+)$/.exec(window.location.hash);
    return match ? clamp(parseInt(match[1], 10) - 1) : 0;
  }

  function show(index, updateHash) {
    index = clamp(index);

    if (slides[current] !== slides[index]) {
      slides[current].classList.remove('is-active');
      slides[current].setAttribute('aria-hidden', 'true');
    }

    current = index;
    slides[current].classList.add('is-active');
    slides[current].setAttribute('aria-hidden', 'false');
    slides[current].scrollTop = 0;

    if (counter) {
      counter.textContent = String(current + 1);
    }
    if (progress) {
      progress.style.width = (((current + 1) / total) * 100).toFixed(2) + '%';
    }

    if (updateHash !== false) {
      var hash = '#' + (current + 1);
      if (window.location.hash !== hash) {
        window.history.replaceState(null, '', hash);
      }
    }
  }

  function next() {
    show(current + 1);
  }

  function prev() {
    show(current - 1);
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      var root = document.documentElement;
      if (root.requestFullscreen) {
        root.requestFullscreen();
      }
    } else if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }

  document.addEventListener('keydown', function (event) {
    if (event.altKey || event.ctrlKey || event.metaKey) {
      return;
    }

    switch (event.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
      case 'Enter':
        event.preventDefault();
        next();
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
      case 'Backspace':
        event.preventDefault();
        prev();
        break;
      case 'Home':
        event.preventDefault();
        show(0);
        break;
      case 'End':
        event.preventDefault();
        show(total - 1);
        break;
      case 'f':
      case 'F':
        toggleFullscreen();
        break;
      case 'p':
      case 'P':
        window.print();
        break;
      case 'v':
      case 'V': {
        var articleLink = document.querySelector('.deck-back');
        if (articleLink) {
          event.preventDefault();
          window.location.href = articleLink.href;
        }
        break;
      }
    }
  });

  /* Balayage horizontal sur écran tactile. */
  var startX = null;
  var startY = null;

  document.addEventListener(
    'touchstart',
    function (event) {
      if (event.touches.length !== 1) {
        return;
      }
      startX = event.touches[0].clientX;
      startY = event.touches[0].clientY;
    },
    { passive: true }
  );

  document.addEventListener(
    'touchend',
    function (event) {
      if (startX === null) {
        return;
      }
      var deltaX = event.changedTouches[0].clientX - startX;
      var deltaY = event.changedTouches[0].clientY - startY;
      startX = null;
      startY = null;
      if (Math.abs(deltaX) > 60 && Math.abs(deltaX) > Math.abs(deltaY)) {
        if (deltaX < 0) {
          next();
        } else {
          prev();
        }
      }
    },
    { passive: true }
  );

  /* Le fragment d’URL peut aussi être modifié à la main. */
  window.addEventListener('hashchange', function () {
    show(readHash(), false);
  });

  show(readHash(), false);
})();
