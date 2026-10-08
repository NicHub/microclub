---
title: "Ajout d'un routeur WiFi"
date: "2008-05-27T18:00:25"
lastmod: "2015-04-24T23:21:15"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["reseau"]
url: "/2008/05/27/ajout-dun-routeur-wifi/"
wordpress_id: 52
comment_count: 0
---
<p>Afin de me libérer des câbles, je me suis proposé d’ajouter un router WiFi dans ma config at home. Il faut savoir que depuis ma dernière expérience – pas concluante – le wireless a fait des progrès. Et les prix ont chuté à moins de 100.-. Or donc, je me décide pour un Netgear 54 Mb G, modèle WGR614. En oubliant que Netgear est le roi de l’utilisation du DHCP, et que j’ai tout mis mon matos en adresses fixes. Entre autre à cause d’un SAN Netgear qui bouffe 4 adresses IP, alors que le Modem Routeur n’en délivre que… 4.</p>
<p>Mais voyons ce qui se passe. Connecté, le router veut se mettre en 192.168.1.1. Cette adresse ne vous rappelle rien? C’est la même que celle du modem ADSL… Et il me signale qu’il n’arrive pas à reconnaître  la config du réseau, ni l’adresse fournie par mon provider. J’essaie ce demi-mensonge: oui, j’ai une adresse fixe, c’est 192.168.1.6 (vrai, mon PC est ainsi relié), et la passerelle par défaut est en 192.168.1.1. Mais peine perdue. J’apprends alors à utiliser le bouton de reset de la config (tenir 20 secondes).</p>
<p>A deux doigts de renoncer après moult essais, j’ai finalement opté pour la reconfiguration du modem ADSL, de manière à servir de DHCP pour 1 adresse, ce qui a passé. Une fois que le routeur Wifi a pris sa config, j’ai pu aller la figer en fixe, élargir le masque et reprogrammer le modem ADSL en fixe, comme avant.</p>
<p>Ouf! Maintenant j’ai deux connexions LAN.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
