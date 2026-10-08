---
title: "Préparation d’Arduino pour l’atelier IA avec la camera XIAO ESP32S3 Sense"
date: "2025-04-05T15:51:53"
lastmod: "2025-04-11T18:19:21"
author: "franic"
categories: ["Microclub"]
tags: []
url: "/2025/04/05/preparation-darduino-pour-latelier-ia-avec-la-camera-xiao-esp32s3-sense/"
wordpress_id: 5509
comment_count: 1
---
<p>Pour commencer rendez-vous sur le site arduino et téléchargez la dernière version de l’IDE <a href="https://www.arduino.cc/en/software">https://www.arduino.cc/en/software</a> actuellement c’est la version IDE 2.3.5.</p>
<h2>1 Installation d’Arduino</h2>
<p>Pour commencer rendez-vous sur le site arduino et téléchargez la dernière version de l’IDE <a href="https://www.arduino.cc/en/software">https://www.arduino.cc/en/software</a> actuellement c’est la version IDE 2.3.5.</p>
<p>Une fois le fichier téléchargé, vous pouvez l’installer</p>
<h2>2 Configuration d’Arduino</h2>
<p>Il faut maintenant configurer l’environnement pour la compilation de l’ESP32</p>
<p> Allez donc sous fichier à préférences</p>
<figure><a href="/media/2025/04/image.png"><img alt="" height="428" src="/media/2025/04/image.png" width="258"/></a></figure>
<p>Cette fenêtre va apparaître. Sous Additional board management URL, il faut ajouter le lien suivant, puis sauver les changements :</p>
<p>Cette fenêtre va apparaître. Sous Additional board management URL, il faut ajouter le lien suivant, puis sauver les changements :</p>
<p>https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json</p>
<p>Ensuite il faut cliquer sur Tools  Board  et Board Manager :</p>
<p>Il faut installer la version 2.0.17 de Espressif, j’ai rencontré beaucoup de problèmes avec la version 3.x.x. Pourtant Arduino vous proposera de faire un update …</p>
<figure><a href="/media/2025/04/image-2.png"><img alt="" height="329" src="/media/2025/04/image-2.png" width="534"/></a></figure>
<p>Ensuite il faut cliquer sur Tools à Board à et Board Manager :</p>
<figure><a href="/media/2025/04/image-1.png"><img alt="" height="266" src="/media/2025/04/image-1.png" width="605"/></a></figure>
<p>Il faut installer la version <strong>2.0.17</strong> de Espressif, j’ai rencontré beaucoup de problèmes avec la version 3.x.x. Pourtant Arduino vous proposera de faire un update …</p>
<figure><a href="/media/2025/04/image-3.png"><img alt="" height="842" src="/media/2025/04/image-3.png" width="501"/></a></figure>
<p></p>
<h2>3 Divers liens</h2>
<p>Voici quelques liens vers le fabricant Seeed :</p>
<ul>
<li><a href="https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/">https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/</a></li>
<li><a href="https://wiki.seeedstudio.com/xiao_esp32s3_camera_usage/">https://wiki.seeedstudio.com/xiao_esp32s3_camera_usage/#preliminary-preparation</a></li>
<li><a href="https://github.com/limengdu/SeeedStudio-XIAO-ESP32S3-Sense-camera/tree/main">https://github.com/limengdu/SeeedStudio-XIAO-ESP32S3-Sense-camera/tree/main</a></li>
</ul>
<p></p>
<h2>4 Edge impulse</h2>
<p>Afin de pouvoir entraîner votre prochain projet, il faut que vous vous inscrire auprès de Edge impulse :</p>
<p><a href="https://edgeimpulse.com">https://edgeimpulse.com</a></p>
<figure><a href="/media/2025/04/image-5.png"><img alt="" height="103" src="/media/2025/04/image-5.png" width="373"/></a></figure>
<p>5 Projet de test qui prend une photo toutes les 2 secondes : <a href="/media/2025/04/take_photos.zip">takePhotos.zip</a></p>
<p>6 Projet complet de détection de canettes et bouteilles : <img alt="" src="/media/2025/04/ei-canette2-arduino-1.0.4.zip"/><code><a href="/media/2025/04/ei-canette2-arduino-1.0.4.zip">canette2</a></code> ou sur edge <a href="https://studio.edgeimpulse.com/public/669697/live">https://studio.edgeimpulse.com/public/669697/live</a></p>
<p>7 Configuration de la caméra : <a href="/media/2025/04/ConfigXIAOcam.txt">config.txt</a></p>
<p><img alt="" src="/media/2025/04/take_photos.zip"/></p>
<p></p>

## Commentaires

### Nicolas Jeanmonod — 6 mars 2026 à 14:05

<section class="comment-content comment">
<p>Merci pour ce tuto Laurent !</p>
<p>J’ai migré sur PlatformIO l’exemple de serveur caméra pour XIAO ESP32-S3 Sense.</p>
<p>C’est beaucoup plus simple à flasher qu’avec l’IDE Arduino.</p>
<p><a href="https://github.com/NicHub/xiao-esp32s3-camera-webserver.git" rel="nofollow ugc">https://github.com/NicHub/xiao-esp32s3-camera-webserver.git</a></p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
