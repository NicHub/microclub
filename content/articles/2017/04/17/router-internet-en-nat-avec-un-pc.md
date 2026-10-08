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
<h3>Besoin</h3>
<p>La configuration est la suivante : vous avez un PC portable (ou pas…) qui est connecté en Wi-Fi à Internet, et vous voulez router l’internet sur sa prise LAN sur laquelle peuvent être connectés différents hardwares, mais qui n’ont, eux, pas de Wi-Fi. Ou une connexion Wi-Fi est obtenue avec un code, et vous avez besoin de la partager.  Les différentes possibilités de partage sont décrites sur ce blog : <a href="https://anwaarullah.wordpress.com/2013/08/12/sharing-wifi-internet-connection-with-raspberry-pi-through-lanethernet-headless-mode/">https://anwaarullah.wordpress.com/2013/08/12/sharing-Wi-Fi-internet-connection-with-raspberry-pi-through-lanethernet-headless-mode/</a></p>
<p>Le matériel minimum suivant est requis :</p>
<ul>
<li>Un routeur Wi-Fi, connecté sur l’Internet</li>
<li>PC avec 2 connexions LAN : Wi-Fi et RJ45 ; l’OS Win10 (Win7 aussi testé)</li>
<li>Un câble LAN croisé (rouge)</li>
<li>Un « device » à connecter, par exemple un RaspBerry Pi 2</li>
</ul>
<p>Bien entendu, le « device » peut être autre : Arduino, second PC, etc.</p>
<p>Bref, un schéma est plus simple pour l’expliquer.</p>
<p><a href="/media/2017/04/1_schema_link.jpg"><img alt="" height="213" src="/media/2017/04/1_schema_link.jpg" width="788"/></a><br/>
Le PC est connecté sur le routeur internet par son Wi-Fi, et le RaspBerry Pi par un câble croisé (câble rouge) à la prise LAN du PC. Bien entendu, un petit switch qui s’occupe du croisement automatiquement irait très bien aussi.</p>
<h3>Partager la connexion</h3>
<p>Il y a 3 options (ou peut être plus) pour établir la liaison :</p>
<ul>
<li>Le Network Translation Adress, ou NAT</li>
<li>Le pont – transparence de connexion</li>
<li>Le partage de la connexion</li>
</ul>
<h3>Activer le NAT</h3>
<p>On va utiliser la première, car vu du routeur Wi-Fi, seule l’adresse du PC est distribuée. Les autres options demandent au routeur Wi-Fi de distribuer en DHCP une adresse supplémentaire pour le RaspBerry.</p>
<p>Le NAT s’occupe de modifier les paquets IP pour changer l’adresse de la carte A en adresses de la carte B. C’est utilisé pour créer des sous-réseaux, et grouper une série de machines avec une seule adresse sur l’Internet. Voir : <a href="https://fr.wikipedia.org/wiki/Network_address_translation">https://fr.wikipedia.org/wiki/Network_address_translation</a></p>
<h2>Réglage des cartes LAN</h2>
<h3>Partage du WI-FI</h3>
<ul>
<li>Clic Droit sur icone Windows de la barre des tâche-&gt; Connexions réseau<a href="/media/2017/04/2_Connexion_reseau.jpg"><img alt="" height="197" src="/media/2017/04/2_Connexion_reseau.jpg" width="970"/></a></li>
<li>Clic droit sur le Wi-Fi -&gt; Propriétés</li>
<li>Onglet « partage »</li>
<li>Cocher « Autoriser… » et décocher la seconde option si besoin</li>
</ul>
<p><a href="/media/2017/04/3_Partage.jpg"><img alt="" height="316" src="/media/2017/04/3_Partage.jpg" width="545"/></a></p>
<p>Si vous avez plus d’une carte, il faut choisir laquelle sera utilisée pour ce partage:</p>
<p><a href="/media/2017/04/Capture-décran-2017-04-29-16.59.49.png"><img alt="" height="231" src="/media/2017/04/Capture-décran-2017-04-29-16.59.49.png" width="618"/></a></p>
<p>Après quelques secondes, la carte Ethernet obtient la configuration suivante, à vérifier en ligne de commande par<strong> ipconfig</strong> :</p>
<p><a href="/media/2017/04/4_ipconfig_ethernet.jpg"><img alt="" height="211" src="/media/2017/04/4_ipconfig_ethernet.jpg" width="743"/></a></p>
<p>Ou encore en ouvrant la carte Ethernet et en lisant ses propriétés IPV4. Au départ, les champs sont vides : ils sont remplis par le partage de connexion. La carte prend l’adresse 192.168.137.1/24. L’adresse de la passerelle reste vide, ainsi que les DNS.</p>
<p><a href="/media/2017/04/5_proprietes.jpg"><img alt="" height="403" src="/media/2017/04/5_proprietes.jpg" width="361"/></a></p>
<h2>Contrôle de la connexion NAT</h2>
<ul>
<li>Connecter le RaspBerry sur le LAN du PC, à savoir la carte Ethernet</li>
<li>L’enclencher, pour qu’il prenne une adresse IP</li>
</ul>
<p>Si le Raspberry était déjà allumé, il aura pris une adresse bidon, genre 169.x.y.z et un masque réseau 255.0.0.0. On peut redémarrer les services réseau avec les commandes Linux:</p>
<p>sudo ifdown -a</p>
<p>sudo ifup -a</p>
<ul>
<li>Vérifier l’adresse prise par : <strong>ifconfig</strong> et la noter pour la suite</li>
<li>Vérifier l’accès à Internet avec : <strong>ping ch.ch</strong> (ou autre site répondant au ping)</li>
</ul>
<h2>Limites de la connexion NAT avec Win10</h2>
<p>L’adressage du sous réseau ne peut pas être choisi ; c’est Windows qui décide. Selon les essais, l’adresse de base est toujours 192.168.137.1, avec un réseau de classe C, à savoir 253 adresses à disposition, ce qui suffit amplement.</p>
<p>Avec un laptop qui se met en veille… le partage disparait ! La carte Ethernet (du PC donc) reprend une adresse du genre : 169.254.245.127, et un masque 255.255.0.0. Remettre la coche du partage sur la carte Wi-Fi relance la fonction NAT ; et si cela n’a pas duré trop longtemps, le « device » connecté aura gardé son adresse et reprend sa liaison. On peut bien sûr tester avec la commande <strong>ping ch.ch</strong> pour en vérifier la fonctionnalité.</p>
<p>Yves Masur (4/2017)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
