---
title: "MPY-jama"
date: "2023-02-18T15:25:53"
lastmod: "2023-02-18T15:30:00"
author: "franic"
categories: ["Articles"]
tags: ["hardware", "programmation"]
url: "/2023/02/18/mpy-jama/"
wordpress_id: 5099
comment_count: 0
---
<p>MPY-Jama est un IDE simplifié qui ressemble beaucoup à l’environnement Arduino. Ce qui est pratique, ce sont les divers outils qui sont directement disponibles :</p>
<ul>
<li>Configurateur de réseau wifi en mode AP</li>
<li>Configurateur de réseau wifi local</li>
<li>Affichage des IO en couleur, rouge=0, vert=1</li>
<li>RAM utilisée</li>
<li>Température interne du processeur</li>
<li>Terminal REPL</li>
<li>Editeur de code avec coloration syntaxique, mais sans auto complétion !</li>
<li>Un gestionnaire de fichier très pratique</li>
</ul>
<p><a href="/media/2023/02/MPY1.png"><img alt="" height="673" src="/media/2023/02/MPY1.png" width="986"/></a></p>
<p>L’environnement est soigné, le graphisme agréable.</p>
<p>D’autres IDE, comme Thonny et Mu, ont déjà ces fonctionnalités de base. Toutefois, ESP32 MPY-Jama se différencie grâce à une suite d’outils appelée Jama Funcs. Ces fonctions prédéfinies vous aident à configurer votre appareil. De plus, les outils de connexion Wi-Fi facilitent la recherche des réseaux disponibles.</p>
<p><a href="/media/2023/02/MPY2.png"><img alt="" height="641" src="/media/2023/02/MPY2.png" width="984"/></a></p>
<p>L’interface graphique comporte un widget dans le coin inférieur gauche qui affiche l’utilisation de la RAM, le capteur de température et la durée de fonctionnement de la carte.</p>
<p><a href="/media/2023/02/MPY3.png"><img alt="" height="260" src="/media/2023/02/MPY3.png" width="303"/></a></p>
<p>La section Informations système fournit des détails supplémentaires qui vous évitent d’avoir à taper des commandes sur le REPL pour voir quelle version de code se trouve sur l’appareil. En outre, il donne une lecture en temps réel de l’état de la broche GPIO.</p>
<p><a href="/media/2023/02/MPY5.png"><img alt="" height="641" src="/media/2023/02/MPY5.png" width="984"/></a></p>
<p>Vous pouvez le <a href="https://github.com/jczic/ESP32-MPY-Jama">télécharger sur github depuis ce lien</a></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
