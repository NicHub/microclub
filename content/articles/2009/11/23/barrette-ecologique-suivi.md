---
title: "Barrette écologique – suivi"
date: "2009-11-23T22:11:16"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["barrette", "c", "cpu", "ecologie", "hardware", "javascript", "lan", "programmation", "reseau", "rtc", "web"]
url: "/2009/11/23/barrette-ecologique-suivi/"
wordpress_id: 252
comment_count: 11
---
<p>Comme ce projet avance par étapes, je me propose d’en relater les avancées ici. Eh oui, c’est finalement assez complexe, et ça mérite quelques éclaircissements. Il ya :</p>
<ul>
<li>Le hard</li>
<li>le logiciel bas niveau</li>
<li>les processus LAN</li>
<li>du temps réel</li>
<li>l’interface WEB</li>
<li>de la compression</li>
<li>des stockages et transmission de données</li>
</ul>
<p>Actuellement (novembre 2009),  le hard est posé dans les grandes lignes; mais pas complètement arrêté. La clock RTC sera matérialisé par un DS1307, une pile, un quartz. La commande de triacs sera fortement inspirée d’une interface de Franic (merci Laurent!).</p>
<p>Les couches logicielles assez bien définies; toutefois, c’est la partie qui risque de subir les plus grand changements – même si le hard est terminé! Chacun pour</p>
<figure aria-describedby="caption-attachment-256"><a href="/media/2009/11/ck_datas.jpg"><img alt="clock et datas" height="225" src="/media/2009/11/ck_datas.jpg?w=300" title="ck_datas" width="300"/></a><figcaption>clock et datas</figcaption></figure>
<p>ra peaufinner son interface WEB. Pour cela, il faudra une bibliothèque bien établie de tags, et de modules en Javascript. Et de modules en C, bien sûr.</p>
<p>Le tout est téléchargeable ici: http://yves.masur.microclub.ch/articles/</p>
<p>Ce n’est pas vraiment un article, mais il y a: le code source, les pages WEB, et deux documents au format pdf. « MXBOARD_decouverte » présente les différentes facette de cette plateforme, alors que « barette » est le cahier des charges – qui se transforme en cahier de réalisation petit à petit.</p>
<p>Yves Masur</p>

## Commentaires

### ymasur — 23 novembre 2009 à 22:16

<section class="comment-content comment">
<p>Et l’image représente l’envoi en série dans un 74HC595 d’un byte qui allumera des LEDs…</p>
 </section>

### ymasur — 16 décembre 2009 à 22:25

<section class="comment-content comment">
<p>Pour la comparaison des temps de commutation, j’ai fait une fonction qui rend un indice basé sur HH * 100 + MM. Pas facile: il faut indiquer au compilateur que chaque élément est un entier signé, sinon résultats farfelus! De plus, lorsque l’indice compare:<br/>
23:30 – 22:59 = 71, la minute après c’est:<br/>
23:30 – 23:00 = 30. Surprenant, mais utilisable pour tri et comparaisons.</p>
 </section>

### ymasur — 6 mars 2010 à 18:19

<section class="comment-content comment">
<p>La fonction de comparaison de temps et de « tracking » est désormais OK. Voir <a href="../../../../2010/03/06/horloge-et-table-de-commutation/index.html" rel="ugc">http://microclub.ch/2010/03/06/horloge-et-table-de-commutation/</a></p>
 </section>

### ymasur — 7 mars 2010 à 14:42

<section class="comment-content comment">
<p>La documentation est partagé ici:<br/>
<a href="http://docs.google.com/View?id=dd2z4nh9_1fbx246hr" rel="nofollow ugc">http://docs.google.com/View?id=dd2z4nh9_1fbx246hr</a></p>
 </section>

### ymasur — 17 mai 2010 à 19:59

<section class="comment-content comment">
<p>Laissé un peu de côté, j’ai repris l’affaire en main. Maintenant, l’horloge fait correctement la sélection de la dernière commutation, et de la prochaine. En fait, le problème venait de calculs de la fonction de comparaison – toujours le même bug du compilateur.<br/>
Lorsque le temps doit être ajusté, le calcul est:<br/>
if (dt1 &lt; 0) dt1 += 7 * 24 * 60;<br/>
Hormis un comportement aberrant de la sélection des lignes de commutation, j'avais des delta négatifs sur le module SBC, alors que la simulation avec CodeBloks donnait des résultats corrects (v. mon message du 6 mars 2010).<br/>
Le calcul est modifié par une macro ainsi:<br/>
#define M_WEEK ((int) 7 * 24 * 60)<br/>
if (dt1 &lt; 0) dt1 += M_WEEK;<br/>
Le truc, c'est bien sûr le (int) pour forcer le compilateur à calculer sur 16 bits!!</p>
 </section>

### ymasur — 17 mai 2010 à 20:12

<section class="comment-content comment">
<p>La partie WEB offre aussi ses surprises. Plein d’entrain, je profite de corriger un aspect esthétique de la DialogBox permettant d’ajuster l’horloge.<br/>
Rien que pour voir, j’utilise Adobe DreamWeaver CS5 (version d’essais 30 jours). Ce finaud m’a mis en forme le code, mais aussi l’a « corrigé » en changeant:<br/>
 …  par:<br/>
 …<br/>
Évidemment, le script sert à manipuler les données pour les transmettre en GET. Pas étonnant que ma DialogBox soit plus belle, mais… aussi inopérante!!</p>
 </section>

### ↳ Réponse — Yves Masur — 12 juin 2010 à 20:48

<section class="comment-content comment">
<p>Nom d’une pipe: le code n’est pas affiché: évidemment c’est un peu difficile de suivre ma prose 🙁</p>
 </section>

### Yves Masur — 12 juin 2010 à 20:43

<section class="comment-content comment">
<p>Maintenant, il s’agit de détecter le courant consommé dans 2 prises. Je vais essayer avec un opto et un pont + 1 ohm en série. A ce stade, je ne sais pas s’il faut faire une moyenne soft – étant donné que le courant sera pulsé à 100 Hz – ou filtrer par hard. Et a quoi ressemblera la dérive en température? Pas trop important, vu que le seuil à détecter est du genre 120W -&gt; 15 W.</p>
 </section>

### Yves Masur — 10 juillet 2010 à 20:10

<section class="comment-content comment">
<p><b>Piégé par le hard et le temps réel!!</b><br/>
Après de heures de recherche, je constate que je me suis fait avoir par le hard qui lit les 8 boutons et allume 8 LEDs. Les deux chips partagent le même fil de DATA, de CLOCK et de LATCH. Pour le data, il faut programmer la patte de lecteur en entrée pour lire les switch, en sortie pour les LEDs.<br/>
Cependant, dans mon design de code, je lis les switchs à 50 ms, tandis que les LEDs sont mise à jour à 250 ms, histoire de faire des clignotements avec une phase de 1/4 ou 3/4 de seconde.<br/>
Mais voilà… chaque fois que je lis les switchs, j’envoie leur config sur les LEDs!! Je suis donc obligé de les mettre au même rythme.</p>
 </section>

### ymasur — 30 juillet 2010 à 13:29

<section class="comment-content comment">
<p><b>version 08d utilisable!</b><br/>
Après un long travail de mise au point, les modules suivants sont opérationnels:<br/>
– commutation par table<br/>
– commutation par page WEB<br/>
– commutation par bouton-poussoir<br/>
– état des LEDs<br/>
– transitions (partiellement)<br/>
De plus, des parties de code sont rendues compatible avec CodeBlocks. Grâce à ceci, il est possible de modifier et tester ses modules avec rapidité sous Windows. Une fois au point, on peut le compiler sous l’IDE de MPLAB et le charger sur le MXBOARD. Les fichiers concernés ont une inclusion conditionnelle d’entête:<br/>
<code><br/>
#if defined(__GNUC__)<br/>
    #include "_gnu_.h"<br/>
#else<br/>
</code><br/>
Bien entendu, ce qui est relatif au hard est remplacé par un printf() exprimant où l’on en est…<br/>
A dispo sous: <a href="http://yves.masur.microclub.ch/articles/index.php" rel="nofollow ugc">http://yves.masur.microclub.ch/articles/index.php</a> et choisi [Mxboard].</p>
 </section>

### ymasur — 24 août 2010 à 19:52

<section class="comment-content comment">
<p>Voici une image du prototype:<br/>
<a href="http://yves.masur.microclub.ch/articles/Mxboard/barette_prises_2.jpg" rel="nofollow ugc">http://yves.masur.microclub.ch/articles/Mxboard/barette_prises_2.jpg</a>, ajoutée dans l’article initial.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
