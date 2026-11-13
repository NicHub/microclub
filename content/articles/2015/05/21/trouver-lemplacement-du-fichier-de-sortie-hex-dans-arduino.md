---
title: "Trouver l’emplacement du fichier de sortie *.hex dans Arduino"
date: "2015-05-21T15:39:48"
lastmod: "2015-05-21T15:40:44"
author: "franic"
categories: ["Microclub"]
tags: ["ardui", "arduino", "hardware", "processeurs"]
url: "/2015/05/21/trouver-lemplacement-du-fichier-de-sortie-hex-dans-arduino/"
wordpress_id: 1929
comment_count: 0
---
J’ai développé un logiciel avec l’environnement Arduino.

Je désire mettre ce logiciel dans un hardware personnalisé donc pas sur une carte Arduino.

Comment trouver l’emplacement où se trouve le fichier hex compilé ?

Voici la marche à suivre :

1 Ouvrir l’environnement Arduino, sous l’onglet « fichier » sélectionner l’option « Préférences » :

[![Préférences](/media/2015/05/Préférences-257x300.png)](/media/2015/05/Préférences.png)

2 Cocher l’option « compilation » :

[![Coche](/media/2015/05/Coche-300x162.png)](/media/2015/05/Coche.png)

3 Compiler le logiciel. Dans la fenêtre de sortie, repérer le répertoire du fichier hex :

[![OUT](/media/2015/05/OUT-300x97.png)](/media/2015/05/OUT.png)

Ensuite, vous pouvez utiliser votre programmateur et transférer le logiciel dans votre carte personnalisée !

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
