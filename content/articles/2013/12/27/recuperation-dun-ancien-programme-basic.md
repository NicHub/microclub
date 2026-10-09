---
title: "Récupération d’un ancien programme BASIC"
date: "2013-12-27T20:36:40"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["basic", "langage", "lpc", "programmation", "python", "systeme-dexploitation", "windows"]
url: "/2013/12/27/recuperation-dun-ancien-programme-basic/"
wordpress_id: 1395
comment_count: 0
---

## Quelle est la durée de vie d’un programme ?

Dans notre univers de plus en plus informatisé, la question de la mise à jour et de la pérennité d’un programme est légitime. Faire tenir des anciens programmes DOS est le lot de techniciens qui travaillent sur des machines d’un prix très élevé (pas le PC, mais bien la machine cible…) et dont il faut assurer la maintenance une vingtaine d’années, voire plus. Parfois, on peut avoir de bonnes surprises !

Le programme dont je vais discuter ici est un « codeur LPC ». Il s’agit de présenter à l’écran une main, avec 8 configurations des doigts ; un visage autour duquel 5 positions où la main devra être placée. C’est la technique que ma femme et moi avions adoptée lorsque nous avions appris la surdité de notre fils Robin. Vous trouverez plus d’explication sur ce code, sa genèse et son utilisation sur le site [www.alpc.ch](http://www.alpc.ch); ou bien sûr en lisant le livre qui traite de ce sujet à <http://www.yvesmasur.ch/livre/> .

Après avoir fini des études en 1986, donc avec du temps libre à disposition je me suis mis en tête de créer un programme d’aide à l’apprentissage du LPC, et de le mettre à disposition de personnes intéressées. D’abord sur Commodore 64, qui possédait quelques atouts graphiques comme 8 sprites, ce qui convenait parfaitement pour exprimer les 8 configurations des doigts d’une main. Puis le PC est venu ; je l’ai transposé en pseudo-graphique, donc sur un écran de console en mode texte. Ce programme m’avait pris – pour la version C-64 – environ 3 mois les soirs, un investissement conséquent. Je l’ai traitée comme un projet, avec tout ce qu’il faut pour le suivi.

## Récupération de l’ancien code

Afin de piloter un nouveau projet sur le même sujet – soit coder en LPC –, je me suis penché sur mes archives. J’ai retrouvé le classeur. Il comporte de la documentation, un article publié dans le journal interne du CHUV ou je travaillais à l’époque, un listing de 550 lignes en papier cranté et la disquette… au format 5’ ¼. Le listing suffirait, mais il est daté du 10/08/1987, alors que l’étiquette de disquette mentionne 1/1988.

En lançant une demande aux membres du MICROCLUB afin de relire ce média, Laurent m’annonce qu’il a toujours une machine PC 386, comportant un lecteur 5’1/4. Je vais donc à son bureau, avec la disquette dans ma serviette… Je me maudis en constatant qu’elle se ferme magnétiquement ! Quel imbécile je suis! Que va-t-il se passer ? Fort heureusement, les bits sont solidement inscrits ; ou l’effet du champ magnétique pas suffisant pour les effacer. Ouf… Le contenu est copié sur une disquette 1.44 MB (l’autre faisait 360 KB), puis je m’empresse de le poser sur le HDD de mon laptop.

Quels étaient ces fameux fichiers ? C’est écrit dans « READ-IT », en caractères DOS, bien sûr :

```
 Volume dans unité B est CUED-SPEECH
 Répertoire de  B:\
CUED-SCR COM    22400   5.01.88   9.46  &lt;-- programme avec accès écran
CUED     BAS    13883  28.01.88  11.16  &lt;-- source du programme
CUED     COM    22784  28.01.88  11.51  &lt;-- programme avec accès BIOS
CUED     DAT      866  28.01.88  11.31  &lt;-- datas (modifiable) chargés au départ
CUED     TRF     1528  16.07.87  10.42  &lt;-- transformeurs, également modifiable
READ-IT             0  20.06.88  18.31  &lt;-- CE fichier
ZB       COM    32384  10.03.87  15.30  &lt;-- compilateur nécessaire pour modifier le programme
ZBASIC   HLP    33536  26.08.87         &lt;-- HELP du compilateur
LPC              9344  20.06.88  18.27  &lt;-- Mon article paru dans l'antenne du CHUV 1/88
        9 Fichier(s)
   221184 octets disponibles
```

## Époque spartiate (à l’aune de 2014)

On peut en déduire que le PC travaillait sur deux unités de floppy ; le DOS en A : et celui de travail en B :. On remarquera la sobriété des programmes : le compilateur ZBASIC (nommé par ses auteurs « interpiler ») ne prend que 32 Kb ; le « help » à peine plus. Un souci d’économie que l’on ne retrouve certes plus dans le développement des programmes modernes, où plus de 100 Mb devient facilement la norme. Le programme compilé n’est pas bien gros non plus, avec 22 Ko. Remarquez également que c’est le format « image mémoire », soit un « COM », et non pas un « EXE ».

ZBASIC implémentait un BASIC plus élaboré que le standard BASICA (ou MS-BASIC, ce qui revient au même), avec des possibilités graphiques, non utilisées par mon programme prévu pour une console. Les références remplacent les numéros des lignes.

Qu’est devenu le producteur de ZBASIC, un compilateur (interpiler…) de 1988 ? La société proposait son compilateur pour MS-DOS, Apple II, MacIntosh, CP/M, TRS-80. Elle s’est orientée sur des solutions embarquées, en se posant comme concurrent du BASIC Stamp. Sa force mathématique reposait sur les calculs en BCD, dont la résolution – variable – peut aller jusqu’à 54 digits.

Un programme prévu pour système monotâche, 256 Kb de mémoire, 2 floppy et console va-t-il tourner sur PC Windows 7 ? C’est la bonne surprise, mais oui, ça fonctionne encore. Pour être précis, il me faut mentionner le fait que le clavier de l’interpréteur COMMAND.COM est le QWERTY. Afin d’y remédier, il faut lancer un KB16 SF, histoire de le mettre au Suisse français.

## Utilisation du programme

Le programme comporte 2 versions : CUED et CUED-SCR, qui accède à la page texte via le BIOS, et non par adressage direct. Il avait donc une option de compilation permettant de faire le distinguo. L’ensemble des fichiers sont disponibles sous :  <http://yvesmasur.ch/articles> puis en développant l’arborescence « Cued speech ». Ou directement par :

<http://www.yvesmasur.ch/articles/Cued%20speech/LPC.ZIP>

L’archive contient le tout. Une fois déballé, le programme CUED.COM devrait fonctionner, pour autant que les données contenues dans CUED.DAT et CUED.TRF soient présentes dans le même répertoire.

Et je constate que le codage est correct pour la phrase entrée « Hello Microclub » ; que voici en action.

[![Hello_microclub](/media/2013/12/Hello_microclub.jpg)](/media/2013/12/Hello_microclub.jpg)

Une commande est précédée de ‘\*’ pour qu’elle ne soit pas interprétée comme du texte à coder. La commande \*Help nous montre ce qui est à disposition :

— Fonctions : \*SHOW, \*NONE, \*TIME\<1..9\>, \*TONE, \*BYE —

Là ça se gâte un peu. Dès que \*TIME est utilisé, au lieu de rythmer les codes, le programme fonce à la fin du texte ! Les tempos du programme, pour rythmer la présentation du codage ne sont visiblement pas basées sur un timer, mais par une boucle dépendant de la vitesse du CPU… Beurk ! Sans parler du son, qui bloque sur un ton. J’ai cependant remarqué un tel défaut avec d’autres programmes DOS tournant sous Windows. Quitter par \*BYE fonctionne… Il ne faut pas oublier qu’au temps du DOS, si un programme n’avait pas de sortie correcte, le redémarrage par Ctrl – Alt – Del était la règle. Voir un bon OFF – ON, dans les cas récalcitrants.

Avec le recul, je me dis que le but du programme est atteint ; son fonctionnement est tout à fait satisfaisant pour coder une phrase entrée au clavier en LPC. Quelle en a été la diffusion ? Confidentielle… Seules quelques disquettes m’ont été demandées. Il faut dire qu’en 1987 l’ordinateur personnel (le Personnal Computer !) était peu répandu ; l’époque beaucoup moins technophile et connectée qu’aujourd’hui.

Il me reste maintenant à décortiquer les astuces de ce code pour le transposer dans un langage moderne et normalisé : le Python (enfin, on verra ce qu’il en reste dans 25 ans…) Mais ceci est une autre histoire, que je ne manquerai pas de vous rapporter.

Yves Masur (12/2013)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
