function normalizeHostname(hostname) {
  return (hostname || "").replace(/^www\./, "").toLowerCase();
}

function shouldOpenInNewWindow(anchor, currentHost) {
  const href = anchor.getAttribute("href");
  if (!href || href.startsWith("#")) return false;

  let url;
  try {
    url = new URL(href, window.location.href);
  } catch {
    return false;
  }

  if (!["http:", "https:"].includes(url.protocol)) return false;
  return normalizeHostname(url.hostname) !== currentHost;
}

function ensureNoopener(anchor) {
  const relValues = new Set((anchor.getAttribute("rel") || "").split(/\s+/).filter(Boolean));
  relValues.add("noopener");
  relValues.add("noreferrer");
  anchor.setAttribute("rel", Array.from(relValues).join(" "));
}

function decorateExternalLinks() {
  const currentHost = normalizeHostname(window.location.hostname);

  document.querySelectorAll("a[href]").forEach(function (anchor) {
    if (!shouldOpenInNewWindow(anchor, currentHost)) return;

    const target = anchor.getAttribute("target");
    if (!target || target === "_self") anchor.setAttribute("target", "_blank");
    if (anchor.getAttribute("target") === "_blank") ensureNoopener(anchor);
  });
}

function getPageNavHref(kind) {
  const link = document.querySelector(`[data-page-nav="${kind}"]`);
  return link ? link.getAttribute("href") : "";
}

function shouldIgnoreKeyNavigation(event) {
  const target = event.target;
  if (!target) return false;

  if (target.closest("input, textarea, select, button, [contenteditable='true']")) return true;
  return event.metaKey || event.ctrlKey || event.altKey;
}

function navigateTo(href) {
  if (href) window.location.href = href;
}

document.addEventListener("keydown", function (event) {
  if (event.repeat || shouldIgnoreKeyNavigation(event)) return;

  if (event.key === "ArrowLeft") {
    const href = getPageNavHref("prev");
    if (href) {
      event.preventDefault();
      navigateTo(href);
    }
    return;
  }

  if (event.key === "ArrowRight") {
    const href = getPageNavHref("next");
    if (href) {
      event.preventDefault();
      navigateTo(href);
    }
    return;
  }

  if ((event.key === "ArrowUp" && event.shiftKey) || event.key === "§") {
    const href = getPageNavHref("home");
    if (href) {
      event.preventDefault();
      navigateTo(href);
    }
  }
});

decorateExternalLinks();
