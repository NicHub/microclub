---
title: "Enfer CPL"
date: "2007-11-26T13:03:48"
lastmod: "2015-04-24T23:20:23"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["hardware", "reseau"]
url: "/2007/11/26/enfer-cpl/"
wordpress_id: 22
comment_count: 0
---
<p>Mon modem ADSL est à la cave, où arrive ma ligne ISDN, mais mes PC sont dans toute la maison, qui est assez vaste et dotée de murs assez épais pour que le Wifi ne parvienne pas dans tous les coins. Après plusieurs tentatives avec de meilleures antennes et des répéteurs, je me suis rabattu sur un réseau à <a href="http://www.cpl-france.org/" target="_blank">Courants Porteurs en Ligne</a> (CPL) qui fonctionne très bien.</p>
<p>Jusqu’à ce week-end, où après avoir <a href="/2007/11/29/petit-upgrade-deviendra-grand/">upgradé une de mes machines</a>, le débit réseau vers tous mes PC a chuté à quelques kilo-octets / seconde au grand maximum. ça fait bizarre de se retrouver d’un coup au bon vieux temps des modems 9600 bauds, mais les PC modernes sont encore moins tolérants : plus rien ne fonctionne.</p>
<p>J’ai passé tout le week-end à suspecter Sunrise, mon modem ADSL, le driver réseau de mon « nouveau » PC et même mon réseau CPL qui marchait bien jusque là… Finalement, après de nombreuses péripéties que je vous épargne ici, le diagnostic était le suivant :</p>
<ul>
<li>quand mon nouveau PC était éteint, tout marchait bien</li>
<li>quand mon nouveau PC était allumé, « ping 192.168.1.1 » donnait entre 1000 et 2000 millisecondes de délai entre n’importe quel PC et le modem ADSL, mais pratiquement pas de paquets perdus</li>
<li>le diagnostic de mon CPL m’annonçait fièrement 10 à 20 Mb/s dans les deux cas …</li>
</ul>
<p>Soudain l’éclair de compréhension : la nouvelle alim de mon PC perturbe le réseau 220V, donc le CPL ! Je me remémore une ligne du mode d’emploi déconseillant de brancher les prises CPL sur une prise multiple partagée avec le PC, conseil que j’avais ignoré parce que ça marchait très bien… Déplacement de la prise = retour au 21ème siècle, et je peux écrire cet article, tout va bien.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
