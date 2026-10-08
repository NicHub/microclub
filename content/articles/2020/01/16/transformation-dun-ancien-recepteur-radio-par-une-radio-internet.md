---
title: "Transformation d’un ancien récepteur radio par une radio internet"
date: "2020-01-16T17:28:45"
lastmod: "2020-01-16T17:53:49"
author: "franic"
categories: ["Microclub", "Nostalgique"]
tags: ["mediator", "radio-internet", "raspberry"]
url: "/2020/01/16/transformation-dun-ancien-recepteur-radio-par-une-radio-internet/"
wordpress_id: 4700
comment_count: 1
---
<p>En faisant de l’ordre dans son galetas, mon père a retrouvé quelques vieux postes radios. J’ai alors récupéré un vieux Médiator M111U/16 ; cet appareil était très poussiéreux. Une fois son couvercle arrière démonté, j’ai remarqué que plusieurs pièces étaient manquantes, quelques fils ont été coupés, … En conclusion, plus possibles de le remettre en état d’origine !</p>
<p><img height="375" src="/media/2020/01/word-image.jpeg" width="416"/></p>
<p>Vous pouvez retrouver l’historique de ce poste de radio fabriqué à la Chaux-de-Fonds en 1946 sur le site suivant : <a href="https://www.radiomuseum.org/r/mediator_bijou_111a_111u.html">https://www.radiomuseum.org/r/mediator_bijou_111a_111u.html</a></p>
<p>Toutefois, une idée me trottait dans la tête depuis longtemps, pourquoi ne pas garder le boîtier et les boutons et remplacer son contenu par une électronique moderne ? Alors j’ai décidé d’utiliser un Raspberry comme récepteur, une fois connecté à internet, j’ai accès à une panoplie de radios internet. J’ai alors préparé un Raspberry, trouvé un programme qui me permet d’écouter une radio diffusée sur internet. Il me fallait encore un interface entre les divers boutons de la radio Mediator et le Raspberry ; pas possible d’utiliser des encodeurs, car lors de la mise sous tension de la nouvelle radio, il faut savoir exactement la position de l’aiguille de la fréquence ! j’ai donc utilisé un potentiomètre pour connaître cette position, et j’ai utilisé ce même principe pour le bouton de volume. Il y a encore un sélecteur de bandes, 3 positions, ceux-ci peuvent être en on/off. J’aurais pu acheter un convertisseur A/D sur un bus SPI ou I2C pour le connecteur au Raspberry, mais comme j’ai plusieurs microcontrôleurs Atmel en stock, j’ai utilisé un atmega8 que j’ai relié par l’UART sur le Raspberry. Tout cela peut sembler facile, mais voici le détail de chaque étape.</p>
<p>Pot. volume Bouton OFF</p>
<p>Raspberry PI3</p>
<p>AtMega8 ou Arduino</p>
<p>Pot. position fréquence LEDs éclairage</p>
<h1>1 Préparation du Raspberry</h1>
<p>J’ai téléchargé la dernière version de debian pour Rasberry, la version « <em>buster raspbian with desktop »</em> sans tous les logiciels bureautiques est suffisante : <a href="https://www.raspberrypi.org/downloads/raspbian/">https://www.raspberrypi.org/downloads/raspbian/</a>.</p>
<p>Une fois mon Raspberry configuré, j’ai encore effectué les commandes suivantes :</p>
<ul>
<li>sudo apt-get update</li>
<li>sudo apt-get upgrade</li>
</ul>
<p>Puis j’ai installé un lecteur de flux audio :</p>
<ul>
<li>sudo apt-get install mpd mpc</li>
</ul>
<p>Pour le tester, j’ai ajouté le flux de radio chablais :</p>
<ul>
<li>mpc add <a href="http://radiochablais.ice.infomaniak.ch/radiochablais-high.mp3">http://radiochablais.ice.infomaniak.ch/radiochablais-high.mp3</a></li>
<li>mpc play 1</li>
</ul>
<p>La radio s’est mise en fonction, mais la sortie audio est sur le HDMI du moniteur ! et rien sur mon hautparleur relié à la sortie jack ! Pour modifier ceci, il faut aller configurer le canal de sortie audio dans raspi-config :</p>
<ul>
<li>sudo raspi-config</li>
<li>sélectionner « Advanced options »</li>
<li>sélectionner « Audio » « Force Audio output HDMI or 3.5mm jack »</li>
<li>sélectionner « 3.5mm headphone jack »</li>
<li>save</li>
<li>sudo reboot now</li>
</ul>
<p>Et après redémarrage, ma radio diffuse de la musique sur mon hautparleur. Reste à ajuster le volume ! Voici la commande :</p>
<ul>
<li>mpc volume 25</li>
</ul>
<p>La valeur en argument est la position du potentiomètre comprise entre 0 et 100.</p>
<p>Avec « mpc add url », nous pouvons ajouter plusieurs adresses de flux (ou le lien vers un fichier MP3), et les faire diffuser avec le no dans lequel on les a entrées par exemple « mpc play 4 »</p>
<h1>2 Trouver les adresses de flux de diverses radios</h1>
<p>Je voulais également diffuser certaines radios dont je ne trouvais pas l’adresse du flux !!! par exemple la RTS1 !</p>
<p>Pour résoudre ceci, j’ai utilisé un module complémentaire de Firefox : « Video download helper »</p>
<p><img height="68" src="/media/2020/01/word-image.png" width="296"/></p>
<p>Une fois ce module installé, voici la marche à suivre pour la radio lausanne fm :</p>
<ul>
<li>ouvrir le site de la radio rouge fm avec Firefox : https://www.rouge.com/ cliquer sur « écouter » en direct, la radio sera diffusé sur votre PC ! vous verrez que le module download helper est alors coloré !</li>
</ul>
<p><img height="347" src="/media/2020/01/word-image-1.png" width="846"/></p>
<ul>
<li>cliquer sur l’icone download helper</li>
</ul>
<p><img height="69" src="/media/2020/01/word-image-2.png" width="715"/></p>
<p>La fenêtre suivante apparaîtra, pour faire afficher les « … » à droite, placer simplement la souris dans cette zone !</p>
<p><img height="134" src="/media/2020/01/word-image-3.png" width="510"/></p>
<ul>
<li>dans le menu déroulant sélectionner « enregistrer l’URL »</li>
</ul>
<p><img height="443" src="/media/2020/01/word-image-4.png" width="510"/></p>
<ul>
<li>copier cette adresse dans un éditeur : <a href="http://rougefm.ice.infomaniak.ch/rougefm-high.mp3">http://rougefm.ice.infomaniak.ch/rougefm-high.mp3</a>.</li>
</ul>
<p>Vous pouvez copier cette adresse dans un nouvel onglet de votre navigateur et vous pourrez écouter le flux !</p>
<p>Cette méthode fonctionne bien pour plusieurs radios, mais pas pour la RTS !!! en effet la RTS ne diffuse pas un flux en continu, mais une série de mp3 ! En fouillant sur le Web, j’ai trouvé un site internet qui donne des raccourcis vers les radios suisses : <a href="https://swissradioplayer.ch/sender-az/#r">https://swissradioplayer.ch/sender-az/#r</a>. Depuis ce site, j’ai remarqué que la RTS est diffusée via une url fixe ! la méthode ci-dessus est donc applicable également pour la RTS ! http://stream.srg-ssr.ch/m/la-1ere/mp3_128</p>
<h1>3 Acquisition des positions des potentiomètres</h1>
<p>D’origine, un bouton fixé à un axe entraîne une roue qui est reliée elle-même par un axe à un condensateur variable à air et sur sa périphérie enroule et déroule un câble sur lequel est fixé l’aiguille de la fréquence.</p>
<p><img height="519" src="/media/2020/01/word-image-5.png" width="510"/></p>
<p>J’ai donc remplacé le condensateur par un nouvel axe qui fait également office de support ; j’ai imprimé en 3d une poulie que j’ai fixée sur ce même axe. J’ai fixé à côté un potentiomètre avec une autre poulie imprimée en 3d. La raison de ne pas avoir fixé l’axe directement sur le potentiomètre est que la poulie ne fait qu’un demi-tour tandis que la plage complète du potentiomètre est de 280 degrés ! le rapport entre les diamètres des poulies est de 1,5 ce qui me permet d’utiliser la plage complète du convertisseur A/D !</p>
<p><img height="837" src="/media/2020/01/word-image-6.png" width="631"/></p>
<p>Comme le contrôle du volume se fait également par une commande numérique, j’ai prévu un second canal du convertisseur A/D pour sa lecture.</p>
<p>Le sélecteur de bande est en réserve pour le moment, mais je pourrais ainsi multiplier par 3 le nombres de radios sur la plage complète.</p>
<p>Sur une plage complète, j’ai programmé 16 canaux possibles.</p>
<p>Utilisant régulièrement l’atmel atmega8, je l’ai utilisé pour faire l’interface entre le hardware de la radio et le Raspberry ; j’aurais aussi pu utiliser un circuit Arduino. L’UART configurée à 9600 bps permettra la communication entre ces 2 modules. Le protocole sera très simple :</p>
<table>
<tbody>
<tr>
<td>Entête 1</td>
<td>Entête 2</td>
<td>Volume</td>
<td>Station</td>
<td>Checksum</td>
</tr>
<tr>
<td>‘R’</td>
<td>‘M’</td>
<td>X</td>
<td>Y</td>
<td>X xor Y</td>
</tr>
</tbody>
</table>
<p><a href="/media/2020/01/Mediator1_SCH.pdf">Schéma :</a> <a href="/media/2020/01/Mediator1_SCH.pdf">Mediator1_SCH</a></p>
<h1>4 Programmation du Raspberry</h1>
<p>Pour automatiser la sélection de la station à écouter et contrôler le volume de sortie, j’ai fait un programme en python.</p>
<p>Le fonctionnement est le suivant :</p>
<ul>
<li>décodage de la trame sérielle reçue de la platine atmel</li>
<li>affectation au player des nouveaux paramètres s’ils sont changés</li>
</ul>
<h1>5 Démarrage automatique de l’application radio</h1>
<p>Pour que le fichier python se lance automatiquement au démarrage, il faut donner les droits nécessaires au fichiers python :</p>
<ul>
<li>sudo chmod o</li>
<li>sudo nano /etc/rc-local</li>
<li>ajouter la ligne : sudo python pgm.py (pgm.py est le nom du programme)</li>
</ul>
<p>Et après cela ma radio ne démarre plus … pourquoi ? Simplement, une erreur est générée si le wifi n’est pas encore présent ! Il faut donc trouver une parade ! la première est de démarrer le soft après une certain délai, simple et mais très pro ! J’ai trouvé un code qui attend que le wifi soit disponible avant de lancer la radio, mais cela ne fonctionne pas toujours ! Il faut que j’améliore encore ceci.</p>
<h1>Conclusions</h1>
<p>Il faut que j’améliore encore la transmission entre les deux poulies, car j’ai du glissement, Je vais donc remplacer le système poulies/courroie par 2 pignons dentés. Il faut également que j’ajoute un bouton qui effectuera un shutdown du Raspberry.</p>
<p>Liens utiles :</p>
<p><a href="https://www.davinghiblog.fr/2016/10/13/projet-radio-wifi-etape-1-faire-sortir-de-raspberry/">https://www.davinghiblog.fr/2016/10/13/projet-radio-wifi-etape-1-faire-sortir-de-raspberry/</a></p>
<p><a href="https://ouiaremakers.com/posts/tutoriel-diy-veritable-radio-reveil-raspberry-avec-radio-internet-et-ecran-lcd">https://ouiaremakers.com/posts/tutoriel-diy-veritable-radio-reveil-raspberry-avec-radio-internet-et-ecran-lcd</a></p>
<p><a href="https://www.spiria.com/fr/blogue/iot-m2m-systemes-embarques/construire-une-radio-web-avec-un-raspberry-pi/">https://www.spiria.com/fr/blogue/iot-m2m-systemes-embarques/construire-une-radio-web-avec-un-raspberry-pi/</a></p>
<p><a href="https://www.spiria.com/fr/blogue/iot-m2m-systemes-embarques/construire-une-radio-web-avec-un-raspberry-pi/">https://www.spiria.com/fr/blogue/iot-m2m-systemes-embarques/construire-une-radio-web-avec-un-raspberry-pi/</a></p>
<p>Exemples de liens vers des flux de diverses radios :</p>
<p><a href="https://swissradioplayer.ch/sender-az/#r">https://swissradioplayer.ch/sender-az/#r</a></p>
<p><a href="http://stream.srg-ssr.ch/m/option-musique/mp3_128">http://stream.srg-ssr.ch/m/option-musique/mp3_128</a></p>
<p><a href="http://stream.srg-ssr.ch/m/la-1ere/mp3_128">http://stream.srg-ssr.ch/m/la-1ere/mp3_128</a></p>
<p><a href="http://stream.srg-ssr.ch/m/espace-2/mp3_128">http://stream.srg-ssr.ch/m/espace-2/mp3_128</a></p>
<p><a href="http://stream.srg-ssr.ch/m/couleur3/mp3_128">http://stream.srg-ssr.ch/m/couleur3/mp3_128</a></p>
<p><a href="https://rtn.ice.infomaniak.ch/rtn-high.mp3">https://rtn.ice.infomaniak.ch/rtn-high.mp3</a></p>
<p><a href="http://rouge-90.ice.infomaniak.ch/rouge-90-128.mp3">http://rouge-90.ice.infomaniak.ch/rouge-90-128.mp3</a></p>
<p><a href="http://rouge-80s.ice.infomaniak.ch/rouge-80s-128.mp3">http://rouge-80s.ice.infomaniak.ch/rouge-80s-128.mp3</a>  ?????</p>
<p><a href="http://onefm.ice.infomaniak.ch/onefm-high.mp3">http://onefm.ice.infomaniak.ch/onefm-high.mp3</a></p>
<p><a href="http://radiofribourg.ice.infomaniak.ch/radiofribourg-high.aac">http://radiofribourg.ice.infomaniak.ch/radiofribourg-high.aac</a></p>
<p><a href="https://radiolac.ice.infomaniak.ch/radiolac-high.mp3">https://radiolac.ice.infomaniak.ch/radiolac-high.mp3</a></p>
<p>http://streams.rro.ch/swissmelody.mp3?usid=0-0-H-M-A-01</p>
<p><a href="https://www.framboise314.fr/une-radio-vintage-avec-le-raspberry-pi/">https://www.framboise314.fr/une-radio-vintage-avec-le-raspberry-pi/</a></p>
<p><a href="http://radiochablais.ice.infomaniak.ch/radiochablais-high.mp3">http://radiochablais.ice.infomaniak.ch/radiochablais-high.mp3</a></p>
<p><a href="http://stream.radiochablais.ch/chablais-100francais.mp3">http://stream.radiochablais.ch/chablais-100francais.mp3</a></p>
<p><a href="http://stream.radiochablais.ch/chablais-folklore.mp3">http://stream.radiochablais.ch/chablais-folklore.mp3</a></p>
<p><a href="http://vibration.stream2net.eu:8510/vibra-chfrancaise.mp3">http://vibration.stream2net.eu:8510/vibra-chfrancaise.mp3</a></p>
<p>http://rhonefm.ice.infomaniak.ch/rhonefm-high.aac</p>
<p><a href="http://laradioplus.ice.infomaniak.ch/laradioplus-high.mp3">http://laradioplus.ice.infomaniak.ch/laradioplus-high.mp3</a></p>
<p><a href="https://lausannefm.ice.infomaniak.ch/lausannefm-high.mp3">https://lausannefm.ice.infomaniak.ch/lausannefm-high.mp3</a></p>
<p><a href="http://94.23.25.62:8080/pirates.mp3">http://94.23.25.62:8080/pirates.mp3</a></p>

## Commentaires

### Yves Masur — 21 janvier 2020 à 21:27

<section class="comment-content comment">
<p>Magnifique réalisation, bravo!!</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
