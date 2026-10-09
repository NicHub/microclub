---
title: "Agenda du Microclub sur Google et en RSS"
date: "2007-11-04T16:41:57"
lastmod: "2015-04-24T23:20:23"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["rss", "social"]
url: "/2007/11/04/agenda-du-microclub-sur-google-et-en-rss/"
wordpress_id: 8
comment_count: 0
---
[![](http://www.google.com/calendar/images/ext/gc_button1_fr.gif)](http://www.google.com/calendar/render?cid=56o3uvros1be2i545u94olbtgg%40group.calendar.google.com)

J’ai créé un Agenda public sur Google Calendar avec les prochaines séances du Microclub. Vous pouvez :

- le consulter à l’aide du bouton ci-contre
- éventuellement utiliser un système de synchronisation de calendriers (iCal) pour importer automatiquement les séances dans Outlook ou votre PIM
- me demander gentiment un accès pour pouvoir éditer le calendrier vous-mêmes 😉

Mais le but de la manip était initialement de créer en même temps [ce flux RSS](http://www.google.com/calendar/feeds/56o3uvros1be2i545u94olbtgg%40group.calendar.google.com/public/basic) pour permettre d’afficher les prochaines séances dans le menu latéral de ce blog. Malheureusement les flux RSS sont traditionnellement dans l’ordre chronologique inverse, ce qui faisait apparaitre la prochaine séance au bas de la liste…

J’ai donc utilisé le génial [yahoo.pipes](http://pipes.yahoo.com) qui permet de manipuler et combiner des flus RSS en ligne, en utilisant bêtement une fonction qui inverse l’ordre des éléments dans le flux pour obtenir [le flux par ordre chronologique](http://pipes.yahoo.com/pipes/pipe.run?_id=MPgk8_yK3BGqJZ5yyp1_DQ&_render=rss) affiché dans le menu latéral.

Avec ceci, il suffit de créer un événement dans le calendrier Google pour chaque séance, et la liste sera automatiquement mise à jour sur le blog, et tous vos agendas automatiquement synchronisés.

Le web, c’est cool 🙂

[\
](http://www.google.com/calendar/render?cid=56o3uvros1be2i545u94olbtgg%40group.calendar.google.com)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
