---
title: "Des PICs – pourquoi faire ? – comment faire ?"
date: "2003-11-11T08:57:29"
lastmod: "2015-04-24T23:20:25"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["pic"]
url: "/2003/11/11/des-pics-pourquoi-faire-comment-faire/"
wordpress_id: 11
comment_count: 0
---
<h3 align="center">J.D. Nicoud</h3>
<p>La famille PIC continue à s’enrichir. En 8 pattes, on a enfin des versions 12F avec le répertoire d’instruction des 16F, des canaux analogiques et naturellement l’oscillateur interne. En 16 pattes, le 16F627/628 a aussi l’oscillateur interne et une interface série. Le nouveau 16F88, si on peut le programmer, est encore plus complet (8A/D, Série, SPI, I2C). La famille 16F87x offre plus d’entrées-sorties. Un 40 pattes (16F871 ou 16F877) est très utile pour mettre au point des applications avec des tout petits processeurs, comme on le verra plus loin.</p>
<p>Maurice Wulliens a dessiné 4 circuits pour disposer d’environnements de développement adaptés à vos diverses applications. Le programmateur est piloté par le graticiel ICprog. Trois cartes de développement sont à disposition pour les processeurs de 8, 14, 18, 28 et 40 pattes (voir <a href="http://www.didel.com/picg/" target="_blank">www.didel.com/picg/</a>).</p>
<p>SmileNG, et son nouveau frère Picolo qui tourne sur Linux, Mac et Windows, offre l’assembleur CALM dont les notations sont nettement plus lisibles que celles de Microchip. La documentation didactique permet de rapidement apprendre à programmer et à apprécier les jolis trucs de programmation du PIC. Une librairie de programmes expliquée facilite les applications.</p>
<p>Ecrire un programme pour le PIC suppose une compréhension des nombres binaires, de leur représentation en hexa et une connaissance des instructions et pseudoinstructions. Mais il y a très peu d’instructions et pas de modes d’adressage compliqués. On se familiarise très vite en exécutant quelques programmes variés.<!--more--></p>
<p>Par exemple, pour qu’un système moteur fasse le va-et-vient entre deux fins de courses, il faut tester ces fin de courses et adapter le sens du moteur. Cela s’écrit</p>
<pre>Loop : 	TestSkip,BS PortC :#bLimitMax
	Jump Recule ; Si le contact est fermé, la ligne  est à zéro (bit clear)
	TestSkip,BS PortC :#bLimitMin
	Jump Avance
	Jump Loop
Recule : Move #MotRec,W
	Move W,PortB
	Jump Loop
Avance : Move #MotAv,W
	Move W,PortB
	Jump Loop</pre>
<p>Pour que l’assembleur soit satisfait, il faut rajouter les déclarations pour définir les bits ou mots binaires associés au câblage des poussoirs et du moteur sur les ports B et C. Il faut ajouter quelques instructions au début pour définir le processeur et initialiser les ports, et quelques pseudo-instructions à la fin pour préparer la programmation.</p>
<p>Pour la mise au point d’un programme, il faut pouvoir visualiser par où il passe, et quel est l’état de certaines variables. Ceci sans perturber le fonctionnement de façon significative. Un simulateur est utile pour les premiers exercices, et pour tester des fonctions arithmétiques. Un émulateur est bien, mais cher, et n’existe que pour les PIC haut de gamme. La solution la plus commode est de disposer d’une interface série et d’afficher sur l’écran d’un terminal ce que l’on décide en complétant son programme par des modules d’affichages qui peuvent devenir assez encombrants, et prendre un temps d’exécution non négligeable. S’il y a des timings critiques, un port libre est essentiel, comme on le verra plus loin.</p>
<p align="center"><a href="/media/2007/11/2003_img_1.jpg" target="_blank"><img alt="2003_img_1.jpg" height="389" src="/media/2007/11/2003_img_1.jpg" width="574"/></a></p>
<p>Dans le cas ou l’environnement de mise au point est différent de l’environnement de l’application, on effectuera dès le début des assemblages conditionnels. Si la constante Test=1, on déclare ce qui correspond au processeur de test. On peut déclarer d’autres constantes liées à des tests que l’on veut pouvoir faire apparaître ou disparaître facilement, mais il ne faut pas s’empêtrer dans un nombre excessif d’options. Il est sage de vérifier fréquemment la compatibilité (assemblage et exécution avec Test=0 et Test=1) pour éviter que l’environnement de test ne devienne incompatible avec la version finale.</p>
<p>La figure précédente montre un exemple où un 16F676 dans son boîtier de 59 milligrammes a été remplacé pour le développement par un 16F871 en boîtier DIL 40 broches (sur kit WdPicDev87x). Le 16F871 offre une liaison série qui permet de visualiser des variables sur l’écran d’un PC sans interagir avec l’application, car la communication série est la seule tâche du programme principal, toute l’application étant gérée par des tâches synchrones par interruption. Les ports B, C et E ont été très utiles pour afficher des variables et compteurs en temps réel, aussi via le convertisseur D/A (voir plus loin).</p>
<p>Disposer d’un port 8 bits avec des leds permet de faire beaucoup, et l’affichage d’une variable quelconque ne prend que 2 microsecondes. On ne peut naturellement pas passer d’une variable à l’autre, et si la variable varie rapidement, l’affichage est guère utile. Néanmoins, notre conseil est dans tous les cas, garder un port 8 bits pour afficher des variables, et ceci jusqu’à la fin de la mise au point.</p>
<p>A noter que si les diodes sont actives lorsque le port est à zéro, il suffit d’inverser tous les bits lors du transfert :</p>
<pre>Not Variable,W  Move W,PortB</pre>
<p>Un convertisseur D/A sur un port 8 bits peut être très utile lorque le signal varie et que l’on dispose d’un oscilloscope, à mémoire de préférence. Si on mesure une vitesse, ou l’écart par rapport une consigne, ce convertisseur 4, 6 ou 8 bits est facile à réaliser avec un réseau de résistances R/2R ou en utilisant un AD588, Max506, DAC0808 ou équivalent.</p>
<p><a href="/media/2007/11/2003_img_3.jpg" title="2003_img_3.jpg"><img align="right" alt="2003_img_3.jpg" height="472" hspace="3" src="/media/2007/11/2003_img_3.jpg" vspace="3" width="271"/></a>Câbler un réseau R/2R sur un connecteur qui s’enfiche sur les connecteurs des modules WdPicDev est facile. La précision 8 bits est rarement nécessaire, et il peut être utile d’avoir un module qui ne prend que les 6 bits ou 4 bits de poids faible.</p>
<p><a href="/media/2007/11/2003_img_2.jpg" title="2003_img_2.jpg"><img alt="2003_img_2.jpg" height="162" src="/media/2007/11/2003_img_2.jpg" width="373"/></a></p>
<p>Par exemple, pour dépanner un programme qui décode un message IR formé d’impulsions de longueur variable, visualiser le compteur/ décompteur associé à la mesure de durée des impulsions aide considérablement à la mise au point, et à l’étude du comportement en cas de mauvaises transmissions.</p>
<p>Pour chaque application, il faut bien réfléchir comment elle sera mise au point, et ne pas hésiter à investir du temps pour construire un environnement de développement adapté. La mise au point d’un programme est toujours plus longue que l’on croit!</p>
<h3>Applications</h3>
<p>Toute application a un certain nombre d’entrées et de sorties. Il y a éventuellement un ampli-op sur une entrée, et fréquemment des transistors ou circuits amplificateurs sur des sorties, mais plus tellement de compteurs, monostables et portes logiques du bon vieux temps. Le soft sait faire beaucoup de choses. Citons 6 types d’applications.</p>
<ol>
<li>Un PIC peut mesurer des longueurs d’impulsions, et à partir d’un signal infrarouge ou radio démodulé, commander des moteurs et toutes sortes de gadgets. Une télécommande universelle aurait quelques boutons en plus et une diode infrarouge pour commander divers appareils à commande infrarouge. Le programme apprendrait les codes quelques utilisés avec chaque appareil, et saurait les rejouer.</li>
<li>Avec des capteurs et des amplis moteurs, on construit un robot. Les capteurs qui on besoin d’un séquencement compliqué, comme une caméra linéaire ou un capteur de distance à ultrasons, ont tout naturellement leur propre PIC pour décharger le processeur principal.</li>
<li>Dallas a de très jolis circuits à 3 pattes qui permettent de faire un bus de plusieurs dizaines de mètres commandé par des impulsions de longueur variable. C’est l’idéal pour un système de surveillance qui déclenche des alarmes, ou met en route une caméra vidéo et un enregistreur, ou pour optimiser chauffage, cellules solaires, stores, ventilation, etc, avec des PICs en réseau qui s’occupent de chaque appareil.</li>
<li>Un codeur incrémental associé à un affichage, ou un mini-joystick à 4 poussoirs comme dans les appareils de photos, permet de se déplacer dans les menus d’un écran.
<p align="center"><a href="/media/2007/11/2003_img_4.jpg" title="2003_img_4.jpg"><img alt="2003_img_4.jpg" height="162" src="/media/2007/11/2003_img_4.jpg" width="465"/></a></p>
</li>
<li>Un potentiomètre peut encore s’avérer utile pour commander manuellement un train électrique. Là aussi, les capteurs et actuateurs sont nombreux et il faut les mettre en réseau.</li>
<li>Une horloge au look spécial et à l’affichage original n’a besoin que d’un circuit horloge avec son quartz 32 kHz. Certains nouveaux PICs ont même la possibilité de brancher un quartz 32 kHz, et d’utiliser l’oscillateur interne plus rapide si les tâches à exécuter sont complexes.</li>
</ol>
<p><em>(article paru dans le journal Mi-Chronique, No 70, Novembre 2003. Re publié ici à partir du pdf le 11/11/07 par Goulu en 12 minutes chrono, pour test)</em></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
