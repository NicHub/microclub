---
title: "téléphone : retour à l'analogique"
date: "2008-03-04T07:46:10"
lastmod: "2015-04-24T23:20:21"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["reseau", "telephone"]
url: "/2008/03/04/telephone-retour-a-lanalogique/"
wordpress_id: 39
comment_count: 4
---
Il y a pile 20 ans, je terminais mon diplôme d’ingénieur informaticien à l’EPFL. A l’époque, on arrivait enfin à dépasser la bande passante du téléphone séculaire grâce à la technologie numérique : le Réseau Numérique à Intégration de Services (RNIS, ou ISDN en anglais) allait mettre au rebut nos bons vieux téléphones et ouvrir la voie au monde digital.

Dans notre maison, rénovée il y a 11 ans, j’ai donc fait installer l’e système du futur : nous avions 3 numéros de téléphone et 2 lignes pouvaient être utilisés en même temps. Nous pouvions même voir le numéro de la personne qui nous appelait! Un accès à internet à 64 kbits/s n’en utilisant qu’une, notre téléphone n’était pas bloqué pendant mes longs surfs. La nuit, on pouvait même downloader à la vitesse fulgurante de 128 kbits/s !

L’arrivée de l’ADSL a commencé à poser des problèmes : il fallait un modem spécial ISDN, et installer un « splitter », le tout devant forcément être à la cave à l’arrivée de la ligne. Après avoir tenté d’utiliser un réseau wifi pour accéder à internet depuis le bureau au 2ème étage, j’ai du investir dans un réseau CPL (éthernet sur le réseau électrique) pour y arriver, le tout avec un surcout assez élevé par rapport à une « simple » installation analogique.

Plus récemment, nous avons du changer notre téléphone sans fil, et je me suis aperçu que le choix en ISDN était très restreint alors qu’il existe aujourd’hui des douzaines de téléphones « analogiques » munis de toutes les fonctions numériques disponibles en ISDN.

Le coup de grâce est arrivé il y a quelques semaines. Notre opérateur (Sunrise) propose désormais un bon rabais à ses clients qui combinent abonnement de téléphonie fixe, mobile et ADSL. C’est notre cas. Mais l’offre ne s’applique pas aux clients ISDN !\
Hier, j’ai donc tout viré : le boitier « NT » de l’ISDN que j’avais payé une fortune, le modem Zyxel 660HW-63 et son wifi inutile, le téléphone sans fil Siemens Gigaset CX450 et l’Ascom Eurit 22 avec fil. En 2h chrono, Swisscom m’a remis ma ligne en « analogique » et j’ai refait toute mon installation téléphonique. En passant, bravo (pour une fois) à Swisscom, qui m’a fait ça pile à l’heure prévue, moins d’une semaine après ma demande par téléphone.

La nouvelle installation fonctionne mais n’est pas encore « optimisée » : le modem (Siemens SX763) est toujours à la cave et j’y accède toujours par un réseau CPL qui fait parfois des bulles, et les 2 téléphones sans fil (Siemens Gigaset A265 DUO) sont branchés sur un filtre.

L’étape suivante c’est le VoIP : en raccordant les téléphones directement au modem, celui-ci est capable de router les communications sur internet plutôt que sur le réseau analogique. Malheureusement Skype n’est pas supporté de cette façon, il faudra attendre que Sunrise propose un service VoIP à un tarif intéressant pour les particuliers.

L’ISDN est mort. Cette technologie a permis de doubler la bande passante centenaire du téléphone. 10 ans plus tard, l’ADSL l’a plus que décuplée, ce qui était considéré comme carrément impossible il y a 20 ans. Une petite prédiction ? Un gigabit par seconde dans tous les foyers en 2013 ?

## Commentaires

### Jacques — 19 mars 2008 à 13:37

Il reste encore un avantage à l’ISDN : simultanément à l’ADSL , les 2 conversations téléphoniques restent possibles ! Ce qui est très pratique quand on travaille à domicile …

Par contre l’ISDN a encore un défaut : il ralentit la vitesse de transmission de l’ADSL d’environ 10 %.

Pour l’instant j’attend, peut-être que le dégroupage va enfin faire avancer les choses.

Jacques

### Dr. Goulu — 19 mars 2008 à 15:57

Merci Jacques,\
oui, les 2 lignes simultanées c’était bien quand j’étais indépendant. mais il y a aussi des inconvénients: quand il n’y a qu’une personne à la maison déjà en ligne et que la deuxième ligne sonne… Peu à peu, les natels ont remplacé la 2ème ligne.

Techniquement, pourquoi l’ADSL va moins vite en ISDN ?

### Jacques — 7 avril 2008 à 14:59

Il semble que l’ISDN utilise une bande passante plus grande, donc il en reste moins pour l’ADSL\
Sauf erreur : 2 x 64 Kbts pour les 2 conversations + 16 kbt pour le canal de signalisation.

### ↳ Réponse — denis — 10 septembre 2009 à 03:23

faux.adsl se trouve a une frequence plus haute,il n’a donc aucune interference ni perte.Je suis en isdn,dans ce cas l’adsl utilise l’annexe B.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
