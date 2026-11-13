---
title: "Microsoft Office, Open Office et la TVA !!!"
date: "2008-12-06T19:07:52"
lastmod: "2015-04-24T23:22:39"
author: "franic"
categories: ["Microclub"]
tags: []
url: "/2008/12/06/microsoft-office-open-office-et-la-tva/"
wordpress_id: 107
comment_count: 1
---
Lors d’un contrôle TVA, le fonctionnaire en question m’a avisé que ma façon d’arrondir la TVA à 10 centimes ne convenait pas ! Il est obligatoire de l’arrondir au centime ou à 5 centimes.

Comme j’ai personnellement horreur des arrondis au centime, j’ai cherché une solution pour arrondir au 5 centimes. Voici la formule utilisée sous Microsoft Excel 2000 :

**=ARRONDI((E7\*0.076)\*20;0)/20**

Cette formule n’arrondit pas simplement au centime supérieur ou inférieur, mais tiens bien compte du rapprochement.

Comme j’édite mes factures avec Word, j’ai simplement inséré dans mon document un tableau excel, et tout fonctionne à merveille.

Comme ma version de Mircosoft Office 2000 devient vieille, je me suis posé la question suivante : « Est-ce que je mets à jour Microsoft Office ou est-ce que j’opte pour OpenOffice ? »

Me souvenant de ce problème TVA, je tente le test avec la version 2.4 d’OpenOffice ! Déception, ma formule d’arrondi n’est par reconnue par OpenOffice. J’ai donc attendu la nouvelle version 3. Après avoir installé cette nouvelle mouture, j’ai fait un test dans « scalc » et ouf, cela fonctionne à merveille ! C’est gagné, je passe sous OpenOffice ? Attention, je fais encore le test dans « swriter » et déception, une fois la formule magique insérée, le résultat s’affiche : \*\* Expression erronée \*\* !!! En fait la fonction « ARRONDI » ou « ROUND » pose problème !!!

J’ai toutefois le désire de passer à OpenOffice, et j’aimerais bien trouver une solution ! Alors si quelqu’un a déjà résolu ce problème, je suis intéressé à connaître l’astuce !

## Commentaires

### Bruno — 28 février 2009 à 16:29

la formule serait\
d4 = montant\
c6 = 7.6%

=ARRONDI.AU.MULTIPLE(D4\*C6,0.05)

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
