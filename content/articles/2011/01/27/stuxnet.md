---
title: "Stuxnet"
date: "2011-01-27T22:59:49"
lastmod: "2015-04-24T23:20:19"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["non-classe", "stuxnet", "virus"]
url: "/2011/01/27/stuxnet/"
wordpress_id: 433
comment_count: 1
---
En juin 2010, des sociétés de sécurité informatique comme Symantec ont détecté un [ver informatique](https://secure.wikimedia.org/wikipedia/fr/wiki/Ver_informatique) assez étrange : il était très complexe, sophistiqué et extrêmement discret puisqu’il ne fait apparemment rien du tout sur les ordinateurs infectés. Il a fallu environ 3 mois de travail intensif pour comprendre ce qu’il fait réellement, et encore 3 mois pour en être vraiment sur tellement c’était étonnant. En plus on a réalisé que Stuxnet circulait depuis environ un an sans avoir été détecté…

Sur chaque ordinateur infecté, [Stuxnet](http://fr.wikipedia.org/wiki/Stuxnet), c’est son nom,  cherche  le logiciel [Simatic Step7 de Siemen](http://www.automation.siemens.com/mcms/simatic-controller-software/en/step7/Pages/Default.aspx)s qui sert à programmer les [automates programmables (PLC en anglais)](http://fr.wikipedia.org/wiki/Automate_programmable_industriel) Siemens, probablement les plus utilisés dans le monde pour la commande d’installations industrielles comme des usines électriques, des raffineries de pétrole ou les  feux de circulation. S’il trouve Step7, Stuxnet cherche dans le code source du PLC s’il servait à commander un grand nombre de moteurs électriques d’un certain type. Et seulement dans ce cas, Stuxnet envoie ce code source à un certain site web, en passant par des clés USB si aucune connexion à internet n’est disponible. Ensuite, Stuxnet attendait gentiment que le site web lui envoie un nouveau code source, ou plus exactement une sorte de « patch » de ce code. Et la prochaine fois que l’utilisateur de ce PC utilisait Step7 pour programmer son PLC, Stuxnet envoyait le code « patché ».

En résumé, le PLC ciblé soigneusement se mettait à exécuter de façon totalement invisible des fonctions envoyées par le site web à la place, ou en plus, du code normal. Tout ceci est démontré dans cette video, en anglais :

\[youtube cf0jlzVCyOI\]

Aujourd’hui il est quasi certain que Stuxnet est le premier virus informatique « militaire » écrit par un ou plusieurs états pour attaquer spécifiquement des installations industrielles stratégiques d’un autre état, en l’occurrence les centrifugeuses servant à l’enrichissement de l’uranium en Iran. Stuxnet a apparemment réussi à les faire tourner à la mauvaise vitesse, voire à les détruire partiellement. Certains articles affirment que le programme nucléaire iranien a pris 5 ans de retard grâce à Stuxnet !

Ce qu’il faut bien réaliser, c’est que Stuxnet aurait pu être dévastateur s’il n’avait pas été aussi soigneusement ciblé. D’abord Stuxnet aurait pu remonter à ses créateurs tous les programmes des PLC rencontrés, ce qui aurait constitué un cas d’espionnage industriel unique. Visiblement les auteurs ne souhaitaient pas se mettre à dos les pays industrialisés et leurs plus grosses entreprises…

Ensuite, si ça avait été le but des auteurs de Stuxnet, ils auraient pu le programmer pour faire tomber en panne, voire détruire les installations sur commande, et comme il s’agit en grande partie d’infrastructures importantes, Stuxnet aurait pu être une véritable arme de guerre.

Du point de vue informatique, Stuxnet est une merveille qui a demandé des années\*hommes de travail de la part de hackers de très haut niveau, qui ont exploité au moins 4 failles de Windows inconnues à ce moment là (à croire qu’ils avaient leurs entrées chez Bill…) ainsi que des connaissances pointues sur Step7 et les PLC Siemens…

Mais qui peut-ce bien être ?

1. « [SIMATIC WinCC / SIMATIC PCS 7: Information concerning Malware / Virus / Trojan](http://support.automation.siemens.com/WW/llisapi.dll?func=cslib.csinfo&lang=en&objid=43876783&caller=view)\
    « [Exploring Stuxnet’s PLC Infection Process](http://www.symantec.com/connect/blogs/exploring-stuxnet-s-plc-infection-process)« , Symantec, 21 septembre 2010
2. « [Iran : la cyber attaque a déjà commencé](http://www.mediapart.fr/club/blog/michbret/260910/iran-la-cyber-attaque-deja-commence)« , Mediapart 26 septembre 2010
3. « [How to Hijack a Controller : Why Stuxnet Isn’t Just About Siemens’ PLCs](http://www.controlglobal.com/articles/2011/IndustrialControllers1101.html) » 13 janvier 2011

## Commentaires

### Yves Masur — 2 février 2011 à 21:57

Les automates Step 7 sont utilisé pour nombre d’applications industrielles et également en réseau, mais **pas** pour les feux de circulation. C’est du matériel spécifique (aussi chez Siemens!).

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
