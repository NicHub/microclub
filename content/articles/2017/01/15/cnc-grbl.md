---
title: "CNC GRBL"
date: "2017-01-15T11:18:47"
lastmod: "2017-02-07T19:20:15"
author: "franic"
categories: ["Microclub"]
tags: []
url: "/2017/01/15/cnc-grbl/"
wordpress_id: 2957
comment_count: 1
---
<p>Les imprimantes 3D se sont démocratisées ces dernières années. Une grande partie des modèles « amateurs » sont basées sur des cartes à micro contrôleur Arduino. Les firmewares utilisés interprètent un protocole de commande très proche du code G utilisé pour les machines d’usinage à commandes numériques appelées <a href="https://fr.wikipedia.org/wiki/Machine-outil_%C3%A0_commande_num%C3%A9rique">CNC</a>.</p>
<p>Il n’y a donc qu’un pas à faire pour utiliser ce même hardware et pouvoir piloter une machine 3 axes et en faire une fraiseuse numérique par exemple ou une graveuse (découpeuse) laser.</p>
<p>C’est ce qui a été développé par la communauté et donné naissance au firmware <a href="https://github.com/gnea/grbl/wiki">GRBL</a>. J’utilise depuis une année la version <a href="https://github.com/grbl/grbl">0.9j</a> et maintenant la version <a href="https://github.com/gnea/grbl/releases">1.1</a> est disponible pour des cartes à micro contrôleur Atmega328 ou Atmega2560 type Arduino.</p>
<p>Comme pour les imprimantes 3D il faut encore ajouter des contrôleurs de moteurs. Le hardware utilisé est le même que pour les imprimantes 3D. Pour les cartes Mega2560, j’ai utilisé la fameuse <a href="http://reprap.org/wiki/RAMPS_1.4/fr">RAMPS 1.4</a>. Pour la fraiseuse, j’utilise la plus petite carte <a href="http://blog.protoneer.co.nz/arduino-cnc-shield/">CNC shield</a>, voir ci-dessous.</p>
<p><a href="/media/2017/01/CNC-V3-1.jpg"><img alt="CNC-V3-1" height="300" src="/media/2017/01/CNC-V3-1-300x300.jpg" width="300"/></a></p>
<p>Il faut encore de la mécanique 3 axes. Pour ma part j’ai hésité longtemps à fabriquer mon propre assemblage, mais lorque j’ai vu le prix du système ci-dessous, j’en ai fait l’acquisition; il s’agit du modèle <a href="http://www.ebay.com/itm/Sable-2015-CNC-ROUTER-ENGRAVER-mill-PCBs-engraving-/201775926773?hash=item2efac84df5:g:FrsAAOSw0HVWEmlq">Sable CNC 2015</a> . J’en suis très content. On trouve également la <a href="http://www.ebay.com/itm/ER11-Spindle-for-Sable-2015-SPD-ER11-ENGRAVER-mill-PCBs-engraving-/192066036794?hash=item2cb807243a:m:m__owmNnXyWzIFE8ycGHQ3A">broche</a> avec un moteur DC.</p>
<p><a href="/media/2017/01/XYZ.png"><img alt="CNC" height="297" src="/media/2017/01/XYZ-300x297.png" width="300"/></a></p>
<p>Voilà, le hardware est assemblé, le câblage réalisé, il faut encore un logiciel pour envoyer les commandes « code G » pour piloter la machine. Pour cela j’ai utilisé Universal <a href="https://github.com/winder/Universal-G-Code-Sender">G code Sender</a>, un logiciel simple mais efficace; il y a aussi cette <a href="http://winder.github.io/ugs_website/#universal-gcode-sender">version</a> dite « classic ».</p>
<figure aria-describedby="caption-attachment-2960"><a href="/media/2017/01/GCodeSenderPlateForm.png"><img alt="GCodeSender version PlateForm" height="203" src="/media/2017/01/GCodeSenderPlateForm-300x203.png" width="300"/></a><figcaption>GCodeSender version PlateForm</figcaption></figure>
<p>Plus tard, une fois bien familiarisé avec la machine, j’ai utilisé le logiciel <a href="https://github.com/vlachoudis/bCNC/wiki">bCNC</a>, un logiciel bien abouti. Il permet également de calibrer le plan XY par palpage matriciel. Etant écrit en Python, je vous conseille d’installer la <a href="https://www.python.org/downloads/release/python-2713/">version 2.7</a> de Python ainsi que le <a href="https://pypi.python.org/pypi/pyserial/2.7">plugin seriel</a> pour Python.</p>
<figure aria-describedby="caption-attachment-2961"><a href="/media/2017/01/bCNC.png"><img alt="bCNC, un magnifique logiciel !" height="222" src="/media/2017/01/bCNC-300x222.png" width="300"/></a><figcaption>bCNC, un magnifique logiciel !</figcaption></figure>
<p>Ce logiciel permet de fraiser par contourage des circuits imprimés. Je l’utilise avec des fichiers importés directement depuis le logiciel CAO de <a href="http://server.ibfriedrich.com/wiki/ibfwikifr/index.php/Accueil">Target</a>.</p>
<p>En conclusion, je n’ai pas encore tout découvert, mais cette évolution des CNC’s pour des amateurs devient très intéressante. Merci à Gaël pour ses précieux essais.</p>
<p> </p>
<p>Laurent Francey (1/2017)</p>

## Commentaires

### Claude Balmer — 14 février 2017 à 22:55

<section class="comment-content comment">
<p>Bravo pour l’article. Pour compléter l’article, peux-tu nous indiquer quels sont les logiciels de détourage que tu proposes?<br/>
Merci</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
