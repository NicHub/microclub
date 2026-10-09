# Cahier des charges — refonte statique de microclub.ch

## 1. Objectif

Remplacer le site WordPress archivé par un site Hugo rapide, actuel, accessible et simple à maintenir dans Git, sans base de données ni interface d’administration. Les textes, informations éditoriales, commentaires historiques et médias utiles sont conservés ; l’ancien thème n’est pas repris.

## 2. Publics et usages

-   visiteurs : découvrir le club, consulter l’agenda, lire et rechercher les archives ;
-   membres : publier un article ou corriger un contenu par Git ;
-   mainteneurs : relire, fusionner et déployer une version statique ;
-   moteurs et lecteurs RSS : retrouver des URL stables, un sitemap et un flux.

## 3. Périmètre fonctionnel

-   accueil éditorial et responsive ;
-   articles classés chronologiquement, par auteur, catégorie et mot-clé ;
-   pages Agenda, Présentation, Photos, Ressources et Contact ;
-   recherche locale côté navigateur, sans service tiers ;
-   flux RSS, sitemap, page 404 et métadonnées essentielles ;
-   publication et commentaires par modification de fichiers Markdown ;
-   conservation des anciennes URL `/AAAA/MM/JJ/slug/`.

Sont exclus : comptes utilisateurs, connexion, formulaire dynamique, base de données, suivi publicitaire et ancien forum dynamique.

## 4. Migration

La branche `httrack-mirror` constitue l’archive immuable. La branche `hugo1` contient la refonte. La migration s’appuie en priorité sur les copies locales de l’API WordPress, puis sur les pages HTML pour les commentaires et mots-clés. Le rapport doit quantifier articles, pages, commentaires, médias copiés et ressources manquantes.

## 5. Ligne visuelle

Identité entièrement renouvelée : mise en page aérée, typographie système performante, palette contrastée, composants sobres et touches graphiques évoquant l’électronique. Aucun composant, CSS, police distante ou habillage WordPress n’est conservé. Le rendu s’adapte au mobile, à la tablette et au bureau.

## 6. Contribution éditoriale

Un article est un fichier Markdown avec titre, date, auteur, catégories et mots-clés. Les médias sont rangés sous `static/media/AAAA/MM/`. Une contribution suit le cycle branche → vérification Hugo → pull/merge request → revue → fusion → déploiement.

Un commentaire est ajouté dans le fichier de l’article sous `## Commentaires`. Cette solution offre historique, attribution et modération avant publication, mais exige un compte sur la forge Git. Aucun contenu sensible ne doit être publié.

## 7. Exigences non fonctionnelles

-   construction reproductible avec Hugo, sans dépendance de thème distante ;
-   fonctionnement sans JavaScript hors recherche ;
-   HTML sémantique, navigation clavier, lien d’évitement et contraste lisible ;
-   images fluides et chargement sans ressources de pistage ;
-   build sans erreur ni avertissement de chemin ;
-   fichiers générés regroupés et ignorés dans `.hugo_nokdrive/` ;
-   thème par défaut isolé sous `themes/` et remplaçable sans modifier les contenus.

## 8. Recette

1. `hugo --gc --printPathWarnings` réussit.
2. Les 301 articles, 7 pages et 311 commentaires archivés sont présents.
3. Les URL historiques principales répondent après génération.
4. La navigation, la recherche, le RSS et la page 404 fonctionnent.
5. Les vues à 360 px, 768 px et 1440 px restent utilisables.
6. Un nouveau contributeur peut publier un article et un commentaire avec la documentation seule.

## 9. Améliorations recommandées

-   ajouter une CI qui compile Hugo et contrôle les liens à chaque proposition ;
-   configurer le dépôt distant dans `params.repository` pour afficher des liens « Modifier cette page » ;
-   automatiser le déploiement atomique (Pages, Netlify ou serveur via rsync) ;
-   convertir progressivement le HTML importé en Markdown propre ;
-   ajouter une licence explicite pour le code et une autre pour les contenus ;
-   formaliser une charte de modération et une politique de conservation des données.
