---
title: "Source de courant à ampli-opérationnel"
date: "2025-06-17T20:23:00"
lastmod: "2025-06-17T20:23:01"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2025/06/17/source-de-courant-a-ampli-operationnel/"
wordpress_id: 5634
comment_count: 0
---
<p></p>
<p><strong>Source de courant à ampli-opérationnel</strong></p>
<p>Afin de donner bonne suite à la présentation, de Laurent Francey et moi-même, sur les amplificateurs opérationnels (AOP), je vous propose quelques articles, un par type de montage.</p>
<p>Pour ce premier article topique nous allons aborder la source de courant à AOP.</p>
<p>Commençons tout d’abord par la configuration la plus simple.</p>
<p>Fig.1</p>
<p><img height="303" src="/media/2025/06/word-image-5634-1.png" width="319"/></p>
<p>Nous avons affaire ici à un montage suiveur. Son montage de base est le suivant :</p>
<p>Fig. 2</p>
<p><img height="185" src="/media/2025/06/word-image-5634-2.png" width="349"/></p>
<p>Avec comme équation de base, V<sub>S</sub> = V<sub>e</sub></p>
<p>Ainsi, la tension présente sur l’entrée non-inverseuse de l’AOP se retrouve sur son entrée inverseuse, et par conséquent aux bornes de la résistance R (la tension différentielle, dans un fonctionnement linéaire, étant nulle).</p>
<p>Revenons à la Fig. 1</p>
<p><img height="303" src="/media/2025/06/word-image-5634-3.png" width="319"/></p>
<p>L’entrée positive de l’AOP est reliée au curseur d’un potentiomètre alimenté par une tension bipolaire de ± 10 V CC. Partant, cette tension se retrouvera aux bornes de la résistance R.</p>
<p>Regardons maintenant la simulation de ce circuit avec une tension d’entrée positive.</p>
<p>Fig. 3</p>
<p><img height="317" src="/media/2025/06/word-image-5634-4.png" width="426"/></p>
<p>Ladite tension de + 4V se retrouve intégralement aux bornes de la résistance R. Donc le courant y circulant, sera de +4V/R.</p>
<p>Fig. 4</p>
<p><img height="325" src="/media/2025/06/word-image-5634-5.png" width="437"/></p>
<p>A la fig. 4, c’est cette fois-ci une tension négative de -4V qui est appliquée à l’entrée non-inverseuse de l’AOP. Ce qui implique que le courant dans la résistance R sera de -4V/R et que notre source de courant est bipolaire.…</p>
<p>Avec un transistor en plus…</p>
<p>Fig. 5</p>
<p><img height="375" src="/media/2025/06/word-image-5634-6.png" width="519"/></p>
<p>Nous sommes en présence, ici, d’une source de courant avec charge à la masse.</p>
<p>R2 constituant la résistance de « charge ». La tension appliquée à l’entrée non-inverseuse de l’AOP est égale à : Vcc – la tension de la diode Zener, soit 15V – 3V = 12 V</p>
<p>Cette tension va se retrouver sur la borne inférieure de la résistance R3. La tension aux bornes de R3 sera de 15V (Vcc) – 12 V = 3 V. Par conséquent le courant circulant dans ladite résistance sera de 3V/3K = 1 mA. Preuve en est, la tension aux bornes de la résistance de charge est 100 Ω * 1 mA = 0.1 V .</p>
<p><img height="436" src="/media/2025/06/word-image-5634-7.jpeg" width="1113"/></p>
<p>Fig. 6</p>
<p>Quelques montages avec charge à la masse</p>
<p>Voici un montage pratique avec charge au Vcc, V<sup>+</sup>.</p>
<p><img height="458" src="/media/2025/06/word-image-5634-8.png" width="586"/></p>
<p>Fig. 7</p>
<p>Le courant dans la LED est égal à : Vin/Rsense</p>
<p>Un autre encore</p>
<p>Fig. 8</p>
<p><img height="706" src="/media/2025/06/word-image-5634-9.jpeg" width="960"/></p>
<p>Maintenant, voyons à quoi ressemble une source de courant commandée par une tension. Précisons que nous n’aborderons pas les tensions de commandes alternatives, bien que plusieurs des montages vus ici, y sont compatibles.</p>
<p><img height="235" src="/media/2025/06/word-image-5634-10.png" width="432"/></p>
<p>Fig. 9</p>
<p>Le principe de la source de courant présentée à la Fig. 9 est basé sur le fait que le courant de sortie est monitoré par la tension aux bornes de R1. De manière à déterminer le courant de sortie, appliquons le KCL (Kirchoff’s Current Law) à l’entrée non-inverseuse, l’entrée inverseuse et à la sortie.</p>
<p>Fig. 10</p>
<p><img height="114" src="/media/2025/06/word-image-5634-11.png" width="185"/></p>
<p>V<sub>O </sub> V<sub>N </sub>U<sub>1 </sub>U<sub>2 </sub>I<sub>2 </sub>V<sub>P </sub>R<sub>2</sub><sup>2</sup></p>
<p>(V<sub>O – </sub>V<sub>N </sub>)/R<sub>2 </sub>– V<sub>N</sub>/R<sub>3 </sub>= 0 ;</p>
<p>(U<sub>1 – </sub>V<sub>P </sub>)/R<sub>2 </sub>+ ( U<sub>2 – </sub>V<sub>P </sub>)/R<sub>2 </sub>= 0 ;</p>
<p>(V<sub>O – </sub>U<sub>2 </sub>)/R<sub>1 </sub>+ (V<sub>P – </sub>U<sub>2 </sub>)/R<sub>2 – </sub>I<sub>2 </sub>= 0 ;</p>
<p>Comme V<sub>N </sub>= V<sub>P</sub>, nous obtenons pour le courant de sortie <strong>I<sub>2 </sub>=</strong></p>
<p>Pour une seule valeur de R3, le courant de sortie devient indépendant de la tension de sortie ; c’est le cas où le second terme de l’équation est nul ! Et si</p>
<p>R3 = <em> <br/></em></p>
<p>La valeur du courant est</p>
<p>I2 = U1/(R1//R2)</p>
<p>En pratique R2 &gt;&gt; R1, et de fait <strong>I2 ~ U1/R1 ce qui est bien indépendant de la tension de sortie, de la charge.</strong></p>
<p>L’histoire aurait pu s’arrêter là, mais c’était sans compter que les férus d’électronique analogique allaient s’emparer de l’affaire…</p>
<p>Ce qui est ennuyeux et compliqué à mettre en équation, c’est que nous avons un courant qui circule depuis Vo dans R2 et R3.</p>
<p>Et, c’est là, que les férus entrent en scène. Ils insèrent un montage suiveur à la borne inférieure de la résistance de setting du courant de sortie !</p>
<p>Cela donne le circuit suivant, Fig. 11 avec les équations idoines</p>
<p><img height="569" src="/media/2025/06/word-image-5634-12.png" width="1058"/></p>
<p>Moins de texte, mais plus d’actes, vérifions avec le simulateur Proteus, la justesse des équations ci-dessus</p>
<p><img height="448" src="/media/2025/06/word-image-5634-13.jpeg" width="704"/> Fig. 11.</p>
<p><strong>U1 = 2*U3…U3 = 2.38 V, donc U1 = 4.76 V Ok !</strong></p>
<p><strong>U3 = (Ue + U2)/2 Ue = 1.2 V, U2 = 3.57 V, donc U3 = (1.2 V + 3.57 V)/2 = 2.38 V OK !</strong></p>
<p><strong>Ue = U1 – U2 ; 4.77 V – 3.57 V = 1.2 V Ok !</strong></p>
<p>La tension aux bornes de la résistance de charge RCH (300 Ω) est 3.57 V. Ce qui implique que le courant la traversant est de 3.57 V/0.3 KΩ = 11.9 mA. <strong>I = Ue/Rset = 1.2 V / 100 Ω = 12 mA</strong></p>
<p>Au vu de ce qui précède, la simulation démontre ladite justesse des équations !</p>
<p>Etant donné le peu de composants nécessaires à la réalisation de ce montage, il est vivement conseillé de le tester sur une bredboard.</p>
<p>Un, petit dernier, montage analysé…</p>
<p><img height="470" src="/media/2025/06/word-image-5634-14.png" width="637"/> Fig. 12</p>
<p>Nous avons ici, une source de courant de puissance, unipolaire, avec charge à la masse. L’étage de puissance est composé de deux transistors PNP montés en Darlington (et non pas tête bêche…comme il m’arrive de le dire). La tension d’alimentation (Vcc) est de 20 V. La valeur de la résistance R1 limitera le courant de sortie à 4 A. La tension minimale aux bornes de R1 est de 16 V. On notera que la tension présente sur l’entrée non inverseuse (18 V) se retrouve sur l’émetteur du transistor Q2. Nous sommes donc bien en présence d’un suiveur de tension. Le courant circulant dans ce transistor est donné par l’équation (Vcc – VE<sub>Q2</sub>)/R4. En l’occurrence (20 V – 18V)/1Ω = 2A. Et, la tension aux bornes de R3 est bien de 4V, soit, 2Ω * 2A.</p>
<p>Quelques montages…trouvés sur la toile</p>
<p><img height="722" src="/media/2025/06/word-image-5634-15.png" width="900"/></p>
<p><img height="789" src="/media/2025/06/word-image-5634-16.png" width="900"/></p>
<p><img height="700" src="/media/2025/06/word-image-5634-17.png" width="900"/></p>
<p><img height="537" src="/media/2025/06/word-image-5634-18.png" width="963"/></p>
<p><a href="https://www.analog.com/en/resources/analog-dialogue/articles/a-large-current-source-with-high-accuracy-and-fast-settling.html">https://www.analog.com/en/resources/analog-dialogue/articles/a-large-current-source-with-high-accuracy-and-fast-settling.html</a></p>
<p>Pour le Microclub Jean-Pierre Broillet, juin 2025</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
