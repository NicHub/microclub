---
title: "CMS, Blogs et Wikis"
date: "2006-06-03T19:44:29"
lastmod: "2015-04-24T23:20:25"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["web"]
url: "/2006/06/03/cms-blogs-et-wikis/"
wordpress_id: 85
comment_count: 0
---
<p>Comment faire un site web presque aussi réussi que Goulu.net ? Vous saurez tout sur les nombreux systèmes que j’ai utilisé depuis près de 10 ans pour la construction de sites internet.</p>
<p><!--more--></p>
<h3>Principe</h3>
<p>Les pages disponibles sur le « Workd Wide Web » sont en principe codées en HTML. Un site est simplement un serveur capable de de fournir du contenu au format HTML en fonction de l’adresse, appelée URL, de la page.</p>
<p>La manière la plus simple est de stocker les pages au format HTML dans des fichiers séparés. L’URL contient alors le nom du fichier, par exemple « photos.htm » ou « articlesurlevelo.html ». On parle alors d’un site « statique ». Pour fabriquer ces pages, il existe 3 possibilités:</p>
<ol>
<li>taper le code HTML à la main dans un éditeur de texte. Il faut apprendre le HTML pour commencer…</li>
<li>utiliser un editeur HTML plus ou moins sophistiqué comme Microsoft Frontpage. C’est ainsi que j’ai commencé par créer ce site en 1997 déjà…</li>
<li>exporter un document écrit avec un programme quelconque au format HTML. Facile et pratique si on veut faire une ou deux pages, mais pas souple du tout pour créer des sites complexes.</li>
</ol>
<p>La plupart des sites récents sont « dynamiques » : un programme fonctionnant sur le serveur produit le code HTML au moment où il est demandé en extrayant le contenu d’une base de données et en le mettant en forme en fonction de l’URL demandée. Ceci a de très nombreux avantages:</p>
<ol>
<li>plus besoin de connaitre le HTML : on peut écrire du contenu très facilement, souvent directement dans l’explorateur.</li>
<li>on peut ainsi facilement créer des sites collaboratifs, où les visiteurs peuvent interagir en ajoutant du contenu, dans des forums par exemple.</li>
<li>la présentation est séparée du contenu : on peut changer le look complet d’un site en quelques minutes, sans avoir à modifier le contenu.</li>
<li>les pages peuvent afficher des informations différentes selon la date, par exemple ajouter des actualités venant d’autres sites.</li>
</ol>
<h3>CMS</h3>
<p>Le programme fonctionnant sur le serveur est un CMS (Content Management System). Il en existe de très nombreux, répertoriés sur <a href="http://www.cmsmatrix.org/">CMS Matrix</a>. Beaucoup sont gratuits (« open source »), écrits en langage <a href="http://www.php.net/">PHP</a> et utilisent la base de données <a href="http://www.mysql.com/">MySQL</a>, qui sont disponibles dans la plupart des offres d’hébergement.</p>
<p>Bien que la distinction soit un peu arbitraire, on peut distinguer plusieurs types de CMS:</p>
<ul>
<li>les « portails » donnent accès aux visiteurs à divers contenus structurés, principalement un contenu édité par des rédacteurs précis. Des forums permettent un dialogue avec/entre les visiteurs. Les sites d’entrerprises et d’organisations sont en principe des « portails »</li>
<li>les Blogs ou Blogues sont des sortes de journaux affichent les articles écrits par une personne dans l’ordre chronologique, en laissant parfois la possibilité aux visiteurs d’y ajouter leurs commentaires</li>
<li>les Wikis sont des sites permettant à chaque visiteur d’ajouter ou d’éditer le contenu! La fameuse encyclopédie <a href="http://www.wikipedia.org/">Wikipedia</a> est l’exemple le plus spectaculaire de ce qui peut en résulter.</li>
</ul>
<p>Voici les CMS que je connais, dans l’ordre où je les ai utilisés pour divers sites, dont celui-ci:</p>
<h4><a href="http://www.dotclear.net">DotClear</a></h4>
<p>DotClear est le meilleur compromis puissance/facilité que j’aie trouvé jusqu’ici pour un site personnel ou de petite taille, genre blogs. Il s’installe et se configure facilement, et on trouve sur le web de nombreux « templates » pour la mise en forme et « modules » complémentaires pour des fonctionnalités étendues. L’essayer c’est l’adopter!</p>
<h4><a href="http://www.mamboserver.com/">Mambo</a>/<a href="http://www.joomla.org/">Joomla</a></h4>
<p>Mambo est un CMS qui marche fort ces temps pour la création de « portails » sophistiqués, d’autant qu’il existe un quantité de « composants » et de « modules » pour compléter ses déjà nombreuses fonctions. Je l’ai proposé pour le nouveau site de mon employeur, en particulier parce qu’il se marie bien avec « SugarCRM », un système de gestion de clientèle traité dans un autre article.</p>
<p>A la suite d’une petite guéguerre du genre « je suis plus open-source que toi », un groupe de développeurs s’est mis à travailler sur Joomla, en empruntant beaucoup de code à Mambo… Mambo et Joomla sont donc 2 CRM extrêmement similaires actuellement, difficile de dire lequel deviendra la plus répandu.</p>
<h4><a href="http://www.ez.no">ez-Publish</a></h4>
<p>A mon avis, c’est le top du must du CMS, mais version « usine à gaz »:</p>
<ul>
<li>Il contient tout ce qu’il faut pour faire un super site professionnel, avec e-Commerce et tout.</li>
<li>De plus, il a un modèle de « classes » permettant de définir de nouveaux types de pages et un « workflow » pour faire circuler l’information. Je pense qu’il serait possible par exemple de faire un système de suivi de problèmes avec eZ-Publish</li>
<li>Il a même un éditeur de contenu « off-line » qui permet de contourner le principal inconvénient que j’ai trouvé aux CMS : il faut être connecté pour écrire un article.</li>
</ul>
<p>J’avais essayé de créer un size avec ez-Publish, mais la gestion d’un tel site est vraiment lourde pour une utilisation privée.</p>
<h4><a href="http://www.spip.net">SPIP</a></h4>
<p>CMS très complet d’origine française, idéal pour les sites de journaux ou de magazines. L’installation est extrêmement simple : il suffit de télécharger un seul fichier PHP sur le serveur, et il s’occupe de tout! Par contre la personnalisation de la présentation par des « squelettes » est malheureusement très laborieuse, et il n’existe que peu de squelettes tout faits et bien faits.</p>
<p>J’ai utilisé SPIP pour Goulu.net pendant quelques mois, mais craqué pour les facilités d’édition de MediaWiki</p>
<h4><a href="http://www.mediawiki.org">[MediaWiki</a></h4>
<p>MediaWiki est le moteur de la Wikipedia, mais il peut être utilisé pour tout autre site. Goulu.net l’a utilisé pendant plus d’un an, principalement pour sa facilité d’édition de contenu.</p>
<p>Rien à redire, si ce n’est que le wiki a surtout du sens lorsqu’il y a plusieurs rédacteurs, et que la présentation des pages est un peu trop sobre, avec peu de moyens de modifier facilement le look du site.</p>
<p>J’ai donc utilisé MediaWiki pour créer la « base de connaissances » interne à l’entreprise qui m’emploie, et je trouve que c’est l’idéal. Mais pour un site perso, il y a mieux.</p>
<p>Les wikis ont inventé la « syntaxe Wiki » utilisée pour l’édition aisée de contenu. Tous mes futurs CMS devront impérativement accepter cette convention, qui permet entre autres de transférer facilement du contenu d’un CMS à un autre.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
