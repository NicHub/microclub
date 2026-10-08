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
<p><img alt="" height="48" src="http://upload.wikimedia.org/wikipedia/fr/thumb/0/06/Python_logo.svg/200px-Python_logo.svg.png" width="200"/>Ces temps-ci, je découvre <a href="http://www.python.org/" target="_blank">Python</a>, un langage de programmation très apprécié en particulier dans la communauté scientifique. Ce « <a href="http://fr.wikipedia.org/wiki/Python_(langage)" target="_blank">langage interprété multi paradigme</a> » intègre des concepts développés dans plusieurs langages récents, ce qui en fait peut-être le langage le plus complet disponible actuellement.</p>
<p>Pour une première approche de ce langage, je vous propose l’analyse du</p>
<h3>Plus Court Solveur de Sudoku</h3>
<p>Voici un  programme en Python de 173 caractères seulement qui serait le plus court <a href="http://drgoulu.wordpress.com/2005/10/26/sudoku/">solveur de sudoku</a> connu actuellement :</p>
<p><code>def r(a): i=a.find('0') if i&lt;0:print a [m in[(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3)or a[j]for j in range(81)]or r(a[:i]+m+a[i+1:])for m in`14**7*9`]r(raw_input())</code></p>
<p>Ce programme est extrêmement compact et condensé, voire cryptique à l’instar des <a href="http://drgoulu.wordpress.com/2008/02/05/cignatures/">Cignatures</a>. Ce n’est pas forcément la meilleure façon de programmer, mais ça révèle souvent la puissance cachée de certains langages. Ce programme est décrit en anglais et en détail <a href="http://www.daniweb.com/forums/thread86363.html" target="_blank">ici</a>, mais voici son principe en gros et en français:</p>
<p><a href="http://drgoulu.wordpress.com/2008/10/12/python/">(la suite sur le blog de Dr. Goulu)</a></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
