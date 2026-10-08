---
title: "Javascript : le langage de programmation le plus incompris du monde"
date: "2012-10-21T09:33:47"
lastmod: "2015-04-24T23:20:18"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["histoire", "javascript"]
url: "/2012/10/21/javascript-le-langage-de-programmation-le-plus-incompris-du-monde/"
wordpress_id: 1033
comment_count: 3
---
<p dir="ltr"><em>en 2001, <a href="http://fr.wikipedia.org/wiki/Douglas_Crockford" target="_blank">Douglas Crockford</a>  a publié « JavaScript:The World’s Most Misunderstood Programming Language » <a href="http://javascript.crockford.com/javascript.html" target="_blank">sur son site</a> <a href="http://www.crockford.com/">www.crockford.com</a>. Ce texte fut traduit en plusieurs langues, dont le français par mes soins en 2009, mais un autre traducteur m’avait devancé de quelques jours… Comme cette autre traduction n’est plus disponible (<a href="http://lepinekong.fr/douglas-crockford-javascript-le-plus-incompris-des-languages-au-monde/" target="_blank">lien cassé</a>), je publie la mienne ici.</em></p>
<p dir="ltr"><em>Je trouve ce texte intéressant dans la mesure où « le langage de programmation le plus incompris du monde est devenu le langage de programmation le plus populaire du monde ». C’est <a href="http://javascript.crockford.com/popular.html" target="_blank">le titre d’un autre texte</a> de Crockford à traduire un de ces jours.</em></p>
<p><a href="http://www.crockford.com/javascript">JavaScript,</a> alias Moka, alias LiveScript, alias JScript, alias ECMAScript, est l’un des plus langages de programmation les plus populaires. Pratiquement tous les ordinateurs personnels au monde ont au moins un interpréteur JavaScript installé et utilisé intensivement. La popularité de JavaScript est entièrement due à son rôle en tant que langage de script du web.<br/>
Malgré sa popularité, peu de gens savent que JavaScript est un très bon langage de programmation dynamique, orienté objet, d’usage général.Comment cela peut-il être un secret? Pourquoi ce langage est-il si mal compris?</p>
<h3 dir="ltr">Le Nom</h3>
<p>Le préfixe Java suggère que JavaScript est en quelque sorte liés à Java, que c’est un sous-ensemble ou une version moins puissante de Java. Il semble que ce nom ait été volontairement choisi pour créer la confusion, et de cette confusion vient le malentendu. JavaScript n’est pas un Java interprété. Java est un Java interprété. JavaScript est un langage différent.<br/>
JavaScript est syntaxiquement similaire à Java, tout comme Java ressemble à C. Mais il n’est pas plus un sous-ensemble de Java que Java est un sous-ensemble de C. Il vaut mieux que Java dans les applications auxquelles Java (originellement Oak) était initialement destiné.<br/>
JavaScript n’a pas été développé chez Sun Microsystems, les créateurs de Java. JavaScript a été développé chez Netscape. Il a été à l’origine appelé LiveScript, mais ce nom n’était pas suffisamment confus.<br/>
Le suffixe -Script suggère que ce n’est pas un vrai langage de programmation, qu’un langage de script est inférieur à un langage de programmation. Mais c’est vraiment une question de spécialisation. Par rapport à C, JavaScript sacrifie la performance pour le dynamisme et le pouvoir expressif.</p>
<h3 dir="ltr">un Lisp dans un costume de C</h3>
<p>La syntaxe à la C de JavaScript, avec ses accolades et sa maladroite déclaration for le font apparaître comme un langage procédural ordinaire. Ceci est trompeur parce que JavaScript a plus en commun avec les langages fonctionnels comme <a href="http://javascript.crockford.com/little.html">Lisp ou Scheme</a> qu’avec C ou Java. Il a des tableaux plutôt que des listes et des objets au lieu de listes de propriétés. Les fonctions sont de première classe. Il a les fermetures. Vous avez les lambdas sans avoir à équilibrer toutes ces parenthèses.</p>
<h3 dir="ltr">Transtypage</h3>
<p>JavaScript a été conçu pour fonctionner dans Netscape Navigator. Son succès le conduisit à devenir un composant standard de presque tous les navigateurs Web. Il en est résulté le transtypage. JavaScript est le <a href="http://www.amazon.com/exec/obidos/ASIN/B000KWZ7JC/wrrrldwideweb">George Reeves</a> des langages de programmation. <a href="http://www.amazon.com/exec/obidos/ASIN/B000KWZ7JC/wrrrldwideweb">(note du traducteur : je ne comprends pas vraiment l’allusion…)</a>JavaScript convient bien à un large éventail d’applications non liées au Web</p>
<h3 dir="ltr">Cible mouvante</h3>
<p>Les premières versions de JavaScript étaient assez faible. Il manquait la gestion des exceptions, les fonctions internes et l’héritage. Dans sa forme actuelle, c’est maintenant un langage de programmation orienté objet complet. Mais de nombreux avis sur ce langage sont basés sur ses anciennes formes immatures.<br/>
Le comité de l’ECMA qui gère le langage développe des extensions qui, quoique bien intentionnées, vont aggraver l’un des plus grands problèmes du langage: il y a déjà de trop nombreuses versions. Cela crée de la confusion.</p>
<h3 dir="ltr">Erreurs de conception</h3>
<p>Aucun langage de programmation n’est parfait. JavaScript a sa part d’erreurs de conception, telles que la surcharge de + pour désigner à la fois l’addition et la concaténation avec forçage de type, ainsi que le with source d’erreurs, à éviter. La politique des mots réservés est beaucoup trop stricte. L’ajout des point-virgule a été une énorme erreur, tout comme la notation des expressions régulières littérales. Ces erreurs ont conduit à des erreurs de programmation, et remis en question toute la conception du langage. Heureusement, beaucoup de ces problèmes peuvent être atténués avec un bon programme <a href="http://www.crockford.com/javascript/lint.html">lint</a>.<br/>
Dans l’ensemble, la conception du langage est bien solide. Étonnamment, le comité ECMAScript ne semble pas être intéressé à corriger ces problèmes. Peut-être qu’ils sont plus intéressés à en créer de nouveaux.</p>
<h3 dir="ltr">Implementations Douteuses</h3>
<p>Certaines des premières implémentations de JavaScript étaient assez boguées. Cela jeta le discrédit sur le language. De plus, ces implémentations ont été incorporées dans des navigateurs web horriblement bogués.</p>
<h3 dir="ltr">Mauvais livres</h3>
<p>Presque tous les livres concernant JavaScript sont carrément mauvais. Ils contiennent des erreurs, de mauvais exemples, et promeuvent de mauvaises pratiques. Les principales caractéristiques du language sont souvent mal expliquées, ou entièrement ignorées. J’ai passé en revue des dizaines de livres JavaScript, et je ne peux en recommander qu’ un: <a href="http://www.amazon.com/exec/obidos/ASIN/0596101996/wrrrldwideweb">Javascript: The Definitive Guide (5th Edition)</a> par David Flanagan. (Auteurs attention: Si vous en avez écrit un bon, s’il vous plaît envoyez-moi une copie d’examen.)</p>
<h3 dir="ltr">Standard sous-standard</h3>
<p>La <a href="http://www.ecma-international.org/publications/standards/Ecma-262.htm">spécification officielle du langage</a> est publié par <a href="http://www.ecma-international.org/">l’ECMA.</a> La spécification est de très mauvaise qualité. Elle est difficile à lire et très difficile à comprendre. Cela a contribué au promlème « Mauvais Livres » parce que les auteurs ont été incapables d’utiliser le document standard pour améliorer leur propre compréhension du langage. L’ECMA et le comité TC39 devraient être profondément gênés.</p>
<h3 dir="ltr">Amateurs</h3>
<p>La plupart des gens qui écrivent en JavaScript sont pas des programmeurs. Il leur manque la formation et la discipline pour écrire de bons programmes. JavaScript a tellement de pouvoir expressif qu’ils sont capables d’en faire des choses utiles malgré ceci. Cela a donné à JavaScript la réputation d’être strictement destiné aux amateurs, et qu’il ne convient pas à la programmation professionnelle. Ce n’est tout simplement pas le cas.</p>
<h3 dir="ltr">Orienté Objet</h3>
<p>JavaScript est-il orienté objet ?Il a des objets qui peuvent contenir des données et des méthodes qui agissent sur ces données. Les objets peuvent contenir d’autres objets. Il n’a pas de classes, mais il a des constructeurs qui font ce que les classes font, notamment en agissant comme des conteneurs de variables de classe et de méthodes. Il n’y a pas d’héritage orienté classe, mais il y a un héritage orienté prototype.<br/>
Les deux principales façons de construire des systèmes objets sont par héritage (est-un) et par agrégation (a-un). JavaScript fait les deux, mais sa nature dynamique lui permet d’exceller dans l’agrégation.<br/>
Certains prétendent que JavaScript n’est pas véritablement orienté objet, car il ne permet pas de cacher l’information. Autrement dit, les objets ne peuvent pas avoir de variables privées ou de méthodes privées: tous les membres sont publics.<br/>
Mais il s’avère que <a href="http://www.crockford.com/javascript/private.html">les objets JavaScript peuvent avoir des variables privées et des méthodes privées.(Cliquez ici maintenant pour savoir comment faire.)</a> Bien sûr, peu de gens comprennent cela parce que JavaScript est le langage le plus incompris au monde.<br/>
Certains prétendent que JavaScript n’est pas véritablement orienté objet, car il ne prévoit pas l’héritage. Mais il s’avère que <a href="http://javascript.crockford.com/inheritance.html">JavaScript supporte non seulement l’héritage classique, mais aussi d’autres modèles de réutilisation du code.</a><br/>
Copyright 2001 <a href="mailto:douglas@crockford.com">Douglas Crockford.</a> <a href="http://www.crockford.com/">Tous droits réservés Wrrrldwide.</a></p>

## Commentaires

### Yves Masur — 27 octobre 2012 à 16:39

<section class="comment-content comment">
<p>Je confesse être totalement tombé dans les travers mentionnés par cet article. Parce que le code que je pouvais lire était obscur, commence par tester sur quel browser il tourne pour charger des correctifs. Je n’en ai utilisé que pour le projet de la barrette (<a href="../../../../2011/03/25/projet-barrette-livrable/index.html" rel="nofollow"> ici </a>) en 2010. Même pour le formulaire de commande de mon <a href="http://www.yvesmasur.ch/livre/" rel="nofollow"> livre </a> a été fait 100% en PHP. Et probablement que le livre « tout en poche » de Javascript ne m’a pas aidé a y voir quelque chose de mieux qu’une touille juste bonne a bricoler une adresse email invisible pour le moteurs de recherche; ou dans le meilleur des cas un gadget inutile pouvant planter le browser…</p>
 </section>

### Luc ROLLAND — 3 décembre 2012 à 09:16

<section class="comment-content comment">
<p>Bonjour,</p>
<p>Merci pour cette intéressante traduction.</p>
<p>Je pense que <cite>JavaScript est le George Reeves des langages de programmation</cite> devrait être compris comme « JavaScript est le Superman des langages de programmation » (cet acteur est très connu aux USA pour son interprétation de ce super héro dans une série des années 50).</p>
<p>Le lien brisé <strike>lint </strike>pourrait être redirigé sur cette adresse :<br/>
<a href="http://www.javascriptlint.com/" rel="nofollow ugc">http://www.javascriptlint.com/</a></p>
<p>Je m’interroge sur l’intérêt de <strong>WAKANDA</strong> basé sur JavaScript et NoSQL pour des développements Web …</p>
 </section>

### ymasur — 19 septembre 2015 à 20:39

<section class="comment-content comment">
<p>Alex, Coorden, co-fondateur de Guru99, signale qu’un tuto moderne (2015) est disponible ici:<br/>
<a href="http://www.guru99.com/interactive-javascript-tutorials.html" rel="nofollow ugc">http://www.guru99.com/interactive-javascript-tutorials.html</a></p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
