---
title: "Python : un petit Sudoku pour commencer"
date: "2008-10-12T11:24:46"
lastmod: "2015-04-24T23:20:20"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation", "python"]
url: "/2008/10/12/python-un-petit-sudoku-pour-commencer/"
wordpress_id: 91
comment_count: 0
---
![Logo Python](/images/articles/python-logo.svg)Ces temps-ci, je découvre [Python](http://www.python.org/), un langage de programmation très apprécié en particulier dans la communauté scientifique. Ce « [langage interprété multi paradigme](http://fr.wikipedia.org/wiki/Python_(langage)) » intègre des concepts développés dans plusieurs langages récents, ce qui en fait peut-être le langage le plus complet disponible actuellement.

Pour une première approche de ce langage, je vous propose l’analyse du

### Plus Court Solveur de Sudoku

Voici un  programme en Python de 173 caractères seulement qui serait le plus court [solveur de sudoku](http://drgoulu.wordpress.com/2005/10/26/sudoku/) connu actuellement :

\<code\>def r(a): i=a.find('0') if i\<0:print a \[m in\[(i-j)%9\*(i/9^j/9)\*(i/27^j/27\|i%9/3^j%9/3)or a\[j\]for j in range(81)\]or r(a\[:i\]+m+a\[i+1:\])for m in\`14\*\*7\*9\`\]r(raw_input())\</code\>

Ce programme est extrêmement compact et condensé, voire cryptique à l’instar des [Cignatures](http://drgoulu.wordpress.com/2008/02/05/cignatures/). Ce n’est pas forcément la meilleure façon de programmer, mais ça révèle souvent la puissance cachée de certains langages. Ce programme est décrit en anglais et en détail [ici](http://www.daniweb.com/forums/thread86363.html), mais voici son principe en gros et en français:

[(la suite sur le blog de Dr. Goulu)](http://drgoulu.wordpress.com/2008/10/12/python/)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
