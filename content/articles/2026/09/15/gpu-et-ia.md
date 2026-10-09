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
**La carte RTX 3090 (28 milliards de transistors) son impact sur l’IA et la question philosophiques sous-jacente**

Le sujet est plus profond qu’il n’y paraît, car la [RTX 3090](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/?utm_source=chatgpt.com) est un bon exemple d’un phénomène historique : **un composant conçu principalement pour le graphisme est devenu une petite machine de calcul neuronal accessible aux particuliers**.

![Image](/media/2026/09/image.jpeg)

**1. Pourquoi un GPU est-il si adapté à l’IA ?**

Un processeur classique possède relativement peu de cœurs très sophistiqués.

Un GPU adopte presque la philosophie inverse : énormément d’unités de calcul relativement simples travaillant simultanément.

Or un réseau neuronal passe une énorme partie de son temps à effectuer des opérations du genre :

![](/media/2026/09/word-image-5826-2.png)

c’est-à-dire des **multiplications matricielles**. Prenons une couche d’un réseau :

![](/media/2026/09/word-image-5826-3.png)

avec :

![](/media/2026/09/word-image-5826-4.png)

Pour quelques neurones, rien d’impressionnant, de difficile. Mais avec des milliards de paramètres, il faut effectuer **des milliards d’opérations similaires**.

Et c’est précisément ce que les GPU savent faire extrêmement efficacement.

**2. Les Tensor Cores changent encore la situation**

Avec les RTX, NVIDIA a ajouté des circuits spécialisés : les **Tensor Cores**.

Ils sont particulièrement adaptés aux opérations matricielles utilisées par l’apprentissage profond.

Schématiquement :

![](/media/2026/09/word-image-5826-5.png)

peut être réalisée massivement en parallèle. Ainsi la RTX 3090 n’est plus simplement : « une carte graphique très rapide ». Elle devient pratiquement : **un accélérateur de calcul matriciel vendu au grand public.**

C’est une différence conceptuelle considérable.

**3. Et c’est là que commence la question philosophique**

À mon sens, la révolution la plus importante n’est pas : « les ordinateurs deviennent plus rapides ».

Elle est plutôt : **la capacité cognitive artificielle se déplace progressivement du centre vers la périphérie.**

Pendant longtemps, utiliser une IA puissante impliquait :

![](/media/2026/09/word-image-5826-6.png)

Mais une machine équipée d’un GPU de cette catégorie permet maintenant :

![](/media/2026/09/word-image-5826-7.png)

directement. Et cela change énormément de choses.

**4. L’IA devient une propriété de l’individu**

Imaginons un ordinateur personnel contenant une IA locale.

Elle peut disposer de :

- vos documents,
- vos livres,
- vos programmes,
- vos photographies,
- vos recherches,
- vos notes,
- vos bases de données,
- votre correspondance.

Tout cela peut potentiellement rester **sur votre ordinateur**.

On obtient alors quelque chose qui ressemble à :

![](/media/2026/09/word-image-5826-8.png)

Le PC avait démocratisé le **calcul**.

Internet avait démocratisé **l’accès à l’information**.

Le GPU pourrait contribuer à démocratiser **le traitement intelligent de cette information**.

**5. Cela rappelle étrangement l’histoire du PC**

Dans les années 1960 :

![](/media/2026/09/word-image-5826-9.png)

Puis sont arrivés les microprocesseurs.

Dans les années 1980 :

![](/media/2026/09/word-image-5826-10.png)

Nous observons peut-être aujourd’hui quelque chose d’analogue.

Première phase :

![](/media/2026/09/word-image-5826-11.png)

Deuxième phase :

![](/media/2026/09/word-image-5826-12.png)

Troisième phase possible :

![](/media/2026/09/word-image-5826-13.png)

puis :

![](/media/2026/09/word-image-5826-14.png)

La RTX 3090 n’est évidemment pas à elle seule responsable de cette évolution. Mais elle en constitue un **symbole particulièrement intéressant**.

**6. Et il y a une conséquence encore plus profonde**

Jusqu’à présent, l’ordinateur était principalement un outil.

Vous lui disiez : calcule ceci.

Il calculait.

Puis : affiche ceci.

Il affichait.

Puis : cherche ceci.

Il cherchait.

Avec l’IA générative, nous commençons à lui dire : réfléchis à ce problème.

Et la nature de la relation change.

Nous passons progressivement de :

![](/media/2026/09/word-image-5826-15.png)

à

![](/media/2026/09/word-image-5826-16.png)

voire, dans certains usages :

![](/media/2026/09/word-image-5826-17.png)

Le terme doit être utilisé avec prudence — le modèle ne possède pas nécessairement une compréhension ou une conscience comparable aux nôtres — mais **fonctionnellement**, pour l’utilisateur, la transformation est réelle.

**7. Cela pose immédiatement la question de l’intelligence**

Pendant des siècles, nous avons implicitement associé :

![](/media/2026/09/word-image-5826-18.png)

Les ordinateurs nous obligent progressivement à séparer :

![](/media/2026/09/word-image-5826-19.png)

de

![](/media/2026/09/word-image-5826-20.png)

Et c’est philosophiquement beaucoup plus important que les performances d’une carte graphique.

Car si certaines activités que nous considérions comme intellectuelles peuvent être obtenues par :

![](/media/2026/09/word-image-5826-21.png)

une question vertigineuse apparaît :

**Quelle partie de ce que nous appelons intelligence provient réellement de propriétés exclusivement humaines ?**

**8. Et cela conduit à une autre question**

Supposons une machine équipée d’une IA locale connaissant :

- tous vos travaux,
- vos raisonnements précédents,
- vos préférences intellectuelles,
- vos méthodes de calcul,
- vos erreurs habituelles,
- vos projets.

Vous lui posez un problème.

Elle ne répond plus comme une IA générique.

Elle raisonne en exploitant **votre propre corpus intellectuel**.

Nous obtenons alors quelque chose d’intéressant :

![](/media/2026/09/word-image-5826-22.png)

La frontière pertinente n’est donc peut-être plus :

![](/media/2026/09/word-image-5826-23.png)

mais :

![](/media/2026/09/word-image-5826-24.png)

**9. Il existe cependant un paradoxe**

L’IA nécessite actuellement des infrastructures gigantesques pour **créer les grands modèles**.

Entraîner un modèle de pointe demeure une activité industrielle.

Nous avons donc simultanément deux mouvements :

![](/media/2026/09/word-image-5826-25.png)

mais :

![](/media/2026/09/word-image-5826-26.png)

Une RTX 3090 ne permettra évidemment pas d’entraîner chez soi un modèle géant comparable aux modèles de frontière. En revanche, elle permet d’utiliser, adapter ou parfois affiner des modèles déjà entraînés. C’est un peu comparable à l’imprimerie : peu de personnes fabriquent une presse, mais énormément de personnes peuvent ensuite produire et diffuser des textes.

**10. La carte TRX 3090 représente une étape historique assez amusante**

On pourrait résumer l’histoire ainsi :

![](/media/2026/09/word-image-5826-27.png)

conçu pour calculer :

![](/media/2026/09/word-image-5826-28.png)

puis utilisé pour :

![](/media/2026/09/word-image-5826-29.png)

puis :

![](/media/2026/09/word-image-5826-30.png)

puis :

![](/media/2026/09/word-image-5826-31.png)

et finalement :

![](/media/2026/09/word-image-5826-32.png)

C’est une magnifique illustration d’un phénomène fréquent dans l’histoire des techniques :

**Une invention devient véritablement révolutionnaire lorsqu’elle commence à servir à quelque chose pour laquelle elle n’avait pas été initialement conçue.**

**Et je pousserais volontiers cette discussion encore un cran plus loin**

Il existe à mon avis une question encore plus fascinante que celle de la RTX 3090 :

![](/media/2026/09/word-image-5826-33.png)

Car on peut tracer une chaîne technologique extraordinaire :

![](/media/2026/09/word-image-5826-34.png)

Et derrière cette chaîne se cache une question philosophique encore plus troublante : **comment quelques opérations mathématiques extrêmement simples — essentiellement multiplications, additions et fonctions non linéaires — répétées des milliards de fois finissent-elles par produire un système capable de discuter avec nous de physique, de philosophie ou de concevoir un programme ?**

***Celle-là mérite à elle seule une véritable investigation…***

**Lexique**

**CUDA** signifie **Compute Unified Device Architecture**. C’est une technologie et une plateforme logicielle créée par NVIDIA qui permet d’utiliser le **GPU comme un processeur de calcul général**, et pas seulement pour fabriquer des images.La RTX 3090 possède **10 496 cœurs CUDA**, contrairement aux quelques cœurs très puissants d’un CPU, ces milliers d’unités peuvent effectuer énormément d’opérations **en parallèle**.

**GPU** signifie **Graphics Processing Unit**, que l’on peut traduire par **processeur graphique**.

À l’origine, son rôle était de calculer très rapidement les images 2D et 3D des jeux vidéo : positions des objets, textures, éclairage, pixels, etc. Pour cela, il devait effectuer **un très grand nombre de calculs similaires simultanément**.C’est précisément cette caractéristique qui l’a rendu extrêmement intéressant pour l’IA.

Les **Tensor Core** sont des unités de calcul spécialisées intégrées aux GPU NVIDIA récents. Contrairement aux cœurs CUDA, plus généralistes, ils ont été conçus notamment pour effectuer **extrêmement rapidement des calculs sur des matrices**, ce qui les rend particulièrement adaptés à l’intelligence artificielle.

Une **IA générative** est une intelligence artificielle capable de **produire un nouveau contenu**, et pas seulement d’analyser ou de classer des données.

La différence essentielle est la suivante :

![](/media/2026/09/word-image-5826-35.png)

Elle peut générer du **texte**, des **images**, de la musique, de la vidéo, du code informatique, etc. ChatGPT est, par exemple, une IA générative spécialisée notamment dans le langage.

J-P Broillet 09.2026

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
