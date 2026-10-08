---
title: "Arduino: un succès embarqué"
date: "2012-02-19T18:20:22"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "embarque", "hardware", "initiation", "processeurs", "programmation"]
url: "/2012/02/19/arduino-un-succes-embarque/"
wordpress_id: 728
comment_count: 6
---
<h1>Qu’est ce qu’est Arduino?</h1>
<p>Une plateforme de développement <strong>hard</strong> et<strong> soft</strong>, souple, bon marché, aux sources multiples, facile à mettre en oeuvre, bien documentée, bref l’environnement idéal pour débuter dans le domaine de l’embarqué (embedded in english). Vous désirez utiliser de l’électronique et de la microprogrammation? Piloter un moteur, activer un buzzer? afficher des informations, lire une température, une pression? C’est de prime abord passablement difficile.</p>
<p>Il faut se farcire des datasheet éprouvantes, souvent en anglais. Faire un schéma des composants qui tienne la route. Sortir le fer à souder, picots, circuit imprimé, ou pour le moins câbler (sans se tromper!) des chips et autres composants pas facile à appréhender, poser des connecteurs. Choisir une alimentation.</p>
<p>Ce n’est pas fini: il faut aussi trouver un environnement de développement: en assembleur (pas de chance! On se retappe des liste d’opcodes et on cherche les registres du processeur et leurs multiples finesses) en BASIC ou en C. Puis il faut se documenter comment produire le code exécutable et le charger dans la mémoire de la cible que vous aurez sélectionnée. Avec un peu de chance, on trouve des exemples de code qui résolvent notre problème: mais là encore, il faut adapter, voire fortement modifier le code pour que ce soit compatible avec notre montage.</p>
<p>Arduino standardise tout ça et le rend accessible rapidement: hard, soft, exemples Voyons comment.</p>
<h2>La plateforme hardware</h2>
<p>Commençons par voir ce qui se fait au point de vue du matériel. La carte processeur est faite autour du <a href="http://fr.wikipedia.org/wiki/Microcontr%C3%B4leur" title="Microcontrôleur">microcontrôleur</a> <a href="http://fr.wikipedia.org/wiki/Atmel" title="Atmel">Atmel</a> <a href="http://fr.wikipedia.org/wiki/Atmel_AVR" title="Atmel AVR">AVR</a>. La carte de base classique est la <strong>Arduino Uno</strong>.</p>
<p><img alt="Arduino Uno" height="311" src="http://arduino.cc/en/uploads/Main/ArduinoUno_R3_Front_450px.jpg" title="Arduino Uno" width="450"/></p>
<p>On en trouve de nombreuses déclinaisons, dont celle mise au point par le <a href="http://fr.wikipedia.org/wiki/Jean-Daniel_Nicoud" target="_blank">Professeur Nicoud</a>, la <strong>Diduino</strong> (<a href="http://didel.com" target="_blank">http://didel.com</a>) basée sur le modèle ATmega328, un modèle RISC de 8 bits à 20 MHz (voir: <a href="http://www.atmel.com/devices/ATMEGA328.aspx" target="_blank">http://www.atmel.com/devices/ATMEGA328.aspx</a> pour les détails). Car c’est possible de fabriquer soi-même une carte compatible Arduino: <a href="http://arduino.cc/en/Main/Policy" target="_blank">http://arduino.cc/en/Main/Policy</a>. La carte Diduino possède un bloc d’expérimentation, elle est livrée avec un set de composants pour tester des montages.<img alt="Diduino" height="310" src="http://www.bricobot.ch/actualite/Diduino.jpg" title="Diduino" width="569"/></p>
<p>Suivant le but du montage, on peut choisir une autre déclinaison du board CPU: le modèle Mega, Lyli Pad, le Nano, ou le Mini, voir d’autres dérivations de fabricants imaginatifs.</p>
<p>Des extensions, dénommées « shield », peuvent être rapportées sur la version de base pour y ajouter, Bluetooth, Ethernet, Flash card, commande de moteurs. Bref un joli pannel d’interfaces possibles. Les modules d’origine des différentes versions de l’Arduino sont fabriqués par la société italienne <em>Smart Projects</em>. Mais oui, les concepteurs d’Arduino sont italiens!</p>
<h1>L’environnement soft</h1>
<h2>Installation</h2>
<p>L’environnement de développement se charge depuis le site officiel: <a href="http://arduino.cc/en/Main/Software" target="_blank" title="http://arduino.cc/en/Main/Software">http://arduino.cc/en/Main/Software</a>. C’est assez lourd: 70 Mb, et une fois décomprimé, c’est 232 Mb. Par contre vous pouvez déplacer le répertoire arduino-1.0 ou bon vous semble, voire sur une clef USB: il se lancera sans problème. Comme il est écrit en Java, il tourne sur les trois OS phares: Windows (32 et 64 bits), Linux, Mac. Il est basé sur <a href="http://fr.wikipedia.org/wiki/Processing" target="_blank">Processing</a> et contient le compilateur avr-gcc, ainsi qu’une panoplie de softs Open Source.</p>
<p>Une fois arduino.exe lancé, le développement proprement dit se fait dans des modules appelés « sketch ». Voici à quoi cela ressemble.</p>
<h2>Sketch</h2>
<p><a href="/media/2012/02/sketch_screen.png"><img alt="Sketch" height="659" src="/media/2012/02/sketch_screen.png" title="sketch_screen" width="452"/></a></p>
<p>La barre des menus est suivie d’icônes, permettant de faire son développement: valider le code, le charger, créer un nouveau Sketch, charger et enregistrer. Le source, en C/C++ est introduit dans la fenêtre texte. La partie code montre une syntaxe à peine colorée: les mots-clefs reconnus sont en brun. Le Sketch est sauvé dans un répertoire du nom du projet, et le fichier de même nom prend l’extension « .ino »; c’est en fait le fichier source à l’identique, sans fioriture, éditable et copiable p. exemple avec Notepad++.</p>
<p>Une fenêtre inférieure montre le résultat des différentes commandes: ici celui d’une compilation réussie. Des erreurs seraient écrites en rouge.</p>
<p>Les paramètres de transfert sont réglés par le choix de la cible, et le port série à utiliser. Ici: Atmega328 et COM11.</p>
<p>De manière générale, le programme est constitué d’une fonction d’initialisation<strong> setup()</strong>, et d’une boucle infinie <strong>loop()</strong>. Elles constituent une surcouche du C qui habituellement appelle le programme principal par la fonction <strong>main()</strong>.</p>
<p>Vous trouverez une introduction pratique plus détaillée sur le site de notre HB9 préféré, Michel Vonlanthen, ici: <a href="http://www.von-info.ch/hb9afo/arduino/main.htm" target="_blank" title="Arduino - intro Vonlanthen">http://www.von-info.ch/hb9afo/arduino/main.htm</a></p>
<p>Parmi un foultitude d’exemples de programmation, la base consensuelle et universelle est toujours le clignotement d’une LED, alimentée par une patte de sortie du CPU via une résistance de quelques kilo-Ohms. Le programme consiste à : positionner la sortie à l’état haut, attendre, positionner à l’état bas, attendre, et boucler ad aeternam. Ensuite, on peut compliquer à souhait en testant un bouton, en attendant une valeur, en écrivant sur le port sériel, en pilotant un moteur, etc, etc!</p>
<p>Or l’exemple ci-dessus montre l’utilisation d’une technique fort avancée: l’utilisation de <a href="http://fr.wikipedia.org/wiki/Interruption_%28informatique%29" target="_blank">l’interruption</a>. On en discute plus bas.</p>
<h2>Chargement et éxécution</h2>
<p>Le programme est fait, la cible connue (type de circuit Arduino ATmega328) , il faut maintenant charger le programme. Diduino (et d’autres…) proposent la connexion USB. Celle-ci, non seulement alimente la carte – tant qu’on ne lui ajoute pas de moteurs ou de relais qui demande de la puissance – ouvre une connexion série. Autant sous Windows que Mac, il faut installer le pilote adéquat. La version la plus simple est de laisser Windows « chercher le pilote adéquat »; sinon, il faut le faire à la main. Les pilotes sont dans le répertoire: \arduino-1.0\drivers\. Ou directement du fabricant,  FTDI, a disposition ici: <a href="http://www.ftdichip.com/Drivers/VCP.htm">http://www.ftdichip.com/Drivers/VCP.htm</a>.</p>
<p>Un fois la fiche USB connectée, le pilote Windows se montre: Start -&gt; Périphérique et imprimantes -&gt; Non spécifié(e)s</p>
<p><a href="/media/2012/02/UART.png"><img alt="UART" height="133" src="/media/2012/02/UART.png" title="UART" width="140"/></a></p>
<p>Malgré l’installation réussie du pilote, du paramètre Tools -&gt; Serial Port (et le choix du bon n° de seriel), il se peut que ça ne fonctionne pas. A titre indicatif, sur 2 PC différents j’ai expérimenté:</p>
<p>– Pas de recherche automatique de Windows 7: il m’a fallut indiquer où se situe le pilote sur le bon répertoire, et l’installer. Tout a fonctionné parfaitement</p>
<p>– Recherche automatique: Windows recherche le pilote, l’installe.</p>
<p>Par contre à l’utilisation, des soucis de menu: il met 18 secondes pour se développer! La programmation patine aussi, avec le message sibyllin suivant: avrdude: stk500_getsync(): not in sync: resp=0x00. Un driver corrigé s’adresse à ce problème, ici: <a href="http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1237179908">http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1237179908</a>. Il appert que la DLL qui scrute les ports série les énumère à tout coup et attend leur time-out… Suite au remplacement de la DLL : <strong>rxtxSerial.dll</strong>, tout fonctionne bien sur mes deux PCs.</p>
<p>Il faut donc persévérer et rechercher sur le WEB une solution.</p>
<h2>La souplesse et l’exemple</h2>
<p>La force de l’ensemble Arduino est d’offrir d’une part un matériel défini, puisque même les sources d’autres constructeurs « collent » aux spécifications des originaux; en offrant bien entendu plus de ports, ou un processeur plus puissant. Et d’autre part, un ensemble logiciel préparé et épuré pour programmer la cible. Le choix du C/C++ est à mon avis fort judicieux: ce langage permet de compiler du code très efficace et proche de la machine.</p>
<p><em>NDA: je suis un peu plus dubitatif avec le C++. Vu la taille mémoire à disposition, on ne voit pas trop comment des instanciations d’objets ou des templates un peu compliquées auraient leur place. Mais comme à l’heure d’écrire ces lignes je n’ai que pratiqué des petits exercices, cela pourrait changer à l’avenir.</em></p>
<p>Il vaut la peine de se pencher un peu plus sur ce programme d’interruption, pour montrer la souplesse et la puissance d’abstraction des librairies Arduino. Comment est gérée une <a href="http://fr.wikipedia.org/wiki/Interruption_mat%C3%A9rielle" target="_blank">interruption</a>? Pour répondre à une requête d’interruption, le processeur devra (source Wikipédia) :</p>
<ul>
<li>préserver le contexte d’exécution du programme en cours afin de pouvoir, à terme, en reprendre l’exécution ;</li>
<li>lire en mémoire l’emplacement du programme destiné à gérer l’événement particulier (appelé gestionnaire d’interruption ou routine de gestion d’interruption), pré-établi lors de la prise en charge, par l’ordinateur, de l’ensemble spécialisé ici, par la routine <strong>start()</strong>;</li>
<li>exécuter la routine, court programme grâce auquel le processeur interagira avec l’ensemble spécialisé qui le sollicite afin de satisfaire ses attentes ;</li>
<li>restaurer le contexte d’exécution du programme interrompu ; et enfin</li>
<li>continuer à exécuter ce dernier.</li>
</ul>
<p>On le voit, ce mécanisme est aussi complexe que délicat à mettre en oeuvre. Eh bien, avec Arduino, on initialise l’interruption en une fonction de 3 paramètres: attachInterrupt(0, irq_func, FALLING); . Ceci a pour effet de lier lorsque l’interruption hardware n°0 est déclenchée, d’appeler la routine d’interruption ici réalisée par la fonction « irq_func() », sur un flanc descendant. Les autres possibilités étant: flanc montant, état haut, état bas. Le fameux flanc descendant est activé lorque la LED rouge s’eteint, car on aura pris soin de relier cette sortie n°13 sur la patte n°2 qui est effectivement l’entrée d’interruption 0.</p>
<p>La fonction d’interruption se contente d’inverser l’état de la LED jaune, ce qui fait qu’elle clignote à une fréquence de moitié de la LED rouge. Avec l’environnement de développement viennent de nombreux exemples didactiques de programmation : \arduino-1.0\examples\, et bien sûr sur le site officiel: <a href="http://arduino.cc/en/Tutorial/HomePage" target="_blank">http://arduino.cc/en/Tutorial/HomePage</a>.</p>
<h2>Les fonctions dédiées et librairies</h2>
<p>Il est clair que le C pur ne suffit pas – a vrai dire, le C pur n’existe pas! Ce langage s’applique a quasi tous les CPU, du 8 bit au 64 bits (voir plus?) et un montage 8 bits n’a pas les mêmes possibilités qu’un système multicoeurs. Pour chaque implémentation, il y a des fonctions dédiées qui permettent d’utiliser toutes les finesses du système. Arduino a aussi les siennes, sur le WEB ici: « <a href="http://arduino.cc/en/Reference/HomePage" target="_blank" title="Langage Reference">langage reference</a>« , en local dans /arduino-1.0/reference/index.html.</p>
<p>On y trouve notamment les possibilités de positionner directement et efficacement une patte à 0 ou à 1, de la lire, par respectivement <a href="http://arduino.cc/en/Reference/DigitalWrite">digitalWrite</a>() et <a href="http://arduino.cc/en/Reference/DigitalRead">digitalRead</a>(). Plus exotique, la fonction qui permet de moduler une largeur d’impulsion (PWM, Pulse Width Modulation) s’appelle <a href="http://arduino.cc/en/Reference/AnalogWrite">analogWrite</a>(), en décalage par rapport à <a href="http://arduino.cc/en/Reference/AnalogRead">analogRead</a>(), qui fait elle fait une vraie conversion analogique -&gt; numérique (A/D: Analog -&gt; Digital). C’est bien sûr dépendant des possibilités du CPU.<br/>
Des librairies sont également à disposition <a href="http://arduino.cc/en/Reference/Libraries" target="_blank">http://arduino.cc/en/Reference/Libraries</a>. Il s’agit des les importer pour pouvoir en utiliser les fonctions. Celles-ci d’adressent à du matériel (EEPROM, LCD, cartes SD) ou des protocoles souvent utilisés (Serie, Ethernet, SPI).</p>
<h1>Du hard et du soft, un cours très complet</h1>
<p>Le document ci-dessous est une large représentation de réalisations Arduino. Mais constitue aussi un cours complet de mise en oeuvre, qui explore toutes les facettes en partant de l’électronique, de la réalisation pratique avec des maquettes dessins, schémas. En français, s’il vous plaît.<br/>
<a href="http://fr.flossmanuals.net/arduino/" target="_blank"> http://fr.flossmanuals.net/_booki/arduino/arduino.pdf</a></p>
<h1>Des fournisseurs</h1>
<p>Pour débuter et tester, la carte <a href="http://www.didel.com/DiduinoPub.pdf" target="_blank">Diduino</a>, elle est idéale.</p>
<p><em>Les indications ci-dessous m’ont été communiquées par M. Frédéric Benninger, donc pas (encore) testées personnellement.</em></p>
<p>Le Seeeduino Starter Kit Standard[<a href="http://shop.boxtec.ch/product_info.php/products_id/40368" target="_blank">Shop.boxtec.ch</a>] vise le même but, mais elle pourra par la suite être réutilisée dans un produit fini. Pour ceux qui visent une application dédiée, cela dépend de la taille du projet et du type d’alimentation envisagée. Par exemple en modélisme le <a href="http://www.seeedstudio.com/depot/seeeduino-film-p-689.html?cPath=132_133" target="_blank">Seeeduino </a>Film est un must, seulement quelques grammes, elle est livrée avec une petite batterie et le régulateur de charge pour panneaux solaires est inclus.</p>
<p>Pour faire une application qui a besoin de gérer une horloge calendaire, par exemple à des fins d’ d’acquisition de données, le <a href="http://www.seeedstudio.com/depot/seeeduino-stalker-atmega-168-p-639.html?cPath=77" target="_blank">Seeeduino Stalker</a> est parfait, il intègre une RTC et un emplacement pour carte micro SD.</p>
<p>Voici encore des châssis [<a href="http://www.sparkfun.com/products/11056" target="_blank">www.sparkfun.com</a>] pour les bricoleurs, sans oublier des boîtes [<a href="http://shop.boxtec.ch/advanced_search_result.php?keywords=box&amp;x=0&amp;y=0" target="_blank">shop.boxtec.ch</a>] pour mettre en valeur le fruit du travail fourni.</p>
<h1>Des références</h1>
<p>LE site de référence: <a href="http://arduino.cc/" target="_blank">Arduino.cc</a></p>
<p>Documentation Arduino/Diduino très complète+exercices ici: <a href="http://www.didel.com/diduino/Liens.pdf">http://www.didel.com/diduino/Liens.pdf</a></p>
<p>Wikipédia: <a href="http://fr.wikipedia.org/wiki/Arduino" target="_blank">http://fr.wikipedia.org/wiki/Arduino</a></p>
<p>Liste de discussion (Suisse) : <a href="http://fr.groups.yahoo.com/group/arduino_suisse/" target="_blank" title="Arduino Suisse">http://fr.groups.yahoo.com/group/arduino_suisse/</a></p>
<pre></pre>

## Commentaires

### Vonlanthen — 19 février 2012 à 20:24

<section class="comment-content comment">
<p>Bravo Yves, excellente description susceptible de rassembler les « brebis »égarées !</p>
 </section>

### Georges — 22 février 2012 à 12:24

<section class="comment-content comment">
<p>Bravo pour ce magnifique article sur Arduino, vraiment trais complet, félicitation!</p>
 </section>

### Michel Vonlanthen — 10 mars 2012 à 11:28

<section class="comment-content comment">
<p>Le cours Arduino est maintenant terminé et il ne fait nulle doute que ça « arduine » dans les chaumières ces temps… Mais la vie n’est pas simple et il arrive qu’on sèche sur un problème, que le fatras s’installe sur sa table de travail et même que son oscillo tombe en passe.<br/>
C’est ici que ça se passe:   <a href="http://www.bricobot.ch/" rel="nofollow ugc">http://www.bricobot.ch</a><br/>
Où l’on voit l’utilité d’une liste de distribution…</p>
<p>Amitiés<br/>
michel von</p>
 </section>

### Michel Vonlanthen — 10 mars 2012 à 11:29

<section class="comment-content comment">
<p>Correction: … oscillo tombe en PANNE !</p>
 </section>

### Michel Vonlanthen — 10 mars 2012 à 11:30

<section class="comment-content comment">
<p>Parce que si, maintenant, les oscillos vont faire des passes au bois, où va-t-on ?</p>
 </section>

### Laurent Francey — 1 avril 2012 à 16:39

<section class="comment-content comment">
<p>Parfois, pour tester certaines fonctions il peut être intéressant de simuler certaines parties d’un programme.<br/>
Voici même un simulateur arduino, malheureusement payant … mais pas cher !<br/>
<a href="http://www.arduino.com.au/Simulator-for-Arduino.html" rel="nofollow ugc">http://www.arduino.com.au/Simulator-for-Arduino.html</a></p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
