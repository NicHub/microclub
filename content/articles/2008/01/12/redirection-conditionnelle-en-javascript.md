---
title: "redirection conditionnelle en JavaScript"
date: "2008-01-12T17:03:58"
lastmod: "2015-04-24T23:20:22"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation", "web"]
url: "/2008/01/12/redirection-conditionnelle-en-javascript/"
wordpress_id: 31
comment_count: 1
---
<p>Je remonte un peu le temps pour vous expliquer le problème:</p>
<ol>
<li>En même temps que mon domaine <a href="http://goulu.net" target="_blank">goulu.net</a>, j’avais acheté un hébergement web pas cher auprès d’une boite lointaine, ce qui m’avait permis de créer de nombreuses versions de mon site internet.</li>
<li>Lorsque j’ai créé mon blog <a href="/2008/01/12/redirection-conditionnelle-en-javascript/http;/drgoulu.wordpress.com" target="_blank">drgoulu.wordpress.com</a>, hébergé gratuitement sur le génial wordpress.com , j’ai créé sur mon ancien hébergement une redirection HTTP toute simple en créant un fichier index.php contenant simplement ces lignes:<br/>
<code>&lt;?<br/>
Header( "HTTP/1.1 301 Moved Permanently" );<br/>
Header( "Location: http://drgoulu.wordpress.com/" );<br/>
?&gt;</code><br/>
ce qui redirigeait les accès à l’ancien site vers le nouveau blog.</li>
<li>J’ai cependant conservé mon contrat d’hébergement car j’avais besoin d’un serveur e-mail @goulu.net</li>
<li>Pour différentes raisons, j’ai  acheté d’autres noms de domaine comme <a href="http://pro-g.ch" target="_blank">pro-g.ch</a> et <a href="http://projets.ch" target="_blank">projets.ch</a>, et un hébergement chez <a href="http://infomaniak.ch" target="_blank">infomaniak.ch</a>, qui permet de définir des domaines « synonymes » : plusieurs domaines peuvent ainsi partager le même site web.</li>
</ol>
<p>A ce moment, je me suis dit que j’allais pouvoir économiser mon vieil hébergement si j’arrivais :</p>
<ol>
<li>à définir goulu.net comme un nouveau synonyme de l’hébergement chez infomaniak, ce qui me permet de plus de recevoir tous mes mails sur un seul compte au lieu de 2</li>
<li>à réaliser un « redirection conditionnelle » pour que les gens qui tapent <a href="http://www.goulu.net" target="_blank">www.goulu.net</a> continuent à se retrouver sur mon blog au lieu de tomber sur mon site <a href="http://pro-g.ch" target="_blank">pro-g.ch</a> en construction.</li>
</ol>
<p>Petite contrainte supplémentaire, je voulais éviter de faire ça en PHP pour ne pas interférer avec le système existant sur pro-g. Par chance, infomaniak a bien configuré ses serveurs : s’il existe un document nommé index.html, il a la priorité sur index.php. Donc il m’a suffit de faire un fichier index.html contenant un peu de JavaScript :</p>
<p><code>&lt;html &gt;<br/>
&lt;head&gt;<br/>
&lt;title&gt;goulu.net redirect page&lt;/title&gt;<br/>
&lt;/head&gt;<br/>
&lt;body&gt;<br/>
&lt;script language="JavaScript" type="text/javascript"&gt;<br/>
&lt;!--<br/>
var d="http://projets.ch/index.php";<br/>
var p=document.URL;<br/>
if (p.indexOf("goulu.net") != -1) d="http://drgoulu.wordpress.com/";<br/>
window.location.replace(d);<br/>
--&gt;<br/>
&lt;/script&gt;<br/>
&lt;/body&gt;<br/>
&lt;/html&gt;</code></p>
<p>ça marche, et ça donne des pistes sur comment faire un système de redirection assez sophistiqué grâce à JavaScript, un langage incontournable du Web, souvent sous-estimé.</p>

## Commentaires

### ysengrimus — 16 juillet 2009 à 12:31

<section class="comment-content comment">
<p>Quel type de blogue êtes-vous? Voici la typologie:</p>
<p><a href="http://ysengrimus.wordpress.com/2009/07/15/typologie-des-carnets-blogues-electroniques/" rel="nofollow ugc">http://ysengrimus.wordpress.com/2009/07/15/typologie-des-carnets-blogues-electroniques/</a></p>
<p>Merci.<br/>
Paul Laurendeau</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
