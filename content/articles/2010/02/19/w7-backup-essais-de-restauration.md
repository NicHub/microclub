---
title: "W7 – backup, essais de restauration"
date: "2010-02-19T21:41:00"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["backup", "initiation", "sauvegarde", "securite", "systeme-dexploitation", "vista", "windows", "windows-7"]
url: "/2010/02/19/w7-backup-essais-de-restauration/"
wordpress_id: 268
comment_count: 2
---
Les version de Windows précédentes utilisaient NTBACKUP pour copier des fichiers sur une sauvegarde. Une optimisation plus user friendly est implémentée sous W7. Mais comment se passe une restauration depuis zéro? Il faut un certain courage pour s’y lancer. Ou avoir confiance dans le système…

Comme ma version (RC2) arrive au terme de sa période – plus que 10 jours!! – c’est le bon moment pour s’y mettre. Bien entendu, je lance un dernier backup sur un disque de 500 Go connecté par USB, avant d’insérer le DVD de la version finale de W7 et redémarrer le PC. Comme je n’ai plus utilisé Vista depuis, je me propose de formater et installer sur cette partition. Que j’efface (tiens, j’ai plus de place tout à coup!). Et que je formatte, et sélectionne comme LA partition W7 (tiens, W7 demande 100 Mo pour y faire des sauvegardes).

Suit la série d’installation et redémarrage… la clef… le WLAN, la clef WPA… l’utilisateur… le password… le clavier… la langue… la zone. Me voici devant un bureau vierge, avec une résolution minable. Que je passe immédiatement en 1920 x 1200.

**Restauration des fichiers:** elle redonne tous les fichiers qui étaient dans le chemin C:\Users\\nom); pas de souci de ce côté. Si un fichier existe déjà, par exemple « desktop.ini » qui est un fichier caché, il pose la question et propose le même traitement pour la suite:

- ecraser par celui de la sauvegarde
- conserver
- remplacer et conserver un copie, au cas où

Evidemment, mon bureau n’a pas changé… Faut-il ré-installer tous les programmes? Essayons avant cela la…

**Restauration du système**: un avertissement m’indique que la récupération standard suffit pour la plupart des problèmes, sinon, il est possible de passer à la version avancée. Allons-y pour la standard. Après la restauration, le système me délogue et redémarre. Et après l’ouverture de session, je me retrouve devant un bureau pourvu d’icônes… standard. Je 2xclique dessus Total Commander, et contre toute attente, il se lance! Idem avec Code::Block, DOSBOX, TTermPro… jusqu’à SoundRescue, qui prétend ne pas être enregistré. Humm… Mon soupçon augmente lorque je regarde C:\Program Files, qui est quasi vide; il se vérifie lorsque la dé-installation de programme est vide, et se confirme lorsque je vérifie le lien de VNC: « D:\Program Files\RealVNC\VNC4\vncviewer.exe ». Ils pointent sur la partition D:, qui – toujours présente – est l’ancienne de W7!!

En outre, tous les programmes installés « à la main » dans la racine de C: n’y sont pas non plus. Je les ai repris de la partition D:. En guise de conclusion, le backup de W7 sauvegarde vos données de profil, mais guère plus.

Yves Masur

## Commentaires

### ymasur — 27 février 2010 à 22:14

Pas de chance, j’ai dû ré-installer à nouveau W7, pour une sombre histoire de clef. A cette occasion, j’ai pu voir que la récup n’est pas évidente.\
Evidemment j’ai perdu quelques données au passage, vu qu’avant cette dernière(?) installation, j’ai travaillé sur des données, re4u des emails.\
Après l’installation initiale, aller dans sauvegarde et récupération vous propose de configurer la sauvegarde; puis d’en faire une! Attention, danger d’écraser ce que vous tenez à restituer! Par contre, j’ai pu voir que dans la récupération de fichiers, ceux de qui sont dans C:Users(nom)Appdata sont bel et bien sauvegardées. Un outil de recherche par nom permet de s’en sortir. Indiquer « Mozilla » laisse apparaître l’emplacement et la date – sans taille toutefois – d’au moins 50 références…\
Bref, il vaut mieux faire les deux sorte de sauvegarde: image disque et fichiers.

### Jacques — 11 mars 2010 à 08:48

Yves, deux remarques :\
– la partition de 100 MB ne seraitutile que si tu utilises le BitLocker Drive Encryption (version pro et ultimate seulement).\
– pour le backup complet du PC, il est nécessaire d’utiliser la sauvegarde d’image du disque et non pas le backup.\
A+\
Jacques

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
