---
title: "Superordinateurs de table"
date: "2009-03-13T09:32:33"
lastmod: "2015-04-24T23:20:20"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["consoles", "futur", "gpgpu", "gpu", "hardware", "nvidia", "processeurs", "programmation", "science"]
url: "/2009/03/13/superordinateurs-de-table/"
wordpress_id: 182
comment_count: 0
---
Depuis de nombreuses années, les [ordinateurs les plus puissants](http://top500.org/) sont formés de très nombreux processeurs calculant en parallèle. Le record actuel est tenu par le [“Roadrunner” d’IBM](http://www.silicon.fr/fr/news/2008/06/09/supercalculateur_roadrunner_d_ibm_est_bien_le_plus_rapide) qui comprend 6′948 Opteron bicœurs et 12′960 processeurs [PowerXCell 8i](http://www.onversity.net/cgi-bin/progactu/actu_aff.cgi?Eudo=bgteob&P=00001079) d’IBM, contenant chacun [8 unités de calcul en flux](http://fr.wikipedia.org/wiki/Cell_%28processeur%29#Un_c.C5.93ur_principal_et_huit_c.C5.93urs_sp.C3.A9cifiques) (”[Stream Processing](http://en.wikipedia.org/wiki/Stream_processing) Unit”, SPU).

“Roadrunner” peut effectuer 1 [petaflops](http://fr.wikipedia.org/wiki/Floating-point_operations_per_second), soit un million de milliards d’opérations arithmétiques par seconde et vaut des millions d’euros. Vous pouvez aujourd’hui assez facilement disposer dans votre PC du millième de cette puissance pour quelques centaines d’euros seulement.

En effet, les [processeurs graphiques](http://fr.wikipedia.org/wiki/Processeur_graphique) “GPU” récents sont formés de centaines d’[unités de calcul en flux](http://en.wikipedia.org/wiki/Graphics_processing_unit#Stream_Processing_and_General_Purpose_GPUs_.28GPGPU.29) assez semblables aux 8 SPU du Cell. Initialement dédiés à la génération d’images réalistes en 3D temps réel et limités au calcul en virgule fixe, les GPU sont devenus capables d’exécuter certains programmes en virgule flottante beaucoup plus rapidement que sur les processeurs classiques : c’est le calcul générique sur GPU  ([GPGPU](http://en.wikipedia.org/wiki/GPGPU)).

La [série 5000 d’ATI (racheté par AMD) et les nouvelles GTX 200 de nVidia](http://www.pcauthority.com.au/Review/119738,ati-radeon-hd-4000-vs-nvidia-geforce-gtx-200.aspx) offrent désormais une puissance de l’ordre du teraflops, soit 200x plus que [les plus puissants processeurs intel](http://www.intel.com/support/processors/sb/CS-023143.htm#1). D’ailleurs nVidia commercialise désormais ses derniers processeurs sur des [cartes “Tesla”](http://www.nvidia.com/object/tesla_computing_solutions.html) dédiées au calcul, et dépourvues de sortie video, un comble pour des processeurs graphiques !

[La suite sur mon blog…](http://drgoulu.com/2009/03/13/superordinateurs-de-table/)

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
