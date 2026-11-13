---
title: "Barrette écologique – suivi 2"
date: "2010-08-27T08:26:43"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["barrette", "ecologie", "hardware", "pic"]
url: "/2010/08/27/barrette-ecologique-suivi-2/"
wordpress_id: 318
comment_count: 0
---
<p>Nous voici donc dans la partie <strong>hardware</strong>. Le <a href="/2009/11/23/barrette-ecologique-suivi/">logiciel</a> va continuer son évolution, mais dans des fonctions plus fines et des ajustements. Il s’agit donc de mettre le prototype sous forme de prints à réaliser, et de câblage à définir.</p>
<div>
<dl>
<dt><a href="/media/2010/08/barette_prises_2.jpg"><img alt="barette_prises_2" height="148" src="/media/2010/08/barette_prises_2.jpg?w=300" title="barette_prises_2" width="300"/></a></dt>
<dd>Prototype barrette</dd>
</dl>
</div>
<p>Un grand merci à Maurice Wulliens qui s’attelle à la réalisation des prints! Après discussion, nous avons décidé d’organiser le montage en minimisant les composants dans le boîtier de commande, lequel contiendra:</p>
<ul>
<li>Le module WEB Modtronic SBC65EC</li>
<li>Une alimentation 230 VAC – 9VDC</li>
<li>l’horloge temps réel</li>
<li>les entrés de commutateurs</li>
<li>les pilotages de LEDs</li>
<li>les pilotage des triacs</li>
</ul>
<p>Ces 3 derniers iront sur des connecteurs et seront reliés par câbles plats.</p>
<p>L’intégration dans une barrette du commerce, suffisamment démontable est prévue pour:</p>
<ul>
<li>2 à 3 prints pour le puissance, avec triacs et optos</li>
<li>1 print de mesure du courant</li>
<li>les boutons poussoirs</li>
<li>les LEDs</li>
</ul>
<p>Donc pas mal de choses à intégrer à la barrette. Le modèle retenu est vendu par la Migro. C’est un assemblage dans un rail en plastique, comportant un bouton d’allumage et 6 prises. les extrémités du profil sont fermées par deux flasques, facilement usinables pour nos besoins. En voici un aperçu:</p>
<p><a href="/media/2010/08/49_barrette_m_complete.jpg"><img alt="barrette Migro avant démontage" height="225" src="/media/2010/08/49_barrette_m_complete.jpg?w=300" title="barrette Migro avant démontage" width="300"/></a></p>
<figure aria-describedby="caption-attachment-321"><a href="/media/2010/08/51_barrette_m_couvercle_ouvert.jpg"><img alt="Barrette Migro couvercle ouvert" height="225" src="/media/2010/08/51_barrette_m_couvercle_ouvert.jpg?w=300" title="Barrette Migro couvercle ouvert" width="300"/></a><figcaption>couvercle ouvert</figcaption></figure>
<p>L’idée est donc de mettre des prints avec les triacs dans la barrette, de manière à diminuer la taille du module de commande, et aussi à ne pas y introduire de puissance. Suite au prochain épisode!</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
