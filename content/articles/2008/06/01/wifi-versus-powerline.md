---
title: "WiFi versus PowerLine"
date: "2008-06-01T15:56:21"
lastmod: "2015-04-24T23:21:15"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["performances", "plc", "reseau", "site", "wifi"]
url: "/2008/06/01/wifi-versus-powerline/"
wordpress_id: 53
comment_count: 0
---
<p>Lorsque le modem est au sous-sol et le PC dans le salon, vous avez trois options de liaison:</p>
<p>1 – tirer des câbles dans l’appartement</p>
<p>2 – brancher deux modem « PowerLine », soit transmettre les datas par le secteur</p>
<p>3 – connecter par les ondes, soit brancher un routeur WiFi</p>
<p>L’option 1 est la meilleure en terme de bande passant, mais pas très pratique à mettre en oeuvre. Ni à utiliser, si l’on a un portable susceptible d’aller dans n’importe quelle pièce. Le PowerLine fonctionne bien, même s’il est très critiqué par les radio-amateurs (voir: <a href="http://www.von-info.ch/technique/plc/PLC.htm">http://www.von-info.ch/technique/plc/PLC.htm</a> ). WiFi a la cote, et prend de plus en plus d’ampleur, les prix chutent.</p>
<p>Voyons donc en détail ce qui diffère des techniques PowerLine et WiFi. Dans les deux cas, la sécurité n’est pas un problème: il suffit d’enclencher le cryptage. Quand à la fiabilité de la transmission, les deux souffrent de faiblesses. Le PowerLine voit sa bande passante diminuer fortement avec le changement de phase et l’introduction de bloc d’alimentation à découpage dans les prises… En effet, les chargeurs de tout poil diminuent de taillent, mais en contrepartie augmentent la fréquence du découpage et, par conséquent, l’injection de fréquences peu compatibles avec des courants porteurs…</p>
<p>L’expérimentation du WiFi montre des variations de la qualité de la transmission inexpliquées, ou bien sûr simplement par l’orientation des antennes, de la présence de murs ou meubles faisant écran. La mobilité est par contre totale. Bien entendu, si vous travaillez longtemps avec le portable, il lui faut une connexion secteur. Mais ça fait un câble de moins comparé au PowerLine.</p>
<p>On remarquera que si quasi tous les portables sont doté d’un élément WiFi, aucun à ma connaissance n’est équipé de PowerLine, qui pourrait par exemple être inséré dans le bloc secteur.</p>
<p>Si les deux techniques de communication de données fonctionnent à satisfaction, laquelle est la <strong>plus rapide</strong>? Ou d’abord, comment les tester individuellement? Pour cela il suffit de pinger un device connu, puis de retirer le câble réseau ou d’éteindre le module Wifi du PC de façon à n’avoir qu’une liaison active. Le retrait du câble suffira dans mon cas, car c’est la liaison préférée. Mais est-elle la meilleure? Analysons.</p>
<p>Par le câble et PowerLine:</p>
<p>C:\&gt;ping zyxel</p>
<p>Envoi d’une requête ‘ping’ sur zyxel [192.168.1.1] avec 32 octets de données :</p>
<p>Réponse de 192.168.1.1 : octets=32 temps=3 ms TTL=254</p>
<p>Par le WiFi:</p>
<p>C:\&gt;ping zyxel</p>
<p>Envoi d’une requête ‘ping’ sur zyxel [192.168.1.1] avec 32 octets de données :</p>
<p>Réponse de 192.168.1.1 : octets=32 temps=2 ms TTL=253</p>
<p>Ce ping est celui de mon modem routeur ( entre nous, assez minable comme routeur, car le DNS ne vaut que pour 4 adresses). Pour ne pas encombrer l’affichage, j’ai supprimé les autres lignes de la commande ping; par défaut 4 essais sont lancés. On constate que la voie WiFI est meilleure (malgré le passage dans le routeur) que celle du PowerLine, pourtant plus directe au niveau IP. En effet, les modems PowerLine se comportent comme des switch (pas de routage, ni de NAT).</p>
<p>Ceci se remarque par le Time To Live qui passe à 253 par la voie WiFi.</p>
<p>La bande passante est limitée (dans mon cas, bien sûr) à environ 7 Mb/s; tandis que le WiFi affiche 48 Mb/s (avec un max à 54 Mb/s). Ceci s’observe dans le temps de réponse, plus court.</p>
<p>Conclusion (actuelle, compostable…) le WiFi peut remplacer avantageusement le PowerLine.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
