---
title: "Emulation en JavaScript"
date: "2013-06-01T18:47:58"
lastmod: "2015-04-24T23:20:17"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["emulation", "javascript"]
url: "/2013/06/01/emulation-en-javascript/"
wordpress_id: 1249
comment_count: 3
---
Poursuivant ma quête de pages web capables de faire tourner des programmes antédiluviens ou de petites créations vite faites sur le gaz, je suis tombé sur [repl.it](http://repl.it/languages) . Ce site permet d’exécuter du code dans le bon vieux mode « [Read Eval Print Loop](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)« , mais ce qui a titillé ma curiosité, c’est le nombre et la variété des langages supportés. Outre différents dialectes de JavaScript, il y a mon cher Python, mais aussi Ruby, Lua, Scheme (un LISP moderne) et ces bons vieux Forth et QBasic !

Or tout ceci ne tourne pas sur le serveur, mais bien sur votre machine, dans une page web. Comment font-ils ? la réponse figure dans <http://repl.it/help> : ils utilisent un truc qui s’appelle « emscripten ».

![](https://a248.e.akamai.net/camo.github.com/b13f9c10472ae855af98d549d5bb47c3b3ec486c/687474703a2f2f646c2e64726f70626f782e636f6d2f752f38303636343934362f656d736372697074656e5f6c6f676f2e6a7067)

Et [emscripten](https://github.com/kripken/emscripten/wiki), c’est de la tuerie. Cette chose traduit en javsacript du code [LLVM](http://fr.wikipedia.org/wiki/LLVM), un code intermédiaire entre le « haut niveau » et l’assembleur, généré par certains compilateurs comme [clang](http://fr.wikipedia.org/wiki/Clang) par exemple.

En gros, avec emscripten on peut exécuter sur une page web du code C/C++ compilé, donc on peut exécuter [CPython](http://fr.wikipedia.org/wiki/CPython) ou les autres interpréteurs.

Pour QBasic c’est un peu différent : repl.it utilise [qb.js](http://stevehanov.ca/blog/index.php?id=92) un interpréteur écrit directement en JavaScript par Steve Hanov. Sur [sa page](http://stevehanov.ca/blog/index.php?id=92) on trouve une version complète de son émulateur QBasic qui gère même les « graphiques » en couleur utilisant les bons vieux caractères de l’IBM PC, mais surtout des infos sur la manière dont est fait son interpréteur, avec une remarque intéressante: Javascript est très efficace pour ce genre de choses.

emscripten permet aussi de porter en technologie web des applications conçues initialement pour d’autres plateformes, donc de les rendre multiplateforme de-facto. Il y a par exemple déjà

- des outils comme SQlite, LaTEX, gnuplot ou graphviz, prêt à être intégrés dans des applications web
- la [plateforme Qt](http://fr.wikipedia.org/wiki/Qt). Avec ça, [plein d’applications](http://vps2.etotheipiplusone.com:30176/redmine/projects/emscripten-qt/wiki/Demos) écrites pour des OS variés peuvent tourner dans des pages web
- des jeux allant de [ce petit jeu sympa et désuet](http://noctua-software.com/voxel-invaders/play) à [Epic Citadel](http://www.unrealengine.com/en/showcase/mobile/epic_citadel/), un jeu très pro construit sur le moteur graphique Unreal 3, porté en 4 jours en Javascript, ce qui lui permet de [tourner sur Firefox](http://www.unrealengine.com/html5/)
- des émulateurs de hardware obsolète comme MAME ou MESS :

<!-- -->

<!-- -->

- si vous téléchargez [Robby roto and friends](https://chrome.google.com/webstore/detail/robby-roto-and-friends-vi/kcfbijoldkenmemnbbkjnpdhnijgahck?hl=en-US) pour Chrome, vous obtenez en réalité le le [Multi Arcade  Machine Emulator](http://mamedev.org/) capable d’émuler un nombre incroyable de jeux d’arcade d’époque pour autant que vous lui fournissiez un fichier contenant la ROM d’époque. MAME porté en JS arrive donc à émuler en temps réel les processeurs Z80, 6502 etc de ce bon vieux temps4. Ce portage a été [fait par des googlers](https://developers.google.com/native-client/community/porting/MAME)…
- le projet [jsmess](http://jsmess.textfiles.com/) webifie quant à lui  le [Multi Emulator Super System](http://www.mess.org/) capable d’émuler d’autres machines d’époque. La version Javascript supporte déjà [Atari 2600](http://jsmess.textfiles.com/messbeta.html?module=atari2600)·[ColecoVision](http://jsmess.textfiles.com/messbeta.html?module=colecovision)·[Fairchild Channel F](http://jsmess.textfiles.com/messbeta.html?module=channelf), [Odyssey2](http://jsmess.textfiles.com/messbeta.html?module=odyssey2)·[Sega Genesis](http://jsmess.textfiles.com/messbeta.html?module=genesis) et la [Texas Instruments 99 4/a](http://jsmess.textfiles.com/messbeta.html?module=ti99_4) , et [d’autres bientôt](https://github.com/jsmess/jsmess/wiki/status) !

Pour ma part je tire plusieurs leçons de ce qui est en train de se passer:

1. le hardware devient obsolète plus vite que le soft, qui peut survivre grâce à l’émulation du hardware
2. la frontière entre système d’exploitation et applications et entre compilation et interprétation disparaît complètement
3. quand le browser sera la seule et unique fenêtre ouverte sur un PC, pourquoi faudra-t-il encore des fenêtres ? et un PC ?

## Commentaires

### Marc — 5 juin 2013 à 21:02

Pourquoi sur ce site tous les accents sont faux??? Pas UTF8?. C’est illisible sur iphone

### ↳ Réponse — Goulu — 6 juin 2013 à 04:56

ça a l’air d’être le truc sensé formatter pour les mobiles, le site « full » est ok… j’investigue…

### ↳ Réponse — Goulu — 6 juin 2013 à 05:15

voilà trouvé : il y avait deux extensions pour mobile qui se marchaient dessus. J’en ai enlevé une, et ça marche sur mon Samsung… Merci de l’avoir signalé !

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
