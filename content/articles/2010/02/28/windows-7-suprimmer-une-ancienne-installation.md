---
title: "Windows 7 – suprimmer une ancienne installation"
date: "2010-02-28T11:36:03"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["systeme-dexploitation", "windows"]
url: "/2010/02/28/windows-7-suprimmer-une-ancienne-installation/"
wordpress_id: 277
comment_count: 3
---
<p>Sur une partition restait une ancienne installation de Windows 7. Impossible de la supprimer, même comme administrateur – c’est un comble, non? Si je pouvais changer son nom, pas moyen de retrouver les environ 8 Go de ce répertoire. Bon, formater la partition est toujours possible, mais y a-t-il plus simple? Ou plus élégant? Un essais ce jour m’indiquait qu’il fallait une autorisation « <strong>Trustedinstaller</strong>« , comme si j’étais un installateur de pacotille!</p>
<p>La solution est de s’approprier les droits pour ce faire. Soit: clic droit, Propriété, onglet Sécurité, bouton [Avancé] (sinon vous pouvez voir les droits, mais rien changer), Modifier les autorisations et une nouvelle boîte de dialogue vient.</p>
<figure aria-describedby="caption-attachment-278"><a href="/media/2010/02/autorisations.jpg"><img alt="autorisations" height="238" src="/media/2010/02/autorisations.jpg?w=300" title="autorisations" width="300"/></a><figcaption>autorisations</figcaption></figure>
<p>Il s’agit ensuite de s’approprier les autorisations, en cliquant sur le groupe « Utilisateurs » et allant dans l’onglet « Autorisation effectives ».</p>
<p>Comme prévu, les droits effectifs sont des coches vides…</p>
<p>Aller sur [Sélectionner] et une nouvelle boîte s’affiche: « Sélectionner un utilisateur ou un groupe », avec un champ « Entrer le nom de l’objet à sélectionner ».</p>
<p>Hé bien, l’objet c’est le nom de l’utilisateur que vous êtes, probablement sur le PC en cours. Dans mon cas, « VOSTRO\Yves » (VOSTRO est le nom du PC).</p>
<p>Si le nom est vérifié, il se souligne. Mais on ne peut toujours rien changer… Revenir à l’onglet « Propriétaire ». Maintenant, il y a 2 nouvelles lignes, « Administrateurs » et « VOSTRO\Yves » .</p>
<p>Ensuite, l’appropriation est un jeu d’enfant; on coche [x] remplacer le propriétaire des sous conteneurs et objets!</p>
<figure aria-describedby="caption-attachment-280"><a href="/media/2010/02/remplacer_proprio.jpg"><img alt="remplacer_proprio" height="134" src="/media/2010/02/remplacer_proprio.jpg?w=300" title="remplacer_proprio" width="300"/></a><figcaption>remplacer_proprio</figcaption></figure>
<p>Comme c’est (enfin… c’était) le répertoire système, une ou deux confirmations sont à cliquer;  puis en tant que proprio, rien ne nous empêche d’éliminer tous ces fichiers inutiles.</p>
<p>Remarquez au passage que le disque est « D: » !</p>
<p>Yves Masur</p>
<p><img alt="" src="/Users/Yves/Documents/temp/autorisations.jpg"/></p>

## Commentaires

### fennec — 1 octobre 2011 à 13:00

<section class="comment-content comment">
<p>Bonjour,<br/>
Merci pour l’astuce mais pour moi ça n’a pas fonctionné.<br/>
L’attribution des droits fonctionne, mais au moment de la suppression il me disait « Vous avez besoins des droits de Mon-PC\fennec » alors que c’est précisément l’utilisateur sur lequel j’étais connecté !<br/>
J’ai essayé de donner les droits à Administrateur, rien à faire !</p>
<p>En renommant le dossier « Windows » en « Windows.old » et en lançant un nettoyage du disque, il m’a proposé de « supprimer une ancienne installation de Windows »<br/>
Et là ça fonctionne</p>
 </section>

### ↳ Réponse — Alex — 17 janvier 2013 à 14:11

<section class="comment-content comment">
<p>Je rejoins fennec. J’ai eu beau modifier les autorisations, il me demandait toujours qu’il ne voulait pas supprimer les fichiers parce qu’il lui fallait ma propre autorisation…<br/>
On renomme le fichier en windows.old, un coup de nettoyage disque et c’est fini.</p>
 </section>

### marcNice — 23 juillet 2013 à 15:38

<section class="comment-content comment">
<p>merci je ne m’en sortais pas!!</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
