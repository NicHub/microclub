---
title: "Mémoire Windows: Hit parade"
date: "2011-04-03T20:21:32"
lastmod: "2015-04-24T23:21:12"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["non-classe"]
url: "/2011/04/03/memoire-windows-hit-parade/"
wordpress_id: 469
comment_count: 2
---
<p>Quelle est l’application la plus gourmande? la plus économe? Une application de sysinternals, gratuite, permet d’y voir clair (<a href="http://technet.microsoft.com/fr-fr/sysinternals/" target="_blank" title="http://technet.microsoft.com/fr-fr/sysinternals/">http://technet.microsoft.com/fr-fr/sysinternals/</a> ).</p>
<figure aria-describedby="caption-attachment-470"><a href="/media/2011/04/mem_used.png"><img alt="mem_used" height="609" src="/media/2011/04/mem_used.png" title="mem_used" width="838"/></a><figcaption>Mémoire utilisée, avec pointe</figcaption></figure>
<p>Si le CPU n’est pas surbooké par la tonne d’application, on peut voir qui a besoin de combien de RAM. Clairement la fondation Mozilla ne fait pas dans le léger: 104 Mo pour Thunderbird!</p>
<p>Les navigateurs, ici sur la page d’accueil (fort légère) de google, montrent:</p>
<ul>
<li>Firefox 74.7 Mo</li>
<li>Chrome 38.1 Mo</li>
<li>Internet Explorer 36.4 Mo</li>
</ul>
<p>Se dernier ‘appuie fortement sur Explorer, qui consomme 41.5 Mo, alors que Chrome ajoute 22.2 Mo dans une instance séparée (probablement le moteur, qui surveille si une fenêtre crash).</p>
<p>Le lecteur de bulletins de versement, MyPen, est aussi surprenant. Prévu pour XP, il prend 35.7 Mo. Est-ce la virtualisation sous Windows 7? Cependant, on peut l’arrêter, il ne s’utilise qu’une fois par mois! Mon lecteur de musique favori, Winamp reste modeste: 10.4 Mo!!</p>
<p>Dans la partie invisible de cette photographie, pas mal d’utilitaires et pilotes qui, vous l’aurez compris, consomment moins de 10 Mo, souvent de 3 à 5 Mo. Le seul plus gourmand est DropBox, permettant l’échange/partage de fichiers via Internet, à 20.3 Mo, fortement dépendant des échanges.</p>
<p>Pour les applications, il peut y a aussi un recours +/- intense à svchost.exe, qui est un service Windows appelé par DLL. Mais ceci est une autre histoire qui dépasse ce coup d’oeil…</p>
<p>Yves Masur</p>

## Commentaires

### Robin — 4 avril 2011 à 10:23

<section class="comment-content comment">
<p>Question de béotien : qu’est-ce que ces infos apportent de plus par rapport à celles d’un simple gestionnaire des tâches de Windows?</p>
<p>Pour Firefox, je suppose que ça dépend aussi si des modules complémentaires sont activés (moi, je dois bien en avoir une dizaine/quinzaine). Dropbox est assez gourmand, c’est clair, mais on peut aussi l’arrêter (bon ce n’est pas prévu pour, non plus).</p>
 </section>

### ↳ Réponse — Yves Masur — 4 avril 2011 à 21:06

<section class="comment-content comment">
<p>Cet outil est bien plus complet que le gestionnaire de Windows. Il permet de voir la mémoire utilisée, mais aussi le pic min et max, la mémoire partagée, l’historique des I/O en lecture/écriture, les « page fault », les objets GDI. Au niveau CPU: le « context switch », les cycles, le temps utilisé, etc. Bref, une foultitude de paramètres.</p>
<p>Bien entendu, autant pour Firefox que pour les autres navigateurs, la mémoire dépend des modules chargés.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
