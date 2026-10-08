---
title: "La barrette secteur écologique MICROCLUB"
date: "2008-12-06T21:43:12"
lastmod: "2015-04-24T23:21:14"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["ecologie", "futur", "gadgets", "hardware", "processeurs", "programmation", "reseau", "web"]
url: "/2008/12/06/la-barrette-secteur-ecologique-microclub/"
wordpress_id: 110
comment_count: 8
---
<h2>L’idée</h2>
<p>M’est venue en pensant à tous ces périphériques connectés plus ou moins intelligemment sur le secteur, que l’on pouvait faire mieux. Mieux que laisser ce bazar enclenché ou au mieux, enclenché/déclenché par le PC de bureau.</p>
<p>Un simple (!) horloge fait déjà mieux. Mais est-ce suffisant?</p>
<p><img alt="horloge-electronique" height="218" src="/media/2008/12/horloge-electronique.jpg" title="horloge-electronique" width="285"/></p>
<h2>L’utilité</h2>
<p>Par exemple, vous avez un PC, lampe de de bureau, chargeurs divers, imprimante, modem VDSL et routeur wi-fi.<br/>
Si le PC est allumé, tout est enclenché. Par contre, s’il est éteint, la lampe de bureau doit être éteinte. Les chargeurs devraient être enclenchés comme le PC, mais avec au moins un minimum de 6H par jour (horloge + tempo). Par contre, l’imprimante (réseau?) ainsi que le VDSL et le wi-fi restent allumés jusqu’à 23h. Sauf s’il y a du trafic internet: un portable est peut-être toujours actif, par exemple.<br/>
L’horloge pour ce bazar pourrait être 17h-23h les jours de semaine, 8h-24h00 samedi, 9h-23h dimanche. Le tout programmable, bien sûr. Par contre si quelqu’un utilise le PC la journée, le reste s’enclenche aussi et serait maintenu tant qu’il y a du trafic sur le net. Ou par un bouton qui lance une tempo de, mettons 1h, puis surveille le trafic réseau LAN pour les prolongations.</p>
<h2>Le projet</h2>
<p>Posons donc quelque définitions. Bien entendu, scalable et transformable à souhait!</p>
<p>Il faut au moins :</p>
<ul>
<li>6 prises</li>
<li>dont 2 assez espacées pour accepter des chargeurs</li>
<li>1 avec un capteur de courant,</li>
<li>5 relais de commande</li>
<li>Une horloge RTC</li>
<li>? Éventuellement un afficheur LCD</li>
<li>?  Un connecteur LAN RJ45</li>
<li>? une télécommande</li>
<li>un/des boutons</li>
<li>un CPU pour gérer tout ça</li>
<li>Une mécanique qui intègre cet ensemble</li>
</ul>
<p>Donc, en plus d’avoir des idées globales, il faut du personnel pour les réaliser:</p>
<ul>
<li>un électronicien (LAN, low-power, courant faible)</li>
<li>un informaticien (WEB + Embedded + realtime)</li>
<li>un mécanicien (boitier, plastic, industrialisation… 	si ça tire fort!)</li>
</ul>
<h2>Le goupe de réalisation</h2>

<p>Dans sa séance du 05/12/08, l’AG a décidé de porter cette proposition comme micro-projet, financé à hauteur de 1000.- pour les frais. Toute personne intéressée est donc priée d’annoncer sa participation auprès du soussigné: ymasur[at]microclub.ch</p>
<p>Il est prévu de se voir en avant séance du Microclub, éventuellement un autre jour/soir.</p>

## Commentaires

### Laurent Francey — 7 décembre 2008 à 10:22

<section class="comment-content comment">
<p>Super cette idée, et en plus sur cette base, on peut imaginer toutes sortes d’applications, de logiciels spécifiques ! Donc un projet super pour donner l’envie de bricoler. Je suis partant pour ce projet ! J’ai déjà plein d’idées ! on pourrait peut-être découper le projet en divers blocs qui pourraient donner naissance à un print pour chacun d’eux, avec cette solutions, on pourrait imaginer que le projet fonctionne sur plusieurs micro-contrôleurs, interface Ethernet ou USB, ou pourquoi pas via SMS ! pourquoi ne pas placer toutes les prises horizontales et non verticales ainsi tous les transfos prises ont leur place … enfin il y a tout de sorte d’idées la derrière. Afin de faire connaître le Microclub au monde entier, on pourrait même soumettre notre projet final à Elektor ? (traduit en 12 langues ) J’espère que le projet ne restera pas seulement au niveau du blog ! Mais connaissant l’initiateur, la barrette verra le jour !</p>
 </section>

### Jacques — 21 décembre 2008 à 14:26

<section class="comment-content comment">
<p>C’est en effet un projet intéressant. Pour les éléments directement utilisés par le PC, il existe déjà un bidule chez Conrad : un relais USB (voir <a href="http://www1.ch2.conrad.com/scripts/wgate/zcop_ch2/~flN0YXRlPTE1NzczMDQ3ODE=?direkt_aufriss_area=SHOP_AREA_22403&amp;~template=PCAT_AREA_S_browse&amp;p_page_to_display=&amp;catalogs_sub_id=sub1&amp;aktiv=1&amp;navi=oben_2" rel="nofollow ugc">http://www1.ch2.conrad.com/scripts/wgate/zcop_ch2/~flN0YXRlPTE1NzczMDQ3ODE=?direkt_aufriss_area=SHOP_AREA_22403&amp;~template=PCAT_AREA_S_browse&amp;p_page_to_display=&amp;catalogs_sub_id=sub1&amp;aktiv=1&amp;navi=oben_2</a> )</p>
<p>Un fabricant suisse produit aussi un appareil plus sophistiqué. Il fourni aussi un module (voir <a href="http://www.liisa.info/ShopNew/03b5e49b1611fba20/03b5e49b361476813.php" rel="nofollow ugc">http://www.liisa.info/ShopNew/03b5e49b1611fba20/03b5e49b361476813.php</a>)<br/>
J’en utilise un mais, du fait qu’il nécessite un driver, ce n’est pas aussi simple que la solution Conrad.</p>
<p>Bonne chance au projet</p>
<p>Jacques</p>
 </section>

### ymasur — 3 janvier 2009 à 08:39

<section class="comment-content comment">
<p>Voici quelques sujets de réflexions. Tout comme Laurent, je pense qu’il faut mettre les prises « horizontales » – ça donne plus de place. A côté ou dessous, il faut un bouton poussoir pour forcer l’enclenchement, avec un témoin LED combiné (ex. 70 12 36-15 chez Conrad), car il faut savoir où l’on en est!<br/>
Un filtrage HF est simple à mettre en oeuvre avec un tore ferrite. Une barette comportant un filtre est vite onéreuse: voir 05 94 11-83 (110.- chez Conrad).<br/>
Maintenant, même s’il y a plusieurs contrôleurs, le principal devra être placé en bout de la barette, avec une alimentation, que je suppose à 5 VDC.</p>
<p>Question câblage, on peut se poser la question s’il faut amener la phase par un relais (ex. 50 38 90-15 à 5.45) ou un triac, p. ex 621032 Distrelec? Dans ce cas, il faut également penser à un optocouplage… Et s’il faut concentrer les éléments de commande prés du CPU/Alimentation, ou les répartir près des prises?<br/>
Yves Masur</p>
 </section>

### Yves Masur — 29 avril 2009 à 17:51

<section class="comment-content comment">
<p>Aie! Il y a un sérieux concurrent ici:<br/>
<a href="http://newsletter.arp.com/u/gm.php?prm=EwUUhwOTGy_115008531_136166_3804" rel="nofollow ugc">http://newsletter.arp.com/u/gm.php?prm=EwUUhwOTGy_115008531_136166_3804</a></p>
<p>Mais visiblement, pas d’horloge!! La doc est trop spartiate pour savoir ce que fait cette multiprises IP; et si sa consommation en « stand-by » est acceptable.</p>
 </section>

### Jacques — 3 mai 2009 à 08:06

<section class="comment-content comment">
<p>Yves,<br/>
Tout d’abord merci pour ta présentation de vendredi passé.<br/>
J’ai essayé d’analyser mes besoins en fonction de tes explications. Les appareils à alimenter seraient les suivants :<br/>
– PC 1 avec ses périphériques (moniteur 1 , HP 1)<br/>
– PC 2 avec ses périphériques (moniteur 2, HP 2)<br/>
– moniteur 3 connecté aux PC 1 et PC 2 (moniteur avec 2 entrées)<br/>
– serveur WHS avec périphérique (imprimante)<br/>
– routeur 1 Gz, routeur Netopia, routeur WIFI<br/>
– chargeur PC portable<br/>
Avant de définir le fonctionnement désiré, il est nécessaire de savoir que le serveur, un Windows Home Server (WHS), est déjà piloté par un module complémentaire, LightsOut (voir <a href="http://blog.monhomeserver.fr/2009/03/26/lightsout-francais-080/" rel="nofollow ugc">http://blog.monhomeserver.fr/2009/03/26/lightsout-francais-080/</a>) qui le met en hibernation si tous les PC de mon réseau (Ethernet et WIFI) sont déclenchés. D’autre part le serveur se met en route entre 01:00 et 04:00 pour effectuer automatiquement le backup de tous les PC.<br/>
Pour répondre à mes voeux, la barette devrait comporter 8 prises dont 3 avec mesures de courant (prise Master) pour alimenter les 2 PC et le serveur. Une table permettrait de définir à quel master sont attribués les 5 prises Slave. Une Slave peut être attribuée à plusieurs Master (fonction OU, dans mon cas le moniteur 3 est allimenté dès que le PC 1 ou le PC 2 est enclenché). Une table horloge devrait permettre d’empécher l’enclenchement des prises Slave pendant certaines périodes (par exemple pendant le backup de nuit il n’est pas nécessaire que les moniteurs et HP se mettent en marche. Surtout ces derniers, car c’est désagréable d’entendre à 2 heure du matin qu’Avast a fait une mise à jour …). Les prises Slave peuvent bien entendu aussi n’être dépendantes que de l’horloge (par exemple chargeur du PC portable).<br/>
En ce qui concerne les possibilités de déclencher les équipements réseau (routeurs), j’ai besoin d’aide. Il serait possible de les alimenter par une prise Slave dépendante des 3 Master. Mais je ne sais pas si le temps nécessaire au Netopia pour accéder à l’ADSL ne provoquerait pas un problème. D’autre part le PC réseau, connecté par Ethernet, de ma femme est situé dans une autre pièce et donc invisible si le routeur est hors tension. De même les PC relié par WIFI ne seraient pas visible. Quelqu’un a des idées ?<br/>
Enfin une suggestion pour la réalisation du « bidule » :<br/>
– le seuil de courant des prises Master doit être réglable<br/>
– il faut un interrupteur principal<br/>
– ne serait il pas possible de prendre une barette 8 prises de travers du commerce et de la relier par un câble multifilaires (longeur entre 1,5 et 3 mètres?) à un boitier qui contiendrait l’électronique,  l’alimentation, l’interrupteur principal, les 8 LED d’état et les 8 interrupteurs ? Cette solution permetrait de ne pas modifier la barette de prises (il faut juste pouvoir connecter les 8 fils) et d’avoir sur la table le coffret de commande bien visible.<br/>
Qu’en pensez-vous ?</p>
 </section>

### Yves Masur — 3 mai 2009 à 16:22

<section class="comment-content comment">
<p>Hé bien voilà une config intéressante! Quand à la question des prises avec mesure iraient sur une entrée A/D: a priori, on peut régler le seuil d’enclenchement, je suppose même qu’un hystérésis + tempo sont indispensables.</p>
<p>Concernant les prises slave, le OU est certainement envisageable. Maintenant, pour des fonction plus élaborées, je suppose que des pages contenant des macros, démarrées par l’application particulière peuvent – ceci par n’importe quel PC – envoyer des commandes d’enclenchement/déclenchement au bidule. Pour le déclenchement (exemple du PC dans une autre pièce, ou portable par Wi-FI, on peut en déduire l’activité ou non par un ping. Cependant, je n’ai pas encore de telle solution via le module Modtronix.</p>
<p>La suggestion d’utiliser une barrette du commerce va être étudiée, en vue de baisser les coûts du hardware. Par contre, Laurent m’a rendu attentif au fait que ces blocs sont constitués de formes en plastic, et les connexions sous-jacentes sont faites par des lames pré-formées, pas du tout évident à modifier.</p>
<p>Un boîtier et des sorties sur une barrette, pourquoi pas? je pensais faire le proto dans ce sens. Et pourquoi pas 8 fiches volantes, de longueur différrentes. A voir!</p>
 </section>

### ↳ Réponse — Jacques — 4 mai 2009 à 08:09

<section class="comment-content comment">
<p>L’observation de Laurent est aussi valables pour les barettes de prises « de travers » ?<br/>
Je verrais mieux des prises comme sur le boitier ARD que 8 « queues » …</p>
 </section>

### Yves Masur — 20 juin 2009 à 20:17

<section class="comment-content comment">
<p>Bienvenue à Georges Barré, qui remforcera le développement soft de ce projet.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
