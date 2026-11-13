---
title: "Scalable Vector Graphics (SVG)"
date: "2006-02-24T12:46:17"
lastmod: "2015-04-24T23:20:25"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["graphiques", "non-classe", "svg", "web"]
url: "/2006/02/24/scalable-vector-graphics-svg/"
wordpress_id: 454
comment_count: 0
---

## Introduction

Scalable Vector Graphics (SVG) est un format [XML](http://www.goulu.net/wordpress/wp-admin/XML) standardisé par le [W3C](http://www.w3.org/Graphics/SVG/) qui offre de nombreux avantages sur les autres formats vectoriels :

-   C’est un format ouvert, non-propriétaire, au contraire de DXF, DWG et DWF (Autodesk), EMF, EMZ, WMF, WMZ ou CGM (Microsoft), PDM (Adobe) ou Flash (Macromedia) et bien d’autres
-   La version comprimée (.SVGZ) est très compacte. En sauvant par exemple un grand plan CAO en différents formats, seul DWF produit un fichier encore plus petit que SVGZ
-   SVG supporte l’animation presque aussi bien que Flash, auquel il ressemble beaucoup.
-   SVG peut être affiché sur des pages web.

## Affichage

Pour visualiser des fichiers SVG ou des pages contenant du SVG, tout dépend de votre navigateur:

-   Mozilla Firefox supporte désormais [SVG en mode natif](http://www.mozilla.org/projects/svg)
-   Microsoft Internet Explorer a besoin d’un plugin, le plus connu étant [Adobe SVG Viewer](http://www.adobe.com/svg/viewer/install)
-   Opera nécessite d’installer un plugin en suivant [ces instructions](http://www.opera.com/support/search/supsearch.dml?index=466)

## Génération

On peut créer des fichiers SVG de différentes manières:

1. avec un programme de dessin pouvant exporter, voire importer du SVG:
    -   [Adobe Illustrator](http://www.adobe.com/products/illustrator/main.html) (v.9 export, v.10 import/export)
    -   [Corel Draw](http://www.corel.com) Draw v.11 import+export
    -   [IsoDraw](http://www.itedo.com/E/274.php)
2. Avec un programme de dessin spécialisé en SVG comme [InkScape](http://www.inkscape.org), [XStudio](http://www.evolgrafix.de/htDocs/html/products/xstudio6x/index.shtml), [WebDraw](http://www.corel.com/servlet/Satellite?pagename=Corel3/Products/Display&pid=1047024390402).
3. En « imprimant » n’importe quel document depuis n’importe quelle application (notamment les CAO comme [SolidWorks](http://www.goulu.net/wordpress/wp-admin/SolidWorks)…) grâce au génial [ePrint](http://www.goulu.net/wordpress/wp-admin/ePrint)
4. Certains programmes spécialisés produisent des résultats au format SVG. C’est notamment le cas de [ImageMagick](http://www.goulu.net/wordpress/wp-admin/ImageMagick) et [GraphViz](http://www.goulu.net/wordpress/wp-admin/GraphViz), qui génère automatiquement de beaux graphes à partir d’une simple description texte. Sur <http://www.cadml.org> je montre comment générer ainsi des graphes de dépendances entre fichiers CAO, un peu sur le même principe que [Doxygen](http://www.goulu.net/wordpress/wp-admin/Doxygen).
5. En « programmant » directement le code SVG. En principe on peut le faire avec un simple éditeur de texte, mais il existe des éditeurs XML comme [Amaya](http://www.w3.org/Amaya/Amaya.html) ou [XML Spy](http://www.altova.com/products_ide.html)

## Programmation

<http://www.svgbasics.com> contient tout ce qu’il faut savoir pour créer des fichiers SVG, mais c’est en anglais. En français il existe [ce cours](http://tecfa.unige.ch/staf/staf-g/sierra/staf2x/sitesvg.htm) qui est bien fait.

<http://blog.codedread.com/archives/2005/12/01/guide-to-deploying-svg-with-html>

## Références

-   <http://svgfr.org> et <http://www.svg.org>
-   [Comment intégrer du svg dans un article spip](http://marc.lauffer.free.fr/article.php3?id_article=23)
-   [Embedding SVG in WordPress posts](http://www.latenightpc.com/blog/archives/2006/01/13/embedding-svg-in-wordpress-posts)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
