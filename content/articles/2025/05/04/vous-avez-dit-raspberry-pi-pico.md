---
title: "Vous avez dit Raspberry Pi ? Pico ?"
date: "2025-05-04T16:35:28"
lastmod: "2025-05-04T16:35:29"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2025/05/04/vous-avez-dit-raspberry-pi-pico/"
wordpress_id: 5577
comment_count: 0
---
![](/media/2025/05/word-image-5577-1.png)

Le Raspberry Pi Pico est une carte à microcontrôleur développée par la fondation Raspberry Pi et lancée en janvier 2021. Contrairement aux autres modèles Raspberry Pi, qui sont de véritables nano-ordinateurs, le Pico est conçu pour des applications embarquées et l’apprentissage de la programmation électronique.

**Caractéristiques principales :**

**Microcontrôleur** : RP2040, conçu par Raspberry Pi, avec deux cœurs ARM Cortex-M0+ cadencés à 133 MHz

**Capteur de température intégré…**

**Mémoire vive** (SRAM) : 264 Ko

Stockage : 2 Mo de mémoire flash externe pour les programmes et les données

**Connectique** :

26 broches GPIO multifonctions (entrées/sorties numériques et analogiques)

3 entrées analogiques (ADC)

2 ports UART, 2 ports I2C, 2 ports SPI, 16 canaux PWM

Port micro-USB pour l’alimentation et la programmation

**Dimensions** : 21 mm x 51 mm

**Alimentation** : Fonctionne entre 1,8 et 5,5 V DC

**Led embarquée** : Sur la broche GPIO 25, idéale pour les premiers tests

**Versions disponibles** :

![](/media/2025/05/word-image-5577-2.jpeg)

**Programmation**

Le Pico se programme principalement en MicroPython, Python, C ou C++. L’IDE Thonny est recommandé pour débuter, mais il est aussi possible d’utiliser Visual Studio Code ou d’autres outils. Le port micro-USB permet de transférer facilement les programmes sur la carte, et le Pico peut également émuler un périphérique USB (clavier, souris, etc.).

**Le Raspberry Pi Pico est utilisé dans de nombreux domaines :**

**Education :** Apprentissage de la programmation et de l’électronique, projets scolaires, ateliers de robotique et ateliers Microclub.

**Prototypage** : Idéal pour tester des idées rapidement grâce à ses GPIO et sa simplicité d’utilisation.

**Automatisation**: Contrôle de petits robots, domotique, surveillance environnementale, objets connectés (IoT).

**Projets ludiques** : Création de jeux, claviers personnalisés, capteurs de température, arrosage automatique de plantes, etc.

**Exemples de projets simples** :

Allumer et éteindre une LED (projet « blink »).

Mesurer la température avec le capteur intégré.

Créer un clavier ou une manette USB personnalisée.

Automatiser l’arrosage d’une plante avec un capteur d’humidité.

Construire un robot simple ou une station météo miniature.

**Différences avec les autres Raspberry Pi**

Contrairement aux modèles classiques (Raspberry Pi 4, Zero, etc.), le Pico ne fait pas tourner de système d’exploitation comme Linux, n’a pas de sortie HDMI ni de connectivité réseau native (sauf version W), et se rapproche davantage des cartes Arduino ou micro:bit.

**Première conclusion** :

Le Raspberry Pi Pico est un microcontrôleur polyvalent, abordable (environ 5 €), parfait pour l’initiation à la programmation embarquée, la réalisation de projets électroniques et l’automatisation de tâches simples. Sa communauté active et sa documentation abondante en font un excellent choix pour débuter ou expérimenter dans le domaine de l’électronique.

**Quels sont les avantages du microcontrôleur RP2040 ?**

**Faible coût et accessibilité**

Le RP2040 est reconnu pour son prix très bas, ce qui le rend accessible à un large public, des amateurs aux professionnels.

**Bonnes performances**

Il embarque un processeur double cœur ARM Cortex-M0+ cadencé jusqu’à 133 MHz, offrant de bonnes capacités de calcul pour un microcontrôleur de cette gamme. Ses performances sont particulièrement élevées pour les traitements impliquant des entiers.

**Grande capacité mémoire**

Il dispose de 264 Ko de SRAM, ce qui est bien supérieur à de nombreux concurrents dans la même gamme de prix (par exemple, un Arduino Uno n’a que 32 Ko).

Il peut supporter jusqu’à 16 Mo de mémoire flash externe via un bus QSPI dédié, permettant d’étendre facilement la capacité de stockage.

**Richesse des interfaces d’entrées/sorties**

Il propose jusqu’à 30 broches GPIO multifonctions, dont plusieurs peuvent être utilisées pour des interfaces série (UART, SPI, I2C), PWM, ADC et PIO (Programmable I/O).

Les machines d’état PIO permettent de créer des périphériques personnalisés ou de gérer des protocoles non pris en charge nativement.

**Flexibilité et facilité d’intégration**

Son format compact (7 x 7 mm pour la puce seule) et sa large plage d’alimentation (1,8 à 5,5 V) facilitent son intégration dans de nombreux projets.

Il est facile à programmer, notamment grâce à la possibilité de le flasher par simple glisser-déposer via USB.

**Polyvalence d’utilisation**

Il convient aussi bien à l’éducation, au prototypage rapide qu’à la production industrielle, grâce à sa disponibilité en tant que composant seul ou intégré sur des cartes comme le Raspberry Pi Pico.

**Communauté et documentation**

Bénéficie d’une communauté active et d’une documentation très complète, facilitant la prise en main et le développement de projets.

En résumé, le RP2040 combine faible coût, bonnes performances, grande flexibilité d’utilisation et richesse des interfaces, ce qui en fait un microcontrôleur particulièrement attractif pour de nombreux usages.

**Quelles sont les différences entre le Raspberry Pi Pico et une carte Arduino**

![](/media/2025/05/word-image-5577-3.jpeg)

**Points clés de différenciation**

**Puissance de calcul :** Le Pico est beaucoup plus puissant grâce à son processeur double cœur 32 bits, contre un simple cœur 8 bits pour la plupart des Arduino classiques.

**Mémoire :** Le Pico dispose de beaucoup plus de mémoire vive et de stockage, ce qui permet des projets plus complexes

**Programmation** : Le Pico peut être programmé en MicroPython, ce qui facilite l’apprentissage pour les débutants, alors que l’Arduino utilise principalement le C/C++.

**E/S programmables (PIO)** : Le Pico possède un sous-système PIO qui permet de créer des interfaces personnalisées, ce que ne permet pas l’Arduino.

**Convertisseur analogique** : Le Pico propose un ADC 12 bits, plus précis que l’ADC 10 bits de l’Arduino Uno.

**En résumé**

Le Raspberry Pi Pico est plus puissant, plus flexible et plus moderne, idéal pour des projets avancés ou nécessitant plus de ressources.

Une carte Arduino classique est plus simple à prendre en main pour les débutants, très bien documentée, et parfaitement adaptée aux petits projets de contrôle ou d’automatisation simples.

**Comment la programmation en Python sur le Raspberry Pi Pico se compare-t-elle à celle en C/C++ sur l’Arduino ?**

**Comparaison de la programmation en Python sur Raspberry Pi Pico et en C/C++ sur Arduino**

**Points clés**

**Simplicité et rapidité** : Programmer le Raspberry Pi Pico en Python (MicroPython) est beaucoup plus simple et rapide à prendre en main, surtout pour les débutants. Il suffit de brancher la carte, flasher MicroPython et écrire du code dans Thonny ou une console interactive.

**Programmation interactive** : MicroPython permet d’exécuter des commandes en temps réel via le REPL, ce qui facilite les tests et le débogage.

**Performance** : Le C/C++ sur Arduino offre de meilleures performances et une gestion plus fine des ressources matérielles, ce qui est crucial pour des applications temps réel ou nécessitant une grande rapidité.

**Écosystème et bibliothèques :** Arduino dispose d’une immense bibliothèque de ressources et d’exemples, tandis que MicroPython en propose moins, mais reste très adapté pour la plupart des projets courants.

**![](/media/2025/05/word-image-5577-4.png)**

**Installation** : La mise en place d’un environnement Python pour le Pico est plus rapide et intuitive, alors que le C/C++ demande plus de configuration, notamment pour le SDK natif.

**Transfert de compétences** : Apprendre le C/C++ sur Arduino facilite l’adaptation à d’autres microcontrôleurs (ESP32, STM32, etc.), tandis que Python est plus universel pour l’apprentissage général de la programmation.

**Finalement**:

**Python/MicroPython sur Pico** : idéal pour débuter, prototyper rapidement, ou pour des projets éducatifs et interactifs.

**C/C++ sur Arduino** : préférable pour des projets nécessitant performance, optimisation, ou compatibilité avec un vaste écosystème matériel et logiciel.

Le choix dépend donc du niveau de l’utilisateur, du type de projet et des besoins en performance ou en simplicité

**![](/media/2025/05/word-image-5577-5.png)**

**Jean-Pierre Broillet, Microclub, mai 2025**

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
