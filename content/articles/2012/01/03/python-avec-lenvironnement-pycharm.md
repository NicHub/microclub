---
title: "Python avec l’environnement PyCharm"
date: "2012-01-03T15:02:15"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["consoles", "initiation", "programmation", "python", "software"]
url: "/2012/01/03/python-avec-lenvironnement-pycharm/"
wordpress_id: 674
comment_count: 2
---
<h3>Installation et 1ère prise en main</h3>
<p>L’environnement PyCharm, de Jetbrains (http://www.jetbrains.com/pycharm/) est prévu pour la programation, test, debug et déployement en Python. Le fichier téléchargé pour l’installation pèse env.80 MB. Elle se fait sans problème, pas besoin de redémarrer Windows. Avant de le lancer, il faut avoir un (ou plusieurs) interprèteur(s) Python installé(s). Dans mon cas, j’ai la version 2.7.2.</p>
<p>Au lancement, PyCharm vous demande lequel vous utilisez, afin de l’analyser et l’indexer. Ce qui prend pas mal de temps.</p>
<p><a href="/media/2012/01/pycharm01.jpg"><img alt="scann de Python" height="96" src="/media/2012/01/pycharm01.jpg" title="pycharm01" width="482"/></a></p>
<p>Si comme moi vous rangez vos projets Python dans un répertoire, il suffit d’indiquer à PyCharm avec lequel vous voulez travailler; il en fait un projet. Chaque fichier *.py du répertoire peut être démarré, Par contre, il faut le configurer en conséquence. Ci-dessous, le message: « Configure Python Interpreter », qui survient, la config étant accessible en tout temps via l’icône « clef à écrou » juste avant le « Help ».</p>
<div>
<dl>
<dt><a href="/media/2012/01/pc-open-dir.jpg"><img alt="Open dir" height="495" src="/media/2012/01/pc-open-dir.jpg" title="pc-open dir" width="746"/></a></dt>
<dd>Ouvrir un projet</dd>
</dl>
</div>
<h3>Disposition</h3>
<p>Les fenêtres sont assez parlantes par elles même: Projet, Structure, Favorites, mais précisons qu’on peut les développer par Alt + n° de la fenêtre dans le layout, qui lui même est configurable et modifiable. Les fenêtres peuvent être Pined, Docked, Split ou encore Floating. Un double clic sur un nom de fichier du projet l’ouvre dans l’éditeur. Évidemment en syntaxe colorée. La structure correspondante apparaît et peut être développée. L’élément est représenté par un symbole coloré. On a v: variable, C: classe ou m: fonction (méthode, selon la terminologie PyCharm); si le symbole est cliqué, le curseur est positionné à l’endroit adéquat dans le fichier source. Celui-ci est encodé en utf-8 par défaut, PyCharm gère aussi le format de lignes Mac ou Unix.</p>
<p>Toutefois, j’ai été surpris par un fichier de config contenant des lettres accentuées au format ANSI Windows-1252 (et non utf-8 comme indiqué ci-dessous), il affichait de vilains losanges avec ‘?’.</p>
<p><a href="/media/2012/01/win-1252.jpg"><img alt="codage win-1252" height="51" src="/media/2012/01/win-1252.jpg" title="win-1252" width="456"/></a></p>
<div>
<dl>
<dd>codage win-1252</dd>
<dt></dt>
</dl>
<h2></h2>
<h3>Configuration</h3>
<p>Reprenons les paramètres de lancement du module. Dans l’écran ci-dessus, le module chargé « det_an02 » est un programme simple, qui tient dans un seul fichier. Il faut qu’il soit déclaré « main » pour démarrer. Voyons donc la configuration, pas encore établie, donc avec un ‘x’ rouge.</p>
<div>
<dl>
<dt><a href="/media/2012/01/Edit-config.jpg"><img alt="Edit config" height="152" src="/media/2012/01/Edit-config.jpg" title="Edit config" width="227"/></a></dt>
<dd>Editer la config</dd>
</dl>
</div>
<p><a href="/media/2012/01/run_debug_conf.jpg"><img alt="run_debug_conf" height="376" src="/media/2012/01/run_debug_conf.jpg" title="run_debug_conf" width="498"/></a></p>
<p>Par défaut, le nom de la config est celle du nom de fichier de script. Le plus souvent, si le module doit être testé, l’important est de fournir des paramètres en ligne de commande. Dans ce cas, se sont un fichier d’entrée à traiter « riponne20.txt » et celui de sortie « out3.txt ».</p>
<p>Pour lancer l’exécution,<a href="/media/2012/01/Logo-Run.jpg"><img alt="Logo Run" height="19" src="/media/2012/01/Logo-Run.jpg" title="Logo Run" width="17"/></a> la lancera en mode normal, tandis que <a href="/media/2012/01/Logo-debug.jpg"><img alt="Logo debug" height="20" src="/media/2012/01/Logo-debug.jpg" title="Logo debug" width="23"/></a> la lancera en mode « debug », dont le temps d’exécution est environ 10 fois plus grand.</p>
<p>Une fenêtre de l’interpréteur Python montre le résultat. Ou les erreurs de compilation, vu que le Python produit du byte-code. Un clic sur l’erreur amène l’édition à la ligne coupable.</p>
<h3>Debugger</h3>
<p>Le mode debugger est un point important d’un environnement de développement. Plutôt que d’envoyer des « print » aux points blocants du programme, PyCharm permet d’insérer des « break point » dans le code. Ou de lancer l’exécution jusqu’à la position du curseur dans le source. Ensuite, on peut suivre le déroulement en pas à pas, avec ou sans détailler les appels à des fonctions/méthodes, attendre le retour d’un fonction, voire un prochain « break point ». Il faut noter, cependant, un ralentissement considérable de l’exécution du programme!</p>
<p>Dès que le programme est suspendu, on peut changer au vol des variables, et procéder à l’évaluation d’expression, ce qui est utile dans des tests compliqués. Il suffit de faire une sélection partielle du code source et de le copier dans l’évaluateur pour en avoir le résultat.</p>
<h3>Éditeur</h3>
<p>L’éditeur est – nous l’avons vu – a coloration syntaxique. Ce n’est pas tout: il met automatiquement la parenthèse fermante si l’on en ouvre une, ainsi que les guillemets, crochets, etc, de ce qui va par paire. Ajouter un appel à la méthode d’une classe nous les propose et cette liste se réduit au fur et à mesure que les caractères sont tapés; on peut cliquer sur une des propositions pour la valider. La méthode acceptée, les paramètres nécessaires ou en option sont indiqués en suivant, mettant en gras le paramètre à introduire.</p>
<h3>Aide à la rédaction</h3>
<p>Dès qu’une ligne est en édition, ou si vous y posez le curseur, une lampe vient et vous propose une amélioration du code. Par exemple:</p>
<p><a href="/media/2012/01/Aide-redaction.jpg"><img alt="Aide redaction" height="111" src="/media/2012/01/Aide-redaction.jpg" title="Aide redaction" width="331"/></a></p>
<p>C’est vrai qu’à l’instar de la ligne précédente, on pourrait écrire l’incrément de ‘duree’: duree += 1, ce qui est fait par un simple clic!</p>
<p>Une refactorisation des expressions dans une condition est parfois proposée plus compliquée que l’original, et n’amène rien:</p>
<p><a href="/media/2012/01/Aide-if.jpg"><img alt="Aide if" height="90" src="/media/2012/01/Aide-if.jpg" title="Aide if" width="302"/></a></p>
<p>D’une manière générale, on peut lancer « Inspect code », et une liste de propositions d’améliorationn sera faite, classées par genre:</p>
<p><a href="/media/2012/01/inspect-code.jpg"><img alt="inspect code" height="167" src="/media/2012/01/inspect-code.jpg" title="inspect code" width="381"/></a></p>
<p>L’édition est régulièrement sauvegardée dans un tampon qui mémorise les modifications apportées. On peut revenir sur nos dernières retouches (un bon millier est conservé) et les restituer à l’état précédent si besoin.</p>
<p><a href="/media/2012/01/diff.jpg"><img alt="diff" height="257" src="/media/2012/01/diff.jpg" title="diff" width="691"/></a></p>
<p>Ceci a un coût: PyCharm a besoin de 160 à 270 Mb de RAM. Sur mon netbook, la mise en veille a un réveil bien lent. Il lui faut joliment 1 minute pour tout retrouver. En le démarrant depuis zéro, comme il prend par défaut le dernier projet, toujours sur mon netbook ça prend 1’35 : chargement du programme, chargement et analyse des fichiers (une barre de progression et les fichiers traités sont affichés), initialisation des fenêtres… arrive ensuite le pop-up « Tips of the day », soit une astuce ou conseil du jour, tandis-que la fenêtre « structure » se complète.</p>
<h3>Productivité</h3>
<p>PyCharm ne se laisse pas « avoir » par une modification de fichier extérieure, il a un oeil sur tout. Sa puissance est démontrée lors de modification tel le renommage d’une structure. Son nom n’est pas terrible, vous voulez le changer? Un clic droit dessus, et « refactor » permet de la renommer ou de la déplacer: toutes les références dans les différents sources sont mises à jour, même dans les commentaires!</p>
<p><img alt="refactor" height="180" src="/media/2012/01/refactor.jpg" title="refactor" width="565"/></p>
<p>Ceci est particulièrement bienvenu dans Python, car des erreurs dans un bloc qui passe rarement peuvent facilement passer inaperçues, jusqu’au jour ou la condition est remplie. Et l’erreur sort à l’éxécution. La limite du système se voit si vous utilisez un nom un peut trop général: PyCharm scannant tous les modules, il va vous en proposer un peut trop. Mais on peut facilement les exclure, et éviter de modifier par mégarde du code importé qui fonctionne.</p>
<p>Une fenêtre sympathique: Todo. Il suffit de mettre ce mot clef dans un commentaire de votre code, et vous pourrez en atteindre rapidement l’endroit:</p>
<p><a href="/media/2012/01/todo.jpg"><img alt="todo" height="148" src="/media/2012/01/todo.jpg" title="todo" width="386"/></a></p>
<p>S’il y en a beaucoup, la présentation arborescente par fichier en facilite l’accès.</p>
<h3>Mode interactif – console Python</h3>
<p>Démarrer la console n’est pas – contrairement à ce qu’on peut s’y attendre – sous le menu « Run », mais sous « Tools ». Cette console permet – comme dans d’autres solutions – de rentrer une portion de code pour en tester la forme et les réactions. Les lignes entrées sont mémorisées, même après l’arrêt et le redémarrage de la console, voir du programme, ce qui permet d’y revenir facilement. De plus, la fenêtre « structure » montre les éléments introduits, comme pour un source Python.</p>
<h3>Conclusion provisoire</h3>
<p>Forcément provisoire… JetBrains est un éditeur plein de ressources, proposant plus d’une dizaine d’environnement. Les versions progressent rapidement et sont mise à jour en fonction non seulement des nouveautés, mais avec des fonctionnalités nouvelles ou supérieures. Il y a encore ce dont je ne vous ai pas parlé (car non utilisé): l’édition de Javascript et de HTML, et pour rester coté Python,  le développement WEB avec Django. Utilisable 30 j gratuit, la licence est de 99$. Pour un usage entreprise, c’est $199. Avec du support dans les deux cas.</p>
<p>Yves Masur</p>
</div>

## Commentaires

### Goulu — 25 janvier 2012 à 18:03

<section class="comment-content comment">
<p>Je ne connaissais pas PyCharm, alors j’ai essayé et c’est effectivement très bien. Mais, outre le  fait qu’il soit payant, il y a un truc qui m’a énervé : ces incessantes bulles qui apparaissent au curseur pour signaler des problèmes ou proposer l’autocomplétion. Je suis sur qu’il y a un moyen de les désactiver, mais j’en ai eu marre, et j’ai cherché une alternative …</p>
<p>L’alternative « lourde » que je connaissais, c’est Eclipse + PyDev. Mais vraiment long à configurer, mettre à jour, usine à gaz etc. Et là je suis tombé sur un truc vraiment intéressant : <a href="http://aptana.com/" rel="nofollow">Aptana</a>. C’est une sorte d’Eclipse light préconfiguré avec plein d’outils ciblés pour la programmation Web, mais (c’est pas écrit sur la page principale) aussi PyDev, donc un excellent support de Python. Je teste actuellement, j’écrirais un article si j’ai le temps…</p>
 </section>

### yvon — 8 mai 2014 à 14:10

<section class="comment-content comment">
<p>Bonjour,</p>
<p>Svp, Je souhaiterai savoir s’il est possible d’utiliser TKinter avec PyCharm ou y a t’il un un équivalent pour PyCharm?</p>
<p>Yvon</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
