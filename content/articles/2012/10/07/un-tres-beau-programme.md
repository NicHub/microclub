---
title: "Désobfuscation du Mandelbrot en Python"
date: "2012-10-07T15:29:55"
lastmod: "2015-04-24T23:20:18"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["bmp", "graphiques", "mandelbrot", "python"]
url: "/2012/10/07/un-tres-beau-programme/"
wordpress_id: 1023
comment_count: 3
---
L’autre jour, j’ai découvert un [magnifique programme en Python](http://preshing.com/20110926/high-resolution-mandelbrot-in-obfuscated-python) [obfusqué](http://fr.wikipedia.org/wiki/Code_imp%C3%A9n%C3%A9trable):

\[code lang= »python »\]\_ = (\
255,\
lambda\
V ,B,c\
:c and Y(V\*V+B,B, c\
-1)if(abs(V)\<6)else\
( 2+c-4\*abs(V)\*\*-0.4)/i\
) ;v, x=1500,1000;C=range(v\*x\
);import struct;P=struct.pack;M,\\\
j ='\<QIIHHHH’,open(‘M.bmp’,’wb’).write\
for X in j(‘BM’+P(M,v\*x\*3+26,26,12,v,x,1,24))or C:\
i ,Y=\_;j(P(‘BBB’,\*(lambda T:(T\*80+T\*\*9\
\*i-950\*T \*\*99,T\*70-880\*T\*\*18+701\*\
T \*\*9 ,T\*i\*\*(1-T\*\*45\*2)))(sum(\
\[ Y(0,(A%3/3.+X%v+(X/v+\
A/3/3.-x/2)/1j)\*2.5\
/x -2.7,i)\*\*2 for \\\
A in C\
\[:9\]\])\
/9)\
) )\[/code\]

Il produit en une vingtaine de minutes cette image de l’ [Ensemble de Mandelbrot](http://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot):

![](http://preshing.com/wp-content/uploads/2011/09/M.jpg)

Vous aurez noté la similitude graphique entre le listing en [art ASCII](http://fr.wikipedia.org/wiki/Art_ASCII) et le résultat qui démontre  que [l’indentation en Python](http://docs.python.org/reference/lexical_analysis.html#indentation) n’est pas si contraignante que ça.

Mais ce code est aussi intriguant car il produit en réalité à la volée un fichier  « M.bmp » contenant l’image, et ce de manière tellement compacte que c’est illisible. Donc je l’ai décrypté pour comprendre. Une fois le code reformatté de manière plus traditionnelle, on obtient ce listing:

\[code lang= »python »\]\
\_ = ( 255,\
lambda V,B,c :\
c and Y(V \* V + B, B, c – 1) if (abs(V) \< 6) else (2 + c – 4 \* abs(V) \*\* -0.4) / i\
);

v, x = 1500, 1000;\
C = range(v \* x);

import struct;\
P = struct.pack;\
M, j = ‘for X in j(‘BM’ + P(M, v \* x \* 3 + 26, 26, 12, v, x, 1, 24)) or C:\
i , Y = \_;\
j(P(‘BBB’,\
\*(lambda T:(T \* 80 + T \*\* 9 \* i – 950 \* T \*\* 99, T \* 70 – 880 \* T \*\* 18 + 701 \* T \*\* 9,\
T \* i \*\* (1 – T \*\* 45 \* 2)))\
(sum(\[Y(0,(A%3/3.+X%v+(X/v+A/3/3.-x/2)/1j)\*2.5/x -2.7,i)\*\*2 for A in C\[:9\]\])/ 9)\
))\
\[/code\]

On commence à y voir un peu plus clair, mais c’est encore mieux en remplaçant les [fonctions lambda](http://diveintopython.adrahon.org/power_of_introspection/lambda_functions.html) par des fonctions « normales » et en clarifiant l’écriture du fichier:

\[code lang= »python »\]\
def Y(V,B,c):\
if (abs(V) \< 6):\
return c and Y(V \* V + B, B, c – 1)\
else:\
return (2 + c – 4 \* abs(V) \*\* -0.4) / i

def F(T):\
return (T \* 80 + T \*\* 9 \* i – 950 \* T \*\* 99, T \* 70 – 880 \* T \*\* 18 + 701 \* T \*\* 9, T \* i \*\* (1 – T \*\* 45 \* 2))

v, x = 1500, 1000;\
C = range(v \* x);

from struct import pack\
f=open(‘M.bmp’, ‘wb’)\
f.write(‘BM’ + pack(‘\<QIIHHHH’, v \* x \* 3 + 26, 26, 12, v, x, 1, 24))\
for X in C:\
i=255\
f.write(pack(‘BBB’, \*F(sum(\[Y(0,(A%3/3.+X%v+(X/v+A/3/3.-x/2)/1j)\*2.5/x -2.7,i)\*\*2 for A in C\[:9\]\])/ 9)))\
\[/code\]

Un oeil entraîné reconnait dans la première moitié de la fonction  Y la fameuse formule de calcul de chaque pixel de l’ensemble de Mandelbrot écrite sous forme récursive, où V et B sont des nombres complexes ([natifs en Python](http://docs.python.org/library/functions.html#complex)), et c le nombre de boucles, qui se décrémente. Soit il atteint 0 et la fonction renvoie 0 en stoppant la récursion grâce au « c and », soit le module de V atteint 6 et la fonction renvoie le résultat de la seconde moitié de la fonction, que j’interprète comme un niveau de gris qui donnera une couleur.

Une fois les dimensions v,x définies (on peut fort heureusement les réduire pour que le calcul soit plus rapide), le programme écrit l’entête du fichier au [format BMP](http://en.wikipedia.org/wiki/BMP_file_format) en utilisant la fonction [struct.pack](http://docs.python.org/library/struct.html) où la chaîne ‘\<QIIHHHH’ spécifie le format binaires des 7 paramètres requis dans cet entête.

Ensuite on calcule et on écrit chaque point de l’image sous forme de 3 bytes (‘BBB’) représentant les couleurs RGB fourrnies par la fonction F que j’ai renoncé à analyser. Reste que l’appel à la fonction de calcul Y me semblait bien compliqué: pourquoi cette moyenne de 9 points ‘sum (\[… for A in C\[;9\]\])/9’ ? Et bien il s’agit d’un [surchantillonnage](http://fr.wikipedia.org/wiki/Sur%C3%A9chantillonnage) qui permet de produire une très belle image anti-aliasée, au prix d’un calcul 9x plus lent. Si on décide de s’en passer, la ligne devient (pour A=0):

\[code lang= »python »\]f.write(pack(‘BBB’, \*F(Y(0,(X%v+(X/v-x/2)/1j)\*2.5/x -2.7,i)\*\*2)))\[/code\]

et là on reconnait la production du nombre complexe de départ à partir de X décomposé en coordonnées horizontales et verticales par X%v et X/v respectivement.

Ce programme peut être considéré comme une pure horreur ou une merveille selon qu’on l’observe d’un point de vue professionnel ou geek.

Et comme geek, j’aime bien la combine de l’écriture du BMP. Ca me donne plein d’idées. Pas vous ?

## Commentaires

### Goulu — 7 octobre 2012 à 15:42

Je découvre en faisant de la pub pour cet article qu’il y a déjà eu pas mal d’analyses faites ici : <http://www.reddit.com/r/programming/comments/krpem/highresolution_mandelbrot_in_obfuscated_python/>

Ok, mais la mienne est en français 🙂

### Michel Vonlanthen — 8 octobre 2012 à 08:51

Que oui que ça me donne des idées: je vais envoyer un listing de ce type mais en forme de coeur à ma Belle pour son Noël. Bon, ce serait mieux qu’il dessine un graphique « Pain d’amande » de cette forme plutôt que d’un glups bi-ovoïde. Mais c’est sympa, ça confirme qu’on n’a jamais tout vu dans ce bas monde…

Pour mon cadeau de Noël, l’avantage c’est que je n’aurai même pas besoin de faire une « traduction » du listing, de toute façon elle n’y comprendra rien, elle ne programme pas (à ma part mes week-ends).

Ca va être ça le concours de Noël 2012: faire un listing Arduino en forme de coeur et qui dessine un coeur dans l’espace avec une led, de la fumée, un jet d’eau, du lancer de petits pois ou autres. Ce sera le succès assuré dans les chaumières le soir de Noël et un respect infini de la part des petits-enfants ce qui n’est pas rien parce qu’à force d’entendre de leurs parents, de mes enfants donc, que leur grand-papa préféré commence à gâtouiller, il vont finir par le croire. Là ça va être un bond stratosphérique (quantum leap) dans leur estime…

PS: On pourrait envisager, aussi, de dessiner un sapin avec des bougies pour les plus petits. Et si on veut suggérer quelque action, action, il suffira de dessiner le symbole adéquat. Par exemple une tire-lire si on a besoin d’argent, une moumoute si on espère une repousse rapide des cheveux (mais le mieux, c’est d’aller à Lourdes quand.-même), une bouteille si on veut suggérer un cadeau de Château Margaux 1973, etc, etc.

Bon le soft se complique un peu mais on pourrait même envisager une commande vocale pour déterminer la forme du dessin.

Ah j’ai encore oublié un symbole important: un soustif si on est à la recherche d’une compagne pour la nuit ou pour la vie. Quoique dans ce cas-là il vaut mieux ne pas prévoir une cohabitation trop longue si j’en juge par ce que disait notre brave Sacha Guitry « Avec ma femme, on a eu 25 ans de bonheur, et après on s’est marié »…

### ↳ Réponse — Goulu — 10 octobre 2012 à 11:49

Si tu veux piloter un bidule qui dessine des coeurs, tu trouveras quelques formes utiles sur <http://eljjdx.canalblog.com/archives/2007/02/10/3961202.html> .

Après, donner une forme voulue au listing n’est pas possible dans tous les langages. Il y a ceux où c’est facile parce que les retours de ligne sont non significatifs (C, Java), ceux où c’est impossible parce que le format d’une ligne est imposé (Fortran, assembleurs je pense. Pour Smile/CALM je ne sais pas) et ceux où c’est difficile parce qu’il existe des contraintes (BASIC à cause des GOTO/GOSUB, Python et probablement d’autres)

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
