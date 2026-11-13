---
title: "P19 Montage de base"
date: "2019-06-05T10:20:11"
lastmod: "2019-06-05T10:20:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: []
url: "/2019/06/05/p19-montage-de-base/"
wordpress_id: 4547
comment_count: 0
---
<p>La, les cartes ont été livrée avec les composants CMS montés, sans les composants pour la carte SD ainsi que les capteurs IR dans les coins, ceux-ci peuvent être monté plus tard si besoins.</p>
<p></p>
<p><br/></p>
<figure><img alt="" height="480" src="/media/2019/06/P19-CPU-OLED.jpg" width="640"/></figure>
<p>Ici la photo avec le module ESP32(Version 38 pins) insérée. On peut-y voir les 4 neo-pixels touts montées en série, la pin « NEO » permet de commander les neo-pixels. Le fichier P19.h continent toutes les définitions des pins utiles et pré-câblées sur la carte. Fichier disponible dans ce forum</p>
<p>La photo montre également le connecteur Accu (Blanc) ce dernier n’est utile que pour alimenter la carte (pas les moteurs). Photo du proto, les cartes livrées n’ont pas le fil rouge à côté de l’interrupteur.</p>
<figure><img alt="" height="480" src="/media/2019/06/P19-Gyro.jpg" width="640"/><figcaption>On voit ici un gyroscope câblé sur le connecteur approprié (voir schéma). Ce connecteur se trouve en dessous de l’affichage OLED. Un exemple de code pour afficher le gyro sur le display est également disponible dans le forum. La photo montre également le circuit RTC qui se trouve sous l’emplacement du processeur (DS3231M) demandé par certains membres. A côté on observe le circuit MCP32017, circuit permettant de gérer les interruptions non prioritaires offrant également 8 lignes IO supplémentaires à notre montage.</figcaption></figure>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
