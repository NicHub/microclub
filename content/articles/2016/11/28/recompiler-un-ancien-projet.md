---
title: "Recompiler un ancien projet"
date: "2016-11-28T21:34:53"
lastmod: "2016-11-29T10:08:26"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["embarque", "processeurs", "programmation", "software"]
url: "/2016/11/28/recompiler-un-ancien-projet/"
wordpress_id: 2779
comment_count: 0
---
Un projet est-il facilement recompilable, après quelques années ?

Bonne question, je dois justement reprendre un projet PIC. Le compilateur est gratuit, téléchargeables depuis le site de Microchip. Pour modifier un projet de 2012, je dois ré-installer le soft permettant d’apporter une modification mineure.

Certes, j’ai les sources, mais pas/plus l’environnement de développement : en effet, j’ai changé de PC entretemps. Allons-y…

## Essai

C’est le projet « barrette intelligente » ([http://microclub.ch/2011/03/25/projet-barrette-livrable/](/2011/03/25/projet-barrette-livrable/)) dont j’aimerai retoucher le soft. En effet, le système comporte une prise électrique « master », qui pilote une ou plusieurs autres prises. Et mon nouveau PC (un ACER Aspire VN7) qui est justement branché sur la prise « master » a un nouveau mode de consommation : il prend du courant, puis travaille quelques secondes sur la batterie, et reprend du courant… Ma lampe de bureau, branchée sur une prise « slave » clignote ! Pas très utilisable. Je me dis qu’une tempo au déclenchement un peu plus longue va régler le problème.

Je copie mon projet dans un nouveau répertoire, examine les sources clés, et après quelques minutes de réflexion, je rajoute une constante pour la tempo « déclenchement » de 15 secondes alors qu’auparavant, j’avais mis la même pour l’enclenchement et le déclenchement, fixée à une seconde.

Et il faut recompiler ce projet. Recherche de l’outil sur le WEB. Visite de [www.microchip.com](http://www.microchip.com) .

Téléchargement depuis ce site pour le moins compliqué. Enregistrement nécessaire chez Microchip, login, tout le tralala… Mais un outil universel est proposé. Il faut télécharger le « MPLABX-v3.45-windows-installer.exe », poids de 574 MB… tout ça pour faire quelques Ko de soft 8 bits, ça laisse songeur.

L’environnement de développement, l’IDE donc, propose dans une fenêtre d’accueil « Projet : import legacy ». Cool, me dis-je ; ils y ont pensé, on y va. Et une boite de dialogue propose de reprendre mon ancien projet en 8 étapes. Son extension mcp signifie : microchip projet.

[![01-import](/media/2016/11/01-import.png)](/media/2016/11/01-import.png)

Le device cible est reconnu automatiquement: PIC18F6627

Pour le tool, je suis emprunté : il me faut simplement faire un .HEX, à télécharger. Mettons un PIC KIT 2, on verra plus tard.

[![02-select-tool](/media/2016/11/02-select-tool.png)](/media/2016/11/02-select-tool.png)

A l’étape suivante, cet univers mystérieux me demande… où est le compilateur ?, tout en me précisant que le mcc18 à la racine de C: n’y est plus (oui, c’est vrai, vu que j’ai changé de PC il n’est pas réapparu). Et le compilateur 32 bits installé par défaut n’y peut rien. Retour sur le site de Microchip. Après moult recherches, j’y arrive. C’est – pour le 8 bits – le xc8-v1.38-full-install-windows-installer.exe, avec 84 Mo supplémentaires à télécharger.

L’outil d’import me propose le nom du projet « barrette_12 » que j’accepte, et il résume le tout. Ça a l’air très bien.[![03-summary](/media/2016/11/03-summary.png)](/media/2016/11/03-summary.png)

## Ça ne compile pas bien

Une tonne d’erreur apparaît. Pas si grave, à première vue : le fichier inclus « projdefs.h » n’est pas trouvé. Pourtant, il est bien là…

Et là, je perd des heures à essayer de le copier, déplacer, modifier les sources…pfff… pas moyen de contenter le compilateur. Son problème ? Il confond une série de source qui se trouve dans un sous-répertoire « .\net » réunissant le code qui a trait au réseau et ne voit plus le chemin relatif des fichiers à inclure et/ou à compiler.

## Et le compilateur original ?

Je me copie la version originale du compilateur (le MCC18 donc) que j’utilisais – fort heureusement – aussi au travail pour un autre montage sur le même module hardware. Refaire l’importation… essai de compiler un fichier .C, ça marche ! Et de tout recompiler ? … OK, sans erreur ! Le HEX final est produit, dans un sous-sous répertoire tarabiscoté, mais utilisable. Ce HEX fait la même taille que l’ancien : 195’800 octets. Reste à vérifier bit à bit avec le programme FC (file compare, nativement en ligne de commande de Windows) : le code n’est pas vraiment le même.

[![04-compare-hex](/media/2016/11/04-compare-HEX.png)](/media/2016/11/04-compare-HEX.png)

Mais il suffit que le compilateur ne soit pas exactement de la même version pour produire cet effet de bord. Ou que les options, longues comme un jour sans fin, ne soient pas strictement pareilles. Pas de panique.

Le chargement sur la cible s’avère aussi quelque peu laborieux ; mais l’outil JAVA livré pour charger le HEX s’installe sans problème et il est complètement fonctionnel. Je peux donc charger mon nouveau HEX, faire des essais, modifier aussi les pages WEB et finaliser la modification.

## Conclusion

Plus de peur que de mal. Mais on voit que la pérennité des choses peut être vite compromise. Un nouvel environnement, un compilateur plus moderne mais pas compatible avec la MAKEFILE et on est dans le doute et la recherche de solution peut s’avérer longue.

Il me vient en mémoire un critère de qualité de développement de code (réf: <http://www.joelonsoftware.com/articles/fog0000000043.html>) : il est mentionné « compilez-vous  vos sources tous les jours? » Cela m’avait surpris ; mais on mesure que les petites modifications graduelles telles que :

- Changement de version de l’OS
- Mise à jour de compilateurs
- Noms de chemins modifiés
- Version de l’IDE
- Version des outils hardware
- Clefs d’authentification perdues

(liste non-exhaustive) finissent par rendre un code source très éloigné de la cible. Et en cas de modification, même mineure, la chose est soit rendue ardue (perte de temps importante), voire impossible. Et là, il faut passer par un redéveloppement sur une nouvelle cible dans un nouvel IDE.

A l’heure où le soft évolue plus vite que le hardware, c’est un point d’attention à considérer fortement par l’ingénieur soucieux de la pérennité de ses produits.

Yves Masur (11/2016)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
