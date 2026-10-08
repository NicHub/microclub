---
title: "GIt et GitHub – expériences et résultats"
date: "2018-02-25T16:05:12"
lastmod: "2018-02-25T16:16:20"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["git", "github", "initiation", "programmation", "software"]
url: "/2018/02/25/git-et-github-experiences-et-resultats/"
wordpress_id: 3768
comment_count: 1
---
<p>Suite à la conférence de Nicolas, voici quelques expériences avec Git et plus particulièrement GitHub.</p>
<p>On va respectivement:</p>
<ul>
<li>Mettre un répertoire existant dans Git;</li>
<li>Utiliser l’application <strong>Desktop</strong>;</li>
<li>Travailler avec 2 PCs sur un répertoire partagé;</li>
<li>Synchroniser deux PCs avec <strong>git-gui,</strong> et modifier et re-synchroniser les répertoires</li>
</ul>
<h1><strong>Répertoire existant -&gt;GIT</strong></h1>
<p>Le but est de déposer un code existant de son PC sur GitHub, de manière à pouvoir le maintenir. Et surtout de déjouer quelques pièges, car devant la complexité de GitHub, on titube (désolé, je n’ai pas pu me retenir).</p>
<p>Exemple: le contenu du répertoire « main_lpc » (c’est du code Arduino). Aller dans le répertoire :</p>
<p>C:\Programs\Git&gt;<strong>cd c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc</strong></p>
<p>Initialiser:<br/>
c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc&gt;<strong>git init</strong></p>
<p>Initialized empty Git repository in c:/Users/Masur/OneDrive/Documents/Arduino/Soft/main_lpc/.git/</p>
<p>Ici, attention à résister à la tentation à donner le nom de répertoire « lpc_main », qui serait créé. Pousser tous les fichiers:</p>
<p>c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc&gt;<strong>git add .</strong></p>
<p>warning: LF will be replaced by CRLF in const_def.h.<br/>
The file will have its original line endings in your working directory.</p>
<p>Cet avertissement vaut pour tous les fichiers *.ino, *.h ou texte<br/>
Pousser les fichiers dans le répertoire Git local:</p>
<p>c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc&gt;<strong>git commit -m « version du 26.07.2015 »</strong></p>
<p>[master (root-commit) f1a0ba2] version du 26.07.2015<br/>
9 files changed, 806 insertions(+)<br/>
create mode 100644 const_def.h  … ect pour les 9 fichiers.</p>
<p>Ensuite, toutes les commandes <strong>git remote</strong> échouent. Via le WEB, création du dépôt distant (GitHub):</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-13.png" height="1023" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor.png" width="1374"/></p>
<p>Essai avec l’appli <strong>Desktop</strong>, pour pousser les fichiers sur GitHub. Choix du répertoire, renseigné dans les deux champs: repository et local :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-14.png" height="994" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-1.png" width="1443"/></p>
<p>Mauvaise idée… un sous répertoire du même nom est créé!</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-15.png" height="477" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-2.png" width="1106"/></p>
<p>Delete du répertoire …/main_lpc/<strong>main_lpc</strong></p>
<p>Sélection avec Desktop, puis Publish (but, pousser les fichiers sur GIT-HUB)</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-16.png" height="996" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-3.png" width="1445"/></p>
<p>Le dépôt précédemment créé par le WEB gêne.</p>
<p><strong>Solution</strong> : delete du dépôt sur GitHub, puis recommencer l’opération « Publish », qui réussit.</p>
<h1><strong>Piège du répertoire partagé</strong></h1>
<p>Vous avez peut-être remarqué que j’utilise OneDrive pour stocker mes fichiers. Ceci me prémuni contre une panne de HDD et me permet de partager le code sur plusieurs PC. Par contre, si les répertoires ne sont pas strictement identiques entre les 2 PCs, impossible d’utiliser Git sur le second! On obtient:</p>
<p>~\Documents\Arduino\Soft\Blink\blink2 [master ≡ +0 ~0 -1 ~]&gt; git push<br/>
To https://github.com/ymasur/blink2<br/>
! [rejected] master -&gt; master (fetch first)<br/>
error: failed to push some refs to ‘https://github.com/ymasur/blink2’<br/>
hint: Updates were rejected because the remote contains work that you do<br/>
hint: not have locally. This is usually caused by another repository pushing<br/>
hint: to the same ref. You may want to first integrate the remote changes</p>
<p>Dommage…</p>
<h2><strong>Synchro de GitHub, de PC1 et de PC2</strong></h2>
<p>Situation: on développe sur le  PC1, mais on aimerait poursuivre sur PC2, comme si 2 utilisateurs travaillent à tour de rôle. Ici, on utilise Git-Gui.exe, que l’on peut lancer depuis la ligne de commande par: git-gui.</p>
<p>Le code – en l’occurrence blink2 Arduino – est déjà déposé sur GitHub.</p>
<h2><strong>Git-gui (sur PC2)</strong></h2>
<p>Etape 1: Clone. Le répertoire local ne doit <strong>pas préexister</strong>. Charger localement depuis GitHub :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-17.png" height="330" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-4.png" width="776"/></p>
<h2><strong>Ajout et modification de fichier</strong></h2>
<p>Le fichier toto.txt (complètement bidon) est ajouté. Rescan :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-18.png" height="779" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-5.png" width="1344"/></p>
<p>Pour la bonne forme, je modifie le commentaire de blink2.ino. Une fois les modifs terminées, cliquer le fichier pour le passer à Staged…</p>
<p>Puis [Commit] pour enregistrer <em>localement</em> la(les) différence(s)</p>
<h2><strong>Nouvelle version sur GitHub</strong></h2>
<p>La modif est seulement locale. On la met sur GitHub avec [Push] :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-19.png" height="846" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-6.png" width="818"/></p>
<p>Vérification sur GitHub, via le WEB :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-20.png" height="894" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-7.png" width="1299"/></p>
<p>Le fichier toto.txt est bien ajouté; et blink2.ino touché.</p>
<h1><strong>Modif avec un répertoire cloné sur PC1</strong></h1>
<h2><strong>Contrôle des changements</strong></h2>
<p>Repository -&gt; Visualize master’s history</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-21.png" height="894" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-8.png" width="1048"/></p>
<h2><strong>Modifications par PC1</strong></h2>
<p>Delete de toto.txt ; modif de blink2.ino (on remodifie le commentaire)</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-22.png" height="635" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-9.png" width="1127"/></p>
<p>Commit et push de cette version :</p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-23.png" height="371" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-10.png" width="853"/></p>
<h2><strong>Synchro sur PC2</strong></h2>
<p><strong>Obtenir une réplication correcte (sans tout cloner)</strong></p>
<p>Pour mémoire, on a supprimé le fichier toto.txt. Etape 1, synchro du dépôt local de PC2: <strong>git fetch</strong></p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-24.png" height="415" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-11.png" width="1022"/></p>
<p>Etape 2: synchro répertoire de travail : <strong>git merge</strong></p>
<p><img alt="http://microclub.ch/wp-content/uploads/2017/11/word-image-25.png" height="415" src="/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-12.png" width="1022"/></p>
<p>Le répertoire local est à jour sur le PC2.</p>
<p>Yves Masur (11/2017)</p>
<p> </p>

## Commentaires

### Nicolas Jeanmonod — 4 mars 2018 à 11:55

<section class="comment-content comment">
<p>Je vois que tu t’en es super bien sorti (donc pas de titubation comme tu dis sur FB ;-). Perso je n’utilise quasiment que la ligne de commande parce que les GUI sont tellement nombreux que je ne savais plus quoi choisir et finalement ils me troublent plus qu’ils ne m’aident.</p>
<p>La grande majorité du temps, j’utilise Git sans GitHub. L’idée est simplement de gérer l’historique de mes projets et de pouvoir revenir en arrière si nécessaire. Ça m’évite de faire des copies de mes fichiers et de me retrouver avec une multitude de versions : fichier_v1.txt, fichier_v2.txt… C’est particulièrement utile en programmation pour tester une idée dont je ne suis pas sûr qu’elle va fonctionner. Ça me permet de rapidement revenir en arrière et ça me permet aussi de vérifier que je n’ai fait que les modifications que je voulais entre deux commits.</p>
<p>Avec GitHub on peut créer un site web gratuitement. Je pourrais vous montrer la procédure le 20 avril 2018 si ça intéresse les membres.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
