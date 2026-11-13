---
title: "Barrette secteur – la plateforme de développement"
date: "2009-01-04T21:21:58"
lastmod: "2015-11-28T17:43:07"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["ecologie", "hardware", "linux", "processeurs", "programmation"]
url: "/2009/01/04/barette-secteur-la-plateforme-de-developpement/"
wordpress_id: 143
comment_count: 4
---
<p><strong>Barette secteur écologique – le hardware à choisir</strong></p>
<p>Il s’agit maintenant de savoir sur quel hardware le logiciel va être développé. Après une scrutation du catalogue Conrad, qui propose C-Control (trop gros, trop ciblé) un kit Java (pas assez de I/O) et différents kits PIC ou Atmel (pas assez WEB), j’étudie ce que Lextronic propose (<a href="http://www.lextronic.fr/R350-module-netmedia.html">http://www.lextronic.fr/R350-module-netmedia.html</a> ) et parmi la kyrielle des propositions, nous trouvons les produits intéressants qui conviendraient.</p>
<p><strong>Module Freescale</strong></p>
<p><a href="http://www.lextronic.fr/P852-starter-kit-dnpsk16l.html">http://www.lextronic.fr/P852-starter-kit-dnpsk16l.html</a> un kit starter-kit « DNP/SK16L ». Il contient tout ce qu’il faut pour développer des applications embarquées sur la base d’un processeur Freescale™ ColdFire™ 32 bits MCF5282. Ce dernier comprend une platine support sur laquelle est présente un module DIL/NetPC « DNP/5280 » avec un système d’exploitation « <strong>µCLinux</strong> » pré-chargé en usine (Linux Kernel version 2.4.22), à 245 €.</p>
<dl>
<dt><img alt="module Freescale" height="153" src="http://www.lextronic.notebleue.com/imagelib/25/stk16l3.jpg" title="module Freescale" width="170"/></dt>
</dl>
<p>Le bloc CPU seul (donc pour la production) coûte 162€.</p>
<figure><img alt="Platine Freescale" height="78" src="http://www.lextronic.notebleue.com/imagelib/25/dnp8520a.jpg" title="Platine Freescale" width="227"/><figcaption>Platine Freescale</figcaption></figure>
<p>Il a visiblement pas mal pour plaire. Un coup d’œil sur le hard me montre qu’il y a assez de I/O, une prise Ethernet, tout ce qu’il faut pour faire un miniserveur, il supporte Telnet, FTP, DHCP, etc. Et consomme env. 300 mA sous 3,3V (soit ~1 W). On peut le configurer avec une horloge RTC et pile de sauvegarde – très important pour l’application en vue!</p>
<p><strong>Linux… et Windows?</strong></p>
<p>Sur ce genre de plateforme, le soft est fait d’habitude en cross compilation avec GNU C/C++, év. En Java. Mais sur plateforme Linux. Par contre ici est proposé un ensemble <strong>colinux</strong>, soit une version de Linux qui tourne sur Windows 2000/XP et Vista (explications ici: <a href="http://www.dilnetpc.com/coLinux-APN1-e.pdf">http://www.dilnetpc.com/coLinux-APN1-e.pdf</a> ) . J’ai testé sur mon PC, ça se lance comme proposé.</p>
<p><strong>Platine FOX</strong></p>
<p>Le fabricant Axis (caméra…) propose une platine également intéressante, pour 167€.</p>
<figure><img alt="Platine FOX" height="230" src="http://www.lextronic.notebleue.com/imagelib/20/fox3.jpg" title="Platine FOX" width="482"/><figcaption>Platine FOX</figcaption></figure>
<p>Malgré sa petitesse, elle a tout ce qu’il faut, ou presque: Même si tous les ports ne sont pas utilisable en même temps, pour nous c’est OK, d’autant plus que c’est 5 VDC compatible. Par contre, il faut prévoir un interfaçage de la carte avec un circuit horloge (RTC) externe via le bus I2C™, qui est proposé dans la description.</p>
<p><strong>Platine ARM9</strong></p>
<p>Sur base de CPU ARM9 de Atmel, il y a une platine DIL en promo, c’est la plus puissante des propositions:</p>
<p><a href="http://www.lextronic.fr/P856-module-dilnetpc-dnp9200.html">http://www.lextronic.fr/P856-module-dilnetpc-dnp9200.html</a> pour 109€, ressemblant à la première proposée. Mais il faut aussi ajouter une RTC externe. Le kit de développement coûte 246€.</p>
<figure><img alt="Platine DIL ARM" height="78" src="http://www.lextronic.notebleue.com/imagelib/25/dnm9200a.jpg" title="Platine DIL ARM" width="230"/><figcaption>Platine DIL ARM</figcaption></figure>
<p>Consommation est aussi de l’ordre de 1W.</p>
<p>Les autres platine/kit de Lextronic semblent soit trop puissants pour notre application, soit trop orientés I/O et/ou ne sont pas prévus pour une horloge temps réel. A moins de se taper des tonnes de doc et la réalisation détaillée.</p>
<p>Si quelqu’un a une avis sur ce trio, ou bien entendu une autre solution, il faut le faire savoir!</p>
<p>Yves Masur</p>

## Commentaires

### Alain Tornare — 10 janvier 2009 à 20:10

<section class="comment-content comment">
<p>Je propose à Yves de regarder les caractéristiques de la platine SBC65EC de Modtronix. Je l’ai eue pour FRS 45.- + 11.- de port en juillet 2008, mais ils ont dû remarquer que c’était trop bon marché pour les performances, elle vaut maintenant 100.- AU$ + port, et depuis la Suisse, on doit payer en $AU . cours 0.79<br/>
Le lien pour toute la doc:<br/>
<a href="http://www.modtronix.com/product_info.php?products_id=149" rel="nofollow ugc">http://www.modtronix.com/product_info.php?products_id=149</a></p>
<p>A+<br/>
Alain</p>
 </section>

### Yves Masur — 11 janvier 2009 à 21:54

<section class="comment-content comment">
<p>Effectivement, ce hard semble tout à fait <strong>adéquat!</strong> Il ne consomme que 0.7W (et on peut encore le baisser en changeant la F Clock). J’ai juste un petit doute sur la façon et le coût du soft; par exemple, un compilateur C… Il faudra aussi penser à l’horloge en temps réel, qu’il faudra ajouter.<br/>
A priori, le stack IP convient, et le webserver proposé suffit à nos besoins.<br/>
A noter qu’il en existe d’autres, pae ex.: <a href="http://makezine.com/controller/" rel="nofollow ugc">http://makezine.com/controller/</a> à 109 $!</p>
 </section>

### Laurent Francey — 17 janvier 2009 à 17:29

<section class="comment-content comment">
<p>En lisant mon dernier Elektor de l’année dernière, j’ai vu une publicité d’une platine « MiniCore™ RCM5700 ». Celle-ci est a tout ce qu’il nous faut, même l’horloge ! y compris circuiterie pour la pile de sauvegarde !<br/>
Le kit standard de développement comprenant une carte avec le compilateur C vaut 49$ ou 49€ !!! de plus elle est minuscule !<br/>
Voir les spécifications sur le site : <a href="http://www.rabbit.com/products/rcm5700/#specs" rel="nofollow ugc">http://www.rabbit.com/products/rcm5700/#specs</a></p>
<p>Il y a même une représentation en suisse !</p>
<p>A voir, mais celle-ci me plait bien, elle est puissante, et le temps investit pour la mise en marche pourrait servir également à d’autres projets !</p>
 </section>

### Yves Masur — 18 janvier 2009 à 10:09

<section class="comment-content comment">
<p>Argh! en effet, cette platine est super intéressante… Mais j’ai <b>déjà</b> commandé le kit australien proposé par Alain et le chip horloge. Après avoir consulté le code source et la technique utilisée.<br/>
J’avais déjà été intéressé par les kits Rabbit (et leur processeurs) par le passé, mais ce nom ne m’était pas revenu à l’esprit.<br/>
A prix du $ australien, la différence de prix devrait se tenir entre les 2 solutions. La consommation est quasi la même (0.6 W), bien que la carte Rabbit sans Ethernet peut singulièrement sa puissance.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
