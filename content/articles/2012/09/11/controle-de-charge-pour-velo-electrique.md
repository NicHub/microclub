---
title: "Contrôle de charge pour vélo électrique"
date: "2012-09-11T19:47:38"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "barrette", "ecologie", "embarque", "energie", "hardware", "programmation"]
url: "/2012/09/11/controle-de-charge-pour-velo-electrique/"
wordpress_id: 974
comment_count: 0
---
<h2>Chargeur de vélo électrique</h2>
<p>Un vélo électrique se meut par le pédalage de l’utilisateur et lui offre une assistance importante, jusqu’à 250%. Autant dire que les montées deviennent dérisoire, avec ce réglage… Puis, de retour @home, on branche la batterie sur un chargeur. Les expériences décrites ici sont basées sur un ensemble Bosch, livré avec un vélo de marque Cresta. La batterie lithium-ion est donnée à 36 V et 10Ah; le moteur a une puissance de 250 W. Théoriquement, on peut rouler à pleine puissance 360/250 = 1H et 26 minutes. Ce qui n’arrive jamais. A 25 km/H, on parcourrait 36 km; Bosch indique qu’au plat et conduite économe(?), ce devrait être 145 km. La vérité est entre-deux…</p>
<p>Quel est le processus de charge? Une fois connecté à la batterie, le chargeur a deux vitesses de chargement: la rapide par défaut, à 4 A (durée 2,5H selon Bosch) et un ventilateur s’active ; la lente à 1 A (8H, toujours selon Bosch; mais là on aurait seulement 8 AH, petit problème de calcul!). Une protection de surchauffe limite a charge si la t° dépasse 40°C. Donc le chargeur devrait consommer, avec 10% de pertes environ 160W en mode rapide et 40W en mode lent. Et quand il a fini?</p>
<p>Selon ma mesure, il reste environ 90-100 mA sur 230VAC, on a donc une<strong> puissance résiduelle de plus de 20 Watts</strong>! (en fait 20 VA, si l’on tient compte du réactif). C’est horrible, non? Surtout que l’on ne va pas aller au milieu de la nuit débrancher le bazar au garage! Et chaque fois qu’il pleut et que mon fils n’utilise pas son vélo, il risque bien d’y passer un jour de plus branché ainsi. Le constructeur signale qu’il n’est pas « recommandé de laisser la batterie raccordée en permanence au chargeur ». La fameuse <a href="/2011/03/25/projet-barrette-livrable/" title="Projet « Barrette » livrable!">barrette</a> secteur permet de couper une alimentation à une heure donnée; mais dans un tel cas, son utilisation n’est pas adaptée: ce ne sera jamais la bon moment de couper: trop tôt ou trop tard. Il vaut la peine de développer un proto dédié à cette tâche.</p>
<h2>Projet</h2>
<p>La définition algorithmique de base est assez simple: un relais commuté en auto-maintient met le chargeur du vélo sur le 230VAC, ceci tant que la puissance consommée sur le réseau est supérieure à 23 W. En dessous, il déclenche. Ça serait <em>low-cost</em> et ça fonctionnerait à merveille. Si Bosch avait une sensibilité écologique, c’est exactement ce qu’il aurait dû faire…</p>
<p>A la base, il faut une mesure de courant. Dans le fond, elle n’a pas besoin d’une grande précision; mais comme j’ai un prototype électronique qui est justement conçu pour répondre à un tel cas (<a href="/2012/07/02/mesure-de-courant-surprise/" target="_blank" title="Mesure de courant – surprise">il a été présenté ici</a>), avec un microprocesseur alimenté en 5VDC, on peut faire plus. Comme la mesure du courant de ce dispositif est assez précise, qui offre une résolution à 230 VAC au watt, il est possible de le coupler avec un timer et de sommer chaque seconde les courants/puissances instantanés pour en calculer l’énergie totale à la fin de la charge.</p>
<h3>Choix du matériel, basé sur Arduino</h3>
<p>Voilà un bon projet pour le système <a href="http://www.arduino.cc/" target="_blank" title="Arduino">Arduino</a>, présenté <a href="/2012/02/19/arduino-un-succes-embarque/" target="_blank" title="Arduino: un succès embarqué">ici il y a peu</a>! Pour le montage, je demande à mes collègues électriciens de récupérer un boitier électrique comportant une prise Type 13, un rail DIN de 35 mm et des bornes à ressort. Dans le but futur d’enregistrer les données, il me faut une carte compatible Arduino, avec une carte SD en formatée en FAT; une horloge temps réel RTC: ce sera la Stalker de Seeeduino.</p>
<p>Pour la rapidité du montage et de connexion, je choisi du même constructeur un kit <a href="http://www.seeedstudio.com/wiki/GROVE_System" target="_blank" title="Grove shield">Grove Shield</a>. Et de celui-ci, j’en retiens un relais, pour couper l’alimentation; un bouton pour valider un menu; un potentiomètre pour régler et/ou défiler un menu; une LED; un buzzer pour signaler la transition; ainsi que le charmant afficheur LCD pour indiquer les infos d’état et de consommation. L’alimentation est choisie avec soin: un bloc <a href="http://www.tracopower.com/products/ac-dc-power-supplies/" target="_blank" title="Traco">Traco</a> 230VAC / 5VDC. Grâce à son bon rendement, le montage consommera moins de 0.8 Watt.</p>
<p>C’est certes un tout passablement luxueux. Si <a href="http://www.lausanne.ch/view.asp?DocId=20627" target="_blank" title="Lausanne">Mme vélo de la Ville de Lausanne</a> m’en demande pour les bi-cycles qui roupillent au garage, il faudra en repenser l’industrialisation. Toute la partie électronique vient montée sur une planchette. Voici ce que ça donne:</p>
<p><a href="/media/2012/09/Load_control_interieur.jpg"><img alt="" height="636" src="/media/2012/09/Load_control_interieur-951x1024.jpg" title="Load_control_interieur" width="591"/></a></p>
<p>On y voit, de gauche à droite: la prise T-13 « slave »; les bornes à ressort; la planchette comportant l’électronique. Tout en bas, le bloc bleu est la bobine de mesure de courant. Comme la puissance mesurée est réduite, le fil jaune qui est parcouru par le courant total est enroulé 10 x, afin d’obtenir la sensibilité suffisante. Le couvercle reçoit le bouton « start » et l’afficheur.</p>
<h2>Première version du logiciel</h2>
<p>Pour mettre au point une première version du logiciel au coin de mon bureau, j’utilise la plateforme <a href="http://www.didel.com/" target="_blank" title="Diduino">Diduino </a>(mis au point par le Pr. Nicoud), avec un Grove Shield, identique à celui du montage. La boucle principale à la structure suivante:</p>
<ul>
<li>Délai de 1000 ms (soit une seconde)</li>
<li>Lecture du courant</li>
<li>Logique de commutation</li>
<li>Affichage des infos: nb de secondes écoulées, courant</li>
</ul>
<p>Malheureusement, c’est un peu simple. En assembleur, ça pourrait passer, si l’exécution est infiniment plus rapide que la boucle d’attente. Diminuer le délai du temps pris par les instructions de traitement (env. 70 ms) ajuste le quelque peu timing, mais ça reste un peu naïf. C’est cependant suffisant pour un premier test validant le matériel.</p>
<h3>Problèmes électo-soft…</h3>
<p>Sur la cible, rien ne fonctionne. Malédictis! Un enchaînement de problèmes m’ont pourri un après-midi. Comme le montage est au garage, j’utilise un netbook pour aller y charger le programme. La synchro entre le PC et le netbook est assurée par <a href="/2011/08/30/dropbox-et-wuala-le-cloud-senrichit/" target="_blank" title="DropBox et Wuala: le cloud s’enrichit">Wuala</a>. Mais voilà, suite à la ré-installation de mon PC, la synchro ne s’est pas faite… Ceci corrigé: rien ne marche. Pour voir la santé de la carte, je me résoud à charger le programme « LED clignotante ». Rien ne clignote! Mais je vois sur le site de Seeduino que la LED, classiquement sur OUT 12 dans Arduino est sur la OUT 8 de la carte Stalker… Puis, en voyant sa fréquence lente, je me rappelle d’un autre souci: il faut charger avec la bonne carte en paramètre (Outil -&gt; Type de carte -&gt; Pro Mini, 8 MHz) au lieu de Duemilanove w/ Atmega328! Mais… rien ne marche! Je démonte le proto et l’apporte au bureau, en y connectant le LCD sur le système de test, mais rien! Est-il mort? Non, un examen du code me montre que c’est le programme qui est incomplet (mais il compile, ce qui m’a trompé). En effet, fatigué de mes essais le soir précédent, j’avais quitté le programme sans le sauver… Après ces quelques heures de déboires rétablis péniblement – mais avec pugnacité – je me dis que M. tout-le-monde ne va pas forcément trouver en Arduino la panacée simple et facile, facile…</p>
<p>Une fois le système opérationnel (la boucle tourne, la mesure de courant est correcte, l’affichage est OK et la sortie série l’est aussi), je cherche à améliorer le programme.</p>
<h3>Timing précis</h3>
<p>Un petit tour sur le site de Arduino me montre un méthode de synchronisation parfaite. Et je l’intègre derechef! C’est réalisé grâce à la fonction millis(), qui retourne un long (32 bits) contenant le nombre de millisecondes depuis le démarrage. Il tient 50 jours avant l’overflow…  Il suffit de vérifier dans la boucle principale que 1000 ms sont écoulées. Ceci tient compte du « jitter ». Ainsi je peut rythmer mes appels à la fonction pulse_1Sec() de manière très précise. De pus, l’action sur le bouton de démarrage est prise en compte de manière quasi immédiate.</p>
<pre>//Boucle principale
const unsigned long cycleTime = 1000; // t boucle: 1 sec.
unsigned long previousMillis = 0UL;
void loop() 
{
  unsigned long currentMillis = millis();  // t écoulé
  if (currentMillis - previousMillis &gt; cycleTime)
  {
    previousMillis = currentMillis;
    pulse_1Sec();
  }

  if (digitalRead(BtnStart) &amp;&amp; state == 0)// voir si le bouton est pressé?
    state = 5;   // tempo
}// fin de la boucle principale</pre>
<h3>Énergie</h3>
<p>Puisque le problème du timing est réglé, voyons celui du calcul de l’énergie. Dans le cycle d’une seconde, le courant est mesuré à chaque fois, puis affiché. Il suffit de le sommer, ainsi nous obtenons: I x t, soit des [milliampères secondes]. A la fin de la charge, le compteur de temps s’arrête; le relais est ouvert. Pour en retirer l’énergie délivrée, la fonction suivante nous rend des Watt heure [WH]:</p>
<pre>/*
  Calcule de l'énergie en supposant:
  - le courant en mA
  - sommé chaque seconde
  - tension secteur 230VAC
  retour: résultat en WH
*/
long energy_computed(unsigned long mAS)
{
  return mAS * 230L / 3600000L;
}</pre>
<p>Il ne reste qu’à indiquer la valeur en fin de charge sur l’afficheur.</p>
<h3>Fin de la charge</h3>
<p>Pour s’assurer que la charge est bel et bien terminée et n’est pas due à une mesure incorrecte ou a une diminution transitoire, il faut garantir l’état par un timer qui maintient le relais pendant encore quelques secondes (ici 6). Le buzzer se fait entendre pour marquer la transition. Extrait final enregistré par la ligne sérielle:</p>
<pre>I:158    n:851
I:157    n:852
I:158    n:853
I:87    n:854
I:86    n:855
I:85    n:856
I:85    n:857
I:85    n:858
I:85    n:859
Energie:    10</pre>
<p>Cette fin de charge montre que 10 WH ont été consommés. Ceci n’est pas représentatif, vu que la durée de charge était d’un peu plus de 14 minutes. Par contre j’ai pu remarquer que le courant, fort au départ de 400 mA baissait régulièrement; puis à la fin, il passe rapidement en dessous de 100 mA. Le seuil a été fixé à 130 mA, soit à P=30 W, mi-chemin entre la puissance résiduelle et la charge lente, de 40 W. La consommation du contrôleur de charge lui-même est de moins de 1 W, soit un courant résiduel de 3-4 mA.</p>
<p><a href="/media/2012/09/Load_control_global.jpg"><img alt="" height="552" src="/media/2012/09/Load_control_global-1024x957.jpg" title="Load_control_global" width="591"/></a></p>
<p>Le montage et son environnement: le boitier comportant bouton de démarrage et afficheur. A savoir, la photo ne montre pas l’affichage actuel, le texte est mieux disposé et affiche les unités. Le chargeur est à droite. Il ne comporte qu’un bouton – lui aussi – permettant de commuter la vitesse de charge. Un LED indique le mode : si elle clignote, c’est la charge rapide.</p>
<h2>Conclusion</h2>
<p>Le montage est simple, mais permet de connaître l’énergie consacrée à la recharge d’une batterie de vélo. De plus, avec une interruption complète du chargeur, il permet la sauvegarde d’une consommation « grise » importante. Il ménage aussi la batterie, qui ne sera pas maintenue inutilement sous tension.</p>
<p>Il me reste à peaufiner la gestion: réglages divers; l’enregistrement sur carte SD et restitution des données; actuellement, tout s’efface lorsque l’alimentation est coupée.</p>
<h2>Références</h2>
<ul>
<li>Le vélo: <a href="http://www.cresta-swiss-bike.ch/" target="_blank" title="http://www.cresta-swiss-bike.ch/">http://www.cresta-swiss-bike.ch/</a> (ce site est franchement horrible…)</li>
<li>Le système Grove: <a href="http://www.seeedstudio.com/wiki/GROVE_System" target="_blank" title="http://www.seeedstudio.com/wiki/GROVE_System">http://www.seeedstudio.com/wiki/GROVE_System</a></li>
<li>La carte Stalker: <a href="http://www.seeedstudio.com/depot/seeeduino-stalker-v2-p-727.html" target="_blank" title="http://www.seeedstudio.com/depot/seeeduino-stalker-v2-p-727.html">http://www.seeedstudio.com/depot/seeeduino-stalker-v2-p-727.html</a></li>
</ul>
<p>Yves Masur (9/2012)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
