---
title: "Fabrication de prototypes PCB mon marché, finition avec une CNC"
date: "2017-04-16T21:30:54"
lastmod: "2017-04-21T23:01:21"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["circuit-imprime", "cnc", "decoupe", "fusion", "fusion-360", "pcb", "seeedstudio"]
url: "/2017/04/16/fabrication-de-prototypes-pcb-mon-marche-finition-avec-une-cnc/"
wordpress_id: 3205
comment_count: 3
---
Nous avons récemment découvert que le shop en ligne « Seeedstudio » offrait la fabrication de circuits imprimés aux dimensions de 100x100mm pour la somme modique de \$9.90 pour 10 circuits (19.80 avec livraison). Il était donc intéressant de passer commande d’un circuit que je n’aurais pas fabriqué sans avoir un prix très attractif.

**Dessin et commande du circuit :**

Je me lance donc dans un dessin avec le logiciel CAO Eagle (Autodesk), la version limitée à 100x180mm est gratuite pour les utilisations non-professionnelles.

![](/media/2017/04/word-image.png)   ![](/media/2017/04/word-image-1.png)

Mon projet est un interrupteur basé sur un module Wifi ESP8266, un relai et un module 230V/5V ([schéma](/media/2017/04/schema.png)).

Circuit 2 couches, je vais dessiner des fentes pour mettre le circuit aux normes concernant la tension 230V.

Avant d’envoyer les fichiers au fabricant, je vérifie le contenu avec « gerbv », un logiciel gratuit qui permet de visualiser les couches du circuit.

![](/media/2017/04/word-image-2.png) ![](/media/2017/04/word-image-3.png)

Le site de commande en ligne de Seeedstudio et d’autres fabricants tels que Eurocircuits permettent également d’effectuer cette vérification en ligne avant de passer la commande, ce qui est très pratique et évite des surprises. Une fois satisfait du contrôle visuel, j’envoie les fichiers gerber (zip) au fabriquant.

**Livraison:**

Il ne reste plus qu’à attendre la livraison. Attente un peu longue (4 semaines), mais finalement les 10 circuits arrivent et sont d’un état très acceptable.

![2017-04-13 11.53.26.jpg](/media/2017/04/2017-04-13-11-53-26-jpg.jpeg)

A première vue tout va pour le mieux, les circuits sont propres et correspondent exactement à mon attente. Il ne me reste plus qu’à découper les circuits au format circulaire et avec des entailles pour isoler les pistes 230V. Faire effectuer cette opération aurait juste fait exploser le prix de l’offre, raison pour laquelle je décide d’effectuer cette étape dans mon petit atelier. Vu le nombre de circuits, je vais utiliser ma petite CNC.

**Découpe du circuit :**

Pour la découpe sur la CNC , j’ai dessiné les contours et fentes dans la couche CAM du logiciel Eagle. Une fonction d’Eagle permet de convertir cette information en format dxf. Ces données doivent maintenant être transformées en commandes pour ma machine (CNC), ceci se fera au moyen d’un logiciel CAO mécanique.

Autodesk a publié dernièrement le nouveau logiciel **« Fusion 360** ». Ce logiciel permet la création d’objets 2D et 3D et la génération des fichiers CAM pour une CNC ou pour imprimantes 3D. J’utilisais auparavant divers logiciels, chacun dans un but bien précis, chacun avec des commandes spécifiques ce qui compliquait passablement le travail. D’après la description de « Fusion 360 » je dois pouvoir remplacer tous ces logiciels par ce dernier (fraisage, contournage, perçage) ce qui devrait me simplifier passablement le travail dans l’avenir! Mon petit projet est donc idéal pour apprendre à utiliser et à tester « Fusion 360 ».

**Fusion 360:**

La prise en main est plutôt facile si l’on a déjà utilisé des outils CAO auparavant. L’équipe d’Autodesk nous fournis une aide précieuse en tutoriels « YouTube » et en articles en ligne. Le logiciel contient divers modes, l’un pour dessiner et modéliser, l’autre pour générer les données pour la machine qui effectuera le travail (CNC ou autre).

**En mode Modèle**, j’importe les données de la CAO Eagle au moyen du fichier « dxf » que j’attribue à l’axe Z. De cette façon, le plan du dessin est perpendiculaire à l’axe de travail des outils. Il faut maintenant définir la surface exacte à découper et la largeur des ouvertures (fentes) dans le circuit *(Je désire contourner le circuit avec une forme circulaire qui rentre dans le boitier d’un interrupteur mural et de tailler des fentes d’isolation pour la partie courant fort).*

![](/media/2017/04/word-image-4.png)

Vue du logiciel Fusion 360 et des données du fichier «dxf» importées. Il ne reste qu’à ajuster les éléments graphiques.

*Remarque : Avant d’envoyer les fichiers, j’ai ajouté 4 trous qui me permet de centrer le circuit sur ma CNC, en fait il n’en faut que 2, un premier trou comme point de référence (zéro) et un deuxième pour l’orientation dans l’axe x/y. Ces 2 trous sont visibles sur l’image ci-dessus.*

**Opérations en mode 2D**

1. La fonction « Slot » me permet de donner une largeur aux fentes à fraiser (image de gauche). Je choisis une largeur de 1.5mm correspondant à un outil en stock et je suis les lignes déjà présentes.
2. Il me reste à ajuster les contours et à corriger les lignes non contigües (image de droite), le travail en mode dessin 2D est terminé.

![](/media/2017/04/word-image-5.png) ![](/media/2017/04/word-image-6.png)

La fonction « extrusion » me permet de donner du volume à mon circuit, j’obtiens ainsi le modèle exact de la forme à découper.

![](/media/2017/04/word-image-7.png)    ![](/media/2017/04/word-image-8.png)

A gauche: Les traits continus permettent de délimiter automatiquement la surface.

A droite: Après extrusion on voit le volume de la pièce. La surface supérieure du circuit est définie comme niveau zéro (Z=0). Avec un Z\>0 on éloigne l’outil de la pièce, avec un  Z négatif, on taille dans la pièce.

**Étapes de fabrication**:

Je prévois la découpe en 3 étapes :

1. Perçage de 2 trous de référence (3mm) dans la plaque martyre de la CNC: (sans circuit), ces trous dans le bois solidaire à la machine me permettent d’y planter 2 tiges de 3mm et d’aligner chaque circuit.
2. Avec l’aide des 2 tiges, fixer un circuit sur le martyre (avec du ruban autocollant double face)
3. Lancer le programmer de découpe (J’utilise la même largeur d’outil pour les fentes et pour le contournage, ce qui m’évite de changer d’outils à chaque circuit).
4. Je répète l’opération 2 et 3 pour les circuits suivants.

Suite à la création du modèle 3d (dessin ci-dessus) et à la définition de chaque étape de fabrication, je bascule en mode CAM dans Fusion 360.

**Mode CAM dans Fusion :** Dans ce mode, il existe de multitudes de possibilités de générer des donnes CAM

Il me faut :

1. Drill (perçage)
2. Slot (fentes)
3. Contour (détourage de la pièce)

Les données pour le perçage iront dans un premier fichier utilisé qu’une seule fois, les données pour l’étape 2et 3 iront dans un 2\<sup\>ème\</sup\> fichier utilisé pour chaque circuit. Le logiciel permet de visualiser le déplacement de l’outil (simulation) ce qui me rend plus confiant quand à l’exécution du travail.

![](/media/2017/04/word-image-9.png)    ![](/media/2017/04/word-image-10.png)

Affichage et simulation du perçage et du découpage. On peut distinguer en grisé la tête de la fraisage et l’outil qui sont définis dans les paramètres outils de « Fusion ».

Le logiciel Fusion 360 contient déjà toutes les fonctions pour la génération du fichier à charger sur la machine, entre autres la définition d’un magasin d’outils et les paramètres pour diverses machines CNC, cette phase est la plus difficile à réaliser vu le nombre de paramètres et le vocabulaire utilisé qui m’est inconnu. Sur ma petite CNC, j’utilise le logiciel « MACH3 ». Ce logiciel faisant partie des interfaces supportées par « Fusion » je ne suis donc pas trop inquiet.

![](/media/2017/04/word-image-11.png)

Exemple de fichier CNC, on y reconnait les commandes (G-Code) qui vont piloter la CNC.

Il me faudra plusieurs itérations entre la CAO et la machine avant de lancer la première découpe. Les premiers essais se font sans outils et sans matière. A ma surprise, les déplacements se font correctement, il n’y a qu’a modifier le paramètre pour la vitesse de déplacement horizontale de l’outil et à enlever un mystérieux code G28 qui semble envoyer la CNC hors limites en fin de programme. L’apprentissage de cette dernière étape me sera utile pour d’autres projets.

**Travail sur la machine (CNC).**

[![2017-04-15 14.13.36.jpg](/media/2017/04/2017-04-15-14-13-36-jpg-e1492374817839-225x300.jpeg)](/2017/04/16/fabrication-de-prototypes-pcb-mon-marche-finition-avec-une-cnc/2017-04-15-14-13-36-jpg/)     [![2017-04-15 14.14.13.jpg](/media/2017/04/2017-04-15-14-14-13-jpg-e1492374795275-225x300.jpeg)](/2017/04/16/fabrication-de-prototypes-pcb-mon-marche-finition-avec-une-cnc/2017-04-15-14-14-13-jpg/)

1. Perçage des trous de référence                    2. Ajustement du circuit sur la machine (martyre)

![2017-04-15 13.47.17.jpg](/media/2017/04/2017-04-15-13-47-17-jpg.jpeg)   ![2017-04-15 14.18.56.jpg](/media/2017/04/2017-04-15-14-18-56-jpg.jpeg)

3\. Circuit après découpe.                                                                       4. Circuit nettoyé

Suit le nettoyage, enlever les bavures et les restes de ruban double face.

**J’ai finalement traversé toute la chaine des outils depuis le dessin jusque à la pièce découpée.**

![2017-04-14 00.01.56.jpg](/media/2017/04/2017-04-14-00-01-56-jpg.jpeg)

Dernière étape, souder les composants et mise sous tension.\
**Tout a fonctionné du premier coup !!!**

Rolf Ziegler (4/2017)

## Commentaires

### franic — 17 avril 2017 à 09:30

Superbe réalisation, très intéressant de voir toute la chaîne entre le dessin de PCB jusqu’au montage final. Cela peut paraître simple, mais il y a plusieurs étapes pas toujours faciles à passer ! Bravo et en plus cela fonctionne du premier coup !

### Yves Masur — 17 avril 2017 à 21:28

Excellent tuto pour se rendre compte des étapes!\
Question: as-tu prévu un connecteur pour (re-) programmer le CPU ESP8266?

### Rolf Ziegler Auteur de l’article — 17 avril 2017 à 22:33

Le module ESP8266 est sur un socle pour la première programmation et pour le dépannage, par contre on peut le programmer par wifi une fois le code ESPEasy installé.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
