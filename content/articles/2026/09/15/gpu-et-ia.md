---
title: "GPU et IA"
date: "2026-09-15T11:19:48"
lastmod: "2026-09-15T11:19:49"
author: "Jean-Pierre Broillet"
featureimage: "images/articles/gpu-ia.svg"
categories: ["Microclub"]
tags: []
url: "/2026/09/15/gpu-et-ia/"
wordpress_id: 5826
comment_count: 0
---
<p><strong>La carte RTX 3090 (28 milliards de transistors) son impact sur l’IA et la question philosophiques sous-jacente</strong></p>
<p>Le sujet est plus profond qu’il n’y paraît, car la <a href="https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/?utm_source=chatgpt.com">RTX 3090</a> est un bon exemple d’un phénomène historique : <strong>un composant conçu principalement pour le graphisme est devenu une petite machine de calcul neuronal accessible aux particuliers</strong>.</p>
<p><img alt="Image" height="750" src="/media/2026/09/image.jpeg" width="1000"/></p>
<p><strong>1. Pourquoi un GPU est-il si adapté à l’IA ?</strong></p>
<p>Un processeur classique possède relativement peu de cœurs très sophistiqués.</p>
<p>Un GPU adopte presque la philosophie inverse : énormément d’unités de calcul relativement simples travaillant simultanément.</p>
<p>Or un réseau neuronal passe une énorme partie de son temps à effectuer des opérations du genre :</p>
<p><img height="30" src="/media/2026/09/word-image-5826-2.png" width="149"/></p>
<p>c’est-à-dire des <strong>multiplications matricielles</strong>. Prenons une couche d’un réseau :</p>
<p><img height="36" src="/media/2026/09/word-image-5826-3.png" width="165"/></p>
<p>avec :</p>
<p><img height="98" src="/media/2026/09/word-image-5826-4.png" width="222"/></p>
<p>Pour quelques neurones, rien d’impressionnant, de difficile. Mais avec des milliards de paramètres, il faut effectuer <strong>des milliards d’opérations similaires</strong>.</p>
<p>Et c’est précisément ce que les GPU savent faire extrêmement efficacement.</p>
<p><strong>2. Les Tensor Cores changent encore la situation</strong></p>
<p>Avec les RTX, NVIDIA a ajouté des circuits spécialisés : les <strong>Tensor Cores</strong>.</p>
<p>Ils sont particulièrement adaptés aux opérations matricielles utilisées par l’apprentissage profond.</p>
<p>Schématiquement :</p>
<p><img height="22" src="/media/2026/09/word-image-5826-5.png" width="163"/></p>
<p>peut être réalisée massivement en parallèle. Ainsi la RTX 3090 n’est plus simplement : « une carte graphique très rapide ». Elle devient pratiquement : <strong>un accélérateur de calcul matriciel vendu au grand public.</strong></p>
<p>C’est une différence conceptuelle considérable.</p>
<p><strong>3. Et c’est là que commence la question philosophique</strong></p>
<p>À mon sens, la révolution la plus importante n’est pas : « les ordinateurs deviennent plus rapides ».</p>
<p>Elle est plutôt : <strong>la capacité cognitive artificielle se déplace progressivement du centre vers la périphérie.</strong></p>
<p>Pendant longtemps, utiliser une IA puissante impliquait :</p>
<p><img height="35" src="/media/2026/09/word-image-5826-6.png" width="420"/></p>
<p>Mais une machine équipée d’un GPU de cette catégorie permet maintenant :</p>
<p><img height="39" src="/media/2026/09/word-image-5826-7.png" width="182"/></p>
<p>directement. Et cela change énormément de choses.</p>
<p><strong>4. L’IA devient une propriété de l’individu</strong></p>
<p>Imaginons un ordinateur personnel contenant une IA locale.</p>
<p>Elle peut disposer de :</p>
<ul>
<li>
    vos documents,</li>
<li>
    vos livres,</li>
<li>
    vos programmes,</li>
<li>
    vos photographies,</li>
<li>
    vos recherches,</li>
<li>
    vos notes,</li>
<li>
    vos bases de données,</li>
<li>
    votre correspondance.</li>
</ul>
<p>Tout cela peut potentiellement rester <strong>sur votre ordinateur</strong>.</p>
<p>On obtient alors quelque chose qui ressemble à :</p>
<p><img height="48" src="/media/2026/09/word-image-5826-8.png" width="444"/></p>
<p>Le PC avait démocratisé le <strong>calcul</strong>.</p>
<p>Internet avait démocratisé <strong>l’accès à l’information</strong>.</p>
<p>Le GPU pourrait contribuer à démocratiser <strong>le traitement intelligent de cette information</strong>.</p>
<p><strong>5. Cela rappelle étrangement l’histoire du PC</strong></p>
<p>Dans les années 1960 :</p>
<p><img height="33" src="/media/2026/09/word-image-5826-9.png" width="456"/></p>
<p>Puis sont arrivés les microprocesseurs.</p>
<p>Dans les années 1980 :</p>
<p><img height="31" src="/media/2026/09/word-image-5826-10.png" width="386"/></p>
<p>Nous observons peut-être aujourd’hui quelque chose d’analogue.</p>
<p>Première phase :</p>
<p><img height="41" src="/media/2026/09/word-image-5826-11.png" width="238"/></p>
<p>Deuxième phase :</p>
<p><img height="38" src="/media/2026/09/word-image-5826-12.png" width="231"/></p>
<p>Troisième phase possible :</p>
<p><img height="29" src="/media/2026/09/word-image-5826-13.png" width="249"/></p>
<p>puis :</p>
<p><img height="31" src="/media/2026/09/word-image-5826-14.png" width="220"/></p>
<p>La RTX 3090 n’est évidemment pas à elle seule responsable de cette évolution. Mais elle en constitue un <strong>symbole particulièrement intéressant</strong>.</p>
<p><strong>6. Et il y a une conséquence encore plus profonde</strong></p>
<p>Jusqu’à présent, l’ordinateur était principalement un outil.</p>
<p>Vous lui disiez : calcule ceci.</p>
<p>Il calculait.</p>
<p>Puis : affiche ceci.</p>
<p>Il affichait.</p>
<p>Puis : cherche ceci.</p>
<p>Il cherchait.</p>
<p>Avec l’IA générative, nous commençons à lui dire : réfléchis à ce problème.</p>
<p>Et la nature de la relation change.</p>
<p>Nous passons progressivement de :</p>
<p><img height="38" src="/media/2026/09/word-image-5826-15.png" width="100"/></p>
<p>à</p>
<p><img height="39" src="/media/2026/09/word-image-5826-16.png" width="209"/></p>
<p>voire, dans certains usages :</p>
<p><img height="36" src="/media/2026/09/word-image-5826-17.png" width="188"/></p>
<p>Le terme doit être utilisé avec prudence — le modèle ne possède pas nécessairement une compréhension ou une conscience comparable aux nôtres — mais <strong>fonctionnellement</strong>, pour l’utilisateur, la transformation est réelle.</p>
<p><strong>7. Cela pose immédiatement la question de l’intelligence</strong></p>
<p>Pendant des siècles, nous avons implicitement associé :</p>
<p><img height="25" src="/media/2026/09/word-image-5826-18.png" width="293"/></p>
<p>Les ordinateurs nous obligent progressivement à séparer :</p>
<p><img height="24" src="/media/2026/09/word-image-5826-19.png" width="124"/></p>
<p>de</p>
<p><img height="27" src="/media/2026/09/word-image-5826-20.png" width="198"/></p>
<p>Et c’est philosophiquement beaucoup plus important que les performances d’une carte graphique.</p>
<p>Car si certaines activités que nous considérions comme intellectuelles peuvent être obtenues par :</p>
<p><img height="24" src="/media/2026/09/word-image-5826-21.png" width="363"/></p>
<p>une question vertigineuse apparaît :</p>
<p><strong>Quelle partie de ce que nous appelons intelligence provient réellement de propriétés exclusivement humaines ?</strong></p>
<p><strong>8. Et cela conduit à une autre question</strong></p>
<p>Supposons une machine équipée d’une IA locale connaissant :</p>
<ul>
<li>
    tous vos travaux,</li>
<li>
    vos raisonnements précédents,</li>
<li>
    vos préférences intellectuelles,</li>
<li>
    vos méthodes de calcul,</li>
<li>
    vos erreurs habituelles,</li>
<li>
    vos projets.</li>
</ul>
<p>Vous lui posez un problème.</p>
<p>Elle ne répond plus comme une IA générique.</p>
<p>Elle raisonne en exploitant <strong>votre propre corpus intellectuel</strong>.</p>
<p>Nous obtenons alors quelque chose d’intéressant :</p>
<p><img height="26" src="/media/2026/09/word-image-5826-22.png" width="377"/></p>
<p>La frontière pertinente n’est donc peut-être plus :</p>
<p><img height="24" src="/media/2026/09/word-image-5826-23.png" width="219"/></p>
<p>mais :</p>
<p><img height="45" src="/media/2026/09/word-image-5826-24.png" width="523"/></p>
<p><strong>9. Il existe cependant un paradoxe</strong></p>
<p>L’IA nécessite actuellement des infrastructures gigantesques pour <strong>créer les grands modèles</strong>.</p>
<p>Entraîner un modèle de pointe demeure une activité industrielle.</p>
<p>Nous avons donc simultanément deux mouvements :</p>
<p><img height="28" src="/media/2026/09/word-image-5826-25.png" width="284"/></p>
<p>mais :</p>
<p><img height="31" src="/media/2026/09/word-image-5826-26.png" width="351"/></p>
<p>Une RTX 3090 ne permettra évidemment pas d’entraîner chez soi un modèle géant comparable aux modèles de frontière. En revanche, elle permet d’utiliser, adapter ou parfois affiner des modèles déjà entraînés. C’est un peu comparable à l’imprimerie : peu de personnes fabriquent une presse, mais énormément de personnes peuvent ensuite produire et diffuser des textes.</p>
<p><strong>10. La carte TRX 3090 représente une étape historique assez amusante</strong></p>
<p>On pourrait résumer l’histoire ainsi :</p>
<p><img height="33" src="/media/2026/09/word-image-5826-27.png" width="123"/></p>
<p>conçu pour calculer :</p>
<p><img height="37" src="/media/2026/09/word-image-5826-28.png" width="178"/></p>
<p>puis utilisé pour :</p>
<p><img height="29" src="/media/2026/09/word-image-5826-29.png" width="175"/></p>
<p>puis :</p>
<p><img height="29" src="/media/2026/09/word-image-5826-30.png" width="174"/></p>
<p>puis :</p>
<p><img height="45" src="/media/2026/09/word-image-5826-31.png" width="205"/></p>
<p>et finalement :</p>
<p><img height="44" src="/media/2026/09/word-image-5826-32.png" width="388"/></p>
<p>C’est une magnifique illustration d’un phénomène fréquent dans l’histoire des techniques :</p>
<p><strong>Une invention devient véritablement révolutionnaire lorsqu’elle commence à servir à quelque chose pour laquelle elle n’avait pas été initialement conçue.</strong></p>
<p><strong>Et je pousserais volontiers cette discussion encore un cran plus loin</strong></p>
<p>Il existe à mon avis une question encore plus fascinante que celle de la RTX 3090 :</p>
<p><img height="47" src="/media/2026/09/word-image-5826-33.png" width="475"/></p>
<p>Car on peut tracer une chaîne technologique extraordinaire :</p>
<p><img height="35" src="/media/2026/09/word-image-5826-34.png" width="808"/></p>
<p>Et derrière cette chaîne se cache une question philosophique encore plus troublante : <strong>comment quelques opérations mathématiques extrêmement simples — essentiellement multiplications, additions et fonctions non linéaires — répétées des milliards de fois finissent-elles par produire un système capable de discuter avec nous de physique, de philosophie ou de concevoir un programme ?</strong></p>
<p><strong><em>Celle-là mérite à elle seule une véritable investigation…</em></strong></p>
<p><strong>Lexique</strong></p>
<p><strong>CUDA</strong> signifie <strong>Compute Unified Device Architecture</strong>. C’est une technologie et une plateforme logicielle créée par NVIDIA qui permet d’utiliser le <strong>GPU comme un processeur de calcul général</strong>, et pas seulement pour fabriquer des images.La RTX 3090 possède <strong>10 496 cœurs CUDA</strong>, contrairement aux quelques cœurs très puissants d’un CPU, ces milliers d’unités peuvent effectuer énormément d’opérations <strong>en parallèle</strong>.</p>
<p><strong>GPU</strong> signifie <strong>Graphics Processing Unit</strong>, que l’on peut traduire par <strong>processeur graphique</strong>.</p>
<p>À l’origine, son rôle était de calculer très rapidement les images 2D et 3D des jeux vidéo : positions des objets, textures, éclairage, pixels, etc. Pour cela, il devait effectuer <strong>un très grand nombre de calculs similaires simultanément</strong>.C’est précisément cette caractéristique qui l’a rendu extrêmement intéressant pour l’IA.</p>
<p>Les <strong>Tensor Core</strong> sont des unités de calcul spécialisées intégrées aux GPU NVIDIA récents. Contrairement aux cœurs CUDA, plus généralistes, ils ont été conçus notamment pour effectuer <strong>extrêmement rapidement des calculs sur des matrices</strong>, ce qui les rend particulièrement adaptés à l’intelligence artificielle.</p>
<p>Une <strong>IA générative</strong> est une intelligence artificielle capable de <strong>produire un nouveau contenu</strong>, et pas seulement d’analyser ou de classer des données.</p>
<p>La différence essentielle est la suivante :</p>
<p><img height="80" src="/media/2026/09/word-image-5826-35.png" width="416"/></p>
<p>Elle peut générer du <strong>texte</strong>, des <strong>images</strong>, de la musique, de la vidéo, du code informatique, etc. ChatGPT est, par exemple, une IA générative spécialisée notamment dans le langage.</p>
<p>J-P Broillet 09.2026</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
