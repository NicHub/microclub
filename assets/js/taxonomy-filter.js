document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("taxonomy-filter");
  const grid = document.getElementById("taxonomy-tag-grid");
  const count = document.getElementById("taxonomy-filter-count");
  const empty = document.getElementById("taxonomy-filter-empty");

  if (!input || !grid || !count || !empty) return;

  const tags = Array.from(grid.querySelectorAll(".taxonomy-tag"));
  const normalize = (value) =>
    value
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLocaleLowerCase("fr");

  function filterTags() {
    const query = normalize(input.value.trim());
    let visible = 0;

    tags.forEach(function (tag) {
      const matches = normalize(tag.dataset.taxonomyName || "").includes(query);
      tag.classList.toggle("hidden", !matches);
      if (matches) visible += 1;
    });

    count.textContent = `${visible} ${visible === 1 ? "mot-clé affiché" : "mots-clés affichés"}`;
    grid.classList.toggle("hidden", visible === 0);
    empty.classList.toggle("hidden", visible !== 0);
  }

  input.addEventListener("input", filterTags);
  input.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && input.value) {
      input.value = "";
      filterTags();
    }
  });
});
