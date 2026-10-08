---
title: "servo-moteur, les limites"
date: "2013-09-03T15:52:18"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: []
url: "/2013/09/03/servo-moteur-les-limites/"
wordpress_id: 1297
comment_count: 2
---
<p>Dans le cadre d’un projet électro-mécanique, j’utilise des <a href="http://fr.wikipedia.org/wiki/Servomoteur" target="_blank">servo-moteurs</a> (ci-après: servo) miniatures, pour des mouvements contrôlés.Bienvenu pour du contrôle commande, peu cher (le modèle en photo est à … 4,95 CHF!) livré avec un jeu de roues, étoiles et levier plastiques pour commander une position, le servo est de plus facile à piloter et simple à connecter.</p>
<figure aria-describedby="caption-attachment-1298"><a href="/media/2013/09/673-main_LPC-mot2-detail-traction-L.jpg"><img alt="673 main_LPC mot2 detail traction L" height="225" src="/media/2013/09/673-main_LPC-mot2-detail-traction-L-300x225.jpg" width="300"/></a><figcaption>Servo</figcaption></figure>
<p>Mon projet n’a pas besoin d’une grande précision, ni même de force extraordinaire. cependant je me suis posé quelques questions… et les ai relayées aux membres du club! En voici la teneur:</p>
<ol>
<li>quelle est la résolution/précision envisageable?</li>
<li>pourquoi le mécanisme vibre-t-il à l’arrêt?</li>
<li>quelle est la charge admissible?</li>
<li>quel est le comportement en surcharge?</li>
</ol>
<h3>1 – Précision</h3>
<p>Avec Arduino, la formule consacrée à la position est indiquée par un exemple. Lecture d’un potentiomètre sur 10 bits (valeur 0..1023) et réglage de la consigne 0 à179; donc 180°.</p>
<pre>void loop() 
{ 
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023) 
  Serial.print("\t");
  Serial.print(val, DEC);
  val = map(val, 0, 1023, 0, 179);     // scale it to use it with the servo (value between 0 and 180) 
  myservo.write(val);                  // sets the servo position according to the scaled value 
  delay(15);                           // waits for the servo to get there 
}</pre>
<p>Donc on en déduit que la résolution ne saurait être supérieure à 1/180. Il en résulte, sur la pin de commande, une impulsion positive dont la largeur est au minimum de 0.55 ms, et 2,38 ms au maximum, si j’en crois mon scope; répétée toute les 20 ms. De plus, il faut savoir que les servos, connectés par 3 fils (+Alim, 0V, impulsion) ont une électronique interne qui positionne l’axe selon la largeur d’impulsion.</p>
<h3>2 – Vibrations</h3>
<p>Le programme ci-dessus, appliqué à un servo, même non chargé, laisse entendre des vibrations et montre un frétillement. Est-ce le rafraichissement de la consigne donnée par la boucle?</p>
<p>Selon Laurent Francey, le positionnement est réalisé de manière interne par un potentiomètre couplé sur l’axe de rotation. Or celui-ci est mû par le moteur via des rouages en plastique,  si le servo est bon marché (c’est mon cas!), sinon en laiton; qui ont du jeu. L’axe n’étant  pas parfaitement solidaire du potentiomètre de position, il s’ensuit – pour certains paliers, certaines positions –  une correction envoyée au moteur à travers ces jeux; ce qui provoque les vibrations.</p>
<h3>3 – Charge admissible</h3>
<p>Avec un design mécanique parfait, un servo n’a pas besoin de puissance de maintien: toutefois, la vitesse d’exécution de la position, voire le déplacement de la charge nécessite un certain couple: on peut alors alimenter ces moteurs avec une tension plus élevée. Souvent les caractéristiques sont données pour 4,8V et pour 6V. Comme dans mon projet le rappel est fait par des ressorts, le servo nécessite de la puissance pour tenir sa position  (ce n’est pas bien; mais c’est partit comme cela…) Un autre phénomène peut provoquer de la consommation: un changement incessant de position.En clair: ça chauffe.</p>
<h3>4 –  Comportement en surcharge</h3>
<p>Afin de tester les limites du système (modèle <a href="http://www.conrad.ch/ce/fr/product/230500/" target="_blank">230500-62</a> chez Conrad: ), j’ai provoqué des aller-retour, avec charge. Au bout d’un moment, le moteur commence à chauffer; l’électronique interne le débranche quelques secondes, puis il reprend sa poursuite. Cela se traduit par un hoquet.</p>
<p>La charge a aussi une influence sur la position, et tend à la fausser selon le gain proportionnel de la régulation interne du moteur.</p>
<p>Yves Masur (9/2013)</p>

## Commentaires

### michel von — 3 septembre 2013 à 21:38

<section class="comment-content comment">
<p>Effectivement, il y a un potentiomètre solidaire de l’axe du moteur. J’en avais démonté un pour voir.<br/>
Tu as utilisé un servo-moteur très bon-marché, c’est ce que j’ai aussi. Mais j’aurais besoin d’un servo-moteur de meilleure qualité, qui n’ait pas de vibration. J’aimerais diriger une caméra TV avec ce système et si ça vibre, ça empêche de faire des panoramiques ou des travellings car ça se voit sur l’image. </p>
<p>Question: Connais (ou quelqu’un connaît-il) un type de servo-moteur haut de gamme qui serait mécaniquement plus sérieux ?</p>
 </section>

### ↳ Réponse — Sébastien Pieren — 4 septembre 2013 à 05:52

<section class="comment-content comment">
<p>Bonjour,<br/>
Etant modéliste amateur, j’utilise très souvent de tels servos, il en existe un très grand nombre sur le marché, de technologie différente. A savoir analogiques ou digital, à palier ou roulement à bille, à moteur à charbon ou « brushless », à engrenages plastique, métal, carbone, ou autre. Ensuite on peut choisir les caractéristiques désirées comme l’angle de travail, la puissance mécanique, la vitesse de travail.<br/>
Sachant tout cela, les prix varie du servo très bon marché de l’exemple à des servos à 300.- pièce, dans les modèles courant. un petit site qui rassemble les données des servo les plus utilisé :<a href="http://www.servodatabase.com/" rel="nofollow ugc">http://www.servodatabase.com</a>.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
