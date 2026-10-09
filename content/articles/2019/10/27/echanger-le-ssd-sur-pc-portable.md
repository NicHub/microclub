---
title: "Echanger le SSD sur PC portable"
date: "2019-10-27T20:04:05"
lastmod: "2019-10-27T20:04:06"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: []
url: "/2019/10/27/echanger-le-ssd-sur-pc-portable/"
wordpress_id: 4663
comment_count: 2
---

## Situation de départ

Un SSD de 120 Go devient trop petit, sur un PC portable – en l’occurrence un PC HP Pavillion X360 13-V140NZ – le SSD d’origine de 120 Go devient trop petit, et je veux le remplacer par un SSD de 1 To. Soit 8 fois plus, ce qui donne de l’air.

Problème : le HDD 120Go contient Win10, et une partition avec les outils HP de diagnostic… Il s’agit de conserver la licence Win10. Il n’y a pas de place physique, dans ce genre de petits PC pour mettre les deux SSD dans la même machine ; et le slot est un connecteur M.2.

Allure du SSD d’origine:

![](/media/2019/10/word-image.png)

Même si c’est indiqué de le remplacer par une pièce HP, je prends le risque d’en mettre une version moins chère, fabriqué par Western Digital. Que voici : <https://www.digitec.ch/fr/s1/product/wd-blue-3d-nand-1000go-m2-2280-ssd-6408461> à 136.-

## Opérations à conduire pour l’échange

1. Contrôler le SSD 1
2. Connecter le nouveau SSD (nommé par la suite SSD 2) sur le PC
3. Copier les partitions bit à bit de SSD 1 à SSD 2
4. Étendre la partition Windows selon la place disponible

## Contrôle et préparation

Le contrôle est fait par : Explorateur de fichier / click droit sur C : / propriétés / onglet « Outils » -\> Vérifier. Bien que ce ne soit pas indispensable, on peut faire un peu d’ordre sur le disque, par l’onglet « Nettoyage ». Nettoyer la registry, avec CCLeaner par exemple, également est une bonne chose. Une fois les données bien préparées, on peut envisager la suite.

## Connecter le SSD 2

Il faut que le disque destination soit vu par la machine. Via l’USB, je connecte un lecteur externe. Dans mon cas ce lecteur est prévu pour disque SATA 5 ¼ ou 3 ½ , mais pas pour M.2. Heureusement, on trouve des adapteurs. Exemple, chez Digitec :

<https://www.digitec.ch/fr/s1/product/delock-m2-oder-msata-zu-sata-adapter-disques-durs-accessoires-6292841> . Bien sûr, cela renchérit l’opération… Si quelqu’un en a besoin, je le lui prête volontiers !

Le M.2 est monté dans cet adapteur, puis dans le lecteur externe et connecté via l’USB au PC.

Vision des partitions, avec l’utilitaire Win10 :

Diskmgmt.msc

![](/media/2019/10/word-image-1.png)

Le disque SSD 2 – sur l’image, « Disque 1 » – est bien vu par Win10, avec 931.5 Go, non alloué. Mais pour la suite, comment procéder ?

Une recherche Internet montre une jolie quantité de programmes pour copier ou redimensionner des partitions. Pour faire le job, le programme doit pouvoir booter séparément de Windows, idéalement sur clé USB ; ou avoir le pilote qui permet de farfouiller les partitions à partir de l’OS.

Après quelques essais (et beaucoup de redémarrages et de déconvenues), je sélectionne Macrium Reflect 7, 64 bits : <https://www.macrium.com/reflectfree>

Qui est gratuit, du moins pour le privé et l’usage que je souhaite faire. Installé sur une clé USB libre. Il faut bien sûr se battre avec le BIOS du PC qui doit accepter de démarrer sur… autre chose que le Win10 installé ! La notion de « démarrage UEFI » s’interpose. Selon Wikipédia :

*L’UEFI offre quelques avantages sur le BIOS : fonctionnalités réseau en standard, interface graphique de bonne résolution, gestion intégrée d’installations multiples de systèmes d’exploitation et affranchissement de la limite des disques à 2,2 To.*

*Le BIOS, écrit en assembleur, limitait les modifications et/ou remplacements, gage de sûreté de fonctionnement et de sécurité. L’UEFI est écrit en C, ce qui rend sa maintenance plus souple et reste acceptable en raison des coûts décroissants de la mémoire. Développé pour assurer l’indépendance entre système d’exploitation et plate-forme matérielle sur laquelle il fonctionne, l’UEFI est disponible sur les plates-formes Itanium (IA-64), x86 (32 et 64 bits) et ARM.*

Finalement, on arrive à booter sur une clé USB, et Macrium Reflect Free se monte.

![](/media/2019/10/word-image-2.png)

Joli avantage, il est possible de déplacer ou retailler les partitions par curseurs, contrairement aux outils (certes gratuits) basés sur Linux.

Une fois démarré, on demande les copies des partitions sources, puis l’étirement de C: au max de la nouvelle capacité du disque destination.

![](/media/2019/10/word-image-3.png)

Ça devrait donner ceci :

![](/media/2019/10/word-image.jpeg)

Mais voilà… pas possible d’étirer la partition C : comme désiré !

![](/media/2019/10/word-image-1.jpeg)

Pas très explicite, l’erreur en question :

![](/media/2019/10/word-image-2.jpeg)

D : est le lecteur de la clé USB, sur laquelle le soft tourne. On voit que Macrium est écrit en Pascal.

Après plusieurs essais (diverses tailles d’étirement), je renonce à faire ces opérations d’un bloc ; mais les reprend une à une, en rebootant à chaque fois. Et là, c’est OK.

![](/media/2019/10/word-image-3.jpeg)

C’est tout bon : le SSD est désormais de 930 Go. Windows est reconnu, la partition augmentée.

YM (10/2019)

## Commentaires

### franic — 22 décembre 2019 à 10:33

J’ai fait la même chose que toi, mais j’ai utilisé un logiciel open source Clonezilla.\
J’ai préparé une clé USB « Clonezilla » qui boot avec linux.\
J’ai ensuite branché mon SSD avec un adaptateur USB et j’ai lancé le clonage.\
Il m’a créé automatiquement toutes les partitions windows 10, recovery, …\
Tout s’est déroulé finalement très simplement alors que cette opération semble assez compliquée; j’ai suivi ce tutoriel : <https://www.malekal.com/clonezilla-tutoriel-clonage-de-disque/>

### ↳ Réponse — Yves Masur — 22 décembre 2019 à 10:57

Effectivement, c’est plus simple. Et dans les 2 cas, il faut créer l’USB bootable. Si Macrium ne présentait pas cette erreur à l’extension de la partition, on arriverai au même nombre d’opérations.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
