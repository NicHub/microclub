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
MPY-Jama est un IDE simplifié qui ressemble beaucoup à l’environnement Arduino. Ce qui est pratique, ce sont les divers outils qui sont directement disponibles :

- Configurateur de réseau wifi en mode AP
- Configurateur de réseau wifi local
- Affichage des IO en couleur, rouge=0, vert=1
- RAM utilisée
- Température interne du processeur
- Terminal REPL
- Editeur de code avec coloration syntaxique, mais sans auto complétion !
- Un gestionnaire de fichier très pratique

[![](/media/2023/02/MPY1.png)](/media/2023/02/MPY1.png)

L’environnement est soigné, le graphisme agréable.

D’autres IDE, comme Thonny et Mu, ont déjà ces fonctionnalités de base. Toutefois, ESP32 MPY-Jama se différencie grâce à une suite d’outils appelée Jama Funcs. Ces fonctions prédéfinies vous aident à configurer votre appareil. De plus, les outils de connexion Wi-Fi facilitent la recherche des réseaux disponibles.

[![](/media/2023/02/MPY2.png)](/media/2023/02/MPY2.png)

L’interface graphique comporte un widget dans le coin inférieur gauche qui affiche l’utilisation de la RAM, le capteur de température et la durée de fonctionnement de la carte.

[![](/media/2023/02/MPY3.png)](/media/2023/02/MPY3.png)

La section Informations système fournit des détails supplémentaires qui vous évitent d’avoir à taper des commandes sur le REPL pour voir quelle version de code se trouve sur l’appareil. En outre, il donne une lecture en temps réel de l’état de la broche GPIO.

[![](/media/2023/02/MPY5.png)](/media/2023/02/MPY5.png)

Vous pouvez le [télécharger sur github depuis ce lien](https://github.com/jczic/ESP32-MPY-Jama)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
