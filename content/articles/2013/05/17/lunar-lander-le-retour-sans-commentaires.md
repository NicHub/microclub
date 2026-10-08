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
<p><img alt="" height="262" src="http://visualnews.columnfivemedia.netdna-cdn.com/wp-content/uploads/2010/11/pagecover.jpg" width="197"/>En écrivant <a href="http://www.drgoulu.com/2013/04/28/pourquoi-je-kiffe-la-science/" target="_blank">pourquoi j’aime la science</a>, je me suis souvenu d’un de mes premiers programmes en BASIC : un simulateur d’alunissage. « Simulateur » parait un peu prétentieux aujourd’hui pour un programme qui fonctionnait en mode texte et pas en temps réel, mais j’en étais très fier.</p>
<p>Au point d’avoir envie de le résusciter, mais comme je n’ai plus de PET 2001 capable de relire une cassette d’époque que je n’ai plus, je me suis rabattu sur un plan B:</p>
<ol>
<li>retrouver le livre « <a href="http://openlibrary.org/works/OL8683892W" target="_blank">Basic Computer Games</a> » de David H. Ahl</li>
<li>retrouver le listing du simulateur d’alunissage qui y était. <a href="http://atariarchives.org/basicgames/showpage.php?page=106" target="_blank">La page est là</a>, scannée en piètre qualité</li>
<li>avant de retaper le programme, essayer <a href="http://finereader.abbyyonline.com/fr/Task/Queue">ABBYY Online</a>, un service d’OCR en ligne que j’avais déjà utilisé et qui donne des résultats très largement meilleurs que les autres. Ca marche ! le résultat a très peu besoin d’être édité et voilà:<br/>
[code]10 PRINT TAB(33);"LUNAR"<br/>
20 PRINT TAB(13);"CREATIVE COMPUTING MORRISTOWN, NEW JERSEY"<br/>
25 PRINT:PRINT:PRINT<br/>
30 PRINT "THIS IS A COMPUTER SIMULATION OF AN APOLLO LUNAR"<br/>
40 PRINT "LANDING CAPSULE.": PRINT: PRINT<br/>
30 PRINT "THE ON-BOARD COMPUTER HAS FAILED (IT WAS MADE BY"<br/>
60 PRINT "XEROX) SO YOU HAVE TO LAND THE CAPSULE MANUALLY."<br/>
70 PRINT: PRINT "SET BURN RATE OF RETRO RQCKEIS TO ANY VALUE BETWEEN"<br/>
80 PRINT "0 (FREE FALL) AMD 200 (MAXIMUM BURN) POUNDS PER SECOND."<br/>
90 PRINT "SET NEW BURN RATE EVERY 10 SECONDS.": PRINT<br/>
100 PRINT "CAPSULE WEIGHI 32,500 LBS; FUEL WEIGHT 16,500 LBS."<br/>
110 PRINT: PRINT: PRINT: PRINT "GOOD LUCK"<br/>
120 L=0<br/>
130 PRINT: PRINT "SEC","HI FT","MPH","LB FUEL","BURN RATE":PRINT<br/>
140 A=120:V=1:M=33000:N=16500:G=1E-03:Z=1.8<br/>
150 PRINT L,INT(A);INT(5280*(A-INT(A))),3606*V,H-M:INPUT K:T=10<br/>
160 IF M-N&lt;1E-03 THEN 240<br/>
170 IF T&lt;1E-03 THEN 150<br/>
180 S=T: IF M&gt;=N+S*K THEN 200<br/>
190 S=(M-N)/K<br/>
200 GOSUB 420: IF I&lt;=0 THEN 340<br/>
210 IF V&lt;=0 THEN 230<br/>
220 IF J&lt;0 THEN 370<br/>
230 GOSUB 330: GOTO 150<br/>
240 PRINT "FUEL OUT AT";L;"SECONDS":S=(-V*SQR(V*V+2*A*G))/G<br/>
250 V=V+G*S: L=L-S<br/>
260 W=3600*V: PRINT "ON MOON AT";L;"SECONDS – IMPACT VELOCITY";W;"MPH"<br/>
270 IF W&lt;=1.2 THEN PRINT "PERFECT LANDING!": GOTO 440<br/>
280 IF W&lt;=10 THEN PRINT "GOOD LANDING (COULD BE BETTER)":GOTO 440<br/>
282 IF W&gt;60 THEN 300<br/>
284 PRINT "CRAFT DAMAGE… YOU’RE STRANDED HERF. UNTIL A RESCUE"<br/>
286 PRINT "PARIY ARRIVES. HOPE YOU HAVE ENOUGH OXYGEN!"<br/>
288 GOTO 440<br/>
300 PRINT "SORRY THERE ARE NO SURVIVORS. YOU BLEU IT!"<br/>
310 PRINT "IN FACT, YOU BLASTED A NEW LUNAR CRATER";W*.277;"FEET DEEP !"<br/>
320 GOTO 440<br/>
330 L=L+S: T=T-S: M=M-S*K: A=I: V=J:RETURN<br/>
340 IF S&lt;5E-03 THEN 260<br/>
350 D=V+SQR(V*V+2*A*(G-Z*K/M)):S=2*A/D<br/>
360 GOSUB 420: GOSUB 330: GOTO 340<br/>
370 W=(1-M*G/(Z*K))/2: S=M*V/(Z*K*(W+SQR(W*W+V/Z)))+.05:GOSUB 420<br/>
380 IF I&lt;=0 THEN 340<br/>
390 GOSUB 330: IF J&gt;0 THEN 160<br/>
400 IF V&gt;0 THEN 370<br/>
410 GOTO 160<br/>
420 R=S*K/M: J=V+G*S+Z*(-R-Q*Q/2-Q^3/3-Q^4/4-Q^5/5)<br/>
430 I=A-G*S*S/2-V*S+Z*S*(R/2+Q^2/6+Q^3/12+Q^4/20+Q^5/30):RETURN<br/>
440 PRINT:PRINT:PRINT:PRINT "TRY AGAIN??":GOTO 70[/code]</li>
<li>il ne reste plus qu’à trouver un interpréteur BASIC d’époque… Heureusement, internet regorge de geeks nostalgiques, donc on trouve plusieurs interpréteurs BASIC écrits en Javascript, donc permettant d’exécuter ce genre de vieux programmes dans une page web. Après en avoir essayé plusieurs, le meilleur me semble être « <a href="http://www.calormen.com/applesoft/" target="_blank">Applesoft BASIC in Javascript</a> » de Joshua Bell.<br/>
Un petit cut&amp;paste, on clique sur RUN et la machine à remonter le temps fonctionne !<br/>
<a href="/2013/05/17/lunar-lander-le-retour-sans-commentaires/capture-2/" rel="attachment wp-att-1242"><img alt="Capture" height="425" src="/media/2013/05/Capture.png" width="601"/></a></li>
</ol>
<p>Bon, en fait elle ne fonctionne pas tant bien que ça. Il doit y avoir un bug soit dans l’interpréteur BASIC en Javascript, soit dans le programme BASIC, ce qui ne serait pas étonnant vu l’OCR.</p>
<p>Et c’est là qu’on s’aperçoit que la lisibilité des programmes a quand même fait des progrès en 35 ans, parce que ce listing est une véritable horreur ! Dire que non seulement on osait publier ça, mais que c’était même un best seller avec lequel une génération de programmeurs a appris la programmation… Des variables d’une seule lettre, d’horribles formules mêlant des constantes parachutées, le tout sans le moindre commentaire.</p>
<p>Pourtant il existait déjà une instruction REM pour ça en BASIC, mais ça n’était pas dans les moeurs. Un programme devait être lisible par les machines, pas pour les humains…</p>

## Commentaires

### Jdu — 18 mai 2013 à 07:34

<section class="comment-content comment">
<p>On appelle çà la programmation spaghetti.<br/>
Quand aux commentaires dans les programmes, ce n’est toujours pas entré dans le mœurs.  Même chose pour la doc.</p>
 </section>

### Claude — 23 mai 2013 à 20:29

<section class="comment-content comment">
<p>Tu oublies un tout petit détail: à l’époque, les commentaires prenait de la place mémoire. Donc, beaucoup de commentaires=peu de place pour le code.<br/>
Hé oui, ça ne nous rajeuni pas….</p>
 </section>

### MHP — 21 août 2013 à 12:14

<section class="comment-content comment">
<p>Merci pour cette tranche de nostalgie informatique.</p>
<p>J’ai aussi connu les « simulateurs » d’alunissage sur calculatrices programmables, en 1980 sur une SR-56 de Texas Instrument, les ordinateurs étaient encore hors de prix.</p>
<p>Il y a quelques mois, j’ai acheté une HP 35S et j’ai trouvé le listing d’un simulateur d’alunissage sur Internet qui m’a permis de replonger dans cette époque !</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
