---
title: "Contribuer au site"
url: "/contribuer/"
---

Le site est entièrement géré avec Git. Une proposition est relue avant sa fusion et sa publication.

## Publier un article

1. Créez une branche depuis la branche du site.
2. Copiez `archetypes/articles.md` vers `content/articles/AAAA/MM/JJ/mon-titre.md`.
3. Placez les images ou documents dans `static/media/AAAA/MM/` et référencez-les avec `/media/AAAA/MM/fichier.ext`.
4. Vérifiez le site avec `hugo server`, puis ouvrez une merge/pull request.

## Ajouter un commentaire

Ouvrez le fichier Markdown de l’article concerné, trouvez le titre `## Commentaires`, puis ajoutez à la fin :

```markdown
### Votre nom — 2026-10-08

Votre commentaire.
```

Les commentaires sont donc publics, versionnés, relus et attribuables. N’ajoutez aucune donnée personnelle sensible.
