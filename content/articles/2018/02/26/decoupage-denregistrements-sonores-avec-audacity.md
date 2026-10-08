---
title: "Découpage d’enregistrements sonores avec Audacity"
date: "2018-02-26T08:00:08"
lastmod: "2018-02-22T18:33:45"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["cd-a", "echantillonnnage", "mp3", "musique"]
url: "/2018/02/26/decoupage-denregistrements-sonores-avec-audacity/"
wordpress_id: 3716
comment_count: 1
---
<h1>But et méthode</h1>
<p>Depuis quelques années, j’enregistre les soirées de la fanfare. C’est donc de la musique « live ». L’enregistrement d’une soirée est constitué de deux fichiers au format brut WAV, 44.1 kHz stéréo en 24 bits, d’environ une heure chacun. Ce format a l’échantillonnage standard d’un CD, avec une résolution supérieure : le CD comporte du WAV en 16 bits.</p>
<p>Le processus consiste à importer le fichier, puis de le segmenter de manière à exporter des morceaux numérotés et nommés. Il s’agit aussi de normaliser l’amplitude, d’égaliser gauche et droite, et de limiter à quelques secondes d’applaudissements en fin de morceau, en fondu enchaîné. Une fois cette préparation effectuée, on exportera les morceaux dans des fichiers individuels, en WAV pour le gravage de CD et/ou en MP3 pour la diffusion sur le WEB.</p>
<h2>Equipements utilisés</h2>
<ul>
<li>Micro d’enregistrement : ZOOM H2N ou équivalent</li>
<li>Soft Audacity 2.2.1 ou supérieur</li>
<li>PC Win 10 ou supérieur</li>
</ul>
<h1>Importation et création du projet</h1>
<p>Le travail se fait dans un répertoire bien déterminé. Dans mon cas, j’ai choisi d:\Musique\WAV\Soirees-2018\. Glisser le fichier WAV dans la fenêtre Audacity. Après quelques secondes, l’enveloppe des deux canaux apparait ; ici, C02.WAV. Audacity propose de travailler sur une copie du fichier original. Comme ce dernier est repris de la carte SD du micro-enregistreur, ce n’est pas nécessaire. En cas de dommage total, on pourra toujours le reprendre…</p>
<p>Audacity importe le son par défaut en floating point 32 bits, afin de conserver la précision sur les manipulations qui affectent l’amplitude. Celle-ci est normalisée entre -1.0 et + 1.0.</p>
<p><img height="1080" src="/media/2018/04/word-image.png" width="1920"/></p>
<p>Les travaux que nous allons faire sur cet enregistrement doivent être sauvegardés dans un <strong>projet Audacity</strong> : le nommer à sa convenance. Le fichier de projet prend l’extension « .aup » ; p. exemple C02.aup. Au fur et à mesure des opérations, il faut régulièrement l’enregistrer. Ceci crée un répertoire (ici : C02_data), des sous-répertoires et fichiers avec un nom hexadécimal .au et .auf (audacity bloc file).</p>
<h1>Manipulation courantes</h1>
<h2>Raccourcis utiles</h2>
<table>
<tbody>
<tr>
<td><strong>Touches</strong></td>
<td><strong>Fonction</strong></td>
<td><strong>Utilité</strong></td>
</tr>
<tr>
<td>Ctrl + 1</td>
<td>Zoom</td>
<td>Repérage précis : début, fin de morceau</td>
</tr>
<tr>
<td>Ctrl + 3</td>
<td>Dé – zoom</td>
<td>Vue d’ensemble</td>
</tr>
<tr>
<td>Ctrl + B</td>
<td>Marquer un segment</td>
<td>Sur la sélection ou sur un point</td>
</tr>
<tr>
<td>Ctrl + S</td>
<td>Sauver le projet</td>
<td></td>
</tr>
<tr>
<td>Ctrl + Shift + L</td>
<td>Export multiple</td>
<td>Crée les fichiers audios préparés</td>
</tr>
<tr>
<td>Ctrl + Z</td>
<td>Annuler la manipulation</td>
<td>Revenir à l’état précédent</td>
</tr>
</tbody>
</table>
<h2>Croiser G et D</h2>
<p>Suivant le type de micro et de l’enregistrement, il peut être nécessaire de croiser les canaux :</p>
<p><img height="547" src="/media/2018/04/word-image-1.png" width="395"/></p>
<h2>Normaliser le niveau G et D</h2>
<p>Pour s’assurer de l’équilibre, il faut écouter un passage musical représentatif. Le niveau max est mémorisé par un trait bleu ; le passage par un trait vert. Dans l’exemple ci-dessous, on voit que G est 3 dB plus fort que D : pointe à -9 dB, respectivement à -12 dB.</p>
<p><img height="133" src="/media/2018/04/word-image-2.png" width="597"/></p>
<p>Seule une écoute au casque attentive permet de décider s’il faut équilibre la balance. Il s’agit de ne pas se laisser influencer par des instruments qui « donnent » réellement plus fort dans un passage, par exemple. En cas de doute, il vaut mieux ne pas corriger ; ou ne le faire que partiellement.</p>
<p>Pour équilibrer des canaux, il faut :</p>
<ul>
<li>Séparer les canaux stéréo vers mono</li>
<li>Sélectionner le canal plus faible</li>
<li>Menu Effet -&gt; Amplification</li>
<li>Ajouter x dB (ici 3 dB) pour obtenir l’équilibre</li>
<li>Joindre les pistes en stéréo</li>
</ul>
<h2>Marquage des segments</h2>
<p>Le but est de marquer le début et la fin du morceau et de nommer la fenêtre ainsi définie. Par l’amplitude affichée, il est relativement facile de voir le début du morceau.</p>
<ul>
<li>Positionne le curseur environ 1 seconde avant le début de la musique</li>
<li>Marqueur : Ctrl + B</li>
<li>Nommer, en commençant par un n°, à 2 digits, p. ex : « 01 Balade »</li>
<li>Etirer le segment vers la fin par le <img height="33" src="/media/2018/04/word-image-3.png" width="31"/></li>
</ul>
<p>Si on tire par la boule, tout le segment est déplacé. Pour positionner précisément, zoomer avec Ctrl + 1 ; dé-zoomer par Ctrl + 3.</p>
<p><img height="330" src="/media/2018/04/word-image-4.png" width="359"/></p>
<h2>Normaliser l’amplitude du morceau</h2>
<p>Afin d’avoir une écoute au niveau optimal, il s’agit de régler l’amplitude globale du morceau au maximum de l’amplitude possible sans distorsion (saturation).</p>
<ul>
<li>Sélectionner le segment par un clic sur le marqueur (ici : « 01 Balade »</li>
<li>Menu : Effet -&gt; Amplification…</li>
</ul>
<p>Par défaut, Audacity propose l’amplification maximale pour amener le niveau crête à 0dB. Il s’agit de ne pas arriver en saturation, case à décocher.</p>
<p><img height="280" src="/media/2018/04/word-image-5.png" width="610"/></p>
<h2>Traiter la fin du morceau</h2>
<p>La fin est aussi facilement identifiable visuellement : après un silence d’approximativement deux secondes, les applaudissements se voient aisément. On ne laisse pas tous les applaudissements, mais plutôt laisse quelques secondes, puis on termine par un fading sur une seconde. <img height="765" src="/media/2018/04/word-image-6.png" width="927"/></p>
<ul>
<li>Positionner le marquage de fin après 5 à 7 secondes des applaudissements</li>
<li>Sélectionner des applaudissements avec le curseur sur 1 sec. Environ de la fin</li>
</ul>
<p>Une petite main apparaît lorsqu’on survole la zone proche du marquage de fin; une ligne jaune permet de positionner précisément le curseur sur celle-ci. Sélectionner en reculant à partir de la fin du segment. On peut s’aider des compteurs de temps au bas de la fenêtre. Puis :</p>
<ul>
<li>Menu : Effets -&gt; Fondu en fermeture</li>
</ul>
<p>Après écoute si le choix n’est pas bon, revenir en arrière avec Ctrl + Z et répéter l’opération. Attention à ne plus déplacer le marqueur de fin, sinon le fading ne sera pas/plus au bon endroit ! Le cas échéant, répéter l’opération.</p>
<h1>Exporter les morceaux</h1>
<p>Tous les morceaux sont traités : segmenté début – fin, nom indiqué, équilibre, amplitude, fading sont posés. Audacity permet d’exporter efficacement les segments nommés, et de créer les fichiers nécessaires. Pour ce faire : Fichier -&gt; Exporter -&gt; Export multiples.</p>
<p>Si le nommage des morceaux est précédé d’un nombre, le classement chronologique sera facilité.</p>
<p>Par défaut, l’export sera fait dans le répertoire de travail. Les options dépendent du format exporté : le WAV 16 bits signé, destiné au gravage de CD Audio (CD-A), n’a pas d’options. Si le format désiré est en MP3, il faut préférer la qualité à la compression. Un format de 224 Kb/s au débit constant (quality : high) permet une qualité très proche du CD-A.</p>
<p><img height="561" src="/media/2018/04/word-image-7.png" width="1090"/></p>
<p>Les métadonnées sont à renseigner. Elles suivent le fichier MP3 ; c’est particulièrement important pour la diffusion sur le WEB.</p>
<p><img height="500" src="/media/2018/04/word-image-8.png" width="756"/></p>
<p>Des players montrent ces informations. Par exemple, voici l’affichage par le programme WinAmp:</p>
<p><img height="495" src="/media/2018/04/word-image-9.png" width="647"/></p>
<h1>Conclusion</h1>
<p>Grâce au logiciel gratuit Adacity et des manipulations relativement simples, il est possible à partir d’un enregistrement brut et sans délimitation – mais de bonne qualité – de produire des archives sonores optimales. Le produit sera une série de morceaux de musique nommés, dont le début, fin, l’amplitude sonore et l’équilibre représenterons le plus fidèlement possible l’exécution « live ».</p>
<h3>Références</h3>
<p>Micro Zoom : <a href="https://www.zoom.co.jp/products/handy-recorder/h2n-handy-recorder">https://www.zoom.co.jp/products/handy-recorder/h2n-handy-recorder</a></p>
<p>Logiciel Audacity : free, open source, cross-platform audio software for multi-track recording and editing: <a href="https://www.audacityteam.org/">https://www.audacityteam.org/</a></p>
<p>Yves Masur (2/2018)</p>

## Commentaires

### Yves Masur — 4 avril 2018 à 17:25

<section class="comment-content comment">
<p>Une excellente description des format de compression et leur effet, ici:<br/>
<a href="https://www.lesnumeriques.com/audio/mp3-aac-ogg-voyage-coeur-formats-compresses-a2053.html" rel="nofollow ugc">https://www.lesnumeriques.com/audio/mp3-aac-ogg-voyage-coeur-formats-compresses-a2053.html</a></p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
