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
<div data-block="true" data-editor="ca46p" data-offset-key="emmb2-0-0">
<div data-offset-key="emmb2-0-0"><span data-offset-key="emmb2-0-0">Je travaille depuis quelques semaines sur mon interface/télécommande pour mon enregistreur Revox B77. J’ai presque terminé mon interface WEB au niveau fonctionnalités (j’ai appris à utiliser HTML, JS, CSS, WEBSOCKETS, JSON dans tous les sens) la télécommande fonctionne presque mais j’aimerais ajouter des délais pour retarder ou avancer le freinage des bandes du B77. Je crée donc une page web supplémentaire avec les délais, j’utilise pour ceci la fonction HTML « input type=nombres ». Je veux lire un nombre entier (de -100 à  +100) à mémoriser dans l’EEPROM de mon ESP8266. Je déclare les variables pour le stockage intermédiaire en « int » et les premiers essais sont concluants, les nombres sont bien mémorisés (Serial.print… m’indique le bon fonctionnement).</span></div>
<p> </p>
<div data-offset-key="emmb2-0-0"><a href="/2017/07/14/petit-rappel-des-differences-de-processeurs-en-programmation-de-c/revoxb77_main/" rel="attachment wp-att-3396"><img alt="" height="172" src="/media/2017/07/revoxb77_main-300x172.jpg" width="300"/></a><a href="/2017/07/14/petit-rappel-des-differences-de-processeurs-en-programmation-de-c/b77_stop/" rel="attachment wp-att-3395">      <img alt="" height="172" src="/media/2017/07/B77_stop-300x155.jpg" width="333"/></a></div>
<p data-offset-key="emmb2-0-0">&lt;Interfaces après correction&gt;</p>
<div data-offset-key="emmb2-0-0"></div>
<div data-offset-key="emmb2-0-0"><span data-offset-key="emmb2-0-0"> Surprise, après Reset du module ESP, les nombres restitués s’affichent juste pour les nombres positifs, mais faux pour les nombres négatifs ! J’ai l’impression que « C » utilise un « unsigned int » pour restituer les nombres alors que je les ai bien déclarés en « int ». L’effet est qu’à la place de m’afficher par exemple « -100 » il m’affiche « 65436 » Damned!</span></div>
</div>
<div data-block="true" data-editor="ca46p" data-offset-key="7h5qd-0-0">
<div data-offset-key="7h5qd-0-0"><span data-offset-key="7h5qd-0-0">Après 4h de tests et une revue de chaque ligne de code, il est passé 2h du matin, quand je me dis que « int » n’est peut-être pas la bonne définition !!!! Processeur 32 bits =&gt; « int » correspond à « int32_t » et non pas « int16_t » ce qui expliquerait le comportement ! Je remplace les déclarations des variables en int16_t (-32767 à +32767) et tout rentre dans l’ordre ! je peux enfin aller me coucher ! Mon code est prêt pour un nouveau test pratique !!!</span></div>
<div data-offset-key="7h5qd-0-0"></div>
</div>
<div data-block="true" data-editor="ca46p" data-offset-key="de7d1-0-0">
<div data-offset-key="de7d1-0-0"><span data-offset-key="de7d1-0-0">Super la programmation, mais pleine d’embûches !!!</span></div>
</div>
<p> </p>
<div data-block="true" data-editor="ca46p" data-offset-key="3vv7r-0-0">
<div data-offset-key="3vv7r-0-0"><span data-offset-key="3vv7r-0-0">Rolf Ziegler 7/2017<br/>
</span></div>
<div data-offset-key="3vv7r-0-0">Présentation du projet au printemps 2018</div>
</div>

## Commentaires

### Nicolas Jeanmonod — 15 juillet 2017 à 12:18

<section class="comment-content comment">
<p>Il me semble que c’est une contrainte du stockage en EEPROM. Malheureusement, la documentation a été écrite par un manche de pelle qui n’a pas précisé clairement ce point :</p>
<p><a href="https://github.com/esp8266/Arduino/blob/master/doc/libraries.rst#user-content-eeprom" rel="nofollow ugc">https://github.com/esp8266/Arduino/blob/master/doc/libraries.rst#user-content-eeprom</a></p>
<p>Il indique que l’on doit appeler `EEPROM.begin(size)` avant de lire ou d’écrire dans l’EEPROM et que `size` est le nombre d’octets que l’on veut utiliser. Mais il ne dit pas si ce nombre concerne les adresses ou le contenu de la mémoire.</p>
<p>Comme l’EEPROM est limité en nombre d’écritures que tu peux faire, je me demande si tu ne ferais pas mieux de stocker tes valeurs sur le système de fichiers SPIFFS.</p>
 </section>

### Yves Masur — 15 juillet 2017 à 17:36

<section class="comment-content comment">
<p>L’utilisation de int en C est un problème ancien. En effet, les compilateurs K&amp;R ont assumé que int était la largeur de bits du CPU utilisé… Dès que le C est venu sur des CPU 8 bits, p. ex. Keil qui a porté un C sur 8051 fin des années 80, a utilisé char pour 8 bits, et int était 16 bits. Souvent, le 16 bits était représenté par WORD. Sans parler de l’ordre des octets Big Endian, Little Endian.<br/>
Pour revenir à ton problème, il semble que le int en question passe par un pilote qui écrit/lit en EEPROM. Et c’est à ce niveau qu’il y a un masquage (style 0xFFFF), sans propagation du signe.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
