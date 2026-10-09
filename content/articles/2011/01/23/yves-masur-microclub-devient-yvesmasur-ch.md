---
title: "yves.masur.microclub devient yvesmasur.ch"
date: "2011-01-23T18:39:33"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["mysql", "non-classe", "php", "programmation", "site", "software", "unix", "web"]
url: "/2011/01/23/yves-masur-microclub-devient-yvesmasur-ch/"
wordpress_id: 413
comment_count: 2
---
Bouger son site perso est une entreprise… pas facile. Surtout si l’on pas d’échéance: on bricole une heure par-ci, par-là en laissant un chantier terrible. Mais par le fait que le site du Microclub, que j’utilisais comme sous domaine depuis (au moins) 2004 a changé d’hébergeur, je me suis retrouvé dans l’obligation d’accélérer le mouvement!!

Pourquoi pas une simple page de redirection? Surtout que l’ancienne structure est toujours visible. Il suffit de connaitre le nom du site principal ([www.scdi.org](http://www.scdi.org "SCDI")) et le nom « UNIX » de l’utilisateur. Par exemple, l’ancienne structure du microclub visible ici:  <http://www.scdi.org/~microclub/> et vous pouvez toujours consulter nos anciennes news (pas trop fraîches!) etc! Alors donc, j’aurai pu me contenter de mettre une page de redirection sur ma structure. Las! Sur l’hébergeur Infomaniak, il n’est pas possible d’indiquer une redirection avec un sous-sous domaine, avec deux points dans l’URL.

Pire, comme le site <www.microclub.ch> est maintenant motorisé par WordPress, pas moyen d’avoir un petit bout d’arborescence, comme <www.microclub.ch/**monsite>**. En effet, WordPress pratique l’URL rewrite: tout ce qui est après le « .ch »  renvoie à un article. Essayez [http://microclub.ch/truc](/truc "truc") pour vous faire une idée.

Bon, je fignole le transport des fichiers sur ma nouvelle adresse. Et viennent les problèmes d’update.

**Problème de POST**

Une fois les pages copiées, un test me montre que les POST ne fonctionnent pas. En fait, sur le site de SCDI, des variables PHP sont définies, probablement au niveau de Apache:

- \$PHP_SELF
- \$SCRPT_NAME
- \$HTTP_HOST

Mais pas sur le nouveau, hébergé par BigHosting. Pour tester le comportement, j’ai un script ici: <http://www.scdi.org/~ymasur/tests/php/web-path.php> et copié ici: <http://www.yvesmasur.ch/tests/php/web-path.php> et là, on voit bien que les variables en question sont vides.

Pas d’autre solution que de modifier les scripts en recherchant une technique propre pour initialiser ce qu’il faut. Le pire est ma page admin, qui se transforme en un gouffre: plus de login/password pour accéder à l’interface! l’horreur…

Même ceci réparé, je constate que le script limitant la durée en enregistrant l’IP et date, heure ne limite rien du tout… Il faut que le fichier qui l’enregistre aie les droits rw-rw-rw (666 pour les intimes à UNIX).

**Problème de DB**

Et la base de donnée? Le plus simple est de copier par un fichier SQL, via l’interface PHPMyAdmin, et de le pousser sur le nouveau site. Et ça marche. Il faut bien sûr changer le fichier de config qui initialise les données de DB, Tables, User, Password pour y accéder.

Mais voilà, les références des liens indiqués dans les news sont faux! La correction est de tout effacer, modifier au niveau texte dans le fichier SQL, et rebalancer le tout. Voilà que l’accès à la DB m’interdit de sucrer les tables! Je dois donc travailler via l’interface « officiel » de BigHosting pour pouvoir effacer la DB. Et importer le fichier SQL. Mais là, on me demande l’encodage qui par défaut est UTF-8. Hé bien ce n’est pas le bon, d’après le résultat ou chaque news s’arrète au premier apostrophe. Rebelote pour effacer et importer…

**Conclusion**

Il n’y a rien de neuf sur mon site, mais il va plus vite! Il reste toutefois quelques petits problèmes de lien cassés. Et de fonctionnalités que je ne vais pas m’amuser à reproduire.

## Commentaires

### Karim El Khalifa — 26 janvier 2011 à 23:09

En fait wordpress gère très bien les URL comme <http://www.microclub.ch/monsite>\
grâce aux commandes magiques\
RewriteCond %{REQUEST_FILENAME} !-f\
RewriteCond %{REQUEST_FILENAME} !-d\
présente dans le fichiers .htaccess\
qui indique à l’url rewriting qu’il faut appliquer le rewriting que si les fichiers n’existent pas physiquement sur le serveur.\
C’est pour ça que [http://www.microclub.ch/truc](../../../../truc.html) qui n’existe pas donne une page par défaut mais que les fichiers javascript et CSS de la page peuvent se charger.\
Par exemple, le fichier jQuery à l’adresse [http://microclub.ch/wp-includes/js/jquery/jquery.js?ver=1.4.2](../../../../wp-includes/js/jquery/jquery1159.js?ver=1.4.2)\
Donc ça aurait été possible.\
De plus chez infomaniak, il est possible de faire des sous-domaines comme yves-masur.microclub.ch qui pointe dans le dossier yves-masur.

### Yves Masur — 28 janvier 2011 à 20:22

Merci pour ces infos détaillées! Par contre, impossible de mapper mon ancienne url: il y avait **deux** points!!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
