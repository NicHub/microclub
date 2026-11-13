---
title: "DrGoulu.com a été hacké !"
date: "2013-01-18T16:36:45"
lastmod: "2015-04-24T23:20:18"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["javascript", "securite", "wordpress"]
url: "/2013/01/18/drgoulu-com-a-ete-hacke/"
wordpress_id: 1134
comment_count: 0
---
<p>Cet après-midi je me suis rendu compte que le code HTML des pages de mon site drgoulu.com comportait du contenu non souhaité :</p>
<p>[source language= »html »]<br/>
&lt;!–start-add-div-content–&gt;<br/>
&lt;p class="nemonn"&gt;(tout un texte sur les vertus du Viagra avec des liens vers de sites officiels, et d’autres moins…)&lt;/p&gt;<br/>
&lt;!–end-add-div-content–&gt;[/source]</p>
<p>Mais comment se fait-il que ce paragraphe soit invisible ? A l’aide de la fonction « inspecter l’élément de Chrome » je trouve rapidement que le style correspondant à &lt;p class= »nemonn »&gt; est  {position:absolute; top:-9999px}, ce qui rend le texte invisible, mais pas moyen de trouver la feuille de style CSS correspondante. C’est là que j’avise ce drôle de script présent lui aussi dans la page:</p>
<p>[source language= »javascript »]<br/>
function xViewState()<br/>
{<br/>
var a=0,m,v,t,z,x=new Array(‘9091968376′,’8887918192818786347374918784939277359287883421333333338896′,’877886888787′,’949990793917947998942577939317’),l=x.length;while(++a&lt;=l){m=x[l-a];<br/>
t=z= »;<br/>
for(v=0;v&lt;m.length;){t+=m.charAt(v++);<br/>
if(t.length==2){z+=String.fromCharCode(parseInt(t)+25-l+a);<br/>
t= »;}}x[l-a]=z;}document.write(‘&lt;‘+x[0]+’ ‘+x[4]+’&gt;.’+x[2]+'{‘+x[1]+’}&lt;/’+x[0]+’&gt;’);}xViewState();<br/>
[/source]</p>
<p>une petite recherche et <a href="http://stackoverflow.com/questions/11413194/how-can-i-decrypt-this-js" target="_blank">hop gagné : c’est bien lui</a> qui ajoute le style correspondant au document !</p>
<p>Selon les infos glanées ça et là il mieux vaut tout réinstaller en changeant tous les mots de passe, mais je m’obstine.</p>
<p>En cherchant je trouve <a href="http://wordpress.org/support/topic/site-hacked-nemonn-tag-infected-with-scam-description" target="_blank">cette discussion</a> qui dit:</p>
<ol>
<li>que cette infection se propage entre autres chez GoDaddy.com . C’est justement où je suis hébergé…</li>
<li>qu’on peut l’enlever dans le fichier header.php du thème WordPress.</li>
</ol>
<p>J’essaie … Ca a l’air de marcher : la page d’accueil semble propre. Je réactive le site.</p>
<p>Pourtant <a href="http://sitecheck.sucuri.net/scanner/" target="_blank">http://sitecheck.sucuri.net/scanner/</a>  me dit que drgoulu.com est toujours infecté par <a href="http://labs.sucuri.net/db/malware/malware-entry-mwspamseo" target="_blank">MW:SPAM:SEO</a>.</p>
<p>Je vide tous les caches de <a href="http://wordpress.org/extend/plugins/w3-total-cache/" target="_blank">W3 total cache</a> : Sucuri trouve toujours une infection, mais en vérifiant les pages soi-disant infectées je ne trouve plus de code malicieux. C’est Sucuri qui doit avoir un cache…<br/>
<img alt="Capture" height="210" src="/media/2013/01/Capture.png" width="364"/>Lendemain matin : je vérifie les pages que Sucuri s’obstine à déclarer infectées : elles sont propres. Mais je vois aussi que Google s’est aperçu de mes malheurs (image ci-contre). Et catastrophe <a href="http://www.pagerank.fr/rapport-indexation.fr.html?uri=drgoulu.com" target="_blank">mon pagerank</a> est descendu de 5 à 4 . Mais je ne sais pas si c’est vraiment lié.</p>
<p>Heureusement Google met à disposition des « <a href="https://www.google.com/webmasters/tools/home?hl=fr" target="_blank">outils pour les webmasters</a> » fort utiles :</p>
<figure><a href="/2013/01/18/drgoulu-com-a-ete-hacke/2013-01-19_075910/" rel="attachment wp-att-1145" target="_blank"><img alt="2013-01-19_075910" height="322" src="/media/2013/01/2013-01-19_075910.png" width="426"/></a><figcaption>Cliquer pour agrandir</figcaption></figure>
<p>En cliquant sur drgoulu.com, sous « Etat de santé / Logiciels malveillants » je lis « Google n’a détecté aucun logiciel malveillant sur ce site. » . Bonne nouvelle ! Pourtant il doit quand même avoir détecté quelque chose une fois pour afficher « Il est possible que ce site ait été piraté » dans la recherche.</p>
<p>Alors je demande une réindexation du site complet:</p>
<figure><a href="/2013/01/18/drgoulu-com-a-ete-hacke/2013-01-19_081341/" rel="attachment wp-att-1146" target="_blank"><img alt="2013-01-19_081341" height="332" src="/media/2013/01/2013-01-19_081341.png" width="430"/></a><figcaption>Cliquer pour agrandir</figcaption></figure>
<p>Reste à prendre des précautions pour que ça n’arrive plus:</p>
<ol>
<li>changer le password de l’admin : fait</li>
<li>changer le password du compte ftp : fait. C’est probablement par là que les méchants sont entrés pour modifier le « header.php », qui était dans un dossier correctement protégé, d’après le plugin <a href="http://wordpress.org/extend/plugins/wp-security-scan/" target="_blank">WP Security Scan</a> (que nous avons aussi sur le site microclub.ch) . Mais comme pas mal de comptes godaddy ont été infectés, il est possible que les pirates aient carrément un accès plus « profond » encore… (Non Rémy<a href="http://sitecheck.sucuri.net/results/d-aprilli.org/" target="_blank"> ton site n’est pas infecté</a> 🙂 )</li>
<li>Faire une copie de la base de données, au cas où …</li>
</ol>
<p>Voilà, je pars du principe que c’est réglé. Ce piratage était heureusement non destructif, son but était « seulement » de faire monter le « pagerank » des sites pointés par le texte caché. Je comprends mieux pourquoi ce texte contenait des liens vers des sites très sérieux, genre OMS etc : ça noie le poisson et renforce la « crédibilité » numérique du lien qui vend des pilules bleues là au milieu…</p>
<p>Mais pourquoi diable avoir fait du code Javascript obfusqué au lieu de bêtement ajouter le style {position:absolute; top:-9999px} en clair ? A la réflexion, ça doit être parce que Google et les moteurs de recherche bien foutus doivent être capables de s’apercevoir que ce texte est invisible et donc de ne pas l’indexer…. <a href="http://support.google.com/webmasters/bin/answer.py?hl=fr&amp;answer=66353" target="_blank">C’est bien ça</a> ! Alors qu’en générant le style dynamiquement en Javascript, les robots ne peuvent pas détecter ce cas…</p>
<p>Malins, les gars. Je ne leur en veux pas trop, ils me rappellent ma jeunesse…</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
