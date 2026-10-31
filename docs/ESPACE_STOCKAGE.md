# Espace de stockage

## Situation au 31 octobre 2026

### Taille locale

La copie de travail complète occupe environ **2,2 Go**. Cette valeur inclut
des éléments qui ne sont pas envoyés à GitHub :

| Élément                   | Taille approximative | Rôle                                                |
| ------------------------- | -------------------: | --------------------------------------------------- |
| `.git/`                   |               1,4 Go | Historique Git local, références et objets du dépôt |
| `.hugo_nokdrive/`         |               336 Mo | Cache et site généré localement                     |
| `.hugo_nokdrive/public/`  |               335 Mo | Site statique envoyé à GitHub Pages                 |
| Copie de travail complète |               2,2 Go | Total local, y compris les éléments ci-dessus       |

La taille locale ne constitue donc pas la taille du dépôt GitHub. Les autres
worktrees locaux et l'historique du sous-module `themes/blowfish` augmentent
aussi l'occupation sur le disque de développement.

### Dépôt GitHub

L'API GitHub indiquait pour `NicHub/microclub` une taille de **295 040 Ko**,
soit environ **288 Mio**, au 31 octobre 2026. Cette valeur concerne le dépôt
GitHub principal ; le sous-module Blowfish est un dépôt distinct.

GitHub recommande de conserver les dépôts sous **1 Go** et recommande
fortement de rester sous **5 Go**. Il s'agit de recommandations de taille de
dépôt, et non d'une limite stricte à 1 Go. GitHub bloque en revanche les
fichiers individuels de plus de **100 Mio** ; aucun fichier suivi actuellement
ne s'en approche.

### GitHub Pages

Le site publié par GitHub Pages est actuellement d'environ **335 Mo**. La
limite indiquée par GitHub pour un site Pages est de **1 Go**. Il reste donc
environ **650 à 690 Mo** de marge, selon la convention utilisée (Go ou Gio).

La marge à surveiller pour le site est donc celle du dossier généré
`.hugo_nokdrive/public/`, et non celle du répertoire local complet.

### Ce qui reste inconnu

La note ne peut pas déterminer le quota global encore disponible sur le
compte ou l'organisation GitHub, notamment pour les caches et artefacts
GitHub Actions. Ce quota doit être consulté dans les paramètres GitHub,
section **Settings → Billing and licensing**.

### Références

-   [Limites des dépôts GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)
-   [Fichiers volumineux sur GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
-   [Limites de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
