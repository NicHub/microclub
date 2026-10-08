(() => {
  const input = document.querySelector('#search');
  const results = document.querySelector('#search-results');
  const status = document.querySelector('#search-status');
  let index = [];
  fetch('/index.json').then(r => r.json()).then(data => { index = data; status.textContent = 'Prêt à rechercher.'; });
  input.addEventListener('input', () => {
    const words = input.value.toLocaleLowerCase('fr').trim().split(/\s+/).filter(Boolean);
    if (!words.length) { results.replaceChildren(); status.textContent = ''; return; }
    const found = index.filter(item => words.every(word => `${item.title} ${item.author} ${item.text} ${item.terms}`.toLocaleLowerCase('fr').includes(word))).slice(0, 30);
    status.textContent = `${found.length} résultat${found.length > 1 ? 's' : ''}`;
    results.replaceChildren(...found.map(item => {
      const article = document.createElement('article');
      const heading = document.createElement('h2');
      const link = document.createElement('a'); link.href = item.url; link.textContent = item.title; heading.append(link);
      const meta = document.createElement('p'); meta.className = 'eyebrow'; meta.textContent = `${item.date}${item.author ? ` · ${item.author}` : ''}`;
      const text = document.createElement('p'); text.textContent = item.text;
      article.append(meta, heading, text); return article;
    }));
  });
})();
