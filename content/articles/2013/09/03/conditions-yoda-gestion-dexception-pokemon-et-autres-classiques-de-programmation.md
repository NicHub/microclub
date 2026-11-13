---
title: "« Conditions Yoda », « Gestion d’exception Pokémon » et autres classiques de programmation"
date: "2013-09-03T21:05:45"
lastmod: "2015-04-24T23:20:17"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["humour", "programmation"]
url: "/2013/09/03/conditions-yoda-gestion-dexception-pokemon-et-autres-classiques-de-programmation/"
wordpress_id: 1306
comment_count: 6
---
<p><em>(traduction de <a href="http://www.dodgycoder.net/2011/11/yoda-conditions-pokemon-exception.html" target="_blank">« Yoda Conditions », « Pokémon Exception Handling » and other programming classics</a> sur <a href="http://www.dodgycoder.net/">dodgycoder.net/</a> )</em></p>
<p>Voici les meilleures réponses à une <a href="http://stackoverflow.com/questions/2349378/new-programming-jargon-you-coined">question</a> posée sur <a href="http://stackoverflow.com/">StackOverflow.com</a> par  <a href="http://stackoverflow.com/users/179972/john-k">John K</a> :</p>
<div>
<blockquote><p>Quelles sont les expressions de jargon de programmation que vous avez notées dans vos équipes ou remarquées sur Internet ?</p></blockquote>
<h3>Les Conditions Yoda</h3>
<h3><img alt="" border="0" height="116" src="http://2.bp.blogspot.com/-M61Y-VuCCSM/TtIQMTYPNrI/AAAAAAAAAGM/YtTOGRknF1s/s320/yoda-conditions.jpg" width="320"/></h3>
<p>Utiliser <code>if(constante == variable)</code><br/>
au lieu de <code>if(variable == constanet)</code>,<br/>
comme dans <code>if (4 == foo)</code>.</p>
<p>« Yoda » parce que c’est comme dire « si bleu est le ciel » ou « si grand est l’homme »</p>
<p>A l’origine les conditions Yoda ont peut-être été introduites pour éliminer les erreurs potentielles de la forme<br/>
<code>if(count=5)</code> (qui génère une assignation C, le test nécessitant ==). En écrivant <code>if(5=count)</code>, l’erreur est détectée à la compilation.</p>
<h3>La gestion d’exception Pokémon</h3>
<figure><img alt="" height="232" src="http://1.bp.blogspot.com/-dkywl8jyDsE/TtIRTqSZBhI/AAAAAAAAAG0/ejKitc2c3eY/s320/pokemon-exception-handling.png" width="320"/><figcaption>Attrapez-les tous !</figcaption></figure>
<div></div>
<p>Quand vous devez juste les attraper tous:.</p>
<p>[code lang= »c »]<br/>
try<br/>
{<br/>
// do something<br/>
}<br/>
catch<br/>
{<br/>
// catch em all<br/>
}<br/>
[/code]</p>
<h3>Les accolades Egyptiennes<img alt="" border="0" height="320" src="http://2.bp.blogspot.com/-w3QG1xDtQWM/TtIQcSMhL-I/AAAAAAAAAGc/IsOoCDIuhFg/s320/egyptian-brackets.jpg" width="272"/></h3>
<p>Le style d’accolades où l’accolade ouvrante se met à la fin de la première ligne</p>
<p>[code lang= »c »]if (a == b) {<br/>
  printf("hello");<br/>
}[/code]</p>
<p>Ce style est utilisé dans le livre de Kernighan and Ritchie « Le Langage C », donc beaucoup l’appellent le « style » K&amp;R.</p>
<p>Voyez la Wikipédia sur <a href="https://fr.wikipedia.org/wiki/Style_d%27indentation" target="_blank">les styles d’indentation</a> sur les styles Whitesmiths, GNU ou Pico.</p>
<div>
<h3><img alt="" border="0" height="200" src="http://4.bp.blogspot.com/-6_myshiocX0/TtIT3XI-UiI/AAAAAAAAAG8/-qv4wm468AM/s200/ninja.jpg" width="185"/>Les commentaires Ninja</h3>
<div>Aussi appelés commentaires invisibles. commentaires secrets ou « sans commentaires ».</div>
<h3>La Convention de Nommage Schtroumpf</h3>
<p>Quand presque toutes les classes ont le mêmes préfixe</p>
<h3>Le typage enchaîné</h3>
<p>(« stringly typed » en anglais, jeu de mot sur « strongly typed », <a href="https://fr.wikipedia.org/wiki/Typage_fort">typage_fort</a>) Une implémentation qui dépend sans nécessité des chaînes de caractère alors que des alternatives plus agréables pour les programmeurs et les outils de refactoring existent. Par exemple des paramètres de méthodes acceptant des chaînes alors que des types plus appropriés devraient être utilisés. Le code trop enchaîné est habituellement difficile à comprendre et explose à l’exécution sur des erreurs qu’un compilateur aurait normalement trouvé.</p>
<h3>Le Refucktoring</h3>
<p>Variante du <a href="https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code">refactoring</a> popularisé par Martin Fowler dans son livre du même nom, c’est le processus consistant à prendre un bout de code bien conçu et, par une série de petites modifications réversibles, le rendre totalement non maintenable par quiconque d’autre que vous-même.</p>
<h3>Le Fear Driven Development</h3>
</div>
<div>(Développement Piloté par la Peur) : lorsque la gestion de projet ajoute de la pression, par exemple en virant quelqu’un.</div>
<div><img alt="" border="0" height="219" src="http://2.bp.blogspot.com/-eHbGdg8HUDQ/TtIQh90CZNI/AAAAAAAAAGs/SgItRMQ92dM/s320/hydra-code.jpg" width="320"/></div>
<h3>Types de fonctionnalités</h3>
<ul>
<li>La Licorne : une fonctionnalité planifiée si tôt qu’elle peut tout aussi bien être imaginaire.</li>
<li>La Barack Obama: une fonctionnalité qu’on aimerait bien ajouter au projet, mais on n’y sera probablement jamais autorisés.</li>
</ul>
<h3>Les differents types de rapports de bug</h3>
<ul>
<li>Le rapport complaisant : un bug soumis par un utilisateur qui croit qu’il en connait beaucoup plus sur le système que ce qu’il en sait vraiment. Rempli de détails techniques irrelevants et contenant des suggestions (toujours fausses) sur ce qu’il pense être la cause du problème et ce que l’on devrait faire pour le corriger.</li>
<li>Le rapport de junkie: un rapport si profondément incompréhensible que celui qui l’a soumis devait fumer du crack. La version la plus douce est le rapport enfumé, où l’émetteur a du en prendre une de trop…</li>
<li>Le rapport « haussement d’épaule » : un rapport de bug sans message d’erreur ni manière de le reproduire et juste une vague description du problème. Contient généralement la phrase « ça ne fonctionne pas ».</li>
<li>Le « dernier message de Fermat » : un message dans un forum ou un système de suivi de problèmes où l’auteur prétend avoir trouvé un moyen simple de contourner le bug mais ne dit jamais comment et ne revient jamais pour l’expliquer, même si d’autres se sont cassés la  tête sur le bug pendant des années.</li>
<li>Le « flottant » : dans un  système de suivi de problèmes, le ou le bug reste « flottant » en haut de la pile mais n’est jamais assigné à un développeur, peut-être parce qu’il y a un moyen de le contournerl.</li>
</ul>
<h3>Les differents types de bugs</h3>
<ul>
<li>Le Heisenbug : un bug qui disparaît ou change ses caractéristiques quand on essaie de l’étudier</li>
<li><img alt="" border="0" height="180" src="http://3.bp.blogspot.com/-urlJJk7s74A/TudRbjRt7AI/AAAAAAAAAHM/Og3QqWk4D70/s320/large_hadron_debugger_higgs_bugson_yoda_condition.jpg" width="320"/>Le Bugson de Higgs : un bug hypothétique dont on pense qu’il existe d’après un petit nombre d’entrées de logs éventuellement reliées et de vagues rapports de bugs anecdotiques d’utilisateurs, mais difficile si ce n’est impossible à reproduire sur une machine de dev parce que vous ne savez pas s’il est vraiment là, et si oui ce qui le cause. Pour trouver ces bugs, il faut investir dans un Large Hadron Debugger…</li>
<li>Le Hindenbug : un bug détruisant les données de manière catastrophique. Souvent c’est un humain.</li>
<li>Le contre-bug : un bug que vous montrez à la personne qui l’a causé lorsque cette personne vous montre un bug.</li>
<li>Le Bloombug : un bug qui rapporte accidentellement de l’argent.</li>
<li>Le Schrödinbug : se réfère à une fonctionnalité qui fluctue apparemment entre boguée et correcte (comme le <a href="https://fr.wikipedia.org/wiki/Chat_de_Schr%C3%B6dinger" target="_blank">chat de Schrödinger</a>, à la fois vivant et mort), jusqu’à ce que quelqu’un regarde le code (ouvre la boîte) , moment dès lequel la fonctionnalité devient boguée de façon permanente.</li>
<li><img alt="" border="0" height="176" src="http://4.bp.blogspot.com/-oPGnuNG3we8/TtIQdy_gWxI/AAAAAAAAAGk/D04COII0QGk/s200/loch-ness-monster-bug.jpg" width="200"/>Le Bug Monstre du Loch Ness Monster Bug : un bug qui ne peut pas être reproduit ou n’a été vu que par une seule personne.</li>
<li>Le Bug OVNI : un bug rapporté par des clients qui, même lorsqu’on leur montre que le bug n’existe pas, continuent à le rapporter encore et encore croyant qu’il est réel.</li>
<li>Le Mandelbug  : un bug dont les causes sont si complexes que son comportement apparaît chaotique ou même non déterministe. Nommé d’après <a href="https://fr.wikipedia.org/wiki/Beno%C3%AEt_Mandelbrot">Benoît Mandelbrot</a>, découvreur des fractales.</li>
<li>Le bug en sac de papier brunBrown : un bug dans un logiciel public si gênant que son auteur se cache la tête dans un sac de papier brun pendant quelques temps</li>
<li>Le bug de l’apprenti sorcier : un bug dans un protocole qui, dans certaines circonstances, cause l’envoi de multiple messages dont chacun redéclanche le même bug</li>
<li>Le bug de la copine folle : un bug dont l’effet immédiat est invisible, l’application semblant à première vue fonctionner normalement et vous disant qu’elle fonctionne normalement.</li>
<li>Le bug Excalibur : celui que tous les employés de l’entreprise ont tenté de résoudre, mais aucun n’a été assez valeureux pour y arriver.</li>
<li>Le printf indispensable : lorsqu’une ligne de debug est indispensable pour que le code fonctionne. Le programme bogue si on l’enlève.</li>
</ul>
<h3>Les differents types de code</h3>
<div>
<ul>
<li>
<h3><img alt="" border="0" height="191" src="http://1.bp.blogspot.com/-LiaCumm4kHQ/TtIQOZuVBNI/AAAAAAAAAGU/And_DNBTzaw/s1600/baklava-code.jpg" width="288"/></h3>
<p>Le code Spaghetti : code avec trop de GOTO, d’exceptions, de  threads ou d’autres constructions de branchements non structurés. Le flux du programme ressemble à un plat de spaghetti emmêlés.</p></li>
<li>Le code Spaghetti avec boules de viande : Une tentative de code orienté objet, mais où le résultat final reste dépendant de code procédural emberlificoté (spaghetti.</li>
<li>Le code Baklava : code avec trop de couches. Appelé aussi code Lasagne.</li>
<li>Le code Ravioli : code orienté objet constitué d’un grand nombre de petits copmposants mal liés.</li>
<li>Le code Saucisse : Une fois que vous avez examiné ce code en détail pour voir de quoi il est fait, vous ne voulez plus jamais l’utiliser.</li>
<li>Le code <a href="http://fr.wikipedia.org/wiki/Jenga" target="_blank">Jenga</a> : l’ensemble s’effondre dès que vous y touchez.</li>
<li>Le code <a href="https://fr.wikipedia.org/wiki/Hydre_de_Lerne" target="_blank">Hydre</a> : code qui ne peut être corrigé. Chaque correction provoque deux nouveaux bugs. Il faut le réécrire.</li>
<li>Code sparadrap : tout code transformé en commentaire mais toujours inclus dans la version courante.</li>
<li>Le code putain : code problématique qui fait que l’application se couche souvent.</li>
<li>Le rouge à lèvres de cochon : code comportant beaucoup de vieux code historique ou spaghetti caché derrière des classes enveloppes (wrappers). Il apparait aux nouveaux développeurs comme bien conçu, élégant, orienté objet. Ce n’est que lorsqu’ils travaillent dessus qu’ils réalisent à quel point il est moche.</li>
<li>Le code hypothécaire : code volontairement si compliqué que vous seul pouvez le maintenir, forçant votre employeur à vous garder, ce qui vous permet de payer votre hypothèque.</li>
<li>Le code Ghetto : portion de code particulièrement inélégante et suboptimale, mais qui cependant satisfait les spécifications.</li>
<li>le code Couteau Suisse : code qui souffre de spécifications rampantes (feature creep) : il fait plein de choses, mais ne fait rien bien.</li>
<li>Code NP rusé : un algorithme dont la complexité est trop dure à comprendre par le simple mortel.</li>
<li>Code NP hilarant : un algorithme dont la complexité est une plaisanterie, littéralement comme le <a href="https://fr.wikipedia.org/wiki/Tri_stupide" target="_blank">BogoSort </a>par exemple, ou métaphoriquement,</li>
<li>NP Hilarious Code – An algorithm whose complexity is « a joke », literally (as in BogoSort) or metaphorically.</li>
<li>Le code « coupé-gaspillé » (Cut-and-waste) : lorsque quelqu’un a coupé/collé du code touvé en ligne (souvent depuis un blog) dans un code de production. le résultat est souvent beaucoup de temps perdu à traquer un bug obscur d’un code qui avait sans doute du sens dans le contexte d’origine, mais pas dans notre application. Aussi appelé « Blog Driven Development » (BDD).</li>
<li>Le code « vélo du quartier » : un module ou bout de code que tous les programmeurs de la boîte ont touché.</li>
<li>Le code traces de gomme : code qui a été écrit puis refactoré de nombreuses fois, laissant du vieux code dans son sillage. Comme lorsqu’on efface du papier plusieurs fois, on ne voit plus les traces du crayon mais la grosse tache de la gomme.</li>
<li>Le code « objetfusqué » : code orient objet qui a été abstrait à tellement de niveaux que plus personne ne peut le comprendre.</li>
<li>Code Bernacle: tout bout de code (souvent une méthode statique) qui a été ajouté à une classe à laquelle il n’appartient pas vraiment, en raison de l’absence d’un autre endroit logique où le mettre.</li>
<li>Code en pilotage automatique : code écrit par un programmeur qui était en « pilotage automatique » ou ne réfléchissait pas vraiment à ce qu’il faisait.</li>
<li>Protoduction : un prototype qui finit en production</li>
</ul>
</div>
<p>voir aussi : le « <a href="http://www.catb.org/jargon/index.html" target="_blank">Jargon File</a> »</p>
</div>

## Commentaires

### kévin — 3 septembre 2013 à 21:14

<section class="comment-content comment">
<p>il y a aussi le {;}</p>
 </section>

### kévin — 3 septembre 2013 à 21:27

<section class="comment-content comment">
<p>et le programmeur parano (appelé aussi compteur geger) :</p>
<p>if (a==42)<br/>
{<br/>
    if (a!=42)<br/>
    {<br/>
        printf (« Oups… Des particules relativistes traversent votre ordinateur \n Si ce n’est pas la première foi que vous voyez ce message fuyez !!! »);</p>
<p>    }<br/>
}</p>
 </section>

### michel von — 3 septembre 2013 à 21:42

<section class="comment-content comment">
<p>Mes deux préférés:<br/>
Le code putain et le code rouge à lèvres de cochon…</p>
<p>Amitiés<br/>
michel von</p>
 </section>

### michel von — 3 septembre 2013 à 21:43

<section class="comment-content comment">
<p>Mais attention: n’en tirez pas de conclusions hâtives !…<br/>
(complément au message précédent)</p>
 </section>

### Proteos — 3 septembre 2013 à 21:53

<section class="comment-content comment">
<p>« barnacle » se traduit par « bernacle » en français. Un coquillage impossible à décoller du rocher auquel il est accroché. Un truc que les continentaux ne peuvent connaître.</p>
 </section>

### ↳ Réponse — Goulu — 4 septembre 2013 à 04:57

<section class="comment-content comment">
<p>J’avais cherché mais je n’avais trouvé que bernacle=oie sauvage. Merci je corrige</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
