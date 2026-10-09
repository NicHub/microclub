---
title: "Explorer des éléments de domotique"
date: "2017-01-07T22:08:42"
lastmod: "2017-01-07T22:13:24"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["barrette", "domotique", "gadgets", "hardware", "iot", "reseau", "software"]
url: "/2017/01/07/explorer-des-elements-de-domotique/"
wordpress_id: 2919
comment_count: 2
---
# Lampe de bureau IOT

Titillé par ce qui est proposé sur le marché, j’ai testé pour vous deux éléments : un relais électronique et une lampe de bureau. Commençons par celle-ci.

La lampe de bureau est présentée comme suit, avec le titre un peu pompeux « Original Xiaomi LED Smart Table Lamp Dimming Reading Light For Cellphone » sur le site de Banggood, au prix de environ 50.-. Comptez 3 semaines pour la livraison, mais le port est gratuit. Elle correspond physiquement complètement à la description, son maniement est simple (heureusement, car le mode d’emploi est … en chinois). Le bouton par impulsion sert à allumer/éteindre ; sa rotation diminue/augmente la luminosité ; et maintenu pressé, change la température couleur.

Mais que peut-on piloter par soft ? Le nom de l’application (ci-après nommée Apps), pas mentionné, m’est donnée via le forum : c’est Yeelight. Pour Androïd et IPhone (iOS). Une fois chargée, il faut s’inscrire sur un site, avec email (ou n° de téléphone) et password. Ensuite, il s’agit d’appairer le/les éléments contrôlables par l’Apps.

Pour la bonne compréhension, voici le schéma (partiel) de liaison que j’ai à la maison. Il y a un répéteur WiFi pour que le signal soit assez fort au 1er étage, le routeur étant au sous-sol.

[![schema-lan-masur](/media/2017/01/schema-LAN-Masur-1024x576.jpg)](/media/2017/01/schema-LAN-Masur.jpg)

En cherchant l’appairage, je n’ai pas réussi en le faisant par le répéteur ; alors que PC portable ou le mobile passent sans difficulté du WiFi AP du sous-sol au répéteur au rez. J’ai donc déménagé la lampe près du routeur/WiFi pour ce faire ; malgré tout, il m’a fallu quelques essais pour y parvenir avec succès.

Une fois connecté, l’Apps Yeelight permet d’enclencher/déclencher la lampe ; de commuter sur une température couleur.

Les fonction sont : On-Off, une température couleur élevée pour de la lecture ; et une basse pour consulter un écran de PC sans trop de lumière bleue.

On peut renommer l’élément et même mettre un raccourci de bouton On-Off sur le bureau Androïd, ici « LED Bureau » :

[![](/media/2017/01/16-bouton-racc-295x300.jpg)](/media/2017/01/16-bouton-racc.jpg)

Ceci a du sens lorsqu’on a plusieurs éléments commutables, pour les atteindre rapidement avec son mobile.

## Conclusion provisoire

L’apps ne sert pas à grand-chose. En effet, si on travaille sur son bureau, pourquoi sortir son portable pour allumer ou éteindre la lampe qui y trône plutôt qu’allonger le bras? Il serait plus intéressant d’y avoir une commutation pour simuler une présence, par exemple. Ou un allumage progressif à partir d’une heure donnée pour servir de réveil sympathique.

De plus, comme mentionné peu avant, elle essaie de se connecter sur le routeur ; la communication est mauvaise, donc inutilisable. Souvent, le On-Off est inopérant.

[![17-yeelight-offline](/media/2017/01/17-yeelight-offline-300x224.jpg)](/media/2017/01/17-yeelight-offline.jpg)

Et l’aide pour le reset, pas secourable :

[![18-yeelight-how](/media/2017/01/18-yeelight-how-300x96.jpg)](/media/2017/01/18-yeelight-how.jpg)

# Switch Sonoff

Le switch est aussi disponible par le site de Banggood, sous le nom de « DIY Wi­Fi Wireless Switch For Smart Home » pour moins de 7.-. Il fonctionne sur le 230 VAC et un pouvoir de coupure de 7 A, un courant maximal de 10A. Le voici inséré dans une rallonge secteur.

Dommage qu’il n’y ait pas de bornes pour le fil de terre…

[![00-sonoff](/media/2017/01/00-sonoff.jpg)](/media/2017/01/00-sonoff.jpg)

*Attention : dans la description qui suit, « switch » nomme cet élément, et non un switch informatique.*

Le constructeur Slampher a d’autres produits, dont des culots E27 permettant des commutations. Ce qui est moins clair est : comment sont faites les transmissions ? Sur le site, il est dit que la transmission est à 433 MHz, mais aussi WiFi. Avec sur le croquis un nuage, un AP et un smartphone… Le texte est un peu plus clair : Sonoff and Slampher will send data to cloud platform through Wi­Fi Router, they pair with the Wi­Fi through the APP, thus you can control all added appliances and lights with your smart phone or tablet.

## Application

L’Apps à charger sur smartphone est : EWeLink. Son installation demande une inscription, un login, un mot de passe. Ce qui peut inquiéter toutefois est ceci :

[![01-ewelink-droits](/media/2017/01/01-ewelink-droits-173x300.jpg)](/media/2017/01/01-ewelink-droits.jpg)

Pourquoi une telle Apps a besoin de la position, du micro, de la caméra ? très intrusif, tout ça ! En tous cas, j’hésiterais à l’utiliser pour, disons, enclencher/déclencher un réacteur nucléaire.

La confirmation qui suit n’est pas de nature à tranquilliser :

[![02-securite](/media/2017/01/02-securité-169x300.jpg)](/media/2017/01/02-securité.jpg)

De mon expérience précédente, je n’essaie même pas d’appairer le switch via le répéteur ; mais je le fait directement au sous-sol, où se situe mon atelier de bricolage. Je commence bien sûr par un câblage du réseau et d’une prise femelle, et y branche une lampe. Le témoin vert commence à clignoter.

Malgré les précautions prises, cet appairage s’avère ardu. Il faut de la patience… 3 minutes par essai.

[![03-ewelink-pairing](/media/2017/01/03-ewelink-pairing-169x300.jpg)](/media/2017/01/03-ewelink-pairing.jpg)

Après x essais, je prends le parti d’y aller « à la main », comme proposé à l’écran suivant.

[![03-ewelink-pair-fail](/media/2017/01/03-ewelink-pair-fail-169x300.jpg)](/media/2017/01/03-ewelink-pair-fail.jpg)

## Mécanisme d’appairage

Là, je comprends mieux le système : lorsqu’on appuie 5 secondes sur le bouton du switch (il sert aussi à enclencher/déclencher à la main), le WiFi interne du module se met en mode AP et présente une identification WiFi ; l’Apps connecte le WiFi du mobile sur le switch en mode AP, lui configure quelque chose, puis retourne sur la connexion WiFi « normale » et finalise la connexion sur le serveur. Il faut évidemment que ceci joue dans un certain laps de temps. Il suffit que le switch soit passé en mode client ; ou que le mobile n’ait pas eu le temps de tout faire pour « programmer » l’appairage et c’est à refaire.

Après quelques combats insoutenables, l’appairage est fait. Une fois le switch connecté, un bouton (renommable) se présente, et permet de le commuter.

Un coup d’œil sur la liste des appareils connectés sur le routeur montre ceci :

[![06-dhcp](/media/2017/01/06-DHCP.png)](/media/2017/01/06-DHCP.png)

Le genre de chip WiFi doit être le même pour la lampe Xiaomi et le switch que nous testons présentement. Intéressant, ce « ESP » au début de l’identification… Notez aussi le « computer » dont l’adresse finit par 107 : c’est mon portable Windows 10, qui demande un nombre impressionnant d’adresses IPV6. Les « android » sont le mobile de ma femme et le mien.

## Essai de timer

L’Apps propose une tempo pour enclencher/déclencher ; ainsi qu’un maximum 8 timers programmables à date fixe ou selon les jours de la semaine. La question est : que se passe-t-il si je programme un timer et que mon mobile se déconnecte du WiFi ?

Le test est effectué, en programmant un déclenchement dans 2 minutes, puis en mettant le mobile en mode « avion »… Test passé avec succès. Ceci signifie que c’est bien par le serveur distant que les ordres sont stockés et effectués. Ou que la puce du switch maintient l’heure et une liste d’enclenchement déclenchement ?

## Essai via la connexion GSM

La connexion WIFI du mobile est coupée. Comment va réagir le switch, si l’Apps n’est plus en connexion WiFi locale ?

Test : c’est fonctionnel. Donc, là on est sûr que ça passe bien par un serveur distant. Ou en bonne partie.

## Essai avec réseau local, sans Internet

Est-ce que la liaison locale ne suffit pas pour commander en On-Off ? Pour en voir le cœur net, je coupe la liaison Internet du routeur ; le téléphone fixe de la maison devient hors service… Malgré la liaison WiFi active, par lequel tout le potentiel local subsiste, pas moyen d’actionner le switch. La preuve est bien là : les ordres de commutation instantanés passent aussi via le serveur chinois.

[![04-ewelink-device-offline](/media/2017/01/04-ewelink-device-offline-576x1024.jpg)](/media/2017/01/04-ewelink-device-offline.jpg)

## Réponse aux sollicitations

Passant par un serveur distant, on peut s’attendre à quelque délai. Toutefois, si la connexion et établie, c’est-à-dire que l’application est en avant-plan et que le réseau est stable, le délai entre le moment où l’on clique sur le bouton et l’activation du relais ne dépasse pas les 200 ms. A l’oreille bien sûr, je n’ai pas mis en place des conditions de labo pour cette mesure ! Et à l’oreille, parce que c’est bien un relais électromécanique qui clique dans le switch, et non un triac qui commute silencieusement.

Un ping sur <www.ewelink.com> montre une réponse de 27 ms. C’est peu. Comment est-ce possible ? Un coup d’œil sur le site répond à la question : ils utilisent le service « amazone cloud AWS » pour ce faire. Et via ce dominateur de la WebSphere qu’est Amazone, dont les serveurs sont distribués partout sur la planète. C’est aussi pourquoi l’Apps demande la localisation à l’inscription…

## Essais de coupure d’alimentation du switch

Dans un tel cas, le switch doit reprendre la connexion WiFI avec le routeur/AP. Pour vérifier son temps de reconnexion, je lance un ping -t sur son adresse. Et lui coupe le jus.

Test : j’allume la barrette sur laquelle le switch est connecté et enclenche le chrono, puis observe la fenêtre des pings… il reprend la ligne en 5 secondes ! Si tous les appareils connectés en faisaient autant…

## Conclusion provisoire

Le switch remplit sa fonction. Il est à dispo, reconnecté et reconnectable, rapide. L’état est à jour sur l’Apps, même en cas de changement manuel par le bouton. Les renommages, ajouts, ou encore du groupage (pas essayé avec 1 élément…) sont pratiques. Les fonctions de timers sont raisonnablement sûres.

On peut toutefois blâmer la difficulté à appairer les devices. Pour un bricoleur/développeur, on attend de pourvoir utiliser en direct de tels éléments avec une API de sorte ; ce qui ne semble pas le cas. A moins de sortir l’artillerie lourde et d’espionner les flux TCP-IP, on ne saura pas quel est le protocole. C’est bien dommage.

Tout bouge et tout change, c’est à surveiller.

Yves Masur (1/2017)

Références:\
[lampe LED Xiaomi\
](http://www.banggood.com/Original-Xiaomi-LED-Smart-Table-Lamp-Dimming-Reading-Light-For-Cellphone-p-1057361.html?rmmds=search)[Relais Sonoff](http://forum.banggood.com/forum-topic-132828.html)

## Commentaires

### Yves Masur — 21 janvier 2017 à 16:20

Démonté, le print du Sonoff montre bien un ESP8266EX/PAGX80 en SMD, carré de 4 x 8 pattes, et une mémoire PN25F08, Flash série de 8Mbits. Il comporte aussi une alim à découpage, 3 transistors et une circuiterie plus complexe que je m’imaginais.

### Yves Masur — 7 février 2017 à 22:36

Relais physique ou Triac? N. Jeanmonod préfère le relais pour sa coupure franche. Afin de savoir quelle sont les fuites d’un triac (celui utilisé dans le projet barrette), j’ai fait les mesures suivantes.\
j’ai mesurée la tension résiduelle après un triac. Avec un voltmètre sur une prise libre, triac OFF, j’obtiens 112VAC. L’impédance est de 10 MOhms. Le courant en CC est de 0.01 mA (mais le multimètre hésite entre 0 et 1 pour le dernier digit quand je tient en l’air…)

Si je mesure sur une prise qui a deux chargeurs de mobile et un transfo , bref quelques charges, la tension est de 0,14 VAC.\
Avec un voltmètre analogique, sur la gamme:\
1000 j’ai env. 100 VAC\
250, j’ai ~35 VAC\
50, env. 7,5 VAC,\
10, env. 1,5 VAC\
soit approximativement la même déviation d’aiguille.\
Il a une impédance de 8000 Ohms/VAC

Le courant serait donc: 1,5/(10 \* 80000) = 1,875 uA. Donc, en chargeant avec une R de 100 KOhms, on aurait une tension résiduelle de 0.18V. Ce n’est pas \*rien\*, mais acceptable.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
