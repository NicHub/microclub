---
title: "Le projet 2019 est lancé"
date: "2019-01-26T11:18:24"
lastmod: "2019-02-12T11:30:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: []
url: "/2019/01/26/le-projet-2019-est-lance/"
wordpress_id: 4195
comment_count: 8
---
<p>Robot/Crabe, Araignée, lampe de chevet magique ? projets à décider….</p>
<p>Nous venons de passer une soirée à voir ce que nous pouvons utiliser  dans notre projet 2019 et ce que nous voudrions y intégrer. Nous  retenons:</p>
<ul><li>Module ESP32 36 pattes</li><li>Régulateur à découpage 5V 3A</li><li>Ponts en H type DRV 8825 (une majorité désirant utiliser des moteurs pas à pas NEMA17</li><li>Connecteur pour sous-module pour servos PCA9685</li><li>Connecteur Neopixel</li><li>Connecteur pour module Audio</li><li>Connecteur Gyro MPU9250 + Baro BMP280</li><li>Pins du module ESP32 pour faciliter le déverminage</li><li>Connecteur I2C, SPI et UART Grove et 1 Wire sur platine principale</li><li>Connecteur pour 2nd circuit optionnel tels que Module Relais/230V ou Veroboard ou combiné</li><li>Fonction RTC</li><li>Connecteur pour fonction touch (touches capacitives)</li><li>Évaluer une possibilité de mettre la carte en mode low-power</li></ul>
<p><strong>A quoi notre circuit pourrait ressembler </strong>?? voici un premier brouillon</p>
<p>avec Module ESP32 (centre) Alim (M1) Ponts en H (StrepDRV1+2( des capteur de distance (à intégrer côté processeur), divers connecteurs I2C (2 Grove)  Affichage OLED (LCD1) connecteur Carte SD (Bas gauche) + 5 neopixels sur les 4 coins et au centre, un trou au centre pour Nicolas, 2 modules ADC/I2C pour les capteurs IR, Gyro (M1). !!!! ceci n’est qu’une ébauche de projet = brouillon2! Présentation du 25.1.2018 <a href="/media/2019/01/Project-2019.pdf">lien</a></p>
<p>Alternative en 2 parties</p>
<p><br/></p>
<figure><img alt="" height="439" src="/media/2019/02/MicroRobot_2019_proto1.1g-1-1024x683.png" width="659"/><figcaption> Circuit vue de dessus, Dessiné sur Eagle 9.3.0 </figcaption></figure>
<figure><img alt="" height="823" src="/media/2019/02/power-topG2-1-1024x823.jpg" width="1024"/><figcaption> Et voici le circuit sous Fusion 360 (mise à jour 8.2.2019), presque prêt  pour une présentation/discussion au Microclub et fabrication </figcaption></figure>
<p>Alternative en 2 parties</p>
<figure><img alt="" height="683" src="/media/2019/02/MicroRobot_2019_proto1.1g_split65-1-1024x683.png" width="1024"/><figcaption><br/>Alternative, circuit en 2 parties, circuit moteurs séparé:<br/>Moins de capteurs IR, Capteurs time of flight à l’avant et à l’arrière<br/><br/>Circuit RTC + IO digital 8 lignes</figcaption></figure>

## Commentaires

### Yves Masur — 27 janvier 2019 à 22:27

<section class="comment-content comment">
<p>Excellent!! Pour la RTC, ne faut-il pas prévoir une pile?</p>
 </section>

### Rolf Ziegler Auteur de l’article — 26 février 2019 à 13:28

<section class="comment-content comment">
<p>Un sockle 2 pins est disponible sous le module CPU ou l’on peut également cacher la pile. Malheureusement il n’y avait pas de place pour un sockle dédié.</p>
 </section>

### Charles-Jimmy Geissler — 28 février 2019 à 16:46

<section class="comment-content comment">
<p>Bravo Rolf pour ton magnifique PCB<br/>
Je suggérerais en plus un petit commutateur 10 pôles pour enregistrer les programmes.<br/>
Attention, j’ai acheté un  » ESP32-WROOM-32 ESPRESSIF  » en ayant eu que des problèmes de chargement du programme Wifi Scan ou autres. Après des heures de test, je me suis rendu compte qu’il fallait presser le bouton Boot durant tout le chargement du programme et maintenant ça marche. Mais par la suite il faudra y inclure un condensateur sur la pin « EN » et le processeur, c’est une question de timing.</p>
 </section>

### ↳ Réponse — Rolf Ziegler Auteur de l’article — 28 février 2019 à 18:28

<section class="comment-content comment">
<p>Merci Jimmy,<br/>
J’ai effectivement évaluer un commutateur 8/16 positions pour changer de programmes.<br/>
Mais par manque de place, il n’y pas fini sur notre PCB.<br/>
Par contre vu que toutes les pins du processeur sont atteignable, un peut facilement en ajouter un et sacrifier une ou l’autre des fonctionnalités.<br/>
Pour le problème de flash, nous avons constaté que cela pouvait être lié au driver USB si on est sous WIN7.<br/>
Problème qui ne semble pas apparaitre sous WIN10.<br/>
A suivre.<br/>
RZ</p>
 </section>

### Rolf Ziegler Auteur de l’article — 28 février 2019 à 19:07

<section class="comment-content comment">
<p>Ah concernant le commutateur, 10 pins voulait probablement dire 10 positions.<br/>
En fait nous avons une fonction TOUCH sur l’ESP32 et on peut programmer un commutateur avec 2 touches et le display OLED, Menu Rotatif pour 1 touche et Select pour la 2ème touche.<br/>
Joli exercice !</p>
 </section>

### Rolf Ziegler Auteur de l’article — 28 février 2019 à 19:31

<section class="comment-content comment">
<p>Il faut continuer cette discussion dans le forum !!!!</p>
 </section>

### Tornare — 9 mars 2019 à 19:31

<section class="comment-content comment">
<p>Il serait fort utile d’avoir une liste de référence des différents modules prévu dans le schéma.<br/>
Il y a tellement de variantes pour les ESP, Ponts en H, Gyro et convertisseur AD que sans références on va se planter !<br/>
Merci d’avance.</p>
 </section>

### ↳ Réponse — Rolf Ziegler Auteur de l’article — 10 mars 2019 à 13:12

<section class="comment-content comment">
<p>Les composants choisis sont listé sur la page principale de notre GitHub <a href="https://github.com/microclub-ch/P19-projets-microclub-2019" rel="nofollow ugc">https://github.com/microclub-ch/P19-projets-microclub-2019</a>, pour la suite visitez notre forum ou je vais ajouter les détails des compsants.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
