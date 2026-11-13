---
title: "HUGO & OPENCODE — Créer et gérer un site web entièrement avec l’IA"
date: "2026-11-13T19:00:00"
publishDate: "2026-11-11T20:00:00"
lastmod: "2026-11-13T19:00:00"
author: "Nicolas Jeanmonod"
featureimage: "images/cover.png"
categories: ["Microclub"]
tags: ["Hugo", "OpenCode", "IA", "site web", "conférence"]
url: "/2026/11/13/conference-hugo-opencode/"
draft: false
outputs: ["HTML", "slides"]
showPresentation: true
showReadingTime: false
showWordCount: false
showTableOfContents: false
showHeadingAnchors: false
showPagination: false
---

Salut Jean-Marc !

{{< comment >}}

    ## DÉSACTIVE CERTAINES NOTIFICATIONS MarkdownLint

    -   MD046 - Code block style
        <https://github.com/DavidAnson/markdownlint/blob/v0.41.1/doc/md046.md>
        <!-- markdownlint-disable MD046 -->

{{< /comment >}}

![Cover][cover]

---

## MICRoCLUB

![Logo HUGO][logo-hugo]

![Logo OpenCode][logo-opencode]

> Nicolas Jeanmonod · Microclub · EPFL · 13 novembre 2026

---

![Logo HUGO][logo-hugo]

[gohugo.io]

---

### [Hugo]

[Hugo] est un générateur de sites web statiques.

---

## Quelques méthodes de génération de sites web

---

### À la main, en écrivant chaque fichier

HTML, CSS, JS

![Créer un site web à la main][categorie-a-la-main]

---

### Avec un constructeur visuel / no-code

**Desktop :** Microsoft FrontPage, Adobe Dreamweaver, Pinegrow,...

**Cloud :** Wix, Squarespace, Webflow, Framer,...

![Créer un site avec un constructeur visuel][categorie-no-code]

---

### Avec un CMS

WordPress, Joomla,...

![Créer un site avec un CMS][categorie-cms]

---

### Avec un générateur de sites statiques

[Hugo], [Jekyll], [Quarto],…

![Générer un site statique][categorie-site-statique]

---

## Avantages d’un générateur de sites statiques

---

### Simple à comprendre et à maintenir

_Les pages sont de simples fichiers texte au [format Markdown]._

![De Markdown à HTML, CSS et JavaScript avec Hugo][md-hugo-html-css-js]

---

### Versionnable avec Git

Les fichiers texte rendent l’utilisation de Git possible :

-   versionnage
-   collaboration
-   synchronisation

![Logo Git][logo-git]

---

### Rapide à générer et à servir

_Surtout avec Hugo._

![Rapidité d’un générateur de sites statiques][avantage-rapidite]

---

### Peu coûteux à héberger

_Un “petit” site est hébergé gratuitement sur des forges comme GitHub._

![Faible coût d’hébergement][avantage-cout]

---

### Plus sûr

Pas de base de données ni de code serveur à protéger.

_Par exemple, insensible à [PHP2Shell][php2shell] : deux failles critiques permettant l’exécution de code à distance sans authentification._

![Sécurité d’un site statique][avantage-securite]

---

### Rapide à distribuer

Les fichiers sont générés à l’avance.

![Diffusion rapide de fichiers statiques][avantage-diffusion]

---

### Matrice de comparaison des méthodes

| Paramètre             | À la main                                      | Constructeur visuel /<br>no-code  | CMS                                          | Générateur de sites statiques |
| --------------------- | ---------------------------------------------- | --------------------------------- | -------------------------------------------- | ----------------------------- |
| Vitesse de diffusion  | rapide                                         | dépend de l’hébergement           | limitée par le serveur et la base de données | **très rapide**               |
| Complexité            | élevée, nécessite des connaissances techniques | faible à moyenne                  | moyenne                                      | moyenne à élevée              |
| Base de données       | non                                            | généralement gérée par le service | souvent nécessaire                           | non                           |
| Vitesse de génération | immédiate, fichier par fichier                 | dépend du service                 | limitée par le serveur et la base de données | limitée par la durée du build |
| Pages générées        | en avance                                      | selon le service                  | à la demande                                 | en avance                     |

Mais là où les sites web statiques sont imbatables, c’est la facilité avec laquelle on peut les générer avec des agents IA.

---

### Installation de Hugo sur Windows

Pour installer Hugo, exécutez cette commande dans PowerShell :

```shell
winget install -e --id Hugo.Hugo.Extended
```

Je vous conseille aussi d’installer ces programmes

```shell
winget install -e --id Git.Git
winget install -e --id PedroAlbanese.QREncode
```

---

### Installation de Hugo sur macOS

```shell
brew install hugo git qrencode
```

---

### Installation de Hugo sur Ubuntu

```shell
sudo apt update
sudo apt install hugo qrencode
```

---

![Logo OpenCode][logo-opencode]

[opencode.ai]

---

### OpenCode

[OpenCode] est un agent de codage fondé sur l’IA.

Il est comparable à [Codex], [Claude Code] ou [Gemini CLI], mais s’en distingue par une possibilité fondamentale :

**il permet de choisir parmi plusieurs fournisseurs de modèles d’IA.**

Le catalogue [models.dev] utilisé par [OpenCode] recense actuellement plus de **9 000 modèles** proposés par plus de **230 fournisseurs**.

Au 13 novembre 2026, il comptabilise précisément **9 136 modèles** et **236 fournisseurs**. Ces chiffres évoluent
continuellement ; le catalogue à jour est consultable sur [models.dev].

On peut ainsi passer d’un fournisseur à l’autre au cours d’une même conversation.

_**Attention à cette limitation ! :**_\
_**[Anthropic] n’autorise l’accès qu’au moyen de son API, et non par authentification directe.**_

---

## Les grandes catégories d’assistants IA

Du chatbot à l’agent, en très simplifié.

1. Chatbot (Assistant conversationnel)
2. Chatbot outillé
3. Agent

---

### 1. Chatbot (Assistant conversationnel)

-   Répond aux questions

#### Exemples

-   ChatGPT ¹ ²
-   Claude ¹ ²
-   Gemini ¹ ²

####

_¹ navigateur web_\
_² application desktop_\
_³ TUI (interface en terminal)_

---

### 2. Chatbot outillé

-   Fait tout ce que fait un chatbot
-   Recherche des informations
-   Utilise des applications à la demande
-   Peut modifier des fichiers

#### Exemples

-   ChatGPT avec recherche web ¹ ²
-   Claude Desktop avec [MCP] ²
-   Gemini avec extensions ¹

####

_¹ navigateur web_\
_² application desktop_\
_³ TUI (interface en terminal)_

---

### 3. Agent

-   Fait tout ce que fait un chatbot outillé
-   Poursuit un objectif
-   Enchaîne des actions
-   Adapte son travail selon les résultats
-   Peut vérifier ses résultats et corriger ses erreurs

#### Exemples

-   OpenCode ³
-   Codex ² ³
-   Claude Code ³

####

_¹ navigateur web_\
_² application desktop_\
_³ TUI (interface en terminal)_

---

## Les trois couches d’un système d’IA

Du prompt à l’environnement d’exécution, dans les grandes lignes.

Ces catégories forment un continuum : un assistant peut être progressivement doté d’outils et d’autonomie jusqu’à devenir un agent.

1. Prompt engineering
2. Context engineering
3. Harness engineering

---

### 1. Prompt engineering

-   Le prompt = les instructions
-   Que doit faire l’IA ?
-   Bien formuler les instructions données à l’IA

popularisé entre 2020 et 2022

---

### 2. Context engineering

-   Le contexte  = les informations disponibles
-   Que doit savoir l’IA ?
-   Fournir à l’IA les informations pertinentes au bon moment

popularisé en 2025

---

### 3. Harness engineering

-   Le harnais  = les outils, l’environnement et les contrôles
-   De quoi dispose l’IA pour travailler ?
-   Concevoir l’environnement et les outils qui permettent à l’IA d’agir efficacement
-   Prévoir les mécanismes de contrôle, de vérification des résultats et de gestion des erreurs

popularisé en 2026

---

## Pour situer ces systèmes

| Aspect                 |          Chatbot          | Chatbot outillé |         Agent         |
| ---------------------- | :-----------------------: | :-------------: | :-------------------: |
| Prompt                 |             ×             |        ×        |           ×           |
| Contexte               |                           |        ×        |           ×           |
| Harnais                |                           |        ×        |           ×           |
| Production de code     |     te donne du code      |                 | modifie tes fichiers  |
| Connaissance du projet | ne connaît pas ton projet |                 |     lit ton dépôt     |
| Mode d’interaction     |     tu copies-colles      |                 | il exécute et vérifie |
| Fonctionnement         |        une réponse        |                 |      une boucle       |

Dans cette classification, [OpenCode] est donc un agent.

---

## Note sur le type d’agents

[OpenCode] est un agent de codage.

Il peut orchestrer plusieurs agents spécialisés, notamment _Plan_ pour concevoir et _Build_ pour réaliser.

On peut voir [OpenCode] comme le système d’orchestration, et _Build_ et _Plan_ comme deux modes de fonctionnement agentiques configurables.

---

## Avantage décisif

S’il ne fallait retenir qu’une chose de cette conférence, ce serait celle-ci :

### Un agent peut utiliser un programme en ligne de commande (CLI)

Et cela sans qu’on lui explique à l’avance chaque étape.

Il peut ~~RTFM~~ consulter la documentation du logiciel, découvrir les commandes utiles et les exécuter pour vous.

Pas besoin d’intégrations spécialisées comme [MCP], des plugins ou des API dédiées.

---

<!--

## La marche du progrès de Rudolph F. Zallinger, 1965

-   <https://en.wikipedia.org/wiki/March_of_Progress>
-   <https://fr.wikipedia.org/wiki/Marche_du_Progr%C3%A8s>

Voir aussi:

> Ce qu’on a appris à l’école et qui n’est plus vrai aujourd’hui\
> Scilabus\
> <https://www.youtube.com/watch?v=rB-s51uPACc>

 -->

## Aparté sur l’évolution ultrarapide de l’intelligence artificielle

---

### L’évolution en 6 étapes

![La marche du progrès en 6 étapes][marche-du-progres-6]

L’évolution humaine est souvent présentée avec cette frise en 6 étapes

---

### L’évolution en 15 étapes

![La marche du progrès en 15 étapes][marche-du-progres-15]

Cette frise célèbre nous induit en erreur de plusieurs façons :

-   On oublie que la frise originale de 1965 réalisée par Zallinger comportait en fait 15 étapes.
-   Seuls des mâles sont représentés.
-   Certaines espèces ont évolué sans laisser de descendance et ne peuvent donc pas être représentées dans une lignée unique, mais plutôt comme des embranchements.
-   Certaines espèces ont coexisté et ont même pu se reproduire entre elles.\
  Elles ne devraient pas être représentées à la suite, mais côte-à-côte.

---

### L’évolution en réalité

![La marche du progrès — version réaliste][marche-du-progres-2026]

Mais rappelons nous que la réalité est un peu plus complexe.

> Source :\
> Ce qu’on a appris à l’école et qui n’est plus vrai aujourd’hui\
> Scilabus\
> <https://www.youtube.com/watch?v=rB-s51uPACc>

---

### En attendant l’IApocalypse…

![La marche du progrès inversée en 7 étapes][marche-du-progres-2026-inversee-v3]

En conclusion, prenez avec des pincettes mes explications sur les IA, elles sont déjà très simplifiées aujourd’hui et seront probablement obsolètes dans pas longtemps...\
...et nous aussi peut-être

> Illustration de ChatGPT, inspirée de [Cagle Cartoons][source-marche-du-progres]

---

### Installation de OpenCode

Télécharger depuis

<https://opencode.ai/product>

N.B. La version Desktop contient la version terminal.

---

## SiteSucker & httrack

---

[![Logo SiteSucker][logo-sitesucker]][SiteSucker]

[SiteSucker]

[![Logo HTTrack][logo-httrack]][HTTrack]

[HTTrack]

---

[SiteSucker] et [HTTrack] sont des [aspirateurs de sites Web][aspirateur-de-site-web] que j’ai utilisés pour préparer la génération des sites que je vais vous montrer.

J’utilise [SiteSucker] depuis longtemps et il marche super bien, mais avec [opencode], je privilégie les programmes en ligne de commande et c’est pour ça que j’essaie [HTTrack] (_cf. avantage décisif_).

---

## Herdr

![Logo HERDR][logo-herdr]

[herdr.dev]

---

[Herdr] est un multiplexeur de terminal.

Il remplace des solutions traditionnelles comme [GNU Screen] ou [tmux].

Des compétiteurs sérieux se pressent au portillon :

-   [tuios]
-   [rex]
-   [cmux] _(macOS)_

---

## Démo


---

## Conclusion

Ce site n’a pas été écrit par une IA.

Il a été écrit par un membre du Microclub, avec une IA.

La différence, c’est la responsabilité.

> Et si ChatGPT le dit, c’est que ça doit être vrai _🤭_

---

## Ressources

-   [microclub.ch][microclub.ch]
-   [gohugo.io][gohugo.io]
-   [blowfish.page][blowfish.page]
-   [opencode.ai][opencode.ai]
-   [github.com/NicHub/microclub][github-microclub]
-   [hypnodingues.org/posts/2026-03-30-l-echelle-dalia/][echelle-dalia]
-   [hypnodingues.org/posts/2026-04-10-les-dangers-des-ia/][dangers-des-ia]

---

> Nicolas Jeanmonod • MICRoCLUB • 13 novembre 2026
>
> [Dalia D3][echelle-dalia]

[gohugo.io]: https://gohugo.io/
[microclub.ch]: https://microclub.ch
[blowfish.page]: https://blowfish.page
[Hugo]: https://gohugo.io/
[Jekyll]: https://jekyllrb.com/
[Quarto]: https://quarto.org/
[OpenCode]: https://opencode.ai/
[opencode.ai]: https://opencode.ai/
[github-microclub]: https://github.com/NicHub/microclub
[echelle-dalia]: https://hypnodingues.org/posts/2026-03-30-l-echelle-dalia/
[dangers-des-ia]: https://hypnodingues.org/posts/2026-04-10-les-dangers-des-ia/
[herdr.dev]: https://herdr.dev/
[Herdr]: https://herdr.dev/
[GNU Screen]: https://www.gnu.org/software/screen/
[tmux]: https://github.com/tmux/tmux
[cmux]: https://github.com/manaflow-ai/cmux
[tuios]: https://tuios.dev/
[rex]: https://www.superlogical.com/rex
[cover]: images/cover.png
[logo-hugo]: images/logo-hugo.webp
[logo-opencode]: images/opencode-wordmark-dark.svg
[categorie-a-la-main]: images/categorie-a-la-main.png
[categorie-no-code]: images/categorie-no-code.png
[categorie-cms]: images/categorie-cms.png
[categorie-site-statique]: images/categorie-site-statique.png
[logo-git]: images/logo-git.svg
[avantage-rapidite]: images/avantage-rapidite.png
[avantage-cout]: images/avantage-cout.png
[avantage-securite]: images/avantage-securite.png
[avantage-diffusion]: images/avantage-diffusion.png
[marche-du-progres-6]: images/la-marche-du-progres-1965-6-etapes.jpg
[marche-du-progres-15]: images/la-marche-du-progres-1965-15-etapes.jpg
[marche-du-progres-2026]: images/la-marche-du-progres-2026.jpg
[marche-du-progres-2026-inversee-v3]: images/la-marche-du-progres-2026-inversee-v3.png
[logo-herdr]: images/logo-herdr.svg
[md-hugo-html-css-js]: images/md-hugo-html-css-js.png
[Codex]: https://openai.com/codex/
[Claude Code]: https://www.anthropic.com/claude-code
[Gemini CLI]: https://github.com/google-gemini/gemini-cli
[Anthropic]: https://www.anthropic.com/
[models.dev]: https://models.dev/
[logo-sitesucker]: images/logo-sitesucker.png
[logo-httrack]: images/logo-httrack.svg
[SiteSucker]: https://ricks-apps.com/osx/sitesucker/
[HTTrack]: https://www.httrack.com/
[source-marche-du-progres]: https://caglecartoons.com/sku/302452?utm_source=chatgpt.com
[aspirateur-de-site-web]: https://fr.wikipedia.org/wiki/Aspirateur_de_site_web
[php2shell]: https://php2shell.com/
[MCP]: https://fr.wikipedia.org/wiki/Model_Context_Protocol
[format Markdown]: https://www.markdownlang.com/fr/extended/
