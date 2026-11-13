---
title: "PlatformIO 5.0.1: Gestion des librairies"
date: "2020-10-04T15:35:24"
lastmod: "2020-10-04T15:35:26"
author: "franic"
categories: ["Ateliers"]
tags: ["arduino", "esp32", "esp8266", "platformio"]
url: "/2020/10/04/platformio-5-0-1-gestion-des-librairies/"
wordpress_id: 4831
comment_count: 1
---
<p>Un nouveau mode d’utilisation des librairies a été mis en place dans la version 5.0.1 de PlatformIO.</p>
<p>Lorsque vous développez un projet et que vous avez besoin d’une librairie, vous pouvez procéder de la manière suivante :</p>
<p>Allez dans le menu principale et sélectionner l’onglet verticale Librairies</p>
<figure><img alt="" height="504" src="/media/2020/10/PFIO_L1.png" width="631"/></figure>
<p>Puis recherchez votre librairie, par exemple horloge DS3231</p>
<figure><img alt="" height="460" src="/media/2020/10/PFIO_L2-1024x460.png" width="1024"/></figure>
<p>Une fois que vous avez trouvé la librairie qui vous intéresse, cliquez dessus et vous y verrez ces caractéristiques :</p>
<p>la version actuelle, des exemples … Si elle vous convient, ne cliquez pas sur le bouton Add to Project, mais cliquez sur l’onglet « installation » ainsi vous pourrez sélectionner exactement le type d’installation que vous désirez faire.</p>
<figure><img alt="" height="404" src="/media/2020/10/PFIO_L3-1024x404.png" width="1024"/></figure>
<p>Cliquez sur l’onglet « installation » et vous obtiendrez ces informations :</p>
<figure><img alt="" height="656" src="/media/2020/10/PFIO_L4.png" width="929"/></figure>
<p>On vous propose 3 modes d’installation de la librairie :</p>
<ol><li>&lt;nom de librairie&gt; @ <strong>^</strong>X.Y.Z : l’accent circonflexe indique qu’à chaque compilation, PlatformIO mettra à jour la librairie si une nouvelle version est disponible.</li><li>&lt;nom de librairie&gt; @ <strong>~</strong>X.Y.Z : le « tilse » indique qu’à chaque compilation, PlatformIO mettra à jour la librairie pour autant que les version majeur et mineur sont identiques, seul un correctif est disponible. Exemple version ~1.2.5 il faut qu’uniquement 5 soit supérieur pour que la mise à jour soit faite, mais le 1.2 doit rester.</li><li>&lt;nom de librairie&gt; @ X.Y.Z : La version indiquée est forcée, il n’y aura pas de mise à jour.</li></ol>
<p>Allez ensuite dans le fichier platformio.ini et coller ce lien après la balise Lib_deps comme l’exemple ci-dessous :</p>
<figure><img alt="" height="332" src="/media/2020/10/PFIO_L5.png" width="920"/></figure>
<p>Lors de la première compilation, les libraires seront téléchargées dans votre projet.</p>
<p>Je préfère ce mode d’utilisation à d’autres qui installent la librairie sur votre PC dans une répertoire commun à tous vos projets. Lorsque vous distribuez votre projet à un autre développeur, les librairies se téléchargeront si nécessaires et tout est propre.</p>

## Commentaires

### Yves Masur — 2 novembre 2020 à 07:25

<section class="comment-content comment">
<p>Décidément, la fourmi PFIO est un environnement difficile à utiliser… Pour ma part, je procède ainsi: les bibliothèques sont copiées dans le répertoire « projet\lib » du projet (remplacez le « projet » par son nom).<br/>
Ensuite j’édite le fichier « projet\platformio.ini « , avec les lib utilisées. Par exemple:<br/>
framework = arduino<br/>
; multi-line definition<br/>
lib_deps =<br/>
  jm_LCM2004A_I2C<br/>
  jm_PCF8574<br/>
  jm_Scheduler<br/>
  OneWire<br/>
; end of lib dependence</p>
<p>Ainsi, les lib sont complètement maitrisée, indépendamment des mises à jour qui surviennent (trop?) rapidement.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
