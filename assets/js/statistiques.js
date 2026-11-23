(() => {
  "use strict";

  const root = document.querySelector("[data-statistiques]");
  if (!root) return;

  const authorSelect = root.querySelector("#statistiques-auteur");
  const yearSelect = root.querySelector("#statistiques-annee");
  const grid = root.querySelector("[data-calendar-grid]");
  const count = root.querySelector("[data-calendar-count]");
  const empty = root.querySelector("[data-calendar-empty]");
  const authors = root.querySelectorAll("[data-author-filter]");
  const formatDate = new Intl.DateTimeFormat("fr-CH", { dateStyle: "full", timeZone: "UTC" });
  const formatMonth = new Intl.DateTimeFormat("fr-CH", { month: "short", timeZone: "UTC" });
  const years = Array.from(root.querySelectorAll("[data-year]"), (element) => {
    const days = Array.from(element.querySelectorAll("[data-day]"), (day) => ({
      key: day.dataset.day,
      element: day,
      count: day.querySelector("[data-day-count]"),
      articles: Array.from(day.querySelectorAll("[data-author]")),
    }));
    return { key: element.dataset.year, element, days };
  });

  function articleCount(total) {
    return `${total} ${total === 1 ? "article" : "articles"}`;
  }

  function initRanking() {
    const controls = root.querySelector("[data-ranking-controls]");
    const start = controls.querySelector("#statistiques-debut");
    const end = controls.querySelector("#statistiques-fin");
    const reset = controls.querySelector("[data-ranking-reset]");
    const status = root.querySelector("[data-ranking-status]");
    const ranking = root.querySelector("[data-ranking]");
    const first = start.options[0].value;
    const last = end.options[end.options.length - 1].value;
    const rows = Array.from(authors, (link) => {
      const element = link.closest("li");
      return {
        element,
        author: link.dataset.authorFilter,
        count: element.querySelector(".stats-rank-count"),
        bar: element.querySelector(".stats-rank-bar"),
      };
    });
    const [all, ...individuals] = rows;

    function renderRanking() {
      const from = Number(start.value);
      const to = Number(end.value);
      const counts = new Map();
      let total = 0;
      for (const year of years) {
        const value = Number(year.key);
        if (value < from || value > to) continue;
        for (const day of year.days) {
          for (const article of day.articles) {
            const author = article.dataset.author;
            counts.set(author, (counts.get(author) ?? 0) + 1);
            total += 1;
          }
        }
      }

      function updateRow(row, amount) {
        row.count.textContent = articleCount(amount);
        row.bar.style.width = total ? `${100 * amount / total}%` : "0%";
        row.bar.hidden = amount === 0;
        row.element.hidden = row !== all && amount === 0;
      }

      updateRow(all, total);
      const ordered = individuals.map((row) => ({ row, amount: counts.get(row.author) ?? 0 }));
      ordered.sort((a, b) => b.amount - a.amount);
      for (const { row, amount } of ordered) {
        updateRow(row, amount);
        ranking.append(row.element);
      }

      const period = from === to ? `en ${from}` : `de ${from} à ${to}`;
      status.textContent = total ? `${articleCount(total)} ${period}.` : `Aucun article publié ${period}.`;
      reset.disabled = start.value === first && end.value === last;
    }

    start.addEventListener("change", () => {
      if (Number(start.value) > Number(end.value)) end.value = start.value;
      renderRanking();
    });
    end.addEventListener("change", () => {
      if (Number(end.value) < Number(start.value)) start.value = end.value;
      renderRanking();
    });
    reset.addEventListener("click", () => {
      start.value = first;
      end.value = last;
      start.focus();
      renderRanking();
    });
    renderRanking();
    controls.hidden = false;
  }

  function renderGrid(year, activeDays) {
    const first = new Date(Date.UTC(year, 0, 1));
    const end = new Date(Date.UTC(year + 1, 0, 1));
    const offset = (first.getUTCDay() + 6) % 7;
    const dayCount = (end - first) / 86400000;
    const fragment = document.createDocumentFragment();
    grid.style.setProperty("--stats-weeks", Math.ceil((offset + dayCount) / 7));

    for (const [row, name] of [[2, "lun."], [4, "mer."], [6, "ven."]]) {
      const label = document.createElement("span");
      label.className = "stats-weekday";
      label.style.gridRow = row;
      label.setAttribute("aria-hidden", "true");
      label.textContent = name;
      fragment.append(label);
    }

    for (let i = 0; i < dayCount; i += 1) {
      const date = new Date(Date.UTC(year, 0, i + 1));
      const column = Math.floor((i + offset) / 7) + 2;
      if (date.getUTCDate() === 1) {
        const month = document.createElement("span");
        month.className = "stats-month";
        month.style.gridColumn = column;
        month.setAttribute("aria-hidden", "true");
        month.textContent = formatMonth.format(date);
        fragment.append(month);
      }

      const active = activeDays.get(date.toISOString().slice(0, 10));
      const cell = document.createElement(active ? "button" : "span");
      cell.className = "stats-cell";
      cell.dataset.level = Math.min(active?.total ?? 0, 4);
      cell.style.gridColumn = column;
      cell.style.gridRow = ((i + offset) % 7) + 2;
      if (active) {
        cell.type = "button";
        cell.title = `${formatDate.format(date)} : ${articleCount(active.total)}`;
        cell.setAttribute("aria-label", cell.title);
        cell.addEventListener("click", () => {
          active.element.parentElement.open = true;
          active.element.open = true;
          active.element.querySelector("summary").focus({ preventScroll: true });
          active.element.scrollIntoView({ block: "nearest" });
        });
      } else {
        cell.setAttribute("aria-hidden", "true");
      }
      fragment.append(cell);
    }
    grid.replaceChildren(fragment);
  }

  function render() {
    const selectedAuthor = authorSelect.value;
    const selectedYear = yearSelect.value;
    const activeDays = new Map();
    let total = 0;
    for (const year of years) {
      const visible = year.key === selectedYear;
      year.element.hidden = !visible;
      if (!visible) continue;
      year.element.open = true;
      for (const day of year.days) {
        let daily = 0;
        for (const article of day.articles) {
          article.hidden = selectedAuthor !== "all" && article.dataset.author !== selectedAuthor;
          if (!article.hidden) daily += 1;
        }
        day.element.hidden = daily === 0;
        day.count.textContent = `· ${articleCount(daily)}`;
        if (daily) activeDays.set(day.key, { element: day.element, total: daily });
        total += daily;
      }
      year.element.hidden = total === 0;
    }
    empty.hidden = total !== 0;
    count.textContent = `${articleCount(total)} en ${selectedYear} · ${authorSelect.selectedOptions[0].textContent}`;
    renderGrid(Number(selectedYear), activeDays);
  }

  authorSelect.addEventListener("change", render);
  yearSelect.addEventListener("change", render);
  for (const link of authors) {
    link.addEventListener("click", () => {
      const author = link.dataset.authorFilter;
      const hasArticles = (year) => year.days.some((day) => day.articles.some((article) => article.dataset.author === author));
      if (author !== "all" && !years.some((year) => year.key === yearSelect.value && hasArticles(year))) {
        yearSelect.value = years.find(hasArticles).key;
      }
      authorSelect.value = author;
      render();
    });
    link.previousElementSibling.hidden = true;
    link.hidden = false;
  }
  initRanking();
  render();
  root.querySelector("[data-calendar-panel]").hidden = false;
})();
