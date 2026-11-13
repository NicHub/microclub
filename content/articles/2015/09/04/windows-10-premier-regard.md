---
title: "Windows 10 – premier regard"
date: "2015-09-04T22:30:53"
lastmod: "2016-02-02T20:07:24"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["consoles", "graphiques", "musique", "systeme-dexploitation", "windows"]
url: "/2015/09/04/windows-10-premier-regard/"
wordpress_id: 2038
comment_count: 6
---
# Un nouveau PC

C’est ce qui m’a incité à passer à Windows 10 (ci-après Win10). Selon la légende, Microsoft aurait zappé Win9 pour… les applications qui ne testeraient que 1 digit de version et confondraient aves Win95 ! Comme les versions paires sont souvent mauvaises chez MS (DOS2 ; DOS4, DOS6 Millenium, NT 2 ont eu leur lots d’avanies) ce n’est pas d’excellente augure pour Win10. Trêve de supputations, voyons ce qu’il en est. Le nouveau PC, un portable ACER VN7 est équipé de Win8.1. Sans perdre de temps, je clique sur passer à Win10. Quelques Go téléchargés plus tard, il se lance et me propose de me connecter à mon compte MS. Oui, j’en ai un. Je sélectionne avec précaution français, clavier suisse, heure Berne.

## Yves versus Masur

Si l’on a un compte Microsoft, on peut s’y connecter. Et plein de choses se synchronisent entre PC, non pas par miracle, mais par échange de données sur le Cloud, tel Skydrive. Compte, mots de passe, pédigree, préférences, configurations, favoris, listes de lectures… ce qui peut être très pratique – ce qui peut faire peur.

Un petit aperçu, ici : <http://www.nextinpact.com/dossier/652-compte-microsoft-petit-guide-pratique-des-services/1.htm>

Lors de l’installation, Win10 propose la connexion au compte Microsoft. Mon conseil : ne le faite pas, à moins que vous teniez à ses fonctionnalités. Pour mon malheur j’ai croisé nom – prénom. Désormais, mes précieuses données sont sous Users\Masur. Raaah !

Redémarrage pour finaliser ; MS a même mis ma bouille au login, c’est la photo du compte. Mais pas moyen de se logguer. Mais c’est ça, horreur, non, pas le clavier Frouze !! Je me résous à changer mon mot de passe sur le site de MS, pour un plus simple, en chiffres (avec l’aide de mon ancien PC) pour enfin pénétrer la machine. Heureusement, après le 1er login, tout rentre dans l’ordre : le clavier est bien suisse Romand. Mon apprenti Thomas, qui a fait le passage à Win10 avant moi, m’a dit avoir fait la même expérience.

## Windows 10

L’aspect est presque Win7. Presque… des icônes de la barre des tâches diffèrent ainsi :

[![1-barre-taches](/media/2015/09/1-barre-taches.jpg)](/media/2015/09/1-barre-taches.jpg)

Le symbole Windows montre une liste des programmes les plus utilisés à gauche; et 2-3 programmes comme Edge (le nouveau browser) l’email et une série de gadgets à droite. Déplaçable, supprimables.

Puis la loupe (recherche, bien faite) et les bureaux, par l’icône qui ressemble à un photocopieur vu de dessus. Des bureaux, comme dans les versions graphiques des \*nix ? à ceci près qu’un nouveau bureau contient en fond tous les raccourcis déposés – on ne voit donc pas de différence. Seule la présence d’applications diffère : elles s’affichent sur le bureau sur lequel elles ont été lancées. Sauf le Task Manager Gestionnaire des tâches, qui reste en avant partout. Troublant. Il n’est pas dit que les bureaux restent ainsi… Finalement, la « maison » montre un menu proche de Win7.

## Gestionnaire des tâches

[![2-process](/media/2015/09/2-process.jpg)](/media/2015/09/2-process.jpg)

\[Processus\]\
Les infos sont présentées de manière plus synthétique. \[Performance\] permet de choisir via un volet gauche, le détail qui s’affiche à droite. Ici, le WiFI.

[![3-perf](/media/2015/09/3-perf.jpg)](/media/2015/09/3-perf.jpg)

\[Historique des applications\]\
est nouveau : on y voit le temps CPU, réseau, mise à jour, … qui indiquent ce qui est consommé/utilisé. Utile j’imagine pour les entreprises ou le partage de ressources – pas vraiment pour le privé.

Autostart : \[Démarrage\]\
Inutile de bricoler en mettant un raccourci dans le répertoire « Démarrage », il n’existe plus de manière visible. Oui, c’est dans l’onglet \[Démarrage\] du Gestionnaire des tâches qu’il faut travailler.

## Taille de Win10 versus Win7 sur le disque

Taille de c:\Windows : 19.2 Go (20 713 864 732 octets) ; Win7 : 27.5 Go

145 894 Fichiers, 32 939 Dossiers ; Win7 : 93869 Fichiers, 18551 dossiers

## Partitions des disques

Le SSD contient 4 partitions primaires. Je n’ai rien changé à ce que le constructeur a mis en place.

[![4-diskpart](/media/2015/09/4-diskpart.jpg)](/media/2015/09/4-diskpart.jpg)

## Comment supprimer le dossier Windows.old ?

Désemparé, je cherche la ligne de commande… ce sera via la recherche de CMD.EXE, puis la création d’un raccourci sur le bureau. Mais la commande RD Windows.old ne fonctionne pas, non plus en Admin… voici la solution : <http://windows.microsoft.com/fr-fr/windows7/how-do-i-remove-the-windows-old-folder>

## Gérer son PC

« Gérer » le PC est devenu plus abscons. Pour le trouver, sous Win7, il suffisait d’un clic droit sur l’icône « Ordinateur ». Maintenant, il faut passer par : \[Maison\] -\> Ce PC -\> \[Ordinateur\] -\> Gérer

[![5-gere](/media/2015/09/5-gere.jpg)](/media/2015/09/5-gere.jpg)

## Comment mieux utiliser l’espace disque

Avec Win7, il fallait créer une redirection à la main, avec la commande MKLINK. La nouvelle destination permet, par exemple de soulager le SSD et de stocker les images et la musique sur le D :. Une solution facilitée sous Win10 est de proposer, pour les LINK existants (reconnaissables à l’icône) via les propriétés, un nouvel emplacement.

[![6-deplacer](/media/2015/09/6-deplacer.jpg)](/media/2015/09/6-deplacer.jpg)

Et amusant, le backup est … le backup Win7:

[![7-backup](/media/2015/09/7-backup.jpg)](/media/2015/09/7-backup.jpg)

## Conclusion

Souvent, si vous chercher la différence en Win 7 et Win 10, on parle sur le WEB des *applications* livrées avec lui, comme Photo, Edge (le nouveau browser), l’assistant personnel Cortana – tiens ! Celui-là, je ne l’ai pas entendu…

Les avancées majeures sont bel et bien : les bureaux, le retour du menu démarrer. Surtout, son interface graphique s’adapte à des surfaces tactiles (pas essayé).

Au premier contact, Win 10 est certainement un bon OS, bien connecté, performant (en regard de Win 7 ou Win 8). Il utilise les performances des SSD au mieux et démarre très rapidement. L’avenir dira s’il aura une longévité telle que XP. En fait, on a toujours des vilaines farces comme ceci:

[![w10-error](/media/2015/09/w10-error.jpg)](/media/2015/09/w10-error.jpg)

Yves Masur (9/2015)

## Commentaires

### Yves Masur — 5 septembre 2015 à 20:50

On peut aussi activer le GodMode, soit une fenêtre qui donne accès à tous les paramètres.\
Il suffit de créer un dossier, avec pour nom: « GodMode.{ED7BA470-8E54-465E-825C-99712043E01C} » (sans les guillemets). Et c’est fait!

### Laurent — 7 septembre 2015 à 13:48

Ce qui me gêne pour le moment c’est que toutes les 15 minutes, « Windows 10 » envoie chez Microsoft ce qui a été entré au clavier. Mes mots de passes partent donc en claire chez Microsoft ! Ce qui est envoyé chez Microsoft est crypté, mais ….

### ↳ Réponse — ymasur — 7 septembre 2015 à 20:32

As-tu essayé <https://github.com/10se1ucgo/DisableWinTracking> ?

### ymasur — 29 septembre 2015 à 21:54

Après un trop long temps de recherche, j’ai remarqué que le PING est bloqué sur Win10 pour les interfaces considérés comme « public ». Il faut changer la règle dans le pare-feux, ici: <http://www.sysprobs.com/enable-ping-reply-and-ftp-traffic-in-windows-10-and-server>\
Remarquez que si vous avez fait une mise à jour depui W7 par exemple, et que le PC était configuré pour l’accepter, c’est OK.

### Jacques — 22 octobre 2015 à 09:12

Salut Yves, quelques remarques :\
– pour « Gérer » clic droit sur icône Windows – puis Gestion (au choix Ordi ou disque)\
– pour utiliser le stockage sur un autre disque que celui système : Paramètres – Système – Stockage – Emplacements d’enregistrement ( crée automatiquement le/les dossiers)\
– le principe du backup n’est plus actuel. Il est remplacé par l’historique des fichiers.

### ymasur — 22 octobre 2015 à 10:34

Exact pour les 2 premiers points; par contre le backup existe toujours, mais il est plus « caché » et perso, je trouve ceci désagréable. On le voit à l’oeuvre ici: [https://www.dropbox.com/s/yxax77vahmavm6z/Capture%20d%27%C3%A9cran%202015-10-22%2011.22.29.png?dl=0](https://www.dropbox.com/s/yxax77vahmavm6z/Capture%20d%27écran%202015-10-22%2011.22.29.png?dl=0)\
Il est identique à celui de Win7.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
