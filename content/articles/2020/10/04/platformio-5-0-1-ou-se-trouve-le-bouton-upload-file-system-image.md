---
title: "PlatformIO 5.0.1 : Où se trouve le bouton « Upload File System Image » ?"
date: "2020-10-04T15:45:07"
lastmod: "2020-10-27T21:29:10"
author: "franic"
categories: ["Microclub"]
tags: ["esp32", "esp8266", "platformio"]
url: "/2020/10/04/platformio-5-0-1-ou-se-trouve-le-bouton-upload-file-system-image/"
wordpress_id: 4838
comment_count: 1
---
<p>Dans l’ancienne version il y avait un bouton qui permettait de télécharger dans un ESP8266 ou ESP32 les fichiers web contenus dans le répertoire /data du projet.</p>
<p>Or dans la nouvelle version, ce bouton a été « oublié » !!!</p>
<p>Pour ce faire il suffit d’ouvrir un terminal et d’y taper manuellement la commande suivante : pio run -t uploadfs</p>
<figure><img alt="" height="164" src="/media/2020/10/PFIO_L6.png" width="783"/></figure>
<p>Si, comme moi, vos fichiers ne fonctionnent pas du premier coup, vous devrez procéder à plusieurs mises à jours.</p>
<p>Il n’est pas nécessaire de retaper cette commande, il suffit simplement d’ouvrir le terminal et d’appuyer sur la flèche du haut, la commande mémorisée réapparaitra !</p>
<p><strong>Depuis une dernière mise à jour, nous avons retrouvé le bouton !!!</strong></p>
<p>Il suffit de sélectionner votre projet puis d’appuyer sur le bouton Plateformio du ruban de gauche. </p>
<p>Ensuite suivez les étapes suivantes :</p>
<p><img alt="" height="423" src="/media/2020/10/PFIO_fileSys.png" width="350"/></p>
<p>1 sélectionnez  le dossier env:esp12e</p>
<p>2 déroulez le menu Platform</p>
<p>3 sélectionner enfin le bouton Upload Filesystem image</p>

## Commentaires

### Yves Masur — 8 juin 2021 à 14:30

<section class="comment-content comment">
<p>Pas si simple. En effet, chaque tâche utilise le port COM pour charger. Pour que ça fonctionne, il faut s’assurer que toutes les tâches qui y ont eu accès soient éteinte. Le plus simple est de les fermer par l’icone « poubelle »</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
