---
title: "Windows 7 – forces et faiblesses"
date: "2009-06-06T09:32:13"
lastmod: "2015-04-24T23:21:14"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["systeme-dexploitation", "vista", "windows"]
url: "/2009/06/06/windows-7-forces-et-faiblesses/"
wordpress_id: 200
comment_count: 7
---

## Win7 : le bon

Après quelques jours d’utilisation, voici un petit bilan de Win7. Parlons déjà de ce qui fonctionne bien.

Il est facile à installer: image ISO, créer un DVD, lancer l’installation. Choisir la partition non-Vista. Ainsi, il crée un « dual-boot » qui permet de choisir. Curieusement, mes disques étaient ainsi:

C: Vista et programmes -et- D: données

Avec Win7, je me retrouve les lettres de lecteurs inversées. Par contre il supporte parfaitement le NTFS de Vista. Evidemment, les liens créés avec la commande MKLINK pointent faux sous Win7.

Le menu Démarrer est (a mon avis) moins perturbant et difficile à régler que sous Vista: il ressemble plus à un tableau, présentant des portions d’Explorer: déplacer, copier, renommer y est facile.

Win7 boote plus vite que Vista; mange moins de mémoire. Et utilise 4 Gb sur 4, alors que Vista n’utilise que 3,5 Gb. Même si j’ai une version 64 bits, toute les applications 32 bits fonctionnent parfaitement. Même l’application Sysinternal « Process Explorer », le remplacement du Tasmanager est OK. La gravure de DVD avec CDBurnerXP, la conversion de son MP3 par dBpowerAMP, l’inevitable OpenOffice 3.1, tout fonctionne.

Certaines applications, que j’avais la flemme d’installer, ont été simplement copiées. Le dilemne est dans quel répertoire: « c:\Program Files » désormais dévolu aux applications 64 bits, ou dans « c:\Program Files (x86) » ? La tricherie ne marche bien que dans le premier, à cause du nom du chemin.

## Win7 : le moins bon

Tout ne se passe pas sans douleur.  Des détails? la webcam pas reconnue (je ne désespère pas), la gestion de l’énergie semble mal fagotée: l’écran s’allume à demi luminosité, et la première combinaison « Fn + soleil » le met à fond, ensuite la progression est correcte. Au prochain stand-by, ce sera à refaire, la luminosité n’est pas mémorisée.

Si le driver USB de mon stylo optique, prévu pour Win XP a pu marcher en le lançant comme Administrateur dans Vista, là il ne voit pas la présence du stylo. Si je plante le stylo dans la prise (son: bidup…) Win7 lui cherche un pilote… Idem pour installer des convertisseurs série RS-232 USB.

J’ai déjà parlé de la limitation video, sans savo![MediaPlayer](/media/2009/06/mediaplayer.jpg "MediaPlayer")ir si c’est Win7 ou quoi?

Avast n’a pas apprécié le passage. ![vm_avast](/media/2009/06/vm_avast.jpg "vm_avast")

Et je le voit **présentement**, Firefox plante si l’on veut télécharger une image! Je saisi donc le reste de ce texte dans IE8, 64 bits!

Pour les ennuis, il ne reste qu’à suivre les conseils avisés du Dr Goulu: conserver une émulation de Vista…

Yves Masur

<!--more-->

## Commentaires

### ymasur — 6 juin 2009 à 15:33

Autre lien en relation:\
Le programme de mise à jour de Vista vers Windows 7 disponible dès cet été ?\
<http://www.zdnet.fr/actualites/informatique/0,39040745,39503673,00.htm?xtor=RSS-1>

### ↳ Réponse — Dr. Goulu — 6 juin 2009 à 22:01

jamais vu de conversion 32bits -\> 64 bits fonctionner. Et à mon humble avis Seven permet de faire le grand saut…

### Dr. Goulu — 6 juin 2009 à 21:59

L’utilisation de 4Gb sur 4, ça vient du 64 bits, pas de Seven. J’avais déjà ça sur Windows 2000 x64. Mais il y a enfin des drivers 64 bits pour (presque) tous les périfs, enfin … Ta webcam c’est une Logitech ? ils trainent pour le 64 bits…

Pour Firefox, en 64bits il faut installer la version 3.5 beta 4. J’ai un peu ramé pour mettre tous les plugins (flash en particulier) mais ça roule maintenant.

### Yves Masur — 9 juin 2009 à 18:38

L’analyse de réseau par Wireshark n’est pas possible, à cause du programme WinPcap auquel il fait appel. Ce dernier ne peut pas s’instaler. A propos de l’erreur, inutile de désactiver l’antivirus: c’est du même.

Q-30: The WinPcap installation fails with the error message « An error occurred while installing the NPF driver ( -1 ). Please contact the WinPcap team ».\
A: This error is usually caused by an antivirus or antimalware software that incorrectly detects the WinPcap kernel driver (NPF) as malware. This is because in the past some malware tools have been developed over the WinPcap library.

The workaround is to disable such antivirus/antimalware programs while installing WinPcap.

### Yves Masur — 23 juin 2009 à 19:23

Problème ftp avec une application java: le Modtronix Network Bootloader ne fonctionne pas bien avec W7 64 bits. Le plus troublant est que rien ne signale une erreur ou un problème. Pour faire une démo, j’ai modifié une page WEB; recompilé avec cet outil; mais il ne fini jamais l’opération de chargement et reste dans un état bizarre.\
Effet démo, garanti!

### Yves Masur — 4 juillet 2009 à 13:39

Or donc, j’ai remplacé le Vista 64 bits par la version 32 bits (au lieu de revenir à Vista). Etpresque tous les drivers 32 bits fonctionnent : serielle USB, autres utilitaire Dell du PC, etc. Il ne reste que le stylo Mypen qui bute… une question de temps pour trouver les bons paramètres, je suppose L’écrasement par l’installation m’a noté que la version serait renommée Windows.old; et je l’ai ensuite effacée. Le boot loader a été mis à jour, pas de souci de ce côté.\
Surtout, le ftp du « Modtronix Network Bootloader » (ref. ci-dessus) fonctionne!

### Yves Masur — 2 octobre 2009 à 20:23

Un bon article pour passer à W7;\
<http://www.clubic.com/article-292098-1-windows-7-nos-conseils-pour-preparer-la-mise-a-jour.html>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
