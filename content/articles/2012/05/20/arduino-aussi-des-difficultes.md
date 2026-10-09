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

## Introductions aux difficultés(!)

Dans un article précédent ([http://microclub.ch/2012/02/19/arduino-un-succes-embarque/](/2012/02/19/arduino-un-succes-embarque/ "Arduino, un succès embarqué")), j’avais mis en lumière les facilités offertes par le concept Arduino: hard+soft défini, bon marché, secondes sources et dérivés de plusieurs fabricants de « shield » (soit les extension de la plaque de base Arduino).

Afin d’explorer rapidement les possibilités de mettre au point un prototype, j’ai décidé de mettre l’accent sur du matériel très complet et facile à mettre en œuvre, sans me focaliser sur le prix.

Après m’être renseigné sur le net, je penche pour une carte Arduino compatible, [Seeeduino Stalker](http://shop.boxtec.ch/product_info.php/products_id/40211 "Stalker") version 2.1. Elle a tout pour bien faire par son équipement d’origine: horloge RTC, support pour carte FLASH, faible consommation (elle est prévue pour faire du « data logger »).

Comme périphérique, j’opte pour le [Grove system](http://seeedstudio.com/wiki/GROVE_System "Grove system"). Avec le kit assez complet du [Mega Shield](http://shop.boxtec.ch/product_info.php/products_id/40498) et des relais, un servo et des câbles supplémentaires, je suis paré. Enfin, je le suppose. Voici les résultats de mes trouvailles, c’est assez long je le reconnais, avec à la fin, en résumé les recommandations et tour de main pour s’approprier l’Arduino.

## LCD Série

[![LCD](/media/2012/05/affiche_13-300x135.jpg "LCD")](/media/2012/05/affiche_13.jpg)

D’abord afficher quelque chose, me dis-je. En effet, lors de nos premiers essais, les infos sortantes du kit étaient envoyées en série sur le PC. Pour un système embarqué autonome, il faut un affichage. Celui de Grove est un [modèle série](http://seeedstudio.com/wiki/Grove_-_Serial_LCD_v1.0b "LCD serie"), la bibliothèque est disponible après quelques recherches sur le WEB. Ce principe économise les connexions, vu que seuls Rx et Tx sont nécessaires pour communiquer au lieu d’un port parallèle et des signaux de handshake. Un premier doute s’installe: quelle version hardware est la bonne? La réponse est sur le print du LCD: V2.1 Je prend le zip, le déballe et l’ajoute dans bibliothèque de l’environnement de développement intégré (EDI) Arduino 1.0, le redémarre… Et les problèmes arrivent.

### Erreur de compilation

La compilation coince avec un message pour le moins curieux: il manque « wprogram.h » dans « arduino.h ». Inutile d’essayer de la supprimer, ni de la corriger. Un coup de Google m’indique qu’il faut utiliser une nouvelle bibliothèque au lieu de « SoftwareSerial.h », soit « NewSoftSerial.h ». (A mon avis, c’est un peu débile d’appeler un logiciel « software », ou un programme « program » mais bon, passons). De nouveau une heure de mise en place de bibliothèque, déplacer l’ancienne (au cas où)… Sans résultats probants. Je ne suis pas seul: un *user* dépité s’exprime [ici](http://forums.adafruit.com/viewtopic.php?f=24&t=25002 "user dépité"). Il semble qu’un nombre important de sketch ne compilent plus et doivent être adaptés pour Arduino 1.0. Contrairement à ce que l’on pourrait croire, le 1.0 est un aboutissement, il y a des versions précédentes qui on été numérotées 1 à 23, toujours obtensibles ici: <http://arduino.cc/en/Main/Software>

### Correction de la bibliothèque

```
Le code devient donc:
// include the library code:
 #include &lt;SerialLCD.h&gt;
 #include &lt;NewSoftSerial.h&gt; //this is a must
```

Mais voilà, ça ne compile pas le moins du monde (même si c’est un « must »!)et il y a une tonne d’erreurs du même topo, pas du tout parlantes et obscures à souhait. Sur la page de « NewSoftSerial », il est dit qu’il faut modifier toutes les références à « NewSoftSerial » par « SoftwareSerial ». Je me lance donc dans le chercher/remplacer… Sans plus de succès à la compile. Les erreurs obscures ont changé, mais restent obscures. Le trouble s’accentue lorsque sur le [site de l’auteur](http://arduiniana.org/2011/01/newsoftserial-11-beta/ "(old NewsoftSerial)") de « NewSoftSerial », il est dit que désormais sa bibliothèque est en standard dans Arduino 1.0! Et bien entendu, sur le site officiel de Arduino, ce qui concerne le LCD est le mode **parallèle** et n’aide en rien.

Un petit tour dans les forums, et je me dis que la route et fausse, fausse! Je reprend un exemple de pilotage LCD série du site Arduino, qui lui compile! je fais milles essais avec une connexion différente, PIN différentes, mais pas la moindre réaction du LCD, même pas un curseur qui clignote, une ombre de pixel qui bouge, rien! J’en viens à me demander si mon module est KO?

Retour donc de « SoftwareSerial ». Et redémarage de l’éditeur, et recherche, parmi les milliers de sorties Google, et crawl dans les forums. Puis un soir, la lumière. De désespoir, je revisite le forum du site de Seeestudio, ou une indication de mise à jour de la librairie est à utiliser… ici: <http://www.seeedstudio.com/wiki/File:SerialLCD_for_Arduino1.0_20120307.zip;> c’est une version du 7.3.2012 qui est déposée… Et ça fonctionne. Ouf!!

## Se connecter à la carte Stalker

```
<a href="/media/2012/05/200px-Seeduino_Stalker_v2.2.jpg"><img alt="Seeduino_Stalker_v2.2" height="150" src="/media/2012/05/200px-Seeduino_Stalker_v2.2.jpg" title="Seeduino_Stalker_v2.2" width="200"/></a>
```

Ou: encore du sériel à manager. La carte Stalker de Seeeduino n’as pas de connexion USB, mais seulement du RS232  5V TTL par une série de broche à 2,54 mm. J’ai commandé un câble USB – RS232 [ici](http://shop.boxtec.ch/product_info.php/products_id/40385 "cable serie"), qui avait l’air de faire l’affaire, d’autant plus que le chip utilisé qui semble le roi de la transmission est le FTDI, et que sa version intégrée au Diduino du Pr Nicoud marche pile poil. Voici la connexion d’origine:

```
Color     FTDI     Stalker
---------------------------
Black     0V       0V
Braun     CTS      0V
Red       5V       5V
Orange    Tx       Rx
Yellow    Rx       Tx
Green     RTS      DTR
```

Mais une fois connecté… pas de liaison! Seule l’alimentation (via USB) a un effet sur Seeduino qui tourne, la fameuse LED de la pin 13 clignote.

Bien entendu, j’ai passé par rechercher les définitions et les câblages des CTS, RTS, DTR… Et vu avec désespoir que les signaux DSR, DCD n’étaient pas câblés. Essayer de démonter une fiche moulée tient de la haute voltige, inutile d’y penser. Évidemment, Rx et Tx, ça dépend du point de vue auquel on se place: le Rx de l’un est forcément le Tx de l’autre. Après un peu trop d’heures de recherche, voici la solution:

```
Color     FTDI     Stalker
---------------------------
Black     0V       0V
Braun     CTS      0V
Red       5V       5V
Yellow    Rx       Rx
Orange    Tx       Tx
Green     RTS      DTR
```

Soit simplement croiser Rx et Tx!

[![USB-serie](/media/2012/05/31402.jpg "USB-serie")](/media/2012/05/31402.jpg)

Visiblement, le CTS (clear to send) à 0V ne gêne pas: soit il n’est pas utilisé par Arduino 1.0, soit il le voit comme toujours OK.

Et encore une chose: j’ai remarqué avec le terminal que la Baud rate est à la moitié de la valeur donnée (4800 au lieu de 9600). J’ai supposé que le quarz de 8 MHz est à la demi fréquence standard… Mais en fait, il faut changer la config de l’EDI par: Tools-\>Board-\>Atmega 328, et la vitesse de transmission devient correcte.

## Carte mémoire SD

Maintenant que Staker est programmable, essayons ses possibilités. Et sa mémorisation sur SD. Dans les exemples qui sont disponibles sur le site de Seeeduino, il y a le sketch « StalkerV21_DataLogger_15Sec_NoSerialPort ». Mais l’inclusion de \<Fat16.h\> et de \<Fat16util.h\> ne passe pas…Bien que la lecture de forum me montre qu’il vaut mieux se contenter du format FAT16 bits, qui fait certes des blocs de fichiers plus gros que la FAT32, mais qui est visiblement mieux géré par Arduino. Si le formatage ou la lecture du chip sur le PC ne pose aucun problème, c’est par contre assez difficile d’insérer mécaniquement le chip entre quartz et le DS3231, soit le plus gros IC de la carte; ça va être coton pour la retirer et la lire.

[![SD](/media/2012/05/49001.jpg "SD")](/media/2012/05/49001.jpg)

Un essai avec l’exemple de la biliothèque \<SD.h\> compile, mais le pilote ne reconnais pas la carte. Allez! une recherche et le chargement de « fat16lib20111205.zip », déballé, installé et l’ajout de la lib \<Fat16\> dans l’EDI… coucou! revoilou l’erreur « WProgram.h ». Désormais, je sais qu’il est inutile de vouloir corriger quoique ce soit.

Un essais des exemples d’Arduino d’origine me montrent que certains passent: le test « fat16write » et « fat16read » compilent et laissent un fichier de bonne facture sur la SD. Ouf!

## Horloge DS3231

C’est le complément indispensable à un enregistrement de log: connaitre date et heure. Mais que dit l’exemple DS3231.CPP ? WProgram.h introuvable! Ben voyons… Une recherche de « DS3231 Arduino library »  me donne sur un site un zip, que je déballe et dépose dans la librairie, suivi de la relance de l’EDI (refrain connu).

Cette fois, la leçon ayant porté, je commence par la base Arduino 1.0, pour voir ce qui fonctionne parmi les sketches de: File -\>Examples-\>Time. Par exemple, « TimeRTC », qui compile sans souci, bien que prévu pour le DS1307. Chargé sur la carte Stalker, il affiche par le terminal:

```
03:06:01 1 1 2000
```

et compte en continu chaque seconde, même après un reset. Si je retire la prise USB et la remet, ça recommence à 3h de l’an 2000; mais une fois la pile CR2032 clippée dans son logement, la date ne revient plus en arrière en cas de coupure de l’alimentation. C’est encourageant; je change maintenant l’inclusion \<DS1307RTC.h\> par \<DS3231.h\> pour profiter des performances du chip DS3231. Mais qui revoilou? WProgram.h introuvable!

Une comparaison des datasheet – rapide, hein, ne me prenez pas au mot – montre que je peux me passer pour le moment des 2 alarmes programmables et du capteur de température dont est doté le DS3231. Je me rabat donc sur le soft de base du DS1307, chip que je connais, l’ayant utilisé avec succès pour le projet de la barrette, décrit [ici](/2011/03/25/projet-barrette-livrable/ "Barrette").

Mais il me faut tout de même mettre cette clock à l’heure; ce que je tente par l’exemple « TimeRTCSet ». Difficulté: il faut via le terminal, indiquer le nombre de secondes depuis 1970 pour qu’un SET soit fait. Si ça ne vous dit rien, consultez la définition de [EPOCH](http://fr.wikipedia.org/wiki/Epoch "Epoch"). Cependant le programme est fonctionnel. Et l’horloge réagit correctement.

## Servo

Pas d’intelligence artificielle, mais bien d’un servo-moteur que l’on va implémenter. La première difficulté est de découvrir comment connecter un servo avec 3 fils sur des connecteurs à 4 fils du Grove system. Des câbles existent, mais le raccord sera femelle-femelle! Grâce à Laurent, auteur [bien connu sous le pseudo de Franic](/membres/ "Membres"), j’ai une liste des modèles de servo avec les couleurs des fils: +5V, 0V et pulse de commande. Grâce à ma collection de câbles, je peux brancher le servo sans sortir mon attirail électronique. Dans ce genre de raccord, le risque est grand de faire fumer du matériel, voir la carte CPU par une mauvaise connexion. Ici, avec un seul petit moteur, je ne dépasse pas le courant de 350 mA: c’est donc compatible avec l’alim via le port USB du PC.

L’exemple de sketch File-\>Examples-\>Servo-\>Knob, légèrement modifié pour lire un potentiomètre qui donne la consigne, fonctionne du premier coup.

# Conclusions et recommandations

### Version de soft

Arduino est bien l’ensemble hard+soft large, fourmillant et plein de ressources qui est promis. Par contre, pour le novice qui débute en programmation et qui ne connait pas forcément le hard, il y a plein de chausse-trappes. Le principal, on l’a vu, est lié à l’évolution du logiciel. Nombre de drivers et exemples ne sont pas à jour, et la difficulté est grande de savoir si oui ou non un logiciel est prêt pour *notre* solution.

[![wProgram_h](/media/2012/05/wProgram_h-300x229.jpg "wProgram_h")](/media/2012/05/wProgram_h.jpg)

Un symptôme classique est l’erreur « WProgram.h » à la compilation. Dire dans un forum, comme je l’ai vu qu’il faut *soi-même dépanner le soft, c’est ainsi que l’on apprend à programmer* est bien joli… mais ça n’aide pas beaucoup. Les pilotes mis à jour ont l’inclusion suivante:

```
#if defined(ARDUINO) &amp;&amp; ARDUINO &gt;= 100
#include "Arduino.h"    // for digitalRead, digitalWrite, etc
#else
#include "WProgram.h"
#endif
```

Ce code tient compte de la version, qui a fait un saut de 023 à 100.

On ne peut donc pas tabler sur un hard offert par un fabricant, sans savoir s’il sera fonctionnel avec la dernière version de l’EDI Arduino. On ne peut pas demander à un novice en la matière de maîtriser à la fois le hard, le soft qui est bien entendu spécifique sur une cible 8 bits, de maîtriser l’architecture interne du CPU et des astuces propres à des déclinaisons hardware comme la compatibilité entre les shield. Je m’attendais plus à une sorte de LEGO, où il suffit de choisir les blocs hard et soft pour construire un projet autant en hardware qu’en software.

Si l’on veut sortir des exemple unitaires (quoique, vu les difficultés évoquées ci-dessus, ce n’est pas donné…) pour réaliser un ensemble, une solide connaissance logicielle et matérielle est nécessaire. Ou bénéficier de l’aide d’un groupe actif via un forum!

### l’EDI

Il fait assez minimaliste, par rapport à d’autre environnements intégrés: l’EDI Arduino se contente de colorer en brun les mots clef et les fonctions de la bibliothèque, les commentaires en vert, les chaînes en bleu. Un éditeur comme [Notepad++](http://notepad-plus-plus.org/fr) se révèle bien plus  efficace: syntaxe colorée complète, recherche/remplacement, comparaison, complétion, multi-vues, etc, etc! De plus, l’EDI Arduino n’a pas d’aide contextuelle. Par rapport à d’autre compilateurs, l’utilisation du « make » serait plus productive: en effet, pourquoi tout recompiler avant d’envoyer le fichier sur la cible alors qu’on vient de le faire? Les erreurs ne renvoient pas non plus au fichier/ligne fautif par un clic sur le message.

Et diable, pourquoi ne se rappelle-t-il pas de la position de la fenêtre?  à chaque fois qu’on l’ouvre, on doit l’étirer!

Comme il est gratuit, on le prend comme il est. Mais on peut rêver à mieux.

### Ajout /mise à jour des librairies

L’opération semble simple: copier les fichiers proposés – souvent zippés – dans le répertoire Arduino-1.0\librairies. Mais si l’on peut nommer le répertoire comme une variable (lettre et chiffres), un test est fait au démarrage de l’EDI. Par exemple, je crée une copie de « SerialLCD », en SerialLCD-2, on aura une erreur:

[![lib-conflict](/media/2012/05/lib-conflict-300x103.jpg "lib-conflict")](/media/2012/05/lib-conflict.jpg)

Qui est clair dans **ce** contexte. Si c’est une mise à niveau et que vous voulez garder l’ancienne, il faudra très certainement la retirer de la librairie et la déposer ailleurs sur votre espace de stockage. Et la swapper avec la nouvelle si vous devez reconstruire une ancienne version. Heureusement, le ZIP conserve les dates des fichiers… ce qui m’a permis de lever un doute lors de mes multiples modifications concernant le LCD.

A chaque coup, ne pas oublier d’arrêter toutes les instances de l’EDI, qui a la fâcheuse option d’en lancer une nouvelle à chaque ouverture de fichier. C’est lourd et générateur de confusion.

### La connectique Grove system

On l’a entrevu à la connexion du LCD, il y a 4 fils par prise: 0V, 5V, signal 1 et signal 2. Sur la prise suivante, les alim, signal2 et signal 3… voir le diagramme [ici](http://www.seeedstudio.com/wiki/File:Stem-diagram-conn.jpg "Stem-diagram-conn.jpg"). C’est futé, mais.. ça peut amener à des problèmes subtils si on utilise les 2 signaux par un connecteur: court circuit, double charge. Au point de vue montage, c’est la perplexité: les trous de fixation demandent des vis de 2 mm! De plus comment voulez-vous monter un bouton sur face avant, avec un connecteur plus haut? [![bouton](/media/2012/05/bouton-300x278.jpg "bouton")](/media/2012/05/bouton.jpg) Le problème est bien entendu le même pour LED et potentiomètre. On le voit sur cette image, la fixation est simple: un fil de wrapp passe dans les trous du print pour l’attacher à la planchette percée.

Il serait intéressant d’avoir des plugs à 90°. Heureusement, il y a aussi des plaque pour prototype, qui permettent de monter son électronique à sa façon ([ici](http://shop.boxtec.ch/product_info.php/manufacturers_id/22/products_id/40780 "Prototype")).

[![cables](/media/2012/05/cables-150x150.jpg "cables")](/media/2012/05/cables.jpg) Tous les câbles ont la même longueur; dommage, ça devient vite un brouillard de câble, bien que ce soit acceptable pour un prototype. Il faudra par contre les attacher et les marquer.

Malgré tout, on peut construire des montages hard + soft sans sortir le fer à souder et une panoplie d’outils pas forcément à portée de toute les bourses.

## Références

Elles sont intégrées dans le textes par liens.

Yves Masur (5/2012)

## Commentaires

### Michel Vonlanthen — 21 mai 2012 à 10:08

Bravo Yves, bien travaillé… pour nous !

Actuellement je suis en stand-by en ce qui concerne l’Arduino, pas une seconde à lui consacrer, je dois me défendre contre ceux qui veulent me barrer la vue sur les Alpes avec des tours de 60 mètres de haut (demainbussigny.ch)… Mais je reprendrai tout ça à fin juin. Donc pas beaucoup plus d’expérience, mais j’ai constaté les mêmes choses que toi, notamment en ce qui concerne la librairie LCD série. J’en suis arrivé à faire ma propre librairie, au moins elle fonctionne. Je n’ai pas été très loin, elle ne fait pas encore grand chose, mais je sais au moins que ma carte LCD est OK. Je vois que tu avais le même doute…

J’ai un tas de circuits et de shields à tester et je m’en réjouis. Pour le moment j’ai terminé mon émetteur TV et il fonctionne bien. Je dois encore lui augmenter la puissance en lui rajoutant un ampli, ce sera mon prochain boulot lorsque je serai de retour des USA. Ensuite l’étendre à d’autres bandes et c’est pour ça que j’ai besoin de la LCD série, de façon à libérer des pins pour autre chose. Là, avec la commandes du panneau avant, du synthétiseur et la mesure de température et de la tension d’alimentation je suis complet.\
Une fois la doc mise au propre et éventuellement publiée (sur mon site en tous cas), je m’attaquerai au logger pour caractériser mon chauffage électrique et pour préparer son évolution vers le solaire.

Toutes ces expériences m’amènent à la conclusion que, quoi qu’on fasse, on ne pourra jamais s’éviter de connaitre les bases de l’électronique si on veut travailler avec l’Arduino et systèmes du même genre. De mon point de vue, il est illusoire de croire qu’on va pouvoir faire des montages hard-soft sans aucune connaissance en électronique. Si on ne sait même pas calculer une loi d’Ohm, on sera bloqué par des bricoles, on fera fumer son matos, et le tout passera à la poubelle et dans les souvenirs ! C’est la même chose du point de vue software. Je trouve l’Arduino idéal parce qu’on peut très rapidement passer de l’idée à la réalisation, sans devoir ré-inventer la roue. Par contre, si on n’a jamais pratiqué la programmation, ça pose quand-même quelques problèmes. C’est peut-être un système idéal pour les vieux briscards des Gas-Fets pétés comme nous, mais les vrais néophytes qui ne connaissent encore rien à rien seront mieux servis par un système du genre Lego par exemple. On ne peut pas tout avoir…

Pour des kids, le mieux est qu’il restent en atmosphère pilotée par un moniteur, encadrés dans un cours, afin qu’ils soient guidés pour résoudre ces problèmes-là. Sinon c’est la cata et le découragement assurés. J’ai tenté d’intéresser mes petits-enfants à la chose mais sans grand succès. Leurs parents m’ont trop vus passer des nuits entières dans mon gourbi pour penser que ce que je fais soit amusant. Et ils ont transmis cette mémoire-là à leurs propres enfants sous forme d’anticorps à l’électronique…

Une autre constatation en passant: quelque chose qu’on obtient trop facilement a peu de valeur. C’est peut-être ça qui pèche avec mes tentatives d’intéresser mes petits à l’électronique. Comme ils auraient tout à disposition, y compris un prof bienveillant, ça leur semble trop facile et pas assez origjnal. Ca en aurait peut-être plus si c’était amené par un copain et qu’ils doivent suer du burnous avant de voir clignoter la led.

ARDUINamitiés\
michel vonlanthen

### ↳ Réponse — Meriem — 7 mai 2014 à 07:29

heey,\
Actuellement j’ai comme « projet » de développer un logger pour un capteur solaire.\
En ce moment j’ai câblé l’arduino DUE et l’horloge RTC … j’ai commencé par faire un premier programme que je vous le laisserai ci-dessous. mon programme doit mettre a l’heure le système manuellement ensuite l’ envoyer a l’horloge puis régler la fréquence d’acquisition et lancer les mesures. Je dois récupérer et afficher les mesures puis arrêter les mesures quand je veux.\
Voici le premier sketch:\
\#include « Wire.h »\
\#define DS1307_I2C_ADDRESS 0x68\
//Pour convertir des nombres décimaux normal à des nombres décimaus codés binaire\
byte decToBcd(byte val)\
{\
return ( (val/10\*16) + (val%10) );\
}\
//Pour convertir des nombres binaires à des nombres normales\
byte bcdToDec(byte val)\
{\
return ( (val/16\*10) + (val%16) );\
}

void setDateDs1307\
(byte seconde, // 0 à 59 secondes\
byte minute, // 0 à 69 minutes\
byte heure, // 1 à 23 heures\
byte joursdanslasemaine, // 1 à 7 jours\
byte joursdanslemois, // 1 à 28jours ou 1 à 29jours ou 1 à 30jours ou 1 à 31jours\
byte mois, // 1 à 12mois\
byte annee) // 0-99\
{\
Wire.beginTransmission(DS1307_I2C_ADDRESS);\
Wire.write(0);\
Wire.write(0x80);\
Wire.write(decToBcd(seconde));\
Wire.write(decToBcd(minute));\
Wire.write(decToBcd(heure));\
Wire.write(decToBcd(joursdanslasemaine));\
Wire.write(decToBcd(joursdanslemois));\
Wire.write(decToBcd(mois));\
Wire.write(decToBcd(annee));\
Wire.endTransmission();\
}\
// Obtient la date et l’heure du DS1307.\
void getDateDs1307\
(byte \*seconde,\
byte \*minute,\
byte \*heure,\
byte \*joursdanslasemaine,\
byte \*joursdanslemois,\
byte \*mois,\
byte \*annee)\
{\
// Réinitialiser le pointeur de registre.\
Wire.beginTransmission(DS1307_I2C_ADDRESS);\
Wire.write(0);\
Wire.endTransmission();\
Wire.requestFrom(DS1307_I2C_ADDRESS, 7);

\*seconde = bcdToDec(Wire.read() & 0x7f);\
\*minute = bcdToDec(Wire.read());\
\*heure = bcdToDec(Wire.read() & 0x3f); //Besoin de changer cela si 12 heures am / pm\
\*joursdanslasemaine = bcdToDec(Wire.read());\
\*joursdanslemois = bcdToDec(Wire.read());\
\*mois = bcdToDec(Wire.read());\
\*annee = bcdToDec(Wire.read());\
}\
void setup()\
{\
byte seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee;\
Wire.begin();\
Serial.begin(9600);

seconde = 4;\
minute = 3;\
heure = 7;\
joursdanslasemaine = 5;\
joursdanslemois = 17;\
mois = 4;\
annee = 8;\
setDateDs1307(seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee);\
}\
void loop()\
{\
byte seconde, minute, heure, joursdanslasemaine, joursdanslemois, mois, annee;\
getDateDs1307(&seconde, &minute, &heure, &joursdanslasemaine, &joursdanslemois, &mois, &annee);\
Serial.print(heure, DEC);\
Serial.print(« : »);\
Serial.print(minute, DEC);\
Serial.print(« : »);\
Serial.print(seconde, DEC);\
Serial.print( » « );\
Serial.print(mois, DEC);\
Serial.print(« / »);\
Serial.print(joursdanslemois, DEC);\
Serial.print(« / »);\
Serial.print(annee, DEC);\
Serial.print( » jours_dans_lasemaine: »);\
Serial.println(joursdanslasemaine, DEC);\
delay(1000);\
}

Mon problème c’est que je n’arrive pas à avoir la date et l’heure du pc mais que des 0 partout.\
Il me semble que l’horloge n’arrive pas à démarrer !!!\
Voici ce que m’affiche le port com :\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0\
0:0:0 0/0/0 jours_dans_lasemaine:0

### ↳ Réponse — Yves Masur — 7 mai 2014 à 19:52

En effet, pas très vivant… Je ne vois pas de défaut rédhibitoire dans le code. Pour ma part, j’ai utilisé l’API TimeRTC pour la DS1307. Est-ce que l’adresse est juste? Essayez l’exemple d’une lib pour voir si ça 1) compile; 2) si un résultat plus parlant en sort.

### ↳ Réponse — Meriem — 12 mai 2014 à 07:40

Veuillez m’excuser pour le retard de ma réponse (j’étais en congé et j’avais pas l’arduino sur moi).\
Je suis une débutante concernant l’arduino , je viens d’essayer plusieurs librairies ainsi que les examples qui vont avec , mais je j’obtiens toujours que des 0 partout . J’ai revérifier aussi le câblage qui me semble bien . Je ne vois pas ce que j’ai commis comme faute . ça fait plus d’une semaine que j’essaye de chercher la faute mais je ne trouve rien . Je dois avancer pour faire l’autre partie du projet…\
Pouvez-vous m’envoyer svp en détail ce que je dois télécharger comme librairie ainsi que le sketch que vous avez utilisé …

### ↳ Réponse — Meriem — 12 mai 2014 à 07:44

Concernant le cablage j’au juste mis :\
Vcc avec 5v\
GND avec GND\
SDA avec SDA\
SCL avec SCL

### ↳ Réponse — Yves Masur — 12 mai 2014 à 19:55

Essayez les points suivants:\
– mettre les variables en global dans void setDateDs1307() et void getDateDs1307() pour être sût qu’il n’y ait pas d’entourloupe\
– Castez les Wire.write(BYTE(val)); pour que ce ne soit pas un int avec un 0 Lo-Hi qui soit écrit\
– vérifiez les signaux avec le scope sur SDA et SLC; éventuellement mettre des pull-Up de 22K ou 10K… Quelle est la longueur des fils?

### Meriem — 13 mai 2014 à 14:09

Bonjour,\
j’ai finalement pu obtenir la date et l’heure … j’ai remplacer la carte due par uno et j’ai changé le module RTC (qui était grillé)…\
Merci pour votre aide.\
J’avais une autre question : Je veux récupérer la voltage proportionnel à l’intensité lumineuse d’un capteur solaire à l’aide de l’arduino et le module RTC qui me donnera la date et l’heure de ma mesure.\
Ce que je veut obtenir : date, heure, Voltage.\
j’ai commencé par faire ce programme :\
\[… code incomplet retiré …\]\
Mais le port série m’a sorti des valeur inapproprié à ce que je dois obtenir, et je ne suis pas sure de mon sketch .\
Concernant le cabl\
Pouvez-vous vérifié si j’ai oublié quelque chose ?\
Merci d’avance.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
