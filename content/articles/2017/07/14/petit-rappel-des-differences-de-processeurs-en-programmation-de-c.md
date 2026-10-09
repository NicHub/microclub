---
title: "Petit rappel des différences de processeurs en programmation de C."
date: "2017-07-14T10:02:15"
lastmod: "2017-07-14T13:41:20"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["b77", "c-programming", "html", "interface", "remote", "revox"]
url: "/2017/07/14/petit-rappel-des-differences-de-processeurs-en-programmation-de-c/"
wordpress_id: 3394
comment_count: 2
---

Je travaille depuis quelques semaines sur mon interface/télécommande pour mon enregistreur Revox B77. J’ai presque terminé mon interface WEB au niveau fonctionnalités (j’ai appris à utiliser HTML, JS, CSS, WEBSOCKETS, JSON dans tous les sens) la télécommande fonctionne presque mais j’aimerais ajouter des délais pour retarder ou avancer le freinage des bandes du B77. Je crée donc une page web supplémentaire avec les délais, j’utilise pour ceci la fonction HTML « input type=nombres ». Je veux lire un nombre entier (de -100 à  +100) à mémoriser dans l’EEPROM de mon ESP8266. Je déclare les variables pour le stockage intermédiaire en « int » et les premiers essais sont concluants, les nombres sont bien mémorisés (Serial.print… m’indique le bon fonctionnement).

[![](/media/2017/07/revoxb77_main-300x172.jpg)](/2017/07/14/petit-rappel-des-differences-de-processeurs-en-programmation-de-c/revoxb77_main/)[![](/media/2017/07/B77_stop-300x155.jpg)](/2017/07/14/petit-rappel-des-differences-de-processeurs-en-programmation-de-c/b77_stop/)

\<Interfaces après correction\>

 Surprise, après Reset du module ESP, les nombres restitués s’affichent juste pour les nombres positifs, mais faux pour les nombres négatifs ! J’ai l’impression que « C » utilise un « unsigned int » pour restituer les nombres alors que je les ai bien déclarés en « int ». L’effet est qu’à la place de m’afficher par exemple « -100 » il m’affiche « 65436 » Damned!

Après 4h de tests et une revue de chaque ligne de code, il est passé 2h du matin, quand je me dis que « int » n’est peut-être pas la bonne définition !!!! Processeur 32 bits =\> « int » correspond à « int32_t » et non pas « int16_t » ce qui expliquerait le comportement ! Je remplace les déclarations des variables en int16_t (-32767 à +32767) et tout rentre dans l’ordre ! je peux enfin aller me coucher ! Mon code est prêt pour un nouveau test pratique !!!

Super la programmation, mais pleine d’embûches !!!

Rolf Ziegler 7/2017\

Présentation du projet au printemps 2018

## Commentaires

### Nicolas Jeanmonod — 15 juillet 2017 à 12:18

Il me semble que c’est une contrainte du stockage en EEPROM. Malheureusement, la documentation a été écrite par un manche de pelle qui n’a pas précisé clairement ce point :

<https://github.com/esp8266/Arduino/blob/master/doc/libraries.rst#user-content-eeprom>

Il indique que l’on doit appeler \`EEPROM.begin(size)\` avant de lire ou d’écrire dans l’EEPROM et que \`size\` est le nombre d’octets que l’on veut utiliser. Mais il ne dit pas si ce nombre concerne les adresses ou le contenu de la mémoire.

Comme l’EEPROM est limité en nombre d’écritures que tu peux faire, je me demande si tu ne ferais pas mieux de stocker tes valeurs sur le système de fichiers SPIFFS.

### Yves Masur — 15 juillet 2017 à 17:36

L’utilisation de int en C est un problème ancien. En effet, les compilateurs K&R ont assumé que int était la largeur de bits du CPU utilisé… Dès que le C est venu sur des CPU 8 bits, p. ex. Keil qui a porté un C sur 8051 fin des années 80, a utilisé char pour 8 bits, et int était 16 bits. Souvent, le 16 bits était représenté par WORD. Sans parler de l’ordre des octets Big Endian, Little Endian.\
Pour revenir à ton problème, il semble que le int en question passe par un pilote qui écrit/lit en EEPROM. Et c’est à ce niveau qu’il y a un masquage (style 0xFFFF), sans propagation du signe.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
