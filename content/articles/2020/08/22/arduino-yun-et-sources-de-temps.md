---
title: "Arduino Yun et sources de temps"
date: "2020-08-22T07:50:13"
lastmod: "2020-08-22T07:50:14"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["arduino", "enregistrements", "horodatage", "log", "ntp", "rtc", "synchronisation"]
url: "/2020/08/22/arduino-yun-et-sources-de-temps/"
wordpress_id: 4809
comment_count: 0
---
<p>Les machines qui doivent enregistrer des informations avec précision se doivent d’avoir une source (ou mieux : plusieurs) sources de temps.</p>
<p>Dans un domaine que je connais particulièrement bien, il y a les carrefours à feux. L’horloge interne est pilotée par des sources de temps, qui sont étagées de la plus à la moins précise :</p>
<ul>
<li>La centrale de trafic</li>
<li>Le GPS</li>
<li>L’horloge radio DCF</li>
<li>Le quartz du CPU</li>
<li>Le 50 Hz du secteur</li>
</ul>
<p>Si la source de temps ne délivre pas son signal, on se rabat sur la source inférieure. C’est certes un cas extrême.</p>
<p>Le temps étant un thème extrêmement vaste, je vais limiter cet article au temps donné par une RTC (real time clock) et sa correction par NTP, le network time protocol. Pour plus de précision sur le NTP, consultez <a href="https://fr.wikipedia.org/wiki/Network_Time_Protocol">https://fr.wikipedia.org/wiki/Network_Time_Protocol</a></p>
<p>Pour faire simple, on a au sommet de la pyramide des ordinateurs « horloge mère » distribuant le temps sur le réseau Internet. Les ordinateurs de la couche 1, ont une relation privilégiée qui leur permet une grande précision de la référence de temps.</p>
<p><img height="335" src="/media/2020/08/word-image-1.png" width="375"/></p>
<p>Ceux des couches inférieures peuvent être aussi une référence pour synchroniser un pool d’ordinateurs. Ils pratiquent en plus, une gestion parallèle pour améliorer la fiabilité et la précision. Le NTP permet que les délais dus au réseau soient calculés pour en tenir compte.</p>
<p>La source de temps RTC utilisée dans le cadre de mon projet de compteur Geiger (<a href="https://github.com/ymasur/geiger">https://github.com/ymasur/geiger</a> ) est le chip horloge DS3231. La partie Internet est assurée par l’Arduino Yun comportant le Linux Linino, alors que la partie real-time de collection des données et leur enregistrement est réalisée par la partie Arduino Atmega 32U4. Elle est similaire à un Arduino Leonardo.</p>
<h1>Pourquoi deux sources de temps ?</h1>
<p>Voilà la bonne question. Si on se base sur une RTC, comme toute montre de poignet, bien nommée garde-temps, elle garde le temps selon sa précision intrinsèque. Et donc elle finit par dériver, en avance ou en retard.</p>
<p><img height="330" src="/media/2020/08/word-image-2.jpeg" width="338"/></p>
<p>La précision donnée par le fabricant de la RTC (surnommée Extremely Accurate I2C-Integrated) est : Accuracy ±2ppm from 0°C to +40°C. Si la température dépasse, on arrive à 3ppm, partie par million.</p>
<p><img height="326" src="/media/2020/08/word-image-3.jpeg" width="459"/></p>
<p>Comme on a 31’536’000 secondes par an, on peut s’attendre à une dérive d’environ 64 secondes à 2 ppm. Certes, sur une année c’est peu. Mais on doit tout de même prévoir de la remettre à l’heure.</p>
<p>La source NTP est, elle, exacte. Elle intègre aussi la seconde intercalaire, due au ralentissement de la rotation de la terre si besoin. Mais… si l’Internet n’est pas à disposition, pas de NTP ! Par exemple, si le WiFi est éteint, ou le réseau inatteignable par l’Arduino pour toutes sortes de raisons.</p>
<p>La RTC prend dans ce cas toute sa valeur. En cas d’indisponibilité du NTP, on utilisera la RTC. Elle peut fournir une précision à la seconde pendant au moins 5 jours (nb jours/an : dérive -&gt; 365/64 = 5.7)</p>
<h1>Méthode de synchronisation</h1>
<p>A quelle fréquence faut-il remettre la RTC à l’heure ? Aussi peu que possible, mais aussi souvent que nécessaire. Ä cause du passage à l’heure d’été (casse-tête classique, qui est en voie de disparition, mais en attendant, il faut en tenir compte) on évite de le faire la nuit entre 1h et 2h. 3h est un bon candidat. Le test doit se faire tous les jours.</p>
<p>Mais avant de se lancer dans une mise à l’heure, encore faut-il avoir le NTP opérationnel ! Voici donc la proposition complète.</p>
<h1>Au démarrage</h1>
<p>L’Arduino boote quasi en 2 secondes, alors que la partie Unix du Yun prend (au moins) une minute, et doit encore se connecter au WiFi ou au réseau. On utilise donc en premier la RTC. Il s’agit tout même de la tester : elle peut être neuve et non réglée, ou sa pile est à bout de course.</p>
<p>Dans les extraits de code qui suivent, display_info(« msg ») affiche une ligne sur le LCD, et log_msg(« msg ») ajoute une ligne au fichier de log et l’imprime sur le port série. Voici le code de setup() qui concerne l’horloge :</p>
<p><img height="240" src="/media/2020/08/word-image-2.png" width="499"/></p>
<p>On obtient l’heure RTC, après ces quelques tests indispensables : est-t-elle connectée ? a-t-elle perdu son alimentation (pile) ? Elle a peut-être une dérive, mais elle est réputée OK. La structure myTime est initialisée. C’est cette date/heure qui est utilisée par le montage, jusqu’à ce que le NTP soit utilisable. Pour amorcer sa lecture, la dernière instruction de startup() est :</p>
<p>timeSyncStep <strong>=</strong> 1<strong>;</strong> // starts NTP sync</p>
<p>Voyons maintenant comment agencer la synchronisation.</p>
<h1>Appels de la boucle principale</h1>
<p>A partir d’une des boucles principales, ici poll_loop1<strong>()</strong> qui est appelée chaque seconde, on vérifie si la fenêtre de synchronisation est ouverte. Soit si l’occurrence de 3h survient :</p>
<p><img height="80" src="/media/2020/08/word-image-3.png" width="551"/></p>
<p>De plus, l’appel à la fonction de synchronisation est fait :</p>
<h1><img height="22" src="/media/2020/08/word-image-4.png" width="482"/></h1>
<h1>Obtenir le temps Unix</h1>
<p>Le dialogue entre la partie Arduino U32 et la partie Unix se fait par série. L’avantage est que les deux parties tournent de manière très indépendante. Le désavantage est qu’il faut passer par des chaînes de caractères autant pour la commande que pour traiter le résultat.</p>
<p>Comme ce genre de commande est un processus plutôt lent, on n’y fait appel que lorsque c’est nécessaire. C’est-à-dire que le temps sera lu de la RTC ; et celle-ci sera mise à jour au moins une fois par jour via le temps NTP, via une commande Unix.</p>
<h1>Synchronisation</h1>
<p>La fonction timSync() est donc appelé chaque seconde. Après les déclarations de variables locales, le premier test est : si aucune synchronisation n’est nécessaire, on ressort immédiatement :</p>
<p><img height="42" src="/media/2020/08/word-image-5.png" width="485"/></p>
<p>Le pas de synchronisation est démarré par le setup() ou ensuite par le passage à 3h00 décelé dans la boucle qui tourne à la seconde. Une fois démarré, la variable est incrémentée à chaque appel. Seulement si la variable vaut 1, la suite de la synchronisation sera traitée. Si supérieur à 1, retour immédiat.</p>
<p><img height="61" src="/media/2020/08/word-image-6.png" width="546"/></p>
<p>On va chercher le temps Unix, basé sur le NTP, et comme il est en ASCII, il s’agit de le convertir et de renseigner la structure ntp_time :</p>
<p><img height="240" src="/media/2020/08/word-image-7.png" width="391"/></p>
<h2>Piège du NTP au démarrage</h2>
<p>Avant de prendre cette valeur comme exacte, il s’agit de vérifier si le Yun a bien eu le temps de se connecter sur l’Internet… En effet le Yun a un mécanisme qui consiste à prendre la date du fichier le plus récent, et de la considérer comme utile jusqu’à la connexion sur un serveur NTP !</p>
<p>En cas de coupure de courant brève, la différence de temps entre le Yun et la RTC peut être que de 3 minutes ! C’est peu, mais beaucoup pour un système prévu pour travailler à quelques secondes près ! On ne peut pas filtrer sur un écart aussi faible. D’une part, lors du changement de l’heure d’été/hiver, la différence est de 3600 secondes. Et si l’horloge a été remplacée, ou que sa pile est neuve, elle ne serait jamais corrigée.</p>
<p>Pour contourner ce problème, j’ai ajouté une commande au démarrage du Yun qui force son l’horloge Unix à la date du 01.01.2001. Dès lors, il n’y a plus de doute. Si la date retournée est plus petite que 2020, on ne l’utilise pas.</p>
<p><img height="146" src="/media/2020/08/word-image-8.png" width="666"/></p>
<h2>Indication de l’écart</h2>
<p>L’écart entre les deux horloges est calculé et logué. Une compilation conditionnelle permet d’éliminer ces logs, si on estime qu’ils ne sont plus nécessaires, une fois le dispositif mis au point.</p>
<p><img height="178" src="/media/2020/08/word-image-9.png" width="623"/></p>
<h2>Plage de correction</h2>
<p>Une précaution supplémentaire consiste à ne corriger l’horloge que si l’écart est supérieur à une valeur donnée. On prend la valeur absolue, et on la compare à l’écart max admissible :</p>
<p><img height="402" src="/media/2020/08/word-image-10.png" width="623"/></p>
<p>Si la différence est dans la fourchette admissible, on ne fait rien de plus. Autrement, nous ajustons la valeur de la RTC à celle du NTP, avec le message idoine :</p>
<p><img height="82" src="/media/2020/08/word-image-11.png" width="609"/></p>
<p>L’avantage de la fourchette est de vérifier dans quelle mesure l’horloge dérive. En effet, si elle est de mauvaise qualité, on n’aura pas l’occasion de voir comment sa dérive se produit en corrigeant (ou pas !) par l’ajustage chaque jour.</p>
<h1>Résultat</h1>
<p>Les résultats suivants sont issus des logs du compteur Geiger, implémentant ce code.</p>
<p>2020-03-28 03:00:00 Get NTP time…</p>
<p>2020-03-28 03:00:00 T Correction: 2</p>
<p>2020-03-28 03:00:00 Time NTP = RTC</p>
<p>2020-03-29 03:00:00 Get NTP time…</p>
<p>2020-03-29 03:00:00 T Correction: 3602</p>
<p>2020-03-29 03:00:00 Get NTP time…</p>
<p>2020-03-29 03:00:00 NTP used for RTC</p>
<p>Le 28.03.2020, l’écart est de 2 secondes. Comme il est inférieur à MIN_CORRECTION, on n’ajuste pas la RTC. Par contre, au changement d’heure d’été, l’écart prend 3600 secondes supplémentaires et devient 3602 secondes et là, bien sûr, on ajuste ! Le message « NTP used for RTC » le confirme.</p>
<h1>Conclusion</h1>
<p>Obtenir une source de temps fiable et continue au fil du temps demande une logique bien testée pour pallier aux événements tels la dérive, la coupure de courant, voir le redémarrage du système par le watchdog.</p>
<p>Ces événements ne manqueront pas de troubler l’horodatage des mesures enregistrées sur le système. La méthode présentée ci-dessus montre sa robustesse et répond aux critères posés.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
