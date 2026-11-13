---
title: "Router Internet en NAT avec un PC"
date: "2017-04-17T21:05:53"
lastmod: "2017-05-01T17:37:14"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["embarque", "ethernet", "lan", "linux", "nat", "reseau", "software", "systeme-dexploitation", "web", "wi-fi", "windows"]
url: "/2017/04/17/router-internet-en-nat-avec-un-pc/"
wordpress_id: 3244
comment_count: 0
---

### Besoin

La configuration est la suivante : vous avez un PC portable (ou pas…) qui est connecté en Wi-Fi à Internet, et vous voulez router l’internet sur sa prise LAN sur laquelle peuvent être connectés différents hardwares, mais qui n’ont, eux, pas de Wi-Fi. Ou une connexion Wi-Fi est obtenue avec un code, et vous avez besoin de la partager.  Les différentes possibilités de partage sont décrites sur ce blog : [https://anwaarullah.wordpress.com/2013/08/12/sharing-Wi-Fi-internet-connection-with-raspberry-pi-through-lanethernet-headless-mode/](https://anwaarullah.wordpress.com/2013/08/12/sharing-wifi-internet-connection-with-raspberry-pi-through-lanethernet-headless-mode/)

Le matériel minimum suivant est requis :

- Un routeur Wi-Fi, connecté sur l’Internet
- PC avec 2 connexions LAN : Wi-Fi et RJ45 ; l’OS Win10 (Win7 aussi testé)
- Un câble LAN croisé (rouge)
- Un « device » à connecter, par exemple un RaspBerry Pi 2

Bien entendu, le « device » peut être autre : Arduino, second PC, etc.

Bref, un schéma est plus simple pour l’expliquer.

[![](/media/2017/04/1_schema_link.jpg)](/media/2017/04/1_schema_link.jpg)\
Le PC est connecté sur le routeur internet par son Wi-Fi, et le RaspBerry Pi par un câble croisé (câble rouge) à la prise LAN du PC. Bien entendu, un petit switch qui s’occupe du croisement automatiquement irait très bien aussi.

### Partager la connexion

Il y a 3 options (ou peut être plus) pour établir la liaison :

- Le Network Translation Adress, ou NAT
- Le pont – transparence de connexion
- Le partage de la connexion

### Activer le NAT

On va utiliser la première, car vu du routeur Wi-Fi, seule l’adresse du PC est distribuée. Les autres options demandent au routeur Wi-Fi de distribuer en DHCP une adresse supplémentaire pour le RaspBerry.

Le NAT s’occupe de modifier les paquets IP pour changer l’adresse de la carte A en adresses de la carte B. C’est utilisé pour créer des sous-réseaux, et grouper une série de machines avec une seule adresse sur l’Internet. Voir : <https://fr.wikipedia.org/wiki/Network_address_translation>

## Réglage des cartes LAN

### Partage du WI-FI

- Clic Droit sur icone Windows de la barre des tâche-\> Connexions réseau[![](/media/2017/04/2_Connexion_reseau.jpg)](/media/2017/04/2_Connexion_reseau.jpg)
- Clic droit sur le Wi-Fi -\> Propriétés
- Onglet « partage »
- Cocher « Autoriser… » et décocher la seconde option si besoin

[![](/media/2017/04/3_Partage.jpg)](/media/2017/04/3_Partage.jpg)

Si vous avez plus d’une carte, il faut choisir laquelle sera utilisée pour ce partage:

[![](/media/2017/04/Capture-décran-2017-04-29-16.59.49.png)](/media/2017/04/Capture-décran-2017-04-29-16.59.49.png)

Après quelques secondes, la carte Ethernet obtient la configuration suivante, à vérifier en ligne de commande par **ipconfig** :

[![](/media/2017/04/4_ipconfig_ethernet.jpg)](/media/2017/04/4_ipconfig_ethernet.jpg)

Ou encore en ouvrant la carte Ethernet et en lisant ses propriétés IPV4. Au départ, les champs sont vides : ils sont remplis par le partage de connexion. La carte prend l’adresse 192.168.137.1/24. L’adresse de la passerelle reste vide, ainsi que les DNS.

[![](/media/2017/04/5_proprietes.jpg)](/media/2017/04/5_proprietes.jpg)

## Contrôle de la connexion NAT

- Connecter le RaspBerry sur le LAN du PC, à savoir la carte Ethernet
- L’enclencher, pour qu’il prenne une adresse IP

Si le Raspberry était déjà allumé, il aura pris une adresse bidon, genre 169.x.y.z et un masque réseau 255.0.0.0. On peut redémarrer les services réseau avec les commandes Linux:

sudo ifdown -a

sudo ifup -a

- Vérifier l’adresse prise par : **ifconfig** et la noter pour la suite
- Vérifier l’accès à Internet avec : **ping ch.ch** (ou autre site répondant au ping)

## Limites de la connexion NAT avec Win10

L’adressage du sous réseau ne peut pas être choisi ; c’est Windows qui décide. Selon les essais, l’adresse de base est toujours 192.168.137.1, avec un réseau de classe C, à savoir 253 adresses à disposition, ce qui suffit amplement.

Avec un laptop qui se met en veille… le partage disparait ! La carte Ethernet (du PC donc) reprend une adresse du genre : 169.254.245.127, et un masque 255.255.0.0. Remettre la coche du partage sur la carte Wi-Fi relance la fonction NAT ; et si cela n’a pas duré trop longtemps, le « device » connecté aura gardé son adresse et reprend sa liaison. On peut bien sûr tester avec la commande **ping ch.ch** pour en vérifier la fonctionnalité.

Yves Masur (4/2017)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
