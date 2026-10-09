# Plan — Regrouper les médias avec les articles

## Objectif

Adopter les *page bundles* Hugo pour que chaque nouvel article soit accompagné de ses images et documents, sans casser les 301 articles et les anciennes URL publiques déjà publiées.

## État actuel

- 301 articles sont stockés sous forme de fichiers Markdown simples ;
- aucun article n’est actuellement un bundle Hugo (`index.md`) ;
- 143 articles référencent au moins un fichier dans `static/media/` ;
- `static/media/` contient environ 744 fichiers pour 308 Mo, dont 317 JPG, 269 PNG et 92 PDF ;
- aucun fichier de média référencé n’est partagé par plusieurs articles ;
- certaines pages générales (`presentation.md`, `liens.md`, `contribuer.md`) utilisent aussi `static/media/` ;
- les URL historiques ont la forme `/media/AAAA/MM/fichier.ext`.

## Décision recommandée

1. Utiliser les bundles pour tous les nouveaux articles.
2. Conserver `static/media/` comme espace historique et comme espace partagé pour les pages générales.
3. Ne pas déplacer en masse les médias historiques tant qu’une stratégie de compatibilité des anciennes URL n’est pas validée.
4. Tester toute migration historique sur un petit lot avant de l’étendre.

Cette approche améliore immédiatement l’organisation sans risquer de casser les liens existants.

## Structure cible

```text
content/articles/AAAA/MM/JJ/mon-article/
├── index.md
├── images/
│   ├── featured.svg
│   ├── schema-01.png
│   └── montage.jpg
└── docs/
    ├── presentation.pdf
    └── sources.zip
```

Conventions proposées :

- `images/` : illustrations, photographies, schémas et image à la une ;
- `docs/` : PDF, archives, sources et autres fichiers à télécharger ;
- `featured.*` : nom recommandé pour l’image principale ;
- noms courts, descriptifs, sans espace ni accent ;
- références relatives depuis `index.md`.

Exemples :

```yaml
featureimage: "images/featured.svg"
```

```markdown
![Schéma du montage](images/schema-01.png)

[Télécharger la présentation](docs/presentation.pdf)
```

Le HTML brut importé peut temporairement employer des chemins relatifs :

```html
<img src="images/schema-01.png" alt="Schéma du montage">
<a href="docs/presentation.pdf">Télécharger la présentation</a>
```

Le Markdown natif reste préférable pour les nouveaux contenus.

## Phase 1 — Nouveaux articles

### Mise en place

- [ ] Adapter l’archétype pour créer un bundle contenant `index.md`.
- [ ] Ajouter automatiquement les dossiers `images/` et `docs/`, ou documenter leur création à la demande.
- [ ] Mettre à jour `content/contribuer.md`.
- [ ] Mettre à jour `CONTRIBUTING.md`.
- [ ] Ajouter les conventions de nommage et les exemples de liens relatifs.
- [ ] Vérifier qu’un article sans média peut rester un bundle ne contenant que `index.md`.

### Commande cible

La commande de création devra produire un dossier et non un fichier Markdown isolé. Deux approches sont possibles :

```sh
hugo new content articles/AAAA/MM/JJ/mon-article/index.md
```

ou un script dédié plus simple pour les contributeurs :

```sh
./scripts/new-article.sh "Titre de l’article"
```

Le script dédié est recommandé s’il doit créer les sous-dossiers et normaliser automatiquement le slug.

### Validation de la phase 1

- [ ] Créer un article d’essai avec une image et un PDF.
- [ ] Vérifier l’image dans le corps de l’article.
- [ ] Vérifier le téléchargement du PDF.
- [ ] Vérifier l’image à la une dans les cartes de l’accueil et de la liste des articles.
- [ ] Vérifier les chemins sous la base GitHub Pages `/microclub/`.
- [ ] Vérifier le build de production avec `HUGO_CANONIFYURLS=true`.
- [ ] Supprimer l’article d’essai après validation.

## Phase 2 — Projet pilote sur des articles existants

Cette phase est facultative. Elle ne commence qu’après validation de la phase 1.

### Sélection du lot

Choisir entre un et quatre articles récents, faciles à contrôler. Les quatre articles illustrés récemment constituent un lot candidat :

- Thérémine à la sauce Arduino ;
- RFID_Microclub ;
- GPU et IA ;
- Josephson.

Le pilote peut commencer uniquement par leurs nouvelles illustrations SVG, avant de déplacer leurs nombreux médias historiques.

### Opérations par article

- [ ] Transformer `slug.md` en `slug/index.md` sans modifier son URL publique.
- [ ] Créer `images/` et `docs/`.
- [ ] Déplacer les ressources appartenant uniquement à l’article.
- [ ] Réécrire les références en chemins relatifs.
- [ ] Conserver le front matter, l’auteur, la date, les taxonomies et l’URL explicite.
- [ ] Vérifier les images, téléchargements, métadonnées sociales et cartes.
- [ ] Comparer l’ancienne et la nouvelle page rendue.

### Critères d’arrêt

Arrêter et corriger le pilote si :

- une URL d’article change ;
- une ressource renvoie 404 ;
- une image n’apparaît plus dans une carte ;
- un PDF n’est plus téléchargeable ;
- une ancienne URL `/media/…` doit rester accessible mais ne l’est plus ;
- le build Hugo émet de nouvelles erreurs.

## Phase 3 — Compatibilité des médias historiques

GitHub Pages ne fournit pas de règle de redirection serveur adaptée aux anciennes URL de PDF et d’images. Une migration historique doit donc choisir explicitement une stratégie.

### Option A — Ne pas migrer les anciens médias (recommandée)

- les nouveaux articles utilisent les bundles ;
- les anciens articles continuent d’utiliser `static/media/` ;
- aucun ancien lien n’est cassé ;
- aucune duplication n’est introduite.

### Option B — Migrer avec copies de compatibilité générées

- la source canonique est déplacée dans le bundle ;
- un manifeste associe l’ancienne URL au nouveau fichier ;
- le workflow copie les fichiers concernés dans la sortie générée sous leur ancien chemin `/media/…` ;
- les fichiers ne sont pas dupliqués dans Git, seulement dans l’artefact publié.

Exemple de manifeste :

```yaml
- source: content/articles/2026/09/15/rfid_microclub/docs/RFID_Microclub.pdf
  legacy: media/2026/09/RFID_Microclub.pdf
```

Cette option demande un script de contrôle, une adaptation du workflow et une solution équivalente pour les aperçus locaux. Elle ne doit être choisie que si une migration globale apporte un bénéfice suffisant.

### Option C — Déplacer en cassant les anciennes URL

Déconseillée. Elle nuit aux liens externes, aux favoris, aux moteurs de recherche et aux archives.

## Phase 4 — Migration historique éventuelle

À entreprendre uniquement si l’option B est validée.

- [ ] Produire un inventaire machine : article → ressources utilisées.
- [ ] Détecter les références avec paramètres (`?w=300`), espaces, encodage URL et variantes de casse.
- [ ] Exclure les médias utilisés par les pages générales.
- [ ] Écrire un script reproductible de migration plutôt qu’une série de déplacements manuels.
- [ ] Migrer par petits lots, idéalement année par année.
- [ ] Générer le manifeste de compatibilité.
- [ ] Construire le site après chaque lot.
- [ ] Contrôler automatiquement tous les `src` et `href` locaux.
- [ ] Vérifier que chaque ancienne URL renvoie encore HTTP 200.
- [ ] Créer un commit indépendant par lot pour faciliter le diagnostic et le retour arrière.

## Contrôles automatiques à prévoir

Un script de validation devrait signaler :

- une référence locale vers un fichier inexistant ;
- un média du bundle non référencé ;
- une image sans texte alternatif dans les nouveaux contenus ;
- un chemin absolu `/media/…` ajouté dans un nouvel article ;
- deux ressources portant un nom ambigu dans le même bundle ;
- une entrée de manifeste dont la source n’existe plus ;
- une ancienne URL de compatibilité absente de la sortie publiée.

## Documentation à maintenir

- `archetypes/articles.md` ou le nouvel archétype de bundle ;
- `content/contribuer.md` pour les contributeurs du site ;
- `CONTRIBUTING.md` pour les contributeurs Git ;
- le workflow GitHub Pages si des copies de compatibilité sont retenues ;
- ce document pour noter la stratégie finalement choisie.

## Hors périmètre initial

- déplacer les ressources des pages générales dans des bundles ;
- optimiser ou recompresser automatiquement les 308 Mo de médias historiques ;
- renommer systématiquement tous les anciens fichiers ;
- convertir tout le HTML importé en Markdown ;
- supprimer `static/media/`.

## Ordre recommandé

1. Implémenter uniquement la phase 1.
2. Publier quelques nouveaux articles sous forme de bundles.
3. Mesurer si l’organisation est réellement plus pratique.
4. Effectuer le petit pilote de phase 2.
5. Décider ensuite seulement si les phases 3 et 4 valent leur coût.
