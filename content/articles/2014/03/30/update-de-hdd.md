---
title: "Update de HDD"
date: "2014-03-30T19:51:07"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["disque-dur", "hardware", "lien-symbolique", "systeme-dexploitation", "windows"]
url: "/2014/03/30/update-de-hdd/"
wordpress_id: 1442
comment_count: 0
---
<p>Le disque dur du PC commence à se faire un peu petit? Plus des 3/4 de sa capacité remplie de musique, de photos, de films? Voici une technique ultra simple et… qui a fonctionné du 1er coup. Assez rare pour être mentionnée!</p>
<p>En fait, c’est simple pour autant qu’on aie pris quelques précautions en amont. Il faut que les données de ce type (soit des DATA, différents des programmes) aient bien été séparément enregistrées. Pour ma part, sur le disque C: qui est un SSD figurent le système, les programmes (<strong>C:\Program Files</strong>), les données de faible taille. Le profil (<strong>C:\user\Yves\Documents</strong>) est bien sûr l’objet de backup réguliers, et avec Windows 7, ça marche plutôt bien. Le backup copie les fichiers pointés par les liens – donc inutile de lancer un second backup de D: qui contient réellement les fichiers. Pour plus de détails sur l’organisation des données, voir un précédent article ici, qui précise tout ça: <a href="/2012/08/06/installer-un-disque-ssd-et-re-installer-w7-et-les-programmes/ " target="_blank" title="Installer un SSD">http://microclub.ch/2012/08/06/installer-un-disque-ssd-et-re-installer-w7-et-les-programmes/ </a>.</p>
<p>Avec en tête l’idée de toujours déposer les <strong>données volumineuses</strong> sur une autre unité. On précise par des <strong>liens symboliques</strong> (commande MKLINK, en administrateur) que les images et les sons sont déposés sur la seconde unité physique. Justement, celle que l’on va remplacer, par les étapes suivantes:</p>
<ul>
<li>connecter le nouveau HDD au PC</li>
<li>copier les données</li>
<li>échanger les disques</li>
<li>vérifier que les liens symboliques fonctionnent toujours…</li>
</ul>
<h3>Station d’accueil pour HDD</h3>
<p>La connexion est faite par un dispositif que j’ai trouvé chez Conrad: <a href="http://www.conrad.ch/ce/fr/product/971937/" target="_blank" title="Lien Conrad"><code>http://www.conrad.ch/ce/fr/product/971937/</code></a></p>
<p><img alt="" height="360" src="http://www.conrad.fr/medias/global/ce/9000_9999/9700/9710/9719/971937_AB_00_FB.EPS_1000.jpg" width="360"/></p>
<p>Ce bidule permet de connecter un disque dur 3’1/2 ou 2’1/2 via USB sur le PC. Une alimentation et un bouton permettent son enclenchement; le PC le voit comme <em>un périphérique de stockage de masse</em>. Ce qu’il nous faut, quoi.</p>
<h3>Copier les données</h3>
<p>Après l’inévitable formatage (NTFS, please), pour lequel le nouveau HDD via la station d’accueil a pris la lettre F:, il faut faire attention à <strong>tout</strong> copier du disque D: à F:, si l’on veut que les liens symboliques fonctionnent. Tout, c’est les droits, les fichiers cachés, les ACL, les liens symboliques (et non les fichiers sous-jacents).</p>
<p>La commande via CMD.EXE lancé en admin, est: <strong>xcopy d:*.* /S /H /O /B  f:</strong></p>
<p>ça prend effectivement un peu de temps…</p>
<h3>Échange des disques</h3>
<p>Ensuite, démonter le PC, enlever l’ancien D: et y placer le nouveau F:. Remontage, démarrage… Windows réfléchi plus longuement que d’habitude… Mais démarre normalement. Mais voilà: le nouveau disque a conservé la lettre ‘F’! Un clic sur Ordinateur – Gérer – Stockage – Modifier la lettre de lecteur et les chemins d’accès; on corrige en D: et un petit CHKDSK. Puis on vérifie…</p>
<p>Tout fonctionne! C’est pas nickel, tout ça?</p>
<p>Yves Masur (3/2014)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
