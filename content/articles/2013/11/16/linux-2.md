---
title: "Linux (2)"
date: "2013-11-16T11:16:33"
lastmod: "2013-11-16T11:16:33"
author: "Marcel Bruchez"
categories: ["Microclub"]
tags: ["linux"]
url: "/2013/11/16/linux-2/"
wordpress_id: 1373
comment_count: 0
---
En complément à sa présentation Jacques Menu nous envoie ces infos :

J’ai mélangé les deux familles de shells dans le feu de l’action, il a une différence de syntaxe pour les alias… :

**Avec bash :**\
root@jupiter:~# alias LLL=’ls -sal’\
root@jupiter:~# LLL\
total 1995028\
4 drwx—— 41 root root       4096 Nov  5 11:38 .\
4 drwxr-xr-x 28 root root       4096 Sep  9 15:42 ..\
4 -rw——-  1 root root       1388 Oct 28 11:14 .ICEauthority\
4 -rw——-  1 root root        742 Nov  5 11:38 .Xauthority\
4 -rw-r–r–  1 root root        170 Oct 31  2012 .Xdefaults

Pour le relister :

root@jupiter:~# alias LLL\
alias LLL=’ls -sal’

**Avec tcsh :**\
root@jupiter:~ \> alias LLL ‘ls -sal’\
root@jupiter:~ \> LLL\
total 1995028\
4 drwx—— 41 root root       4096 Nov  5 11:38 .\
4 drwxr-xr-x 28 root root       4096 Sep  9 15:42 ..\
4 -rw——-  1 root root       1388 Oct 28 11:14 .ICEauthority\
4 -rw——-  1 root root        742 Nov  5 11:38 .Xauthority

Pour ce qui est de bash, je joins une doc très détaillée de ses possibilités. Il y a un de vos membres que ça peut intéresser s’il ne la connaît pas déjà!

[abs-guide](/media/2013/11/abs-guide.pdf)

Pour le parallélisme avec MPI (), voici un exemple (Echange.c) dans lequel les « n » processus gèrent un anneau, chacun échangeant une variable avec des deux voisins immédiats pour faire tourner toutes les valeurs d’un cran dans l’anneau.

Dans MPI, tous les processus exécutent le même code, mais chacun vit sa vie à sa vitesse propre.

– MPI_Barrier () force un rendez-vous global de tous les processus : les premiers arrivés attendent les autres, puis tout le monde redémarre;

– MPI_Sendrecv_replace () force un rendez-vous entre deux processus : le premier arrivé attend l’autre, l’échange de données se fait, puis les deux redémarrent.

Le nombre de processus est défini au lancement de l’application.

J’ai joint une trace d’exécution avec 32 processus (id allant de 0 à 31).

b343 et b344 sont les deux nœuds de calcul alloué au job, à raison de 16 cœurs, et donc processus, chacun.

L’ordre dans lequel les processus affichent leurs lignes de trace est variable à chaque exécution, puisque l’avancement des processus parallèles peut dépendre de la charge des nœuds de calcul ou de l’accès aux entrées/sorties.

Bonne continuation!

—

jmenu@bellatrix:/scratch/jmenu \> cat Echange.c

\#include « mpi.h »\
\#include \<stdlib.h\>\
\#include \<stdio.h\>\
int main(int argc, char \*\*argv)\
{\
int processes, id;\
MPI_Status    status;\
char hostname \[256\];\
int namelength;\
int to, from, a;\
//          On doit commencer par…\
MPI_Init (&argc, &argv);\
//          Récupération d’informations sur l’environnement MPI\
MPI_Comm_size (MPI_COMM_WORLD, & processes);\
MPI_Comm_rank (MPI_COMM_WORLD, & id);\
MPI_Get_processor_name (hostname, & namelength);\
//          Initialisation\
a = id;\
printf (« %s: I am id %d of %d procs with INITIAL a = %d\n »,hostname, id, processes, a );\
fflush (stdout);\
//      On attend que tout les processeurs arrivent jusqu’ici\
MPI_Barrier (MPI_COMM_WORLD);\
if ( id == 0 )\
{\
printf (« — BARRIER! —\n »);\
fflush (stdout);\
}\
//          Détermination du numéro du processeur voisin\
to = (id + 1) % processes;\
from = (id – 1 \>= 0)\
?         id – 1\
:          processes – 1; /\* id of the sender \*/\
//          Echange\
MPI_Sendrecv_replace (& a, 1, MPI_INT, to, 0, from, 0, MPI_COMM_WORLD, & status );\
printf ( « %s: id %d sends to %d and receives from %d a = %d\n », hostname, id, to, from, a );\
//      On attend que tout les processeurs arrivent jusqu’ici\
MPI_Barrier (MPI_COMM_WORLD);\
if ( id == 0 )\
{\
printf (« — BARRIER! —\n »);\
fflush (stdout);\
}\
//          Resultat\
printf ( « %s: I am id %d of %d procs with initialFINAL a = %d\n », hostname, id, processes, a );\
fflush (stdout);\
//          …et on doit finir  par…\
MPI_Finalize ();\
return 0;\
}

—-

b343: I am id 2 of 32 procs with INITIAL a = 2\
b343: I am id 3 of 32 procs with INITIAL a = 3\
b343: I am id 4 of 32 procs with INITIAL a = 4\
b344: I am id 18 of 32 procs with INITIAL a = 18\
b343: I am id 5 of 32 procs with INITIAL a = 5\
b344: I am id 19 of 32 procs with INITIAL a = 19\
b343: I am id 6 of 32 procs with INITIAL a = 6\
b344: I am id 20 of 32 procs with INITIAL a = 20\
b343: I am id 10 of 32 procs with INITIAL a = 10\
b344: I am id 21 of 32 procs with INITIAL a = 21\
b343: I am id 11 of 32 procs with INITIAL a = 11\
b344: I am id 22 of 32 procs with INITIAL a = 22\
b343: I am id 12 of 32 procs with INITIAL a = 12\
b343: I am id 13 of 32 procs with INITIAL a = 13\
b344: I am id 23 of 32 procs with INITIAL a = 23\
b343: I am id 14 of 32 procs with INITIAL a = 14\
b344: I am id 16 of 32 procs with INITIAL a = 16\
b343: I am id 1 of 32 procs with INITIAL a = 1\
b344: I am id 17 of 32 procs with INITIAL a = 17\
b343: I am id 7 of 32 procs with INITIAL a = 7\
b344: I am id 24 of 32 procs with INITIAL a = 24\
b343: I am id 8 of 32 procs with INITIAL a = 8\
b344: I am id 25 of 32 procs with INITIAL a = 25\
b343: I am id 9 of 32 procs with INITIAL a = 9\
b344: I am id 26 of 32 procs with INITIAL a = 26\
b343: I am id 15 of 32 procs with INITIAL a = 15\
b344: I am id 27 of 32 procs with INITIAL a = 27\
b344: I am id 28 of 32 procs with INITIAL a = 28\
b344: I am id 29 of 32 procs with INITIAL a = 29\
b344: I am id 30 of 32 procs with INITIAL a = 30\
b344: I am id 31 of 32 procs with INITIAL a = 31\
b343: I am id 0 of 32 procs with INITIAL a = 0\
— BARRIER! —\
b343: id 7 sends to 8 and receives from 6 a = 6\
b344: id 17 sends to 18 and receives from 16 a = 16\
b343: id 8 sends to 9 and receives from 7 a = 7\
b343: id 2 sends to 3 and receives from 1 a = 1\
b343: id 3 sends to 4 and receives from 2 a = 2\
b343: id 4 sends to 5 and receives from 3 a = 3\
b343: id 5 sends to 6 and receives from 4 a = 4\
b343: id 6 sends to 7 and receives from 5 a = 5\
b343: id 9 sends to 10 and receives from 8 a = 8\
b343: id 10 sends to 11 and receives from 9 a = 9\
b343: id 11 sends to 12 and receives from 10 a = 10\
b343: id 12 sends to 13 and receives from 11 a = 11\
b343: id 13 sends to 14 and receives from 12 a = 12\
b343: id 14 sends to 15 and receives from 13 a = 13\
b343: id 15 sends to 16 and receives from 14 a = 14\
b343: id 0 sends to 1 and receives from 31 a = 31\
b343: id 1 sends to 2 and receives from 0 a = 0\
— BARRIER! —\
b343: I am id 0 of 32 procs with initialFINAL a = 31\
b343: I am id 1 of 32 procs with initialFINAL a = 0\
b343: I am id 2 of 32 procs with initialFINAL a = 1\
b343: I am id 3 of 32 procs with initialFINAL a = 2\
b343: I am id 4 of 32 procs with initialFINAL a = 3\
b343: I am id 5 of 32 procs with initialFINAL a = 4\
b343: I am id 6 of 32 procs with initialFINAL a = 5\
b343: I am id 7 of 32 procs with initialFINAL a = 6\
b343: I am id 8 of 32 procs with initialFINAL a = 7\
b343: I am id 9 of 32 procs with initialFINAL a = 8\
b343: I am id 10 of 32 procs with initialFINAL a = 9\
b343: I am id 11 of 32 procs with initialFINAL a = 10\
b343: I am id 12 of 32 procs with initialFINAL a = 11\
b343: I am id 13 of 32 procs with initialFINAL a = 12\
b343: I am id 14 of 32 procs with initialFINAL a = 13\
b343: I am id 15 of 32 procs with initialFINAL a = 14\
b344: id 18 sends to 19 and receives from 17 a = 17\
b344: id 16 sends to 17 and receives from 15 a = 15\
b344: id 19 sends to 20 and receives from 18 a = 18\
b344: id 20 sends to 21 and receives from 19 a = 19\
b344: id 21 sends to 22 and receives from 20 a = 20\
b344: id 22 sends to 23 and receives from 21 a = 21\
b344: id 23 sends to 24 and receives from 22 a = 22\
b344: id 24 sends to 25 and receives from 23 a = 23\
b344: id 25 sends to 26 and receives from 24 a = 24\
b344: id 26 sends to 27 and receives from 25 a = 25\
b344: id 27 sends to 28 and receives from 26 a = 26\
b344: id 28 sends to 29 and receives from 27 a = 27\
b344: id 29 sends to 30 and receives from 28 a = 28\
b344: id 30 sends to 31 and receives from 29 a = 29\
b344: id 31 sends to 0 and receives from 30 a = 30\
b344: I am id 16 of 32 procs with initialFINAL a = 15\
b344: I am id 17 of 32 procs with initialFINAL a = 16\
b344: I am id 18 of 32 procs with initialFINAL a = 17\
b344: I am id 19 of 32 procs with initialFINAL a = 18\
b344: I am id 20 of 32 procs with initialFINAL a = 19\
b344: I am id 21 of 32 procs with initialFINAL a = 20\
b344: I am id 22 of 32 procs with initialFINAL a = 21\
b344: I am id 23 of 32 procs with initialFINAL a = 22\
b344: I am id 24 of 32 procs with initialFINAL a = 23\
b344: I am id 25 of 32 procs with initialFINAL a = 24\
b344: I am id 26 of 32 procs with initialFINAL a = 25\
b344: I am id 27 of 32 procs with initialFINAL a = 26\
b344: I am id 28 of 32 procs with initialFINAL a = 27\
b344: I am id 29 of 32 procs with initialFINAL a = 28\
344: I am id 30 of 32 procs with initialFINAL a = 29\
b344: I am id 31 of 32 procs with initialFINAL a = 30

—

En voici deux que je vous ai montrés :

« psg » [psg](/media/2013/11/psg.txt) fait un « ps » pour afficher les processus, suivi d’un « grep » pour restreindre l’affichage aux seules lignes contenant l’argument fourni. Un premier « ps »  pour récupérer les entêtes de colonnes qui sont écrémées par le « grep », puis un second pour afficher les lignes utiles;

« dfs »[dfs](/media/2013/11/dfs.txt) traite les lignes produites par « df » avec « awk » pour présenter les volumes montés et leur taille de manière plus lisible que « df » lui-même.

A+!

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
