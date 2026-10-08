---
title: "Full Wave Rectifier"
date: "2025-07-02T16:52:24"
lastmod: "2025-07-02T16:52:25"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2025/07/02/full-wave-rectifier/"
wordpress_id: 5655
comment_count: 0
---
<p><strong>Le circuit suivant génère la valeur absolue du signal d’entrée (Full Wave Rectifier).</strong></p>
<p><img height="236" src="/media/2025/07/word-image-5655-1.png" width="664"/></p>
<p>Deux cas se présentent :</p>
<p><strong>Cas 1 : Vi &gt; 0</strong> :</p>
<p>Lorsque Vi &gt; 0, la partie « inverseuse » de A1 force sa sortie à être négative, ce qui permet à D1 de conduire et à D2 d’être bloquée. Comme aucun courant ne circule dans la résistance R connectée entre Vn1 et Vp2, les deux sont équipotentielles.</p>
<p>Vn1 = Vp2 = 0 V</p>
<p>La figure suivante montre son schéma équivalent</p>
<p><img height="235" src="/media/2025/07/word-image-5655-2.png" width="575"/></p>
<p>A partir du circuit équivalent, la tension de sortie peut être calculée :</p>
<p><strong>Vo = Vi</strong></p>
<p><strong>Cas 2</strong> <strong>: Vi &lt; 0</strong> : Lorsque Vi &lt; 0, négatif, la tension de sortie de A1 passe au niveau positif, ce qui rend la diode D1 bloquée et la diode D2 conductrice.</p>
<p>La figure suivante montre son schéma équivalent</p>
<p><img height="272" src="/media/2025/07/word-image-5655-3.png" width="612"/></p>
<p>v</p>
<p>La tension de sortie de l’amplificateur A1 est de V. Comme l’entrée différentielle de A2 est nulle, la borne d’entrée inverseuse est également à la tension V, comme le montre la figure.</p>
<p>Appliquons la loi de Kirchhoff au nœud a :</p>
<p><img height="192" src="/media/2025/07/word-image-5655-4.png" width="363"/></p>
<p>Pour trouver Vo en fonction de V, nous nous concentrons sur le circuit équivalent de A2 (montage non-inverseur), comme le montre la figure.</p>
<p><strong> = </strong></p>
<p>En substituant la valeur de V dans l’équation ci-dessus, on obtient,</p>
<p>Par conséquent, pour Vi &lt; 0, la sortie est positive. Ceci est illustré à la figure suivante.</p>
<p><img height="401" src="/media/2025/07/word-image-5655-5.jpeg" width="457"/></p>
<p>Examinons ce montage avec la simulation Proteus. Pour ce faire nous appliquerons une tension de 2V DC, de 0V DC et -2V DC sur l’entrée. Si les calculs effectués ci-avant sont corrects, la tension de sortie doit être respectivement de +2 V DC, 0V DC et à nouveau +2V DC.</p>
<p><strong>Avec + 2V</strong></p>
<p><img height="430" src="/media/2025/07/word-image-5655-6.png" width="965"/></p>
<p><strong>Avec 0V</strong></p>
<p><img height="408" src="/media/2025/07/word-image-5655-7.png" width="964"/></p>
<p><strong>Avec -2V</strong></p>
<p><strong><img height="413" src="/media/2025/07/word-image-5655-8.png" width="969"/></strong></p>
<p><strong>Vo = -Vi, car Vi &lt; 0</strong></p>
<p><strong><img height="410" src="/media/2025/07/word-image-5655-9.jpeg" width="612"/></strong></p>
<p><strong>Cerise sur le gâteau….</strong></p>
<p><strong>Un montage sans diode, avec un comparateur, des amplis op et un switch. Vous ne le trouverez nulle part ailleurs !</strong></p>
<p><strong><img height="989" src="/media/2025/07/word-image-5655-10.gif" width="2064"/></strong></p>
<p><strong>Fonctionnement du montage</strong></p>
<p>Quelques mots tout d’abord sur le MAX912.</p>
<p>Les comparateurs doubles (dual), tels que le MAX912, possèdent grande vitesse de basculement (propagation) 10 ns, une faible consommation, des entrées différentielles et des sorties TTL complémentaires.</p>
<p>L’alimentation est simple +5V (ou ±5V).</p>
<p>Les sorties du MAX912 restent stables sur toute la région linéaire. Cette caractéristique élimine l’instabilité de sortie commune aux comparateurs à grande vitesse lorsqu’ils sont pilotés par un signal d’entrée lent.</p>
<p>Le DG419 est Analog Switch, avec les caractéristiques suivantes :</p>
<p>Low RDS(ON) (35Ω max)</p>
<p>Single-Supply Operation +10V to +30V</p>
<p>Bipolar-Supply Operation ±4.5V to ±20V</p>
<p>Low Power Consumption (35μW max)</p>
<p>Rail-to-Rail Signal Handling</p>
<p>TTL/CMOS-Logic Compatible</p>
<p>D’apprès son schéma synoptique, il appert qu’un niveau logique 1 (Switch 2 ON) sur la borne 6 (IN) relie, commute, les bornes 1 (D) et 8 (S2), alors qu’un niveau logique 0 (Switch1 ON) sur cette borne IN, reliera la borne D (1) à la borne S1 (2).</p>
<p><img height="424" src="/media/2025/07/word-image-5655-11.jpeg" width="423"/></p>
<p>Lorsqu’une tension positive est appliquée sur l’entrée négative du comparateur, sa sortie bascule à l’état négatif (trace rouge), à contrario de la sortie complémentaire (trace bleue). De ce fait, c’est la tension de sortie du suiveur (U4) qui va se retrouver à la sortie du switch analogique. Une tension négative appliquée à l’entrée négative du comparateur va occasionner un basculement à l’état haut dudit comparateur et par conséquent, un passage à l’état bas de la sortie complémentaire.  Cette sortie à l’état bas permet au signal d’entrée inversé (U3) de se retrouver à la sortie du switch. Cette sortie est représentée par la trace verte qui montre bien un comportement de redresseur. Les AOP utilisés pour un test réel ne sont pas des OP05, mais des AD746. Ceux-ci n’étant malheureusement pas encore disponible pour la simulation Proteus, d’où les OP05.</p>
<p><img height="807" src="/media/2025/07/word-image-5655-12.gif" width="805"/></p>
<p><strong><img height="800" src="/media/2025/07/word-image-5655-13.gif" width="797"/></strong></p>
<p><strong>Ce montage fonctionne sans problème jusqu’à 500 kHz…</strong></p>
<p><strong>Jean-Pierre Broillet, Microclub, juin 2025</strong></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
