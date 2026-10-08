---
title: "Niveau de complexité"
date: "2018-08-26T20:52:52"
lastmod: "2018-08-26T20:54:35"
author: "Rolf Ziegler"
categories: ["Articles"]
tags: ["arduino", "divers", "initiation", "programmation", "securite"]
url: "/2018/08/26/niveau-de-complexite/"
wordpress_id: 3985
comment_count: 0
---
<h2>Introduction</h2>
<figure aria-describedby="caption-attachment-3987"><a href="/media/2018/08/LED-adafruit.jpg"><img alt="" height="150" src="/media/2018/08/LED-adafruit-150x150.jpg" width="150"/></a><figcaption>LED (image: Adafruit)</figcaption></figure>
<p>Quelles peuvent être les niveaux de complexité d’un système (ou d’une combinaison de systèmes) permettant de faire clignoter, ou commuter une LED ? Voici un petit aperçu de ce que l’on pourrait voir comme une progression se pliant aux besoins (voir les devançant…) de l’utilisateur.</p>
<h2>Niveau 0</h2>
<figure aria-describedby="caption-attachment-3991"><a href="/media/2018/08/clign555.gif"><img alt="" height="188" src="/media/2018/08/clign555.gif" width="208"/></a><figcaption>Montage NE555 – exemple</figcaption></figure>
<p>Une LED clignote avec une électronique : un chip 555, associé à 2 résistances et un condo pour la base de temps du clignotement.</p>
<h2>Niveau 1</h2>
<p>Un Arduino (ou tout autre module) fait clignoter la LED à 50% avec une boucle software comportant 2 attentes, et une inversion de la sortie active ou arrêtée. Il faut retoucher le code source pour changer la période allumé/éteinte, le compiler et le recharger.</p>
<figure aria-describedby="caption-attachment-3988"><a href="/media/2018/08/blink.jpg"><img alt="" height="159" src="/media/2018/08/blink.jpg" width="337"/></a><figcaption>Exemple de programme Arduino: blink.ino (partiel)</figcaption></figure>
<h2>Niveau 2</h2>
<p>Des boutons de commande contrôlent la séquence : plus ou moins rapide. Les paramètres de boucle et de n° de sortie utilisée sont dans des variables, qui sont lues de la mémoire flash par le programme. Un bouton permet d’enregistrer la config ainsi modifiée. Le programme gère les interruptions, sans forcément être multitâche.</p>
<h2>Niveau 3</h2>
<p>Le module a une liaison série ou IP en SSH, à laquelle une console permet d’envoyer des commandes. Le programme a un mini interpréteur, qui réagit à des commandes série ou en SSH : ‘+’ et ‘-‘, ‘s’ = sauver ; ‘r’ = relire les temps, voire de modifier le rapport cyclique. On n’oubliera pas le help, avec le caractère ‘ ?’. Le programme est multitâche.</p>
<h2>Niveau 4</h2>
<p>Le module a un serveur de pages WEB. Une page contient des boutons et des champs permettant de régler les variables, de les enregistrer et de les sauver. Ceci à distance du module. Idéalement, ce mode d’action est compatible avec le niveau 2 et comporte les boutons hardware pour une action locale</p>
<h2>Niveau 5A</h2>
<p>Le module a un serveur WEB, une liaison sécurisée, une base de donnée (DB), une synchro NTP pour une mise à l’heure exacte. Il enregistre les événements, tels que les arrêt/démarrages du système, les connexions. Les manipulations sont dans la base de données. Il envoie un email d’alerte lorsque des tentatives d’intrusions sont faites.</p>
<figure aria-describedby="caption-attachment-3989"><a href="/media/2018/08/mvc_diagram_with_routes.png"><img alt="" height="1274" src="/media/2018/08/mvc_diagram_with_routes.png" width="1998"/></a><figcaption>source: selftaughtcoders.com</figcaption></figure>
<h2>Niveau 5B</h2>
<p>Le module fait partie d’un ensemble interconnecté. Il reçoit les paramètres selon son n° ou son nom de module. Tous sont enregistrés dans une DB centrale. Des logs centralisés sont consultables, ainsi que l’état du réseau. Des informations historiques peuvent être consultées.</p>
<h2>Conclusion</h2>
<p>Il n’y en n’a pas. La complexité élevée demande des compétences de programmation élargies et fait appel à des techniques qu’il faut dominer et mettre en œuvre. Elle demande plus de puissance, de la connectivité ; mais amène de la souplesse à l’utilisateur. Et son lot d’erreurs, de possibilités d’intrusion. Il s’agit de choisir le niveau d’abstraction et de réglage… avec du bon sens.</p>
<p>Yves Masur (8/2018)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
