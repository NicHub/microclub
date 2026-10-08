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
<p>En juin 2010, des sociétés de sécurité informatique comme Symantec ont détecté un <a href="https://secure.wikimedia.org/wikipedia/fr/wiki/Ver_informatique" target="_blank">ver informatique</a> assez étrange : il était très complexe, sophistiqué et extrêmement discret puisqu’il ne fait apparemment rien du tout sur les ordinateurs infectés. Il a fallu environ 3 mois de travail intensif pour comprendre ce qu’il fait réellement, et encore 3 mois pour en être vraiment sur tellement c’était étonnant. En plus on a réalisé que Stuxnet circulait depuis environ un an sans avoir été détecté…</p>
<p>Sur chaque ordinateur infecté, <a href="http://fr.wikipedia.org/wiki/Stuxnet" target="_blank">Stuxnet</a>, c’est son nom,  cherche  le logiciel <a href="http://www.automation.siemens.com/mcms/simatic-controller-software/en/step7/Pages/Default.aspx" target="_blank">Simatic Step7 de Siemen</a>s qui sert à programmer les <a href="http://fr.wikipedia.org/wiki/Automate_programmable_industriel" target="_blank">automates programmables (PLC en anglais) </a> Siemens, probablement les plus utilisés dans le monde pour la commande d’installations industrielles comme des usines électriques, des raffineries de pétrole ou les  feux de circulation. S’il trouve Step7, Stuxnet cherche dans le code source du PLC s’il servait à commander un grand nombre de moteurs électriques d’un certain type. Et seulement dans ce cas, Stuxnet envoie ce code source à un certain site web, en passant par des clés USB si aucune connexion à internet n’est disponible. Ensuite, Stuxnet attendait gentiment que le site web lui envoie un nouveau code source, ou plus exactement une sorte de « patch » de ce code. Et la prochaine fois que l’utilisateur de ce PC utilisait Step7 pour programmer son PLC, Stuxnet envoyait le code « patché ».</p>
<p>En résumé, le PLC ciblé soigneusement se mettait à exécuter de façon totalement invisible des fonctions envoyées par le site web à la place, ou en plus, du code normal. Tout ceci est démontré dans cette video, en anglais :</p>
<p>[youtube cf0jlzVCyOI]</p>
<p>Aujourd’hui il est quasi certain que Stuxnet est le premier virus informatique « militaire » écrit par un ou plusieurs états pour attaquer spécifiquement des installations industrielles stratégiques d’un autre état, en l’occurrence les centrifugeuses servant à l’enrichissement de l’uranium en Iran. Stuxnet a apparemment réussi à les faire tourner à la mauvaise vitesse, voire à les détruire partiellement. Certains articles affirment que le programme nucléaire iranien a pris 5 ans de retard grâce à Stuxnet !</p>
<p>Ce qu’il faut bien réaliser, c’est que Stuxnet aurait pu être dévastateur s’il n’avait pas été aussi soigneusement ciblé. D’abord Stuxnet aurait pu remonter à ses créateurs tous les programmes des PLC rencontrés, ce qui aurait constitué un cas d’espionnage industriel unique. Visiblement les auteurs ne souhaitaient pas se mettre à dos les pays industrialisés et leurs plus grosses entreprises…</p>
<p>Ensuite, si ça avait été le but des auteurs de Stuxnet, ils auraient pu le programmer pour faire tomber en panne, voire détruire les installations sur commande, et comme il s’agit en grande partie d’infrastructures importantes, Stuxnet aurait pu être une véritable arme de guerre.</p>
<p>Du point de vue informatique, Stuxnet est une merveille qui a demandé des années*hommes de travail de la part de hackers de très haut niveau, qui ont exploité au moins 4 failles de Windows inconnues à ce moment là (à croire qu’ils avaient leurs entrées chez Bill…) ainsi que des connaissances pointues sur Step7 et les PLC Siemens…</p>
<p>Mais qui peut-ce bien être ?</p>
<ol>
<li>« <a href="http://support.automation.siemens.com/WW/llisapi.dll?func=cslib.csinfo&amp;lang=en&amp;objid=43876783&amp;caller=view" target="_blank">SIMATIC WinCC / SIMATIC PCS 7: Information concerning Malware / Virus / Trojan</a><a name="A0"></a><br/>
« <a href="http://www.symantec.com/connect/blogs/exploring-stuxnet-s-plc-infection-process" target="_blank">Exploring Stuxnet’s PLC Infection Process</a>« , Symantec, 21 septembre 2010</li>
<li>« <a href="http://www.mediapart.fr/club/blog/michbret/260910/iran-la-cyber-attaque-deja-commence" target="_blank">Iran : la cyber attaque a déjà commencé</a>« , Mediapart 26 septembre 2010</li>
<li>« <a href="http://www.controlglobal.com/articles/2011/IndustrialControllers1101.html" target="_blank">How to Hijack a Controller : Why Stuxnet Isn’t Just About Siemens’ PLCs</a> » 13 janvier 2011</li>
</ol>

## Commentaires

### Yves Masur — 2 février 2011 à 21:57

<section class="comment-content comment">
<p>Les automates Step 7 sont utilisé pour nombre d’applications industrielles et également en réseau, mais <b>pas</b> pour les feux de circulation. C’est du matériel spécifique (aussi chez Siemens!).</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
