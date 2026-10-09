---
title: "Emulation et Virtualisation"
date: "2006-09-15T19:37:25"
lastmod: "2015-04-24T23:20:25"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["emulation", "systeme-dexploitation", "vmware"]
url: "/2006/09/15/emulation-et-virtualisation/"
wordpress_id: 78
comment_count: 0
---
j’avais déjà été sidéré par [Mame](http://www.mame.net/) et d’autres émulateurs, mais je viens d’avoir un très gros choc en utilisant un logiciel de virtualisation : [VMware](http://www.vmware.com/fr/)

<!--more-->

#### Emulation

La puissance des ordinateurs doublant tous les 18 mois, il arrive un moment ou il devient possible d’écrire un programme qui simule le fonctionnement d’un ordinateur plus ancien. C’est un « émulateur ». Quelques Exemples:

- [DOSBox](http://dosbox.sourceforge.net/) simule un bon vieux PC sous MS/DOS. DOSBox existe pour Windows, mais aussi Linux, Mac OS X etc, ce qui prouve que non seulement le logiciel, mais aussi le fonctionnement du matériel de la machine d’origine peut être simulé sur un matériel totalement différent.
- [Mame](http://www.mame.net/) est un « Muliple Arcade Machine Emulator » permet de retrouver toutes les pompes à fric qui peuplaient les bistrots de ma jeunesse : de « Space Invaders » à « Out Run », des centaines de microprocesseurs et de puces graphiques et sonores sont simulées sur des PC musclés, mais aussi sur des téléphones portables! Encore une illustration spectaculaire de la Loi de Moore : un téléphone actuel contient un ordinateur plus puissant que le top de la machine multimedia il y a 20 ans!

A part l’aspect ludique et éducatif, les éditeurs de systèmes d’exploitations sont très intéressés à garantir une compatibilité maximale avec leurs systèmes précédents pour conserver leur clientèle. Exemple:

- En 1999, Lorsque les « Mac Intosh » sont passés des processeurs Motorola 68040 aux PowerPC, Apple a du intégrer un émulateur à son Mac OS 9 pour permettre à tous les programmes Mac écrits depuis 1984 de fonctionner.
- Puis en 2001, Mac OS X a introduit un émulateur « Classic » permettant d’y faire fonctionner des applications Mac OS 9.
- En 2006, les Mac vont être équipés de processeurs Intel, et la version correspondante de Mac OS X sera équipée de « Rosetta », un émulateur PowerPc sur x86.

Avec un peu de chance, on devrait donc bientôt faire voir des programmes Mac de 1984 fonctionner dans un émulateur émulé par un émulateur émulé par un troisième émulateur ! Si vous doutez de la performance du résultat rapellez-vous : un ordinateur actuel est 2^(20\*12/18) = 10’000 fois plus puissant que le premier Mac…

#### les « Machines Virtuelles »

Pour introduire la virtualisation, voyons comment l’arrivée du 80386, le premier processeur 32 bits d’Intel, a transformé le monde du PC en 1985.

Là, Intel était au moins aussi intéressé que Microsoft à ce que les programmes écrits pour ses processeurs 16 bits précédents continuent à fonctionner.

Intel a donc conçu le [« Mode virtuel 8086 »](http://fr.wikipedia.org/wiki/Mode_virtuel_8086) qui permet au 80386 d’exécuter du code 16 bits à pleine vitesse dans des « machines virtuelles » gérée par un système d’exploitation 32 bits comme Windows 95

Une « machine virtuelle » est « simplement » une zone de la mémoire qui ressemble à la mémoire d’un vieux PC, vue de l’intérieur.

Mais avec l’aide du « gestionnaire de pagination mémoire » existant sur les processeurs modernes, on pose des pièges : dès que le programme fonctionnant dans la machine virtuelle lit ou écrit les adresses mémoire correspondant aux périphériques, la machine réelle s’en aperçoit et effectue l’opération correspondante.

Par exemple, si un programme MS/DOS tournant en « virtuel » essaie d’allumer un point de « son » écran en croyant accéder à une carte VGA, Windows 95 reçoit une interruption, et le code réel (32 bits) détermine la fonction à réaliser, et allume le pixel correspondant dans la fenêtre de la machine virtuelle, puis rend le contrôle au programme « virtuel » qui continue son exécution, inconscient de n’être qu’un pantin manipulé…

En pratique, créer une machine virtuelle revient principalement à écrire des « drivers » pour les périphériques, divisés en 2 moitiés : la partie « virtuelle » singe le comportement du périphérique « vu de l’intérieur », la partie « réelle » réalise effectivement le fonctionnement du périphérique, mais intégré à un système différent.

#### Virtualisation

L’arrivée des processeurs 64 bits repose le problème de la virtualisation, mais les processeurs ont anticipé : il est désormais possible de créer des machines virtuelles 32 bits sur des machines réelles 32 bits. Quel intérêt ? Par exemple de faire tourner plusieurs systèmes d’exploitation en même temps sur un ordinateur « hôte », et c’est ce que fait [VMware](http://www.vmware.com/fr/) sur PC

Je n’ai pas encore fait le tour des énormes possibilités de ceci, mais par exemple :

- on peut faire tourner un Linux dans une fenêtre Windows
- préparer des machines préconfigurées avec des logiciels pour démonstration, formation ou expérimentation. Chaque fois qu’on en a besoin, on utilise une copie « propre » qu’on lance sur un PC et qu’on jette après emploi, sans avoir modifié quoi que ce soit à l' »hôte »
- faire tourner plusieurs « serveurs virtuels » sur une machine réelle : si un problème se produit sur une machine virtuelle, les autres continuent à fonctionner et il suffit de relancer une nouvelle copie
- configurer un système complexe en combinant des machines virtuelles pré-configurées, chacune réalisant une fonction du système. C’est l’idée des « appliances » dont certaines sont [téléchargeables gratuitement](http://www.vmware.com/vmtn/appliances/) (principalement celles basées sur Linux)

#### Référence

- [PlanetEMU](http://planetemu.net/) site spécialisé sur les émulateurs ludiques
- [VirtuaMag.net](http://www.virtuamag.net/web/) site spécialisé sur la virtualisation

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
