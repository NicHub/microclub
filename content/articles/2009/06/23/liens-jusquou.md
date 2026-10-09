---
title: "Liens –  jusqu'ou?"
date: "2009-06-23T21:06:39"
lastmod: "2015-04-24T23:21:13"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["consoles", "initiation", "systeme-dexploitation", "windows"]
url: "/2009/06/23/liens-jusquou/"
wordpress_id: 227
comment_count: 0
---
Or donc Vista et W7 supportent les liens sur les arborescences NTFS. Jusqu’ou? voici quelques expériences, faites sur un dique à 2 partitions: C: et D: qui ont Vista et W7 64 bits. Le système démarré obtient le C:, l’autre le D: et respectivement. Un seul répertoire \temp est suffisant; on peut le créer ainsi:

```
C:\&gt;mklink /J temp d:\temp
Jonction créée pour temp &lt;&lt;===&gt;&gt; d:\temp
```

Ainsi l’on voit c:\temp et D:\temp, mais le « vrai » est sur D:, est c’est transparent:

```
C:\temp&gt;dir
 Le volume dans le lecteur C s'appelle Vista
 Le numéro de série du volume est 4C45-D48C
 Répertoire de C:\temp
20.06.2009  11:02    &lt;REP&gt;          .
20.06.2009  11:02    &lt;REP&gt;          ..
11.06.2009  10:05           131'906 cmd-c.pdf
06.06.2009  06:25               403 driverinst.log
```

Pour la petite histoire, le disque C: avait déjà un lien sur c:\temp, nommé tmp. Ce dernier était un moment orphelin, vu que le répertoire cible « C:\temp » était détruit en vue de le remplacer par le lien sur son alter-ego de D:\temp. Et maintenant, si je liste C:\tmp, le contenu est automatiquement celui de D:\temp !

Qui dit mieux? Un programme, pour voir. La tricherie est assez monstrueuse: j’envisage de lancer non moins que Firefox de W7 (en 32 bits, donc dans le répertoire x86) par la session Vista. Un premier essai ne fonctianne pas, car des résidus sont restés dans « Programm Files » de Vista:

```
C:\Program Files&gt;mklink /J "Mozilla Firefox" "d:\Program Files (x86)\Mozilla Firefox"
Impossible de créer un fichier déjà existant.
```

La destruction du répertoire soigne le mal; et on reprend:

```
C:\Program Files&gt;mklink /J "Mozilla Firefox" "d:\Program Files (x86)\Mozilla Firefox"
Jonction créée pour Mozilla Firefox &lt;&lt;===&gt;&gt; d:\Program Files (x86)\Mozilla Firefox
```

Ensuite, je crée le raccourci sur l’EXE mappé dans le lien. Celui-ci possède le répertoire: « C:\Program Files\Mozilla Firefox\firefox.exe ». Il vise dont à travers le lien! Et ça fonctionne pile-poil.

En conclusion, on peut grâce aux liens arranger  des configurations sans ré-installer, installer à double ou copier les mêmes données. Prudence avec les backup…

Yves Masur

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
