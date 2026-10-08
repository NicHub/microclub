# Microclub — site Hugo

Version statique moderne de microclub.ch. L’archive HTTrack originale est conservée sur la branche `httrack-mirror`; cette branche contient le site Hugo et les contenus migrés.

## Développement

Prérequis : Hugo Extended récent et Python 3 avec Beautiful Soup uniquement pour rejouer la migration.

```sh
make serve
make build
```

Tous les fichiers de site générés sont regroupés dans `.hugo_nokdrive/` : le site final se trouve dans `.hugo_nokdrive/public/` et les ressources transformées dans `.hugo_nokdrive/resources/`. Aucun CMS, serveur applicatif ou base de données n’est nécessaire.

## Tester un thème

Le thème actif est `themes/microclub-modern/`. Les contenus, médias et paramètres du site restent à la racine, sans `layouts/` ni `assets/` susceptibles d’écraser les fichiers d’un thème alternatif.

Déposez un autre thème dans `themes/<nom>/`, puis lancez :

```sh
make serve THEME=<nom>
# ou, sur macOS :
./scripts/preview-mac.command --theme <nom>
```

Le thème choisi pour ce test ne modifie ni `hugo.toml` ni les contenus. Pour rendre un thème permanent, changez la valeur `theme` dans `hugo.toml`.

## Contenus

- `content/articles/` : 301 articles avec leurs URL historiques ;
- `content/pages/` : pages institutionnelles ;
- `static/media/` : médias réellement référencés par les contenus ;
- `themes/microclub-modern/` : habillage par défaut, isolé et remplaçable ;
- `scripts/migrate_microclub.py` : migration reproductible depuis la branche miroir ;
- `migration-report.json` : bilan automatique de migration.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour publier et [docs/CAHIER_DES_CHARGES.md](docs/CAHIER_DES_CHARGES.md) pour les choix fonctionnels.
