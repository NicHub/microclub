---
title: "Python"
date: "2011-05-13T15:20:24"
lastmod: "2015-04-24T23:20:19"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation", "python"]
url: "/2011/05/13/python/"
wordpress_id: 488
comment_count: 1
---
<blockquote><p><a href="http://www.python.org/"><img alt="" height="106" src="http://www.python.org/images/python-logo.gif" width="316"/></a>Il ne vaut pas la peine de connaitre un langage qui ne modifie pas votre façon de penser la programmation. (<a href="http://drgoulu.com/2008/01/21/perlisismes-les-dictons-informatiques-dalan-perlis/">Alan Perlis</a>)</p></blockquote>
<p><a href="http://www.python.org/"><br/>
</a>Après Basic, Pascal, Modula-2, ADA, LISP, Prolog, C++ et sa STL , je viens de découvrir un nouveau langage qui modifie ma façon de penser la programmation : Python.</p>
<p>Ce langage a été créé par <a href="http://fr.wikipedia.org/wiki/Guido_van_Rossum" target="_blank">Guido van Rossum</a> en une semaine de 1989, sur un Mac, et baptisé en l’honneur des « Monty Pythons »… 20 ans plus tard, son langage  est utilisé dans de <a href="http://www.python.org/about/success/" target="_blank">très nombreux domaines et applications</a>, entre autres au CERN, à la NASA,  et chez Google où travaille désormais Guido.</p>
<h3><!--more-->Python et la Science</h3>
<p>Le point commun de beaucoup d’applications de Python, c’est la science. J’ai compris pourquoi grâce à  à <a href="http://drgoulu.com/2009/02/24/project_euler/" target="_blank">ProjectEuler.net</a>, qui permet de comparer des algorithmes exprimés dans différents langages de programmation. Les solutions en Python sont systématiquement les plus compactes (à l’exception d’<a href="http://fr.wikipedia.org/wiki/APL_(langage)" target="_blank">APL</a>) Par exemple, une seule ligne suffit à calculer la somme des décimales de 100 factorielle :</p>
<p><code>reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])</code></p>
<p>Dans cette seule ligne :</p>
<ul>
<li>le type entier s’étend automatiquement à la demande pour représenter ici un nombre de 158 chiffres</li>
<li>on le convertit en chaîne de caractères par str()</li>
<li>on construit par « compréhension » (for) une liste [ ] des caractères re-convertis en nombres par int()</li>
<li>dont on fait la somme en utilisant la <a href="http://fr.wikipedia.org/wiki/Python_(langage)#Programmation_fonctionnelle" target="_blank">programmation fonctionnelle</a> ( reduce+lambda) une seconde fois.</li>
</ul>
<h3>Mais encore ?</h3>
<ul>
<li>en utilisant l’indentation pour délimiter les blocs, on évite de compter les {{}{{}{}}}</li>
<li>les variables sont fortement typées, mais n’ont pas besoin d’être déclarées</li>
<li>la <a href="http://fr.wikipedia.org/wiki/Python_(langage)#Programmation_objet">programmation objet</a> est très complète, avec héritage multiple et <a href="http://fr.wikipedia.org/wiki/Python_(langage)#M.C3.A9thodes_sp.C3.A9ciales_et_surcharge_des_op.C3.A9rateurs">surcharge d’opérateurs</a>, mais pas de dissimulation (private):</li>
</ul>
<blockquote><p>After all, we are all consenting adults here<br/>
(slogan Python, Karl Fast dans « <a href="http://mail.python.org/pipermail/tutor/2003-October/025932.html" target="_blank">What is Pythonic</a>« )</p></blockquote>
<ul>
<li>les <a href="http://docs.python.org/library/stdtypes.html" target="_blank">types natifs</a> incorporent des structures de données supportés par la syntaxe:
<ul>
<li>str ‘ ‘ ou  » « </li>
<li>list [] et  <a href="http://docs.python.org/tutorial/datastructures.html#tuples-and-sequences" target="_blank">tuple</a> (,)</li>
<li>set (ensemble) {}</li>
<li>dict (ionnaire)</li>
</ul>
</li>
<li>Outre une belle panoplie de <a href="http://docs.python.org/library/functions.html" target="_blank">fonctions prédéfinies</a>, Python dispose d’une impressionnante <a href="http://docs.python.org/library/index.html" target="_blank">librairie standard</a>.</li>
<li>un <a href="http://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d'exceptions" target="_blank">système de gestion des exceptions</a> fait évidemment <a href="http://docs.python.org/tutorial/errors.html" target="_blank">partie du langage</a></li>
<li>on peut effectuer des affectations multiples : a,b=b,a+b #remarquez le swap!</li>
<li>les <a href="http://fr.wikipedia.org/wiki/Python_(langage)#G.C3.A9n.C3.A9rateurs">générateurs</a> permettent  de définir des <a href="http://docs.python.org/library/stdtypes.html#iterator-types" target="_blank">itérateurs </a>d’une manière bien plus simple qu’en C++ (STL)</li>
</ul>
<pre>def gen_fibonacci():
    """Générateur de la suite de Fibonacci"""
    a, b = 0, 1

    while True:
        yield a  # Renvoi de la valeur de "a", résultat de l'itération en cours
        a, b = b, a + b

fi = gen_fibonacci()
for i in range(20):
    print fi.next()</pre>
<ul>
<li>les commentaires entre  »  »  »doc_code »  »  » sont considérés comme un champ nommé __doc__, ce qui permet de générer de la documentation (help) automatiquement.</li>
</ul>
<ul>
<li>l’introspection : les éléments du langage (classes, méthodes…) sont des objets qui peuvent être parcourus à l’aide de la fonction <a href="http://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/power_of_introspection/getattr.php" target="_blank">getattr</a></li>
</ul>
<p>def info(object, spacing=10, collapse=1):</p>
<pre>    """Print methods and doc strings.Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])</pre>
<ul>
<li>la fonction <a href="http://docs.python.org/library/functions.html#eval" target="_blank">eval</a> permet des miracles comme ce  <a href="http://code.activestate.com/recipes/355045-spreadsheet/" target="_blank">tableur en 9 lignes de code</a> !</li>
</ul>
<div>
<pre>class SpreadSheet:
    _cells = {}
    tools = {}
    def __setitem__(self, key, formula):
        self._cells[key] = formula
    def getformula(self, key):
        return self._cells[key]
    def __getitem__(self, key ):
        return eval(self._cells[key], SpreadSheet.tools, self)

&gt;&gt;&gt; from math import sin, pi
&gt;&gt;&gt; SpreadSheet.tools.update(sin=sin, pi=pi, len=len)
&gt;&gt;&gt; ss = SpreadSheet()
&gt;&gt;&gt; ss['a1'] = '5'
&gt;&gt;&gt; ss['a2'] = 'a1*6'
&gt;&gt;&gt; ss['a3'] = 'a2*7'
&gt;&gt;&gt; ss['a3']
210
&gt;&gt;&gt; ss['b1'] = 'sin(pi/4)'
&gt;&gt;&gt; ss['b1']
0.70710678118654746
&gt;&gt;&gt; ss.getformula('b1')
'sin(pi/4)'</pre>
</div>
<ul>
<li>les décorateurs sont une <a href="http://drgoulu.com/2010/12/03/les-decorateurs-python/" target="_blank">extraordinaire invention</a> de Python. Ils permettant d’insérer facilement une fonction à l’appel et au retour d’une autre:</li>
</ul>
<pre>@decorateur
def fonction(parametre):
  code()
  return resultat</pre>
<p>est fonctionnellement équivalent à</p>
<pre>def fonction(parametre):
  parametre=decorateur(parametre,entree)
  code()
  return decorateur(resultat,sortie)</pre>
<p>les décorateurs permettent de réaliser très facilement des logs, du profilage ou du chronométrage de temps d’exécution. Ils permettent aussi d’implanter des mécanismes existant dans d’autres langages, comme les propriétés à la Delphi/C#, ou des mécanismes utiles en programmation concurrente, ou encore d’améliorer les performances par des caches de « memoization ». Une <a href="http://wiki.python.org/moin/PythonDecoratorLibrary" target="_blank">librairie de décorateurs</a> est disponible.</p>
<h3>Ou et Comment</h3>
<ul>
<li>l’interpréteur Python est gratuit, open source (écrit en C, donc appelé parfois CPython), et <a href="http://www.python.org/download/" target="_blank">disponible sur Python.org</a> pour Windows, Mac, Linux et beaucoup d’<a href="http://www.python.org/download/other/" target="_blank">autres plateforme</a>s.
<ul>
<li>Il se lance par la ligne de commande, donc doit être dans le PATH…</li>
<li>la variable PYTHONPATH définit la recherche des « <a href="http://docs.python.org/tutorial/modules.html" target="_blank">modules</a> » (fichiers .py)</li>
</ul>
</li>
<li><a href="http://www.pythonxy.com/" target="_blank" title="Python(x,y)">Python(x,y)</a> est la distribution de Python la plus complète sur PC, incluant de <a href="http://code.google.com/p/pythonxy/wiki/StandardPlugins" target="_blank">nombreuses librairies</a> et outils comme:
<ul>
<li><a href="http://docs.python.org/library/idle.html" target="_blank">IDLE</a> l’IDE standard, suffisant pour de petits développements</li>
<li> l’IDE  Eclipse avec <a href="http://pydev.org/" target="_blank">PyDev</a> et <a href="http://qt.nokia.com/" target="_blank">Qt</a> pour la création d’applications graphiques complexes</li>
<li><a href="http://code.google.com/p/spyderlib/" target="_blank">Spyder</a>, the Scientific PYthon Development EnviRonment</li>
</ul>
</li>
</ul>
<p>en prime la doc de Python(x,y) est partiellement en français. Vivement <a href="http://drgoulu.com/2008/10/17/pythonxy/" target="_blank">conseillé </a>!</p>
<p>ATTENTION ! Python 3 est « nouveau » et le langage a passablement changé. Il ne supporte pas toutes les librairies existantes… Préférez le 2.7 (ou le 2.6 livré avec Python(x,y) ) en tenant compte des changements apportés par la 3.0 …</p>
<p>Existent aussi:</p>
<ul>
<li><a href="http://ironpython.codeplex.com/">IronPython</a> (tournant sur machine virtuelle .NET)</li>
<li><a href="http://www.jython.org/">Jython</a> (tournant sur machine virtuelle Java)</li>
<li><a href="http://pypy.org/">PyPy</a>, un Python avec compilateur JIT, très rapide</li>
<li><a href="http://www.stackless.com/" target="_blank">Stackless</a>, un dialecte facilitant la programmation concurrente, utilisé par le jeu EVE notamment</li>
</ul>
<figure aria-describedby="caption-attachment-495"><a href="/media/2011/05/2011-05-12_230640.png"><img alt='Zen of Python : easteregg apparaissant pour "import this"' height="366" src="/media/2011/05/2011-05-12_230640.png" title="Zen of Python" width="677"/></a><figcaption>Zen of Python : easteregg apparaissant pour "import this"</figcaption></figure>
<p>Un nombre incroyable de librairies Python est disponible un peu partout sur le web pour toutes les applications imaginables.</p>
<p>Beaucoup sont des « binding » vers du code C++ compilé, offrant une performance nettement supérieure à du code purement Python (voir <a href="http://www.swig.org/" target="_blank">SWIG</a> ou <a href="http://www.boost.org/doc/libs/1_46_1/libs/python/doc/" target="_blank">Boost.Python</a> )</p>
<h3>Exemples:</h3>
<h3><a href="http://drgoulu.com/2008/12/04/demosaiquification/">Demosaïquification</a></h3>
<p>Combien de petites images distinctes sont utilisées pour produire une image mosaïque ? Pour répondre à cette question, j’ai développé un petit programme avec <a href="http://drgoulu.wordpress.com/2008/10/17/pythonxy/" target="_blank">Python(x,y)</a> en utilisant la <a href="http://www.pythonware.com/products/pil/" target="_blank">« Python Imaging Library » (PIL)</a></p>
<h3>DicoLib en Python</h3>
<p>Vous vous souvenez tous de <a href="http://drgoulu.com/2005/09/14/dicolib/" target="_blank">DicoLib</a>, la géniale structure de données qui m’a permis de <a href="http://www.puzzles.com/PuzzleHelp/WordDownsizing/WordDownsizingSol.htm" target="_blank">résoudre</a> le problème du <a href="http://drgoulu.com/2005/09/14/word-downsizing/" target="_blank">word downsizing</a> il y a quelques années. Voilà ce que ça donne réécrit en Python:</p>
<h3>En conclusion</h3>
<p>Python est utilisé dans de gros projets, soit directement comme langage de programmation, soit comme langage de script, soit les deux à la fois:</p>
<ul>
<li>Web : <a href="http://www.zope.org/" target="_blank">Zope</a>+<a href="http://www.plone.fr/" target="_blank">Plone</a>, <a href="http://www.djangoproject.com/" target="_blank">Django</a>, <a href="http://twistedmatrix.com" target="_blank">Twisted</a></li>
<li>3D : <a href="http://www.blender.org/" target="_blank">Blender</a>, <a href="http://www.freecad.com/" target="_blank">FreeCAD</a>, <a href="http://www.geeks3d.com/geexlab/" target="_blank">GeeXLab</a></li>
</ul>
<p>Mais c’est avant tout un langage permettant de réaliser des choses complexes avec peu de lignes de code grâce à un très haut niveau d’abstraction.</p>
<h3>Références:</h3>
<ol>
<li><a href="http://fr.wikipedia.org/wiki/Python_(langage)">http://fr.wikipedia.org/wiki/Python_(langage)</a></li>
<li><a href="http://www.scribd.com/doc/21314841/Tutoriel-Python">http://www.scribd.com/doc/21314841/Tutoriel-Python</a></li>
<li>Mark Pilgrim « <a href="http://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/index.php" target="_blank">Plongez au coeur de Python</a>« , livre libre</li>
<li><a href="http://code.activestate.com/recipes/langs/python/" target="_blank">Python Reciepes on ActiveState.com</a></li>
</ol>

## Commentaires

### Yves Masur — 7 décembre 2011 à 20:24

<section class="comment-content comment">
<p>Pour se lancer dans Python, un peu de doc:<br/>
le document cité ci-dessus: <a href="http://www.scribd.com/doc/21314841/Tutoriel-Python" rel="nofollow ugc">http://www.scribd.com/doc/21314841/Tutoriel-Python</a> – un très bon tuto de Olivier Berger, au format PDF.</p>
<p>Site du zéro : <a href="http://www.siteduzero.com/tutoriel-3-223267-apprendre-python.html" rel="nofollow ugc">http://www.siteduzero.com/tutoriel-3-223267-apprendre-python.html</a><br/>
Livre: « Apprenez à programmer en Python » de Vincent Le Goff, très accessible.</p>
<p>Livre aide mémoire: Python Pocket reference (anglais), 4 ème édition, couvre les version 2.6 et 3.x</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
