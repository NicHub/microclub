---
title: "Installer un disque SSD (et ré-installer W7 et les programmes)"
date: "2012-08-06T20:14:16"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["hardware", "initiation", "ssd", "stockage", "systeme-dexploitation", "windows"]
url: "/2012/08/06/installer-un-disque-ssd-et-re-installer-w7-et-les-programmes/"
wordpress_id: 854
comment_count: 8
---
<h2>SSD: un nouveau souffle pour votre PC</h2>
<p>On voit régulièrement de la pub pour remplacer son disque dur classique à plateaux et têtes (Hard Disk Drive, HDD), par un Solid State Disk (SSD), donc sans pièce mécanique en mouvement. Quel en est la difficulté et quel est le gain que l’on peut espérer de ce changement de technologie? Voici donc mon expérience à ce sujet, sur un Dell Vostro 1700, datant de… 4 ans. Cette machine portable est équipée d’un CPU Intel T7500 dual core de 2.2 GHz, 4 Go de mémoire avec 2 HDD de 160 Go de 2,5″. Après une recherche d’un SSD de taille semblable ou supérieur, j’opte finalement pour un SSD Samsung, série 830 MZ-7PC256B – qui est un disque de 256 Go.</p>
<p>Une courte recherche sur Toppreise.ch, je le commande chez Techmania (<a href="http://www.techmania.ch/details.aspx?sessionID=1210&amp;hersteller=Samsung&amp;produkt=MZ-7PC256B/WW" target="_blank">http://www.techmania.ch/details.aspx?sessionID=1210&amp;hersteller=Samsung&amp;produkt=MZ-7PC256B/WW</a>) pour 250.40 (avec les frais de transaction), soit moins de 1.- le Go. A mon retour de vacance, le matériel est là.</p>
<h2>Préparation du PC (software)</h2>
<p>Comme mon W7 32 bits tourne depuis un temps certain, et que l’installation/dé-installation de programmes a laissé des scories, j’opte pour une installation propre de Windows, sans utiliser une copie image. Pour cela, je fais un print papier du répertoire <strong>C:\Program Files</strong>, en cochant ceux que je vais ré-installer. Et de la racine, vu que certain programmes y sont logés, comme [Arduino-1.1] ou [Python27].</p>
<p><a href="/media/2012/07/mozbackup.jpg"><img alt="" height="224" src="/media/2012/07/mozbackup-300x224.jpg" title="mozbackup" width="300"/></a>Bien entendu, je copie l’entier du répertoire <strong>C:\user\Yves\Documents</strong> dans le disque D: restant. Précisons aussi que mes photos et musiques sont aussi sur ce 2ème disque. A cette fin, j’avais remplacé les liens [Ma musique] et [Mes images] de  [Documents] pour ce faire. Je complète la préparation de sauvegarde par l’utilisation de Mozbackup, permettant de sauver/restaurer la config de <a href="http://http://www.mozilla.org/fr/firefox/fx/" target="_blank" title="Firefox">Firefox</a> (complète, y compris les setups, les marques pages, les modules!) ainsi que tous mes emails managés par <a href="http://www.mozilla.org/fr/thunderbird/" target="_blank" title="thunderbird">Thunderbird</a>. Afin de garder la possibilité de retrouver d’autres setups d’application, je zippe le répertoire<strong> c:\Users\Yves\AppData\Roaming\</strong> sur D:. Pour finir, je lance un backup complet du PC sur une unité HDD USB externe. Et je l’éteins.</p>
<h2>Préparation du PC (hardware)</h2>
<p><a href="/media/2012/07/SSD.jpg"><img alt="" height="180" src="/media/2012/07/SSD.jpg" title="SSD" width="240"/></a>Débranchement de toutes les prises, et retournement du portable. Dévisser la plaque cachant les disques, extraction du HDD 0; déballage du SSD, petite frayeur… le connecteur SATA, qui est très semblable… n’a pas la même orientation! Mais en examinant la chose de plus près, je constate que le HDD a, avec son cadre de fixation, une pièce qui fait le raccord: je la récupère pour la placer sur le SSD, et tout joue pile-poil. Revissage du tout, reconnexion, et retournement de la bête. Allumage…</p>
<h2>Installation propre</h2>
<p>Le BIOS ne trouve plus de système d’exploitation, normal. J’installe W7 Ultimate depuis le CD, et là déjà je remarque que les redémarrages successifs sont singulièrement rapides! Pour la bonne compréhension de la suite, je précise que j’ai conservé sans changement le nom d’utilisateur et de mot de passe. Après les premiers paramètres usuels, vient la ré-installation des données et des programmes. Dans cet ordre.</p>
<p>En copiant <strong>Documents</strong>, je constate que le lien initial sur le répertoire de stockage des images <strong>Mes images</strong> est remplacé par le contenu!. En effet, sur le HDD original, le stockage des images était déplacé sur D:\Pictures afin de libérer de la place sur le disque C:, sans toutefois troubler les applications et le backup, pour lesquels le contenu apparaît comme si l’on avait tout sur C:. Pour la nouvelle configuration, je me propose de maintenir le stockage de musiques et d’images sur un disque distinct, soit sur D:.</p>
<h2>Problème de lien</h2>
<p>Donc ma copie n’était pas celle du lien, mais bien du contenu. Ceci n’est pas particulièrement étonnant, vu qu’une fois établit, on ne sais pas si l’on est dans la « jonction » ou dans un véritable répertoire… Pour rétablir correctement cette disposition, j’efface donc le contenu, renomme <strong>Mes images</strong> par autre chose et lance une console en mode Admin. La commande à réaliser est: mklink /J « Mes images » D:\Pictures (les guillemets de l’argument sont nécessaire si il y a un espace). Et aussi pour <strong>Pictures</strong>, qui est dans le répertoire de l’utilisateur, je procède de même:</p>
<p><a href="/media/2012/08/mklink.jpg"><img alt="" height="120" src="/media/2012/08/mklink-300x120.jpg" title="mklink" width="300"/></a></p>
<p>Précisions que ceci ne dépend pas du tout du SSD, mais bien de la ré-installation de Windows sur n’importe quel support de stockage!</p>
<h2>Restauration: programmes et paramètres</h2>
<p>C’est le plus difficile, lorsqu’on fait une installation dite « propre ». Installer un programme est d’une grande facilité; mais le faire fonctionner comme on le désire… ce peut être assez compliqué.  Il y a 3 catégories de programmes:</p>
<ul>
<li>ceux qui stockent leurs paramètres dans le répertoire d’installation</li>
<li>ceux qui les mettent chez l’utilisateur (ou tous les…) dans \Appdata\Roaming</li>
<li>Et ceux qui bricolent dans la registry</li>
</ul>
<p>Dans tous les cas, c’est un peu difficile de savoir quoi faire. Grâce à Mozbackup (v. ci-dessus), les emails, les liens sont restitués en un clin d’oeil pour Firefox et Thunderbird. Un exemple simple, le programme FreePing, (voir <a href="http://www.tools4ever.com/" target="_blank">Tools4ever</a>) stocke les paramètres dans un fichier .INI, sis dans le répertoire d’installation. Pour les retrouver, il faut le faire via le backup de W7. Pour rapidement le chercher et le restaurer, il m’a suffit de connecter l’unité USB, et de cliquer sur le répertoire<strong> VOSTRO</strong> présenté.</p>
<p><a href="/media/2012/08/Wbackup.jpg"><img alt="" height="105" src="/media/2012/08/Wbackup-300x105.jpg" title="Wbackup" width="300"/></a></p>
<p>Sûr, l’installation « propre » n’a pas que des avantages. Mais on évite de traîner des reliquats passés, des ralentissements potentiels, ainsi que de l’espace inutilisé par des kyrielles de code obsolète. Un des effets secondaires est que la signature du PC change. Ça se voit au moment ou j’installe les programmes <a href="http://www.wuala.com" target="_blank" title="Wuala">Wuala </a>et <a href="http://www.DropBox.com" target="_blank" title="DropBox">DropBox</a>, deux accès à des stockages sur le « cloud ».</p>
<p><a href="/media/2012/08/wuala.jpg"><img alt="" height="159" src="/media/2012/08/wuala-300x159.jpg" title="wuala" width="300"/></a></p>
<p>Les répertoires à synchroniser sont reconnus, mais on voit que le partage présente 3 ordinateurs, dont deux fois le Vostro. A nouveau, nous voyons donc que les problèmes d’installation sont liés à un changement de disque, mais pas du tout à son type.</p>
<h2>Tuning de Windows</h2>
<p>Si l’on utilise un SSD, il s’agit aussi de faire quelques réglages de Windows. l’OS est prévu pour un disque dur avec des plateaux, des têtes, des pistes et des secteurs, ce que l’on résume par <a href="http://fr.wikipedia.org/wiki/Disque_dur" target="_blank" title="Wiki HDD"><strong>géométrie</strong></a> du disque. Un SSD est constitué de cellules mémoires au comportement fort différent. Un HDD use ses paliers et son moteur, mais pas ses têtes qui flottent sur un coussin de gaz. le nombre de lecture/écriture est quasi illimité. Un SSD utilise de la mémoire FLASH, dont le nombre d’écriture est limité (voir <a href="http://fr.wikipedia.org/wiki/Solid-state_drive" target="_blank">http://fr.wikipedia.org/wiki/Solid-state_drive</a> ). demande à l’OS de limiter donc ses écritures au besoins avérés, sous peine de diminuer la durée de vie du SSD. Un logiciel permet ce tuning, qui consiste à arrêter des technique de Windows</p>
<p><a href="/media/2012/08/SDD_magicien.jpg"><img alt="" height="196" src="/media/2012/08/SDD_magicien-300x196.jpg" title="SDD_magicien" width="300"/></a></p>
<p><strong>Superfetch</strong>, technique de préchargement d’application est inutile. La défragmentation non plus, vu que le temps d’accès et le débit ne dépend plus de la continuité des secteurs. Les services d’indexation sont nuisibles, par les écritures incessantes qu’ils provoquent et la création et modification de fichiers d’index dans les répertoires. La gestion de puissance est également à modifier, un HDD n’est arrêté qu’après un long laps de temps de non-utilisation, alors que pour un SSD au démarrage quasi instantané ce problème ne se pose pas. Dans le cas d’un portable, la batterie sera moins sollicitée.</p>
<h2>Faut-il activer la compression NTFS sur un SSD?</h2>
<p>Windows permet une assez bonne compression sur les unités NTFS. L’idée est bien entendu de gagner de la place de stockage, mais aussi d’augmenter la rapidité. La théorie est que le temps pris par le CPU pour la compression/expansion est négligeable par rapport à celui, gagné, de temps de lecture raccourci dû au fichier physiquement plus court. Mais avec un SSD? comme il reste cher, mieux vaut l’épargner; mais si on perdait du temps de chargement? D’autant plus que certains fichiers tels que des images JPG ou de la musique MP3 n’offre aucun gain de compression! Dans <a href="http://www.tomshardware.com/reviews/ssd-ntfs-compression,3073.html" target="_blank" title="Tom's Hardware">un article</a> de Tom’s hardware, l’analyse fouillée sur un PC de bureau ne donne pas de résultats flagrants permettant de faire pencher la balance. Je m’en tiendrai à la conclusion : des répertoires de grandes quantités de données peuvent être comprimés sans que les performances CPU d’une machine de 2 ou 4 coeurs soient sensiblement atteintes. Cependant, ceci n’est pas forcément vrai pour des portables aux performances inférieures…</p>
<p>Pour ma part, je considère que la fragmentation (elle existe bien sûr!) sur un SSD n’a aucune importance, et je ne comprimerai que si je vois la place libre fondre fortement. Les gros fichiers étant les images et le son, d’ores et déjà installés sur le HDD classique restant, l’unité SSD C: est utilisées à 30,6 Go sur les 238 Go (255’953’203’200 octets) à disposition. J’ai le temps de voir venir….</p>
<h2>Performances</h2>
<p>Ces indications ne sont pas un « benchmark », mais donnent une idée. Démarrage de W7 (après le POST, donc): 16 secondes, alors qu’il me fallait pas loin de 50-60 secondes; démarrage de Libre Office 4-5 secondes (avant: 20-25 sec.). Sortir de la mise en veille profonde: 15 secondes, soit comme le démarrage normal.</p>
<p>Une fois logué, le bureau est mis en place en 3-5 secondes, du bonheur!</p>
<p>A ce jour (8/2012) le prix d’un HDD de 1 Teraoctet est de 130.-, soit 0.13 Fr le Go. C’est huit fois moins cher que le SSD. Par contre ce dernier offre un vitesse et une solidité mécanique bien supérieure; il diminue la consommation d’énergie. Et plus rapide c’est mieux, point!</p>
<p>Yves Masur</p>

## Commentaires

### Goulu — 6 août 2012 à 20:26

<section class="comment-content comment">
<p>Ah ben merci, justement je prévoyais l’installation d’un SSD un de ces jours. Par contre je pensais migrer mon install de Win7 64 bits HD vers SSD, et il semblerait que les softs mettant « ce qu’il faut » du HD vers le SSD sont assez pointus et de qualité variables. Des idées là dessus ?</p>
 </section>

### Yves Masur — 6 août 2012 à 21:38

<section class="comment-content comment">
<p>Le disque SSD que j’ai utilisé se vend aussi avec un kit pour cloner le HDD, câble USB-&gt;SATA. C’est copié via le gost de Norton.</p>
 </section>

### Burnand — 11 août 2012 à 16:52

<section class="comment-content comment">
<p>Idem avec le SSD de Kingston. Par contre le logiciel est un Acronis True Image. Il offre la possibilité de clôner un  HD d’une capacité supérieure au SSD, pour autant que l’espace utilisé soit plus petit que la capacité du SSD.</p>
<p>Concernant l’emplacement du dossier « Utilisateurs » contenant toutes les données et les paramètres du ou des utilisateurs de la machine. Il est possible de déplacer manuellement les dossiers « Documents », Images », « Musique », »Vidéos » pour les mettre sur un deuxième HD. Toutefois il existe un petit soft gratuit « ProfilRelocator » (<a href="http://software.bootblock.co.uk/?id=profilerelocator" rel="nofollow ugc">http://software.bootblock.co.uk/?id=profilerelocator</a>) qui fait ça automatiquement et en déplacant tout le dossier « Utilisateurs » sur un autre disque. La seule condition est de le faire juste après une installation vierge. Petit truc : mettre un nom d’utilisateur provisoire pendant l’installation de Windows. </p>
<p>Quand à l’installation d’un SSD, il n’y a pas à réfléchir le résultat en vaut le prix…</p>
 </section>

### Yves Masur — 25 novembre 2012 à 16:48

<section class="comment-content comment">
<p>Avec Linux, il faut « tuner » les pilotes pour attaquer un SSD. Utiliser le format ext4, et prendre quelques précautions avec l’allocation par <i>extent</i>.<br/>
Explications ici: <a href="http://libre-ouvert.toile-libre.org/?article72/ssd-crucial-m4-64-go-linux-trim-ext4-noatime" rel="nofollow ugc">http://libre-ouvert.toile-libre.org/?article72/ssd-crucial-m4-64-go-linux-trim-ext4-noatime</a></p>
 </section>

### ytaz23 — 16 janvier 2014 à 17:48

<section class="comment-content comment">
<p>salut et bonne année……. voilà j’ai décidé de changer le support hd suite a un bug magistral de l' »os » de m…. qui est vista. J’avais en plus sur un autre hd Seven. Depuis que j’ai viré vista, ma licence Seven est soit disant une copie illègale ????, Ce qui m’ennuie énormément ……<br/>
je ne sait pas quoi faire ! réinstallé vista pour que Seven fonctionne normalement ????? et si je change de hd pour un ssd faut il que je rachète une nouvelle licence ?????? je comprends mieux pourquoi microsoft est le n°1 de l’informatique !!!<br/>
help me</p>
 </section>

### ↳ Réponse — Jacques — 17 janvier 2014 à 11:26

<section class="comment-content comment">
<p>Bonjour et idem pour les vœux…<br/>
– Licence Windows 7 : elle n’est valable que sur un seul PC. Si tu essaies de l’installer sur un autre, tu reçois un message de non validité. Tu peux la valider en utilisant la méthode par téléphone. A la question « nombre d’appareils… » réponds 1.</p>
<p>– je suppose que tu as une licence Windows 7de mise à jour. Si c’est le cas, tu ne peux l’installer que sur un PC tournant Windows Vista ou XP. Il te faut donc installer Vista, effectuer les mises à jour, sauf erreur au minimum le SP1, puis effectuer la mise à jour vers Windows 7.</p>
 </section>

### GROT jc — 26 février 2015 à 15:53

<section class="comment-content comment">
<p>26 02 2015<br/>
bonjour  avec grand intérêt vos commentaires me sont très intéressant ,<br/>
 je suis sur un portable P Bel  avec VISTA,  le transfert via  kingston 223 GO et 212 d’effectif , comme indiquer<br/>
BONNE vitesse de mise en route ,, le problème après quelques jours de travail sans installations  l’espace libre a fondu ;a ce jour  reste 2,90go,<br/>
les dossiers photo,doc se trouvent en totalités sur une clef usb<br/>
 je m’interroge sur la marge a suivre afin de retrouver un peu d’aisance<br/>
 merci pour vos conseils<br/>
 jicigi</p>
 </section>

### ↳ Réponse — ymasur — 26 février 2015 à 22:56

<section class="comment-content comment">
<p>En effet, c’est louche… Il faut vérifier s’il n’y a pas des doublons de répertoire entiers, ou si une application pédale à fond et crée des logs monstrueux. Attention avec la défragmentation et les programmes d’indexages, qu’il faut bannir!!</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
