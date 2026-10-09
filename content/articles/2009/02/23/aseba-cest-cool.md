---
title: "Aseba, c'est cool !"
date: "2009-02-23T20:09:26"
lastmod: "2015-04-24T23:20:20"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["aseba", "epfl", "programmation", "robot"]
url: "/2009/02/23/aseba-cest-cool/"
wordpress_id: 164
comment_count: 0
---
Suite à la présentation d’[Aseba](http://mobots.epfl.ch/aseba.html) par Stéphane Magnenat, je me suis attaqué à la programmation d’un robot mobile pour le « Challenge ». Voici le résultat d’un duel de deux exemplaires partageant le même code:

\[youtube=<http://www.youtube.com/watch?v=Ed082QUKMXE\>]

Si vous voulez vous y mettre et tenter de battre mon robot :

1. [téléchargez Aseba](http://mobots.epfl.ch/temp/aseba-microclub-2009-02-19.zip) et la [doc en français](http://mobots.epfl.ch/data/aseba-user-manual-fr.pdf)
2. lancez asebachallenge et créez 2 robots : un « Goulu » et un pour vous
3. lancez asebastudio.exe, connectez vous au port 33333 (par défaut), coupez/collez mon code ci-dessous et cliquez \[Charger\] puis \[Executer\] : mon robot démarre. fermez asebastudio
4. relancez asebastudio.exe, connectez vous au port 3333**4** et programmez votre robot. Si vous battez le mien, mettez votre code dans un commentaire, ça m’intéresse 😉

```
var gains_R[3]=1,0,-1
var gains_B[3]=-1,0,1
var speed=0
var turn=0
var turn_R=0
var turn_B=0
var mode=1
onevent timer
    if mode==1 then #forward
        speed=(camB[1]-camR[1])/5
        call math.dot(turn_R,camR,gains_R,3)
        call math.dot(turn_B,camB,gains_B,3)
        turn=turn_R+turn_B
        leftSpeed=speed+turn
        rightSpeed=speed-turn
        if leftSpeed&amp;lt;2 and rightSpeed&amp;lt;2 then
            mode=2
            colorB=255 #follow me
            colorR=0
            colorG=0
        end
    elseif mode==2 then #rotate
        leftSpeed=-max_speed/3
        rightSpeed=-max_speed
        speed=(camB[1]-camR[1])/8
        if speed&gt;5 then
            mode=1
            colorB=0
            colorR=255 #avoid me
            colorG=0
        end
    end
```

Pour rappel et pour publicité j’ai traduit en français la description d’Aseba figurant sur la [page de l’EPFL](http://mobots.epfl.ch/aseba.html) :

*Aseba est une architecture basée « événements » pour la commande distribuée des robots mobiles. Il cible les robots intégrant plusieurs processeurs, ou des groupes d’appareils mono-processeurs pour autant qu’il communiquent par un réseau. Le coeur d’Aseba est une machine virtuelle légère, assez petite pour tourner sur un microcontrôleur. En Aseba, on écrit les comportements du robot dans un langage de script. Ceci se fait dans un environnement de développement tournant sur un PC. L’environnement permet de compiler, déployer et déboguer les comportements en temps réel. Aseba s’applique dans plusieurs contextes:*

- *Dans des robots à multiples microcontrôleurs, Aseba permet de tirer parti de la puissance des microcontrôleurs pour atteindre une modularité hardware, une faible latence entre perception, et une utilisation économique de la bande passante du bus. De plus, son langage facile à comprendre permet l’écriture rapide de comportements du robot ([article IROS 2007](http://infoscience.epfl.ch/getfile.py?recid=111860&mode=best)).*
- *En robotique collective, Aseba accélère le processus de développement en permettant des modifications instantanées du code ainsi que le déboguage en parallèle de tous les robots ([article SIMPAR 2008](http://infoscience.epfl.ch/getfile.py?recid=129025&mode=best)).*
- *Dans l’éducation, la facilité d’apprentissage du langage Aseba, son environnement de programmation user-friendly , et le plaisir de faire bouger un robot apportent une approche originale à l’enseigement et à l’apprentissage de la programmation  ([article FNG 2008](http://infoscience.epfl.ch/getfile.py?recid=128742&mode=best)).*

*Aseba est « open source » et tout le monde peut l’utiliser et le modifier gratuitement tant que l’on respecte la licence  ([GNU General Public License](http://www.gnu.org/copyleft/gpl.html) version 3).*

*Pour en savoir plus sur Aseba, regardez la [presentation](http://stephane.magnenat.net/data/aseba-presentation.pdf) ou lisez les articles sus-mentionnés.*

Pour ceux qui ne l’auraient pas vue, voici une vidéo assez spectaculaire du « robot bibliothécaire » en cours de développement dans ce labo :

\[youtube=<http://www.youtube.com/watch?v=FQYf0pI6fFs\>]

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
