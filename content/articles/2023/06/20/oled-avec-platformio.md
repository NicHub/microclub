---
title: "OLED avec platformIO"
date: "2023-06-20T16:56:15"
lastmod: "2023-07-02T08:09:09"
author: "franic"
categories: ["Microclub"]
tags: []
url: "/2023/06/20/oled-avec-platformio/"
wordpress_id: 5168
comment_count: 0
---
<h5></h5>
<p><img height="224" src="/media/2023/06/word-image-5168-1.jpeg" width="320"/></p>
<h1>Librairie U8g2</h1>
<p>Cette librairie vous permettra d’afficher soit des chaines de caractères soit des formes graphiques et même des logos !</p>
<p><em>La documentation en ligne est très bien rédigée : </em><a href="https://github.com/olikraus/u8g2/wiki"><em>https://github.com/olikraus/u8g2/wiki</em></a></p>
<p><em>La même librairie peut être utilisée en mode a</em><em>lphanumérique et/ou graphique . Elle est c</em><em>ompatible avec une large gamme d’afficheurs !</em></p>
<p>Attention, en mode graphique, il n’y pas de miracle, cela consomme un peu de mémoire !</p>
<p></p>
<h4>Création d’un projet « Alphanumérique »</h4>
<p>Cet exemple a été programmé sur platformIO.</p>
<p><em>1 Insérer le chargement de la librairie dans le fichier PlateformIO.ini (En choisir qu’une seule parmi les 3 proposées) :</em></p>
<p>lib_deps =</p>
<p>olikraus/U8g2 @ ^2.34.18 <span>; accepte toutes les mises à jour</span></p>
<p>olikraus/U8g2 @ ~2.34.18<span> ; accepte que les mises à jour mineurs</span></p>
<p>olikraus/U8g2 @ 2.34.18 <span>; n’utilise que la version exacte</span></p>
<p></p>
<p><i>2 Dans le fichier main.cpp, inclure la librairie et déclarer l’afficheur (dans notre cas SSD1306 en mode I2C sans pin reset spécifique)</i></p>
<p><span>#include &lt;U8x8lib.h&gt;</span></p>
<p><span>U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8</span><span>(/* reset=*/ U8X8_PIN_NONE);</span></p>
<p></p>
<p><i>3 Dans le setup, initialiser l’afficheur avec le « </i><i>begin</i><i> </i><i>»</i></p>
<p><span>void setup()</span></p>
<p><span>{</span></p>
<p> <span> u8x8.begin</span>();</p>
<p><span>}</span></p>
<p><i>4 Dans la boucle </i><i>loop</i><i>, sélectionnez la police de caractères, écrivez le texte à l’endroit désiré et affichez le résultat :</i></p>
<p><span>void loop()</span></p>
<p><span>{</span></p>
<p>  <span>u8x8</span>.<span>setFont</span><span>(u8x8_font_chroma48medium8_r)</span>;  <span>// sélection de la police de caractères</span></p>
<p>  <span>u8x8</span>.<span>drawString</span><span>(0,1, »Hello World! »)</span>; <span> // coordonnées de la ligne et colonne du texte et la chaîne de caractères</span></p>
<p>  <span>u8x8</span>.<span>refreshDisplay<span>()</span>;</span>  <span>// afficher le résultat</span></p>
<p>  <span>delay(2000);</span></p>
<p><span>}</span></p>
<p><i>Il est possible d’inverser </i><i>les couleurs de </i><i>l’affichage d’un texte en utilisant la fonction </i><i>SetInverseFont</i><i>() :</i></p>
<p><span>void loop()</span></p>
<p><span>{</span></p>
<p>  <span>u8x8</span>.<span>setFont</span><span>(u8x8_font_chroma48medium8_r)</span>;</p>
<p>  <span>u8x8</span>.<span>setInverseFont</span><span>(1)</span>;  </p>
<p>  <span>u8x8</span>.<span>drawString</span><span>(0,1, »Hello World! »)</span>;</p>
<p>  <span>u8x8</span>.<span>drawString</span><span>(0,0, »0123456789″)</span>;</p>
<p>  <span>u8x8</span>.<span>refreshDisplay</span><span>()</span>;    </p>
<p>  delay(2000);</p>
<p><span>}</span> </p>
<p></p>
<p>Et voici le résultat :</p>
<p><img height="181" src="/media/2023/06/word-image-5168-1.png" width="318"/></p>
<p><a href="/media/2023/06/ESP32ssd1306_alpha.zip">Télécharger l’exemple complet pour plateformIO</a></p>
<h4>Création d’un projet « Alphanumérique »</h4>
<p><i><em>1 Comme dans l’exemple précédent, insérer le chargement de la librairie dans le fichier PlateformIO.ini (En choisir qu’une seule parmi les 3 proposées) :</em></i></p>
<p>lib_deps =</p>
<p>  olikraus/U8g2 @ ^2.34.18<span> ; accepte toutes les mises à jour</span></p>
<p>  olikraus/U8g2 @ ~2.34.18<span> ; accepte que les mises à jour mineurs</span></p>
<p>  olikraus/U8g2 @ 2.34.18 <span>; n’utilise que la version exacte</span></p>
<p></p>
<p><i>2 Dans le fichier main.cpp, inclure la librairie et déclarer l’afficheur (dans notre cas SSD1306 en mode I2C sans pin reset spécifique)</i></p>
<p><span>#include &lt;U8g2lib.h&gt;</span></p>
<p><span>U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2</span><span>(U8G2_R0, /* reset=*/ U8X8_PIN_NONE, /* clock=*/ 22, /* data=*/ 21);</span></p>
<p></p>
<p><i>3 Dans le setup, initialiser l’afficheur avec le « </i><i>begin</i><i> » :</i></p>
<p>void setup()</p>
<p>{</p>
<p>  <span>u8g2<span>.</span></span><span>begin();</span></p>
<p>}</p>
<p>4 Dans le loop, voici le programme pour afficher :</p>
<p><span>void loop()</span></p>
<p>{</p>
<p> <span> u8g2</span><span>.firstPage()</span>;  <span>//affiche la première page</span></p>
<p>  do {</p>
<p>    <span>u8g2</span><span>.setFont</span>(u8g2_font_ncenB14_tr);  <span>// sélectionne la police de caractères</span></p>
<p>    <span>u8g2</span><span>.drawStr</span>(0,15, »Microclub »); <span>//affiche le texte à la position 0;15</span></p>
<p>    <span>u8g2</span><span>.drawCircle</span>(20, 35, 10, U8G2_DRAW_ALL);<span> // dessine un cercle de rayon 10 à la position 20;35</span></p>
<p>    <span>u8g2</span><span>.drawFrame</span>(80,30,25,15);<span> // dessine un rectangle coordonnée du premier point 80;30 et second point 25;15</span></p>
<p>  } <span>while</span> ( <span>u8g2</span>.<span>nextPage()</span> ); <span>// ajoute toutes les pages</span></p>
<p>  delay(1000);</p>
<p>}</p>
<p>Et voici le résultat :</p>
<p></p>
<p><img height="191" src="/media/2023/06/word-image-5168-1-1.png" width="328"/></p>
<p><a href="/media/2023/06/ESP32ssd_graph1.zip">Téléchargez cet exemple pour platformio </a></p>
<h4> </h4>
<h4>Importation d’un bitmap et conversion pour OLED</h4>
<p><em>Ajouter un logo bitmap dans votre projet :</em></p>
<ul>
<li>Téléchargez un logo depuis un site comme <a href="http://www.flaticon.com/">www.flaticon.com</a></li>
<li>Ouvrer le logiciel de traitement d’image GIMP</li>
<li>Importez l’image dans le logiciel</li>
<li>Sous image, sélectionner Echelle et taille de l’image</li>
</ul>
<p><img height="401" src="/media/2023/06/word-image-5168-1-4.png" width="517"/></p>
<p></p>
<ul>
<li>Choisissez une taille plus petite ou égale à la résolution de votre afficheur</li>
<li>Sélectionne à nouveau le menu image, puis Mode et sélectionnez couleurs indexées</li>
</ul>
<p><img height="351" src="/media/2023/06/word-image-5168-2-2.png" width="524"/></p>
<ul>
<li>Sélectionnez «utiliser la palette noir et blanc(1-bit)»</li>
<li>Sous tramage des couleurs, sélectionnez aucun</li>
<li>Terminez en appuyant sur «convertir»</li>
</ul>
<p><img height="447" src="/media/2023/06/word-image-5168-3-1.png" width="545"/></p>
<ul>
<li>Terminez en exportant le dessin en format XBM</li>
<li>Sous le menu Fichier, sélectionnez «Exportez sous …»</li>
<li>Terminez en exportant le dessin en format XBM</li>
<li>Attention le nom du fichier sera repris plus tard, alors choisissez un nom simple !</li>
</ul>
<p><img height="401" src="/media/2023/06/word-image-5168-4.png" width="517"/></p>
<ul>
<li>Ouvrez un éditeur de texte et copiez son contenu</li>
<li>Collez ce contenu dans le fichier main.cpp après la déclaration de l’afficheur</li>
</ul>
<p><span>U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2</span><span>(U8G2_R0, /* reset=*/ U8X8_PIN_NONE, /* clock=*/ 22, /* data=*/ 21);</span></p>
<p><span>// importation du fichier *.xbm</span><br/><span>#define</span> u8g2_logo_97x51_width 97</p>
<p><span>#define</span> u8g2_logo_97x51_height 51</p>
<p><span>static const unsigned char</span> u8g2_logo_97x51_bits[] U8X8_PROGMEM = {</p>
<p>   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,</p>
<p>   0x00, 0x3c, 0x80, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00,</p>
<p>   0x00, 0x00, 0x3c, 0x80, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfe,</p>
<p>…..</p>
<p><span>void loop()</span></p>
<p>{</p>
<p>  <span>u8g2</span>.<span>firstPage()</span>;</p>
<p>  do</p>
<p>  {</p>
<p>    <span>u8g2</span><span>.drawXBMP</span>(0,0, pouces_width, pouces_height, pouces_bits); <span> // affichez le bitmap à la coordonnée 0,0</span></p>
<p>  } while ( <span>u8g2<span>.</span></span><span>nextPage()</span> );</p>
<p>  delay(1000);</p>
<p>}</p>
<p><img height="157" src="/media/2023/06/word-image-5168-5.png" width="276"/></p>
<p><a href="/media/2023/06/ESP32ssd_logo.zip">Téléchargez cet exemple pour platformIO</a></p>
<p></p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
