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
Depuis quelques mois j’explore les possibilités du « [Web 2.0](http://fr.wikipedia.org/wiki/Web_2.0)« , dont l’utilisation des [flux RSS](http://www.projets.ch/goulu/?p=213) est l’élément le plus concret. Par exemple, mes blogs offrent chacun un flux auquel vous pouvez vous abonner, mais aussi :

1. un bloc « Nouvelles Choisies » qui liste les articles qui m’ont intéressé sur les dizaines de flux auxquels je suis abonné.
2. un bloc « Goulu News » qui regroupe les articles publiés sur tous mes blogs en un seul fluy

Voici comment ces flux sont générés.

Pour les « Nouvelles Choisies », c’est très simple : utilisant [« Google Reader » pour lire mes flux](/2007/05/10/flux-rss/), il me suffit de cocher l’icône « Share » au bas de chaque article intéressant pour l’ajouter à [ce flux généré tout seul par Google](http://www.google.com/reader/public/atom/user/07530539290389081456/state/com.google/broadcast).

Pour les « Goulu News », il me fallait un système permettant d' »agréger » plusieurs flux automatiquement en un seul en ligne, sans intervention humaine.

La solution la plus simple a été d’utiliser Ziki.com : dans [mon profil Ziki](http://www.ziki.com/fr/people/goulu), j’ai pu définir tous mes blogs et leur flux RSS respectifs, et Ziki les combine pour moi [en un seul](http://www.ziki.com/fr/people/goulu/rss/10), que je peux ensuite réutiliser dans les différents blogs. Le seul ennui de cette solution est un retard de plusieurs heures, voire 1 jour entre la publication d’un nouveau billet et la mise à jour du flux aggrégé par Ziki.

[![](http://www.groupereflect.net/blog/images/xfruits-1.png)xFruits.com](http://xfruits.com/) est un service permettant non seulement d’agréger des flux en ligne, mais aussi de les convertir dans tous les sens à l’aide de « briques ». On peut par exemple générer des pages web pour téléphones mobiles à partir de flux RSS, ou convertir un flux en « podcast » à l’aide d’un service de voix synthétique. Les « xFruits » ainsi définis par chaque utilisateur peuvent être partagés et consultés par tout le monde. [Les miens sont ici](http://xfruits.com/goulu/).

La prochaine étape serait une véritable « langage de programmation » permettant de manipuler des flux RSS facilement, et en ligne si possible.

[![](http://pipes.yahoo.com/img/logo-lg.gif)](http://pipes.yahoo.com/)C’est exactement ce que fait « [Yahoo Pipes](http://pipes.yahoo.com)« , un outil aussi spectaculaire que facile à utiliser pour combiner, filter, trier des informations provenant de différentes sources via flux RSS ([mes « pipes » sont ici](http://pipes.yahoo.com/pipes/person.info?eyuid=5S9f6qU0p3bLsNVYuvVJjec-))

![](http://www.dashes.com/anil/images/yahoo-pipes.gif)

Dans Yahoo Pipes, on « programme » de manière graphique en câblant des opérations entre des entrées , généralement des flux RSS (en haut) et une sortie, un nouveau flux RSS (en bas). Des opérations intermédiaires permettent de trier les flux, de les filtrer en enlevant certains articles, ou d’effectuer des recherches

![](http://www.dashes.com/anil/images/yahoo-pipes-ide.png)

on peut ainsi créer de véritable « mashups » en combinant les fonctionnalités de sites web 2.0, et les mettre à disposition de tout le monde. En explorant les « [pipes les plus populaires](http://pipes.yahoo.com/pipes/pipes.popular) » on trouve par exemple:

- [Un moteur de recherche combinant les résultats de Google et de Yahoo](http://pipes.yahoo.com/pipes/pipe.info?_id=0mwRk4O72xGtSjMVl7okhQ)
- Une carte trouvant des [photos flickr prises d’endroits cités à la première page du new York Times](http://pipes.yahoo.com/pipes/pipe.info?_id=vvW1cD212xGMiR9aqu5lkA)
- Un « [Aggregated News Alert](http://pipes.yahoo.com/pipes/pipe.info?_id=0g8N7Hu82xGydYNOJjBjOg) » capable de retrouver beaucoup de choses sur les blogs du monde entier…
- et bien d’autres choses qui donnent une petite idée de ce que pourra devenir un web dans lequel les sites échangent leurs informations…

Références:

- [article en français](http://www.outilsfroids.net/news/yahoo-pipes-un-puissant-service-pour-la-veille-entre-autres-choses)
- [article en anglais](http://www.dashes.com/anil/2007/02/08/yahoo_pipes) d’où j’ai tiré les illustrations

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
