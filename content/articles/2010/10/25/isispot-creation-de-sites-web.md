---
title: "IsiSpot – création de sites WEB"
date: "2010-10-25T09:43:48"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation", "site", "web"]
url: "/2010/10/25/isispot-creation-de-sites-web/"
wordpress_id: 338
comment_count: 0
---

## IziSpot – le must?

Suite à l’excellente présentation des frères Francey sur ce sujet,  je télécharge le produit: IziSpot 4.3.1, l’installe sans problème. Juste une chose étrange, W7 me demande à chaque lancement si ce logiciel peut modifier les données de l’ordi – je suppose que c’est un soft encore au style XP; bien que les données se trouvent dans les paramètres utilisateur. Puis je me lance dans l’édition d’un site comportant 3 pages:

- accueil, logo des sponsors
- info, tableau avec des liens
- contact, avec formulaire

## Édition des pages

La première chose est de faire son layout, très bien indiqué comme « charte graphique »: image, logo, menus, couleurs de fond. Ceci est facilité en observant des modèles, forts nombreux; voir en en prenant un pour le modifier – ce que je fait.

Une fois la page d’accueil construite, pour me simplifier la vie je la **copie**, en vue d’avancer la page « info ». Mal m’en prend… la page d’accueil est spéciale, reconnue comme tel. Après une heure d’essais de toute sorte, qui me font passer en revue tous les menus, je fini par voir que la page d’accueil et/ou sa copie ne peuvent pas être supprimée. L’ édition de la copie trouble IziSpot! En effet, le contenu est différent et présenté par l’environnement correctement, mais le test avec le browser montre 2 x la page d’accueil initiale.

Heureusement, le fichier .IZI qui contient l’ensemble du site et les paramètres peut être facilement sauvé, copié et numéroté pour en avoir une version. Même si l’environnement semble assez solide (mis a rude épreuve avec mes essais!), il vaut mieux sauver souvent, il n’y a pas de « undo ». Sans en avoir la certitude, il semblait que les éléments qui composent cet environnement est basé sur des web-services. Vu avec l’excellent « Process Explorer », on peut voir sans ambiguïté que des instances de Explorer sont actives dès qu’on édite.

[![](/media/2010/10/izi-menu.png "izi-menu")](/media/2010/10/izi-menu.png)

On voit dans ce menu mes copies malheureuses de la page d’accueil, renommée en information-old. Pour finir, j’ai refait une « Info » depuis la page blanche. Par contre je n’ai pas eu besoin de remettre les éléments (tableau, images, liens) depuis zéro. En effet, en copiant le HTML de la page informations-old, la nouvelle page « Info » a tout repris!

Certes, cet environnement est au départ un peu déconcertant. Il ne faut pas confondre le nom de la page IziSpot, le nom de la page WEB telle qu’affichée dan le browser et le nom dans le menu cliquable. Cliquer sur une des pages (active ou non) lance l’édition wisiwig, confortable et bien pensée.

La manipulation de tableau est – comme dans nombre de concurrent – dépendante du contexte; par contre, on sait particulièrement bien si on s’adresse au tableau dans son entier ou une cellule, ou un groupe de cellules sélectionnées. On peut aussi agir directement dans le HTML, voir intégrer des script. Pour ce faire, le nom de la page WEB pourra obtenir l’extension .php, ou . asp.

Créer un formulaire est très simple: on détermine les champs, indiquant ceux qui sont obligatoires et la page de retour. Par contre, il faut savoir que l’émail passera par le site izisoftware.com:\
\<code\>\
if (err==1) {alert (erreur)} else {document.envoi.action='<http://users.izisoftware.com/Sharing/Form/Default.aspx';document.envoi.submit()}\></code\>

![](/Users/Yves/AppData/Local/Temp/moz-screenshot-1.png)

![](/Users/Yves/AppData/Local/Temp/moz-screenshot.png)

## Organisation du site

L’organisation des pages via le menu, (icône clef 6 pans) est également très facile à utiliser:

[![](/media/2010/10/izi-pages-position.png "izi-pages-position")](/media/2010/10/izi-pages-position.png)

Des flèches permettent de déplacer la page; également dans une arborescence (max 4 niveaux). Depuis ce menu, on peut également changer de charte graphique par page.

## Mise en ligne

Elle est facilitée par un interface ftp, qui permet de garder les nom et password associés au projet. Un fenêtre montre les commandes ftp et un ascenseur indique la progression. En option, le fichier .izi peut également être déposé sur le serveur à titre de sauvegarde. Bien entendu, il est possible de tout relire le code généré. Par contre, il faut résister à la tentation de le modifier, car à la prochaine mise à jour, les corrections seront perdues!

Heureusement, l’option « mise à jour partielle » permet de ne renvoyer sur le site de production que les fichiers touchés, ce qui permet une accélération de la mise à jour d’un site qui devient complexe et plus lourd au fil du temps. L’édition wisiwig et la prévisualisation via browser (choix entre IE et Firefox) permet de finaliser les pages avant leur mise en ligne.

Qu’en est-il de la conformité du code généré? Il y a forcément pas mal de javascript pour lier et faire fonctionner le tout. Avec le site à 3 pages ([www.giron2011.ch](http://www.giron2011.ch "Giron2011")) la validation indique 16 erreurs. Elle concerne des balises unique qui devraient être fermées, tel que, ou des tirets excédentaires dans des commentaires. Des images n’ont pas de « alt ». Pas de quoi en faire un drame…

## Conclusion (provisoire)

Cet environnement – gratuit!! l’option pour un site marchand est seule payante – mérite attention. Il est en progression constante, si l’on en juge le forum très vivant. Et ce qui pas désagréable, énormément d’efforts en français et pour les langues en général sont faits. Il soutient sans rougir la comparaison avec des outils bien plus complexes et onéreux. Une fois passé l’obstacle (mais est-ce évitable?) des menus et génération de fichiers, il est rapide et agréablement efficace.

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
