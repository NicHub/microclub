---
title: "Echanger le SSD sur PC portable"
date: "2019-10-27T20:04:05"
lastmod: "2019-10-27T20:04:06"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: []
url: "/2019/10/27/echanger-le-ssd-sur-pc-portable/"
wordpress_id: 4663
comment_count: 2
---
<h2>Situation de départ</h2>
<p>Un SSD de 120 Go devient trop petit, sur un PC portable – en l’occurrence un PC HP Pavillion X360 13-V140NZ – le SSD d’origine de 120 Go devient trop petit, et je veux le remplacer par un SSD de 1 To. Soit 8 fois plus, ce qui donne de l’air.</p>
<p>Problème : le HDD 120Go contient Win10, et une partition avec les outils HP de diagnostic… Il s’agit de conserver la licence Win10. Il n’y a pas de place physique, dans ce genre de petits PC pour mettre les deux SSD dans la même machine ; et le slot est un connecteur M.2.</p>
<p>Allure du SSD d’origine:</p>
<p><img height="319" src="/media/2019/10/word-image.png" width="1024"/></p>
<p>Même si c’est indiqué de le remplacer par une pièce HP, je prends le risque d’en mettre une version moins chère, fabriqué par Western Digital. Que voici : <a href="https://www.digitec.ch/fr/s1/product/wd-blue-3d-nand-1000go-m2-2280-ssd-6408461">https://www.digitec.ch/fr/s1/product/wd-blue-3d-nand-1000go-m2-2280-ssd-6408461</a> à 136.-</p>
<h2>Opérations à conduire pour l’échange</h2>
<ol>
<li>Contrôler le SSD 1</li>
<li>Connecter le nouveau SSD (nommé par la suite SSD 2) sur le PC</li>
<li>Copier les partitions bit à bit de SSD 1 à SSD 2</li>
<li>Étendre la partition Windows selon la place disponible</li>
</ol>
<h2>Contrôle et préparation</h2>
<p>Le contrôle est fait par : Explorateur de fichier / click droit sur C : / propriétés / onglet « Outils » -&gt; Vérifier. Bien que ce ne soit pas indispensable, on peut faire un peu d’ordre sur le disque, par l’onglet « Nettoyage ». Nettoyer la registry, avec CCLeaner par exemple, également est une bonne chose. Une fois les données bien préparées, on peut envisager la suite.</p>
<h2>Connecter le SSD 2</h2>
<p>Il faut que le disque destination soit vu par la machine. Via l’USB, je connecte un lecteur externe. Dans mon cas ce lecteur est prévu pour disque SATA 5 ¼ ou 3 ½ , mais pas pour M.2. Heureusement, on trouve des adapteurs. Exemple, chez Digitec :</p>
<p><a href="https://www.digitec.ch/fr/s1/product/delock-m2-oder-msata-zu-sata-adapter-disques-durs-accessoires-6292841">https://www.digitec.ch/fr/s1/product/delock-m2-oder-msata-zu-sata-adapter-disques-durs-accessoires-6292841</a> . Bien sûr, cela renchérit l’opération… Si quelqu’un en a besoin, je le lui prête volontiers !</p>
<p>Le M.2 est monté dans cet adapteur, puis dans le lecteur externe et connecté via l’USB au PC.</p>
<p>Vision des partitions, avec l’utilitaire Win10 :</p>
<p>Diskmgmt.msc</p>
<p><img height="906" src="/media/2019/10/word-image-1.png" width="1152"/></p>
<p>Le disque SSD 2 – sur l’image, « Disque 1 » – est bien vu par Win10, avec 931.5 Go, non alloué. Mais pour la suite, comment procéder ?</p>
<p>Une recherche Internet montre une jolie quantité de programmes pour copier ou redimensionner des partitions. Pour faire le job, le programme doit pouvoir booter séparément de Windows, idéalement sur clé USB ; ou avoir le pilote qui permet de farfouiller les partitions à partir de l’OS.</p>
<p>Après quelques essais (et beaucoup de redémarrages et de déconvenues), je sélectionne Macrium Reflect 7, 64 bits : <a href="https://www.macrium.com/reflectfree">https://www.macrium.com/reflectfree</a></p>
<p>Qui est gratuit, du moins pour le privé et l’usage que je souhaite faire. Installé sur une clé USB libre. Il faut bien sûr se battre avec le BIOS du PC qui doit accepter de démarrer sur… autre chose que le Win10 installé ! La notion de « démarrage UEFI » s’interpose. Selon Wikipédia :</p>
<p><em>L’UEFI offre quelques avantages sur le BIOS : fonctionnalités réseau en standard, interface graphique de bonne résolution, gestion intégrée d’installations multiples de systèmes d’exploitation et affranchissement de la limite des disques à 2,2 To.</em></p>
<p><em>Le BIOS, écrit en assembleur, limitait les modifications et/ou remplacements, gage de sûreté de fonctionnement et de sécurité. L’UEFI est écrit en C, ce qui rend sa maintenance plus souple et reste acceptable en raison des coûts décroissants de la mémoire. Développé pour assurer l’indépendance entre système d’exploitation et plate-forme matérielle sur laquelle il fonctionne, l’UEFI est disponible sur les plates-formes Itanium (IA-64), x86 (32 et 64 bits) et ARM.</em></p>
<p>Finalement, on arrive à booter sur une clé USB, et Macrium Reflect Free se monte.</p>
<p><img height="602" src="/media/2019/10/word-image-2.png" width="776"/></p>
<p>Joli avantage, il est possible de déplacer ou retailler les partitions par curseurs, contrairement aux outils (certes gratuits) basés sur Linux.</p>
<p>Une fois démarré, on demande les copies des partitions sources, puis l’étirement de C: au max de la nouvelle capacité du disque destination.</p>
<p><img height="374" src="/media/2019/10/word-image-3.png" width="668"/></p>
<p>Ça devrait donner ceci :</p>
<p><img height="839" src="/media/2019/10/word-image.jpeg" width="1061"/></p>
<p>Mais voilà… pas possible d’étirer la partition C : comme désiré !</p>
<p><img height="219" src="/media/2019/10/word-image-1.jpeg" width="542"/></p>
<p>Pas très explicite, l’erreur en question :</p>
<p><img height="234" src="/media/2019/10/word-image-2.jpeg" width="621"/></p>
<p>D : est le lecteur de la clé USB, sur laquelle le soft tourne. On voit que Macrium est écrit en Pascal.</p>
<p>Après plusieurs essais (diverses tailles d’étirement), je renonce à faire ces opérations d’un bloc ; mais les reprend une à une, en rebootant à chaque fois. Et là, c’est OK.</p>
<p><img height="1080" src="/media/2019/10/word-image-3.jpeg" width="1542"/></p>
<p>C’est tout bon : le SSD est désormais de 930 Go. Windows est reconnu, la partition augmentée.</p>
<p>YM (10/2019)</p>

## Commentaires

### franic — 22 décembre 2019 à 10:33

<section class="comment-content comment">
<p>J’ai fait la même chose que toi, mais j’ai utilisé un logiciel open source Clonezilla.<br/>
J’ai préparé une clé USB « Clonezilla » qui boot avec linux.<br/>
J’ai ensuite branché mon SSD avec un adaptateur USB et j’ai lancé le clonage.<br/>
Il m’a créé automatiquement toutes les partitions windows 10, recovery, …<br/>
Tout s’est déroulé finalement très simplement alors que cette opération semble assez compliquée; j’ai suivi ce tutoriel : <a href="https://www.malekal.com/clonezilla-tutoriel-clonage-de-disque/" rel="nofollow ugc">https://www.malekal.com/clonezilla-tutoriel-clonage-de-disque/</a></p>
 </section>

### ↳ Réponse — Yves Masur — 22 décembre 2019 à 10:57

<section class="comment-content comment">
<p>Effectivement, c’est plus simple. Et dans les 2 cas, il faut créer l’USB bootable. Si Macrium ne présentait pas cette erreur à l’extension de la partition, on arriverai au même nombre d’opérations.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
