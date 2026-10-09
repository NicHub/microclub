---
title: "Thérémine à la sauce Arduino"
date: "2026-09-19T18:44:40"
lastmod: "2026-09-19T18:44:40"
author: "Jean-Pierre Broillet"
featureimage: "images/articles/theremine-arduino.svg"
categories: ["Microclub"]
tags: []
url: "/2026/09/19/theremine-a-la-sauce-arduino/"
wordpress_id: 5871
comment_count: 0
---
<p><strong>THÉRÉMINE ULTRASONIQUE</strong></p>
<p><strong>Arduino Uno + deux transducteurs HC-SR04</strong></p>
<p><strong>Jean-Pierre Broillet septembre 2026</strong></p>
<p><em>Étude, câblage, calibration et programme C++ documenté</em></p>
<p><strong>Projet expérimental d’un instrument électronique sans contact</strong></p>
<p><img height="218" src="/media/2026/09/word-image-5871-1.png" width="802"/></p>
<h1>1. Objet du projet</h1>
<p>Le but est de réaliser un thérémine numérique avec un Arduino Uno et deux capteurs ultrasonores HC-SR04. Un capteur mesure la position d’une main pour commander la hauteur du son (pitch), tandis que le second commande le volume. Contrairement au thérémine historique, qui exploite la variation de capacité créée par les mains à proximité d’antennes radiofréquences, cette réalisation mesure directement des distances.</p>
<p>C’est aussi un instrument difficile à maîtriser, car le musicien ne dispose d’aucun repère physique pour placer ses notes.</p>
<p>L’intérêt pédagogique est important : acquisition ultrasonore, filtrage numérique, conversion d’une grandeur physique en paramètre musical, temporisation, génération audio et amplification.</p>
<p>Une virtuose du thérémine :</p>
<p><a href="https://www.youtube.com/watch?v=lY7sXKGZl2w&amp;list=RDlY7sXKGZl2w&amp;start_radio=1">https://www.youtube.com/watch?v=lY7sXKGZl2w&amp;list=RDlY7sXKGZl2w&amp;start_radio=1</a></p>
<h1>2. Architecture générale</h1>
<p><img height="432" src="/media/2026/09/word-image-5871-2.png" width="722"/></p>
<p>Les deux capteurs doivent être suffisamment séparés et, si possible, orientés selon des axes différents. Cela diminue les risques qu’un HC-SR04 reçoive l’écho de l’impulsion émise par l’autre.</p>
<h1>3. Composants proposés</h1>
<ul>
<li>
    1 × Arduino Uno</li>
<li>
    2 × HC-SR04</li>
<li>
    1 × petit amplificateur audio (LM386 ou module équivalent recommandé)</li>
<li>
    1 × haut-parleur 8 Ω</li>
<li>
    1 × bouton-poussoir CALIBRATION (évolution recommandée)</li>
<li>
    1 × bouton-poussoir MUTE (évolution recommandée)</li>
<li>
    Résistances, condensateurs de découplage, plaque d’essai et alimentation 5 V adaptée</li>
</ul>
<h1>4. Affectation des broches</h1>
<table>
<tr>
<td>
  Fonction</td>
<td>
  Arduino Uno</td>
</tr>
<tr>
<td>
  TRIG HC-SR04 Pitch</td>
<td>
  D7</td>
</tr>
<tr>
<td>
  ECHO HC-SR04 Pitch</td>
<td>
  D8</td>
</tr>
<tr>
<td>
  TRIG HC-SR04 Volume</td>
<td>
  D9</td>
</tr>
<tr>
<td>
  ECHO HC-SR04 Volume</td>
<td>
  D10</td>
</tr>
<tr>
<td>
  Sortie audio</td>
<td>
  D3</td>
</tr>
<tr>
<td>
  Alimentation HC-SR04</td>
<td>
  +5 V</td>
</tr>
<tr>
<td>
  Masse</td>
<td>
  GND</td>
</tr>
</table>
<h1>5. Schéma électrique de base</h1>
<p><img height="724" src="/media/2026/09/word-image-5871-3.png" width="766"/></p>
<p>Important : ne pas brancher directement un haut-parleur de 8 Ω sur une sortie de l’Arduino. La broche ne peut pas fournir le courant nécessaire. Pour les premiers essais, un étage transistor peut suffire, mais un LM386 ou un petit amplificateur audio est préférable.</p>
<h1>6. Séquencement des mesures ultrasonores</h1>
<p>Les deux HC-SR04 ne doivent pas être déclenchés simultanément. Une mesure Pitch est effectuée, puis une temporisation est respectée avant la mesure Volume. Un capteur pourrait recevoir l’écho de l’impulsion émise par l’autre et donner une distance totalement fausse.</p>
<p>Une attente d’une trentaine de millisecondes constituent un bon point de départ pour le prototype.</p>
<h1><img height="232" src="/media/2026/09/word-image-5871-4.png" width="722"/></h1>
<h1>7. Conversion de la distance en hauteur musicale</h1>
<p>C’est ici que le projet devient intéressant.</p>
<p>Une conversion simplement linéaire, par exemple :</p>
<p><img height="24" src="/media/2026/09/word-image-5871-5.png" width="768"/></p>
<p>fonctionnerait, mais serait musicalement médiocre, parce que notre perception des hauteurs est logarithmique.</p>
<p>Il vaut mieux travailler par octaves :</p>
<p><img height="25" src="/media/2026/09/word-image-5871-6.png" width="768"/></p>
<p>avec</p>
<p><img height="74" src="/media/2026/09/word-image-5871-7.png" width="768"/></p>
<p>et N le nombre d’octaves.</p>
<p><img height="25" src="/media/2026/09/word-image-5871-8.png" width="768"/></p>
<p>et quatre octaves donnent :</p>
<p><img height="25" src="/media/2026/09/word-image-5871-9.png" width="768"/></p>
<p>C’est beaucoup plus naturel à jouer.</p>
<h1>8. Filtrage des HC-SR04</h1>
<p>Les mesures brutes peuvent varier de quelques millimètres à quelques centimètres, ce qui devient immédiatement audible sous forme de vibrato parasite.</p>
<p>Je propose donc un filtre exponentiel :</p>
<p><img height="30" src="/media/2026/09/word-image-5871-10.png" width="352"/></p>
<p>avec :</p>
<p><img height="26" src="/media/2026/09/word-image-5871-11.png" width="103"/></p>
<p>Une petite valeur donne un instrument très stable mais plus lent ; une grande valeur donne un instrument vif mais plus nerveux.</p>
<p>C’est donc un paramètre que je mettrais explicitement dans le programme.</p>
<h1>9. Commande du volume</h1>
<p>Pour le capteur Volume, la convention retenue est : main proche = silence, main éloignée = volume maximal. Dans la première version utilisant tone(), le niveau calculé sert surtout de seuil marche/arrêt. Une version évoluée utilisera une véritable modulation d’amplitude ou une sortie PWM filtrée.</p>
<h1>10. Programme C++ complet – version de test</h1>
<p>/*</p>
<p>================================================================</p>
<p>THEREMINE A ULTRASONS – Arduino UNO + 2 x HC-SR04</p>
<p>HC-SR04 n°1 : hauteur (PITCH)</p>
<p>HC-SR04 n°2 : volume</p>
<p>================================================================</p>
<p>*/</p>
<p>#include &lt;Arduino.h&gt;</p>
<p>#include &lt;math.h&gt;</p>
<p>const byte TRIG_PITCH  = 7;</p>
<p>const byte ECHO_PITCH  = 8;</p>
<p>const byte TRIG_VOLUME = 9;</p>
<p>const byte ECHO_VOLUME = 10;</p>
<p>const byte AUDIO_PIN   = 3;</p>
<p>const float DIST_MIN = 5.0;      // cm</p>
<p>const float DIST_MAX = 50.0;     // cm</p>
<p>const float FREQ_MIN = 110.0;    // Hz</p>
<p>const float NB_OCTAVES = 4.0;</p>
<p>const float ALPHA = 0.20;</p>
<p>float distancePitchFiltree  = 25.0;</p>
<p>float distanceVolumeFiltree = 25.0;</p>
<p>float mesurerDistance(byte trigPin, byte echoPin)</p>
<p>{</p>
<p>digitalWrite(trigPin, LOW);</p>
<p>delayMicroseconds(3);</p>
<p>digitalWrite(trigPin, HIGH);</p>
<p>delayMicroseconds(10);</p>
<p>digitalWrite(trigPin, LOW);</p>
<p>// Timeout afin d’éviter un blocage si aucun écho n’est reçu.</p>
<p>unsigned long duree = pulseIn(echoPin, HIGH, 30000UL);</p>
<p>if (duree == 0)</p>
<p>return -1.0;</p>
<p>// Vitesse du son ≈ 0,0343 cm/us ; division par 2 : aller-retour.</p>
<p>return duree * 0.0343 / 2.0;</p>
<p>}</p>
<p>float limiter(float valeur, float minimum, float maximum)</p>
<p>{</p>
<p>if (valeur &lt; minimum) valeur = minimum;</p>
<p>if (valeur &gt; maximum) valeur = maximum;</p>
<p>return valeur;</p>
<p>}</p>
<p>float distanceVersFrequence(float distance)</p>
<p>{</p>
<p>distance = limiter(distance, DIST_MIN, DIST_MAX);</p>
<p>// Main proche -&gt; x = 1 ; main éloignée -&gt; x = 0.</p>
<p>float x = (DIST_MAX – distance) / (DIST_MAX – DIST_MIN);</p>
<p>// Loi exponentielle correspondant à NB_OCTAVES octaves.</p>
<p>return FREQ_MIN * pow(2.0, NB_OCTAVES * x);</p>
<p>}</p>
<p>int distanceVersVolume(float distance)</p>
<p>{</p>
<p>distance = limiter(distance, DIST_MIN, DIST_MAX);</p>
<p>// Main proche -&gt; silence ; main éloignée -&gt; maximum.</p>
<p>float x = (distance – DIST_MIN) / (DIST_MAX – DIST_MIN);</p>
<p>return constrain((int)(255.0 * x), 0, 255);</p>
<p>}</p>
<p>void setup()</p>
<p>{</p>
<p>pinMode(TRIG_PITCH, OUTPUT);</p>
<p>pinMode(ECHO_PITCH, INPUT);</p>
<p>pinMode(TRIG_VOLUME, OUTPUT);</p>
<p>pinMode(ECHO_VOLUME, INPUT);</p>
<p>pinMode(AUDIO_PIN, OUTPUT);</p>
<p>Serial.begin(115200);</p>
<p>Serial.println(« Theremine ultrasonique – initialisation »);</p>
<p>}</p>
<p>void loop()</p>
<p>{</p>
<p>// Mesure du capteur de hauteur.</p>
<p>float dPitch = mesurerDistance(TRIG_PITCH, ECHO_PITCH);</p>
<p>if (dPitch &gt; 0)</p>
<p>distancePitchFiltree =</p>
<p>ALPHA * dPitch + (1.0 – ALPHA) * distancePitchFiltree;</p>
<p>// Séparation temporelle des émissions ultrasonores.</p>
<p>delay(30);</p>
<p>// Mesure du capteur de volume.</p>
<p>float dVolume = mesurerDistance(TRIG_VOLUME, ECHO_VOLUME);</p>
<p>if (dVolume &gt; 0)</p>
<p>distanceVolumeFiltree =</p>
<p>ALPHA * dVolume + (1.0 – ALPHA) * distanceVolumeFiltree;</p>
<p>float frequence = distanceVersFrequence(distancePitchFiltree);</p>
<p>int volume = distanceVersVolume(distanceVolumeFiltree);</p>
<p>// Première version : tone() produit une onde carrée.</p>
<p>// Le volume est ici utilisé comme seuil d’activation.</p>
<p>if (volume &gt; 10)</p>
<p>tone(AUDIO_PIN, (unsigned int)frequence);</p>
<p>else</p>
<p>noTone(AUDIO_PIN);</p>
<p>// Informations de mise au point sur le PC.</p>
<p>Serial.print(« Pitch : « );</p>
<p>Serial.print(distancePitchFiltree, 1);</p>
<p>Serial.print( » cm   F = « );</p>
<p>Serial.print(frequence, 1);</p>
<p>Serial.print( » Hz   Volume : « );</p>
<p>Serial.print(distanceVolumeFiltree, 1);</p>
<p>Serial.print( » cm   Niveau = « );</p>
<p>Serial.println(volume);</p>
<p>delay(10);</p>
<p>}</p>
<h1>11. Mais je modifierais ensuite la génération sonore</h1>
<p><strong>tone()</strong> est excellent pour vérifier le fonctionnement, mais pas pour obtenir un beau thérémine. Il produit essentiellement une onde carrée riche en harmoniques impaires.</p>
<p>Le projet devient beaucoup plus intéressant avec cette chaîne :</p>
<p><img height="512" src="/media/2026/09/word-image-5871-12.png" width="341"/></p>
<p>On pourrait générer une onde triangulaire ou une combinaison sinusoïde + harmoniques donnant un timbre beaucoup plus agréable.</p>
<h1>12. Le « calage » que je recommande</h1>
<p>C’est même un point que je considère essentiel.</p>
<p>Plutôt que d’imposer définitivement 5 et 50 cm dans le programme, le thérémine devrait posséder une procédure de calibration.</p>
<p>Au démarrage :</p>
<p><img height="492" src="/media/2026/09/word-image-5871-13.png" width="722"/></p>
<p>On peut ajouter <strong>deux boutons-poussoirs</strong>, ou mieux encore un bouton CALIBRATION et utiliser le moniteur série pour guider l’utilisateur.</p>
<p>Je verrais volontiers :</p>
<p><img height="252" src="/media/2026/09/word-image-5871-14.png" width="386"/></p>
<p>Le bouton <strong>MUTE</strong> serait particulièrement pratique : un thérémine sans moyen simple de couper le son devient vite pénible pendant les essais.</p>
<h1>13. Une amélioration très importante</h1>
<p>Il faudrait séparer <strong>mesure</strong>, <strong>traitement</strong> et <strong>production audio</strong>.</p>
<p>Dans le programme précédent, <strong>pulseIn()</strong> est bloquant. Cela suffit pour une démonstration, mais ce n’est pas idéal pour un véritable instrument.</p>
<p>La version évoluée pourrait fonctionner ainsi :</p>
<p><img height="352" src="/media/2026/09/word-image-5871-15.png" width="722"/></p>
<p>La génération sonore par <strong>Timer1 avec accumulateur de phase</strong> serait nettement supérieure : l’audio continuerait à être généré régulièrement pendant les calculs et les acquisitions.</p>
<h1>14. Architecture finale</h1>
<p><strong>Arduino Uno + 2 HC-SR04 + bouton CALIB + bouton MUTE + sortie audio PWM + filtre RC + LM386 + haut-parleur 8 Ω.</strong></p>
<p>Et surtout, je ferais évoluer le logiciel en trois étapes : d’abord la version <strong>tone()</strong> ci-dessus pour valider la géométrie et les capteurs ; ensuite une version avec <strong>vrai contrôle continu du volume</strong> ; enfin une version avec <strong>DDS/Timer</strong>, forme d’onde travaillée et calibration automatique.</p>
<p>Cette dernière version serait un véritable petit instrument numérique et non plus seulement une démonstration HC-SR04. Elle permettrait même d’ajouter ultérieurement <strong>vibrato, choix du timbre, changement du nombre d’octaves et quantification facultative sur les notes de la gamme</strong>.</p>
<p><strong>L’accumulateur de phase</strong></p>
<p>L’<strong>accumulateur de phase</strong> est une technique numérique très élégante pour fabriquer un signal périodique de fréquence précise. Dans notre thérémine, il permettrait de remplacer avantageusement <strong>tone().</strong></p>
<h3>Le principe</h3>
<p>Imaginez un tour complet de cercle correspondant à une période du signal :</p>
<p><img height="35" src="/media/2026/09/word-image-5871-16.png" width="314"/></p>
<p>À chaque « tic » d’une horloge très régulière, on avance d’une certaine quantité sur ce cercle. Cette position est la <strong>phase</strong>.</p>
<p>On utilise donc une variable entière :</p>
<p><img height="69" src="/media/2026/09/word-image-5871-17.png" width="216"/></p>
<p>C’est cette variable phase que l’on appelle <strong>accumulateur de phase</strong>.</p>
<p>Plus <strong>increment</strong> est grand, plus on fait rapidement le tour, donc plus la fréquence sonore est élevée.</p>
<h3>Exemple très simple</h3>
<h3>Supposons arbitrairement un accumulateur allant de 0 à 255.</h3>
<p>Avec un incrément de 1 :</p>
<p><img height="44" src="/media/2026/09/word-image-5871-18.png" width="766"/></p>
<p>Il faut <strong>256 coups d’horloge</strong> pour effectuer une période.</p>
<p>Avec un incrément de 4 :</p>
<p><img height="32" src="/media/2026/09/word-image-5871-19.png" width="722"/></p>
<p>Il ne faut plus que :</p>
<p><strong>256/4 = 64</strong></p>
<p>coups d’horloge pour une période.</p>
<p>La fréquence est donc quatre fois plus élevée.</p>
<h3>Relation mathématique</h3>
<p>Avec un accumulateur de phase de N bits possède :</p>
<p><strong>2<sup>N</sup></strong></p>
<p>états.</p>
<p>Si la fréquence d’échantillonnage est Fs et l’incrément de phase vaut K, la fréquence générée est :</p>
<p><img height="53" src="/media/2026/09/word-image-5871-20.png" width="118"/></p>
<p>Prenons par exemple un accumulateur <strong>32 bits</strong> et une interruption audio à :</p>
<p><strong>F<sub>S</sub> = 31250Hz</strong></p>
<p>Pour produire le La à 440 Hz :</p>
<p><strong>K = 440 x 2<sup>32</sup>/31250</strong></p>
<p>ce qui donne environ :</p>
<p><strong><img height="26" src="/media/2026/09/word-image-5871-21.png" width="140"/></strong></p>
<p>Cela paraît énorme, mais pour un microcontrôleur ce n’est qu’un entier 32 bits.</p>
<h3>Pour quelle raison, c’est mieux que tone() ?</h3>
<p><strong>tone()</strong> est pratique pour un prototype, mais l’accumulateur de phase permet de contrôler indépendamment <strong>fréquence, amplitude et forme d’onde</strong>. On peut ainsi produire une sinusoïde, un triangle, un signal enrichi en harmoniques, ajouter du vibrato et faire varier la fréquence de façon parfaitement continue.</p>
<p>Et il y a une propriété particulièrement intéressante pour le thérémine : lorsque la fréquence change, <strong>la phase continue</strong>. On ne redémarre pas la sinusoïde à zéro à chaque nouvelle mesure de la main. Les glissandos deviennent donc naturellement continus.</p>
<p>C’est précisément pour cette raison que je propose cette technique. Je suis d’avis que la prochaine étape intéressante est de construire une vraie version <strong>DDS + Timer</strong>, en expliquant en détail <strong>Timer1, fréquence d’échantillonnage, accumulateur 32 bits, table sinus et PWM</strong>, puis d’en tirer le programme C++ complet du thérémine.</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
