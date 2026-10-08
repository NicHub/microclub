---
title: "Deux livres Elektor sur le langage C et l’embarqué"
date: "2016-04-09T19:54:46"
lastmod: "2016-04-09T19:54:46"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["arduino", "atmega", "consoles", "embarque", "hardware", "linux", "processeurs", "programmation", "software", "systeme-dexploitation"]
url: "/2016/04/09/deux-livres-elektor-sur-le-langage-c-et-lembarque/"
wordpress_id: 2280
comment_count: 0
---
<p>Dans les publications d’Elektor, je me suis laissé tenter par la proposition de deux ouvrages:</p>
<ul>
<li>C programming with Arduino, de  Warwick A. Smith, 343 pages</li>
<li>Embedded Linux Control Center, de Hans Henrik Skovgaard, 450 pages</li>
</ul>
<p>Les deux sont dans la catégorie « learn » (il y a « design » et « share » ). Et vous l’aurez compris, ils sont en anglais. Petite revue et opinion.</p>
<h1>1 – C programming with <span>Arduino</span></h1>
<h3>Avec <span>Arduino</span>, vraiment?</h3>
<p><img alt="C" height="93" src="http://i46.servimg.com/u/f46/12/46/57/02/c-logo10.png" width="87"/>‘est la question qu’on peut se poser avec le premier livre; mais le préambule du titre est « AVR Microcontrollers and ATMEL Studio for… »; et c’est bien le cas. Juste pour voir si je vais apprendre des ficelles, des trucs et des astuces pour programmer en C des Arduino, je l’ouvre au milieu, et je tombe sur (p. 174) les spécification du format pour la fonction printf(), et la largeur des champs comme printf(« %5d\n », 123); // padded with 0</p>
<p>Et a peine plus loin, les boucles imbriquées. En fait, non, c’est un livre pour :</p>
<ol>
<li>Apprendre le C</li>
<li> programmer des CPU AVR</li>
</ol>
<p>L’auteur décrit bien qu’il utilise l’Atmel AVR Dragon ou l’AVRISP mkII, soit une sonde qui permet la cross-compilation et le chargement du programme sur la cible par un câble ICSP (voir: <a href="https://fr.wikipedia.org/wiki/Joint_Test_Action_Group" target="_blank">https://fr.wikipedia.org/wiki/Joint_Test_Action_Group</a>).</p>
<p>L’environnement de développement n’est donc pas l’IDE Arduino classique (que l’on peut télécharger ici: <a href="https://www.arduino.cc/en/Main/Software" target="_blank">https://www.arduino.cc/en/Main/Software</a> ), mais l’environnement Atmel Studio. Donc bien plus général. Le début du livre montre bien comment connecter la cible et mettre en place cette méthode de développement. Les points forts sont que l’on a accès à une bonne connaissance des registres et de l’utilisation native de ceux-ci. Par contre, on peut se demander si c’est un moyen rapide et efficace d’apprendre le C?</p>
<p>Pour ma part, je préfère que mes apprentis se fassent les dents sur un IDE de PC. Une fois les bases du langage aquises plus rapidement et plus facilement, on passe à une cible plus… exotique comme un Arduino. Avec ses spécificités et ses limites. Et les difficultés propres à la cross-compilation, et la non-possibilité de debbuguer apparaissent et viennent charger le bateau de la connaissance.</p>
<h3>Apprendre le C efficacement</h3>
<p>En effet, a quoi bon apprendre au stade de débutant qu’un cross-compilateur va râler à l’étape de l’édition de liens (linker) si une fonction de la bibliothèque est mal orthographiée? Les mêmes expériences seront plus efficacement  traitées sur un IDE natif, prévu pour Windows 32 ou 64 par exemple, même s’il cache une (grande) partie du déroulement de la création de l’exécutable. le même étudiant va remarquer rapidement que <strong>printf()</strong> n’est pas vraiment disponible pour de l’embarqué et que l’interface est du texte en mode série.</p>
<p>Bref, on peut garder le livre pour apprendre le C, et obtenir des infos détaillées sur les registres des CPU ATMEGA 328 et 2560, ainsi que leurs connexions sur les ports I/O du print Arduino. Et bien sûr, comment programmer timers, AD et watchdog!</p>
<h1>2 – Embedded Linux Control Center</h1>
<p>Dont le titre complet est « Design our own Embedded Linux Control Centre on PC and RaspBery Pi ». Ce livre touche à de nombreux programmes et concepts, pourtant il reste accessible à un (relativement) débutant grâce aux explications claires dans un anglais simple – aussi certainement parce que l’auteur est Danois. Au cours des explications, il y a de fréquents renvois par des URL sur des sites spécifiques qui permettent d’approfondir un sujet, ou de télécharger des utilitaires et des compléments.</p>
<p>Le livre s’adresse à celui qui aimerait faire de la « home automation » (de la maison intelligente?)</p>
<p>Allez, une jolie image pour illustrer cet anglicisme:</p>
<p><img alt="piqué à Protex.me" height="6624" src="https://www.protex.me/wp-content/uploads/2015/01/home-automation.jpg" width="8824"/></p>
<h3>Exhaustivité</h3>
<p>L’auteur est exhaustif dans son développement et la mise en oeuvre, sans tartiner avec des banalités, ni se répéter. Par exemple, pour la sélection de l’OS à monter sur le RaspBerry, les avantages et inconvénients pour le but proposé sont discutés. Toutefois, il faut ensuite se rappeler au cours de la lecture que <strong>ELCC</strong> signifie Embedded Linux Controle Centre – c’est ce programme et sa mise en œuvre qui est l’objet du livre. Une table des abréviations facilite la recherche d’acronymes.</p>
<p>Où j’ai plus de peine à suivre l’auteur c’est lorsqu’il recommande de lire tout le livre avant d’attaquer un projet… Alors que je ne résiste pas à sauter directement au sujet qui m’intéresse, qui à revenir en arrière pour plus en détail ou un élément qui m’aurait échappé?</p>
<h3>Vivre avec la modernité</h3>
<p>L’auteur montre a plusieurs reprise la difficulté de vivre dans le soft avec des changements et des mises à jour incessantes… Par exemple pour lire une sonde de température USB, il faut installer une librairie LIBUSB … version 1.12 et pas plus récente. Comme dit l’auteur, d’habitude je recommande la dernière version, mais celle-ci n’est pas compatible avec la librairie LIBHID! (lib pour les périphériques tels claviers, souris, manettes).</p>
<h3>WEB Config et connectivité d’accès</h3>
<p>L’auteur précise comment monter un service XAMPP et le sécuriser de manière à ce qu’il fonctionne encore tout en rendant le système fermé pour un accès indésirable. Les autres moyens de connexion, tels que SSH (secure shell), VNC (Virtula Network Computing), le X-server Xming et même le remote desktop xrdp sur RaspBerry sont exposés de manière claire.</p>
<p>Et oui, via l’application de connexion de bureau à distance MSTSC de Windows, on peut se logguer sur le RaspBerry. Attention, le clavier reste QWERTY. Vous voyez ci-dessous les écrans de VNC et MSTSC sur le même RaspBerry.</p>
<p><a href="/media/2016/04/VNC-MSTSC.jpg" rel="attachment wp-att-2294"><img alt="VNC-MSTSC" height="711" src="/media/2016/04/VNC-MSTSC.jpg" width="806"/></a></p>
<h3>Old fashioned et … Arduino</h3>
<p>Par certains aspects, des détails sont quelque peu de style ancien. L’auteur a depuis longtemps travaillé sur son projet, et certains renseignements le montrent. Par exemple, sur un (vieux) PC, comment réaliser une entrée-sortie sur un port parallèle.. Heureusement, on trouve toujours dans le commerce de tels adaptateurs; mais il y a belle lurette que les imprimantes sont connectées en USB ou sur le LAN.</p>
<p>Cependant, l’auteur précise que si l’on ne possède pas de port parallèle, on peut utiliser… un Arduino. Et là, les indications pour trouver comment connecter le hardware : LED, résistance; puis programmer l’Arduino, connecter l’USB à son fameux ELCC – tout y est! Il est également précisé que de couper et replanter l’USB provoque le reset de l’Arduino et rend les I/O instables un instant; ainsi que le moyen d’y palier. Et de se méfier de la limitation de courant si le device est alimenté par l’USB.</p>
<p>L’amour des choses anciennes fait un peu souci quand l’auteur présente son Linux chouchou: le DamnSmallLinux, qui n’a pas été mis à jour depuis 2012. Bon, il fait 50 Mo, mais quand on sait que la sécurité dépend de la fraicheur de l’OS…</p>
<h3>Ou sont les pins du RaspBerry? – WiringPi</h3>
<p>Là aussi, fidèle à son habitude, l’auteur fait une photo et met à disposition un tableau pour se repérer sur le connecteur, que ce soit un Raspberry rev 1 ou 2, modèle B ou B+. Il met en garde à propos de la tension admissible en entrée… Oui, le RaspBerry est en 3,3 V, et non en 5V.</p>
<p>Les commandes de ELCC se font par l’utilisation de <a href="http://wiringpi.com" target="_blank">WiringPi</a>, une bibliothèque générale pour les I/O d’un RaspBerry, écrite et maintenue par Henderson Gordon. C’est un code sur GIT, facile d’accès et d’utilisation. C’est une excellente chose que d’utiliser cette référence qui a une large audience plutôt que de ré-écrire une lib GPIO.</p>
<p>En bref, c’est un excellent livre qui peut rendre de grands services à ceux qui se lanceraient dans l’automatisation domestique.</p>
<p>Yves Masur (4/2016)</p>
<p> </p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
