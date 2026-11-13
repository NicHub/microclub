---
title: "Lecture 230VAC par Arduino (ou autre CPU)"
date: "2020-03-01T18:49:36"
lastmod: "2020-03-01T18:51:41"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: []
url: "/2020/03/01/lecture-230vac-par-arduino-ou-autre-cpu/"
wordpress_id: 4733
comment_count: 0
---
Voici le problème : comment lire la présence d’une tension d’alimentation du secteur, par un CPU alimenté et prévu pour des basses tensions ?

Pas de doute : le secteur est **dangereux**. Une mauvaise manipulation peut **tuer**. Il s’agit d’observer la plus grande prudence. Le diviseur de tension à résistances n’est pas possible : il faut isoler. Il y a donc deux parties distinctes :

- Le circuit connecté au 230VAC
- Le circuit connecté à la basse tension 5V ou 3.3V

## Le relais

Un moyen simple est le relais : sa bobine prévue pour le 230VAC et des contacts libres de potentiel font parfaitement l’affaire pour lire l’état par le microcontrôleur.

![](/media/2020/03/word-image.jpeg)

C’est ce que j’ai utilisé pour connaître (entre autres) le taux d’activité de la pompe de circulation du chauffage solaire de mon installation. Pour les détails, voir l’article : [https://microclub.ch/2014/10/11/yun-monitoring-de-leau-solaire/](/2014/10/11/yun-monitoring-de-leau-solaire/)

Toutefois, si le nombre de commutation est élevé, ou si la rapidité de commutation n’est pas vraiment compatible avec l’électromécanique, on passera à une solution toute électronique.

## Premier schéma

Après une recherche sur le net, et ne rien avoir trouvé qui me plaise, j’ai monté sur bimboard le schéma suivant.

![](/media/2020/03/word-image-1.jpeg)

Le 230VAC est connecté sur J1. Le courant est limité par R1 (1W), il traverse les LED D1 et D2, suivant l’alternance positive ou négative. Puis active l’opto-coupleur U1. Coté basse tension, on alimente la pin J2/1 avec +5V (ou 3.3V suivant le modèle de CPU/Arduino) ; et le 0V sur J2/3. La logique est positive : si le secteur est présent, la tension au point J2/2 sera proche de l’alimentation, à la saturation près de U1. Sinon, 0V.

Pour toutes les mesures présentées ci-après, l’alimentation de la basse tension est de 5V. Avec une tension de 3.3V, on peut s’attendre raisonnablement au même comportement.

Le circuit est simple, avec 6 composants. Les LED montrent la présence de tension sur J1, la logique est positive (1 = présence de tension) et colle très bien à une période près.

## Coller à la période – pourquoi ?

A 50 Hz, une période dure 20 ms ; une alternance est de 10 ms. Quelle est l’utilité de répondre aussi rapidement ?

Lors du passage du technicien pour l’entretien du chauffage, ce dernier m’a proposé un réglage assez surprenant de la pompe de circulation : une modulation en PWM. A savoir, le moteur asynchrone de la pompe voit sa phase coupée ! Les alternances sont rythmées ! La modulation est activée entre 65% (réglable) et 100%. On peut ainsi avoir une vitesse d’écoulement du fluide calo-porteur modulée en fonction de la différence de température entre les panneaux solaires et l’accumulateur. Autant dire que le relais clapote sérieusement et bat la chamade !

Bonne surprise, le soft de mesure de mon Arduino Yun ayant une scrutation asynchrone assez rapide de l’état du contact, la mesure semble correcte. Par exemple, l’après-midi du 20.02.2020 montre bien le taux d’enclenchement modulé de la pompe, sur la courbe verte :

<https://yvesmasur.ch/ecs/chart.php?yyyy=2020&mm=2&dd=20>

Avec le réglage tout-ou-rien, on aurait eu du 100% de 9h à 16h30. Il faut que le circuit qui remplacera le relais ne lisse pas la modulation par une constante de temps trop importante, et montre au plus près l’image de la tension.

## Signal sans filtrage – C1 déconnecté

Le signal bleu montre le passage par zéro de la sinusoïde, pendant lequel le courant s’annule. C’est une pulse contre zéro. Le signal rouge est pris sur le pin 1 de U1, soit aux bornes des diodes internes de l’opto-coupleur. Dans un tel cas, si le soft est asynchrone – ce qui devrait être le cas – on peut très bien tomber sur le signal bas et lire un ‘0’ logique alors que le secteur est présent! Une solution logicielle serait de mesurer avec deux échantillons consécutifs de 2 à 5 millisecondes et procéder à un OU logique des valeurs lues. Mais c’est bien compliqué pour peu de chose, alors qu’une capacité bien dimensionnée fait l’affaire.

![](/media/2020/03/word-image.png)

## Aparté sur la mesure du signal ‘rouge’

Pour mesurer ce signal, il faut que l’oscilloscope soit galvaniquement **séparé de la terre** du réseau. Sans quoi, le disjoncteur différentiel déclenche à coup sûr. Et il s’agit d’être prudent et de bien vérifier que le **commun soit le neutre**.

![](/media/2020/03/word-image-2-300x268.jpeg)

## Signal avec filtre – C1 connecté

Avec un C1 de 100nF et R2 de 22K, on obtient un constante de temps R x C de 2,2 ms – environ la largeur de l’impulsion. La tension résultante de sortie du circuit montre une baisse passagère, mais reste suffisamment haute pour être considérée comme un ‘1’ logique. Le circuit est suffisamment rapide pour présenter le ‘0’ logique à l’absence d’une alternance.

![](/media/2020/03/word-image-1.png)

## Circuit du commerce

Une recherche plus approfondie sur le Net me montre que Banggood propose un circuit adéquat, pour environ 3,80 CHF. Il est présenté comme compatible Arduino. J’en commande deux. Quelques semaines plus tard, les voici dans ma boîte aux lettres.

<https://www.banggood.com/1-Bit-AC-220V-Optocoupler-Isolation-Module-Voltage-Detect-Board-Adaptive-3-5VPLC-Isolamento-Fotoaccoppiatore-M-p-1559478.html>

![](/media/2020/03/word-image-3.jpeg)

La résistance d’entrée de 2W est bien dimensionnée : elle doit dissiper effectivement 0.35 W. La sérigraphie « HIGH VOLTAGE » monte bien la partie exposée au secteur, donc dangereuse. Afin de mieux connaitre les performances du circuit, j’en relève le schéma. Il possède 7 composants.

![](/media/2020/03/word-image-4.jpeg)

Un redresseur crée une alimentation continue, avec une zéner de 5.1V (inutile…) et un lissage par C1 de 100 uF. Le courant traverse une LED affichant la présence de tension sur J1, puis l’optocoupleur. Ici, le câblage donne une information inversée : une tension sur l’entrée J1 provoque la conduction entre les PIN 3 et 4 de U1. La sortie de l’opto tire la pull-up de 47K à 0V. Sans aucun doute, la « boille » qu’est C1 va lisser la tension sans qu’on puisse lire précisément une modulation PWM du 230VAC. La LED verte s’illumine mieux que sur mon montage prototype : en effet, les deux LEDs se divisaient le courant : une pour les alternances positives et l’autre les négatives.

## Signal sans filtre – C1 retiré

Le passage à zéro du secteur provoque une pulse de 0.48 millisecondes, plus fine que mon prototype grâce à la R 47K de pull-up plus grande, et aussi de l’opto qui a un plus grand gain.

![](/media/2020/03/word-image-2.png)

## Filtrage avec un C en sortie

Afin de filtrer cette impulsion de manière judicieuse, je pose un C de 100 nF entre le signal et la masse (soit entre J2/2 et J2/3). La pulse ne dépasse pas 688 mV, et un Arduino verra ceci comme un ‘0’ logique.

![](/media/2020/03/word-image-3.png)

## Pulse avec pull-up renforcée

Comme un Arduino peut programmer une pull-up interne d’environ 47K sur une entrée, je simule celle-ci avec une R de 47K en parallèle de R2, ce qui donne 23.5K :

![](/media/2020/03/word-image-4.png)

La tension de pointe passe sans surprise à 1.34V, et la largeur de l’impulsion à 50% de sa hauteur augmente. Le niveau logique risque, dans ce cas, d’être considéré comme un ‘1’ logique.

## Conclusion

Un montage simple, comportant l’isolation galvanique séparant l’alimentation du secteur et la basse tension du microcontrôleur, permet à ce dernier de lire en tout-ou-rien la tension du secteur. En choisissant judicieusement le filtrage, la possibilité de lire précisément une tension commutée par période est possible.

Yves Masur (2/2020)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
