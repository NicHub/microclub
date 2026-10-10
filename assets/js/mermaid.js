const MERMAID_FONT_SIZE = "11px";
const MERMAID_RANK_SPACING = 30;
const MERMAID_CURVE = "linear";
const MERMAID_START_ON_LOAD = false;
const MERMAID_SELECTOR = "pre.mermaid:not([data-processed])";
const MERMAID_DARK_MODE_CLASS = "dark";
const MERMAID_GRAPH_ATTRIBUTE = "data-graph";
const MERMAID_LIGHT_THEME = "base";
const MERMAID_DARK_THEME = "dark";
const RENDER_DELAY_MS = 0;
const DOCUMENT_READY_STATE_COMPLETE = "complete";

function css(name) {
  return "rgb(" + getComputedStyle(document.documentElement).getPropertyValue(name) + ")";
}

function initMermaidLight() {
  mermaid.initialize({
    startOnLoad: MERMAID_START_ON_LOAD,
    flowchart: {
      rankSpacing: MERMAID_RANK_SPACING,
      curve: MERMAID_CURVE,
    },
    theme: MERMAID_LIGHT_THEME,
    themeVariables: {
      background: css("--color-neutral"),
      primaryColor: css("--color-primary-200"),
      secondaryColor: css("--color-secondary-200"),
      tertiaryColor: css("--color-neutral-100"),
      primaryBorderColor: css("--color-primary-400"),
      secondaryBorderColor: css("--color-secondary-400"),
      tertiaryBorderColor: css("--color-neutral-400"),
      lineColor: css("--color-neutral-600"),
      fontSize: MERMAID_FONT_SIZE,
    },
  });
}

function initMermaidDark() {
  mermaid.initialize({
    startOnLoad: MERMAID_START_ON_LOAD,
    flowchart: {
      rankSpacing: MERMAID_RANK_SPACING,
      curve: MERMAID_CURVE,
    },
    theme: MERMAID_DARK_THEME,
    themeVariables: {
      fontSize: MERMAID_FONT_SIZE,
    },
  });
}

async function renderPendingMermaid() {
  const nodes = document.querySelectorAll(MERMAID_SELECTOR);
  if (!nodes.length) return;

  nodes.forEach((node) => {
    node.setAttribute(MERMAID_GRAPH_ATTRIBUTE, node.textContent);
  });
  if (document.documentElement.classList.contains(MERMAID_DARK_MODE_CLASS)) {
    initMermaidDark();
  } else {
    initMermaidLight();
  }
  try {
    await mermaid.run({ nodes });
  } catch (error) {
    console.error("Mermaid rendering failed:", error);
  }
}

mermaid.initialize({ startOnLoad: MERMAID_START_ON_LOAD });

if (document.readyState !== DOCUMENT_READY_STATE_COMPLETE) {
  document.addEventListener("DOMContentLoaded", () => {
    setTimeout(renderPendingMermaid, RENDER_DELAY_MS);
  }, { once: true });
} else {
  renderPendingMermaid();
}
