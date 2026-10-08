---
title: "Boite à outils Python : PyPI, virtualenv, Git SVN Hg, Goulib"
date: "2012-09-23T17:16:00"
lastmod: "2015-04-24T23:20:18"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["python"]
url: "/2012/09/23/boite-a-outils-python-pypi-virtualenv-git-svn-hg-goulib/"
wordpress_id: 1010
comment_count: 2
---
<p><a href="http://pypi.python.org/pypi/setuptools">setuptools</a> est un outil Python qui n’a (à ma connaissance) aucun équivalent dans l’autres langages : il permet de télécharger des librairies du web, avec toutes leurs dépendances et de les installer, le tout automatiquement .</p>
<p>Après l’avoir installé il suffit par exemple de lancer « easy_install Goulib » depuis une ligne de commande pour incorporer <del>toutes</del> un certain nombre des fonctions Python que j’ai développé ces dernières années à votre propre librairie et les utiliser dans vos propres programmes. Et si vous n’y trouvez pas votre bonheur, il y a environ <a href="http://pypi.python.org/pypi" target="_blank">24000 autres « packages » disponibles sur « PyPI »</a>, le « Python Package Index » dans lequel easy_install.exe va chercher les librairies.</p>
<p>Mais je ne vais pas détailler ici ma librairie, il y aura une doc pour ça un de ces jours… Dans cet article je vais plutôt expliquer ce qu’il faut mettre en place pour diffuser des projets opensource sur le web, et éventuellement permettre à d’autres de corriger vos bugs.</p>
<h3>Tout sur PyPI</h3>
<p>Pour mettre à disposition un package sur PyPI, il suffit de suivre <a href="http://guide.python-distribute.org/creation.html" target="_blank">ces instructions</a>:</p>
<ol>
<li>organiser la structure des répertoires ainsi (je prends Goulib comme exemple):
<pre>Goulib/
    CHANGES.txt
    docs/
    LICENSE.txt
    README.txt
    MANIFEST.in
    setup.py
    Goulib/
        __init__.py
        les_fichiers_source.py</pre>
</li>
<li>où:
<ul>
<li>CHANGES.txt contiendra la liste des changements à chaque version, il peut donc être vide au début</li>
<li>LICENSE.txt doit contenir le texte légal de la licence de diffusion du code. Pour ma part j’utilise la <a href="http://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU" target="_blank">LGPL</a> dont le <a href="http://www.gnu.org/licenses/lgpl-3.0.txt" target="_blank">texte est ici</a></li>
<li>README.txt contient le texte qui sera affiché sur la page PyPI de la lib au format <a href="http://johnmacfarlane.net/pandoc/">pandoc</a> ou  <a href="http://docutils.sourceforge.net/rst.html">ReStructuredText</a>. Par exemple <a href="https://bitbucket.org/goulu/goulib/src/5233290da936/README.txt" target="_blank">mon README.txt</a> produit <a href="http://pypi.python.org/pypi/Goulib" target="_blank">cette page</a></li>
<li>le MANIFEST.in est un <a href="http://docs.python.org/distutils/sourcedist.html#the-manifest-in-template" target="_blank">template</a> permet d’ajouter des fichiers à la distribution, <a href="http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute" target="_blank">les fichiers.py et d’autres</a>étant inclus par défaut. Le fichier minimal contient:
<pre>include *.txt
recursive-include docs *.txt</pre>
<p>pour que les fichiers .txt sus-mentionnés ainsi que ceux qui se trouveraient dans le dossier docs soient inclus</p></li>
<li>enfin, setup.py est le fichier qui décrit tout le package:
<pre>from distutils.core import setup

setup(
    name='Goulib',
    version='1.0.0',
    author='Philippe Guglielmetti',
    author_email='goulib@goulu.net',
    packages=['Goulib'],
    scripts=[],
    url='http://pypi.python.org/pypi/Goulib/',
    license='LICENSE.txt',
    description='My Python library.',
    long_description=open('README.txt').read(),
    install_requires=[],
)</pre>
<p>le « install_requires » est une liste vide dans mon cas car Goulib ne requiert aucune autre librairie à part la librairie Python standard installée avec Python. Mais si le package nécessite au moins la version 1.1.1 de <a href="http://pypi.python.org/pypi/Django" target="_blank">Django</a> et <a href="http://pypi.python.org/pypi/caldav" target="_blank">caldav</a> précisément à la version 0.1.4, on peut spécifier:</p>
<pre>install_requires=[
        "Django &gt;= 1.1.1",
        "caldav == 0.1.4",
    ],</pre>
<p>et ces packages (et toutes leurs propres dépendances…) seront téléchargées et installées automatiquement au besoin (c’est beau !)</p></li>
</ul>
</li>
<li>ensuite, la commande « python setup.py sdist » préparera tout ce qu’il faut et le comprimera dans un fichier .zip placé dans un sous-répertoire « dist »</li>
<li>enfin, il faut créer un compte sur <a href="http://pypi.python.org/pypi" target="_blank">PyPI</a> et faire « python setup.py register » pour y enregistrer le nouveau package puis « python setup.py sdist upload » pour y uploader le package et le rendre disponible à tous les Pythonistes</li>
</ol>
<h3>Il me faut un virtualenv</h3>
<p><img alt="" height="320" src="http://1.bp.blogspot.com/-8DhrncUTCIo/ThWCUyWDxFI/AAAAAAAAEZI/GDmAb4GC2OU/s1600/sandbox.jpg" width="320"/>Oui mais si j’ai un projet qui a besoin d’une certaine version d’un package et un autre projet qui a besoin d’une autre version du même package ? Et si je veux commencer un nouveau projet avec Python 3.3 alors que j’ai toujours besoin de Python 2.7 pour le vieux ?</p>
<p>Microsoft résout ça en remplissant votre PC avec les .dll de toutes les versions sous toutes les versions de .NET, alors que fait ça bien avec <a href="http://www.virtualenv.org/" target="_blank">virtualenv</a>. Comme c’est un package PyPI, on l’installe en faisant « easy_install <a href="http://pypi.python.org/pypi/virtualenv">virtualenv</a>« .</p>
<p>Ensuite quand on a besoin d’un environnement Python différent, on fait « python virtualenv.py ENV » où ENV est le nom du projet ou de l’environnement qu’on veut créer. Ca créer une structure de dossiers comme celle-ci:</p>
<pre>ENV/
    Include/
    Lib/
    Scripts/</pre>
<ul>
<li>Dans « Include » il y a plein de fichiers .h dont Python a besoin je ne sais pas (encore) pourquoi</li>
<li>Dans « Lib » il y a la librairie standard de Python, et rien qu’elle pour l’instant</li>
<li>Dans « Scripts » il y a:
<ul>
<li>une copie de l’interpréteur Python.exe courant, par défaut celui que vous avez installé en dernier sur votre machine</li>
<li>« activate.bat » qui lorsqu’il est lançé, ajuste les variables d’environnement pour utiliser cette copie de l’interpréteur Python et la librairie qui se trouve dans Lib plutôt que celle par défaut</li>
<li>« deactivate.bat » qui remet tout en ordre</li>
<li><a href="http://pypi.python.org/pypi/pip" target="_blank">pip</a>, un remplacement du « easy_install » mentionné au début de cet article. Pip installe les packages dans l’environnement activé plus proprement qu’easy_install.</li>
</ul>
</li>
</ul>
<figure><img alt="" height="384" src="http://s3.pixane.com/python_comrades.png" width="512"/><figcaption>En fait, oubliez easy_install</figcaption></figure>
<p>Voilà, vous avez compris : lancez activate.bat, puis faites « pip Goulib » pour installer votre librairie préférée seulement où il y en a besoin. En prime, absolument tous les fichiers nécessaires à un projet sont réunis dans le dossier ENV, y compris l’exécutable du langage. Il suffit d’archiver tout ça pour pouvoir récupérer et faire tourner le programme sur une autre machine, ou dans <del>très</del> longtemps comme l’exigent les employeurs sensés.</p>
<h3>A plusieurs, c’est mieux</h3>
<p>Avec tout ça le monde entier peut bénéficier de votre code, mais votre code ne peut pas bénéficier du monde entier. Il existe <a href="http://en.wikipedia.org/wiki/Comparison_of_open_source_software_hosting_facilities" target="_blank">plusieurs sites</a> permettant le travail collaboratif, dont les plus connus sont  <a href="http://sourceforge.net" target="_blank">Sourceforge.net</a>, <a href="https://bitbucket.org/" target="_blank">Bitbucket.org</a>, <a href="http://github.com" target="_blank">GitHub.com</a> et <a href="http://code.google.com/">Google Code</a>. Ces sites utilisent un ou plusieurs des 3 logiciels de « <a href="http://fr.wikipedia.org/wiki/Gestion_de_versions" target="_blank">gestion de versions</a> » à la mode:</p>
<ul>
<li><a href="http://fr.wikipedia.org/wiki/Subversion_(logiciel)" target="_blank">Subversion</a>, SVN pour les intimes. Relativement ancien, il est apprécié des entreprises en particulier car c’est un système centralisé : tout le code de la boite est à un endroit précis. En plus, <a href="http://tortoisesvn.tigris.org/" target="_blank">Tortoise SVN</a> rend SVN très utilisable sous Windows avec des menus contextuels et de jolies icônes indiquant le statut des fichiers</li>
<li><a href="http://fr.wikipedia.org/wiki/Git">Git</a> a le vent en poupe sur le web. C’est à la base un système de gestion de fichiers décentralisés, j’ai pas encore vraiment tout compris comment ça marche, mais comme j’ai décidé de l’utiliser, ça viendra. D’autant qu’en écrivant cet article je découvre <a href="http://code.google.com/p/tortoisegit/">Tortoise GIT</a> !</li>
<li><a href="http://fr.wikipedia.org/wiki/Mercurial">Mercurial</a>, Hg pour les chimistes, est le petit dernier qui monte. Il est encore plus décentralisé que Git car il n’a même plus besoin de serveur. Et il est écrit en Python. Et ya aussi un <a href="http://tortoisehg.bitbucket.org/">Tortoise Hg</a> !</li>
</ul>
<p>Ya plus qu’à choisir… ou tout choisir !  Il n’y a que la centralisation de Subversion qui empêche de publier le code sur plus d’un « repository », alors j’ai choisi <a href="https://sourceforge.net/p/goulib/code-0/2/tree/" target="_blank">sourceforge</a>. Pour Git, j’ai carrément configuré les 4 sites comme autant de repository et mon code est sur <a href="https://sourceforge.net/p/goulib/code/ci/5233290da9363b734ee61b8ce66340c4b45bda45/tree/">sur sourceforge</a>, <a href="https://bitbucket.org/goulu/goulib/src">sur bitbucket</a> et <a href="http://code.google.com/p/goulib/source/browse/">sur code.google.com</a>. <a href="https://github.com/goulu/Goulib">Sur github</a> j’ai encore un petit problème que je ne comprends pas bien, mais ça va aller…</p>
<p>Voilà, maintenant les développeurs du monde entier, vous y compris, qu’ils soient accros au shell linux ou utilisateurs d’un Tortoise peuvent télécharger le code source de Goulib, le corriger et le compléter, et soumettre automatiquement leurs modifs sur le site de leur choix. Ce sera toujours à moi de fusionner leurs contributions et de produire de nouvelles versions sur PyPI pour les utilisateurs finaux.</p>
<p>Une fois que vous aurez compris comment ça marche dans ce cas tout simple, vous pourrez collaborer de façon efficace à des projets open source de plus en plus grands, en finissant par Python (<a href="http://docs.python.org/devguide/">géré sous Mercurial</a>) , Apache (<a href="http://www.apache.org/dev/version-control.html" target="_blank">sous SVN</a>) ou Linux (<a href="http://git.kernel.org/" target="_blank">sous Git</a>)</p>

## Commentaires

### Lam Son — 23 septembre 2012 à 19:41

<section class="comment-content comment">
<p>Ca me donne envie de prendre le temps de distribuer le code python de ma thèse sur Pypi. A tout hasard, est-ce que le Dr Goulu sait si c’est possible d’inclure des du code c++ dans un package Pypi ?</p>
 </section>

### ↳ Réponse — Goulu — 26 septembre 2012 à 18:24

<section class="comment-content comment">
<p>oui, c’est possible. Pour le source pas de problème : il suffit d’ajouter « include recursive src *.h *.cpp » dans le MANIFEST.in . Idem si tu as des *.dll ou *.lib appellées depuis Python.<br/>
Mais si tu veux que le code soit compilé sur la machine qui downloade ta lib (Fenêtre, Pomme ou Pingouin), alors je sais pas faire. Mais ça doit être possible, parce que certaines libs comme <a href="http://pypi.python.org/pypi/numpy/" rel="nofollow ugc">http://pypi.python.org/pypi/numpy/</a> le font. Essaie et dis nous !</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
