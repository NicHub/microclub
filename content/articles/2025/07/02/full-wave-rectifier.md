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
**Le circuit suivant génère la valeur absolue du signal d’entrée (Full Wave Rectifier).**

![](/media/2025/07/word-image-5655-1.png)

Deux cas se présentent :

**Cas 1 : Vi \> 0** :

Lorsque Vi \> 0, la partie « inverseuse » de A1 force sa sortie à être négative, ce qui permet à D1 de conduire et à D2 d’être bloquée. Comme aucun courant ne circule dans la résistance R connectée entre Vn1 et Vp2, les deux sont équipotentielles.

Vn1 = Vp2 = 0 V

La figure suivante montre son schéma équivalent

![](/media/2025/07/word-image-5655-2.png)

A partir du circuit équivalent, la tension de sortie peut être calculée :

**Vo = Vi**

**Cas 2** **: Vi \< 0** : Lorsque Vi \< 0, négatif, la tension de sortie de A1 passe au niveau positif, ce qui rend la diode D1 bloquée et la diode D2 conductrice.

La figure suivante montre son schéma équivalent

![](/media/2025/07/word-image-5655-3.png)

v

La tension de sortie de l’amplificateur A1 est de V. Comme l’entrée différentielle de A2 est nulle, la borne d’entrée inverseuse est également à la tension V, comme le montre la figure.

Appliquons la loi de Kirchhoff au nœud a :

![](/media/2025/07/word-image-5655-4.png)

Pour trouver Vo en fonction de V, nous nous concentrons sur le circuit équivalent de A2 (montage non-inverseur), comme le montre la figure.

**=**

En substituant la valeur de V dans l’équation ci-dessus, on obtient,

Par conséquent, pour Vi \< 0, la sortie est positive. Ceci est illustré à la figure suivante.

![](/media/2025/07/word-image-5655-5.jpeg)

Examinons ce montage avec la simulation Proteus. Pour ce faire nous appliquerons une tension de 2V DC, de 0V DC et -2V DC sur l’entrée. Si les calculs effectués ci-avant sont corrects, la tension de sortie doit être respectivement de +2 V DC, 0V DC et à nouveau +2V DC.

**Avec + 2V**

![](/media/2025/07/word-image-5655-6.png)

**Avec 0V**

![](/media/2025/07/word-image-5655-7.png)

**Avec -2V**

**![](/media/2025/07/word-image-5655-8.png)**

**Vo = -Vi, car Vi \< 0**

**![](/media/2025/07/word-image-5655-9.jpeg)**

**Cerise sur le gâteau….**

**Un montage sans diode, avec un comparateur, des amplis op et un switch. Vous ne le trouverez nulle part ailleurs !**

**![](/media/2025/07/word-image-5655-10.gif)**

**Fonctionnement du montage**

Quelques mots tout d’abord sur le MAX912.

Les comparateurs doubles (dual), tels que le MAX912, possèdent grande vitesse de basculement (propagation) 10 ns, une faible consommation, des entrées différentielles et des sorties TTL complémentaires.

L’alimentation est simple +5V (ou ±5V).

Les sorties du MAX912 restent stables sur toute la région linéaire. Cette caractéristique élimine l’instabilité de sortie commune aux comparateurs à grande vitesse lorsqu’ils sont pilotés par un signal d’entrée lent.

Le DG419 est Analog Switch, avec les caractéristiques suivantes :

Low RDS(ON) (35Ω max)

Single-Supply Operation +10V to +30V

Bipolar-Supply Operation ±4.5V to ±20V

Low Power Consumption (35μW max)

Rail-to-Rail Signal Handling

TTL/CMOS-Logic Compatible

D’apprès son schéma synoptique, il appert qu’un niveau logique 1 (Switch 2 ON) sur la borne 6 (IN) relie, commute, les bornes 1 (D) et 8 (S2), alors qu’un niveau logique 0 (Switch1 ON) sur cette borne IN, reliera la borne D (1) à la borne S1 (2).

![](/media/2025/07/word-image-5655-11.jpeg)

Lorsqu’une tension positive est appliquée sur l’entrée négative du comparateur, sa sortie bascule à l’état négatif (trace rouge), à contrario de la sortie complémentaire (trace bleue). De ce fait, c’est la tension de sortie du suiveur (U4) qui va se retrouver à la sortie du switch analogique. Une tension négative appliquée à l’entrée négative du comparateur va occasionner un basculement à l’état haut dudit comparateur et par conséquent, un passage à l’état bas de la sortie complémentaire. Cette sortie à l’état bas permet au signal d’entrée inversé (U3) de se retrouver à la sortie du switch. Cette sortie est représentée par la trace verte qui montre bien un comportement de redresseur. Les AOP utilisés pour un test réel ne sont pas des OP05, mais des AD746. Ceux-ci n’étant malheureusement pas encore disponible pour la simulation Proteus, d’où les OP05.

![](/media/2025/07/word-image-5655-12.gif)

**![](/media/2025/07/word-image-5655-13.gif)**

**Ce montage fonctionne sans problème jusqu’à 500 kHz…**

**Jean-Pierre Broillet, Microclub, juin 2025**

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
