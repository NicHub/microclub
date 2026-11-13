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

Suite à la conférence de Nicolas, voici quelques expériences avec Git et plus particulièrement GitHub.

On va respectivement:

-   Mettre un répertoire existant dans Git;
-   Utiliser l’application **Desktop**;
-   Travailler avec 2 PCs sur un répertoire partagé;
-   Synchroniser deux PCs avec **git-gui,** et modifier et re-synchroniser les répertoires

## Répertoire existant -> GIT

Le but est de déposer un code existant de son PC sur GitHub, de manière à pouvoir le maintenir. Et surtout de déjouer quelques pièges, car devant la complexité de GitHub, on titube (désolé, je n’ai pas pu me retenir).

Exemple: le contenu du répertoire « main_lpc » (c’est du code Arduino). Aller dans le répertoire :

C:\Programs\Git\>**cd c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc**

Initialiser:\
c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc\>**git init**

Initialized empty Git repository in c:/Users/Masur/OneDrive/Documents/Arduino/Soft/main_lpc/.git/

Ici, attention à résister à la tentation à donner le nom de répertoire « lpc_main », qui serait créé. Pousser tous les fichiers:

c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc\>**git add .**

warning: LF will be replaced by CRLF in const_def.h.\
The file will have its original line endings in your working directory.

Cet avertissement vaut pour tous les fichiers \*.ino, \*.h ou texte\
Pousser les fichiers dans le répertoire Git local:

c:\Users\Masur\OneDrive\Documents\Arduino\Soft\main_lpc\>**git commit -m « version du 26.07.2015 »**

\[master (root-commit) f1a0ba2\] version du 26.07.2015\
9 files changed, 806 insertions(+)\
create mode 100644 const_def.h  … ect pour les 9 fichiers.

Ensuite, toutes les commandes **git remote** échouent. Via le WEB, création du dépôt distant (GitHub):

![http://microclub.ch/wp-content/uploads/2017/11/word-image-13.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor.png)

Essai avec l’appli **Desktop**, pour pousser les fichiers sur GitHub. Choix du répertoire, renseigné dans les deux champs: repository et local :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-14.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-1.png)

Mauvaise idée… un sous répertoire du même nom est créé!

![http://microclub.ch/wp-content/uploads/2017/11/word-image-15.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-2.png)

Delete du répertoire …/main_lpc/**main_lpc**

Sélection avec Desktop, puis Publish (but, pousser les fichiers sur GIT-HUB)

![http://microclub.ch/wp-content/uploads/2017/11/word-image-16.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-3.png)

Le dépôt précédemment créé par le WEB gêne.

**Solution** : delete du dépôt sur GitHub, puis recommencer l’opération « Publish », qui réussit.

## **Piège du répertoire partagé**

Vous avez peut-être remarqué que j’utilise OneDrive pour stocker mes fichiers. Ceci me prémuni contre une panne de HDD et me permet de partager le code sur plusieurs PC. Par contre, si les répertoires ne sont pas strictement identiques entre les 2 PCs, impossible d’utiliser Git sur le second! On obtient:

~\Documents\Arduino\Soft\Blink\blink2 \[master ≡ +0 ~0 -1 ~\]\> git push\
To <https://github.com/ymasur/blink2\>
! \[rejected\] master -\> master (fetch first)\
error: failed to push some refs to ‘<https://github.com/ymasur/blink2’\>
hint: Updates were rejected because the remote contains work that you do\
hint: not have locally. This is usually caused by another repository pushing\
hint: to the same ref. You may want to first integrate the remote changes

Dommage…

### **Synchro de GitHub, de PC1 et de PC2**

Situation: on développe sur le  PC1, mais on aimerait poursuivre sur PC2, comme si 2 utilisateurs travaillent à tour de rôle. Ici, on utilise Git-Gui.exe, que l’on peut lancer depuis la ligne de commande par: git-gui.

Le code – en l’occurrence blink2 Arduino – est déjà déposé sur GitHub.

### **Git-gui (sur PC2)**

Etape 1: Clone. Le répertoire local ne doit **pas préexister**. Charger localement depuis GitHub :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-17.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-4.png)

### **Ajout et modification de fichier**

Le fichier toto.txt (complètement bidon) est ajouté. Rescan :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-18.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-5.png)

Pour la bonne forme, je modifie le commentaire de blink2.ino. Une fois les modifs terminées, cliquer le fichier pour le passer à Staged…

Puis \[Commit\] pour enregistrer *localement* la(les) différence(s)

### **Nouvelle version sur GitHub**

La modif est seulement locale. On la met sur GitHub avec \[Push\] :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-19.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-6.png)

Vérification sur GitHub, via le WEB :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-20.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-7.png)

Le fichier toto.txt est bien ajouté; et blink2.ino touché.

## **Modif avec un répertoire cloné sur PC1**

### **Contrôle des changements**

Repository -\> Visualize master’s history

![http://microclub.ch/wp-content/uploads/2017/11/word-image-21.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-8.png)

### **Modifications par PC1**

Delete de toto.txt ; modif de blink2.ino (on remodifie le commentaire)

![http://microclub.ch/wp-content/uploads/2017/11/word-image-22.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-9.png)

Commit et push de cette version :

![http://microclub.ch/wp-content/uploads/2017/11/word-image-23.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-10.png)

### **Synchro sur PC2**

**Obtenir une réplication correcte (sans tout cloner)**

Pour mémoire, on a supprimé le fichier toto.txt. Etape 1, synchro du dépôt local de PC2: **git fetch**

![http://microclub.ch/wp-content/uploads/2017/11/word-image-24.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-11.png)

Etape 2: synchro répertoire de travail : **git merge**

![http://microclub.ch/wp-content/uploads/2017/11/word-image-25.png](/media/2018/02/http-microclub-ch-wp-content-uploads-2017-11-wor-12.png)

Le répertoire local est à jour sur le PC2.

Yves Masur (11/2017)

## Commentaires

### Nicolas Jeanmonod — 4 mars 2018 à 11:55

Je vois que tu t’en es super bien sorti (donc pas de titubation comme tu dis sur FB ;-). Perso je n’utilise quasiment que la ligne de commande parce que les GUI sont tellement nombreux que je ne savais plus quoi choisir et finalement ils me troublent plus qu’ils ne m’aident.

La grande majorité du temps, j’utilise Git sans GitHub. L’idée est simplement de gérer l’historique de mes projets et de pouvoir revenir en arrière si nécessaire. Ça m’évite de faire des copies de mes fichiers et de me retrouver avec une multitude de versions : fichier_v1.txt, fichier_v2.txt… C’est particulièrement utile en programmation pour tester une idée dont je ne suis pas sûr qu’elle va fonctionner. Ça me permet de rapidement revenir en arrière et ça me permet aussi de vérifier que je n’ai fait que les modifications que je voulais entre deux commits.

Avec GitHub on peut créer un site web gratuitement. Je pourrais vous montrer la procédure le 20 avril 2018 si ça intéresse les membres.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
