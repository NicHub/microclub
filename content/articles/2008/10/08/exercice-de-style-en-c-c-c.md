---
title: "Exercice de style en C, C++, C#"
date: "2008-10-08T19:25:43"
lastmod: "2015-04-24T23:21:14"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["programmation"]
url: "/2008/10/08/exercice-de-style-en-c-c-c/"
wordpress_id: 87
comment_count: 1
---
Au départ, un petit exercice pour mes apprentits informaticiens, j’ai porté ce code sous 3 langages de programmation proches: C, C++, C#. C’est la conversion binaire -\> Hexa.

L’environnement est Windows Visual C++ Express (gratuit) et C# (aussi gratuit).

D’abord prévu en ligne de commande, il est finalement construit dans une version en fenêtre en C#. Finalement, les résultats sont passés en revue.\
Article complet: <http://yves.masur.microclub.ch/articles/CPP/quatre_codages-C-CPP-CS.doc>\
Code source (zippés): <http://yves.masur.microclub.ch/files/out/VStudio2008>/

## Commentaires

### Yves Masur — 2 octobre 2009 à 20:20

Dans un projet PIC, je me demandais comment était réalisée la fonction C Nop(), vue dans un bout de code pour écrire l’EEPROM. Une boucle vide? une assertion futile?\
Pas compliqué: dans le fichier compiler.h, on y voit

\#define Nop() asm(« NOP »);

Plus simple, tu meurs!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
