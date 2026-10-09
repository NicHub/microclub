---
title: "Lunar Lander : le retour (sans commentaires)"
date: "2013-05-17T17:37:13"
lastmod: "2015-04-24T23:20:17"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["basic", "nostalgie"]
url: "/2013/05/17/lunar-lander-le-retour-sans-commentaires/"
wordpress_id: 1219
comment_count: 3
---
![](http://visualnews.columnfivemedia.netdna-cdn.com/wp-content/uploads/2010/11/pagecover.jpg)En écrivant [pourquoi j’aime la science](http://www.drgoulu.com/2013/04/28/pourquoi-je-kiffe-la-science/), je me suis souvenu d’un de mes premiers programmes en BASIC : un simulateur d’alunissage. « Simulateur » parait un peu prétentieux aujourd’hui pour un programme qui fonctionnait en mode texte et pas en temps réel, mais j’en étais très fier.

Au point d’avoir envie de le résusciter, mais comme je n’ai plus de PET 2001 capable de relire une cassette d’époque que je n’ai plus, je me suis rabattu sur un plan B:

1. retrouver le livre « [Basic Computer Games](http://openlibrary.org/works/OL8683892W) » de David H. Ahl
2. retrouver le listing du simulateur d’alunissage qui y était. [La page est là](http://atariarchives.org/basicgames/showpage.php?page=106), scannée en piètre qualité
3. avant de retaper le programme, essayer [ABBYY Online](http://finereader.abbyyonline.com/fr/Task/Queue), un service d’OCR en ligne que j’avais déjà utilisé et qui donne des résultats très largement meilleurs que les autres. Ca marche ! le résultat a très peu besoin d’être édité et voilà:\
    \[code\]10 PRINT TAB(33);"LUNAR"\
    20 PRINT TAB(13);"CREATIVE COMPUTING MORRISTOWN, NEW JERSEY"\
    25 PRINT:PRINT:PRINT\
    30 PRINT "THIS IS A COMPUTER SIMULATION OF AN APOLLO LUNAR"\
    40 PRINT "LANDING CAPSULE.": PRINT: PRINT\
    30 PRINT "THE ON-BOARD COMPUTER HAS FAILED (IT WAS MADE BY"\
    60 PRINT "XEROX) SO YOU HAVE TO LAND THE CAPSULE MANUALLY."\
    70 PRINT: PRINT "SET BURN RATE OF RETRO RQCKEIS TO ANY VALUE BETWEEN"\
    80 PRINT "0 (FREE FALL) AMD 200 (MAXIMUM BURN) POUNDS PER SECOND."\
    90 PRINT "SET NEW BURN RATE EVERY 10 SECONDS.": PRINT\
    100 PRINT "CAPSULE WEIGHI 32,500 LBS; FUEL WEIGHT 16,500 LBS."\
    110 PRINT: PRINT: PRINT: PRINT "GOOD LUCK"\
    120 L=0\
    130 PRINT: PRINT "SEC","HI FT","MPH","LB FUEL","BURN RATE":PRINT\
    140 A=120:V=1:M=33000:N=16500:G=1E-03:Z=1.8\
    150 PRINT L,INT(A);INT(5280\*(A-INT(A))),3606\*V,H-M:INPUT K:T=10\
    160 IF M-N\<1E-03 THEN 240\
    170 IF T\<1E-03 THEN 150\
    180 S=T: IF M\>=N+S\*K THEN 200\
    190 S=(M-N)/K\
    200 GOSUB 420: IF I\<=0 THEN 340\
    210 IF V\<=0 THEN 230\
    220 IF J\<0 THEN 370\
    230 GOSUB 330: GOTO 150\
    240 PRINT "FUEL OUT AT";L;"SECONDS":S=(-V\*SQR(V\*V+2\*A\*G))/G\
    250 V=V+G\*S: L=L-S\
    260 W=3600\*V: PRINT "ON MOON AT";L;"SECONDS – IMPACT VELOCITY";W;"MPH"\
    270 IF W\<=1.2 THEN PRINT "PERFECT LANDING!": GOTO 440\
    280 IF W\<=10 THEN PRINT "GOOD LANDING (COULD BE BETTER)":GOTO 440\
    282 IF W\>60 THEN 300\
    284 PRINT "CRAFT DAMAGE… YOU’RE STRANDED HERF. UNTIL A RESCUE"\
    286 PRINT "PARIY ARRIVES. HOPE YOU HAVE ENOUGH OXYGEN!"\
    288 GOTO 440\
    300 PRINT "SORRY THERE ARE NO SURVIVORS. YOU BLEU IT!"\
    310 PRINT "IN FACT, YOU BLASTED A NEW LUNAR CRATER";W\*.277;"FEET DEEP !"\
    320 GOTO 440\
    330 L=L+S: T=T-S: M=M-S\*K: A=I: V=J:RETURN\
    340 IF S\<5E-03 THEN 260\
    350 D=V+SQR(V\*V+2\*A\*(G-Z\*K/M)):S=2\*A/D\
    360 GOSUB 420: GOSUB 330: GOTO 340\
    370 W=(1-M\*G/(Z\*K))/2: S=M\*V/(Z\*K\*(W+SQR(W\*W+V/Z)))+.05:GOSUB 420\
    380 IF I\<=0 THEN 340\
    390 GOSUB 330: IF J\>0 THEN 160\
    400 IF V\>0 THEN 370\
    410 GOTO 160\
    420 R=S\*K/M: J=V+G\*S+Z\*(-R-Q\*Q/2-Q^3/3-Q^4/4-Q^5/5)\
    430 I=A-G\*S\*S/2-V\*S+Z\*S\*(R/2+Q^2/6+Q^3/12+Q^4/20+Q^5/30):RETURN\
    440 PRINT:PRINT:PRINT:PRINT "TRY AGAIN??":GOTO 70\[/code\]
4. il ne reste plus qu’à trouver un interpréteur BASIC d’époque… Heureusement, internet regorge de geeks nostalgiques, donc on trouve plusieurs interpréteurs BASIC écrits en Javascript, donc permettant d’exécuter ce genre de vieux programmes dans une page web. Après en avoir essayé plusieurs, le meilleur me semble être « [Applesoft BASIC in Javascript](http://www.calormen.com/applesoft/) » de Joshua Bell.\
    Un petit cut&paste, on clique sur RUN et la machine à remonter le temps fonctionne !\
    [![Capture](/media/2013/05/Capture.png)](/2013/05/17/lunar-lander-le-retour-sans-commentaires/capture-2/)

Bon, en fait elle ne fonctionne pas tant bien que ça. Il doit y avoir un bug soit dans l’interpréteur BASIC en Javascript, soit dans le programme BASIC, ce qui ne serait pas étonnant vu l’OCR.

Et c’est là qu’on s’aperçoit que la lisibilité des programmes a quand même fait des progrès en 35 ans, parce que ce listing est une véritable horreur ! Dire que non seulement on osait publier ça, mais que c’était même un best seller avec lequel une génération de programmeurs a appris la programmation… Des variables d’une seule lettre, d’horribles formules mêlant des constantes parachutées, le tout sans le moindre commentaire.

Pourtant il existait déjà une instruction REM pour ça en BASIC, mais ça n’était pas dans les moeurs. Un programme devait être lisible par les machines, pas pour les humains…

## Commentaires

### Jdu — 18 mai 2013 à 07:34

On appelle çà la programmation spaghetti.\
Quand aux commentaires dans les programmes, ce n’est toujours pas entré dans le mœurs. Même chose pour la doc.

### Claude — 23 mai 2013 à 20:29

Tu oublies un tout petit détail: à l’époque, les commentaires prenait de la place mémoire. Donc, beaucoup de commentaires=peu de place pour le code.\
Hé oui, ça ne nous rajeuni pas….

### MHP — 21 août 2013 à 12:14

Merci pour cette tranche de nostalgie informatique.

J’ai aussi connu les « simulateurs » d’alunissage sur calculatrices programmables, en 1980 sur une SR-56 de Texas Instrument, les ordinateurs étaient encore hors de prix.

Il y a quelques mois, j’ai acheté une HP 35S et j’ai trouvé le listing d’un simulateur d’alunissage sur Internet qui m’a permis de replonger dans cette époque !

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
