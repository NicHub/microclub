---
title: "4 coeurs c'est mieux que 2, parfois."
date: "2008-04-19T20:02:00"
lastmod: "2015-04-24T23:20:21"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["hardware", "processeurs"]
url: "/2008/04/19/4-coeurs-cest-mieux-que-2-parfois/"
wordpress_id: 41
comment_count: 4
---
![](http://upload.wikimedia.org/wikipedia/en/thumb/d/da/Cell_Broadband_Engine_Processor.jpg/436px-Cell_Broadband_Engine_Processor.jpg)A peine s’est-on habitués à l’idée d’avoir des processeurs à double coeur dans nos PC que les quadruple coeurs ([Intel Core 2 Quad](http://www.intel.com/cd/products/services/emea/fra/processors/core2quad/333916.htm) ou  [AMD Opteron Quad Core](http://multicore.amd.com/us-en/quadcore/)) débarquent dans les PC haut de gamme, et bientôt sur nos bureaux.

Si le double coeur apporte sans conteste un gain de confort (un coeur pour Windows, un autre pour l’application …), il faut reconnaitre que très peu d’applications sont capables de tirer parti du gain de performance qu’apportent théoriquement deux unités de calcul. Que dire pour quatre ?

L’article « [Choosing Dual or Quad Core](http://www.codinghorror.com/blog/archives/000942.html) » de Jeff Atwood donne une réponse simple après de nombreux tests : « ça dépend ».

Certaines applications vont presque 2x plus vite avec 4 coeurs qu’avec 2 : elles sont parfaitement parallélisées, avec des processus très indépendants ne nécessitant que très peu de communication entre eux. [Pov-Ray](http://www.povray.org/), certains benchmarks et des modules de jeux comme le [système de particules du moteur Valve Source](http://www.anandtech.com/tradeshows/showdoc.aspx?i=2868&p=9) sont du nombre.

D’autres logiciels sont moins « scalables », essentiellement parce que les processus doivent s’échanger des données entre eux, et chaque synchronisation bloque l’utilisation simultanée des coeurs. Avec 4 coeurs, l’accélération n’est « que » d’environ 150%. Dans cette catégorie on trouve par exemple  [Windows Media Encoder](http://www.microsoft.com/windows/windowsmedia/forpros/encoder/default.mspx), [Cinebench](http://www.maxon.net/pages/download/cinebench_e.html) et d’autres programmes de traitement d’images notamment.

Enfin, il y a tous les programmes qui ne sont pas parallélisés, ou qui n’ont été codés que pour 2 coeurs. Et il faut bien le reconnaitre, c’est le cas de la plupart des logiciels actuels.

Reste que la tendance est lancée : les processeurs auront bientôt 4, 8, 16 coeurs ([le processeur Cell](http://fr.wikipedia.org/wiki/Cell_%28processeur%29) qui équipe déjà la Playstation III a déjà 1+8 coeurs, on les voit bien sur la photo), et les programmeurs sont en train d’apprendre à en tirer parti.

Pour l’instant, un Quad vous apportera donc peu de gain de performance sur des applications interactives. Mais si vous encodez des videos, faites du rendu réaliste ou autres applications fonctionnant pendant des heures en tâche de fond, les 4 coeurs vous apporteront un gain de vitesse tout en laissant la machine disponible pour du travail interactif, ça peut valoir le coup.

## Commentaires

### Yves Masur — 26 août 2009 à 19:38

Tiens! dans le journal, cet article a été repris en mentionnant que j’en suis l’auteur, alors que – même s’il n’est pas signé, je suis quasi sûr qu’il est de Dr Goulu.\
Rendons à César…

### Dr. Goulu — 27 août 2009 à 10:41

Ah oui, tiens : le nom des auteurs n’apparait pas avec ce template…\
je vais voir si je trouve un meilleur template, en plus ça changera le look du blog avec la saison…

### ↳ Réponse — ymasur — 17 octobre 2009 à 17:04

Hello, je suppose que le nouveau template, c’est le pourquoi de ce nouveau look?\
Autres questions. Je dois mettre au point un site pour le giron des musiques de la Veveyse… Et je n’ai pas trop envie de me taper du HTML! Mais est-ce possible de déposer des PDF avec WordPress, ou faut-il le faire « à la normale » et pointer par un lien?

### ymasur — 16 janvier 2011 à 18:10

Récemment, les dessinateurs du service ont fortement râlé: Autocad 10 va plus lentement sur les nouveaux PC Hp 4 cœurs Windows 7 que sur leurs anciennes stations de travail XP. Qui n’avaient qu’un cœur, mais à fréquence plus rapide. Et la mémoire, de toute façon limitée à 4 Go par W7 32 bits n’amène rien de plus!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
