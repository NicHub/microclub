---
title: "Picasa et la reconnaissance faciale"
date: "2012-01-18T20:46:00"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["google", "photos", "securite", "software", "tags", "web"]
url: "/2012/01/18/picasa-et-la-reconnaissance-faciale/"
wordpress_id: 692
comment_count: 4
---
# Mise en route

Picasa est un gestionnaire d’image gratuit, produit par Google. On peut le télécharger facilement et l’installer sur son PC (<http://picasa.google.fr/>). J’avoue ne l’utiliser qu’occasionnellement, à cause de sa lourdeur en terme de charge et sa prise en main style « prison dorée ». Le produit a un lien fort avec le WEB – c’est un euphémisme que de le dire, venant d’un des acteurs majeur de la blogosphère. Mais ses puissantes fonctionnalités, telles que organisation, retouche photo sont très intéressantes (et gratuites ;-). Mais ici, je ne vous parlerai que de la fonction de reconnaissance faciale, disponible dès fin 2008 mais seulement en version anglaise, elle a évolué en un outils performant dans la version 3.9. Pour plus de précisions sur cette fonctionnalité:  <http://support.google.com/picasa/bin/answer.py?hl=fr&answer=156272>

# Une technologie puissante

En quoi consiste-t-elle, cette reconnaissance faciale? Il s’agit de détecter des visages dans des photos numériques, puis, par classification de traits morphologiques, lui attribuer un nom. C’est dit en 2 phrases, mais penser à la puissance de calcul d’analyse, de tri, de détection qu’il faut rien que pour savoir dans une image de 2 à 15 méga pixels si c’est bien un tête à laquelle on a affaire? Si c’est l’analyse d’une série de portraits ce serait encore raisonnable. Mais dans les milliers de photos qui gisent sur le disque d’un PC personnel, parmi les paysages, les décors, les sites et j’en passe! Une tête peut bien faire partie d’une photo de groupe que d’un portrait posé, avec des possibilités de zoom allant du cadrage photo-passeport, à la prise de Madame devant un site dont la beauté s’ajoute à celle du sujet, à la photo d’un groupe hétérogène…

La tête détectée, il s’agit encore de savoir si les traits du visage appartiennent à un profil donné. Ces traits pris bien sûr dans des conditions de lumière aussi variables qu’un contre-jour photogénique, un trois-quart, voire éclairé en face par un flash. De plus le sujet peut avoir changé de coupe de cheveux, mis un couvre-chef, des lunettes! ça semble une mission impossible. Et pourtant, Picasa le fait. Mais voyons comment.

Activée, la fonction de reconnaissance faciale scanne les images de votre disque, en arrière plan. Avant de laisser démarrer le scan, il vaut mieux limiter le champ d’action à Picasa. Sans quoi, tout le disque y passe. Si comme moi vous avez des montages de photos et des copie de sites WEB, il va vous les trouver à triple! Ceci se fait par « Outils – Gestionnaire de dossier ». Ensuite, l’analyse se passe: il y en a pour des heures, avec un CPU 2 Core, dont un quasi utilisé pour Picasa.[![CPU load](/media/2012/01/CPU-load.jpg "CPU load")](/media/2012/01/CPU-load.jpg)

Après un certain temps, un bon quart d’heure, Picasa commence à vous proposer des visages. Dès lors, vous pouvez leur coller un nom et plus : adresse email, coordonnées, compte de blog, etc. Pour faire simple, le nom suffit a valider la fiche. Dès que Picasa en trouve de nouvelles instances, il les propose avec deux coches : OK, pas OK.

Il a fallut 3 heures pour parcourir l’ensemble de mes photos: 17 Go, 13’000 fichiers dans 543 dossiers.

## Précision de la détection

Il faut l’avouer, la détection dans des conditions de lumière fort diverses fonctionne de manière impeccable. Jugez-en plutôt (désolé si il y a souvent mon portrait, mais c’est pour éviter une fuite WEB incontrôlable côté famille). Il n’y a aucune comparaison – en parlant des pixels entre les conditions de lumière et formes présentées ici:[![Yves lumiere](/media/2012/01/Ex_Yves_lumiere.jpg "Ex_Yves_lumiere")](/media/2012/01/Ex_Yves_lumiere.jpg)

Et à des âges différents, est-ce que ça fonctionne? et de côté? Mais oui!

[![Yves selon age](/media/2012/01/Ex_Yves.jpg "Yves selon age")](/media/2012/01/Ex_Yves.jpg)

Sur la photo bas, à gauche, j’ai 26 ans, une moustache des cheveux mi-longs (et noirs!) pris légèrement en plongée. De plus, ma fille masque un peu le visage: il est pourtant reconnu.

# Reconnaissance de paternité ?

Avant de cliquer OK (ou non), il est intéressant de voir ce que Picasa propose. Avec mon petit-fils Jérémie, il vient souvent son père: Anh-Cat. Picasa prend donc en compte la possibilité d’avoir des images anciennes, scannées dont la date de fichier ne correspond pas à la prise de vue.

[![](/media/2012/01/Ex_Je_AnhCat_comp.jpg "Ex_Je_AnhCat_comp")](/media/2012/01/Ex_Je_AnhCat_comp.jpg)

Dans les quelques photos que j’ai du père de Anh-Cat (donc le beau père de ma fille, vous suivez?), il était proposé comme premier choix en tant que « Anh-Cat ». Même scénario entre mon fils Jonathan et moi:

[![](/media/2012/01/Ex_Jo_Yves_comp.jpg "Ex_Jo_Yves_comp")](/media/2012/01/Ex_Jo_Yves_comp.jpg)

J’apparais dans le deuxième et dernier choix. D’où la réaction de ma femme: est possible qu’il y ait des traits et des ressemblance si frappantes? Il faut avouer que, sur plusieurs cas, c’est surprenant de précision.

## Le contexte et le nommage

En regardant un peu profondément, on s’aperçoit que Picasa a un choix limité de personnes: celles que vous voulez bien reconnaître, en en les ayant en nombre de représentation sur votre disque dur. De plus, j’ai pris le plis de nommer mes photos. Plutôt que IMG_449.JPG, elle ont le n°, puis le nom raccourci des acteurs présents et le lieu ou le contexte. Ce n’est donc pas impossible que Picasa se base sur ces patterns de caractères pour s’aider à la détection. En outre, dans des photos familiales, qu’y trouve-t-on? des gens de la famille, bien sûr.

## Contre exemple

Or donc, la théorie de la paternité imaginée par mon épouse au vu des premiers résultats va vite être réfutée. Pour cela, il faut aller dans la liste des **visages non reconnus**. Sur mon PC, il y en a environ 12’000; ceci est dû notamment à mes activités associatives ou apparaissent nombre d’images de groupe, avec des enfants sourds et leur fratrie. En voici un, avec un sympathique ressortissant du continent africain, par ailleurs père d’un enfant sourd et faisant partie – comme moi – de l’ASPEDA (<www.aspeda.ch>):

[![](/media/2012/01/Contre-exemple.jpg "Contre-exemple")](/media/2012/01/Contre-exemple.jpg)

On voit dès lors que Picasa pioche dans les registres connus… Sans se soucier trop de la ressemblance, ni de race (un africain, un européen, un asiatique!)

Plus amusant, ce vitrail, qui en lieu et place du Christ, propose… (je ne le dirait pas!)

[![Jesus](/media/2012/01/Jesus.jpg "Jesus")](/media/2012/01/Jesus.jpg)

Toujours est-il qu’un visage a été reconnu dans la photo! Dès lors, on peu fortement douter de la précision d’un système d’authentification basé sur la reconnaissance faciale, tel que décrit ici: <http://www.clubic.com/univers-mac/actualite-467310-apple-songerait-deverrouillage-reconnaissance-faciale.html> .

# Conclusion

Forcément provisoire… Picasa permet de faire une collection de portrait d’un personne souvent photographiée pour en faire un montage, un petit film, ou un quiz: où était-ce? Le machines puissantes et multiple-cores d’aujourd’hui permettent ce qui – il y a quelques années, semblait tenir de la science-fiction. Avec bien sûr, des dérives à la clef dès que ça file sur le WEB. Picasa le propose bien sûr en lien avec Goggle+. Associé avec la géolocalisation, Big Brother n’est plus très loin… Cette technologie est possible également avec d’autres logiciels (<http://www.softonic.fr/s/reconnaissance-faciale> ), pas essayé.

Autres liens en relation:

<http://webster.e-monsite.com/home/nouvelles-de-l-informatique/la-reconnaisance-faciale-arrive-sur-google.html>

<http://www.lesnumeriques.com/allemagne-brider-reconnaisance-faciale-facebook-n20471.html>

Yves Masur

## Commentaires

### Jacques — 19 janvier 2012 à 11:41

Pour info : les mêmes fonctionnalités existent dans le logiciel « Galerie de photos Windows Live » fourni gratuitement par Microsoft.

D’autre part, il me semble mieux intégré à Windows et ne crée pas de base de données séparée. Toutes les infos sont intégrées au fichier image. On les retrouve lorsqu’on copie l’image sur un autre PC.

Combiné avec le logiciel de courriergratuit Windows Live Mail, il offre la possibilité d’envoyer un très joli mail photos pouvant contenir un grand nombre de photos sous forme de vignettes. Le transfert des photos sur un serveur est automatique. Cela permet de n’avoir qu’un message relativement léger. Il est possible d’afficher les images sous forme d’un diaporame, et, pour autant que l’expéditeur ait donné son accord, de télécharger les images à leur définition d’origine.

### Goulu — 25 janvier 2012 à 18:03

Il commence bien, ton article, mais il a pas l’air fini… T0aurais pas publié le brouillon des fois ?

### ymasur — 25 janvier 2012 à 19:40

[@Goulu](#comment-365)\
Bizarre, en effet! je n’ai pas bien compris ce qui c’est passé. Il était prêt, et j’attendais l’accord de ma fifille et son mari, vu que sa bobine y figure avant de le publier. Et j’ai juste modifié son état! Heureusement, en récupérant la version prête, ça semble OK. Merci du signalement.

### gravacolecaracole — 24 décembre 2012 à 11:54

Logiciel bluffant, mais efficace.\
Actuellement sur Ubuntu, voilà toute une nuit qu’il scanne à ma grande surprise avec une efficacité remarquable.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
