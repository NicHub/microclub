---
title: "redirection conditionnelle en JavaScript"
date: "2008-01-12T17:03:58"
lastmod: "2015-04-24T23:20:22"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation", "web"]
url: "/2008/01/12/redirection-conditionnelle-en-javascript/"
wordpress_id: 31
comment_count: 1
---
Je remonte un peu le temps pour vous expliquer le problème:

1. En même temps que mon domaine [goulu.net](http://goulu.net), j’avais acheté un hébergement web pas cher auprès d’une boite lointaine, ce qui m’avait permis de créer de nombreuses versions de mon site internet.
2. Lorsque j’ai créé mon blog [drgoulu.wordpress.com](/2008/01/12/redirection-conditionnelle-en-javascript/http;/drgoulu.wordpress.com), hébergé gratuitement sur le génial wordpress.com , j’ai créé sur mon ancien hébergement une redirection HTTP toute simple en créant un fichier index.php contenant simplement ces lignes:\
    \<code\>\<?\
    Header( "HTTP/1.1 301 Moved Permanently" );\
    Header( "Location: <http://drgoulu.wordpress.com/>" );\
    ?\>\</code\>\
    ce qui redirigeait les accès à l’ancien site vers le nouveau blog.
3. J’ai cependant conservé mon contrat d’hébergement car j’avais besoin d’un serveur e-mail @goulu.net
4. Pour différentes raisons, j’ai acheté d’autres noms de domaine comme [pro-g.ch](http://pro-g.ch) et [projets.ch](http://projets.ch), et un hébergement chez [infomaniak.ch](http://infomaniak.ch), qui permet de définir des domaines « synonymes » : plusieurs domaines peuvent ainsi partager le même site web.

A ce moment, je me suis dit que j’allais pouvoir économiser mon vieil hébergement si j’arrivais :

1. à définir goulu.net comme un nouveau synonyme de l’hébergement chez infomaniak, ce qui me permet de plus de recevoir tous mes mails sur un seul compte au lieu de 2
2. à réaliser un « redirection conditionnelle » pour que les gens qui tapent [www.goulu.net](http://www.goulu.net) continuent à se retrouver sur mon blog au lieu de tomber sur mon site [pro-g.ch](http://pro-g.ch) en construction.

Petite contrainte supplémentaire, je voulais éviter de faire ça en PHP pour ne pas interférer avec le système existant sur pro-g. Par chance, infomaniak a bien configuré ses serveurs : s’il existe un document nommé index.html, il a la priorité sur index.php. Donc il m’a suffit de faire un fichier index.html contenant un peu de JavaScript :

\<code\>\<html \>\
\<head\>\
\<title\>goulu.net redirect page\</title\>\
\</head\>\
\<body\>\
\<script language="JavaScript" type="text/javascript"\>\
\<!--\
var d="<http://projets.ch/index.php";\>
var p=document.URL;\
if (p.indexOf("goulu.net") != -1) d="<http://drgoulu.wordpress.com/";\>
window.location.replace(d);\
--\>\
\</script\>\
\</body\>\
\</html\>\</code\>

ça marche, et ça donne des pistes sur comment faire un système de redirection assez sophistiqué grâce à JavaScript, un langage incontournable du Web, souvent sous-estimé.

## Commentaires

### ysengrimus — 16 juillet 2009 à 12:31

Quel type de blogue êtes-vous? Voici la typologie:

<http://ysengrimus.wordpress.com/2009/07/15/typologie-des-carnets-blogues-electroniques/>

Merci.\
Paul Laurendeau

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
