---
title: "Clef USB flash en mode RAW – retrouver les fichiers"
date: "2016-02-02T22:17:02"
lastmod: "2016-02-02T22:17:02"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["chkdsk", "clef-usb-flash-memory-test", "consoles", "linux", "mode-raw", "recovery", "securite", "windows"]
url: "/2016/02/02/clef-usb-flash-en-mode-raw-retrouver-les-fichiers/"
wordpress_id: 2220
comment_count: 0
---
Retirer la clef USB de stockage d’un PC sans l’éjecter peut fonctionner assez longtemps ; mais une fois, un jour, on se retrouve avec un problème. Le problème ? la clef ne peut plus être lue. Windows ne propose pas moins que de formater l’unité.

[![01FormatF](/media/2016/02/01FormatF.png)](/media/2016/02/01FormatF.png)

Peut- on retrouver les fichiers dans un tel cas ? Cet article montre un cas réel d’un confrère de la musique à qui c’est arrivé. Mal lui en prend, il travaille et sauve ses photos, données, courrier seulement sur la clef USB. D’où l’importance – jamais assez dite – de faire des backups. Mais le mal est là, alors je lui promets de tenter ce qui est en mon pouvoir pour récupérer quelque chose sur sa clef de 32 Go.

Comme prévu, la clef est illisible ; je passe sans formater, bien sûr. Selon Win10, il y a 0 octets disponibles sur une capacité de 0 octets.

[![02nodata](/media/2016/02/02nodata.png)](/media/2016/02/02nodata.png)

L’outil classique, dans un tel cas, est de lancer CHKDSK en vue de restituer la table d’allocation des fichiers. Mais c’est plus grave :

[![10chkdsk](/media/2016/02/10chkdsk.png)](/media/2016/02/10chkdsk.png)

Une recherche sur le net avec les mots « raw usb flash drive repair » montre une série de liens sur des forom (parfois très anciens) et des pubs pour des outils de réparation. J’en essaie quelques-uns.

# Essai avec M3 Data Recovery

Site: <http://www.m3datarecovery.com/>

Une fois lancé avec les bons paramètres, soit : un répertoire de destination des (éventuels) fichiers récupérés et l’unité à découvrir, il se met en route pour reconstruire le secteur d’amorce, durée environ 1H40.

[![30m3-buildbootsector](/media/2016/02/30m3-buildbootsector.png)](/media/2016/02/30m3-buildbootsector.png)

A la fin, il nous présente deux dossiers : NTFS et FAT32. Ce dernier comporte une liste de répertoires avec un n°, c’est encourageant. Comme il faut une licence pour en extraire plus de 4, j’y vais déjà avec cette limite pour voir ce qui en sort.

[![32m3-data-recovery](/media/2016/02/32m3-data-recovery-1024x642.png)](/media/2016/02/32m3-data-recovery.png)

Résultat : pas terrible. En effet s‘il y a bien des fichiers, ceux-ci restent illisibles autant pour Word (.doc) que pour Irfanview (.jpg)…

[![32word-nook](/media/2016/02/32word-nook.png)](/media/2016/02/32word-nook.png)

[![33irfanview-no-header](/media/2016/02/33irfanview-no-header.png)](/media/2016/02/33irfanview-no-header.png)

# Essai avec ZAR X

Site : <http://www.z-a-recovery.com/>

Cet utilitaire permet la récupération d’images (gratis), de données Windows et Linux, de disques en mode RAID cassés – ce qui étonnant, puis que le montage de disques en RAID est prévu pour la perte d’un disque dans un agrégat. Comme quoi…

[![41zarx-recover](/media/2016/02/41zarx-recover.png)](/media/2016/02/41zarx-recover.png)

Là également, il faut environ 1h30 pour lire l’entier de la clef USB. Il présente aussi l’arborescence des fichiers, mais avec leurs noms ce qui est encourageant. La version démo permet aussi d’en lire et d’en sauver une partie, ce que je fais. Comme les fichiers sont propres et utilisables, je paie la licence complète, environ CHF 76.- au cours du jour. S’il faut relancer le programme pour lui appliquer la licence, ce n’est pas une perte de temps, car le scan précédent peut être sauvé dans un fichier de configuration que l’on peut reprendre plus tard.

[![42zarx-filescopy](/media/2016/02/42zarx-filescopy.png)](/media/2016/02/42zarx-filescopy.png)

Les données de mon ami sont sauvées. Ouf !

# Essais complémentaires

Il est indiqué sur tous les forums ou tutos sur la question : NE FORMATTEZ PAS VOTRE CLEF USB !

Mais d’un autre côté, si la FAT32 est pourrie, qu’est-ce que ça peut faire de pire ? Et peut-être, on peut aussi récupérer les fichiers, mais sur une unité lisible par Win10 ?

Je procède au formatage ; en mode rapide, bien sûr. Sinon, tout est à zéro, il n’y a rien à récupérer. L’unité F : est désormais présente, et elle affiche 29 Go libres.

# Testdisk 7.0

Site : <http://www.cgsecurity.org/wiki/TestDisk>

Ce programme libre permet de restaurer/modifier des amorces défectueuses, et de modifier/restaurer des partitions et/ou des fichiers. Les menus sont simples, en écran texte. Ce choix est sûrement du fait que le programme est prévu pour tourner sur plusieurs systèmes d’exploitations différents : Dos, Windows, Linux, Mac OSX, etc…

[![51 testdisk](/media/2016/02/51-testdisk.png)](/media/2016/02/51-testdisk.png)

Pour le choix de l’unité, il faut avoir l’œil car c’est selon le principe d’UNIX qu’elles sont montées ; mais aussi répétées avec lettre de lecteur :

[![51testdisk-nofiles](/media/2016/02/51testdisk-nofiles.png)](/media/2016/02/51testdisk-nofiles.png)

Peut-être se fie-t-il trop aux infos de la FAT32 trouvées sur /dev/sbc ; il ne trouve rien à redire, mais pas de fichiers non plus. Pas utile pour ce cas.

# Piriform Recuva

Site : <https://www.piriform.com/recuva>

Vous connaissez sans doute CCleaner ? C’est le même éditeur. Calibré pour Win10, une fois lancé il reconstruit la liste des fichiers en 43 minutes. Mais ils ne sont tous un seul répertoire. De plus quelques fichiers au nom trop long ne seront pas restaurés sans corriger leur nom manuellement.

[![Recuva-recovering-3H](/media/2016/02/Recuva-recovering-3H.png)](/media/2016/02/Recuva-recovering-3H.png)

Le résultat est mitigé. Il faut 3 heures pour extraire les fichiers de la clef ; c’est du tout-venant. Il y a bien entendu des fichiers « normalement » effacé, comme les temporaires, les fichiers de verrou comme « .~lock.TS1.docx# ». Une bonne part des images en jpeg sont cassées. Un moyen simple est de prendre les fichiers dans l’ordre de leur date ; les plus frais sont intacts et récupérables. Mais c’est un travail de bénédictin que d’en retirer les valides, d’autant plus que l’arborescence des répertoires a disparu. Je soupçonne fort que certains fichiers au nom de « ÿÿÿÿÿÿÿÿ_1.ÿÿÿ » pesant 4 Go en fasse partie…

[![61recuva-filesfound](/media/2016/02/61recuva-filesfound.png)](/media/2016/02/61recuva-filesfound.png)

Bref, c’est une solution gratuite, mais de désespoir.

# Conclusion

En cherchant bien, on peut récupérer plus ou moins bien des données sur une clef (ou un disque dur) pourri. Mais… il faut avoir du flair ; les outils de récupération performants se paient. Si ça fonctionne, tous les fichiers vous seront proposés. Même des anciennes versions, des écrasés, des partiels et des tas de temporaires ; à vous de les effacer à nouveau après la restauration.

Faites des copies ; des backups, des sauvegardes de vos données, ce n’est pas une perte de temps.

Yves Masur (2/2015)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
