---
title: "VMWare – un update difficile"
date: "2009-01-02T21:42:36"
lastmod: "2015-04-24T23:21:14"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["histoire", "systeme-dexploitation", "windows"]
url: "/2009/01/02/vmware-update-difficile/"
wordpress_id: 133
comment_count: 0
---
Qui n’a pas pesté une fois ou l’autre quand à une installation difficile? Ou lorsqu’un update se révèle  « pire qu’avant? »

Voici la problématique. En ces jours de l’an nouveau, je profite pour mettre à jour mon PC avec les dernières versions d’update que je laisse volontiers en retard le reste de l’année écoulée. Open Office 3.0 passe sans problème, ainsi que d’autres dont je vous fait grâce. VMWare PLayer a passé de la version 2.05 à 2.5. Je télécharge donc la nouvelle version (<http://vmware.com/download/player/>) et la lance. Malheureusement, mon PC se plante en cours d’installation. Il gèle: écran, pas de souris, plus de réaction. Il faut dire que pendant cette installation, j’écoute de la musique, je zieute des images, je surfe, je teste un autre programme; bref ça charge la machine. Seule solution: presser le bouton de l’alimentation 5 secondes.

Le PC redémarre; oui, on relance Windows en mode normal; les disques sont propres, c’est tout bon. Par contre, VMWare Player est mal installé, on s’en douterai. Il se lance, mais pour exécuter une image Linux, tintin. Je reprend donc l’installation, mais elle refuse d’aller plus loin disant que le programme est déjà en place, et qu’il faut passer par une dé-installation au préalable; ou redémarrer le PC pour que tout soit OK. Bien entendu, rien n’y fait. Et dans le panneau de configuration de Windows, pas de VMWare! Essayer de ré-installer l’ancienne version donne exactement le même résultat. Les ennuis sont là.

**1er essai – arracher le programme à la main**

Pour cela il faut être Admin. J’essaie gentiment de renommer le /Programme Files/VMware autrement; pas de résultat. Avec une console, et la commande rd /S /Q, c’est possible de tout supprimer. Mais que nenni, l’installateur persiste à me signaler une version déjà en place.

**2ème essai – nettoyer le %temp%**

Allez une fois dans votre répertoire temporaire: ça ressemble à une poubelle! Grâce à un petit batch (contenu: del %temp%\\.\* /s /q), je nettoie tout ça. Et les répertoires. Mais que nenni, l’installateur persiste à me signaler une version…

**3ème essai – nettoyer la registry**

Aller zieuter dans la registry, si ce n’est pas une poubelle ça y ressemblee fort.  Là, le moyen approprié est de lancer CCleaner (voir: <http://www.ccleaner.com/>) qui fait fort bien le job, et supprime une kyrielle d’occurences de VMWare. Mais que nenni, l’installateur persiste…

**4ème essai – etudier la faq et les logfiles**

Donc, ce satané installateur à mis quelque part ces infos (erronées), et je ne vais quand même pas reformater le disque pour ça? Une visite sur <http://communities.vmware.com/community/vmtn/desktop/player> n’est que perte de temps. Cependant, j’y voit des références aux logfiles créés par l’installation. Et dedans une telle logfile, j’y vois quelque chose d’instructif:

\<code\> BootStrapper-build-126130: 01/02/09 11:55:55 Warning: Deleting a key that isn't empty: "HKEY_LOCAL_MACHINE\SOFTWARE\VMware, Inc.\NeedReboot"\
BootStrapper-build-126130: 01/02/09 11:55:55 \[Info\] InstallProduct(\[C:\Users\Yves\AppData\Local\Temp\\A53A11EA-0095-493F-86FA-A15E8A86A405}~setup\VMware Player.msi\], \[ TRANSFORMS=:1033\])\
VMInst: 01/02/09 11:55:55 Begin Logging\
VMInst: 01/02/09 11:55:55 Getting Property Installed =\
VMInst: 01/02/09 11:55:55 Getting Property ProductName = VMware Player\
VMInst: 01/02/09 11:55:55 Starting VMware Player installation: Releasebuild-126130\
VMInst: 01/02/09 11:55:55 End Logging\
\</code\>Un petit coup de regedit me montre en effet qu’il ya effectivement une références VMWare à cet endroit: \<code\>HKEY_LOCAL_MACHINE\SOFTWARE\VMware\</code\>! Sans état d’âme, je supprime la clef; dès lors l’installation se fait correctement. Et VMWare Player est à nouveau fonctionnel. Ouf!

Yves Masur

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
