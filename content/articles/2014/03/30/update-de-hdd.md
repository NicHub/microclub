---
title: "Update de HDD"
date: "2014-03-30T19:51:07"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["disque-dur", "hardware", "lien-symbolique", "systeme-dexploitation", "windows"]
url: "/2014/03/30/update-de-hdd/"
wordpress_id: 1442
comment_count: 0
---
Le disque dur du PC commence à se faire un peu petit? Plus des 3/4 de sa capacité remplie de musique, de photos, de films? Voici une technique ultra simple et… qui a fonctionné du 1er coup. Assez rare pour être mentionnée!

En fait, c’est simple pour autant qu’on aie pris quelques précautions en amont. Il faut que les données de ce type (soit des DATA, différents des programmes) aient bien été séparément enregistrées. Pour ma part, sur le disque C: qui est un SSD figurent le système, les programmes (**C:\Program Files**), les données de faible taille. Le profil (**C:\user\Yves\Documents**) est bien sûr l’objet de backup réguliers, et avec Windows 7, ça marche plutôt bien. Le backup copie les fichiers pointés par les liens – donc inutile de lancer un second backup de D: qui contient réellement les fichiers. Pour plus de détails sur l’organisation des données, voir un précédent article ici, qui précise tout ça: [http://microclub.ch/2012/08/06/installer-un-disque-ssd-et-re-installer-w7-et-les-programmes/](/2012/08/06/installer-un-disque-ssd-et-re-installer-w7-et-les-programmes/%20 "Installer un SSD") .

Avec en tête l’idée de toujours déposer les **données volumineuses** sur une autre unité. On précise par des **liens symboliques** (commande MKLINK, en administrateur) que les images et les sons sont déposés sur la seconde unité physique. Justement, celle que l’on va remplacer, par les étapes suivantes:

- connecter le nouveau HDD au PC
- copier les données
- échanger les disques
- vérifier que les liens symboliques fonctionnent toujours…

### Station d’accueil pour HDD

La connexion est faite par un dispositif que j’ai trouvé chez Conrad: [\<code\>http://www.conrad.ch/ce/fr/product/971937/\</code\>](http://www.conrad.ch/ce/fr/product/971937/ "Lien Conrad")

![Station d’accueil pour disque dur](/images/articles/hdd-docking-station.jpg)

Ce bidule permet de connecter un disque dur 3’1/2 ou 2’1/2 via USB sur le PC. Une alimentation et un bouton permettent son enclenchement; le PC le voit comme *un périphérique de stockage de masse*. Ce qu’il nous faut, quoi.

### Copier les données

Après l’inévitable formatage (NTFS, please), pour lequel le nouveau HDD via la station d’accueil a pris la lettre F:, il faut faire attention à **tout** copier du disque D: à F:, si l’on veut que les liens symboliques fonctionnent. Tout, c’est les droits, les fichiers cachés, les ACL, les liens symboliques (et non les fichiers sous-jacents).

La commande via CMD.EXE lancé en admin, est: **xcopy d:\*.\* /S /H /O /B  f:**

ça prend effectivement un peu de temps…

### Échange des disques

Ensuite, démonter le PC, enlever l’ancien D: et y placer le nouveau F:. Remontage, démarrage… Windows réfléchi plus longuement que d’habitude… Mais démarre normalement. Mais voilà: le nouveau disque a conservé la lettre ‘F’! Un clic sur Ordinateur – Gérer – Stockage – Modifier la lettre de lecteur et les chemins d’accès; on corrige en D: et un petit CHKDSK. Puis on vérifie…

Tout fonctionne! C’est pas nickel, tout ça?

Yves Masur (3/2014)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
