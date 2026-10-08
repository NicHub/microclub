---
title: "FLASH: données en sécurité?"
date: "2012-03-10T17:32:32"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["consoles", "donnees", "hardware", "systeme-dexploitation"]
url: "/2012/03/10/flash-donnees-en-securite/"
wordpress_id: 743
comment_count: 3
---
<h1>FLASH – un moyen de backup?</h1>
<p>Une amie, peu férue en informatique, à qui je demandais où ses précieuses photos d’un voyage au USA étaient sauvegardées me répondit que pour elle, la clef USB était un moyen pratique et rapide de sauver tout ça. Devant ma moue dubitative, elle me demanda si ce n’était pas plus sûr que le disque dur? Certes répondis-je, le stockage sous forme de FLASH et bien plus sûr que le système mécanique d’un disque dur, mais il y a toujours une usure quand on écrit. Le nombre de lecture n’est pas limité, les écritures oui. De plus c’est cher au mégabit. Et, on va le voir ci-dessous, il peut y avoir des déconvenues subtiles…</p>
<h1>Copie de données</h1>
<p>Pour ma part, j’utilise volontiers une carte FLASH pour copier directement les photos de l’appareil sur le PC: c’est rapide et préserve les fichiers avec la date originale de la prise  de vue. Et je fait un usage abondant de clefs USB. C’est bien plus rapide que via le réseau quand la transmission se fait par Wi-Fi. Souvent, lors de présentations, il est devenu courant de distribuer les ppt, pdf et programmes par une clef USB publicitaire, plutôt qu’un CD. Une fois les données intéressantes sauvée sur le réseau de l’entreprise, rien n’empêche de l’utiliser pour autre chose.</p>
<p>Cependant, lors d’une utilisation d’une telle clef pour copier des photos, l’une d’entre-elle avait des couleurs étranges, et il en manquait le bas. Après moult essais (recopie-&gt; idem! copie sous un autre nom, OK) la méfiance m’a fait reformater la clef. En <a href="http://fr.wikipedia.org/wiki/New_Technology_File_System" target="_blank" title="NTFS">NTFS</a>, système plus solide que <a href="http://fr.wikipedia.org/wiki/FAT32" target="_blank" title="FAT32">FAT32</a>.</p>
<p><a href="/media/2012/03/format.png"><img alt="format" height="586" src="/media/2012/03/format.png" title="format" width="630"/></a></p>
<p>Quelques semaines plus tard… je l’utilise pour copier un programme d’installation et des fichiers sources. A l’installation, cri d’alerte du programme: il est corrompu! Selon l’Explorer, rien à signaler: même taille, même date. Je lance la console CMD.EXE, puis l’utilitaire FC (file compare).</p>
<p><code>c:\Users\Yves\Documents\Pic\dloaded&gt;fc netloader_jre150_v107.exe h:netloader_jre150_v107.exe<br/>
Comparaison des fichiers netloader_jre150_v107.exe et H:NETLOADER_JRE150_V107.EXE<br/>
003AAC26: 6B 2B<br/>
003AAC34: 50 10<br/>
003AAC40: D1 D0<br/>
...</code></p>
<p>On le voit, c’est pourri. Je lance une copie avec vérification, pour voir, suivi d’une comparaison:<br/>
<code><br/>
c:\Users\Yves\Documents\Pic\dloaded&gt;copy netloader_jre150_v107.exe h: /V<br/>
Remplacer h:netloader_jre150_v107.exe (Oui/Non/Tous) : o<br/>
1 fichier(s) copié(s).</code></p>
<p><code>c:\Users\Yves\Documents\Pic\dloaded&gt;fc netloader_jre150_v107.exe h:netloader_jre150_v107.exe<br/>
Comparaison des fichiers netloader_jre150_v107.exe et H:NETLOADER_JRE150_V107.EXE<br/>
FC : aucune différence trouvée</code></p>
<h1>Tester une FLASH</h1>
<p>La méfiance est maintenant totale. Il suffit que l’allocation soit déplacée à la copie, et c’est bon… Une recherche sur internet et je tombe sur ce programme: http://www.vconsole.com/client/?page=page&amp;id=13. L’installation est rapide; au lancement j’ai dû créer le fichier de log pour qu’il accepte de l’alimenter (indiquer le path/nom ne suffit pas). Et là, sans surprise, on trouve des erreurs.</p>
<p><a href="/media/2012/03/Tests_results.png"><img alt="Tests_results" height="635" src="/media/2012/03/Tests_results.png" title="Tests_results" width="757"/></a></p>
<p>Si je laisse le programme tourner 1/4 heure, le nombre d’erreurs s’accroît encore. Remarquons au passage que ce n’est ni des erreurs de lecture, ni d’écriture, mais de comparaison. C’est d’autant plus vicieux que le système ne détecte pas de problème lors de la copie de fichier!</p>
<p>Décidément, ce petit programme va faire partie de ma trousse à outil. Mieux vaut prévenir que guérir, je passe mes clef USB à la moulinette. On a au passage la vitesse d’écriture, ce qui donne une idée des performances du stockage.</p>

## Commentaires

### Claude — 12 mars 2012 à 15:44

<section class="comment-content comment">
<p>Bonjour<br/>
J’ai eu un problème similaire. Je devais faire une présentation (fichier PPT) chez un client et j’ai mis celle-ci sur une clé USB. Arrivé chez lui, je sort la clé et veux charger ces fichiers. Ca a marché, mais tous étaient pollués… La honte… J’ai été sur le site <a href="http://www.libellules.ch/" rel="nofollow ugc">http://www.libellules.ch</a> et j’ai trouvé un programme de test, ce qui m’a montré qu’il y a de grosse différence entre les clés (marque?)<br/>
Depuis lors, je suis très méfiant<br/>
PS: sur ce site, on trouve la description du programme Flash Drive Tester</p>
 </section>

### Squally — 20 avril 2012 à 19:43

<section class="comment-content comment">
<p>Dernièrement, des collègues ont reçu des clé USB promotionnel avec une coque en bois, ainsi que le bouchon. Les deux parties contiennent des aimants pour les maintenir ensemble, lorsque l’on n’utilise pas la clé.</p>
<p>Est-ce que cela peut avoir une influence néfaste sur la conservation des données à moyen ou long terme? A court terme, ça fonctionne à la grande satisfaction des propriétaires.</p>
<p>J’ai distribué et/ou utilisé une bonne septantaine de clé USB de marque différente et je n’ai jamais rencontré de problème et jusqu’à aujourd’hui personne est revenu se plaindre.<br/>
J’ai même eu la chance de réussir à faire fonctionner ma clé après un passage en machine à laver le linge suivi du sèche linge !</p>
<p>Bravo pour l’article Yves et je serai plus attentif dans le futur.</p>
 </section>

### ymasur — 20 avril 2012 à 20:26

<section class="comment-content comment">
<p><a href="#comment-451" rel="nofollow">@Squally </a><br/>
Pas de souci avec le magnétisme. C’est vraiment la puce « flash » qui peut causer problème. Peut-être aussi – course à la vitesse oblige – les timings d’écriture ne sont pas respectés pour afficher (sur le papier) des performances qui ne sont pas assurées.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
