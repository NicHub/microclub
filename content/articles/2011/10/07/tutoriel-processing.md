---
title: "Tutoriel Processing"
date: "2011-10-07T17:00:37"
lastmod: "2015-04-24T23:20:19"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["processing", "programmation"]
url: "/2011/10/07/tutoriel-processing/"
wordpress_id: 536
comment_count: 0
---
<h3>Introduction</h3>
<p><a href="http://www.flight404.com/blog/?p=111" target="_blank">« Solar with Lyrics » de Flight 404</a></p>
<p>[vimeo 658158 600 337]</p>
<p>Processing : un langage pour artistes multimedia et « visualisateurs »</p>
<h3><!--more-->Installation et « Hello World » !</h3>
<ol>
<li>lire <a href="http://fr.wikipedia.org/wiki/Processing" target="_blank">l’article « Processing » sur Wikipedia</a></li>
<li><a href="http://processing.org/download/" target="_blank">télécharger Processing</a> depuis le site processing.org. Il n’y a <strong>pas </strong>besoin d’installation (à part la machine JAVA)</li>
<li>lancer processing.exe</li>
<li>taper le code figurant dans la fenêtre ci-dessous:<br/>
<a href="/media/2011/10/processing1.png"><img alt="" height="530" src="/media/2011/10/processing1.png" title="processing1" width="466"/></a></li>
<li>dans le menu « Tools » choisir « Create Font… »
<ul>
<li>sélectionner une police quelconque</li>
<li>entrer « myfont » comme nom de police</li>
<li>presser « ok » pour créer la police</li>
</ul>
</li>
<li>cliquer le bouton « Run » : une fenêtre avec « Hello World! » scrollant en blanc sur fond noir apparait</li>
<li>explications:
<ul>
<li>la syntaxe du langage est celle de JAVA (proche de C++, Case Sensitive…)</li>
<li>si elle existe, la fonction « setup » est exécutée automatiquement au lancement du programme</li>
<li>si elle existe, la fonction « draw » est exécutée au prochain « rafraîchissement d’écran ».</li>
</ul>
</li>
<li>ajouter  <code>println(frameRate); </code>dans draw pour visualiser la cadence</li>
<li>ajouter  <code>frameRate(100); </code>dans setup pour forcer la cadence</li>
<li>faire File/Save, sélectionner n’importe quel dossier et donner le nom « tuto »
<ul>
<li>un programme processing s’appelle un « sketch »</li>
</ul>
</li>
<li>faire File/Export Application
<ul>
<li>on peut compiler des applications pour Windows, Mac et Linux d’un seul coup !</li>
</ul>
</li>
<li>faire Sketch/Show Sketch Folder
<ul>
<li>Processing groupe tout ce qu’il faut dans un dossier ayant le nom du sketch. Ne rien déplacer…</li>
</ul>
</li>
</ol>
<h3>Oeuvres et sources d’inspiration</h3>
<ul>
<li><a href="http://processing.org/exhibition/">http://processing.org/exhibition/</a></li>
<li><a href="http://www.openprocessing.org/">http://www.openprocessing.org/</a></li>
<li><a href="http://www.openprocessing.org/portal/?userID=573">http://www.openprocessing.org/portal/?userID=573</a></li>
</ul>
<h3>« <a href="http://drgoulu.com/2011/10/03/pavages-aleatoires/">Pavages aléatoires</a> » : le making of</h3>
<p>Commençons par générer des disques aléatoires:</p>
<p>[sourcecode lang= »java »]void setup() {<br/>
  smooth();<br/>
  size(600,400);<br/>
  colorMode(RGB,255);<br/>
  background(0,0,64);  // dark blue<br/>
  noStroke();<br/>
}</p>
<p>int i=0;</p>
<p>void draw() {<br/>
 colorMode(HSB, 100);<br/>
 fill(i%100,100,100); // color cycle<br/>
 i++;<br/>
 float a=100000/i;  // area<br/>
 float r=sqrt(a/PI); // radius of circle<br/>
 float x=random(r,width-r);<br/>
 float y=random(r,height-r);<br/>
 ellipse(x,y,r*2,r*2);<br/>
}</p>
<p>void keyPressed()<br/>
{<br/>
 setup(); // restart<br/>
}[/sourcecode]</p>
<p>Un peu de classes:</p>
<ul>
<li>On définit la classe Poly représentant un cercle …</li>
<li>… dont le centre est de la classe prédéfinie <a href="http://processing.org/reference/PVector.html" target="_blank">PVector</a> pour faciliter les opérations géométriques</li>
<li>et on mémorise les cercles tracés dans un conteneur prédéfini <a href="http://processing.org/reference/ArrayList.html" target="_blank">ArrayList</a></li>
</ul>
<p>[sourcecode lang= »java »]// a polygon, at this point a circle<br/>
class Poly {<br/>
  float area, radius;<br/>
  PVector center;</p>
<p>  Poly(float a) {  // construct from area<br/>
    area=a;<br/>
    radius=sqrt(area/PI);<br/>
    center = new PVector();<br/>
  }</p>
<p>  void Random() {<br/>
    center.x=random(radius,width-radius);<br/>
    center.y=random(radius,height-radius);<br/>
  }</p>
<p>  void Draw() {<br/>
    ellipse(center.x,center.y,2*radius,2*radius);<br/>
  }</p>
<p>  boolean Intersect(Poly p) {  // true if p intersect this Poly<br/>
    float d=center.dist(p.center);<br/>
    if (d&gt;p.radius+this.radius) return false;<br/>
    return true;<br/>
  }<br/>
}</p>
<p>ArrayList polys;  // list of all drawn shapes</p>
<p>boolean Intersect(Poly p) { // true if p intersects any of the polys<br/>
  for (int i = 0; i&lt;polys.size(); i++) // slower test<br/>
    {if (p.Intersect((Poly)polys.get(i))) return true;}<br/>
  return false;<br/>
}</p>
<p>void setup() {<br/>
  smooth();<br/>
  size(600,400);<br/>
  colorMode(RGB,255);<br/>
  background(0,0,64);  // dark blue<br/>
  noStroke();<br/>
  polys=new ArrayList();<br/>
}</p>
<p>int i=0;</p>
<p>void draw() {<br/>
  colorMode(HSB, 100);<br/>
  fill(i%100,100,100); // color cycle<br/>
  i++;<br/>
  float a=10000/i;  // area<br/>
  Poly p=new Poly(a);<br/>
  p.Random();<br/>
  for (int j=0; Intersect(p); j++) {p.Random();}<br/>
  p.Draw();<br/>
  polys.add(p);<br/>
}</p>
<p>void keyPressed()<br/>
{<br/>
 saveFrame("capture-####.png");<br/>
 setup(); // restart<br/>
}[/sourcecode]</p>
<p>la fonction saveFrame est bien utile pour faire un film, ou juste pour une capture d’écran comme ici:</p>
<p><a href="/media/2011/10/capture-0259.png"><img alt="" height="400" src="/media/2011/10/capture-0259.png" title="capture-0259" width="600"/></a></p>
<p>Pour bien remplir le plan, il faut faire décroître la surface des cercles selon une loi précise, expliquée <a href="http://drgoulu.com/2011/10/03/pavages-aleatoires/" target="_blank">chez Dr. Goulu</a>. Enfin, on peut compléter la classe Poly pour qu’elle gère des polygones à n côtés. Voir <a href="http://www.openprocessing.org/visuals/?visualID=40422" target="_blank">la version finale ici</a>.</p>
<h3><a href="http://processing.org/reference/libraries/">Librairies</a></h3>
<p>il existe de nombreuses <a href="http://processing.org/reference/libraries/">libraries</a> apportant des fonctions multimédia évoluées, la lecture/écriture de divers formats de fichiers et des interface diverses.</p>
<h3>Liens</h3>
<ol>
<li><a href="http://processing.org/learning/index.html">Les tutoriels</a> et le <a href="http://wiki.processing.org/w/Main_Page" target="_blank">wiki </a>officiels (en anglais)</li>
<li><a href="http://processingjs.org/" target="_blank">Processing.js</a> : Processing en Javascript, tourne sur un browser moderne, sans Java !</li>
<li><a href="http://drgoulu.com/2008/04/03/processing/" target="_blank">mon premier article sur Processing</a>, et <a href="http://drgoulu.com/2010/06/13/optimisation-de-la-joconde/" target="_blank">celui sur la Joconde</a></li>
<li><a href="http://delicious.com/goulu/processing" target="_blank">mes bookmarks sur Processing</a> (nombreuses librairies)</li>
<li>utilisation de <a href="http://www.arduino.cc/playground/Interfacing/Processing" target="_blank">Processing avec Arduino</a></li>
<li><a href="http://wiki.processing.org/w/Android" target="_blank">Processing / Android</a></li>
</ol>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
