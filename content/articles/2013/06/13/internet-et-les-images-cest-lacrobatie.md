---
title: "Internet et les images, c’est l’acrobatie"
date: "2013-06-13T09:57:18"
lastmod: "2015-04-24T23:20:17"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["internet", "photos", "securite", "wordpress"]
url: "/2013/06/13/internet-et-les-images-cest-lacrobatie/"
wordpress_id: 1256
comment_count: 1
---
Internet, c’est tellement facile : on voit une image qui nous plait pour illustrer un article, hop, on copie le lien vers l’image dans son propre blog :

[![](http://www.drgoulu.com//HLIC/8d051439297695af67728cb76d11a944.jpg)](http://www.d-aprilli.net/www.d-aprilli.net/GalerieAvions/index.html)

Et voilà. L’auteur de cette magnifique photo, que je salue au passage, pourrait légitimement prétendre que je lui ai volé cette photo sans autorisation, à quoi je pourrais lui répondre que non ( si j’étais de mauvaise foi ) puisqu’elle est toujours sur son serveur  : je ne l’ai pas copiée, j’ai juste mis \<img src= » »<http://www.d-aprilli.net/www.d-aprilli.net/GalerieAvions/content/images/large/dAprilli_Avion002.jpg> »\> dans le texte HTML de cet article…

Mais il pourrait également considérer que ce « [hotlink](http://fr.wikipedia.org/wiki/Hotlinking) » lui vole de la bande passante : chaque visite sur ma page va générer du trafic sur son serveur pour  télécharger 1180 Ko, et son hébergeur doit payer le matos et la connexion en conséquence, dont il répercute le coût sur ses clients, donc mon lien ci-dessus engendre des coûts pour lui.

Avant de voir comment éviter ceci, voyons comment le détecter. Le moyen le plus simple est d’utiliser la recherche d’images Google en mettant comme chaîne de recherche « inurl:monsite.com -site:monsite.com », ce qui signifie « montre les images qui ont monsite.com dans leur URL, mais qui ne sont pas sur monsite.com ».

Par exemple pour drgoulu.com [ça donne ça](https://www.google.ch/search?q=inurl:drgoulu.com+-site:drgoulu.com&um=1&ie=UTF-8&hl=fr&tbm=isch) : des images sont « hotlinkées » vers mon site surtout depuis des forums, des pages Google+ qui ont repris le flux RSS de mon site qui contient évidemment des liens vers les images et des sites « amis » comme [cafe-sciences.org](http://www.cafe-sciences.org/) , [kidiscience](http://kidiscience.cafe-sciences.org/), et [microclub.ch](/).

Quand c’est à petite échelle comme ça c’est tolérable, mais pour un site [comme nationalgeographic.com](https://www.google.ch/search?q=inurl:nationalgeographic.com+-site:nationalgeographic.com&um=1&ie=UTF-8&hl=fr&tbm=isch) par exemple, le hotlinking peut coûte cher …

### Comment empêcher le hotlinking

![](http://www.drgoulu.com//HLIC/6027a4548308db94d64a59a91d7a4d52.gif)La méthode la plus simple pour l’empêcher est de modifier le [fichier .htaccess](http://fr.wikipedia.org/wiki/Htaccess) pour qu’il renvoie aux serveurs extérieurs une autre image que celle demandée, par exemple celle ci-contre ou une pire. Cette image apparaîtra subitement à la place de l’image originale sur tous les sites ayant fait des hotlinks…

MAIS il faut bien faire attention à Google, qui indexe les images de votre site et qui, ne voyant que votre image anti-hotlink, risque de se dire que si toutes vos images sont les mêmes, votre site est sans intérêt et baisser votre pagerank.

De plus, et peut être plus important encore, de plus en plus d’internautes utilisent la recherche d’images. En une année, la recherche « normale » sur Google a amené 110’000 visiteurs sur drgoulu.com, la recherche d’images 35’000 de plus : ce n’est dont pas négligeable du tout, et encore mon site n’est pas spécialisé dans la photo.

Il faut donc permettre à Google et peut être à d’autres sites de recherche d’images comme TinEye (dont je cause plus bas) d’accéder aux images de votre site pour les indexer. Tout ceci et comment procéder est [très bien décrit ici](http://www.referencement-seo.com/htaccess-hotlink-protection-vol-image-contenu.html).

### Empêcher la copie, c’est mission impossible  …

Si un site empêche le hotlinking, il va encourager la copie : pour intégrer une image sur un article je sauve l’image sur mon bureau, je l’uploade sur mon site et voilà.

Et il est impossible d’empêcher ceci : à partir du moment où vous voyez une image sur votre browser, vous pouvez la copier. En fait elle a déjà été copiée sur votre ordinateur par le browser. Comme webmaster, vous pouvez tout au plus utiliser [certains petits trucs](http://www.cambridgeincolour.com/tutorials/protect-online-photos.htm) pour rendre la copie de l’image plus difficile pour un visiteur néophyte, mais c’est impossible contre quelqu’un qui sait lire du code source HTML et dans tous les cas il reste la possibilité de la capture d’écran…

L’astuce de base pour les photos, c’est de publier une version « watermarkée » et/ou basse résolution des images sur les pages web, et de garder la version haute résolution un peu cachée par des liens pour ceux qui ont le droit, éventuellement payant, d’y accéder.

En faisant des copies de ces images, le lien avec le site d’origine est rompu. Si les rédacteurs n’ont pas la courtoisie d’indiquer la source de l’image avec un lien vers la page d’origine comme je l’ai fait pour la photo de D’aprilli, les visiteurs n’ont quasi aucun moyen de retrouver le photographe pour le féliciter.

![](http://www.drgoulu.com//HLIC/2f204297ed68aefb568e162f8ad9278f.jpg)Les seuls moyens que je connaisse sont [TinEye](http://www.tineye.com/) et Google Images (encore), mais il faut [lire le mode d’emploi](http://www.google.com/insidesearch/features/images/searchbyimage.html). Ces étonnants services de « recherche inversée » d’images renvoient renvoie une liste de documents web où une image figure, même déformée, recadrée, recolorée ou passablement altérée. Je les utilise parfois pour retrouver l’original d’une image de mauvaise qualité sur le web, ou qui a piqué mes images…

D’après ma maigre expérience, Google trouve plus d’images car il indexe plus de sites, mais TinEye retrouve des images plus fortement modifiées.

En passant, comme je m’étais intéressé à [l’algorithme de Shazam](http://www.drgoulu.com/2009/07/11/comment-marche-shazam/) je me suis évidemment aussi posé la question pour la recherche d’images. [Sur leur forum, les gens de TinEye ne sont pas plus bavards](http://forums.tineye.com/discussion/77/does-tineye-base-on-mser-sifts/p1) que ceux de Google sur l’algorithme utilisé, et [cette discussion sur stackoverflow](http://stackoverflow.com/questions/1005115/what-algorithm-could-be-used-to-identify-if-images-are-the-same-or-similar-reg) ne permet que d’esquisser quelques pistes, parmi lesquelles:

- L’algorithme [Scale-invariant feature transform (SIFT)](http://fr.wikipedia.org/wiki/Scale-invariant_feature_transform), breveté, mais il le mérite
- La méthode [maximally stable extremal regions (MSER)](http://en.wikipedia.org/wiki/Maximally_stable_extremal_regions)
- J’ai encore trouvé cette référence : Zhong Wu  , Qifa Ke, Michael Isard, and Jian Sun, « [Bundling Features for Large Scale Partial-Duplicate Web Image Search](http://research.microsoft.com/pubs/80803/CVPR_2009_bundle.pdf)« , Microsoft Research, 2009 IEEE

### Le problème avec Google…

c’est qu’ils sont assez riches pour copier tout internet chez eux, y compris les images, et que parfois ils prennent des décisions toutes bêtes qui ont un gros impacts sur les plus petits qu’eux.

Depuis le 25 janvier 2013, Google copie même les images en pleine résolution qui ne sont pas directement visibles sur les sites indexés, et affiche ces images en pleine résolution sur les résultats de recherche, sans s’occuper de droits d’auteurs éventuels …

Il y a des sites commerciaux de photos et de fonds d’écrans qui râlent sec, et il y a de quoi quand on voit par exemple la chute du trafic enregistrée chez [pixabay.com](http://pixabay.com/) à ce moment :

[![](http://www.drgoulu.com//HLIC/c13586da587b889ab33fbafb03b381a9.png)](http://pixabay.com/)trafic chez pixabay.com au moment du changement chez Google…

Le choix est cornélien : comment bénéficier du service d’indexation des images de Google tout en conservant es droits auquel tout créateur a droit ?

Un excellent [article de pixabay](http://pixabay.com/en/blog/posts/hotlinking-protection-and-watermarking-for-google-32/) énumère plusieurs solutions possibles et celle choisie par pixabay : un système anti-hotlink s’appliquant à tout le monde même à Google, mais fournissant les images d’origine « watermarkées », ce qui leur a permis de récupérer une bonne part de leur audience.

### En pratique, pour WordPress

Quand j’écris un article, le hotlinking est tellement simple que je ne peux pas m’empêcher de l’utiliser pour insérer des images, et j’ai procédé ainsi pour toutes les images de cet article . copier l’adresse de l’image désirée, cliquer sur « Ajouter un média » dans [WordPress](http://fr.wordpress.org/) et coller dans « insérer à partir d’une adresse web ».

Mais le hotlinking c’est mal et ça peut être gênant, comme je m’en suis [aperçu il y a quelque années](http://www.drgoulu.com/2007/04/30/hotlinking/). Alors j’ai installé un plugin WordPress qui s’appelle [hot-linked-image-cacher](http://wordpress.org/plugins/hot-linked-image-cacher/) qui télécharge les images hotlinkées sur drgoulu.com et remplace mon hotlink par un link local, tout ça tout seul. Il est vieux mais marche très bien, je le recommande vivement. S’il ajoutait les images proprement à la galerie de WP, il serait parfait.

J’utilise aussi [imsanity](http://wordpress.org/plugins/imsanity/), qui s’occupe de faire automatiquement des versions basse résolution de mes grosses images, ce qui est rend le surf plus rapide et me permet de garder la version haute résolution pour moi…

Finalement, si j’étais photographe je regarderais de très près le [WP-PicShield](http://wordpress.org/plugins/byrev-wp-picshield-hotlink-defence/) recommandé par pixabay, qui me semble proposer toutes les fonctionnalités et compromis actuellement possibles dans ce délicat exercice d’équilibre entre référencement et pillage des images sur internet.

([article aussi publié sur drgoulu.com](http://www.drgoulu.com/2013/06/13/internet-et-les-images-cest-lacrobatie/))

## Commentaires

### helvetica — 19 juin 2013 à 08:49

Merci pour l’article; il est très complet et utile!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
