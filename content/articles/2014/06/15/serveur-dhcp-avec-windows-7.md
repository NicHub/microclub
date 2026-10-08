---
title: "Serveur DHCP avec Windows 7"
date: "2014-06-15T21:05:41"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "barrette", "dhcp", "initiation", "linux", "systeme-dexploitation", "windows"]
url: "/2014/06/15/serveur-dhcp-avec-windows-7/"
wordpress_id: 1490
comment_count: 0
---
<h2>Pourquoi un DHCP ?</h2>
<p>Avec le développement sur l’Arduino Yun, me voici quelque peu ennuyé ; tout ne fonctionne pas comme dans le tuto. Les détails de cette expérience feront l’objet d’un article distinct ! Dans l’immédiat, j’ai besoin de le mettre sur le réseau câblé, avec une adresse connue.<a href="/media/2014/06/9-yun.jpg"><img alt="9-yun" height="183" src="/media/2014/06/9-yun.jpg" width="275"/></a></p>
<p>Pour cela j’ai besoin d’un programme DHCP. Qu’est-ce que le DHCP ? Selon Wikipédia : <b><i>Dynamic Host Configuration Protocol</i></b> (DHCP) est un <a href="http://fr.wikipedia.org/wiki/Protocole_r%C3%A9seau" target="_blank" title="Protocole réseau">protocole réseau</a> dont le rôle est d’assurer la configuration automatique des paramètres IP d’une station, notamment en lui affectant automatiquement une adresse IP et un <a href="http://fr.wikipedia.org/wiki/Masque_de_sous-r%C3%A9seau" target="_blank" title="Masque de sous-réseau">masque de sous-réseau</a>. DHCP peut aussi configurer l’adresse de la passerelle par défaut, des serveurs de noms <a href="http://fr.wikipedia.org/wiki/Domain_Name_System" target="_blank" title="Domain Name System">DNS</a> et des serveurs de noms <a href="http://fr.wikipedia.org/wiki/Netbios#NetBIOS_Name_Service_.28port_UDP_137.29" title="Netbios">NBNS</a> (connus sous le nom de serveurs <a href="http://fr.wikipedia.org/wiki/Windows_Internet_Naming_Service" title="Windows Internet Naming Service">WINS</a> sur les réseaux de la société Microsoft).</p>
<p>À ne pas confondre avec le DNS (<a href="http://fr.wikipedia.org/wiki/DNS">http://fr.wikipedia.org/wiki/DNS</a> ) le Domain Name System – qui s’occupe de faire la relation entre un nom (en fait une URL) et une adresse IP. Le DHCP attribue une adresse IP à un système, parmi une plage d’adresses, avec une durée limitée.</p>
<h2>La configuration initiale</h2>
<p>Voici ma config, qui est assez classique et probablement proche de la vôtre, hormis peut-être la <a href="/2011/08/13/projet-barrette-realise/" title="Projet barrette: réalisé!">barrette électrique</a>:</p>
<p>–        Modem routeur Wi-FI NAT, adresse fixe 192.168.1.1<br/>
–        Un petit PC 14’ N145-YM, Wi-FI DHCP et une connexion LAN libre<br/>
–        Le module Arduino Yun, Wi-FI DHCP et une connexion LAN libre<br/>
–        Portable lourd, PC 17’ Vostro, Wi-FI DHCP<br/>
–        Sa connexion LAN, fixe : 10.1.0.7<br/>
–        La Barrette CBM, sur LAN, en DHCP, mais par défaut en 10.1.0.1</p>
<p>Ces 2 dernières sont câblées en direct ; la barrette peut donc accepter une adresse DHCP si elle est fournie. De plus, elle propage son nom « CBM11 » par NetBIOS. Le modem routeur Wi-Fi permet à la maisonnée d’aller sur l’Internet ; d’autres clients y sont connectés : PCs, PCs portables, imprimantes, NAS, seconde barrette et même mon portable Android… Bref il y a du monde.</p>
<h2>Pourquoi une adresse fixe ?</h2>
<p>L’attribution d’une adresse IP fixe est nécessaire pour les serveurs (on doit savoir où les trouver), sur des petits systèmes simples de disposant pas de mécanisme DHCP, ou qui ne propagent pas leur nom sur le réseau. Ou pas comme on l’aimerait. L’adresse fixe est aussi plus sûre dans certaines configurations techniques, sa présence sur le LAN lors du boot est forcément plus rapide. C’est notamment le cas des switchs managés et des routeurs : on imagine l’horreur en cas de coupure de courant si ces éléments clef commencent à se demander parmi une adresse…</p>
<p>Dans ma config, sont en adresse fixe : le modem routeur, les imprimantes, les NAS.</p>
<h2>Pourquoi pas aussi une adresse pseudo-fixe ?</h2>
<p>Si l’adresse fixe se révèle un besoin, c’est parfois pénible à mettre en œuvre et tout aussi difficile à modifier par la suite. Une possibilité intéressante est de programmer le serveur DHCP afin qu’il délivre toujours la même adresse à un système client. Ainsi, d’un coup d’œil sur la liste, on peut voir les réservations et les modifier facilement au besoin. Connexion/déconnexion, le tour est joué : le système client prend cette adresse. Les modem-routeurs récent le font d’office. Plutôt que d’attribuer le pool d’adresse dans l’ordre des démarrages des machines, selon leur MAC-adresse, il attribuera celle enregistrée auparavant ; mais ce n’est pas suffisant. Rien ne nous garantit que l’adresse soit conservée ad aeternam. Il faut pouvoir l’enregistrer dans une liste.</p>
<p>Ne cherchez pas ce terme de « pseudo-fixe » sur le Net ; je l’ai défini pour l’usage de nos machines dans le cadre d’appels d’offres pour mon travail. Un ennui peut toutefois découler de cette méthode : une machine tombe en panne de communication, et sa carte réseau est changée. Elle est donc réparée et retrouve le réseau, mais elle ne fonctionne toujours pas ! Son adresse MAC a changé. Et donc son adresse IP aussi !</p>
<h2>Serveur DHCP</h2>
<p>Une recherche montre que W7 peut servir de serveur DHCP si une carte réseau est configurée pour le partage Internet (par ICS), ici : <a href="http://answers.microsoft.com/en-us/windows/forum/windows_7-networking/make-windows-7-act-as-a-dhcp-server/8ff345f2-99b5-4670-bb6f-32d7bb63de3c">http://answers.microsoft.com/en-us/windows/forum/windows_7-networking/make-windows-7-act-as-a-dhcp-server/8ff345f2-99b5-4670-bb6f-32d7bb63de3c</a></p>
<p>Il y a toutefois des limitations : l’adresse fixe est imposée, et les écrans abscons proposent de qualifier le sous réseau public, bureau ou privé. Cela a une incidence sur le mode dit de « découverte du réseau. »</p>
<p>A contrario, le programme gratuit DHCPServer (<a href="http://sourceforge.net/projects/dhcpserver/">http://sourceforge.net/projects/dhcpserver/</a> ) permet de construire exactement ce que l’on veut. La version utilisée ci-après est la 1.61, elle occupe 1,3 Mo dans c:\OpenDHCPServer, soit la racine du disque dur. Le programme se démarre soit à la main, soit en service Windows.</p>
<p>Avant de le démarrer, il faut préparer la configuration, mais c’est assez simple (même pour les utilisateurs n’ayant pas des connaissances étendues en DHCP) via le fichier texte « OpenDHCPServer.ini ». Il faut également fixer l’adresse IP d’une carte du PC serveur – ce qui, dans mon cas, est déjà fait – par le Panneau de configuration -&gt; Réseau et Internet -&gt; Connexion réseau : choisir la carte réseau. Puis : Propriété – Gestion de réseau. Cliquer ensuite la ligne cochée Protocole Internet version 4(TCP/IPv4) et le bouton [Propriétés].</p>
<p>Les infos de passerelle et du DNS ne sont pas utiles pour notre utilisation.</p>
<p>Ensuite, on va définir une plage d’adresses à attribuer par le DHCP:</p>
<h2><a href="/media/2014/06/2-DHCP_range.jpg"><img alt="2-DHCP_range" height="49" src="/media/2014/06/2-DHCP_range.jpg" width="272"/></a></h2>
<h2>Nouvelle configuration</h2>
<p>Il y a 4 machines qui seront dans ce sous-réseau. Il nécessite un petit routeur à 4 ports, de ce genre :<a href="/media/2014/06/4-switch.jpg"><img alt="4-switch" height="116" src="/media/2014/06/4-switch.jpg" width="180"/></a></p>
<p>–        Le PC Vostro, qui sera le serveur en 10.1.0.7, hors de la plage dynamique<br/>
–        Le PC N145-YM, dont on va pseudo-fixer l’adresse en 10.1.0.145<br/>
–        La Barrette, dont on va fixer l’adresse en 10.1.0.1, pour la maintenir tel quelle<br/>
–        Et l’Arduino Yun, qu’on va placer en 10.1.0.11</p>
<p>Seule cette dernière est importante ; le PC N145 pour le retrouver plus facilement, vu que sa RAM est si faible que j’ai désactivé un maximum de services dont les gadgets de découverte de réseau, par exemple. Pour la Barrette, c’est juste pour la maintenir ou elle était.</p>
<p>Voici les paramètres, selon les adresses MAC :</p>
<p><a href="/media/2014/06/3-DHCP_pseudo-fixe.jpg"><img alt="3-DHCP_pseudo-fixe" height="154" src="/media/2014/06/3-DHCP_pseudo-fixe.jpg" width="122"/></a></p>
<p>Un coup d’œil dans les logs montre que tout est OK :</p>
<pre>[15-Jun-14 20:43:49] Network changed, re-detecting Static Interfaces..
[15-Jun-14 20:43:49] Lease Status URL: http://127.0.0.1:6789
[15-Jun-14 20:43:49] Listening On: 192.168.178.1
[15-Jun-14 20:43:49] Listening On: 192.168.56.1
[15-Jun-14 20:43:49] Listening On: 10.1.0.7
[15-Jun-14 20:43:49] Listening On: 192.168.216.1
[15-Jun-14 21:35:42] Host e8:11:32:7d:92:e0 (N145-YM) allotted 10.1.0.145 for 36000 seconds
[15-Jun-14 21:38:58] Host 90:a2:da:fc:0a:c0 (Host90a2dafc0ac0) allotted 10.1.0.110 for 36000 seconds
[15-Jun-14 21:41:33] Host 00:04:a3:00:00:00 (Host0004a3000000) allotted 10.1.0.1 for 36000 seconds</pre>
<p>Comme j’ai des cartes virtuelles, dues à une config prévue pour de la virtualisation, elles sont aussi servies. Ceci laisse entrevoir les possibilités à d’intéressantes expériences en mode virtuel.</p>
<p>La page WEB du DHCP Server montre tout ça de manière synthétique.</p>
<p><a href="/media/2014/06/9-DHCP_page.jpg"><img alt="9-DHCP_page" height="415" src="/media/2014/06/9-DHCP_page.jpg" width="511"/></a></p>
<p>On remarque que toutes les adresse statiques (pseudo-fixes) sont prises; et que seul le nom du PC N145-YM est inscrit, les autres sont indiquées sous Host, suivi de l’adresse MAC. Pour savoir qui est qui, il suffit de déconnecter/reconnecter le LAN et d’observer l’écran (ou le log).</p>
<h2>Configuration Arduino Yun en IP pseudo-fixe</h2>
<p>Donc maintenant, le module Arduino est connecté aux 2 PCs par câble. On peut consulter sa page WEB, lancer une console Linux avec Putty, le programmer en connaissant de manière sûre son adresse IP. La dépendance et l’incertitude dues à un Wi-Fi instable sont éliminées. On peut avancer.</p>
<p>Yves Masur (6/2014)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
