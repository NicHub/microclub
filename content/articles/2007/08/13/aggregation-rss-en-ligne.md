---
title: "Aggrégation RSS en ligne"
date: "2007-08-13T18:13:07"
lastmod: "2015-04-24T23:20:24"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["mashup", "rss"]
url: "/2007/08/13/aggregation-rss-en-ligne/"
wordpress_id: 6
comment_count: 0
---
<p>Depuis quelques mois j’explore les possibilités du « <a href="http://fr.wikipedia.org/wiki/Web_2.0" target="_blank">Web 2.0</a>« , dont l’utilisation des <a href="http://www.projets.ch/goulu/?p=213">flux RSS</a> est l’élément le plus concret. Par exemple, mes blogs offrent chacun un flux auquel vous pouvez vous abonner, mais aussi :</p>
<ol>
<li>un bloc « Nouvelles Choisies » qui liste les articles qui m’ont intéressé sur les dizaines de flux auxquels je suis abonné.</li>
<li>un bloc « Goulu News » qui regroupe les articles publiés sur tous mes blogs en un seul fluy</li>
</ol>
<p>Voici comment ces flux sont générés.</p>
<p>Pour les « Nouvelles Choisies », c’est très simple :  utilisant <a href="/2007/05/10/flux-rss/">« Google Reader » pour lire mes flux</a>, il me suffit de cocher l’icône « Share » au bas de chaque article intéressant pour l’ajouter à <a href="http://www.google.com/reader/public/atom/user/07530539290389081456/state/com.google/broadcast" target="_blank">ce flux généré tout seul par Google</a>.</p>
<p>Pour les « Goulu News », il me fallait un système permettant d' »agréger » plusieurs flux automatiquement en un seul en ligne, sans intervention humaine.</p>
<p>La solution la plus simple a été d’utiliser Ziki.com : dans <a href="http://www.ziki.com/fr/people/goulu" target="_blank">mon profil Ziki</a>, j’ai pu définir tous mes blogs et leur flux RSS respectifs, et Ziki les combine pour moi <a href="http://www.ziki.com/fr/people/goulu/rss/10" target="_blank">en un seul</a>, que je peux ensuite réutiliser dans les différents blogs. Le seul ennui de cette solution est un retard de plusieurs heures, voire 1 jour entre la publication d’un nouveau billet et la mise à jour du flux aggrégé par Ziki.</p>
<p><a href="http://xfruits.com/" target="_blank"><img align="left" height="30" hspace="3" src="http://www.groupereflect.net/blog/images/xfruits-1.png" vspace="3" width="121"/>xFruits.com</a> est un service permettant non seulement d’agréger des flux en ligne, mais aussi de les convertir dans tous les sens à l’aide de « briques ». On peut par exemple générer des pages web pour téléphones mobiles à partir de flux RSS, ou convertir un flux en « podcast » à l’aide d’un service de voix synthétique. Les « xFruits » ainsi définis par chaque utilisateur peuvent être partagés et consultés par tout le monde. <a href="http://xfruits.com/goulu/" target="_blank">Les miens sont ici</a>.</p>
<p>La prochaine étape serait une véritable « langage de programmation » permettant de manipuler des flux RSS facilement, et en ligne si possible.</p>
<p><a href="http://pipes.yahoo.com/" target="_blank"><img align="right" height="45" hspace="5" src="http://pipes.yahoo.com/img/logo-lg.gif" vspace="5" width="119"/></a>C’est exactement ce que fait « <a href="http://pipes.yahoo.com" target="_blank">Yahoo Pipes</a>« , un outil aussi spectaculaire que facile à utiliser pour combiner, filter, trier des informations provenant de différentes sources via flux RSS (<a href="http://pipes.yahoo.com/pipes/person.info?eyuid=5S9f6qU0p3bLsNVYuvVJjec-" target="_blank">mes « pipes » sont ici</a>)</p>
<p><img align="left" height="172" hspace="3" src="http://www.dashes.com/anil/images/yahoo-pipes.gif" vspace="3" width="211"/></p>
<p>Dans Yahoo Pipes, on « programme » de manière graphique en câblant des opérations entre des entrées , généralement des flux RSS (en haut) et une sortie, un nouveau flux RSS (en bas). Des opérations intermédiaires permettent de trier les flux, de les filtrer en enlevant certains articles, ou d’effectuer des recherches</p>
<p align="center"><img height="250" hspace="5" src="http://www.dashes.com/anil/images/yahoo-pipes-ide.png" vspace="5" width="360"/></p>
<p align="left">on peut ainsi créer de véritable « mashups » en combinant les fonctionnalités de sites web 2.0, et les mettre à disposition de tout le monde. En explorant les « <a href="http://pipes.yahoo.com/pipes/pipes.popular" target="_blank">pipes les plus populaires</a> » on trouve par exemple:</p>
<ul>
<li><a href="http://pipes.yahoo.com/pipes/pipe.info?_id=0mwRk4O72xGtSjMVl7okhQ" target="_blank">Un moteur de recherche combinant les résultats de Google et de Yahoo</a></li>
<li>Une carte trouvant des <a href="http://pipes.yahoo.com/pipes/pipe.info?_id=vvW1cD212xGMiR9aqu5lkA" target="_blank">photos flickr prises d’endroits cités à la première page du new York Times</a></li>
<li>Un « <a href="http://pipes.yahoo.com/pipes/pipe.info?_id=0g8N7Hu82xGydYNOJjBjOg" target="_blank">Aggregated News Alert</a> » capable de retrouver beaucoup de choses sur les blogs du monde entier…</li>
<li>et bien d’autres choses qui donnent une petite idée de ce que pourra devenir un web dans lequel les sites échangent leurs informations…</li>
</ul>
<p align="left">Références:</p>
<ul>
<li><a href="http://www.outilsfroids.net/news/yahoo-pipes-un-puissant-service-pour-la-veille-entre-autres-choses" target="_blank">article en français </a></li>
<li><a href="http://www.dashes.com/anil/2007/02/08/yahoo_pipes" target="_blank">article en anglais</a> d’où j’ai tiré les illustrations</li>
</ul>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
