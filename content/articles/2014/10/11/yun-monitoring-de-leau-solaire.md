---
title: "Yun – Monitoring de l’eau solaire"
date: "2014-10-11T13:38:05"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "ecologie", "embarque", "graphiques", "hardware", "linux", "programmation", "software"]
url: "/2014/10/11/yun-monitoring-de-leau-solaire/"
wordpress_id: 1526
comment_count: 1
---

## A quoi ressemble un système d’ECS écologique ?

L’eau chaude sanitaire (ECS) de mon logis est une combinaison écologique : le gaz, qui sert aussi au chauffage de l’immeuble produit l’énergie pour chauffer l’eau. Un système avec capteurs solaires sur le toit permet de limiter l’usage du gaz. Le stockage de l’eau chaude est en 2 volumes de 200 litres : un premier pour le circuit solaire, le second pour l’ECS.

[![schema ECS](/media/2014/10/1-schema.jpg)](/media/2014/10/1-schema.jpg)

Ces deux volumes, d’un total de 400 litres, sont cascadés. Le soutirage d’ECS est donc complété par l’eau solaire, qui elle-même est alimenté par l’eau du réseau. SI la température de l’ECS descend en dessous de 43° (réglable), le chauffage à gaz s’active et la remonte à environ 48°. Pour le solaire, une sonde sur les capteurs vérifie que la température est 8° supérieure à celle du volume d’eau solaire : une pompe de circulation commence à tourner et s’arrête si la différence n’est plus que de 4°. Ce pilotage est assuré par un boitier électronique séparé (<http://www.viessmann.ch/content/ch/fr_ch/habitations/produits/Systemes_solaires/vitosolic.html> )

Explication du fabricant, ici :

<http://www.viessmann.ch/content/ch/fr_ch/habitations/produits/Systemes_solaires/Production_solaire_d_eau_chaude_sanitaire.html>

Sur le schéma, on voir +/- clairement les deux circuits ; et dans le solaire, bloc de gauche, 2 thermomètres ‘T’ et une pompe.

## Est-il écologique ?

Donc tout est fait pour que l’énergie solaire soit utilisée au mieux. S’il n’y en a pas la nuit ou un jour de pluie, la pompe doit s’arrêter. On soutire de l’eau déjà tempérée ce qui est mieux que celle du réseau à 8-10°C. Si par beau temps continu l’eau viendrait à monter à plus de 65°C, la pompe devrait s’enclencher la nuit pour… refroidir. En effet, il suffit d’une série de beau et de vacances l’été pour que la température monte, monte… et endommage le système.

## Doutes

Mais voilà… En 2013, ma consommation d’électricité a légèrement augmenté. C’est louche. Mon but est de descendre en dessous de 2 MWH.

Mais voilà… Dès qu’il fait gris, l’eau chaude n’a plus son « pep » habituel.

Mais voilà… en rentrant le soir, parfois à 22h, j’entends au sous-sol la pompe solaire qui tourne…

Bizarre, non ? Je commence à noter.

[![notes manuscrites](/media/2014/10/2-notes-param.jpg)](/media/2014/10/2-notes-param.jpg)

La date, l’heure, le temps, le compteur du gaz, les températures, l’état de la pompe. Une appréciation concernant l’ensoleillement. Mais souvent les données manquent. Comme je n’ai pas une vocation de rat de cave ni de releveur de compteurs, je décide d’employer un Arduino Yun pour ce faire.

## Enregistrement des paramètres

Le montage est fait rapidement : 3 sondes et un relais en parallèle sur l’alimentation de la pompe pour donner son état. Les sondes sont un modèle assez précis, qui travaille avec un bus « on-wire ». Elles ont un connecteur Groove. Plutôt que le Groove Shield, j’utilise celui du Pr Nicoud, le LearnCbot qui a l’avantage d’avoir 2 boutons poussoirs et 4 LEDs. Un bloc secteur USB (non visible sur la photo) alimente le Yun.

[![Yun ECS](/media/2014/10/Yun-ecs-832x1024.jpg)](/media/2014/10/Yun-ecs.jpg)

On remarque sur la photo de ce bricolage les différent éléments, fixés par un rail DIN 35 mm au mur de la buanderie dans un boitier trop petit… contenant le relais « pompe » et une extension Groove pour les 3 sondes.

Comme je mets au point le soft sur mon bureau, j’utilise le bouton comme simulation de la pompe ; une LED pour montrer que l’on voit la pompe active et une LED supplémentaire pour montrer l’activité WEB et une dernière comme signal de vie, elle clignote à la seconde.

La dernière version du soft permet d’afficher sur une page l’instantané des données, puis toute les 10 minutes d’enregistrer les infos dans un fichier mensuel sur la carte SD. Avec un format tabulaire, compatible Excel. Comme le Yun est connecté au WiFi de la maison, je peux ouvrir un browser et consulter en temps réel les données ou en examiner l’enregistrement ; puis les copier et les analyser avec un tableur et en faire des courbes plus parlantes.

## Résultats

Les courbes représentent :

-   1\) bleue l’état de la pompe (0 : Off ; 10 : On)
-   2\) brune : température au retour des capteurs
-   3\) grise : eau solaire
-   4\) jaune : eau sanitaire

[![3-pompe-ko](/media/2014/10/3-pompe-ko.jpg)](/media/2014/10/3-pompe-ko.jpg)

On voit clairement que la pompe est inutilement enclenchée et refroidi l’eau solaire ! D’entrée, je décide d’abaisser la vitesse de la pompe solaire de 3 (75W) à 2 (60W) pour diminuer le gaspillage électrique. Par contre, la circulation entre les deux volumes : eau solaire et ECS, est idéale. L’ECS colle parfaitement à la montée de température, et s’isole lorsque l’eau solaire refroidit. J’en avise l’installateur, courbe à l’appui. Après quelques tribulations et échanges, le diagnostic tombe : le régulateur a une panne intermittente. Une fois la réparation effectuée par le changement du régulateur, voici ce que ça donne :

[![3-pompe-vitesse2](/media/2014/10/3-pompe-vitesse2.jpg)](/media/2014/10/3-pompe-vitesse2.jpg)

Le fonctionnement En/Hors de la pompe recherche désormais bien l’énergie ; mais son état indiqué est un peu trop rigide : il suffit qu’elle ne soit pas enclenchée lors de la mesure pour indiquer un « 0 », ou que ce soit la dernière seconde avant l’arrêt pour qu’un « 10 » peu représentatif soit enregistré.

On remarque aussi que la pompe travaille par à-coups. Lorsque la température est atteinte, le circuit envoie une grande quantité d’eau fraiche dans les capteurs. Ceux-ci n’arrivent pas à la maintenir au-dessus du seuil de déclenchement. La circulation arrêtée, la température remonte ; et on recommence. Je décide de la régler sur la vitesse 1 (40W), la plus basse ; et je modifie le soft pour indiquer un pourcentage d’utilisation dans la tranche des 10 minutes.

[![3-pompe-vitesse1](/media/2014/10/3-pompe-vitesse1.jpg)](/media/2014/10/3-pompe-vitesse1.jpg)

A la fin d’un tel jour, qui a tout de même vu passer des nuages entre 14H00 et 14H40, il y a 400 litres d’eau à 60°C. Merci soleil !

Il reste quelques possibilités d’amélioration. Par exemple, au premier « turbinage » du matin, tout l’eau de la colonne de 12 m jusqu’au toit refroidit forcément fortement les capteurs. Idéalement, on devrait temporiser un peu avant d’enclencher la pompe et attendre un delta plus important de température.

Ces données ont été partagées avec l’installateur. Voici son dernier email :

Le 06.10.2014 14:56, [\<protection de l’anonymat\>](mailto:albert.cusin@swissolaire.ch) a écrit :

Bonjour,

J’ai un client qui a le même problème, ne sachant pas si c’est le  circulateur ou la régulation, je vous demande si vous me mettriez l’enregistreur à ma disposition, autrement, je vous le rachète, Si le programme des relevés va avec ?

## Conclusion

Grâce à un système de mesure précis, un défaut de l’installation de production d’ECS difficile à mettre en évidence a pu être identifié et éliminé ; et un réglage optimal de l’installation fait. Ces prochains mois j’espère économiser du gaz et de l’électricité ; j’ai un suivi instantané et archivé du fonctionnement de l’installation. Cependant, pour pouvoir mettre le système à disposition d’un tiers, il reste à peaufiner le logiciel. Ceci est une autre histoire, qui fera (probablement) l’objet d’un article sur les techniques mises en œuvre sur la plateforme Arduino Yun, Linux, avec code C++, Javascript, Wifi, bus One Wire.

Yves Masur (10/2014

## Commentaires

### Alain — 11 octobre 2014 à 19:12

Bravo pour la découverte du problème ! ça me rappelle un reportage (de TV France 2) qui citait des exemples de propriétaires qui avaient investi dans des panneaux solaires sans jamais avoir vu une quelconque production d’énergie.\
Au fait ton installateur doit être fort content de ta « bricole » mais devrait s’attendre à payer le prix du « dépannage » de toutes les installations qu’il a bien pu faire… Un « service » qui vaut son pesant de MWH !

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
