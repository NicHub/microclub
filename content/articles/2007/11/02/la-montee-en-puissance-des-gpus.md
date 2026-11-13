---
title: "La montée en puissance des GPUs"
date: "2007-11-02T08:10:44"
lastmod: "2015-04-24T23:20:24"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["gpu", "hardware", "parallele", "programmation"]
url: "/2007/11/02/la-montee-en-puissance-des-gpus/"
wordpress_id: 358
comment_count: 2
---

Dans les ordinateurs vendus depuis 2003 environ, le microprocesseur (CPU) fourni par Intel ou AMD n’est plus le composant le plus puissant, et souvent plus le plus couteux non plus. Désormais c’est le GPU, le Graphics Processing Unit, qui détermine largement la puissance d’un PC. Strictement limités au graphisme il y a peu, ces processeurs sont désormais capables d’effectuer certains calculs nettement plus vite que les processeurs classiques. Actuellement, la puissance de calcul du G80 de nVidia est 5 à 6 fois supérieure à celle du Core 2 Duo d’Intel, voire plus (1, 2).

![](http://drgoulu.files.wordpress.com/2007/11/img0019319.jpg)\
*puissance de calcul des GPU et CPU ([source : BeHardware](http://www.behardware.com/articles/659-1/nvidia-cuda-preview.html))*

## Conséquence immédiate

Si vous achetez un ordinateur pour y faire fonctionner les applications les plus exigeantes, c’est-à-dire les jeux vidéo, il faut faire plus attention au choix du GPU qu’au CPU. Vous ne gagnerez que quelques pourcents de performance avec un CPU plus rapide qui vous coûtera quelques centaines de francs, alors que la même somme investie dans une carte graphique basée sur un GPU plus récent ou puissant peut doubler le nombre d’images / seconde (fps) de vos applications favorites.

## Un peu d’architecture des processeurs

([lire la suite sur le blog de Dr. Goulu](http://drgoulu.wordpress.com/2007/11/02/la-montee-en-puissance-des-gpus/))

## Commentaires

### Laurent Francey — 31 octobre 2008 à 07:41

Voici ce que le magasine Elektor a publié ce matin :

Depuis que Nvidia a sorti le système Cuda, les cartes graphiques pourraient rapidement hériter de nouvelles tâches et soulager quelque peu le processeur principal. Compute unified device architecture, de son vrai nom, est un concept original qui a l’ambition d’ouvrir les portes du processeur graphique (GPU) aux programmeurs intéressés. Expressément calqué sur le langage C pour profiter de son inaltérable succès, Cuda ne compte encore qu’une seule application. Badaboom se présente donc comme l’aîné d’une famille de logiciels qui s’appuient sur le processeur de la carte graphique pour exécuter une partie des tâches nécessaires. Destiné à convertir des vidéos d’un format à un autre, ce programme séduira plus par son côté novateur que par ses fonctionnalités. En effet, le seul format d’entrée reconnu jusqu’à présent est le MPEG-II… On l’a compris, il s’agit d’abord d’une vitrine, sorte de démonstration de la puissance inexploitée qui sommeille dans notre carte graphique.\
Connus pour leur efficacité dans les opérations répétitives, les GPU constituent une main d’oeuvre idéale pour les routines de conversion parfois trop exigeantes à l’égard des processeurs habituels. Au lieu de freiner tout le système, déléguer ces besognes à une unité spécialisée permet justement de libérer le processeur pour continuer à assurer la fluidité des opérations en cours.\
Lorsque Cyberlink, l’éditeur du logiciel Power Director entrera dans la danse, ainsi que ArcSoft ou encore Pegasys, le succès de Cuda pourrait rebondir. Aussi intéressante que puisse être cette nouveauté, la partie est toutefois loin d’être gagnée. La majorité des cartes vidéo qui équipent les PC proviennent d’Intel et ne connaissent rien de Cuda, exclusivement réservé aux cartes Nvidia. Quand on sait la réticence des constructeurs aux standards interopérants, on imagine assez mal qu’une entente puisse naître entre eux, sur base d’une simple bonne idée. D’autant qu’Apple prépare déjà la sortie de son langage Open CL, lui aussi destiné aux GPU…

### Dr. Goulu — 31 octobre 2008 à 11:34

pour info badaboom est un transcodeur vidéo. (voir ici : <http://www.presence-pc.com/tests/GeForce-GTX-260-280-22792/25/>) Mais ce n’est pas la seule appli CUDA. Il y a Folding@home (voir <http://drgoulu.wordpress.com/2007/01/20/calcul-distribue-avec-boinc/>) et surtout PhysX, qui est (sera…) utilisé dans beaucoup de jeux et peut-être aussi dans des applications « sérieuses ».

remarque aussi sur « La majorité des cartes vidéo qui équipent les PC proviennent d’Intel ». Ce n’est pas vrai. La majorité des PUCES video viennent d’Intel (les minables trucs qui sont sur les cartes mères). Les CARTES video viennent de nVidia et ATI en grande majorité. Je ne sais même aps si intel fait des cartes graphiques, en fait …

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
