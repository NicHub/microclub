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
<p><img height="585" src="/media/2025/05/word-image-5577-1.png" width="585"/></p>
<p>Le Raspberry Pi Pico est une carte à microcontrôleur développée par la fondation Raspberry Pi et lancée en janvier 2021. Contrairement aux autres modèles Raspberry Pi, qui sont de véritables nano-ordinateurs, le Pico est conçu pour des applications embarquées et l’apprentissage de la programmation électronique.</p>
<p><strong>Caractéristiques principales :</strong></p>
<p><strong>Microcontrôleur</strong> : RP2040, conçu par Raspberry Pi, avec deux cœurs ARM Cortex-M0+ cadencés à 133 MHz</p>
<p><strong>Capteur de température intégré…</strong></p>
<p><strong>Mémoire vive</strong> (SRAM) : 264 Ko</p>
<p>Stockage : 2 Mo de mémoire flash externe pour les programmes et les données</p>
<p><strong>Connectique</strong> :</p>
<p>26 broches GPIO multifonctions (entrées/sorties numériques et analogiques)</p>
<p>3 entrées analogiques (ADC)</p>
<p>2 ports UART, 2 ports I2C, 2 ports SPI, 16 canaux PWM</p>
<p>Port micro-USB pour l’alimentation et la programmation</p>
<p><strong>Dimensions</strong> : 21 mm x 51 mm</p>
<p><strong>Alimentation</strong> : Fonctionne entre 1,8 et 5,5 V DC</p>
<p><strong>Led embarquée</strong> : Sur la broche GPIO 25, idéale pour les premiers tests</p>
<p><strong>Versions disponibles</strong> :</p>
<p><img height="209" src="/media/2025/05/word-image-5577-2.jpeg" width="722"/></p>
<p><strong>Programmation</strong></p>
<p>Le Pico se programme principalement en MicroPython, Python, C ou C++. L’IDE Thonny est recommandé pour débuter, mais il est aussi possible d’utiliser Visual Studio Code ou d’autres outils. Le port micro-USB permet de transférer facilement les programmes sur la carte, et le Pico peut également émuler un périphérique USB (clavier, souris, etc.).</p>
<p><strong>Le Raspberry Pi Pico est utilisé dans de nombreux domaines :</strong></p>
<p><strong>Education : </strong>Apprentissage de la programmation et de l’électronique, projets scolaires, ateliers de robotique et ateliers Microclub.</p>
<p><strong>Prototypage</strong> : Idéal pour tester des idées rapidement grâce à ses GPIO et sa simplicité d’utilisation.</p>
<p><strong>Automatisation </strong>: Contrôle de petits robots, domotique, surveillance environnementale, objets connectés (IoT).</p>
<p><strong>Projets ludiques</strong> : Création de jeux, claviers personnalisés, capteurs de température, arrosage automatique de plantes, etc.</p>
<p><strong>Exemples de projets simples</strong> :</p>
<p>Allumer et éteindre une LED (projet « blink »).</p>
<p>Mesurer la température avec le capteur intégré.</p>
<p>Créer un clavier ou une manette USB personnalisée.</p>
<p>Automatiser l’arrosage d’une plante avec un capteur d’humidité.</p>
<p>Construire un robot simple ou une station météo miniature.</p>
<p><strong>Différences avec les autres Raspberry Pi</strong></p>
<p>Contrairement aux modèles classiques (Raspberry Pi 4, Zero, etc.), le Pico ne fait pas tourner de système d’exploitation comme Linux, n’a pas de sortie HDMI ni de connectivité réseau native (sauf version W), et se rapproche davantage des cartes Arduino ou micro:bit.</p>
<p><strong>Première conclusion</strong> :</p>
<p>Le Raspberry Pi Pico est un microcontrôleur polyvalent, abordable (environ 5 €), parfait pour l’initiation à la programmation embarquée, la réalisation de projets électroniques et l’automatisation de tâches simples. Sa communauté active et sa documentation abondante en font un excellent choix pour débuter ou expérimenter dans le domaine de l’électronique.</p>
<p><strong>Quels sont les avantages du microcontrôleur RP2040 ?</strong></p>
<p><strong>Faible coût et accessibilité</strong></p>
<p>Le RP2040 est reconnu pour son prix très bas, ce qui le rend accessible à un large public, des amateurs aux professionnels.</p>
<p><strong>Bonnes performances</strong></p>
<p>Il embarque un processeur double cœur ARM Cortex-M0+ cadencé jusqu’à 133 MHz, offrant de bonnes capacités de calcul pour un microcontrôleur de cette gamme. Ses performances sont particulièrement élevées pour les traitements impliquant des entiers.</p>
<p><strong>Grande capacité mémoire</strong></p>
<p>Il dispose de 264 Ko de SRAM, ce qui est bien supérieur à de nombreux concurrents dans la même gamme de prix (par exemple, un Arduino Uno n’a que 32 Ko).</p>
<p>Il peut supporter jusqu’à 16 Mo de mémoire flash externe via un bus QSPI dédié, permettant d’étendre facilement la capacité de stockage.</p>
<p><strong>Richesse des interfaces d’entrées/sorties</strong></p>
<p>Il propose jusqu’à 30 broches GPIO multifonctions, dont plusieurs peuvent être utilisées pour des interfaces série (UART, SPI, I2C), PWM, ADC et PIO (Programmable I/O).</p>
<p>Les machines d’état PIO permettent de créer des périphériques personnalisés ou de gérer des protocoles non pris en charge nativement.</p>
<p><strong>Flexibilité et facilité d’intégration</strong></p>
<p>Son format compact (7 x 7 mm pour la puce seule) et sa large plage d’alimentation (1,8 à 5,5 V) facilitent son intégration dans de nombreux projets.</p>
<p>Il est facile à programmer, notamment grâce à la possibilité de le flasher par simple glisser-déposer via USB.</p>
<p><strong>Polyvalence d’utilisation</strong></p>
<p>Il convient aussi bien à l’éducation, au prototypage rapide qu’à la production industrielle, grâce à sa disponibilité en tant que composant seul ou intégré sur des cartes comme le Raspberry Pi Pico.</p>
<p><strong>Communauté et documentation</strong></p>
<p>Bénéficie d’une communauté active et d’une documentation très complète, facilitant la prise en main et le développement de projets.</p>
<p>En résumé, le RP2040 combine faible coût, bonnes performances, grande flexibilité d’utilisation et richesse des interfaces, ce qui en fait un microcontrôleur particulièrement attractif pour de nombreux usages.</p>
<p><strong>Quelles sont les différences entre le Raspberry Pi Pico et une carte Arduino</strong></p>
<p><img height="573" src="/media/2025/05/word-image-5577-3.jpeg" width="683"/></p>
<p><strong>Points clés de différenciation</strong></p>
<p><strong>Puissance de calcul : </strong>Le Pico est beaucoup plus puissant grâce à son processeur double cœur 32 bits, contre un simple cœur 8 bits pour la plupart des Arduino classiques.</p>
<p><strong>Mémoire : </strong>Le Pico dispose de beaucoup plus de mémoire vive et de stockage, ce qui permet des projets plus complexes</p>
<p><strong>Programmation</strong> : Le Pico peut être programmé en MicroPython, ce qui facilite l’apprentissage pour les débutants, alors que l’Arduino utilise principalement le C/C++.</p>
<p><strong>E/S programmables (PIO)</strong> : Le Pico possède un sous-système PIO qui permet de créer des interfaces personnalisées, ce que ne permet pas l’Arduino.</p>
<p><strong>Convertisseur analogique</strong> : Le Pico propose un ADC 12 bits, plus précis que l’ADC 10 bits de l’Arduino Uno.</p>
<p><strong>En résumé</strong></p>
<p>Le Raspberry Pi Pico est plus puissant, plus flexible et plus moderne, idéal pour des projets avancés ou nécessitant plus de ressources.</p>
<p>Une carte Arduino classique est plus simple à prendre en main pour les débutants, très bien documentée, et parfaitement adaptée aux petits projets de contrôle ou d’automatisation simples.</p>
<p><strong>Comment la programmation en Python sur le Raspberry Pi Pico se compare-t-elle à celle en C/C++ sur l’Arduino ?</strong></p>
<p><strong>Comparaison de la programmation en Python sur Raspberry Pi Pico et en C/C++ sur Arduino</strong></p>
<p><strong>Points clés</strong></p>
<p><strong>Simplicité et rapidité</strong> : Programmer le Raspberry Pi Pico en Python (MicroPython) est beaucoup plus simple et rapide à prendre en main, surtout pour les débutants. Il suffit de brancher la carte, flasher MicroPython et écrire du code dans Thonny ou une console interactive.</p>
<p><strong>Programmation interactive</strong> : MicroPython permet d’exécuter des commandes en temps réel via le REPL, ce qui facilite les tests et le débogage.</p>
<p><strong>Performance</strong> : Le C/C++ sur Arduino offre de meilleures performances et une gestion plus fine des ressources matérielles, ce qui est crucial pour des applications temps réel ou nécessitant une grande rapidité.</p>
<p><strong>Écosystème et bibliothèques : </strong>Arduino dispose d’une immense bibliothèque de ressources et d’exemples, tandis que MicroPython en propose moins, mais reste très adapté pour la plupart des projets courants.</p>
<p><strong><img height="548" src="/media/2025/05/word-image-5577-4.png" width="690"/></strong></p>
<p><strong>Installation</strong> : La mise en place d’un environnement Python pour le Pico est plus rapide et intuitive, alors que le C/C++ demande plus de configuration, notamment pour le SDK natif.</p>
<p><strong>Transfert de compétences</strong> : Apprendre le C/C++ sur Arduino facilite l’adaptation à d’autres microcontrôleurs (ESP32, STM32, etc.), tandis que Python est plus universel pour l’apprentissage général de la programmation.</p>
<p><strong>Finalement </strong>:</p>
<p><strong>Python/MicroPython sur Pico</strong> : idéal pour débuter, prototyper rapidement, ou pour des projets éducatifs et interactifs.</p>
<p><strong>C/C++ sur Arduino</strong> : préférable pour des projets nécessitant performance, optimisation, ou compatibilité avec un vaste écosystème matériel et logiciel.</p>
<p>Le choix dépend donc du niveau de l’utilisateur, du type de projet et des besoins en performance ou en simplicité</p>
<p><strong><img height="635" src="/media/2025/05/word-image-5577-5.png" width="636"/></strong></p>
<p><strong>Jean-Pierre Broillet, Microclub, mai 2025</strong></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
