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
<h4>Introduction</h4>
<p>Scalable Vector Graphics (SVG) est un format <a href="http://www.goulu.net/wordpress/wp-admin/XML">XML</a> standardisé par le <a href="http://www.w3.org/Graphics/SVG/">W3C</a> qui offre de nombreux avantages sur les autres formats vectoriels :</p>
<ul>
<li>C’est un format ouvert, non-propriétaire, au contraire de DXF, DWG et DWF (Autodesk), EMF, EMZ, WMF, WMZ ou CGM (Microsoft), PDM (Adobe) ou Flash (Macromedia) et bien d’autres</li>
<li>La version comprimée (.SVGZ) est très compacte. En sauvant par exemple un grand plan CAO en différents formats, seul DWF produit un fichier encore plus petit que SVGZ</li>
<li>SVG supporte l’animation presque aussi bien que Flash, auquel il ressemble beaucoup.</li>
<li>SVG peut être affiché sur des pages web.</li>
</ul>
<h4>Affichage</h4>
<p>Pour visualiser des fichiers SVG ou des pages contenant du SVG, tout dépend de votre navigateur:</p>
<ul>
<li>Mozilla Firefox supporte désormais <a href="http://www.mozilla.org/projects/svg">SVG en mode natif</a></li>
<li>Microsoft Internet Explorer a besoin d’un plugin, le plus connu étant <a href="http://www.adobe.com/svg/viewer/install">Adobe SVG Viewer</a></li>
<li>Opera nécessite d’installer un plugin en suivant <a href="http://www.opera.com/support/search/supsearch.dml?index=466">ces instructions</a></li>
</ul>
<h4>Génération</h4>
<p>On peut créer des fichiers SVG de différentes manières:</p>
<ol>
<li>avec un programme de dessin pouvant exporter, voire importer du SVG:
<ul>
<li><a href="http://www.adobe.com/products/illustrator/main.html">Adobe Illustrator</a> (v.9 export, v.10 import/export)</li>
<li><a href="http://www.corel.com">Corel Draw</a> Draw v.11 import+export</li>
<li><a href="http://www.itedo.com/E/274.php">IsoDraw</a></li>
</ul>
</li>
<li>Avec un programme de dessin spécialisé en SVG comme <a href="http://www.inkscape.org">InkScape</a>, <a href="http://www.evolgrafix.de/htDocs/html/products/xstudio6x/index.shtml">XStudio</a>, <a href="http://www.corel.com/servlet/Satellite?pagename=Corel3/Products/Display&amp;pid=1047024390402">WebDraw</a>.</li>
<li>En « imprimant » n’importe quel document depuis n’importe quelle application (notamment les CAO comme <a href="http://www.goulu.net/wordpress/wp-admin/SolidWorks">SolidWorks</a>…) grâce au génial <a href="http://www.goulu.net/wordpress/wp-admin/ePrint">ePrint</a></li>
<li>Certains programmes spécialisés produisent des résultats au format SVG. C’est notamment le cas de <a href="http://www.goulu.net/wordpress/wp-admin/ImageMagick">ImageMagick</a> et <a href="http://www.goulu.net/wordpress/wp-admin/GraphViz">GraphViz</a>, qui génère automatiquement de beaux graphes à partir d’une simple description texte. Sur <a href="http://www.cadml.org">http://www.cadml.org</a> je montre comment générer ainsi des graphes de dépendances entre fichiers CAO, un peu sur le même principe que <a href="http://www.goulu.net/wordpress/wp-admin/Doxygen">Doxygen</a>.</li>
<li>En « programmant » directement le code SVG. En principe on peut le faire avec un simple éditeur de texte, mais il existe des éditeurs XML comme <a href="http://www.w3.org/Amaya/Amaya.html">Amaya</a> ou <a href="http://www.altova.com/products_ide.html">XML Spy</a></li>
</ol>
<h4>Programmation</h4>
<p><a href="http://www.svgbasics.com">http://www.svgbasics.com</a> contient tout ce qu’il faut savoir pour créer des fichiers SVG, mais c’est en anglais. En français il existe <a href="http://tecfa.unige.ch/staf/staf-g/sierra/staf2x/sitesvg.htm">ce cours</a> qui est bien fait.</p>
<p><a href="http://blog.codedread.com/archives/2005/12/01/guide-to-deploying-svg-with-html">http://blog.codedread.com/archives/2005/12/01/guide-to-deploying-svg-with-html</a></p>
<h4>Références</h4>
<ul>
<li><a href="http://svgfr.org">http://svgfr.org</a> et <a href="http://www.svg.org">http://www.svg.org</a></li>
<li><a href="http://marc.lauffer.free.fr/article.php3?id_article=23">Comment intégrer du svg dans un article spip</a></li>
<li><a href="http://www.latenightpc.com/blog/archives/2006/01/13/embedding-svg-in-wordpress-posts" target="_blank">Embedding SVG in WordPress posts</a></li>
</ul>
<p> </p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
