---
title: "La Macro F"
date: "2025-03-20T18:45:12"
lastmod: "2025-03-20T19:33:46"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2025/03/20/la-macro-f/"
wordpress_id: 5467
comment_count: 1
---
<p>Gestion de la mémoire avec Arduino</p>
<p>Présentation de la macro F()</p>
<p>Si vous cherchez dans toute la page de référence Arduino, vous ne trouverez pas une seule mention de la macro F(). Ce qui est regrettable, car c’est l’une des fonctions les plus puissantes qui a été ajoutée avec la version 1.0 de l’IDE. Je continue à mélanger les termes « macro » et « fonction ». F() n’est pas vraiment une fonction, c’est une macro #define qui se trouve dans WString.h</p>
<pre><code>WString.h:#define F(string_literal) (reinterpret_cast&lt;const FlashStringHelper *&gt;(PSTR(string_literal)))</code></pre>
<p>Cette longue chaîne de code indique au compilateur de conserver une chaîne de caractères dans PROGMEM et de ne pas la laisser consommer de la RAM.</p>
<p>Utilisation de la macro F()</p>
<p>Voici un exemple d’utilisation de la macro F() avec Serial.print() ou Lcd.print(). </p>
<pre><code>Serial.println(F("Hello World")) ;
Lcd.print(F("W")) ;</code></pre>
<p>C’est tout ce qu’il y a à faire. Il suffit d’entourer votre chaîne de caractères (tableau de caractères const) avec F().</p>
<p>Pourquoi la macro F() est-elle nécessaire ?</p>
<p>Rappelez-vous que l’Arduino Uno (et ses cousins) sont basés sur l’ATmega328. Ce microcontrôleur n’offre que 2 048 octets de mémoire vive. 2k, c’est tout. Même le grand frère de l’Uno, le Mega2560, n’a que 8K de RAM.</p>
<p>Qu’en est-il de l’utilisation du mot-clé « const » ?</p>
<p>D’après #define vs const, le mot-clé const indique au compilateur qu’une variable est une constante et qu’elle ne peut pas changer. En fonction des optimisations utilisées, le compilateur avr-gcc évitera de mettre cette valeur en RAM puisqu’il sait qu’elle ne changera jamais. Mais cette technique ne fonctionne pas avec les chaînes de style C ou les tableaux. Comme les tableaux sont basés sur des pointeurs, le compilateur doit mettre le tableau en RAM pour que les pointeurs fonctionnent correctement. Cela signifie que toutes les chaînes de caractères doivent être placées en RAM avant de pouvoir être utilisées.</p>
<figure><img alt="" height="63" src="/media/2025/03/word-image-5467-1.jpeg" width="370"/></figure>
<p></p>
<p>Ce que fait la macro F()</p>
<p>La macro F() indique au compilateur de laisser ce tableau particulier dans PROGMEM. Lorsqu’il est temps d’y accéder, un octet des données est copié en RAM à la fois. Ce travail supplémentaire entraîne un léger surcoût en termes de performances. Cependant, l’impression de chaînes de caractères en série ou sur un écran LCD est un processus très lent, de sorte que quelques cycles d’horloge supplémentaires n’ont pas d’importance.</p>
<p>Les compromis à prendre en compte</p>
<p>#1 : Impossibilité de modifier les données</p>
<p>Le principal inconvénient de la macro F() est que vous ne pouvez pas l’utiliser pour des données que vous souhaitez modifier. Tout ce qui est stocké dans PROGMEM ne peut pas être modifié par le programme en cours d’exécution. En fait, vous ne le souhaiteriez jamais. Le seul code qui peut modifier PROGMEM est le code stocké dans la partition d’amorçage, qui est l’endroit où se trouve le chargeur d’amorçage.</p>
<p>#2 : Ne fonctionne que sur les chaînes de caractères</p>
<p>Un autre inconvénient est que cette macro ne fonctionne que pour les chaînes de caractères. Bien qu’il soit utile d’utiliser PROGMEM pour stocker des choses comme des motifs de bits pour les caractères, cette macro ne va pas aider à cela. Si c’est le genre de choses que vous essayez de stocker, vous devrez utiliser les instructions PROGMEM traditionnelles pour le faire. C’est pourquoi cette référence sur PROGMEM du site Arduino.cc est une excellente lecture.</p>
<p>#3 : Ne convient pas aux gros blocs de texte (comme le HTML)</p>
<p>Stocker des pages HTML est un autre exemple où vous voudrez probablement garder le gros du texte dans PROGMEM. A moins que ce HTML ne soit enveloppé dans Serial.print() ou Client.print(), vous ne pourrez pas utiliser la macro F().</p>
<p>#4 : Optimisation</p>
<p>Il n’y a pas d’optimisation de l’utilisation de la mémoire avec la macro F(). Si vous utilisez la même chaîne de caractères à plusieurs reprises dans votre code, chaque instance consommera un peu de PROGMEM. Si vous êtes à court de PROGMEM, vous pouvez envisager de ne pas utiliser la macro F().</p>
<p>Conclusion</p>
<p>N’attendez pas que votre code commence à agir bizarrement. Chaque fois que vous utilisez des chaînes de caractères dans une méthode print(), prenez l’habitude de les entourer d’une macro F(). De cette manière, vous n’aurez pas à vous soucier de gaspiller de la mémoire vive pour quelque chose qui ne peut pas être modifié de toute façon.</p>
<p>La lecture de données (par exemple une chaîne de caractères) à partir de la mémoire FLASH nécessite l’utilisation de certaines fonctions. L’AVR a une architecture Harvard. Le code et les données sont stockés séparément. L’instruction suivante sera compilée, mais n’imprimera pas la chaîne de caractères. La raison en est que la fonction membre print reçoit un argument de type char* qui est l’adresse de base de la chaîne de caractères stockée dans FLASH. Le problème est que le déréférencement d’un char* renvoie le char stocké dans l’espace de données (RAM) et non dans l’espace de code. La macro F() change le type de char* en FlashStringHelper*. Maintenant que l’argument est d’un type différent, on peut créer des fonctions qui acceptent ce type et appeler les fonctions correctes pour récupérer les données de l’espace de code. Les fonctions membres print et println de la classe Serial possèdent ces surcharges.</p>
<p>Deux exemples probants :</p>
<figure><img alt="" height="477" src="/media/2025/03/word-image-5467-2.jpeg" width="1220"/></figure>
<figure><img alt="" height="481" src="/media/2025/03/word-image-5467-3.jpeg" width="1219"/></figure>
<p></p>

## Commentaires

### franic — 22 mars 2025 à 10:17

<section class="comment-content comment">
<p>Super document ! Effectivement j’utilise très régulièrement cette façon de faire qui est très simple à mettre en oeuvre.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
