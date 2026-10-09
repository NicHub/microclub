---
title: "Main robotique pouvant coder le LPC"
date: "2015-05-18T21:59:07"
lastmod: "2016-02-02T20:11:13"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["arduino", "embarque", "hardware", "python", "robot", "software"]
url: "/2015/05/18/main-robotique-pouvant-coder-le-lpc/"
wordpress_id: 1915
comment_count: 2
---

## Idée…

A l’heure actuelle, il n’y a à ma connaissance aucun robot qui code du LPC. Idée… pourquoi ne pas en faire un? Une recherche sur le WEB montre qu’il y a bien des mains préfabriquées. En bois, en PLA, en métal. Même certaines peuvent être imprimées en 3D, dans la même matière que les LEGOs (réf. 1, 2, 3). Aucune ne peut écarter l’index des autres doigts ; souvent le pouce est seulement opposable. En définitive, il me faut construire une main simple, mais suffisante pour coder.[![](/media/2015/05/1_main_en_action_Y-1024x768.jpg)](/media/2015/05/1_main_en_action_Y.jpg)

## Montage

Dans mon garage, j’essaie de réunir les éléments. Les doigts seront en tube électrique ; les articulations en époxy (matière des circuits imprimés électroniques). Cette mécanique doit être précise : les découpages et les perçages sont réalisés à la fraiseuse. Pour simplifier, les doigts n’auront que deux phalanges.

[![601 doigt plan](/media/2015/05/601-doigt-plan-300x129.jpg)](/media/2015/05/601-doigt-plan.jpg)Quelques voyages à la quincaillerie de Vevey pour y acheter des vis, tarauds, tubes, axes, profil en aluminium, fil à ressort, fil de pêche me fourniront l’essentiel. Le plus difficile est de trouver le bon ressort. Assez souple, pas trop dur, assez fort pour relever les doigts. Un horloger de Vevey, Titzé, m’a donné du ressort de pendulette « qu’il n’utilisera plus ». Pour les dimensions, je me base sur… ma main. Le visage LPC est issu des documents que tout le monde du LPC connait bien, agrandi de façon à obtenir la dimension humaine. Ensuite, la main opérationnelle, je lui ai ajouté un bras avec deux motorisations : élévation et orientation.

La progression du montage est lente ; je ne vais au garage que les weekends s’il ne fait pas trop froid.

Les servomoteurs – c’est en fait la première chose que j’ai achetée – viennent du modélisme. Ils se commandent facilement avec un module Arduino, la plateforme très connue des électroniciens (réf. 4).

[Présentation hard courte en PDF](/media/2015/05/Main_LPC_hard_short.pdf)

## Programmation

Il y a deux programmes. Celui qui gère les mouvements de la main par le module Arduino est écrit en C++ ; il reçoit des ordres simples. Un interpréteur lit les commandes comme : c1 p3, ce qui signifie faire la clef d-p-j et la présenter à la commissure des lèvres. Il gère l’ordre des déplacements des doigts, pour éviter les collisions entre pouce, index et majeur. La clef est posée. Après quelques secondes (programmable…) les moteurs marquent un léger mouvement et sont arrêtés. Il est possible, avec n’importe quel PC et un port USB d’envoyer des ordres pour que la main les exécute séquentiellement.

[![684 Leonardo alim Low](/media/2015/05/684-Leonardo-alim-Low-300x178.jpg)](/media/2015/05/684-Leonardo-alim-Low.jpg)

Les positions sont fixes. Elles sont ajustées pour que l’index tombe visuellement sur les points rouges du visage.

[Présentation soft embarqué en PDF](/media/2015/05/Main_LPC_soft.pdf)

Le second programme est d’une tout autre nature : il s’agit de repérer des phonèmes dans du texte entré par l’utilisateur. Il est écrit en PYTHON, un langage de haut niveau qui permet la programmation objet efficacement. Pour le mettre au point, je me suis basé sur un interpréteur que j’avais fait il y a … 28 ans en BASIC, heureusement assez bien documenté (réf. 5). Le programme prépare le texte en le transformant. Par exemple, « des idées » en « dézidéye ». Il supprime les doublons, la ponctuation, les terminaisons non prononcées comme les ‘s’ au pluriel. Il met tout en majuscule ; les sons ‘é’ et ‘ai’ sont remplacés par ‘@’ et ‘^’.

[![100 Python_running](/media/2015/05/100-Python_running.jpg)](/media/2015/05/100-Python_running.jpg)Vient l’encodage. Une recherche dans le texte transformé par groupe de 3 caractères, puis 2, puis 1 est conduite pour en retirer le son en clef et position. Avec un seul caractère, c’est forcément incomplet. Dans un tel cas, la position par défaut « main ouverte » et/ou « côté » est appliquée pour l’information manquante. Le couple clef-position défini est envoyé à la main robotique – donc au premier programme – par le câble USB pour exécution.

## Conclusion

Cette main robotique ne peut pas vous serrer la main, ni vous servir le café. Elle ne peut pas non plus remplacer une codeuse-interprète. Son utilité est autre : démontrer la simplicité du LPC, et en faire une présentation ludique. Visiblement, l’intérêt montré par les apprentis codeurs/codeuses (enfants, parents, grands-parents) à Villars ce printemps l’a démontré.

Les améliorations ? Bien sûr, on peut en faire des tonnes. Premièrement, améliorer l’interpréteur de texte. Ceci demande un niveau de programmation important, au niveau linguistique. Une autre serait de faire un visage avec une bouche animée, qui suivrait aussi les phonèmes. Pour la bonne forme, on pourrait lui adjoindre un processeur vocal qui dirait le son, la clef, la position. Une autre option serait un redesign complet : plus grosse, moins fragile ; ce serait alors un outil de promotion utilisable par tout un chacun.

Yves Masur (5/2015)

Références :

1. <https://www.youtube.com/watch?v=Z70YWNuOB8E> Flexy-Hand 3D printed prosthesis
2. <https://www.youtube.com/watch?v=zzMPr9aiaSU> Wooden Mechanical Hand
3. <https://www.youtube.com/watch?v=dEHiAItVdiw> Large Mechanical Hand
4. [http://microclub.ch/2012/02/19/arduino-un-succes-embarque/](/2012/02/19/arduino-un-succes-embarque/)
5. [http://microclub.ch/2013/12/27/recuperation-dun-ancien-programme-basic/](/2013/12/27/recuperation-dun-ancien-programme-basic/)

## Commentaires

### Goulu — 19 mai 2015 à 06:24

Magnifique ! Tu as une vidéo de ta main en train de signer ?\
Mets le projet soft sur GitHub pour qu’on t’aide !\
Trouvé quelques librairies Python relatives à la linguistique et supportant le français : <https://pypi.python.org/pypi>?:action=browse&c=107&c=494\
A+

### Yves Masur — 19 mai 2015 à 20:01

Pas encore de vidéo; surtout parce que je n’ai aucune expérience en la matière. Pour les modules Python, merci du tuyau!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
