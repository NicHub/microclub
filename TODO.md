# À faire

## Fiches utilisateur, avatars et commentaires

À étudier ultérieurement.

Le site étant statique, distinguer les fiches d’auteur des comptes de connexion.

### 1. Fiches d’auteur Blowfish

Utiliser la prise en charge native des auteurs multiples de Blowfish. Chaque membre pourrait avoir :

- un nom public ;
- un avatar ;
- une courte biographie ;
- éventuellement des liens ;
- une page regroupant ses articles.

Structure envisagée :

```text
data/authors/rolf-ziegler.json
content/authors/rolf-ziegler/_index.md
assets/images/authors/rolf-ziegler.jpg
```

Référence dans un article :

```yaml
authors:
  - rolf-ziegler
```

Migrer progressivement l’actuel champ :

```yaml
author: "Rolf Ziegler"
```

vers une clé d’auteur stable. Afficher l’avatar dans la carte auteur et faire pointer le nom vers sa fiche.

### 2. Commentaires

#### Option A — Giscus (recommandée)

- connexion avec un compte GitHub ;
- avatar GitHub automatique ;
- commentaires stockés dans GitHub Discussions ;
- modération disponible ;
- aucun serveur ni base de données à maintenir.

Limite : les visiteurs doivent posséder un compte GitHub et leur profil GitHub reste distinct de leur fiche Microclub.

#### Option B — Commentaires associés aux fiches Microclub

Stocker les commentaires dans les articles avec une clé d’auteur, par exemple :

```go
{{< comment author="rolf-ziegler" date="2026-10-09" >}}
Texte du commentaire.
{{< /comment >}}
```

Le commentaire afficherait le même avatar que les articles.

Avantages :

- identité visuelle cohérente ;
- aucune dépendance extérieure ;
- commentaires conservés dans Git.

Limites :

- pas de formulaire public direct ;
- ajout et validation des commentaires via Git ;
- un véritable espace de connexion nécessiterait un service externe.

### 3. Commentaires historiques

Les 311 commentaires importés pourraient recevoir un avatar lorsque leur nom correspond avec certitude à une fiche. Conserver un avatar générique pour les auteurs inconnus ou ambigus.

### Mise en œuvre conseillée

- [ ] Créer les fiches d’auteur Blowfish avec avatars.
- [ ] Définir les clés stables des auteurs existants.
- [ ] Migrer les articles de `author` vers `authors`.
- [ ] Choisir entre Giscus et les commentaires stockés dans Git.
- [ ] Associer les commentaires historiques identifiables aux fiches.
- [ ] Utiliser un avatar générique pour les autres commentaires.

Orientation recommandée : fiches d’auteur Blowfish pour les articles, puis Giscus pour les nouveaux commentaires.
