---
title: "Yun – Expériences & découvertes"
date: "2014-08-13T19:58:08"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["arduino", "consoles", "embarque", "hardware", "initiation", "linux", "processeurs", "python", "systeme-dexploitation"]
url: "/2014/08/13/yun-experiences-decouvertes/"
wordpress_id: 1513
comment_count: 1
---
<h2>Le champ d’application</h2>
<p>Dans un article précédent, je montrais le besoin d’<a href="/2014/06/15/serveur-dhcp-avec-windows-7/" target="_blank" title="Serveur DHCP avec Windows 7">activer une DHCP</a> pour utiliser pleinement un Arduino Yun.</p>
<p>Le présent article répond à quelques questions légitimes de l’utilisation et des possibilités de cette plateforme bi-processeur. Voici rapidement les caractéristiques du Yun. C’est un hardware similaire au Leonardo, équipé du CPU Atmel ATmega32U4, mais il comprend – c’est ici l’essentiel – un second CPU Atheros AR9331, qui tourne un Linux. OpenWrt est adapté pour le Yun, appelé <strong>Linino</strong>. L’OS est sur une flash de 16 Mb ; il en utilise 9 Mb. Il a des connexions Ethernet ; Wifi et USB-A supplémentaires ; un port pour mini carte SD. L’alimentation se fait en 5V, pas de régulateur. Soit par la mini USB, soit par les pins 5V et VCC. La partie Arduino communique avec le Linux via le serial1.</p>
<p>Les détails du système sont décrits ici (en anglais) : <a href="http://arduino.cc/en/Guide/ArduinoYun" target="_blank">http://arduino.cc/en/Guide/ArduinoYun</a> .</p>
<p>Chaque unité à son propre bouton de reset ; ainsi que le WiFi. Gag : il faut <strong>presser 2 x</strong> pour relancer le 32U4, donc le sketch (soit le programme) Arduino ; il se redémarre en quelques secondes pendant que la liaison USB tombe et se reconnecte.</p>
<p>Redémarrer le Linino prend plus de temps, env. 60 sec ; le Wifi n’est actif qu’après 1’ 15’’. Ceci rend donc long les différents essais de configuration et/ou de paramètres.</p>
<p>Au début, commencez par <strong>mettre à jour</strong> votre version de Linux, en en copiant l’image binaire sur une SD, à introduire dans son logement + redémarrage. Ça va vite. Les mises à jour, pas le démarrage…</p>
<h2>Travailler avec le Wifi</h2>
<p>M’a occasionné quelques déboires. Celui-ci n’est pas performant, dans la mesure où mes 2 PCs portables se connectent sans problème avec un débit entre 18 et 36 Mb, selon où ils sont placés sur le bureau ; tandis que le Yun ne « croche » qu’une fois sur deux ; et perd la connexion par la suite.</p>
<p>Si le Yun ne croche pas sur le routeur Wifi, il se met en en mode serveur, et propage un nom Wifi du genre <em>ArduinoYun</em><em>-XXXXXXXXXXXX</em>. Seule la page de config est atteignable. Et on reconfigure… pour la n <sup>ième</sup> fois. D’où mon souhait de développer, configurer et tester avec une liaison Ethernet câble ; puis le programme terminé, le rapprocher du routeur Wifi. Ce dernier est au sous-sol, alors que le bureau est au premier étage.</p>
<h2>Travailler avec le Linuino</h2>
<p>Comme tout bon Linux, il offre la possibilité de se connecter en console – donc avec PuTTY <a href="http://www.putty.org/" target="_blank">http://www.putty.org/</a> – Mais il faut connaître l’adresse IP du Yun, of course. On se logue en ‘root’ avec le PW que l’on aura mis dans la page d’accueil initiale. Le Linuino comporte l’éditeur Nano, ce qui facilite les choses pour les modifications de fichier.</p>
<h2>Nom du Yun propagé sur le réseau</h2>
<p>Le Yun n’utilise pas le classique Netbios pour propager son nom réseau, même si l’EDI Arduino le trouve, le PC ne le voit pas. Il faut donc le pinguer par son adresse ; ce n’est pas pratique. Deux solutions s’offrent pour qu’il soit reconnu nommément sur PC, par exemple par la commande PING :</p>
<p>–        Installer le programme Apple « Bonjour », destiné aux imprimantes sur LAN<br/>
–        Modifier le fichier Linux /etc/network</p>
<pre>root@yunmasur:~# cat /etc/config/network 

config interface 'loopback'
       option ifname 'lo'
       option proto 'static'
       option ipaddr '127.0.0.1'
       option netmask '255.0.0.0'

config interface 'lan'
       option proto 'dhcp'

config interface 'wan'
       option ifname 'eth1'
       option proto 'dhcp'
       option metric '10'
       option hostname 'yunmasur'</pre>
<p><strong>Note 1</strong>: si les 2 interfaces Ethernet et Wifi sont connectées, un ping selon le hostname va sur la 1ère interface qui s’est connectée, donc l’Ethernet.</p>
<p><strong>Note 2</strong> : mes explications se rapportent à un Yun qui s’appelle « yunmasur ». Bien entendu, vous l’interprétez avec le nom du Yun que vous venez de déballer et d’essayer !</p>
<p>Pour le <strong>stockage de données</strong> sur carte SD, on trouve comme exemple: <a href="http://arduino.cc/en/Tutorial/YunDatalogger" target="_blank">http://arduino.cc/en/Tutorial/YunDatalogger</a> . Et pour lire des températures et les <strong>afficher sur une page</strong> WEB, il y a bien un projet qui ressemble à ça, ici : <a href="http://arduino.cc/en/Tutorial/TemperatureWebPanel" target="_blank">http://arduino.cc/en/Tutorial/TemperatureWebPanel</a> . Cependant, d’après le nombre de questions et de posts dans le forum, tout laisse croire qu’il n’est pas du tout clair. Voir incomplet, à tout le moins dans sa partie WEB.</p>
<h2>Où et comment doivent être les fichiers ?</h2>
<p>Rien n’est bien expliqué ; si on les voit depuis Linux ou depuis l’URL, ça change forcément. Mais comment ? La structure des fichiers sur la SD doit être selon les 2 possibilités ci après.</p>
<h2>Servir une page WEB statique</h2>
<p>La SD card doit contenir la page WEB et les fichiers annexes, comme les images ou les CSS, dans le répertoire ainsi: /arduino/www/<strong>index.htm </strong>et le Yun répond à l’URL yunmasur.local/sd/</p>
<p><a href="/media/2014/08/1_index.jpg"><img alt="1_index" height="171" src="/media/2014/08/1_index.jpg" width="404"/></a></p>
<p>Et avec l’extension « html », c’est bien ce fichier qui vient:</p>
<p><img alt="2_index" height="171" src="/media/2014/08/2_index.jpg" width="437"/></p>
<p>Visiblement, tout ce qui est dans la SD /arduino/www/ est servi, on peut y mettre des pages, des images et des scripts JS. Pour du PHP, il faudra avant l’installer sur le Linino. A ce stade, la partie Arduino sketch n’est pas sollicitée.</p>
<h2>Utiliser une URL par le sketch</h2>
<p>L’exemple de base est le programme Bridge.ino qui démontre comment lire une partie de l’URL au profit du sketch. Sur la carte SD, les répertoires : /arduino/www/ (et n’importe quoi, à partir de ça) suffisent.</p>
<p>Les deux URLs suivantes allument et éteignent la LED13, placée d’office sur le Yun. Pour voir à quelle vitesse, je les ai réunies dans un batch, qui tourne en rond. Les URL sont lancées par un programme assez génial fonctionnant en ligne de commande : cURL, qui est installé à la racine du disque C :</p>
<pre>:start
c:\curl\curl http://Yunmasur.local/arduino/digital/13/1
c:\curl\curl http://Yunmasur.local/arduino/digital/13/0
goto start</pre>
<p>Vous vous attendez à un clignotement rapide, imperceptible à l’œil ? Eh bien non. Temps d’une phase ~2,8 sec. (f = 0.17 Hz)</p>
<p>La partie de l’URL passée au sketch est celle en jaune. Après une connexion, on peut lire la partie jusqu’au ‘/’, après l’URL de base <strong>Yunmasur.local/arduino/</strong> , ainsi :</p>
<pre>void process(YunClient client) {
// read the command
String command = client.readStringUntil('/');</pre>
<p>Dans ce cas : ce sera « digital ». Ensuite, c’est assez facile de lire le reste pour en déduire le n° de sortie (13) et l’état, 1 ou 0. S’il n’y a pas d’état, le sketch est prévu pour rendre l’état de la pin 13.</p>
<h2>L’usage du C++ String</h2>
<p>Les exemples font un usage assez abondant de manipulation avec la classe String <a href="http://arduino.cc/en/Reference/StringObject" target="_blank">http://arduino.cc/en/Reference/StringObject</a> . C’est une facilité tentante… la doc de la librairie dit :</p>
<blockquote><p><em>You can concatenate Strings, append to them, search for and replace substrings, and more. It takes more memory than a simple character array, but it is also more useful.</em></p></blockquote>
<p>Avec un processeur doté de 2500 octets( !) est-ce bien raisonnable ? Une recherche sur le WEB l’indique : c’est non ! C’est vite la source de déboires et de comportement peu catholique. Liens en relation :</p>
<p><a href="http://stackoverflow.com/questions/17972523/are-there-limits-on-string-length-in-arduino" target="_blank">http://stackoverflow.com/questions/17972523/are-there-limits-on-string-length-in-arduino</a> et</p>
<p><a href="http://forum.arduino.cc/index.php/topic,85491.0.html" target="_blank">http://forum.arduino.cc/index.php/topic,85491.0.html</a></p>
<p>Donc String, c’est bien pour les exemples, car ça simplifie l’écriture. Sur un PC qui est doté de Gb de mémoire, OK. Mais pour la sûreté et la pérennité du fonctionnement, dans le cas de codage de programme embarqué, on évite les pratiques qui font de l’allocation de mémoire à la tout va.</p>
<h2>Voir le Yun travailler</h2>
<p>Pour cela, il faut se connecter avec PuTTY en console, et lancer la commande top. On voit alors que le programme Python bridge.py est le plus gros consommateur de CPU et de mémoire.</p>
<p><a href="/media/2014/08/3_console.jpg"><img alt="3_console" height="393" src="/media/2014/08/3_console.jpg" width="605"/></a></p>
<h2>Le projet (en cours)</h2>
<p>Il comporte 3 capteurs de température disposés pour mesurer sur ma chaudière:</p>
<p>–        L’eau de retour du circuit des capteurs solaires<br/>
–        L’eau solaire (200 l)<br/>
–        L’eau chaude sanitaire (200 l aussi)</p>
<p>Le programme doit me permettre de voir via un browser, les températures actuelles ; il doit stocker dans un fichier une ligne avec la date et l’heure, les 3 valeurs ; ceci toutes les 10 minutes. Les données seront au format tabulé de manière à être exploitable par Excel. Pour ce faire, j’ai utilisé 4 techniques :</p>
<p>–        La lecture de sondes one-wire<br/>
–        La lecture du temps Linux<br/>
–        Le stockage de données sur carte SD<br/>
–        Un interfaçage WEB avec le sketch.</p>
<p>Il fonctionne, mais n’est pas encore présentable, ce sera pour plus tard…</p>
<p>Yves Masur (8/2014)</p>
<h2>Références :</h2>
<p>cURL: <a href="http://fr.wikipedia.org/wiki/CURL" target="_blank">http://fr.wikipedia.org/wiki/CURL<br/>
</a>Arduino Yun: <a href="http://arduino.cc/en/Main/ArduinoBoardYun" target="_blank">http://arduino.cc/en/Main/ArduinoBoardYun<br/>
</a>One wire : <a href="http://playground.arduino.cc/Learning/OneWire" target="_blank">http://playground.arduino.cc/Learning/OneWire</a></p>

## Commentaires

### franic — 17 août 2014 à 07:57

<section class="comment-content comment">
<p>L’antenne intégrée sur la platine ne permet pas une longue distance entre le routeur wifi et le Yun, mais elle a le mérite de pouvoir, dès la mise sous tension du module, de permettre des échanges de transmissions.<br/>
Par contre le Yun est équipé d’une fiche pour une antenne externe. Vous pouvez ainsi récupérer une antenne d’un ancien router et la brancher sur votre Yun … et tout à coup la distance de transmission sera parfaite !</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
