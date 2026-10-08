---
title: "Projet « Barrette » livrable!"
date: "2011-03-25T21:55:00"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["barrette", "embarque", "hardware", "programmation", "web"]
url: "/2011/03/25/projet-barrette-livrable/"
wordpress_id: 457
comment_count: 4
---
<p>Bonjour tous,</p>
<p>Une bonne nouvelle pour les bricoleurs qui veulent économiser l’énergie! Plutôt que de pédaler sur votre génératrice, la fameuse <strong>barrette écologique du MICROCLUB</strong> est une solution intéressante. Après des mois de développement et de mise au point tant électronique, soft que mécanique, la voici. J’en profite pour remercier très fort mes collègues Maurice Wuillens qui a contribué à la réalisation électronique, et Laurent Francey à la mécanique. Jugez plutôt des caractéristiques du produit:</p>
<ul>
<li>Pilotage par page WEB personnalisable</li>
<li>Donc connectée sur le LAN</li>
<li>Peut enclencher 6 prises 230 VAC séparément</li>
<li>Boutons pour commande manuelle</li>
<li>LEDs de contrôle</li>
<li>Horloge RTC maintenue par pile</li>
<li>Table de 20 ordres d’enclenchement/déclenchement</li>
<li>Maintient (sélectif) par activité LAN</li>
<li>Prise maître, maintient des esclaves (sélectionnés)</li>
<li>Dimensions env. L=62 cm, l=10 cm, h=4 cm</li>
</ul>
<p>La consommation propre, toutes les prises déclenchées est réduite à 1,1 VA! Le kit est basé sur une barrette vendue par la Migro, à laquelle nous rajoutons un bloc constitué d’un CPU PIC 18F. Bien entendu, la partie basse tension est isolée galvaniquement du secteur. Un élégant print, glissé dans la barrette contient les triacs optocouplés permettant la commutation électrique. Pas de relais qui tombent en panne!</p>
<p>Le MICROCLUB vous propose de la monter en kit, pour la somme (pas très modique, c’est vrai, mais c’est le prix coutant de tout ce matériel) de 280.- Mais c’est un produit génial et sans compromis. Pour ceux que le montage rebuterait ou n’est pas évident, un atelier commun sera proposé. Qu’on se le dise! Vous avez un Wi-Fi, une imprimante, un écran, des chargeurs, une lampe de bureau, un disque de sauvegarde… C’est idéal pour commuter tous ce petit monde et éviter la consommation due à l’énergie grise. Désormais, via l’adresse <strong>http://prises</strong> ou un autre nom NetBios que vous aurez choisi sur votre réseau, vous commandez vos consommateurs! Le module accepte les adresse fixes ou le DHCP. Génial, non?</p>
<figure aria-describedby="caption-attachment-458"><a href="/media/2011/03/CMB11-commande_html_2313acf4.jpg"><img alt="CMB11" height="85" src="/media/2011/03/CMB11-commande_html_2313acf4-300x85.jpg" title="CMB11" width="300"/></a><figcaption>CBM11 - Barrette Microclub</figcaption></figure>
<p>Les intéressés peuvent cliquer sur la fiche pdf ci-dessous, et adresser leur commande à notre secrétaire, carlos[at]microclub.ch</p>
<p><a href="/media/2011/03/CMB11-commande.pdf">CMB11-commande</a>.pdf</p>
<p>Limitation: les 9 premiers seront servi rapidement; si plus d’intérêt nous devrons commander des prints…</p>
<p>Yves Masur (resp. du projet)</p>

## Commentaires

### Jacques — 10 mai 2011 à 15:55

<section class="comment-content comment">
<p>Salut les développeurs,<br/>
Avez-vous des informations concernant les délais de livraison et l’organisation de l’atelier de montage ?<br/>
Amitiés à tous</p>
<p>J. Burnand</p>
 </section>

### Yves Masur — 10 mai 2011 à 18:23

<section class="comment-content comment">
<p>Nous laissons le temps aux éventuels intéressés du festival de robot de passer commande et nous lançons les commandes de matériel. Ensuite, nous programmerons l’atelier de montage!</p>
 </section>

### Yves Masur — 26 juin 2011 à 07:10

<section class="comment-content comment">
<p>Premier atelier fait le samedi 25.6. La mécanique est quasi faite – une grand merci à Laurent pour la mise à disposition de son atelier et son aide précieuse, ainsi que pour pallier aux quelques composant qui manquaient.<br/>
Les montages sont fort avancé: câbles préparés et sertis, print « Power » quasi monté. Il faut encore y rapporter le bloc d’alimentation et l’optocoupleur de mesure qui manquait.</p>
 </section>

### ymasur — 30 septembre 2012 à 19:42

<section class="comment-content comment">
<p>Une nouvelle version est disponible. Elle inclut le réglage du seuil de courant de la prise P6-Maître. Le code et les pages WEB modifiées sont disponible sur mon site, sous l’URL <a href="http://www.yvesmasur.ch/articles/index.php" rel="nofollow">ici</a>. Pour mettre à jour, suivez cette procédure:<br/>
– Pomper le soft barrette.zip, déballez-le.<br/>
– désactivez le pare-feux Windows si besoin<br/>
– Lancez NetLoader de Modtronix (aussi disponible sur mon site)<br/>
– entrez l’IP de la barrette, les chemins des soft, comme ci-dessous<br/>
– chargez le code \Pic\Soft\barrette\src\out\barrette_11.hex<br/>
– chargez les pages \Pic\Soft\barrette\webpages\default.img<br/>
Si tout se passe correctement, tous vos paramètres sont conservés. Réactivez le pare-feux, si vous y tenez.<br/>
Le courant est au départ à 255 mA; a vous de l’ajuster! Au démarrage, il est forcé à 10 mA si une valeur inférieur est donnée.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
