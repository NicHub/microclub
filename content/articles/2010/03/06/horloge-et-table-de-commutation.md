---
title: "Horloge et table de commutation"
date: "2010-03-06T18:12:30"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["ecologie", "initiation", "pic", "programmation"]
url: "/2010/03/06/horloge-et-table-de-commutation/"
wordpress_id: 290
comment_count: 2
---
<p>Dans l’implémentation du code nécessaire au projet « barrette écologique », j’ai quelque peu séché sur le problème du suivi de la table de commutation. Celle-ci contient des données non-triée de temps, de jour(s) de la semaine et de la commutation à appliquer.</p>
<p>Comment trouver à coup sûr la dernière commutation et la prochaine à venir? Une fonction de différence de temps est nécessaire et rend un delta:</p>
<p><code>delta = ((int) prtc_line-&gt;hour - (int) DB_SystemClock.Time.hh) * 60 +<br/>
(int) prtc_line-&gt;minute - (int) DB_SystemClock.Time.mm;</code></p>
<p>Petit piège en langage C, les bytes à transformer en int, sinon-&gt; écrêtage à 255. Ensuite, nous parcourons régulièrement toutes les lignes du tableau de commutation.  Ainsi la valeur obsolète sera mise à jour. Celle-ci sera remplacée au fil des scan, si une ligne plus proche existe dans la table, parcourue de 0 à n.</p>
<p>Pour résoudre ce problème, je me suis contenté d’une fonction qui ne traite que 24 heures, laissant à plus tard son complément pour traiter des semaines. Le tableau ci-dessous montre la simplicité du raisonnement pour 24H:</p>
<ul>
<li>Le plus grand delta négatif est celui de la dernière commutation à 11h – l2;</li>
<li>Le plus petit delta positif, la prochaine commutation 13h – l3.</li>
</ul>
<p>Sur une semaine, ça ne fonctionne plus! En effet, admettons que nous sommes lundi (jour=1) et que les commutations sont seulement sur dimanche, jour=7? En admettant que notre fonction « delta » ajoute 24*60 par jour, il apparaît que la prochaine commutation est la première de dimanche, et la commutation en cours est la dernière de dimanche!! Tous des nombres positifs!! Notre fonction va donc trouver</p>
<ul>
<li>Le plus grand delta (mais pas négatif) sera celui de la dernière commutation à 14h – l4;</li>
<li>Le plus petit delta positif, la prochaine commutation 10h – l1.</li>
</ul>
<p>Faut-il une logique « intraday », travaillant avec +/- et une autre pour les jours à distance?</p>
<table border="1" cellpadding="5" cellspacing="0" width="100%">
<thead>
<tr valign="TOP">
<th width="45%">
<p lang="fr-CH">Commutation</p>
</th>
<th width="10%">
<p lang="fr-CH">l1</p>
</th>
<th width="10%">
<p lang="fr-CH">l2</p>
</th>
<th width="10%">
<p lang="fr-CH">time</p>
</th>
<th width="10%">
<p lang="fr-CH">l3</p>
</th>
<th width="15%">
<p lang="fr-CH">l4</p>
</th>
</tr>
</thead>
<tbody>
<tr valign="TOP">
<td width="45%">
<p lang="fr-CH">heure</p>
</td>
<td width="10%">
<p lang="fr-CH">10h00</p>
</td>
<td width="10%">
<p lang="fr-CH">11h00</p>
</td>
<td width="10%">
<p lang="fr-CH">’12:10</p>
</td>
<td width="10%">
<p lang="fr-CH">13h00</p>
</td>
<td width="15%">
<p lang="fr-CH">14h00</p>
</td>
</tr>
<tr valign="TOP">
<td width="45%">
<p lang="fr-CH">Delta</p>
</td>
<td width="10%">
<p lang="fr-CH">-130</p>
</td>
<td width="10%">
<p lang="fr-CH">-70</p>
</td>
<td width="10%">
<p lang="fr-CH">delta</p>
</td>
<td width="10%">
<p lang="fr-CH">+50</p>
</td>
<td width="15%">
<p lang="fr-CH">+110</p>
</td>
</tr>
<tr valign="TOP">
<td width="45%">
<p lang="fr-CH">Delta corrigé 1 semaine</p>
</td>
<td width="10%">
<p lang="fr-CH">+9950</p>
</td>
<td width="10%">
<p lang="fr-CH">+10010</p>
</td>
<td width="10%">
<p lang="fr-CH">–</p>
</td>
<td width="10%">
<p lang="fr-CH">+50</p>
</td>
<td width="15%">
<p lang="fr-CH">+110</p>
</td>
</tr>
</tbody>
</table>
<p lang="fr-CH">La solution est la suivante: lors de la recherche et comparaison, pour éviter les problèmes des jours répartis sur une semaine, on ajoute une correction de 7 jours * 24 heures * 60 minutes au temps de commutation de la ligne lue<strong> s’il est inférieur a 0</strong>. ce calcul tient compte du fait que les écarts sont cycliques sur une semaine de 7 jours. De ce fait, le test de comparaison de temps se fait toujours sur des nombres strictement positifs, et fonctionne pour le jour courant et … les autres de la semaine.</p>
<p lang="fr-CH">Grâce à Code::Blocks, j’ai pu tester et valider mes fonctions efficacement, car modifier + charger le binaire dans le module PIC est bien long… voir: <a href="/2009/11/23/barrette-ecologique-suivi" target="_self" title="Barrette écologique">http://microclub.ch/2009/11/23/barrette-ecologique-suivi</a></p>
<p lang="fr-CH">Yves Masur</p>

## Commentaires

### Laurent — 22 janvier 2011 à 19:24

<section class="comment-content comment">
<p>Intéressant, j’ai rencontré le même problème sur un projet de gestion d’horaire de trains.<br/>
Je l’ai résolu de la manière suivante :<br/>
Je place les dates (et les heures) de commutations dans un tableau.<br/>
Lorsque j’insére une nouvelle commutation, je trie mon tableau dans l’ordre croissant et ajuste l’index de la prochaine commutation.<br/>
Ainsi la présentation des diverses dates de commutations sont oordonnées dans l’ordre croissant, plus faciles à lire, et l’index de la prochaine commutation s’incrémente en fonction du temps écoulé.<br/>
Si une commutation est indépendante de la date, par exemple tous les mardi à 7h45, mon tableau contient un flag « AutoRepete »; lors du traitement du tableau (lors d’une commutation effectuée) une fonction rajoute la date répétitive.</p>
<p>Par cette méthode, je me suis beaucoup simplifé le traitement des commutations.</p>
 </section>

### ymasur — 23 janvier 2011 à 15:16

<section class="comment-content comment">
<p>En effet c’est la meilleure technique… Si la mémoire RAM à disposition est suffisante. Ce qui n’est pas le cas dans ce projet: les informations de commutation sont placées dans une structure en EEPROM. Il n’y en a que 3 en mémoire: celle en travail (édition), l’actuelle et la future.<br/>
Les algorithmes de tri sont donc plus complexes. L’article ci-dessus ne rend pas non plus toute la problématique.<br/>
Par exemple, avec la solution ci-dessus et les paramètres suivants:<br/>
Tables avec commutations à<br/>
– 00.15 et 16:00 Lu-Sa<br/>
– 00:30 Dimanche<br/>
Le mercredi à 23:50, le recalcul trouve Last=00:30 et Next=00:15, alors qu’on s’attendait à 00:15.<br/>
Le BUG n°4 de la présentation – c’est lui! Fait mal à la tête. Il faut le voir sur papier. Je mettrai les slides sur le site quand j’aurai trouvé la technique.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
