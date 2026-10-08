# Microclub — site Hugo

Version statique moderne de microclub.ch. L’archive HTTrack originale est conservée sur la branche `httrack-mirror`; cette branche contient le site Hugo et les contenus migrés.

## Développement

Prérequis : Hugo Extended récent et Python 3 avec Beautiful Soup uniquement pour rejouer la migration.

```sh
hugo server
hugo --gc --minify
```

Le résultat est écrit dans `public/`. Aucun CMS, serveur applicatif ou base de données n’est nécessaire.

## Contenus

- `content/articles/` : 301 articles avec leurs URL historiques ;
- `content/pages/` : pages institutionnelles ;
- `static/media/` : médias réellement référencés par les contenus ;
- `assets/`, `layouts/` : nouvel habillage ;
- `scripts/migrate_microclub.py` : migration reproductible depuis la branche miroir ;
- `migration-report.json` : bilan automatique de migration.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour publier et [docs/CAHIER_DES_CHARGES.md](docs/CAHIER_DES_CHARGES.md) pour les choix fonctionnels.
