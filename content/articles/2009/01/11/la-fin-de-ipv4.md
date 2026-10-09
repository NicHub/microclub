---
title: "La fin de IPV4 ?"
date: "2009-01-11T23:09:00"
lastmod: "2015-04-24T23:21:14"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["it", "web"]
url: "/2009/01/11/la-fin-de-ipv4/"
wordpress_id: 66
comment_count: 2
---
A quand la fin de IPV4, soit l’attribution de 4 milliards d’adresses internet? C’est pour bientôt. Un site en calcule la durée de vie probable, au vu de la demande continue de nouvelles connexions, ici <http://penrose.uk6x.com/>

Malheureusement l’adoption de IPV6, qui – contrairement à ce que son nom laisse croire – utilise 8 octets pour définir pas moins de 2 ^128 adresses traîne les pieds. Il y a moins de 1% de fournisseurs qui s’y mettent… Sans ce passage en IPV6, ce sera la catastrophe programmée. Des astuces comme le NAT (translation d’adresse) ou le tunnelling n’offrent qu’une échappatoire marginale.

## Commentaires

### François — 3 décembre 2009 à 20:58

Petite correction :\
avec 8 octets on n’obtient que 64 bit car 8 x 8 bits=64 bits.\
Une adresse IPv6 n’est pas formé de 8 octets mais de 8 mots, un mot c’est 16 bits.\
8×16=128 donc 2^128 possibilités d’adressage.\
FFEF:FABC:0015:0000:0000:0000:003A:0012\
ou après simplification\
FFEF:FABC:15::3A:12

### ymasur — 19 décembre 2009 à 20:57

Mais oui, c’est bien 8 mots de 16 bits!! Détails complets ici: <http://fr.wikipedia.org/wiki/IPv6>\
Quelle épouvantable erreur… Le rouge de la honte me monte au front. Merci de la correction!

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
