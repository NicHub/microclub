---
title: "Découvrir le Raspberry Pi"
date: "2013-05-11T09:33:19"
lastmod: "2016-04-10T17:11:02"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["bittorrent", "consoles", "embarque", "hardware", "initiation", "processeurs", "python", "web"]
url: "/2013/05/11/decouvrir-le-raspberry-pi/"
wordpress_id: 1225
comment_count: 6
---

### Introduction

Attention – section LAN modifiée

Lors du dernier festival de robotique à l’EPLF (<https://festivalrobotique.epfl.ch/> ) , comme un leitmotiv résonnait les mots « Raspberry Pi » Ainsi que plusieurs amis du MICROCLUB, nous nous décidons d’acquérir un de ces modules, qui a les caractéristiques suivantes (<http://www.raspberrypi.org/> ):

[![board](/media/2013/05/board.jpg)](/media/2013/05/board.jpg)

- Prix \$35 (avec alimentations, câbles boîtier, carte SD, ça revient à CHF 60.-)

- Taille du print: carte de crédit, 85.6 x 54 mm (avec boîtier… compter un peu plus!!)

- Alimentation 5V, via USB, mais 700 mA (3.5 W)

- CPU ARM à 700 MHz (hackable à 1 Ghz…)

- Mémoire RAM 512 Mb

- Mémoire FLASH par SD Card, minimum 2 Go (j’ai mis 8 Go)

- Graphique : 1920×1200, capable de décoder du MP4 (H264); sorties HDMI et PAL/NTSC

- Audio: jack 3.5 mm et HDMI

- LAN: 10/100 MB, RJ45

- Ports: 3 x USB2

La puissance de cette carte est comparable à celle d’un petit portable. Les systèmes d’exploitation possibles sont aussi nombreux; mais les « tunés » sont un Debian (Raspbian), un Arch Debian et un RISC OS. J’ai choisi le Raspbian.

### Lancement

Après avoir téléchargé l’image et initialisé la carte SD par l’excellent tool, le module est connecté sur la TV via le câble HDMI du lecteur DVD. Le chargeur de mobile USB sera l’alimentation; il est plus musclé qu’un port de PC. Sur le site de Raspberry, on y retrouve cette recommandation à de multiples reprises. La plupart des modules prétendus défectueux n’ont pas été alimentés correctement; ou les périphériques ont mis à genoux l’alimentation qui, d’un port de PC, est limitée à 500 mA. J’y adjoint clavier et souris USB. A l’écran de config (qui apparait en mode texte), je choisis d’enclencher le SSH, d’étendre l’espace mémoire « root » sur le restant de la carte SD ainsi que de démarrer le graphique par « startx ». L’utilisateur par défaut et « pi »; on lui donne un mot de passe. Pas trop compliqué, vu que le clavier est resté en « QWERTY ». Okay…

L’interface passe en graphique haute résolution, affiche une belle framboise. La souris est reconnue.

### Configurer Raspberry

Tout cela est bien joli; mais je ne peux pas continûment squatter la TV – qui ne me sert d’écran que pour passer des DVD – et laisser trainer ces câbles ainsi. Il me faut une connexion réseau, que je n’ai bien sûr pas dans cette pièce; et une prise à distance du module pour éviter de devoir utiliser un écran. Même si un câble HDMI – DVI est à disposition pour 20.- chez Distrelec, n° 847355. Pris d’une inspiration en voyant l’icône « Wifi config », je tente de connecter sur l’USB libre une antenne Wifi de marque Netopia, venue avec l’ancien modem/routeur de Swisscom. Bingo! Elle est reconnue. Suit l’introduction de la clef WPA, et la liaison est établie. Via le terminal, il est possible de lire l’adresse IP prise en DHCP.

Pour être sûr que la connexion soit fiable, je retire l’antenne de l’USB, puis je la reconnecte. La liaison se rétablit sans autre. Parfait.

Comment configurer le module ? Après quelques recherches sur l’Internet, un site en français répond à plein de questions, avec des exemples pratiques :

<http://www.tropfacile.net/doku.php/raspberry-pi/>

Dès que le Raspberry est sur le réseau, je peux l’atteindre avec deux outils indispensables via mes PCs Windows:

- Putty, un terminal SSH

- WinSCP, un explorateur 2 panneaux à la TotalCommander

### Ecran à distance par VNC

Or donc, si je veux éviter de poser un second écran et sa panoplie de câbles sur mon bureau, il me faut atteindre Raspberry via le LAN par mes portables. C’est bien sûr déjà fait en ce qui concerne la console, par Putty via une connexion SSH, ainsi que pour manipuler les fichiers par WinSCP. Ajouter VNC? La manip est décrite ici:

<http://reviews.cnet.co.uk/desktops/how-to-make-a-raspberry-pi-solar-powered-ftp-server-50009923/>

En fait, je n’ai pas l’intention de le transformer en serveur FTP solaire, quoique… pour afficher automatiquement des images de mon nid en WiFi, l’idée est à creuser. L’auteur précide justement comment installer un serveur TightVNC. Depuis la console (en root, pas besoin du préfixe « sudo »)

sudo apt-get update\
sudo apt-get install vnc-server\
vncserver

Et là, on indique le password de connexion VNC désiré. Ça devrait déjà fonctionner.

Cependant, si on veut un automatisme au démarrage, il faut ajouter le script suivant dans /etc/init.d :

\#!/bin/sh\

# /etc/init.d/tightvncserver\

# Positionne la variable VNCUSER pour démarrer tightvncserver avec\

VNCUSER=’pi’\
case « \$1 » in\
start)\
su \$VNCUSER -c ‘/usr/bin/tightvncserver :1’\
echo « Démarre TightVNC server pour \$VNCUSER  »\
;;\
stop)\
pkill Xtightvnc\
echo « Tightvncserver stoppé »\
;;\
\*)\
echo « Usage: /etc/init.d/tightvncserver {start\|stop} »\
exit 1\
;;\
esac\
exit 0

Afin qu’il soit éxécutable, il faut encore lui changer ses bits ‘x’, soit par WinSCP, soit via la console, par:

sudo chmod 755 /etc/init.d/tightvncserver

Ce n’est pas tout. Si on lance ce script, on peut en effet démarrer et arrêter le service VNC. Afin qu’il soit lancé au démarrage, il faut l’inscrire dans les services à démarrer, par la commande:

update-rc.d tightvncserver defaults

Il reste a vérifier le résultat. La commande de VNC reader, depuis un PC Windows, est un peu originale.

[![VNC_param](/media/2013/05/VNC_param.jpg)](/media/2013/05/VNC_param.jpg)

Normalement, on y indique l’IP du poste sur lequel on veut se connecter (ou son nom NetBios s’il est propagé). Ici, il faut aussi préciser l’écran, par le le ‘:1’ après l’adresse:

Si tout se passe bien, on accède à Raspberry. Sinon, vérifier que le service démarre, par la commande « top ».

[![VNC_view](/media/2013/05/VNC_view-1024x804.jpg)](/media/2013/05/VNC_view.jpg)

### Adresse LAN fixe (static in english)

Comme je souhaite que le module soit connecté via le câble -ET- qu’il conserve une adresse fixe, car même si le DHCP de mon modem DSL garde la même adresse pour un périphérique donnée, pas sûr que ce soit reproductible sur le long terme. Il distribue les adresses au dessus de 192.168.1. 32. J’ai fixé les adresses de mes imprimantes et du NAS en dessous. L’adresse réservée pour Raspberry, sera la 192.168.1.11.

\<del\>auto lo\</del\>

\<del\>iface lo inet loopback\</del\>

\<del\>iface eth0 inet static\</del\>

\<del\> address 192.168.1.11\</del\>

\<del\> netmask 255.255.255.0\</del\>

\<del\> gateway 192.168.1.1\</del\>

\<del\> network 192.168.1.0\</del\>

\<del\> broadcast 192.168.1.255\</del\>

\<del\>allow-hotplug wlan0\</del\>

\<del\>iface wlan0 inet manual\</del\>

\<del\>wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf\</del\>

\<del\>iface default inet dhcp\</del\>

\<del\>La solution est d’éditer le fichier /etc/network/interfaces\</del\>, ce que je fais grâce à WinSCP. Le fichier est complété comme suit, pour l’interface eth0, soit le câble (le Wifi, wlan0, reste en dynamique).

Depuis mai 2015, le Raspian utilise une nouvelle méthode – tous les tuto qui modifient le fichier /etc/network/interface sont obsolètes.**La nouvelle config est basée sur dhcpcd.**

Il faut travailler sur /etc/dhcpcd.conf:

```
<code>interface eth0
static ip_address=192.168.1.XX/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1</code>
```

Puis je passe au retrait du WiFI, connecte le Raspberry avec un câble réseau au modem/routeur, redémarre le module… Quelques ping et reconfiguration des outils plus tard, c’est tout bon. J’en profite pour retirer le bloc alimentation du mobile; le câble est branché au NAS, qui possède des USB avec alimentation musclée de 1.3 Ampères.

La config est prête, il s’agit de trouver une application. Pour ce faire, le site de Korben propose pas moins de 50 liens sur des solutions à base de Raspberry: <http://korben.info/idees-raspberry-pi.html>

Yves Masur (5/2013) (Modif LAN static 4/2016)

## Commentaires

### franic — 13 mai 2013 à 05:23

Je n’ai pas trouvé l’icone Wifi config !\
Je ne crois pas avoir loupé un pas, mais le service vnc n’est pas chargé lors du démarrage.\
Sinon pour charger le clavier suisse romand, j’ai fais ceci :\
– dans sudo raspi-config, j’ai sélectionné « change keyboard »\
– j’ai choisi standard 101 touches\
– clavier « German swiss »\
– puis « french swiss »

### ↳ Réponse — Yves Masur — 14 mai 2013 à 19:59

Effectivement, par raspi-config, on peut retoucher la config donnée au départ! Par contre, essayer d’installer le clavier par ssh ou même par VNC ne fonctionne pas, il faut aller directement sur le module.

Concernant le non démarrage de ton VNC, vérifie si le script fonctionne: « /etc/init.d/tightvncserver start » (ou stop) puis s’il est inscrit dans les modules de init.d, soit par la commande « update-rc.d tightvncserver defaults ».

### Alain Tornare — 17 juin 2013 à 20:42

Mon sript est bien inscrit dans les modiules de init.d, puisque il essaie de se lancer au boot, mais j’ai l’erreur de syntax retournée: 6:word unexpected (expecting « ) »). et la même chose si je le lance manuellement avec cette commande « /etc/init.d/tightvncserver start » ( ou stop ), mais pas si je le lance simplement avec «tightvncserver » et de plus dans ce cas le serveur VNC fonctionne !\
La ligne 6 c’est  » start) « . et il y a bien une parenthèse ! mais j’ai des espaces devant ?\
Merci d’éclairer ma lanterne. Alain

### Zurlinden MF — 12 décembre 2015 à 20:55

Bonjour 🙂

Où trouver tout le matériel en Suisse bon rapport qualité/Prix ?\
Merci 🙂

### ↳ Réponse — Tornare Alain — 12 décembre 2015 à 21:35

Le fournisseur est ici: <http://ch.farnell.com/fr-CH/acheter-raspberry-pi>

Mais depuis le temps, la version actuelle du Hardware est le Pi 2, avec un Quad Core et la version du Raspbian en est à 4.1, avec un changement radical de philosophie qui rend obsolète bien des forums du Net, car ils se rapportent à la première précédente B ou B+ sous système antérieur au 3.15 !!! Prend garde à la date des articles !\
Alain

### ↳ Réponse — Yves Masur — 12 décembre 2015 à 21:40

La qualité est la même; par contre les prix changent. Il y a un nouveau modèle, « B+ ». Certains fournisseurs proposent des packs de démarrage avec l’alimentation, une carte SD configurée.\
Passer par exemple par toppreise.ch pour trouver une bonne offre.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
