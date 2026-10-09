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

### Introduction

[« Solar with Lyrics » de Flight 404](http://www.flight404.com/blog/?p=111)

\[vimeo 658158 600 337\]

Processing : un langage pour artistes multimedia et « visualisateurs »

### <!--more-->Installation et « Hello World »

1. lire [l’article « Processing » sur Wikipedia](http://fr.wikipedia.org/wiki/Processing)
2. [télécharger Processing](http://processing.org/download/) depuis le site processing.org. Il n’y a **pas** besoin d’installation (à part la machine JAVA)
3. lancer processing.exe
4. taper le code figurant dans la fenêtre ci-dessous:\
    [![](/media/2011/10/processing1.png "processing1")](/media/2011/10/processing1.png)
5. dans le menu « Tools » choisir « Create Font… »
    - sélectionner une police quelconque
    - entrer « myfont » comme nom de police
    - presser « ok » pour créer la police
6. cliquer le bouton « Run » : une fenêtre avec « Hello World! » scrollant en blanc sur fond noir apparait
7. explications:
    - la syntaxe du langage est celle de JAVA (proche de C++, Case Sensitive…)
    - si elle existe, la fonction « setup » est exécutée automatiquement au lancement du programme
    - si elle existe, la fonction « draw » est exécutée au prochain « rafraîchissement d’écran ».
8. ajouter  \<code\>println(frameRate); \</code\>dans draw pour visualiser la cadence
9. ajouter  \<code\>frameRate(100); \</code\>dans setup pour forcer la cadence
10. faire File/Save, sélectionner n’importe quel dossier et donner le nom « tuto »
    - un programme processing s’appelle un « sketch »
11. faire File/Export Application
    - on peut compiler des applications pour Windows, Mac et Linux d’un seul coup !
12. faire Sketch/Show Sketch Folder
    - Processing groupe tout ce qu’il faut dans un dossier ayant le nom du sketch. Ne rien déplacer…

### Oeuvres et sources d’inspiration

- <http://processing.org/exhibition/>
- <http://www.openprocessing.org/>
- <http://www.openprocessing.org/portal/?userID=573>

### « [Pavages aléatoires](http://drgoulu.com/2011/10/03/pavages-aleatoires/) » : le making of

Commençons par générer des disques aléatoires:

\[sourcecode lang= »java »\]void setup() {\
smooth();\
size(600,400);\
colorMode(RGB,255);\
background(0,0,64); // dark blue\
noStroke();\
}

int i=0;

void draw() {\
colorMode(HSB, 100);\
fill(i%100,100,100); // color cycle\
i++;\
float a=100000/i; // area\
float r=sqrt(a/PI); // radius of circle\
float x=random(r,width-r);\
float y=random(r,height-r);\
ellipse(x,y,r\*2,r\*2);\
}

void keyPressed()\
{\
setup(); // restart\
}\[/sourcecode\]

Un peu de classes:

- On définit la classe Poly représentant un cercle …
- … dont le centre est de la classe prédéfinie [PVector](http://processing.org/reference/PVector.html) pour faciliter les opérations géométriques
- et on mémorise les cercles tracés dans un conteneur prédéfini [ArrayList](http://processing.org/reference/ArrayList.html)

\[sourcecode lang= »java »\]// a polygon, at this point a circle\
class Poly {\
float area, radius;\
PVector center;

Poly(float a) { // construct from area\
area=a;\
radius=sqrt(area/PI);\
center = new PVector();\
}

void Random() {\
center.x=random(radius,width-radius);\
center.y=random(radius,height-radius);\
}

void Draw() {\
ellipse(center.x,center.y,2\*radius,2\*radius);\
}

boolean Intersect(Poly p) { // true if p intersect this Poly\
float d=center.dist(p.center);\
if (d\>p.radius+this.radius) return false;\
return true;\
}\
}

ArrayList polys; // list of all drawn shapes

boolean Intersect(Poly p) { // true if p intersects any of the polys\
for (int i = 0; i\<polys.size(); i++) // slower test\
{if (p.Intersect((Poly)polys.get(i))) return true;}\
return false;\
}

void setup() {\
smooth();\
size(600,400);\
colorMode(RGB,255);\
background(0,0,64); // dark blue\
noStroke();\
polys=new ArrayList();\
}

int i=0;

void draw() {\
colorMode(HSB, 100);\
fill(i%100,100,100); // color cycle\
i++;\
float a=10000/i; // area\
Poly p=new Poly(a);\
p.Random();\
for (int j=0; Intersect(p); j++) {p.Random();}\
p.Draw();\
polys.add(p);\
}

void keyPressed()\
{\
saveFrame("capture-####.png");\
setup(); // restart\
}\[/sourcecode\]

la fonction saveFrame est bien utile pour faire un film, ou juste pour une capture d’écran comme ici:

[![](/media/2011/10/capture-0259.png "capture-0259")](/media/2011/10/capture-0259.png)

Pour bien remplir le plan, il faut faire décroître la surface des cercles selon une loi précise, expliquée [chez Dr. Goulu](http://drgoulu.com/2011/10/03/pavages-aleatoires/). Enfin, on peut compléter la classe Poly pour qu’elle gère des polygones à n côtés. Voir [la version finale ici](http://www.openprocessing.org/visuals/?visualID=40422).

### [Librairies](http://processing.org/reference/libraries/)

il existe de nombreuses [libraries](http://processing.org/reference/libraries/) apportant des fonctions multimédia évoluées, la lecture/écriture de divers formats de fichiers et des interface diverses.

### Liens

1. [Les tutoriels](http://processing.org/learning/index.html) et le [wiki](http://wiki.processing.org/w/Main_Page) officiels (en anglais)
2. [Processing.js](http://processingjs.org/) : Processing en Javascript, tourne sur un browser moderne, sans Java !
3. [mon premier article sur Processing](http://drgoulu.com/2008/04/03/processing/), et [celui sur la Joconde](http://drgoulu.com/2010/06/13/optimisation-de-la-joconde/)
4. [mes bookmarks sur Processing](http://delicious.com/goulu/processing) (nombreuses librairies)
5. utilisation de [Processing avec Arduino](http://www.arduino.cc/playground/Interfacing/Processing)
6. [Processing / Android](http://wiki.processing.org/w/Android)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
