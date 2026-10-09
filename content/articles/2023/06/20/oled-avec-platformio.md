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

#####

![](/media/2023/06/word-image-5168-1.jpeg)

# Librairie U8g2

Cette librairie vous permettra d’afficher soit des chaines de caractères soit des formes graphiques et même des logos !

*La documentation en ligne est très bien rédigée :* [*https://github.com/olikraus/u8g2/wiki*](https://github.com/olikraus/u8g2/wiki)

*La même librairie peut être utilisée en mode alphanumérique et/ou graphique . Elle est compatible avec une large gamme d’afficheurs !*

Attention, en mode graphique, il n’y pas de miracle, cela consomme un peu de mémoire !

#### Création d’un projet « Alphanumérique »

Cet exemple a été programmé sur platformIO.

*1 Insérer le chargement de la librairie dans le fichier PlateformIO.ini (En choisir qu’une seule parmi les 3 proposées) :*

lib_deps =

olikraus/U8g2 @ ^2.34.18 ; accepte toutes les mises à jour

olikraus/U8g2 @ ~2.34.18 ; accepte que les mises à jour mineurs

olikraus/U8g2 @ 2.34.18 ; n’utilise que la version exacte

*2 Dans le fichier main.cpp, inclure la librairie et déclarer l’afficheur (dans notre cas SSD1306 en mode I2C sans pin reset spécifique)*

\#include \<U8x8lib.h\>

U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/\* reset=\*/ U8X8_PIN_NONE);

*3 Dans le setup, initialiser l’afficheur avec le «* *begin »*

void setup()

{

  u8x8.begin();

}

*4 Dans la boucle* *loop, sélectionnez la police de caractères, écrivez le texte à l’endroit désiré et affichez le résultat :*

void loop()

{

  u8x8.setFont(u8x8_font_chroma48medium8_r);  // sélection de la police de caractères

  u8x8.drawString(0,1, »Hello World! »);  // coordonnées de la ligne et colonne du texte et la chaîne de caractères

  u8x8.refreshDisplay();  // afficher le résultat

  delay(2000);

}

*Il est possible d’inverser* *les couleurs de* *l’affichage d’un texte en utilisant la fonction* *SetInverseFont() :*

void loop()

{

  u8x8.setFont(u8x8_font_chroma48medium8_r);

  u8x8.setInverseFont(1);  

  u8x8.drawString(0,1, »Hello World! »);

  u8x8.drawString(0,0, »0123456789″);

  u8x8.refreshDisplay();

  delay(2000);

}

Et voici le résultat :

![](/media/2023/06/word-image-5168-1.png)

[Télécharger l’exemple complet pour plateformIO](/media/2023/06/ESP32ssd1306_alpha.zip)

#### Création d’un projet « Alphanumérique »

1 Comme dans l’exemple précédent, insérer le chargement de la librairie dans le fichier PlateformIO.ini (En choisir qu’une seule parmi les 3 proposées) :

lib_deps =

  olikraus/U8g2 @ ^2.34.18 ; accepte toutes les mises à jour

  olikraus/U8g2 @ ~2.34.18 ; accepte que les mises à jour mineurs

  olikraus/U8g2 @ 2.34.18 ; n’utilise que la version exacte

*2 Dans le fichier main.cpp, inclure la librairie et déclarer l’afficheur (dans notre cas SSD1306 en mode I2C sans pin reset spécifique)*

\#include \<U8g2lib.h\>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /\* reset=\*/ U8X8_PIN_NONE, /\* clock=\*/ 22, /\* data=\*/ 21);

*3 Dans le setup, initialiser l’afficheur avec le «* *begin » :*

void setup()

{

  u8g2.begin();

}

4 Dans le loop, voici le programme pour afficher :

void loop()

{

  u8g2.firstPage();  //affiche la première page

  do {

    u8g2.setFont(u8g2_font_ncenB14_tr);  // sélectionne la police de caractères

    u8g2.drawStr(0,15, »Microclub »); //affiche le texte à la position 0;15

    u8g2.drawCircle(20, 35, 10, U8G2_DRAW_ALL); // dessine un cercle de rayon 10 à la position 20;35

    u8g2.drawFrame(80,30,25,15); // dessine un rectangle coordonnée du premier point 80;30 et second point 25;15

  } while ( u8g2.nextPage() ); // ajoute toutes les pages

  delay(1000);

}

Et voici le résultat :

![](/media/2023/06/word-image-5168-1-1.png)

[Téléchargez cet exemple pour platformio](/media/2023/06/ESP32ssd_graph1.zip)

####  

#### Importation d’un bitmap et conversion pour OLED

*Ajouter un logo bitmap dans votre projet :*

- Téléchargez un logo depuis un site comme [www.flaticon.com](http://www.flaticon.com/)
- Ouvrer le logiciel de traitement d’image GIMP
- Importez l’image dans le logiciel
- Sous image, sélectionner Echelle et taille de l’image

![](/media/2023/06/word-image-5168-1-4.png)

- Choisissez une taille plus petite ou égale à la résolution de votre afficheur
- Sélectionne à nouveau le menu image, puis Mode et sélectionnez couleurs indexées

![](/media/2023/06/word-image-5168-2-2.png)

- Sélectionnez «utiliser la palette noir et blanc(1-bit)»
- Sous tramage des couleurs, sélectionnez aucun
- Terminez en appuyant sur «convertir»

![](/media/2023/06/word-image-5168-3-1.png)

- Terminez en exportant le dessin en format XBM
- Sous le menu Fichier, sélectionnez «Exportez sous …»
- Terminez en exportant le dessin en format XBM
- Attention le nom du fichier sera repris plus tard, alors choisissez un nom simple !

![](/media/2023/06/word-image-5168-4.png)

- Ouvrez un éditeur de texte et copiez son contenu
- Collez ce contenu dans le fichier main.cpp après la déclaration de l’afficheur

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /\* reset=\*/ U8X8_PIN_NONE, /\* clock=\*/ 22, /\* data=\*/ 21);

// importation du fichier \*.xbm\
\#define u8g2_logo_97x51_width 97

\#define u8g2_logo_97x51_height 51

static const unsigned char u8g2_logo_97x51_bits\[\] U8X8_PROGMEM = {

   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

   0x00, 0x3c, 0x80, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00,

   0x00, 0x00, 0x3c, 0x80, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfe,

…..

void loop()

{

  u8g2.firstPage();

  do

  {

    u8g2.drawXBMP(0,0, pouces_width, pouces_height, pouces_bits);  // affichez le bitmap à la coordonnée 0,0

  } while ( u8g2.nextPage() );

  delay(1000);

}

![](/media/2023/06/word-image-5168-5.png)

[Téléchargez cet exemple pour platformIO](/media/2023/06/ESP32ssd_logo.zip)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
