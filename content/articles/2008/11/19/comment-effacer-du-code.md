---
title: "Comment effacer du code"
date: "2008-11-19T21:02:08"
lastmod: "2015-04-24T23:20:20"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation"]
url: "/2008/11/19/comment-effacer-du-code/"
wordpress_id: 97
comment_count: 2
---
*trouvé par hasard [cet article en anglais](http://nedbatchelder.com/text/deleting-code.html) sur un sujet plus sérieux qu’il n’y parait. Traduction:*

Il y a plein d’information partout sur comment écrire du code. Voici quelques idées sur comment effacer du code.

#### La meilleure manière d’effacer du code

Ca a l’air évident, mais je suppose que ça ne l’est pas vu les nombreuses autres manières que les programmeurs ont d’effacer du code. Voici comment faire:

\<blockquote\>

Sélectionnez une section de code dans votre éditeur, appuyez sur la touche backspace : voilà c’est fait

\</blockquote\>

La plupart des programmeurs n’aiment pas ceci. Ils veulent garder des bouts de code pour le cas où ils en auraient besoin à nouveau. Ils ont travaillé dur pour programmer ce bout de code. Ils l’ont débogué, il marche. Ils ne veulent juste pas le jeter .

Ces développeurs veulent garder leur vieux code, et ils le font en le désactivant de diverses manières, en le « commentarisant »(\*), en le « conditionnalisant » ou en ne l’appelant plus.

A ces développeurs je dis « Utilise la force, Luke ». La force d’un gestionnaire de source comme [CVS](http://www.cvshome.org/), [Perforce](http://www.perforce.com/), ou [Subversion](http://subversion.tigris.org/) fait que vous n’avez jamais besoin de vous soucier que quelque chose ait disparu pour toujours. Subversion aura le vieux code si vous en avez à nouveau besoin.

Si vous n’avez pas de gestionnaire de source (!?!?!) ou ne voulez pas vous embêter à creuser dans les vieilles révisions, alors copiez le vieux code dans un fichier quelque part et sauvez le. Mais ne le laissez pas là où il n’a rien à faire : dans votre code source.

#### Quel est le problème ?

Si vous avez un bout de code dont vous n’avez plus besoin, il y a une excellente raison de l’effacer plutôt que de le laisser désactivé : réduire le bruit et l’incertitude. Le bruit et l’incertitude font partie des pires ennemis du programmeur, parce qu’ils l’empêcheront de travailler efficacement dans le futur.

Un bout de code désactivé cause de l’incertitude. les autres programmeurs s’interrogent::

- Pourquoi le code était-il comme ça avant ?
- Pourquoi est-ce mieux maintenant ?
- Est-ce qu’on reviendra au vieux code un jour ?
- Comment décidera-t-on?

Si la réponse à l’une de ces questions est importante à connaitre, alors écrivez un commentaire pour l’expliquer, mais ne laissez pas vos collègues deviner.

#### « Commentariser » le code

C’est très facile de transformer une ligne ou deux (ou vingt) en commentaires:\
\<code\>//  VieilleFaconUne(voici);\
//  VieilleFaconDeux(voila);\
NouvelleFacon(voici, voila);\</code\>\
Mais c’est pas bien. Les commentaires servent à donner aux gens des informations utiles en lisant ou écrivant du code. Ils doivent être utilisés pour aider les futurs programmeurs qui vont travailler sur ce code. Mais ces commentaires ne font pas ça. En fait, ils font juste le contraire. En plus d’empêcher la compilation du vieux code, ces commentaires ajoutent au code de la confusion, de l’incertitude, et du doute.

Les futurs développeurs qui verront ce code sauront qu’il marchait de la VieilleFacon et qu’il marche désormais de la NouvelleFacon, mais ils ne sauront pas pourquoi on a commenté les VieilleFacons:

- Est-ce que la NouvelleFacon est juste une expérience ? Si c’est le cas, en quoi est-elle meilleure ? Quand et comment décidera-t-on de la garder ?
- Peut-être que la VieilleFacon était meilleure, mais qu’elle avait un problème? Dans ce cas, quel était le problème ? Etait-ce dans le code de la VieilleFacon, ou dans la façon de l’appeler? Quand sera-ce corrigé ??
- Ou alors la conception a changé et VieilleFacon fait du boulot inutile?

Du code commenté est une question implicite : Pourquoi est-il toujours là ? Il y a des raisons de garder un bout de code commenté. Des modifs que vous savez que vous allez défaire bientôt. Des modifs dont le développeur n’est pas sur. D’accord pour garder le code, mais dites pourquoi vous le gardez. les commentaires sont pour les gens, et une ligne de code dans un commentaire ne dit rien à personne.

Ne commentez pas un bout de code sans dire pourquoi dans le commentaire: N’est-ce pas mieux ?\
\<code\>//  VieilleFacon marchait mieux, mais est inefficace tant que\
// le serveur MumbleFrabbitz est surchargé, donc on utilise\
//  la NouvelleFacon jusqu'à la phase 4\
//  VieilleFaconUne(voici);\
//  VieilleFaconDeux(voila);\
NouvelleFacon(voici, voila);\</code\>\
C’est mieux non ? Mais qui sait si MumbleFrabbitz sera remplacé pour la phase 4? Mais même si ce n’est pas le cas, les développeurs sauront pourquoi on a gardé ce code, et ils sauront quand ils pourront revenir à la meilleure solution.

### La compilation conditionnelle

Les développeurs qui veulent commentariser de gros blocs de code utilisent parfois la compilation conditionnelle pour ça, si le langage la supporte. En C++:\
\<code\>#if 0\
VieilleFaconUne(voici);\
…\
VieilleFaconVingt(voici);\
\#endif\</code\>\
Ce n’est pas mieux que de commentariser le code, c’est juste simple pour le gars qui enlève le code. En fait c’est probablement pire que de le commentariser, car beaucoup d’IDE ne colorieront pas ceci comme commentaire, donc il ne sera pas facile pour d’autres programmeurs de réaliser qu’il a été désactivé.

Donc la même règle s’applique : ne conditionnalisez pas du code sans expliquer pourquoi.

Si vous devez utiliser le préprocesseur C pour enlever du code, « #if 0 » est la meilleure manière de le faire car il est au moins clair que ce code ne doit jamais être compilé.

Chez Lotus, le code source de Notes inclut pas mal de lignes enlevées avec « #ifdef LATER », sous l’hypothèse (correcte) qu’il n’y a pas de symbole « LATER » défini. C’est une forme très faible de documentation; elle indique que le code n’est pas encore prêt a être compilé, mais qu’il le sera « plus tard ». Mais quand ? Une blague circule parmi les développeurs selon laquelle on devrait définir « LATER » et regarder ce qui arrive …

En utilisant des symboles non définis, on laisse les développeurs dans le doute sur leur signification. Peut-être y’a-t-il une configuration du code appelée « LATER » qui dot être prise en compte.

### Code non appelé

Disons que vous avez une très belle classe avec beaucoup de belles méthodes. Un jour vous découvrez qu’une d’entre elles n’est plus utilisée. La gardez-vous ou l’effacez-vous ?

Il n’y a pas de réponse unique à cette question car ça dépend de la classe et de la méthode. Ca dépend surtout de si vous pensez que la méthode pourrait être appelée à nouveau dans le futur. Une réponse grossière pourrait être : si la classe appartient à la librairie, laissez la méthode, et si elle appartient à l’application, alors effacez la.

### Laissez des traces

Un compromis à envisager serait d’enlever un gros bloc de code, mais de laisser un commentaire indiquant où on peut le trouver au besoin, à l’aide d’un commentaire de ce genre :\
\<code\>// (Il y avait un autre algorithme ici basé sur le hachage et il\
// àtait plus rapide mais avait un problème de sécurité.\
// Si vous le voulez, il est ThingMap.java v.1.16 dans CVS.)\</code\>\
C’est court, discret, ça donne un historique et l’endroit où regarder pour plus d’infos.

### Chutes accidentelles

Parfois en écrivant du code, vous n’êtes pas sur de conserver ou effacer une ligne de code et vous voulez essayer de compiler et exécuetr le code avant de décider. Vous commentarisez cette ligne, puis d’autres. Puis vous modifiez plusieurs fichiers et au moment de tester le code, vous avez oublié où sont toutes les lignes temporairement effacées. Vous testez le code, mais vous risquez de laisser accidentellement des lignes code commentarisées un peu partout… Pour éviter ceci, utilisez toujours une marque distinctive pour les lignes de code commentarisées pour que vous puissiez rapidement les retrouver.

Une convention simple comme:\
\<code\>//- VieuxTrucPasSur(test);\</code\>\
fait toute la différence. En utilisant « //- » pour commenter la ligne, vous laissez un marqueur qu’il est très facile de retrouver quand il est temps de nettoyer votre code.

Vous pouvez l’utiliser pour de gros blocs aussi:\
\<code\> \#if 0 //- je ne crois plus en avoir besoin\
VieilleFaconUne(voici);\
…\
VieilleFaconVingt(voici);\
\#endif\</code\>

### Garder les choses propres

En effacant du code, il est trop facile de laisser des fantômes derrière soi. Détruisez les proprement. Par exemple en enlevant la VieilleFacon ici:\
\<code\>if (DansCeCas) {\
VieilleFacon();\
}\</code\>\
N’enlevez pas juste la ligne d’appel à VieilleFacon. Enlevez le test vide aussi. Et si DansCeCas n’est utilisé qu’ici, enlevez la variable aussi. Examinez le code qui initialisait DansCeCas. Est-il obsolete ? Enlevez-le. Soyez sans pitié. Gardez le code propre. Assurez-vous qu’il soit cohérent, sans culs-de-sac qui ne peuvent être compris que par ceux qui savaient ce qu’il y avait là avant.

il est tentant de laisser ce code, car il sera difficile de déterminer ce qui peutêtre enlevé. mais si vous laissez le test vide, un autre développeur le verra un jour ou l’autre et se dira que ce n’est pas logique, et il devra faire une enquête pour comprendre. Ca lui prendra plus longtemps pour comprendre le test vide qu’à vous pour l’enlever.

### Don’t worry, be happy

je sais que ça a l’air drastique de trancher le code sur lequel vous avez transpiré. Ne vous faites pas de souci : ça ira. Il y a un raison pour laquelle vous voulez désactiver ce code. Le gestionnaire de révision aura toujours une copie si vous voulez revenir en arrière. Voyez ça comme ceci : qulles sont les probabilités que vous deviez revenir en arrière comparés à la certitude que vous devrez voir ces lignes de code commentarisé jusqu’à la fin du cycle de vie de votre projet ?

Allez-y ! Effacez votre code ! Il ne vous manquera pas.

[Ned Batchelder](http://nedbatchelder.com/index.html)

*Note\* : j’ai traduit « comment out » par le néologisme « commentariser », pour distinguer l’opération de « commenter », qui consiste à ajouter des commentaires au code.*

## Commentaires

### Herve Kabla — 22 novembre 2008 à 19:54

Excellent article educatif. Il y a une autre façon: c’est quand un morceau de code ressemble furieusement à un autre. Voire… en est la pale copie/coller. Dans ce cas, on efface le bout de code pour le mettre dans une fonction reutilisable ailleurs.

### Yves Masur — 9 décembre 2008 à 20:52

Technique intéressante. Par curiosité j’ai fait une recherche dans mon code pour voir les occurrences de \<code\> \#if 0 \</code\>… Pas beaucoup – ouf! En effet, en C/C++ ceci isole du code commenté ‘normalement’ par /\* \*/ ou double slash. Pas accepté en C#, il faut l’écrire \<code\> \#if nul \</code\>… le progrès.

Par contre, j’ai souvent utilisé \<code\> \#if TEST \</code\> dans lequel figure du code utilisé pour tester les fonctions du module. En effet, il faut parfois des conditions impossible à réunir pour tester son code dans un délai acceptable (changement heure d’été/hiver, nécessité d’avoir des données, etc). Là, un petit main() avec un I/O minimal permet de tester à fond son code avant de le linker avec le reste:\
\<code\>\
\#ifdef TEST\
void main(void)\
{\
char c;\
int i, n;\
float f;\
.\
.\
while(1)\
{\
disp("\n\rEntree diverses");\
cputs("\n\rTexte:");\
n = (int) input_line();\
.\
.\
printf("\n\rvaleur:%f", f);\
}\
}\
\#endif\
\</code\>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
