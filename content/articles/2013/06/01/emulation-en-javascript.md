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
<p>Poursuivant ma quête de pages web capables de faire tourner des programmes antédiluviens ou de petites créations vite faites sur le gaz, je suis tombé sur <a href="http://repl.it/languages">repl.it</a> . Ce site permet d’exécuter du code dans le bon vieux mode « <a href="http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop">Read Eval Print Loop</a>« , mais ce qui a titillé ma curiosité, c’est le nombre et la variété des langages supportés. Outre différents dialectes de JavaScript, il y a mon cher Python, mais aussi Ruby, Lua, Scheme (un LISP moderne) et ces bons vieux Forth et QBasic !</p>
<p>Or tout ceci ne tourne pas sur le serveur, mais bien sur votre machine, dans une page web. Comment font-ils ? la réponse figure dans <a href="http://repl.it/help">http://repl.it/help</a> : ils utilisent un truc qui s’appelle « emscripten ».</p>
<p><img alt="" height="125" src="https://a248.e.akamai.net/camo.github.com/b13f9c10472ae855af98d549d5bb47c3b3ec486c/687474703a2f2f646c2e64726f70626f782e636f6d2f752f38303636343934362f656d736372697074656e5f6c6f676f2e6a7067" width="350"/></p>
<p>Et <a href="https://github.com/kripken/emscripten/wiki" target="_blank">emscripten</a>, c’est de la tuerie. Cette chose traduit en javsacript du code <a href="http://fr.wikipedia.org/wiki/LLVM" target="_blank">LLVM</a>, un code intermédiaire entre le « haut niveau » et l’assembleur, généré par certains compilateurs comme <a href="http://fr.wikipedia.org/wiki/Clang" target="_blank">clang</a> par exemple.</p>
<p>En gros, avec emscripten on peut exécuter sur une page web du code C/C++ compilé, donc on peut exécuter <a href="http://fr.wikipedia.org/wiki/CPython">CPython</a> ou les autres interpréteurs.</p>
<p>Pour QBasic c’est un peu différent : repl.it utilise <a href="http://stevehanov.ca/blog/index.php?id=92" target="_blank">qb.js</a> un interpréteur écrit directement en JavaScript par Steve Hanov. Sur <a href="http://stevehanov.ca/blog/index.php?id=92" target="_blank">sa page</a> on trouve une version complète de son émulateur QBasic qui gère même les « graphiques » en couleur utilisant les bons vieux caractères de l’IBM PC, mais surtout des infos sur la manière dont est fait son interpréteur, avec une remarque intéressante: Javascript est très efficace pour ce genre de choses.</p>
<p>emscripten permet aussi de porter en technologie web des applications conçues initialement pour d’autres plateformes, donc de les rendre multiplateforme de-facto. Il y a par exemple déjà</p>
<ul>
<li>des outils comme SQlite, LaTEX, gnuplot ou graphviz, prêt à être intégrés dans des applications web</li>
<li>la <a href="http://fr.wikipedia.org/wiki/Qt" target="_blank">plateforme Qt</a>. Avec ça, <a href="http://vps2.etotheipiplusone.com:30176/redmine/projects/emscripten-qt/wiki/Demos" target="_blank">plein d’applications</a> écrites pour des OS variés peuvent tourner dans des pages web</li>
<li>des jeux allant de <a href="http://noctua-software.com/voxel-invaders/play" target="_blank">ce petit jeu sympa et désuet</a> à <a href="http://www.unrealengine.com/en/showcase/mobile/epic_citadel/" target="_blank">Epic Citadel</a>, un jeu très pro construit sur le moteur graphique Unreal 3, porté en 4 jours en Javascript, ce qui lui permet de <a href="http://www.unrealengine.com/html5/" target="_blank">tourner sur Firefox</a></li>
<li>des émulateurs de hardware obsolète comme MAME ou MESS :</li>
</ul>
<ul>
</ul>
<ul>
<li>si vous téléchargez <a href="https://chrome.google.com/webstore/detail/robby-roto-and-friends-vi/kcfbijoldkenmemnbbkjnpdhnijgahck?hl=en-US">Robby roto and friends</a> pour Chrome, vous obtenez en réalité le le <a href="http://mamedev.org/" target="_blank">Multi Arcade  Machine Emulator</a> capable d’émuler un nombre incroyable de jeux d’arcade d’époque pour autant que vous lui fournissiez un fichier contenant la ROM d’époque. MAME porté en JS arrive donc à émuler en temps réel les processeurs Z80, 6502 etc de ce bon vieux temps4. Ce portage a été <a href="https://developers.google.com/native-client/community/porting/MAME" target="_blank">fait par des googlers</a>…</li>
<li>le projet <a href="http://jsmess.textfiles.com/">jsmess</a> webifie quant à lui  le <a href="http://www.mess.org/">Multi Emulator Super System</a> capable d’émuler d’autres machines d’époque. La version Javascript supporte déjà <a href="http://jsmess.textfiles.com/messbeta.html?module=atari2600">Atari 2600</a>·<a href="http://jsmess.textfiles.com/messbeta.html?module=colecovision">ColecoVision</a>·<a href="http://jsmess.textfiles.com/messbeta.html?module=channelf">Fairchild Channel F</a>, <a href="http://jsmess.textfiles.com/messbeta.html?module=odyssey2">Odyssey2</a>·<a href="http://jsmess.textfiles.com/messbeta.html?module=genesis">Sega Genesis</a> et la <a href="http://jsmess.textfiles.com/messbeta.html?module=ti99_4">Texas Instruments 99 4/a</a> , et <a href="https://github.com/jsmess/jsmess/wiki/status" target="_blank">d’autres bientôt</a> !</li>
</ul>
<p>Pour ma part je tire plusieurs leçons de ce qui est en train de se passer:</p>
<ol>
<li><span>le hardware devient obsolète plus vite que le soft, qui peut survivre grâce à l’émulation du hardware</span></li>
<li>la frontière entre système d’exploitation et applications et entre compilation et interprétation disparaît complètement</li>
<li>quand le browser sera la seule et unique fenêtre ouverte sur un PC, pourquoi faudra-t-il encore des fenêtres ? et un PC ?</li>
</ol>

## Commentaires

### Marc — 5 juin 2013 à 21:02

<section class="comment-content comment">
<p>Pourquoi sur ce site tous les accents sont faux??? Pas UTF8?.  C’est illisible sur iphone</p>
 </section>

### ↳ Réponse — Goulu — 6 juin 2013 à 04:56

<section class="comment-content comment">
<p>ça a l’air d’être le truc sensé formatter pour les mobiles, le site « full » est ok… j’investigue…</p>
 </section>

### ↳ Réponse — Goulu — 6 juin 2013 à 05:15

<section class="comment-content comment">
<p>voilà trouvé : il y avait deux extensions pour mobile qui se marchaient dessus. J’en ai enlevé une, et ça marche sur mon Samsung… Merci de l’avoir signalé !</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
