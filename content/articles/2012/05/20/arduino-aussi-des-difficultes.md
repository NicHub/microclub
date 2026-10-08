---
title: "Arduino: aussi des difficultés"
date: "2012-05-20T14:38:21"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "diduino", "embarque", "initiation", "lcd-serie", "programmation", "prototype", "stalker"]
url: "/2012/05/20/arduino-aussi-des-difficultes/"
wordpress_id: 766
comment_count: 7
---
<h2>Introductions aux difficultés(!)</h2>
<p>Dans un article précédent (<a href="/2012/02/19/arduino-un-succes-embarque/" target="_blank" title="Arduino, un succès embarqué">http://microclub.ch/2012/02/19/arduino-un-succes-embarque/</a>), j’avais mis en lumière les facilités offertes par le concept Arduino: hard+soft défini, bon marché, secondes sources et dérivés de plusieurs fabricants de « shield » (soit les extension de la plaque de base Arduino).</p>
<p>Afin d’explorer rapidement les possibilités de mettre au point un prototype, j’ai décidé de mettre l’accent sur du matériel très complet et facile à mettre en œuvre, sans me focaliser sur le prix.</p>
<p>Après m’être renseigné sur le net, je penche pour une carte Arduino compatible, <a href="http://shop.boxtec.ch/product_info.php/products_id/40211" target="_blank" title="Stalker">Seeeduino Stalker</a> version 2.1. Elle a tout pour bien faire par son équipement d’origine: horloge RTC, support pour carte FLASH, faible consommation (elle est prévue pour faire du « data logger »).</p>
<p>Comme périphérique, j’opte pour le <a href="http://seeedstudio.com/wiki/GROVE_System" target="_blank" title="Grove system">Grove system</a>. Avec le kit assez complet du <a href="http://shop.boxtec.ch/product_info.php/products_id/40498">Mega Shield</a> et des relais, un servo et des câbles supplémentaires, je suis paré. Enfin, je le suppose. Voici les résultats de mes trouvailles, c’est assez long je le reconnais, avec à la fin, en résumé les recommandations et tour de main pour s’approprier l’Arduino.</p>
<h2>LCD Série</h2>
<p><a href="/media/2012/05/affiche_13.jpg"><img alt="LCD" height="135" src="/media/2012/05/affiche_13-300x135.jpg" title="LCD" width="300"/></a></p>
<p>D’abord afficher quelque chose, me dis-je. En effet, lors de nos premiers essais, les infos sortantes du kit étaient envoyées en série sur le PC. Pour un système embarqué autonome, il faut un affichage. Celui de Grove est un <a href="http://seeedstudio.com/wiki/Grove_-_Serial_LCD_v1.0b" target="_blank" title="LCD serie">modèle série</a>, la bibliothèque est disponible après quelques recherches sur le WEB. Ce principe économise les connexions, vu que seuls Rx et Tx sont nécessaires pour communiquer au lieu d’un port parallèle et des signaux de handshake. Un premier doute s’installe: quelle version hardware est la bonne? La réponse est sur le print du LCD: V2.1 Je prend le zip, le déballe et l’ajoute dans bibliothèque de l’environnement de développement intégré (EDI) Arduino 1.0, le redémarre… Et les problèmes arrivent.</p>
<h3>Erreur de compilation</h3>
<p>La compilation coince avec un message pour le moins curieux: il manque « wprogram.h » dans « arduino.h ». Inutile d’essayer de la supprimer, ni de la corriger. Un coup de Google m’indique qu’il faut utiliser une nouvelle bibliothèque au lieu de « SoftwareSerial.h », soit « NewSoftSerial.h ». (A mon avis, c’est un peu débile d’appeler un logiciel « software », ou un programme « program » mais bon, passons). De nouveau une heure de mise en place de bibliothèque, déplacer l’ancienne (au cas où)… Sans résultats probants. Je ne suis pas seul: un <em>user</em> dépité s’exprime <a href="http://forums.adafruit.com/viewtopic.php?f=24&amp;t=25002" target="_blank" title="user dépité">ici</a>. Il semble qu’un nombre important de sketch ne compilent plus et doivent être adaptés pour Arduino 1.0. Contrairement à ce que l’on pourrait croire, le 1.0 est un aboutissement, il y a des versions précédentes qui on été numérotées 1 à 23, toujours obtensibles ici: <a href="http://arduino.cc/en/Main/Software" target="_blank" title="Arduino download">http://arduino.cc/en/Main/Software</a></p>
<h3>Correction de la bibliothèque</h3>
<pre>Le code devient donc:
// include the library code:
 #include &lt;SerialLCD.h&gt;
 #include &lt;NewSoftSerial.h&gt; //this is a must</pre>
<p>Mais voilà, ça ne compile pas le moins du monde (même si c’est un « must »!)et il y a une tonne d’erreurs du même topo, pas du tout parlantes et obscures à souhait. Sur la page de « NewSoftSerial », il est dit qu’il faut modifier toutes les références à « NewSoftSerial » par « SoftwareSerial ». Je me lance donc dans le chercher/remplacer… Sans plus de succès à la compile. Les erreurs obscures ont changé, mais restent obscures. Le trouble s’accentue lorsque sur le <a href="http://arduiniana.org/2011/01/newsoftserial-11-beta/" target="_blank" title="(old NewsoftSerial)">site de l’auteur</a> de « NewSoftSerial », il est dit que désormais sa bibliothèque est en standard dans Arduino 1.0! Et bien entendu, sur le site officiel de Arduino, ce qui concerne le LCD est le mode <strong>parallèle</strong> et n’aide en rien.</p>
<p>Un petit tour dans les forums, et je me dis que la route et fausse, fausse! Je reprend un exemple de pilotage LCD série du site Arduino, qui lui compile! je fais milles essais avec une connexion différente, PIN différentes, mais pas la moindre réaction du LCD, même pas un curseur qui clignote, une ombre de pixel qui bouge, rien! J’en viens à me demander si mon module est KO?</p>
<p>Retour donc de « SoftwareSerial ». Et redémarage de l’éditeur, et recherche, parmi les milliers de sorties Google, et crawl dans les forums. Puis un soir, la lumière. De désespoir, je revisite le forum du site de Seeestudio, ou une indication de mise à jour de la librairie est à utiliser… ici: <a href="http://www.seeedstudio.com/wiki/File:SerialLCD_for_Arduino1.0_20120307.zip;">http://www.seeedstudio.com/wiki/File:SerialLCD_for_Arduino1.0_20120307.zip;</a> c’est une version du 7.3.2012 qui est déposée… Et ça fonctionne. Ouf!!</p>
<h2>Se connecter à la carte Stalker</h2>
<pre><a href="/media/2012/05/200px-Seeduino_Stalker_v2.2.jpg"><img alt="Seeduino_Stalker_v2.2" height="150" src="/media/2012/05/200px-Seeduino_Stalker_v2.2.jpg" title="Seeduino_Stalker_v2.2" width="200"/></a></pre>
<p>Ou: encore du sériel à manager. La carte Stalker de Seeeduino n’as pas de connexion USB, mais seulement du RS232  5V TTL par une série de broche à 2,54 mm. J’ai commandé un câble USB – RS232 <a href="http://shop.boxtec.ch/product_info.php/products_id/40385" target="_blank" title="cable serie">ici</a>, qui avait l’air de faire l’affaire, d’autant plus que le chip utilisé qui semble le roi de la transmission est le FTDI, et que sa version intégrée au Diduino du Pr Nicoud marche pile poil. Voici la connexion d’origine:</p>
<pre>Color     FTDI     Stalker
---------------------------
Black     0V       0V
Braun     CTS      0V
Red       5V       5V
Orange    Tx       Rx
Yellow    Rx       Tx
Green     RTS      DTR</pre>
<p>Mais une fois connecté… pas de liaison! Seule l’alimentation (via USB) a un effet sur Seeduino qui tourne, la fameuse LED de la pin 13 clignote.</p>
<p>Bien entendu, j’ai passé par rechercher les définitions et les câblages des CTS, RTS, DTR… Et vu avec désespoir que les signaux DSR, DCD n’étaient pas câblés. Essayer de démonter une fiche moulée tient de la haute voltige, inutile d’y penser. Évidemment, Rx et Tx, ça dépend du point de vue auquel on se place: le Rx de l’un est forcément le Tx de l’autre. Après un peu trop d’heures de recherche, voici la solution:</p>
<pre>Color     FTDI     Stalker
---------------------------
Black     0V       0V
Braun     CTS      0V
Red       5V       5V
Yellow    Rx       Rx
Orange    Tx       Tx
Green     RTS      DTR</pre>
<p>Soit simplement croiser Rx et Tx!</p>
<p><a href="/media/2012/05/31402.jpg"><img alt="USB-serie" height="188" src="/media/2012/05/31402.jpg" title="USB-serie" width="188"/></a></p>
<p>Visiblement, le CTS (clear to send) à 0V ne gêne pas: soit il n’est pas utilisé par Arduino 1.0, soit il le voit comme toujours OK.</p>
<p>Et encore une chose: j’ai remarqué avec le terminal que la Baud rate est à la moitié de la valeur donnée (4800 au lieu de 9600). J’ai supposé que le quarz de 8 MHz est à la demi fréquence standard… Mais en fait, il faut changer la config de l’EDI par: Tools-&gt;Board-&gt;Atmega 328, et la vitesse de transmission devient correcte.</p>
<h2>Carte mémoire SD</h2>
<p>Maintenant que Staker est programmable, essayons ses possibilités. Et sa mémorisation sur SD. Dans les exemples qui sont disponibles sur le site de Seeeduino, il y a le sketch « StalkerV21_DataLogger_15Sec_NoSerialPort ». Mais l’inclusion de &lt;Fat16.h&gt; et de &lt;Fat16util.h&gt; ne passe pas…Bien que la lecture de forum me montre qu’il vaut mieux se contenter du format FAT16 bits, qui fait certes des blocs de fichiers plus gros que la FAT32, mais qui est visiblement mieux géré par Arduino. Si le formatage ou la lecture du chip sur le PC ne pose aucun problème, c’est par contre assez difficile d’insérer mécaniquement le chip entre quartz et le DS3231, soit le plus gros IC de la carte; ça va être coton pour la retirer et la lire.</p>
<p><a href="/media/2012/05/49001.jpg"><img alt="SD" height="210" src="/media/2012/05/49001.jpg" title="SD" width="200"/></a></p>
<p>Un essai avec l’exemple de la biliothèque &lt;SD.h&gt; compile, mais le pilote ne reconnais pas la carte. Allez! une recherche et le chargement de « fat16lib20111205.zip », déballé, installé et l’ajout de la lib &lt;Fat16&gt; dans l’EDI… coucou! revoilou l’erreur « WProgram.h ». Désormais, je sais qu’il est inutile de vouloir corriger quoique ce soit.</p>
<p>Un essais des exemples d’Arduino d’origine me montrent que certains passent: le test « fat16write » et « fat16read » compilent et laissent un fichier de bonne facture sur la SD. Ouf!</p>
<h2>Horloge DS3231</h2>
<p>C’est le complément indispensable à un enregistrement de log: connaitre date et heure. Mais que dit l’exemple DS3231.CPP ? WProgram.h introuvable! Ben voyons… Une recherche de « DS3231 Arduino library »  me donne sur un site un zip, que je déballe et dépose dans la librairie, suivi de la relance de l’EDI (refrain connu).</p>
<p>Cette fois, la leçon ayant porté, je commence par la base Arduino 1.0, pour voir ce qui fonctionne parmi les sketches de: File -&gt;Examples-&gt;Time. Par exemple, « TimeRTC », qui compile sans souci, bien que prévu pour le DS1307. Chargé sur la carte Stalker, il affiche par le terminal:</p>
<pre>03:06:01 1 1 2000</pre>
<p>et compte en continu chaque seconde, même après un reset. Si je retire la prise USB et la remet, ça recommence à 3h de l’an 2000; mais une fois la pile CR2032 clippée dans son logement, la date ne revient plus en arrière en cas de coupure de l’alimentation. C’est encourageant; je change maintenant l’inclusion &lt;DS1307RTC.h&gt; par &lt;DS3231.h&gt; pour profiter des performances du chip DS3231. Mais qui revoilou? WProgram.h introuvable!</p>
<p>Une comparaison des datasheet – rapide, hein, ne me prenez pas au mot – montre que je peux me passer pour le moment des 2 alarmes programmables et du capteur de température dont est doté le DS3231. Je me rabat donc sur le soft de base du DS1307, chip que je connais, l’ayant utilisé avec succès pour le projet de la barrette, décrit <a href="/2011/03/25/projet-barrette-livrable/" target="_blank" title="Barrette">ici</a>.</p>
<p>Mais il me faut tout de même mettre cette clock à l’heure; ce que je tente par l’exemple « TimeRTCSet ». Difficulté: il faut via le terminal, indiquer le nombre de secondes depuis 1970 pour qu’un SET soit fait. Si ça ne vous dit rien, consultez la définition de <a href="http://fr.wikipedia.org/wiki/Epoch" target="_blank" title="Epoch">EPOCH</a>. Cependant le programme est fonctionnel. Et l’horloge réagit correctement.</p>
<h2>Servo</h2>
<p>Pas d’intelligence artificielle, mais bien d’un servo-moteur que l’on va implémenter. La première difficulté est de découvrir comment connecter un servo avec 3 fils sur des connecteurs à 4 fils du Grove system. Des câbles existent, mais le raccord sera femelle-femelle! Grâce à Laurent, auteur <a href="/membres/" target="_blank" title="Membres">bien connu sous le pseudo de Franic</a>, j’ai une liste des modèles de servo avec les couleurs des fils: +5V, 0V et pulse de commande. Grâce à ma collection de câbles, je peux brancher le servo sans sortir mon attirail électronique. Dans ce genre de raccord, le risque est grand de faire fumer du matériel, voir la carte CPU par une mauvaise connexion. Ici, avec un seul petit moteur, je ne dépasse pas le courant de 350 mA: c’est donc compatible avec l’alim via le port USB du PC.</p>
<p>L’exemple de sketch File-&gt;Examples-&gt;Servo-&gt;Knob, légèrement modifié pour lire un potentiomètre qui donne la consigne, fonctionne du premier coup.</p>
<h1>Conclusions et recommandations</h1>
<h3>Version de soft</h3>
<p>Arduino est bien l’ensemble hard+soft large, fourmillant et plein de ressources qui est promis. Par contre, pour le novice qui débute en programmation et qui ne connait pas forcément le hard, il y a plein de chausse-trappes. Le principal, on l’a vu, est lié à l’évolution du logiciel. Nombre de drivers et exemples ne sont pas à jour, et la difficulté est grande de savoir si oui ou non un logiciel est prêt pour <em>notre</em> solution.</p>
<p><a href="/media/2012/05/wProgram_h.jpg"><img alt="wProgram_h" height="229" src="/media/2012/05/wProgram_h-300x229.jpg" title="wProgram_h" width="300"/></a></p>
<p>Un symptôme classique est l’erreur « WProgram.h » à la compilation. Dire dans un forum, comme je l’ai vu qu’il faut <em>soi-même dépanner le soft, c’est ainsi que l’on apprend à programmer</em> est bien joli… mais ça n’aide pas beaucoup. Les pilotes mis à jour ont l’inclusion suivante:</p>
<pre>#if defined(ARDUINO) &amp;&amp; ARDUINO &gt;= 100
#include "Arduino.h"    // for digitalRead, digitalWrite, etc
#else
#include "WProgram.h"
#endif</pre>
<p>Ce code tient compte de la version, qui a fait un saut de 023 à 100.</p>
<p>On ne peut donc pas tabler sur un hard offert par un fabricant, sans savoir s’il sera fonctionnel avec la dernière version de l’EDI Arduino. On ne peut pas demander à un novice en la matière de maîtriser à la fois le hard, le soft qui est bien entendu spécifique sur une cible 8 bits, de maîtriser l’architecture interne du CPU et des astuces propres à des déclinaisons hardware comme la compatibilité entre les shield. Je m’attendais plus à une sorte de LEGO, où il suffit de choisir les blocs hard et soft pour construire un projet autant en hardware qu’en software.</p>
<p>Si l’on veut sortir des exemple unitaires (quoique, vu les difficultés évoquées ci-dessus, ce n’est pas donné…) pour réaliser un ensemble, une solide connaissance logicielle et matérielle est nécessaire. Ou bénéficier de l’aide d’un groupe actif via un forum!</p>
<h3>l’EDI</h3>
<p>Il fait assez minimaliste, par rapport à d’autre environnements intégrés: l’EDI Arduino se contente de colorer en brun les mots clef et les fonctions de la bibliothèque, les commentaires en vert, les chaînes en bleu. Un éditeur comme <a href="http://notepad-plus-plus.org/fr" target="_blank">Notepad++</a> se révèle bien plus  efficace: syntaxe colorée complète, recherche/remplacement, comparaison, complétion, multi-vues, etc, etc! De plus, l’EDI Arduino n’a pas d’aide contextuelle. Par rapport à d’autre compilateurs, l’utilisation du « make » serait plus productive: en effet, pourquoi tout recompiler avant d’envoyer le fichier sur la cible alors qu’on vient de le faire? Les erreurs ne renvoient pas non plus au fichier/ligne fautif par un clic sur le message.</p>
<p>Et diable, pourquoi ne se rappelle-t-il pas de la position de la fenêtre?  à chaque fois qu’on l’ouvre, on doit l’étirer!</p>
<p>Comme il est gratuit, on le prend comme il est. Mais on peut rêver à mieux.</p>
<h3>Ajout /mise à jour des librairies</h3>
<p>L’opération semble simple: copier les fichiers proposés – souvent zippés – dans le répertoire Arduino-1.0\librairies. Mais si l’on peut nommer le répertoire comme une variable (lettre et chiffres), un test est fait au démarrage de l’EDI. Par exemple, je crée une copie de « SerialLCD », en SerialLCD-2, on aura une erreur:</p>
<p><a href="/media/2012/05/lib-conflict.jpg"><img alt="lib-conflict" height="103" src="/media/2012/05/lib-conflict-300x103.jpg" title="lib-conflict" width="300"/></a></p>
<p>Qui est clair dans <strong>ce</strong> contexte. Si c’est une mise à niveau et que vous voulez garder l’ancienne, il faudra très certainement la retirer de la librairie et la déposer ailleurs sur votre espace de stockage. Et la swapper avec la nouvelle si vous devez reconstruire une ancienne version. Heureusement, le ZIP conserve les dates des fichiers… ce qui m’a permis de lever un doute lors de mes multiples modifications concernant le LCD.</p>
<p>A chaque coup, ne pas oublier d’arrêter toutes les instances de l’EDI, qui a la fâcheuse option d’en lancer une nouvelle à chaque ouverture de fichier. C’est lourd et générateur de confusion.</p>
<h3>La connectique Grove system</h3>
<p>On l’a entrevu à la connexion du LCD, il y a 4 fils par prise: 0V, 5V, signal 1 et signal 2. Sur la prise suivante, les alim, signal2 et signal 3… voir le diagramme <a href="http://www.seeedstudio.com/wiki/File:Stem-diagram-conn.jpg" target="_blank" title="Stem-diagram-conn.jpg">ici</a>. C’est futé, mais.. ça peut amener à des problèmes subtils si on utilise les 2 signaux par un connecteur: court circuit, double charge. Au point de vue montage, c’est la perplexité: les trous de fixation demandent des vis de 2 mm! De plus comment voulez-vous monter un bouton sur face avant, avec un connecteur plus haut? <a href="/media/2012/05/bouton.jpg"><img alt="bouton" height="140" src="/media/2012/05/bouton-300x278.jpg" title="bouton" width="151"/></a> Le problème est bien entendu le même pour LED et potentiomètre. On le voit sur cette image, la fixation est simple: un fil de wrapp passe dans les trous du print pour l’attacher à la planchette percée.</p>
<p>Il serait intéressant d’avoir des plugs à 90°. Heureusement, il y a aussi des plaque pour prototype, qui permettent de monter son électronique à sa façon (<a href="http://shop.boxtec.ch/product_info.php/manufacturers_id/22/products_id/40780" target="_blank" title="Prototype">ici</a>).</p>
<p><a href="/media/2012/05/cables.jpg"><img alt="cables" height="150" src="/media/2012/05/cables-150x150.jpg" title="cables" width="150"/></a> Tous les câbles ont la même longueur; dommage, ça devient vite un brouillard de câble, bien que ce soit acceptable pour un prototype. Il faudra par contre les attacher et les marquer.</p>
<p>Malgré tout, on peut construire des montages hard + soft sans sortir le fer à souder et une panoplie d’outils pas forcément à portée de toute les bourses.</p>
<h2>Références</h2>
<p>Elles sont intégrées dans le textes par liens.</p>
<p>Yves Masur (5/2012)</p>

## Commentaires

### Michel Vonlanthen — 21 mai 2012 à 10:08

<section class="comment-content comment">
<p>Bravo Yves, bien travaillé… pour nous !</p>
<p>Actuellement je suis en stand-by en ce qui concerne l’Arduino, pas une seconde à lui consacrer, je dois me défendre contre ceux qui veulent me barrer la vue sur les Alpes avec des tours de 60 mètres de haut (demainbussigny.ch)… Mais je reprendrai tout ça à fin juin. Donc pas beaucoup plus d’expérience, mais j’ai constaté les mêmes choses que toi, notamment en ce qui concerne la librairie LCD série. J’en suis arrivé à faire ma propre librairie, au moins elle fonctionne. Je n’ai pas été très loin, elle ne fait pas encore grand chose, mais je sais au moins que ma carte LCD est OK. Je vois que tu avais le même doute…</p>
<p>J’ai un tas de circuits et de shields à tester et je m’en réjouis. Pour le moment j’ai terminé mon émetteur TV et il fonctionne bien. Je dois encore lui augmenter la puissance en lui rajoutant un ampli, ce sera mon prochain boulot lorsque je serai de retour des USA. Ensuite l’étendre à d’autres bandes et c’est pour ça que j’ai besoin de la LCD série, de façon à libérer des pins pour autre chose. Là, avec la commandes du panneau avant, du synthétiseur et la mesure de température et de la tension d’alimentation je suis complet.<br/>
Une fois la doc mise au propre et éventuellement publiée (sur mon site en tous cas), je m’attaquerai au logger pour caractériser mon chauffage électrique et pour préparer son évolution vers le solaire. </p>
<p>Toutes ces expériences m’amènent à la conclusion que, quoi qu’on fasse, on ne pourra jamais s’éviter de connaitre les bases de l’électronique si on veut travailler avec l’Arduino et systèmes du même genre. De mon point de vue, il est illusoire de croire qu’on va pouvoir faire des montages hard-soft sans aucune connaissance en électronique. Si on ne sait même pas calculer une loi d’Ohm, on sera bloqué par des bricoles, on fera fumer son matos, et le tout passera à la poubelle et dans les souvenirs ! C’est la même chose du point de vue software. Je trouve l’Arduino idéal parce qu’on peut très rapidement passer de l’idée à la réalisation, sans devoir ré-inventer la roue. Par contre, si on n’a jamais pratiqué la programmation, ça pose quand-même quelques problèmes. C’est peut-être un système idéal pour les vieux briscards des Gas-Fets pétés comme nous, mais les vrais néophytes qui ne connaissent encore rien à rien seront mieux servis par un système du genre Lego par exemple. On ne peut pas tout avoir…</p>
<p>Pour des kids, le mieux est qu’il restent en atmosphère pilotée par un moniteur, encadrés dans un cours, afin qu’ils soient guidés pour résoudre ces problèmes-là. Sinon c’est la cata et le découragement assurés. J’ai tenté d’intéresser mes petits-enfants à la chose mais sans grand succès. Leurs parents m’ont trop vus passer des nuits entières dans mon gourbi pour penser que ce que je fais soit amusant. Et ils ont transmis cette mémoire-là à leurs propres enfants sous forme d’anticorps à l’électronique…</p>
<p>Une autre constatation en passant:  quelque chose qu’on obtient trop facilement a peu de valeur. C’est peut-être ça qui pèche avec mes tentatives d’intéresser mes petits à l’électronique. Comme ils auraient tout à disposition, y compris un prof bienveillant, ça leur semble trop facile et pas assez origjnal. Ca en aurait peut-être plus si c’était amené par un copain et qu’ils doivent suer du burnous avant de voir clignoter la led.</p>
<p>ARDUINamitiés<br/>
michel vonlanthen</p>
 </section>

### ↳ Réponse — Meriem — 7 mai 2014 à 07:29

<section class="comment-content comment">
<p>heey,<br/>
Actuellement j’ai comme « projet » de développer un logger pour un capteur solaire.<br/>
En ce moment j’ai câblé l’arduino  DUE et l’horloge RTC …  j’ai commencé par faire un premier programme  que je vous le laisserai ci-dessous. mon programme doit mettre a l’heure le système manuellement ensuite l’ envoyer a l’horloge puis régler la fréquence d’acquisition et lancer les mesures. Je dois récupérer et afficher les mesures puis arrêter les mesures quand je veux.<br/>
Voici le premier sketch:<br/>
 #include « Wire.h »<br/>
    #define DS1307_I2C_ADDRESS 0x68<br/>
    //Pour convertir des nombres décimaux normal à des nombres décimaus codés binaire<br/>
    byte decToBcd(byte val)<br/>
    {<br/>
    return ( (val/10*16) + (val%10) );<br/>
    }<br/>
    //Pour convertir des nombres binaires à des nombres normales<br/>
    byte bcdToDec(byte val)<br/>
    {<br/>
    return ( (val/16*10) + (val%16) );<br/>
    }</p>
<p>    void setDateDs1307<br/>
   (byte seconde, // 0 à 59 secondes<br/>
    byte minute, // 0 à 69 minutes<br/>
    byte heure, // 1 à 23 heures<br/>
    byte joursdanslasemaine, // 1 à 7 jours<br/>
    byte joursdanslemois, // 1 à 28jours ou 1 à 29jours ou 1 à 30jours ou 1 à 31jours<br/>
    byte mois, // 1 à 12mois<br/>
    byte annee) // 0-99<br/>
    {<br/>
    Wire.beginTransmission(DS1307_I2C_ADDRESS);<br/>
    Wire.write(0);<br/>
    Wire.write(0x80);<br/>
    Wire.write(decToBcd(seconde));<br/>
    Wire.write(decToBcd(minute));<br/>
    Wire.write(decToBcd(heure));<br/>
    Wire.write(decToBcd(joursdanslasemaine));<br/>
    Wire.write(decToBcd(joursdanslemois));<br/>
    Wire.write(decToBcd(mois));<br/>
    Wire.write(decToBcd(annee));<br/>
    Wire.endTransmission();<br/>
    }<br/>
    // Obtient la date et l’heure du DS1307.<br/>
    void getDateDs1307<br/>
   (byte *seconde,<br/>
    byte *minute,<br/>
    byte *heure,<br/>
    byte *joursdanslasemaine,<br/>
    byte *joursdanslemois,<br/>
    byte *mois,<br/>
    byte *annee)<br/>
    {<br/>
    // Réinitialiser le pointeur de registre.<br/>
    Wire.beginTransmission(DS1307_I2C_ADDRESS);<br/>
    Wire.write(0);<br/>
    Wire.endTransmission();<br/>
    Wire.requestFrom(DS1307_I2C_ADDRESS, 7);</p>
<p>    *seconde = bcdToDec(Wire.read() &amp; 0x7f);<br/>
    *minute = bcdToDec(Wire.read());<br/>
    *heure = bcdToDec(Wire.read() &amp; 0x3f); //Besoin de changer cela si 12 heures am / pm<br/>
    *joursdanslasemaine = bcdToDec(Wire.read());<br/>
    *joursdanslemois = bcdToDec(Wire.read());<br/>
    *mois = bcdToDec(Wire.read());<br/>
    *annee = bcdToDec(Wire.read());<br/>
    }<br/>
    void setup()<br/>
    {<br/>
    byte seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee;<br/>
    Wire.begin();<br/>
    Serial.begin(9600);</p>
<p>    seconde = 4;<br/>
    minute = 3;<br/>
    heure = 7;<br/>
    joursdanslasemaine = 5;<br/>
    joursdanslemois = 17;<br/>
    mois = 4;<br/>
    annee = 8;<br/>
    setDateDs1307(seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee);<br/>
    }<br/>
    void loop()<br/>
    {<br/>
    byte seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee;<br/>
    getDateDs1307(&amp;seconde, &amp;minute, &amp;heure, &amp;joursdanslasemaine, &amp;joursdanslemois, &amp;mois, &amp;annee);<br/>
    Serial.print(heure, DEC);<br/>
    Serial.print(« : »);<br/>
    Serial.print(minute, DEC);<br/>
    Serial.print(« : »);<br/>
    Serial.print(seconde, DEC);<br/>
    Serial.print( » « );<br/>
    Serial.print(mois, DEC);<br/>
    Serial.print(« / »);<br/>
    Serial.print(joursdanslemois, DEC);<br/>
    Serial.print(« / »);<br/>
    Serial.print(annee, DEC);<br/>
    Serial.print( » jours_dans_lasemaine: »);<br/>
    Serial.println(joursdanslasemaine, DEC);<br/>
    delay(1000);<br/>
    }</p>
<p>Mon problème c’est que je n’arrive pas à avoir la date et l’heure du pc mais que des 0 partout.<br/>
Il me semble que l’horloge n’arrive pas à démarrer !!!<br/>
Voici ce que m’affiche le port com :<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0<br/>
0:0:0 0/0/0 jours_dans_lasemaine:0</p>
 </section>

### ↳ Réponse — Yves Masur — 7 mai 2014 à 19:52

<section class="comment-content comment">
<p>En effet, pas très vivant… Je ne vois pas de défaut rédhibitoire dans le code. Pour  ma part, j’ai utilisé l’API TimeRTC pour la DS1307. Est-ce que l’adresse est juste? Essayez l’exemple d’une lib pour voir si ça 1) compile; 2) si un résultat plus parlant en sort.</p>
 </section>

### ↳ Réponse — Meriem — 12 mai 2014 à 07:40

<section class="comment-content comment">
<p>Veuillez m’excuser pour le retard de ma réponse (j’étais en congé et j’avais pas l’arduino sur moi).<br/>
Je suis une débutante concernant l’arduino , je viens d’essayer plusieurs librairies ainsi que les examples qui vont avec , mais je j’obtiens toujours que des 0 partout . J’ai revérifier aussi le câblage qui me semble bien . Je ne vois pas ce que j’ai commis comme faute .  ça fait plus d’une semaine que j’essaye de chercher la faute mais je ne trouve rien . Je dois avancer pour faire l’autre partie du projet…<br/>
Pouvez-vous m’envoyer svp en détail ce que je dois télécharger comme librairie ainsi que le sketch que vous avez utilisé …</p>
 </section>

### ↳ Réponse — Meriem — 12 mai 2014 à 07:44

<section class="comment-content comment">
<p>Concernant le cablage j’au juste mis :<br/>
Vcc avec 5v<br/>
GND avec GND<br/>
SDA avec SDA<br/>
SCL avec SCL</p>
</section>

### ↳ Réponse — Yves Masur — 12 mai 2014 à 19:55

<section class="comment-content comment">
<p>Essayez les points suivants:<br/>
– mettre les variables en global dans void setDateDs1307() et void getDateDs1307() pour être sût qu’il n’y ait pas d’entourloupe<br/>
– Castez les Wire.write(BYTE(val)); pour que ce ne soit pas un int avec un 0 Lo-Hi qui soit écrit<br/>
– vérifiez les signaux avec le scope sur SDA et SLC; éventuellement mettre des pull-Up de 22K ou 10K… Quelle est la longueur des fils?</p>
</section>

### Meriem — 13 mai 2014 à 14:09

<section class="comment-content comment">
<p>Bonjour,<br/>
j’ai finalement pu obtenir la date et l’heure … j’ai remplacer la carte due par uno et j’ai changé le module RTC (qui était grillé)…<br/>
Merci pour votre aide.<br/>
J’avais une autre question : Je veux récupérer la voltage proportionnel à l’intensité lumineuse d’un capteur solaire à l’aide de l’arduino et le module RTC qui me donnera la date et l’heure de ma mesure.<br/>
Ce que je veut obtenir : date, heure, Voltage.<br/>
j’ai commencé par faire ce programme :<br/>
[… code incomplet retiré …]<br/>
Mais le port série m’a sorti des valeur inapproprié à ce que je dois obtenir, et je ne suis pas sure de mon sketch .<br/>
Concernant le cabl<br/>
Pouvez-vous vérifié si j’ai oublié quelque chose ?<br/>
Merci d’avance.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
