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
<p>Nous avons récemment découvert que le shop en ligne « Seeedstudio » offrait la fabrication de circuits imprimés aux dimensions de 100x100mm pour la somme modique de $9.90 pour 10 circuits (19.80 avec livraison). Il était donc intéressant de passer commande d’un circuit que je n’aurais pas fabriqué sans avoir un prix très attractif.</p>
<p><strong>Dessin et commande du circuit :</strong></p>
<p>Je me lance donc dans un dessin avec le logiciel CAO Eagle (Autodesk), la version limitée à 100x180mm est gratuite pour les utilisations non-professionnelles.</p>
<p><img height="324" src="/media/2017/04/word-image.png" width="343"/>   <img height="323" src="/media/2017/04/word-image-1.png" width="336"/></p>
<p>Mon projet est un interrupteur basé sur un module Wifi ESP8266, un relai et un module 230V/5V (<a href="/media/2017/04/schema.png">schéma</a>).</p>
<p>Circuit 2 couches, je vais dessiner des fentes pour mettre le circuit aux normes concernant la tension 230V.</p>
<p>Avant d’envoyer les fichiers au fabricant, je vérifie le contenu avec « gerbv », un logiciel gratuit qui permet de visualiser les couches du circuit.</p>
<p><img height="331" src="/media/2017/04/word-image-2.png" width="327"/> <img height="314" src="/media/2017/04/word-image-3.png" width="340"/></p>
<p>Le site de commande en ligne de Seeedstudio et d’autres fabricants tels que Eurocircuits permettent également d’effectuer cette vérification en ligne avant de passer la commande, ce qui est très pratique et évite des surprises. Une fois satisfait du contrôle visuel, j’envoie les fichiers gerber (zip) au fabriquant.</p>
<p><strong>Livraison:</strong></p>
<p>Il ne reste plus qu’à attendre la livraison. Attente un peu longue (4 semaines), mais finalement les 10 circuits arrivent et sont d’un état très acceptable.</p>
<p><img alt="2017-04-13 11.53.26.jpg" height="698" src="/media/2017/04/2017-04-13-11-53-26-jpg.jpeg" width="930"/></p>
<p>A première vue tout va pour le mieux, les circuits sont propres et correspondent exactement à mon attente. Il ne me reste plus qu’à découper les circuits au format circulaire et avec des entailles pour isoler les pistes 230V. Faire effectuer cette opération aurait juste fait exploser le prix de l’offre, raison pour laquelle je décide d’effectuer cette étape dans mon petit atelier. Vu le nombre de circuits, je vais utiliser ma petite CNC.</p>
<p><strong>Découpe du circuit :</strong></p>
<p>Pour la découpe sur la CNC , j’ai dessiné les contours et fentes dans la couche CAM du logiciel Eagle. Une fonction d’Eagle permet de convertir cette information en format dxf. Ces données doivent maintenant être transformées en commandes pour ma machine (CNC), ceci se fera au moyen d’un logiciel CAO mécanique.</p>
<p>Autodesk a publié dernièrement le nouveau logiciel <strong>« Fusion 360</strong> ». Ce logiciel permet la création d’objets 2D et 3D et la génération des fichiers CAM pour une CNC ou pour imprimantes 3D. J’utilisais auparavant divers logiciels, chacun dans un but bien précis, chacun avec des commandes spécifiques ce qui compliquait passablement le travail. D’après la description de « Fusion 360 » je dois pouvoir remplacer tous ces logiciels par ce dernier (fraisage, contournage, perçage) ce qui devrait me simplifier passablement le travail dans l’avenir! Mon petit projet est donc idéal pour apprendre à utiliser et à tester « Fusion 360 ».</p>
<p><strong>Fusion 360:   </strong></p>
<p>La prise en main est plutôt facile si l’on a déjà utilisé des outils CAO auparavant. L’équipe d’Autodesk nous fournis une aide précieuse en tutoriels « YouTube » et en articles en ligne. Le logiciel contient divers modes, l’un pour dessiner et modéliser, l’autre pour générer les données pour la machine qui effectuera le travail (CNC ou autre).</p>
<p><strong>En mode Modèle</strong>, j’importe les données de la CAO Eagle au moyen du fichier « dxf » que j’attribue à l’axe Z. De cette façon, le plan du dessin est perpendiculaire à l’axe de travail des outils. Il faut maintenant définir la surface exacte à découper et la largeur des ouvertures (fentes) dans le circuit <em>(Je désire contourner le circuit avec une forme circulaire qui rentre dans le boitier d’un interrupteur mural et de tailler des fentes d’isolation pour la partie courant fort).</em></p>
<p><img height="951" src="/media/2017/04/word-image-4.png" width="1040"/></p>
<p>Vue du logiciel Fusion 360 et des données du fichier «dxf» importées. Il ne reste qu’à ajuster les éléments graphiques.</p>
<p><em>Remarque : Avant d’envoyer les fichiers, j’ai ajouté 4 trous qui me permet de centrer le circuit sur ma CNC, en fait il n’en faut que 2, un premier trou comme point de référence (zéro) et un deuxième pour l’orientation dans l’axe x/y. Ces 2 trous sont visibles sur l’image ci-dessus.</em></p>
<p><strong>Opérations en mode 2D</strong></p>
<ol>
<li>La fonction « Slot » me permet de donner une largeur aux fentes à fraiser (image de gauche). Je choisis une largeur de 1.5mm correspondant à un outil en stock et je suis les lignes déjà présentes.</li>
<li>Il me reste à ajuster les contours et à corriger les lignes non contigües (image de droite), le travail en mode dessin 2D est terminé.</li>
</ol>
<p><img height="384" src="/media/2017/04/word-image-5.png" width="233"/> <img height="261" src="/media/2017/04/word-image-6.png" width="398"/></p>
<p> </p>
<p>La fonction « extrusion » me permet de donner du volume à mon circuit, j’obtiens ainsi le modèle exact de la forme à découper.</p>
<p><img height="236" src="/media/2017/04/word-image-7.png" width="291"/>    <img height="237" src="/media/2017/04/word-image-8.png" width="386"/></p>
<p>A gauche: Les traits continus permettent de délimiter automatiquement la surface.</p>
<p>A droite: Après extrusion on voit le volume de la pièce. La surface supérieure du circuit est définie comme niveau zéro (Z=0). Avec un Z&gt;0 on éloigne l’outil de la pièce, avec un  Z négatif, on taille dans la pièce.</p>
<p><strong>Étapes de fabrication</strong>:</p>
<p>Je prévois la découpe en 3 étapes :</p>
<ol>
<li>Perçage de 2 trous de référence (3mm) dans la plaque martyre de la CNC: (sans circuit), ces trous dans le bois solidaire à la machine me permettent d’y planter 2 tiges de 3mm et d’aligner chaque circuit.</li>
<li>Avec l’aide des 2 tiges, fixer un circuit sur le martyre (avec du ruban autocollant double face)</li>
<li>Lancer le programmer de découpe (J’utilise la même largeur d’outil pour les fentes et pour le contournage, ce qui m’évite de changer d’outils à chaque circuit).</li>
<li>Je répète l’opération 2 et 3 pour les circuits suivants.</li>
</ol>
<p>Suite à la création du modèle 3d (dessin ci-dessus) et à la définition de chaque étape de fabrication, je bascule en mode CAM dans Fusion 360.</p>
<p><strong>Mode CAM dans Fusion :</strong> Dans ce mode, il existe de multitudes de possibilités de générer des donnes CAM</p>
<p>Il me faut :</p>
<ol>
<li>Drill (perçage)</li>
<li>Slot (fentes)</li>
<li>Contour (détourage de la pièce)</li>
</ol>
<p>Les données pour le perçage iront dans un premier fichier utilisé qu’une seule fois, les données pour l’étape 2et 3 iront dans un 2<sup>ème</sup> fichier utilisé pour chaque circuit. Le logiciel permet de visualiser le déplacement de l’outil (simulation) ce qui me rend plus confiant quand à l’exécution du travail.</p>
<p><img height="210" src="/media/2017/04/word-image-9.png" width="332"/>    <img height="212" src="/media/2017/04/word-image-10.png" width="331"/></p>
<p>Affichage et simulation du perçage et du découpage. On peut distinguer en grisé la tête de la fraisage et l’outil qui sont définis dans les paramètres outils de « Fusion ».</p>
<p> </p>
<p>Le logiciel Fusion 360 contient déjà toutes les fonctions pour la génération du fichier à charger sur la machine, entre autres la définition d’un magasin d’outils et les paramètres pour diverses machines CNC, cette phase est la plus difficile à réaliser vu le nombre de paramètres et le vocabulaire utilisé qui m’est inconnu. Sur ma petite CNC, j’utilise le logiciel « MACH3 ». Ce logiciel faisant partie des interfaces supportées par « Fusion » je ne suis donc pas trop inquiet.</p>
<p><img height="459" src="/media/2017/04/word-image-11.png" width="783"/></p>
<p>Exemple de fichier CNC, on y reconnait les commandes (G-Code) qui vont piloter la CNC.</p>
<p> </p>
<p>Il me faudra plusieurs itérations entre la CAO et la machine avant de lancer la première découpe. Les premiers essais se font sans outils et sans matière. A ma surprise, les déplacements se font correctement, il n’y a qu’a modifier le paramètre pour la vitesse de déplacement horizontale de l’outil et à enlever un mystérieux code G28 qui semble envoyer la CNC hors limites en fin de programme. L’apprentissage de cette dernière étape me sera utile pour d’autres projets.</p>
<p><strong>Travail sur la machine (CNC).</strong></p>
<p><a href="/2017/04/16/fabrication-de-prototypes-pcb-mon-marche-finition-avec-une-cnc/2017-04-15-14-13-36-jpg/" rel="attachment wp-att-3219"><img alt="2017-04-15 14.13.36.jpg" height="409" src="/media/2017/04/2017-04-15-14-13-36-jpg-e1492374817839-225x300.jpeg" width="307"/></a>     <a href="/2017/04/16/fabrication-de-prototypes-pcb-mon-marche-finition-avec-une-cnc/2017-04-15-14-14-13-jpg/" rel="attachment wp-att-3220"><img alt="2017-04-15 14.14.13.jpg" height="409" src="/media/2017/04/2017-04-15-14-14-13-jpg-e1492374795275-225x300.jpeg" width="307"/></a></p>
<ol>
<li>Perçage des trous de référence                    2. Ajustement du circuit sur la machine (martyre)</li>
</ol>
<p><img alt="2017-04-15 13.47.17.jpg" height="241" src="/media/2017/04/2017-04-15-13-47-17-jpg.jpeg" width="321"/>   <img alt="2017-04-15 14.18.56.jpg" height="241" src="/media/2017/04/2017-04-15-14-18-56-jpg.jpeg" width="321"/></p>
<p>3. Circuit après découpe.                                                                       4. Circuit nettoyé</p>
<p>Suit le nettoyage, enlever les bavures et les restes de ruban double face.</p>
<p><strong>J’ai finalement traversé toute la chaine des outils depuis le dessin jusque à la pièce découpée.</strong></p>
<p><img alt="2017-04-14 00.01.56.jpg" height="567" src="/media/2017/04/2017-04-14-00-01-56-jpg.jpeg" width="756"/></p>
<p>Dernière étape, souder les composants et mise sous tension.<br/>
<strong>Tout a fonctionné du premier coup !!!</strong></p>
<p>Rolf Ziegler (4/2017)</p>

## Commentaires

### franic — 17 avril 2017 à 09:30

<section class="comment-content comment">
<p>Superbe réalisation, très intéressant de voir toute la chaîne entre le dessin de PCB jusqu’au montage final. Cela peut paraître simple, mais il y a plusieurs étapes pas toujours faciles à passer ! Bravo et en plus cela fonctionne du premier coup !</p>
 </section>

### Yves Masur — 17 avril 2017 à 21:28

<section class="comment-content comment">
<p>Excellent tuto pour se rendre compte des étapes!<br/>
Question: as-tu prévu un connecteur pour (re-) programmer le CPU ESP8266?</p>
 </section>

### Rolf Ziegler Auteur de l’article — 17 avril 2017 à 22:33

<section class="comment-content comment">
<p>Le module ESP8266 est sur un socle pour la première programmation et pour le dépannage, par contre on peut le programmer par wifi une fois le code ESPEasy installé.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
