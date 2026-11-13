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

## Pourquoi un DHCP ?

Avec le développement sur l’Arduino Yun, me voici quelque peu ennuyé ; tout ne fonctionne pas comme dans le tuto. Les détails de cette expérience feront l’objet d’un article distinct ! Dans l’immédiat, j’ai besoin de le mettre sur le réseau câblé, avec une adresse connue.[![9-yun](/media/2014/06/9-yun.jpg)](/media/2014/06/9-yun.jpg)

Pour cela j’ai besoin d’un programme DHCP. Qu’est-ce que le DHCP ? Selon Wikipédia : ***Dynamic Host Configuration Protocol*** (DHCP) est un [protocole réseau](http://fr.wikipedia.org/wiki/Protocole_r%C3%A9seau "Protocole réseau") dont le rôle est d’assurer la configuration automatique des paramètres IP d’une station, notamment en lui affectant automatiquement une adresse IP et un [masque de sous-réseau](http://fr.wikipedia.org/wiki/Masque_de_sous-r%C3%A9seau "Masque de sous-réseau"). DHCP peut aussi configurer l’adresse de la passerelle par défaut, des serveurs de noms [DNS](http://fr.wikipedia.org/wiki/Domain_Name_System "Domain Name System") et des serveurs de noms [NBNS](http://fr.wikipedia.org/wiki/Netbios#NetBIOS_Name_Service_.28port_UDP_137.29 "Netbios") (connus sous le nom de serveurs [WINS](http://fr.wikipedia.org/wiki/Windows_Internet_Naming_Service "Windows Internet Naming Service") sur les réseaux de la société Microsoft).

À ne pas confondre avec le DNS (<http://fr.wikipedia.org/wiki/DNS> ) le Domain Name System – qui s’occupe de faire la relation entre un nom (en fait une URL) et une adresse IP. Le DHCP attribue une adresse IP à un système, parmi une plage d’adresses, avec une durée limitée.

## La configuration initiale

Voici ma config, qui est assez classique et probablement proche de la vôtre, hormis peut-être la [barrette électrique](/2011/08/13/projet-barrette-realise/ "Projet barrette: réalisé!"):

–        Modem routeur Wi-FI NAT, adresse fixe 192.168.1.1\
–        Un petit PC 14’ N145-YM, Wi-FI DHCP et une connexion LAN libre\
–        Le module Arduino Yun, Wi-FI DHCP et une connexion LAN libre\
–        Portable lourd, PC 17’ Vostro, Wi-FI DHCP\
–        Sa connexion LAN, fixe : 10.1.0.7\
–        La Barrette CBM, sur LAN, en DHCP, mais par défaut en 10.1.0.1

Ces 2 dernières sont câblées en direct ; la barrette peut donc accepter une adresse DHCP si elle est fournie. De plus, elle propage son nom « CBM11 » par NetBIOS. Le modem routeur Wi-Fi permet à la maisonnée d’aller sur l’Internet ; d’autres clients y sont connectés : PCs, PCs portables, imprimantes, NAS, seconde barrette et même mon portable Android… Bref il y a du monde.

## Pourquoi une adresse fixe ?

L’attribution d’une adresse IP fixe est nécessaire pour les serveurs (on doit savoir où les trouver), sur des petits systèmes simples de disposant pas de mécanisme DHCP, ou qui ne propagent pas leur nom sur le réseau. Ou pas comme on l’aimerait. L’adresse fixe est aussi plus sûre dans certaines configurations techniques, sa présence sur le LAN lors du boot est forcément plus rapide. C’est notamment le cas des switchs managés et des routeurs : on imagine l’horreur en cas de coupure de courant si ces éléments clef commencent à se demander parmi une adresse…

Dans ma config, sont en adresse fixe : le modem routeur, les imprimantes, les NAS.

## Pourquoi pas aussi une adresse pseudo-fixe ?

Si l’adresse fixe se révèle un besoin, c’est parfois pénible à mettre en œuvre et tout aussi difficile à modifier par la suite. Une possibilité intéressante est de programmer le serveur DHCP afin qu’il délivre toujours la même adresse à un système client. Ainsi, d’un coup d’œil sur la liste, on peut voir les réservations et les modifier facilement au besoin. Connexion/déconnexion, le tour est joué : le système client prend cette adresse. Les modem-routeurs récent le font d’office. Plutôt que d’attribuer le pool d’adresse dans l’ordre des démarrages des machines, selon leur MAC-adresse, il attribuera celle enregistrée auparavant ; mais ce n’est pas suffisant. Rien ne nous garantit que l’adresse soit conservée ad aeternam. Il faut pouvoir l’enregistrer dans une liste.

Ne cherchez pas ce terme de « pseudo-fixe » sur le Net ; je l’ai défini pour l’usage de nos machines dans le cadre d’appels d’offres pour mon travail. Un ennui peut toutefois découler de cette méthode : une machine tombe en panne de communication, et sa carte réseau est changée. Elle est donc réparée et retrouve le réseau, mais elle ne fonctionne toujours pas ! Son adresse MAC a changé. Et donc son adresse IP aussi !

## Serveur DHCP

Une recherche montre que W7 peut servir de serveur DHCP si une carte réseau est configurée pour le partage Internet (par ICS), ici : <http://answers.microsoft.com/en-us/windows/forum/windows_7-networking/make-windows-7-act-as-a-dhcp-server/8ff345f2-99b5-4670-bb6f-32d7bb63de3c>

Il y a toutefois des limitations : l’adresse fixe est imposée, et les écrans abscons proposent de qualifier le sous réseau public, bureau ou privé. Cela a une incidence sur le mode dit de « découverte du réseau. »

A contrario, le programme gratuit DHCPServer (<http://sourceforge.net/projects/dhcpserver/> ) permet de construire exactement ce que l’on veut. La version utilisée ci-après est la 1.61, elle occupe 1,3 Mo dans c:\OpenDHCPServer, soit la racine du disque dur. Le programme se démarre soit à la main, soit en service Windows.

Avant de le démarrer, il faut préparer la configuration, mais c’est assez simple (même pour les utilisateurs n’ayant pas des connaissances étendues en DHCP) via le fichier texte « OpenDHCPServer.ini ». Il faut également fixer l’adresse IP d’une carte du PC serveur – ce qui, dans mon cas, est déjà fait – par le Panneau de configuration -\> Réseau et Internet -\> Connexion réseau : choisir la carte réseau. Puis : Propriété – Gestion de réseau. Cliquer ensuite la ligne cochée Protocole Internet version 4(TCP/IPv4) et le bouton \[Propriétés\].

Les infos de passerelle et du DNS ne sont pas utiles pour notre utilisation.

Ensuite, on va définir une plage d’adresses à attribuer par le DHCP:

## [![2-DHCP_range](/media/2014/06/2-DHCP_range.jpg)](/media/2014/06/2-DHCP_range.jpg)

## Nouvelle configuration

Il y a 4 machines qui seront dans ce sous-réseau. Il nécessite un petit routeur à 4 ports, de ce genre :[![4-switch](/media/2014/06/4-switch.jpg)](/media/2014/06/4-switch.jpg)

–        Le PC Vostro, qui sera le serveur en 10.1.0.7, hors de la plage dynamique\
–        Le PC N145-YM, dont on va pseudo-fixer l’adresse en 10.1.0.145\
–        La Barrette, dont on va fixer l’adresse en 10.1.0.1, pour la maintenir tel quelle\
–        Et l’Arduino Yun, qu’on va placer en 10.1.0.11

Seule cette dernière est importante ; le PC N145 pour le retrouver plus facilement, vu que sa RAM est si faible que j’ai désactivé un maximum de services dont les gadgets de découverte de réseau, par exemple. Pour la Barrette, c’est juste pour la maintenir ou elle était.

Voici les paramètres, selon les adresses MAC :

[![3-DHCP_pseudo-fixe](/media/2014/06/3-DHCP_pseudo-fixe.jpg)](/media/2014/06/3-DHCP_pseudo-fixe.jpg)

Un coup d’œil dans les logs montre que tout est OK :

```
[15-Jun-14 20:43:49] Network changed, re-detecting Static Interfaces..
[15-Jun-14 20:43:49] Lease Status URL: http://127.0.0.1:6789
[15-Jun-14 20:43:49] Listening On: 192.168.178.1
[15-Jun-14 20:43:49] Listening On: 192.168.56.1
[15-Jun-14 20:43:49] Listening On: 10.1.0.7
[15-Jun-14 20:43:49] Listening On: 192.168.216.1
[15-Jun-14 21:35:42] Host e8:11:32:7d:92:e0 (N145-YM) allotted 10.1.0.145 for 36000 seconds
[15-Jun-14 21:38:58] Host 90:a2:da:fc:0a:c0 (Host90a2dafc0ac0) allotted 10.1.0.110 for 36000 seconds
[15-Jun-14 21:41:33] Host 00:04:a3:00:00:00 (Host0004a3000000) allotted 10.1.0.1 for 36000 seconds
```

Comme j’ai des cartes virtuelles, dues à une config prévue pour de la virtualisation, elles sont aussi servies. Ceci laisse entrevoir les possibilités à d’intéressantes expériences en mode virtuel.

La page WEB du DHCP Server montre tout ça de manière synthétique.

[![9-DHCP_page](/media/2014/06/9-DHCP_page.jpg)](/media/2014/06/9-DHCP_page.jpg)

On remarque que toutes les adresse statiques (pseudo-fixes) sont prises; et que seul le nom du PC N145-YM est inscrit, les autres sont indiquées sous Host, suivi de l’adresse MAC. Pour savoir qui est qui, il suffit de déconnecter/reconnecter le LAN et d’observer l’écran (ou le log).

## Configuration Arduino Yun en IP pseudo-fixe

Donc maintenant, le module Arduino est connecté aux 2 PCs par câble. On peut consulter sa page WEB, lancer une console Linux avec Putty, le programmer en connaissant de manière sûre son adresse IP. La dépendance et l’incertitude dues à un Wi-Fi instable sont éliminées. On peut avancer.

Yves Masur (6/2014)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
