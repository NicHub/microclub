---
title: "Eau chaude – Calcul de constante de temps"
date: "2018-01-05T21:27:44"
lastmod: "2018-01-09T21:18:29"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["analyse", "arduino", "chauffage-solaire", "ecs", "exponentielle", "python", "yun"]
url: "/2018/01/05/eau-chaude-calcul-de-constante-de-temps/"
wordpress_id: 3592
comment_count: 0
---
<h2>Préambule</h2>
<p>Grâce au montage basé sur un Arduino Yun, je peux monitorer en quasi temps réel par un échantillonnage toute les 10 minutes, l’état du volume de l’eau chaude sanitaire (ECS). Ces données sont enregistrées : un fichier par mois, comprenant une ligne par mesure. On a, séparé par TAB pour un copier-coller facile dans Excel:</p>
<ul>
<li>Date, année/mois/jour</li>
<li>Temps, heure : minute :seconde</li>
<li>Marche de la pompe des panneaux solaires, en pourcent</li>
<li>Température de retour des panneaux solaires</li>
<li>Température du volume d’eau solaire (ES)</li>
<li>Température du volume d’eau chaude sanitaire</li>
</ul>
<p>Le système est décrit ici : <a href="/2014/10/11/yun-monitoring-de-leau-solaire/">https://microclub.ch/2014/10/11/yun-monitoring-de-leau-solaire/</a></p>
<p>Il fonctionne impeccablement ; le Yun est véritablement un excellent produit. Le résultat est visible ici : <a href="http://yvesmasur.ch/ecs/">http://yvesmasur.ch/ecs/</a> ; il est possible également de visionner les données plus anciennes par le formulaire de la page WEB ; avec la case « Tout » cochée, les échantillons par 10 minutes sont affichés.</p>
<p>Fig.0 – DATA ECS</p>
<p><img height="318" src="/media/2018/01/word-image.jpeg" width="718"/></p>
<h2>Analyse plus détaillée</h2>
<p>LA question qu’on me pose souvent, c’est l’apport solaire ? Pour le trouver, c’est assez simple. Le temps d’utilisation de la pompe étant stocké – colonne ‘Pompe’, en pourcent de tranche de 10 minutes – il est facile d’en extraire son temps de fonctionnement ; et en plus, connaissant sa puissance, de calculer l’énergie électrique utilisée… Et oui, le solaire demande (un peu) de puissance au réseau !</p>
<p>Une autre question intéressante, c’est la durée de l’ECS utilisable : combien de jours tient le stockage ?</p>
<p>Avant tout, il s’agit de connaître le fonctionnement du système. Et de son usage. En gros, personne ne se douche après minuit ; ni ne se rase avant 6h le matin : il n’y a pas de soutirage d’eau chaude dans cette tranche de temps. De plus, la chaudière ne remonte la température qu’une demi-heure avant l’enclenchement du chauffage, et seulement si nécessaire. En principe, la consigne est de 45°C. En examinant les données, on voit qu’il faut que la température ECS doive passer en dessous de 43°C (ou même baissé à 38° si le circuit solaire a démarré) ; et que la chaudière s’arrête à environ 48°C. On peut donc, grosso-modo prendre la température à minuit ; puis à 6 heure pour calculer quelque chose.</p>
<h2>Modèle de calcul</h2>
<p>La température de l’eau chaude va diminuer pour atteindre, si l’on ne fait rien, la température ambiante. Une telle décroissance est assimilable à celle bien connue des électroniciens : un réseau RC, ou le condensateur se (dé)charge dans une résistance.</p>
<p>Fig. 1 – Exponentielle décroissante</p>
<p><img height="755" src="/media/2018/01/word-image-1.jpeg" width="968"/></p>
<p>On a là une exponentielle décroissante de la tension, caractérisée par sa constante de temps Tau. Dans la fig.1, la valeur de Tau simulée sur Excel est de 10. A t=10, on a 0.368 de la valeur à t=0.</p>
<p>Exemple : <a href="https://fr.wikipedia.org/wiki/D%C3%A9charge_d%27un_condensateur">https://fr.wikipedia.org/wiki/D%C3%A9charge_d%27un_condensateur</a></p>
<p>Il suffit de considérer que la température est la tension ; et le tour est joué… ? Il y a toutefois un problème. A moins de m’attirer les foudres des occupants, je ne peux pas couper la chaudière pour plusieurs jours, et encore moins interdire l’utilisation d’eau chaude… D’où l’idée de travailler sur les données disponibles. A savoir, une petite portion de l’exponentielle située entre minuit et 6h du matin, enregistrée régulièrement par l’Arduino Yun.</p>
<h2>Paramètres et équation</h2>
<p>Théoriquement, il suffit de prendre des données précises sur la tranche de temps utilisable, et de lancer le calcul pour connaitre cette fameuse constante de temps. Qui devrait être valable pour toute autre jeu de données. Mais quel calcul ? On a trois points en ordonnée :</p>
<ul>
<li>Température à 0h00 : V0</li>
<li>Température à 6h00 : V6</li>
<li>Température ambiante : Va</li>
</ul>
<p>Et bien sûr en abscisse, le temps t de 6h entre les deux mesures V0 et V6. Par rapport au circuit électrique, la température peut être assimile à la tension. La capacité est le volume d’eau qui emmagasine de la chaleur, la résistance est la résistance thermique de l’isolation qui isole le volume d’eau de la température ambiante. On ne les connait pas, et cela ne fait rien : seul leur produit – la constante de temps Tau – est recherché.</p>
<p>Remarquons aussi que la valeur de Va à t = ∞ n’est pas de 0 ; mais la température ambiante reste autour des 20°C. Vous allez me dire que la sonde au retour des panneaux n’est pas une température ambiante ? En fait, si. La nuit le circuit est (normalement !) arrêté ; et la sonde est disposée entre l’isolation et le tube en cuivre dans la buanderie.</p>
<p>Les choses étant posées, la meilleure solution est de consulter le Dr Goulu (PhD, R&amp;D engineer, Lean manager, Science blogger), qui saura nous dire comment faire. Je lui ai donc posé la question par email avec comme exemple: V0=61.9, V6=60.0 ; c’était l’été et il faisait chaud… Voici sa réponse (notez que Tau est indiqué ‘T’ dans le message) :</p>
<p>Hello,</p>
<p>Si j’ai bien compris, il te faut fitter une fonction a*(1-e^(-t/T))+b par tes points et l’asymptote pour obtenir  T …</p>
<ul>
<li>A t=0 tu as b=61.9</li>
<li>à t infini tu as a+b = 22.3 donc a =22.3-61.9 = -39.6</li>
<li>à t = 6 heures tu as a*(1-e^(-6/T))+b = 60 à résoudre pour T</li>
</ul>
<p>Comme il se fait tard : <a href="https://www.wolframalpha.com/input/?i=-39.6*%281-e%5E%28-6%2FT%29%29%2B61.9+%3D+60+for+T">https://www.wolframalpha.com/input/?i=-39.6*(1-e%5E(-6%2FT))%2B61.9+%3D+60+for+T</a></p>
<p>donne T ~ 122 heures.</p>
<p>Merci Dr Goulu ! Wolfram Alpha est décidément un puissant outil. En prenant les valeurs de quelques jours avec des températures de départ différentes, je vois clairement que mon modèle est entaché d’erreur. La constante de temps… est très variable ! Il me faut un outil plus facile d’accès et automatique pour cerner Tau.</p>
<h2>Equation de base</h2>
<p>En consultant l’excellent livre « The art of electronics », 4<sup>ème</sup> édition, p. 22 je peux en tirer l’équation générale me permettant de calculer la constante de temps, sans passer par Wolfram Alpha. La voici :</p>
<p>Tau = dt / ln ((V0 – Va)/(V6 – Va))</p>
<h2>Sensibilité aux erreurs</h2>
<p>Les mesures ne sont pas parfaites ; les sondes enregistrent au 1/10 de degré. A noter que dans cette affaire la précision absolue compte moins que la résolution. Excel est mon ami ; je pose des valeurs représentatives et je modifie un paramètre à la fois, pour en observer l’influence sur le résultat.</p>
<p>Equation de Tau (en ligne 2, colonne A) est introduite:</p>
<p>=6/LN((C2-E2)/(D2-E2))</p>
<table>
<tbody>
<tr>
<td><strong>Tau</strong></td>
<td><strong>Var</strong></td>
<td><strong>V0</strong></td>
<td><strong>V6</strong></td>
<td><strong>Va</strong></td>
<td><strong>Paramètre modifié</strong></td>
</tr>
<tr>
<td>93.60</td>
<td>0.00</td>
<td>49.8</td>
<td>47.9</td>
<td>19.2</td>
<td>Aucun</td>
</tr>
<tr>
<td>93.28</td>
<td>0.32</td>
<td>49.8</td>
<td>47.9</td>
<td>19.3</td>
<td>temp. moyenne entre 0h et 6h</td>
</tr>
<tr>
<td>89.07</td>
<td>4.53</td>
<td>49.9</td>
<td>47.9</td>
<td>19.2</td>
<td>écart -0.1 de V0</td>
</tr>
<tr>
<td>98.64</td>
<td>-5.04</td>
<td>49.7</td>
<td>47.9</td>
<td>19.2</td>
<td>écart +0.1 de V0</td>
</tr>
<tr>
<td>88.77</td>
<td>4.83</td>
<td>49.8</td>
<td>47.8</td>
<td>19.2</td>
<td>écart -0.1 de V6</td>
</tr>
<tr>
<td>98.97</td>
<td>-5.37</td>
<td>49.8</td>
<td>48.0</td>
<td>19.2</td>
<td>écart +0.1 de V6</td>
</tr>
<tr>
<td>91.00</td>
<td>2.60</td>
<td>49.8</td>
<td>47.9</td>
<td>19.2</td>
<td>écart de 10 minutes</td>
</tr>
</tbody>
</table>
<p> </p>
<p>Où l’on voit qu’une erreur minime de mesure de 0.1 °C de V0 ou de V6 se traduit par un écart considérable de Tau d’environ 5%. C’est notamment dû au fait que l’on a à disposition <strong>une portion très limitée</strong> de l’exponentielle de décroissance : 6H pour un Tau d’environ 100H.</p>
<h2>Allure des courbes</h2>
<p>Avant de se lancer dans le logiciel permettant de calculer sur un grand nombre de cas, il est bon de voir l’évolution des températures avec des cas typiques. Puis, à partir des éléments constatés, de construire un modèle s’approchant au mieux de la réalité.</p>
<p>Fig. 2 – par temps froid</p>
<p><img height="659" src="/media/2018/01/word-image-2.jpeg" width="733"/></p>
<p>L’eau chaude sanitaire (ECS) décroit, et elle est en dessous de la valeur de consigne de la chaudière. Un peu avant 6H, le brûleur à gaz remonte rapidement la température ECS à 48°C, ainsi prête pour son utilisation matinale. Le point de décroissance minimal est donc <strong>avant</strong> 6H ; à 5H40 ou à 5H50. La durée de mesure sera également raccourcie d’autant.</p>
<p>On remarque aussi que la température <strong>ambiante varie</strong> : elle baisse de 19° à 16°. De plus, le volume d’eau solaire n’a non seulement reçu aucune énergie solaire, mais <strong>il est réchauffé</strong> par le volume d’eau sanitaire…</p>
<p>Fig. 3 – tempéré</p>
<p><img height="681" src="/media/2018/01/word-image-3.jpeg" width="734"/></p>
<p>Ici, il y a un apport d’énergie solaire stocké ; le gaz n’est pas utilisé, du moins pour l’ECS. On est en octobre ; probablement que le chauffage des radiateurs lui, fournit par la même installation, s’est mis en route. Ceci se déduit en voyant la valeur ambiante augmenter à partir de 6h40. Le volume d’eau solaire suit une pente parallèle à l’ECS.</p>
<p>Fig. 4 – temps chaud</p>
<p><img height="679" src="/media/2018/01/word-image-4.jpeg" width="725"/></p>
<p>L’apport solaire est conséquent et amplement suffisant, puis que la nuit l’ECS est à plus de 56°C. Les courbes autant de l’ECS que de l’ES sont parallèles ; tout au plus un léger fléchissement à partir de 8H par soutirage. L’eau froide du réseau commence par refroidir l’ES, alors que l’ECS reçoit de l’ES à peine moins chaude de 2°C. On voit ici l’intérêt d’avoir deux volumes séparés. La valeur de Va diminue d’environ 3°C pendant la nuit.</p>
<h2>Modèle amélioré</h2>
<p>Premier constat : la température du seul volume de l’ECS n’est pas suffisante pour déterminer Tau. En effet, une partie de son énergie <strong>passe dans le volume d’ES</strong> en le réchauffant ! les deux volumes étant identique (dans mon cas, chacun 200 litres), il faut utiliser une pondération de 0.5 des deux pour tenir compte du transfert d’énergie. Cela se voit dans l’exemple 1 : la forte décroissance de l’ECS (qui conduirait à un Tau faible) est atténuée par la pente positive de l’ES. On sera ainsi bien plus précis.</p>
<p>Second constat : la température ambiante Va varie. Laquelle (voire lesquelles) prendre ? La sensibilité de cette valeur dans le calcul est heureusement moindre. Celle qui semble le mieux convenir est celle à mi-parcours temporel : à 3h00 du matin.</p>
<p>Troisième constat : la valeur de V6 peut être fausse si la chaudière s’enclenche avant 6H. L’algorithme devra donc traquer le minimum et prendre l’échantillon adéquat, tout en corrigeant la durée qui devient alors inférieure à 6h00.</p>
<h2>Programme et résultats</h2>
<p>Afin d’avoir un suivi régulier de la valeur de Tau, j’ai élaboré un programme en Python. Il est disponible sur <a href="https://github.com/ymasur/ecs-calc">https://github.com/ymasur/ecs-calc</a></p>
<p>Il permet de créer un rapport par mois, mais accepte aussi des valeurs partielles : C’est utile pour monitorer les résultats au jour le jour.</p>
<p>Le programme est divisé en modules :</p>
<ul>
<li>ecs-calc.py : le programme principal</li>
<li>esetup.py : constantes et traite les arguments de la ligne de commande</li>
<li>samples.py : lit et met les données en structure</li>
<li>energy.py : calcule le pourcentage solaire et l’énergie de la pompe de circulation</li>
<li>temperatures,py : calcul de Tau</li>
</ul>
<h2>Hostspot sur des fonctions clés</h2>
<h3>Fonction add_points() – extrait</h3>
<p><img height="488" src="/media/2018/01/word-image-5.jpeg" width="824"/></p>
<p>La liste des points des échantillons ‘datas’ de 10 minutes est parcourue. Remarquez l’avantage du langage de haut niveau pour scanner la liste en ligne 91. Pour ne pas m’embêter avec des fonctions date et heure, le temps du jour est lu en minutes dans ‘s.mm’. Le point V0 déterminé à 0h00 (ligne 93), Va à 3h00 (ligne 97), V6 traqué au minimum dès 5h00. Une fois déterminé, le Tpoint est instancié à la ligne 109. Pour traiter des valeurs partielles, le nombre de Tpoints est maintenu à la ligne 113.</p>
<h3>Classe Tpoint</h3>
<p>Met en structure une mesure. Le Tau est calculé et mis en boite à la ligne 35.</p>
<p><img height="530" src="/media/2018/01/word-image-6.jpeg" width="797"/></p>
<p>Pour que le programme fonctionne non seulement sur PC mais aussi en automatique sur l’Arduino Yun, il a fallu encore :</p>
<ul>
<li>convertir les fichiers Python au format UNIX, avec LF en fin de ligne ;</li>
<li>ajouter en 1<sup>ère</sup> ligne le commentaire #!/usr/bin/python ;</li>
<li>supprimer les accents dans les print() console ;</li>
<li>ajouter le path du programme au nom du fichier de donnée</li>
</ul>
<p>Le dernier point est étonnant, car ils sont dans le même répertoire. Mais le CRON destiné à son lancement régulier n’en sait rien…</p>
<h2>Conclusion</h2>
<p>Collecter des (big) datas, c’est bien ; les analyser et en tirer des informations, c’est mieux !</p>
<p>L’isolation des volumes d’ES et d’ECS n’est pas extraordinaire, avec un Tau d’environ 100 heures ; donc utilisable pendant 48h à une température suffisante. Si le choix est possible – ça prend de la place -, on remarque qu’il serait bon d’avoir une capacité de stockage bien supérieure et un Tau de 240 heures, de manière à consommer de l’eau réchauffée gratis par le soleil même pendant 4-5 jours couverts, ceci sans augmenter la surface des panneaux solaires.</p>
<p>Prochaine étape : calculer l’économie de gaz. Vous avez vu comme moi la courbe 2 – par temps froid ; la pente est reconnaissable. Mais je dois trouver le bon modèle. A suivre !</p>
<h2>Références</h2>
<ul>
<li>livre « The art of electronics », 3ème édition, Paul Horowitz et Winfield Hill</li>
<li>Article « https://microclub.ch/2014/10/11/yun-monitoring-de-leau-solaire/ »</li>
</ul>
<p>Yves Masur (1/2018)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
