---
title: "Maitriser le contenu des flux RSS"
date: "2008-03-14T14:58:41"
lastmod: "2015-04-24T23:20:21"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["google", "rss", "xfruits", "yahoo"]
url: "/2008/03/14/maitriser-le-contenu-des-flux-rss/"
wordpress_id: 398
comment_count: 2
---
*([english version here](http://www.swissw2.ch/content/controling-rss-feeds-content))*

Les flux RSS permettent de publier sur un site du contenu « agrégé » à partir d’autres sites. La mésaventure de [Fuzz / Presse-citron](http://www.presse-citron.net/?2008/03/12/3162-bonne-nouvelle-fuzz-rapporte-enfin-beaucoup-d-argent) illustre les problèmes légaux que cela pose, du moins tant que les tribunaux n’auront pas établi une jurisprudence à ce sujet.

Ayant rencontré cette problématique dans d’autres contextes, voici quelques moyens que j’ai trouvé d’agréger du contenu de manière contrôlée:

1. un agrégateur de flux « de confiance ». Plutôt que d’enlever le contenu indésiré, mieux vaut n’agréger que du contenu provenant de sources de confiance, en créant son propre agrégateur. [xfruits.com](http://xfruits.com/goulu/) permet de faire ceci (entre autres). J’obtiens ainsi entre autres [le flux « News des teams »](http://xfruits.com/goulu/?id=35403) diffusé sur le blog [Foilers](http://foils.wordpress.com/), alimenté par les différentes équipes de vitesse à la voile que je connais bien, mais aussi [le flux « Goulu News](http://xfruits.com/goulu/?id=28230) » qui me permet de diffuser sur chacun de mes blogs les nouvelles publiées sur les autres blogs.
2. [Yahoo Pipes](http://pipes.yahoo.com/) est un véritable « langage de programmation » de flux RSS qui permet entre nombreuses autres choses de filtrer le contenu d’un flux en éliminant par exemple les posts contenant les mots « Tom Cruise » ou « scientologie »…
3. Le moyen le plus efficace restera longtemps encore le tri manuel, et [GoogleReader](http://www.google.com/reader/) est un moyen très efficace de l’effectuer : il suffit de cliquer sur l’ icône « partager » d’un post pour ajouter le contenu à un flux personnel. Je produis ainsi [le flux « Nouvelles Choisies »](http://www.google.com/reader/public/atom/user/07530539290389081456/state/com.google/broadcast) qui diffuse sur tous mes blogs les articles lus ou parcourus sur les (trop) nombreux flux que je suis.

Les 3 méthodes peuvent être combinées à souhait pour obtenir des flux bien ciblés et propres, et peut-être éviter des désagréments.

## Commentaires

### Dr. Goulu — 17 mars 2008 à 17:54

un article intéressant sur la situation légale en France : <http://fr.techcrunch.com/2008/03/17/fr-les-flux-rss-et-la-vie-privee/>

### lomig — 30 juin 2008 à 15:18

salut,\
merci pour cet article très clair.\
Je cherche à aggréger plusieurs flux, et à créer avec ces flux un flux RSS unique, publiable. Dois-je utiliser Yahoo Pipes, ou y’a t il des moyens plus simples ?

je suis sous WordPress

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
