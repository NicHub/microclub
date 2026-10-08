---
title: "Windows 7 + ancien OS dans VMware"
date: "2009-05-09T06:24:27"
lastmod: "2015-04-24T23:20:20"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["vista", "vmware", "windows-7"]
url: "/2009/05/09/windows-7-ancien-os-dans-vmware/"
wordpress_id: 189
comment_count: 7
---
<p>Puisqu’on peut<a href="http://technet.microsoft.com/fr-fr/evalcenter/dd353205.aspx" target="_blank"> télécharger une version de Windows 7</a> qui marchera jusqu’en juin 2010 gratuitement, autant en profiter pour faire un grand nettoyage de printemps. J’avais deux options :</p>
<ol>
<li>mettre à jour mon Vista qui avait été mis à jour d’un XP qui avait peut-être bien été mis à jour depuis Windows 2000 il y a longtemps</li>
<li>faire une nouvelle installation, mais dans ce cas autant en profiter pour passer au 64 bits (x64 pour les intimes), maintenant que presque tous les logiciels tournent en 64 bits aussi ou en mode compatibilité sans problème.</li>
</ol>
<p>J’étais très tenté par la deuxième solution, mais elle impliquait de « perdre » de nombreux programmes tout bien configurés, ou du moins de les laisser sur la partition Vista, m’obligeant à rebooter pour y accéder …</p>
<p>Et je suis tombé sur <a href="http://www.vmware.com/fr/products/converter/" target="_blank">VMware Converter</a> : Eureka ! Ce soft aussi génial que gratuit tourne sur tous les Windows* depuis NT4 SP4+ et fabrique une « machine virtuelle » à partir d’une machine physique !</p>
<p>J’ai ainsi pu sauvegarder mon système Vista complet sous forme d’un très gros fichier sur un disque USB, puis installé Seven x64  sur une autre partition que Vista par prudence ( mais ça ne s’est pas révélé utile, j’aurais tout aussi bien pu écraser la partition Vista tout de suite)</p>
<p>Ensuite il ne reste plus qu’à installer VMWare sur Seven, le lancer, charger la machine virtuelle Vista et tadaaammm! :</p>
<figure aria-describedby="caption-attachment-190"><img alt="" height="350" src="/media/2009/05/sevenvista.png" title="Seven+Vista" width="560"/><figcaption>Seven et Vista (cliquez pour agrandir)</figcaption></figure>
<p>Je me retrouve avec mon nouveau système tout <span>neuf </span>sept, tout propre et dedans dans une fenêtre mon vieux système pourri mais bien utile d’ici à ce que j’aie tout migré.</p>
<h3>Premières impressions de Seven:</h3>
<p>En fait c’est les deuxièmes parce que j’avais déjà installé la Beta dans un VMware sous Vista, pour voir. Donc:</p>
<ol>
<li>Seven = ce que Vista aurait du être : plus petit, plus simple. Plus rapide ? c’est toujours plus rapide quand c’est <span>neuf </span>sept. Faudra voir à l’usage.</li>
<li>ils ont encore changé la « barre des tâches » et ça bouleverse (encore) nos habitudes, mais le nouveau système n’est pas mauvais.</li>
</ol>
<p><strong>Note* </strong>: convertir une machine Windows 98 est apparemment aussi possible, mais en utilisant une<a href="http://communities.vmware.com/message/596144#596144" target="_blank"> combine avec Norton Ghost </a></p>

## Commentaires

### Yves Masur — 9 mai 2009 à 07:45

<section class="comment-content comment">
<p>Ah! Bien joué… tu dis Vista= un gros fichier… ce qui m’amène à quelques questions.<br/>
VMWare est payant pour convertir une machine réelle en virtuelle: comment as-tu fait?<br/>
Sur mon PC actuel (bon je peux certainement faire de l’odre…) la partition Vista pèse 51.5 Go, y. c. les outils 32 bits installés. Il faut une super grosse clef USB, non?<br/>
Pour ce qui est réseau, comment as-tu configuré le bazar?</p>
 </section>

### Dr. Goulu — 9 mai 2009 à 11:55

<section class="comment-content comment">
<p>Non non, la version « Starter » (qui ne fonctionne pas à travers le réseau) est gratos ! Suis le lien de l’article vers le « VMware converter » tu verras … Ensuite tu peux utiliser le Player pour exécuter la machine virtuelle , gratuit aussi ( <a href="http://www.vmware.com/products/player/" rel="nofollow ugc">http://www.vmware.com/products/player/</a> )</p>
<p>J’ai pas dit « clé USB » mais bien « disque USB ». Mon fichier vmware fait effectivement dans les 50 Go après avoir déplacé tous les fichiers persos sur ma partition Seven.</p>
<p>J’ai miraculeusement RIEN eu à configurer, et ça m’a scié : ma machine a une carte graphique de la mort avec les drivers optimisés qui vont avec, et elle a booté en VMWare en plus basse résolution mais sans le moindre problème. Idem pour le réseau : le réseau s’est mis tout seul en mode « bridged » et ça a marché direct.</p>
<p>Le terme « miraculeusement » n’est  pas exagéré : à mon avis quand un truc marche comme ça bien en informatique, c’est grâce à l’intervention directe de Saint Alan (Turing). L’état normal, c’est que ça marche pas. Les softs de VMware devraient être plus vénérés que l’eau de Lourdes, parce qu’eux ils font des miracles quasi à tous les coups !</p>
 </section>

### Michael — 27 mai 2009 à 20:41

<section class="comment-content comment">
<p>Bonjour, et merci pour l’info.<br/>
Petite question, quelle version de Vmware avez vous installé, car je n’arrive pas à le faire fonctionner sur Seven.</p>
<p>Merci</p>
 </section>

### ↳ Réponse — Dr. Goulu — 28 mai 2009 à 15:45

<section class="comment-content comment">
<p>VmWare 6.5.0, sans problème aprticulier si je me souviens bien. Qu’est-ce qui ne va pas ?</p>
 </section>

### Michael — 28 mai 2009 à 19:24

<section class="comment-content comment">
<p>Problème résolu :).<br/>
J’ai essayé avec le vmware server 1.0.9 ou les 2.0;0X mais ils ne semblent pas fonctionner correctement avec Seven.<br/>
Je viens de passer au Workstation, ça passe comme une lettre à la poste.</p>
 </section>

### nicolas — 26 août 2010 à 07:18

<section class="comment-content comment">
<p>Est-ce vmware s’installe avec toutes les versions de 7. j’aurai besoin d’installer un xp en vmware sous 7 premnium !</p>
<p>merci.</p>
 </section>

### ↳ Réponse — Dr. Goulu — 26 août 2010 à 08:37

<section class="comment-content comment">
<p>A ma connaissance oui, aucun problème. Comme indiqué, on peut faire tourner un XP 32 bits dans un Vmware sous Windows 7 64 bits, et plus étonnant et inutile mais j’ai testé et ça marche aussi, un Win 7 64 bits dans un Vmware sous XP 32 bits !</p>
<p>Cela dit, je vais essayer d’utiliser <a href="http://www.virtualbox.org/" rel="nofollow ugc">http://www.virtualbox.org/</a> au lieu de VmWare (ou en plus…) un de ces jours. VirtualBox est semble-t-il beaucoup plus performant pour les applications graphiques, car il implante OpenGL en utilisant directement le GPU d’une bonne carte graphique récente au lieu de faire de l’émulation software.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
