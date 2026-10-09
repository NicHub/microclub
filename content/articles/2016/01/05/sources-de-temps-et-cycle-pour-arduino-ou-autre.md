---
title: "Sources de temps et cycle pour Arduino (ou autre)"
date: "2016-01-05T22:21:21"
lastmod: "2016-02-02T20:07:42"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["arduino", "embarque", "micros", "millis", "programmation", "quartz", "rtc", "time"]
url: "/2016/01/05/sources-de-temps-et-cycle-pour-arduino-ou-autre/"
wordpress_id: 2162
comment_count: 2
---
Dans cet article, on va examiner les moyens d’obtenir une base de temps sur la plateforme Arduino (Diduino, Seeeduino Stalker et Arduino Yun). Bien sûr, c’est transposable sur d’autres systèmes, qui tous ont besoin de références de temps. Que ce soit la date/heure exacte pour horodater un événement, ou attendre une certaine durée, qu’elle soit courte ou longue. Parfois, un timer local doit être synchronisé sur une horloge de précision : il y a plusieurs techniques pour ce faire.

[![clock_cff](/media/2016/01/clock_cff.jpg)](/media/2016/01/clock_cff.jpg)

Pour illustrer la complexité du sujet, il faut savoir que même notre planète ralentit et demande d’ajouter une seconde intercalaire. Sauter dans le temps peut être mortel pour la cohérence de données injectées dans une base de données ! Pour y palier, Google a mis au point une technique pour la gérer (<http://www.clubic.com/internet/actualite-748601-google-rajoute-seconde-intercalaire-eviter-plantage.html> )

Un bon exemple de la complexité du maintien d’une référence de temps cohérente se trouve dans les contrôleurs de trafic. Ces machines doivent d’une part donner des durées précises aux enclenchements des sources lumineuses (rouge – jaune – vert), souvent basées sur une résolution de 20 ou 100 millisecondes ; d’autre part maintenir un journal d’événements et commuter de plan de feux. Les plans de feux d’un cycle de – par exemple – 90 secondes doivent être synchronisés entre carrefours d’un même axe à la seconde. La référence utilisée est le Tx. Pour le calculer, on part du nombre de secondes écoulées depuis une origine comme le 1\<sup\>er\</sup\> janvier de l’année en cours, dont on prend le modulo (dans ce cas : 90). Le programme doit donc pouvoir compter sur des sources de temps fiables, précises. Elles sont aussi cascadées, c’est-à-dire que si l’une ne répond pas, on se rabat sur la suivante. On a par exemple :

-   Le temps réseau LAN NTP
-   Un signal GPS
-   L’horloge radio DCF
-   La centrale de trafic (qui donne le temps par télégramme)
-   Le secteur 50 Hz (variations en cours de journée rattrapées)
-   L’horloge interne (mais susceptible de dériver)
-   Un timer du CPU (peu précis)

## Programmer un rythme : le tick

Une approche simple, qui consiste à écrire des routines dont l’exécution est rapide et de rythmer le cycle par une tempo ajustée. Ceci ne fonctionne que très approximativement. C’est pourtant ce qui est montré dans la plupart des exemples de programmation, comme faire clignoter une LED (<https://www.arduino.cc/en/Tutorial/Blink> ) à 0,5 Hz avec deux délais de 1000 ms entre les états allumé et éteint. Pour faire fonctionner un système en temps réel, il faut un « tick » d’horloge qui lance un appel régulier à des routines, qui dureront plus ou moins longtemps ; mais moins que la période de récurrence.

Une approche précise consiste à faire tourner un timer hardware, et d’attendre qu’il ait atteint ou dépassé une valeur pré calculée pour appeler les routines à rythmer. A ce moment, on peut soit agir par interruption, soit par polling. L’utilisation de l’interruption, si elle semble séduisante de prime abord, est plus complexe à mettre en œuvre et présente un danger : la réentrance. Soit l’apparition d’une nouvelle interruption, alors que les fonctions appelées n’ont pas terminé leur tâche. Si elle est masquée (l’interruption attend d’être servie), un tick sera raté sans qu’on s’en rend compte ; si elle ne l’est pas, le programme plante.

Voici un exemple de cycle de 100 millisecondes, basé sur la fonction native de Arduino, millis(). Elle donne le nombre de millisecondes écoulées depuis l’enclenchement. Ce compteur de 32 bits déborde (revient à 0) au bout de 2^32 / 1000 / 60 / 60 / 24 = 49.71 jours.

```c++
/* Main loop.
Run at 100 ms, commute the LED13 and call pulse_01Sec()
call reader() continously
*/
void loop()
{
  unsigned long currentMillis = millis(); // read time passed
  if (currentMillis - previousMillis &gt; cycleTime) //Q: cycle reached?
  {
    previousMillis = currentMillis; //A: yes, set next point
    pulse_01Sec();
    etat_LED13 = !etat_LED13;     // pulse LED13 at 0.1 sec
    digitalWrite(LED13, etat_LED13);
  }
  reader();
}//loop
```

*Désolé pour les commentaires. Selon mon inspiration, ils sont en anglais ou en français.*

La variable locale currentMillis contient la valeur actuelle du compteur. Sil elle a dépassé la borne définie par constante cycleTime (ici 100 ms), on mémorise sa valeur dans la variable globale ou statique previousMillis. On évite ainsi les petites variations entre appels de fonctions qui conduiraient inévitablement à des imprécisions : il n’y a pas de flottement.

## Quelle est la précision de cette technique ?

Au point de vue du rythme, c’est imparable, il n’y a pas d’écart. Si le temps pris par les fonctions appelées dépasse parfois 100 ms, les appels seront consécutifs jusqu’à ce que la synchronisation soit retrouvée. En observant le rythme de la LED, on peut ainsi se rendre compte qu’il y a un problème.

Mais sur la durée, quelle est la précision absolue de cette technique ? Afin de m’en rendre compte, j’ai ajouté à l’Arduino une horloge RTC, un programme qui permet sa mise à l’heure et de l’afficher. De plus, je l’ai doté d’une fonction qui affiche l’heure sur la ligne série théoriquement toute les minutes, soit tous les 600 appels par la fonction pulse_01Sec().

```c++
void dispTimeMinutes()
{
  static int td;
  td++;
  if (td == 600)
  {
    td = 0;
    dispTime();
  }
}
```

## Résultat : anormalement faux

Le board est un Diduino, la RTC une Grove RTC (v. ref en fin d’article ) dotée d’une puce horloge DS1307. Un enregistrement de 10 minutes montre que la précision n’est pas au rendez-vous.

```log
2015/12/31 THU 15:37:16
2015/12/31 THU 15:38:16
2015/12/31 THU 15:39:17
2015/12/31 THU 15:40:18
2015/12/31 THU 15:41:18
2015/12/31 THU 15:42:19
2015/12/31 THU 15:43:19
2015/12/31 THU 15:44:20
2015/12/31 THU 15:45:21
2015/12/31 THU 15:46:21
2015/12/31 THU 15:47:22
```

Soit une dérive de 6 secondes pour 10 minutes. Un essai avec le même programme chargé sur un Seeduino Stalker, dont le board comporte une RTC compatible (chip DS3231) montre une dérive de 10 secondes pour 10 minutes. On conçoit certes qu’une dérive est possible, mais 1/60 d’erreur entre deux quartz, dont la précision attendue ne devrait pas dépasser de quelques secondes par jour, ce n’est pas soutenable.

## Sources d’erreur

Une recherche sur l’Internet concernant l’utilisation de la fonction millis() m’indique que sa précision dépend :

-   Du quartz… ou du résonateur (bien moins précis !!)
-   De la fonction millis(), qui fait… 1024 microsecondes au lieu de 1000 us

On aura donc 2,4 % de retard à cause de cette définition. Pour en tenir compte dans ma « minute », je recalcule la constante : 600 / 1.024 = 585.9375 -\> 586

Résultat, sur le board Stalker : dérive de -5 secondes sur 10 minutes ; sur le Diduino -8 secondes sur 10 minutes. C’est mieux, mais loin d’une précision suisse. Très probablement, le « quartz » du CPU est en fait un résonateur, moins cher. Et bien moins précis.

Pour des durées relativement longues, il vaut mieux interroger une RTC. Contrairement au timer qui est lu directement en quelques instructions, la RTC est connectée par le biais d’un bus I2C. Elle est lue via un pilote software, ce qui est bien plus lent. Mais combien de temps cela prend-il ?[![Yun_et_RTC](/media/2016/01/Yun_et_RTC.jpg)](/media/2016/01/Yun_et_RTC.jpg)

## Interroger la RTC

La fonction micros(), qui retourne un nombre de microsecondes écoulées permet des mesures avec une résolution de 4 us. J’ajoute cette mesure dans mon code. Pour éviter le biais de l’appel à micros(), je l’affiche et le soustrait de l’appel à getTime(), qui se charge de lire la RTC.

```c++
case 'm':
{
  r_time t;
  long t1 = micros();
  long t2 = micros();
  long delta = t2-t1;
  Serial.print(delta);
  t1 = micros();
  getTime(&amp;t);
  t2 = micros();
  delta = t2-t1-delta;
  Serial.print(" Lecture RTC: ");
  Serial.print(delta);
  Serial.print(" us\n");
}
break;
```

Résultats (ici, sur le Stalker) :

```log
m
8 Lecture RTC: 1248 us
m
8 Lecture RTC: 1232 us
m
8 Lecture RTC: 1232 us
m
8 Lecture RTC: 1240 us
```

L’appel de micros() est insignifiant ; il prend 0 à 4 us, soit la résolution du timer (8 us sur Stalker).

Diduino : 1080 à 1100 us\
Stalker : 1232 à 1248 us\
Yun : 1080 à 1104 us

## Horloge sur le Yun

On peut certes y ajouter une horloge RTC comme présenté dans le test ci-dessus.

Le Yun est équipé d’un Linux, qui lui sait se servir du temps sur l’Internet par NTP (Network Time Protocole) et maintenir une horloge interne. Pour cela, il faut aller dans Lucy, le panneau d’administration ; onglet system : Enclencher le service client NTP, et indiquer des serveurs de temps.

[![Yun_NTP](/media/2016/01/Yun_NTP.jpg)](/media/2016/01/Yun_NTP.jpg)

On met la précision suisse en premier ! Il s’agit ensuite de demander, depuis la partie Arduino à Linux de nous donner le temps, à la résolution de 1 seconde. On utilise un tableau de char global, qui sera mis à jour avec le temps actuel et dont on interroge la valeur pour lancer des processus (forcément rythmés à une période de plus d’une seconde). L’exemple ci-dessous est issu d’un système qui enregistre des températures toute les 10 minutes.

```c++
// time given by Unix cmd                  1
//                                    01234567890123456
char dateTime[20]; // asci format, as 14/08/29 22:10:42
// char position for second
#define TIME_S 16
```

La fonction getTimeStamp( char \*p) qui met à jour le temps au format ASCII dans le tableau pointé par p, est appelée au rythme de la boucle principale :

```c++
/* getTimeStamp(char *p)
---------------------
This function fill a string with the time stamp
Vars used:
- *p pointer to the destination str
returned value:
- number of chr written
*/
int getTimeStamp(char *p)
{
int i = 0;
char c;
Process time;
// date is a command line utility to get the date and the time
// in different formats depending on the additional parameter
time.begin("date");
// parameters: for the complete date yy/mm/dd hh:mm:ss
time.addParameter("+%y/%m/%d\t%T");
time.run(); // run the command
// read the output of the command
while(time.available() &gt; 0)
{
  c = time.read();
  if (c != '\n')
  p[i] = c;
  i++;
}
p[i] = '\0'; // end of the collected string
return i;
}
```

Voici maintenant un prédicat simple pour déclencher une action toute les 10 minutes. Il teste que l’unité des minutes soit à 0, ainsi que la dizaine et l’unité des secondes.

```c++
/*
IsSyncTime000(char *s)
----------------------
Prédicat permettant une synchro toute les 10 minutes
s: String au format date comme: 06/10/14-23:02:21
avec l'alignement               01234567890123456
Retour: 1 si synchronisation effective, 0 sinon
*/
bool IsSyncTime000(char s[])
{
if (s[16] == '0' &amp;&amp; s[15] == '0' &amp;&amp; s[13] =='0')
  return true;
else
  return false;
}
```

Dans la boucle principale, nous avons la lecture du temps, un test de synchronisation et l’enregistrement :

```c++
void loop()
{
// maintain state while sync is active
static byte stored;
// get the time from the server:
getTimeStamp(dateTime);
// Toggle LED 3 a the second pulse
digitalWrite(LED3, (dateTime[TIME_S] &amp; 1) ? 1:0);
//store values only at second 00
if (IsSyncTime000(dateTime))//Q: sync windows reached?
{
  if (stored == false)   //Q: not already done?
  {
    storeTemp();         //A: yes, write on file
    stored = true;
  }
}
else //A: no, out of sync windows, reset flag
{
  stored = false;
}
… (autre process)
}//fin de loop()
```

Remarquez la méthode pour la LED de vie qui clignote selon que le digit des secondes, indexé par TIME_S, est paire ou impaire. Lorsque la fenêtre de synchronisation est présente, soit pendant une seconde toute les 10 minutes, l’enregistrement de températures est réalisé par storeTemp(). Des flags évitent qu’on enregistre plusieurs fois pendant la même seconde, car la boucle tourne à 5..10 fois par seconde.

## Résultats de la technique Yun avec NTP

L’enregistreur utilisant cette technique est fiable et précis… tant que l’Access Point (AP) WiFi est présent et que le Yun n’est pas redémarré. En effet, j’ai testé que, après une coupure du courant du Yun, il se reconnecte sans problème au bout d’une minute… pour autant que le WiFi de l’AP soit présent. Mais voilà, lorsqu’une coupure du réseau (c’est rare, mais…) le Yun démarre en 1 minute, alors que l’AP WiFi met facilement 2 minutes pour obtenir la connexion sur le NET.

Sans le WiFi, et donc sans une source de temps NTP, ça ne se passe pas bien. L’horloge Linux va se trouver au 09/09/2011 ; et le Linux va mettre l’Arduino en mode Access Point ! Pour éviter ceci, il Faut modifier le script de démarrage.

Pour cela, aller dans le Web Panel avancé, onglet Administration, Sytem, Startup. Au bas de la page se trouve la fenêtre qui permet l’édition. Commenter la ligne « Wifi-live-or-reset » par un ‘#’ :\<code\>\

## wifi-live-or-reset\

boot-complete-notify\</code\>

Et enregistrer la modification.

En plus de cette précaution, il faut certes prévoir dans le code Arduino d’initialisation de lancer une première lecture du temps Linux ; car ce dernier mets bien plus de temps que la partie Arduino à démarrer.

## Conclusion

Pour une utilisation de tick d’horloge en dessous de la seconde, l’utilisation précautionneuse de la fonction millis() convient parfaitement ; en se rappelant toutefois qu’elle dure 1024 us. Pour des durées plus longue, ou simplement pour maintenir une référence de date/temps complète, il faut disposer d’une RTC. L’idéal est d’avoir une connexion LAN, et de lire l’heure sur une source de temps NTP. Encore mieux, une RTC qui serait régulièrement mise à l’heure par du NTP, faisant office de « backup » en cas d’indisponibilité du réseau.

Yves Masur (1/2016)

**Références**:

Module « Grove RTC » : <http://www.seeedstudio.com/wiki/Grove_-_RTC>

Board « Seeduino Stalker» : <http://seeedstudio.com/wiki/Seeeduino_Stalker>

Seconde intercalaire : <https://fr.wikipedia.org/wiki/Seconde_intercalaire>

Utilisation de millis() et de micros() : <http://www.gammon.com.au/millis>

Forum : How accurate is millis()? <http://forum.arduino.cc/index.php?topic=294542.0>

## Commentaires

### ymasur — 8 janvier 2016 à 20:12

Le code source horloge est disponible ici: <http://yvesmasur.ch/files/out/Arduino/>\
Il y a deux zips: le projet cmd_RTC-160108a.zip à débaler ou sont vos projets; et le pilote avec les fichiers .h, à déposer dans: arduino/librairies/

### Michel Vonlanthen — 11 janvier 2016 à 12:53

Ce que je vais dire va rappeler Coluche à Certains (« dis à Zézette de me laisser les clefs du camion »…) mais je ne me souviens plus comment mettre un commentaire personnel sur ce site. C’est pour ça que je fais semblant de répondre au message d’Yves! Alors voilà:

Le site Bricobot.ch de Jean-Daniel Nicoud cessera de paraître le 31 janvier 2016. Profitez des quelques jours restants pour lui jeter un dernier coup d’oeil !

[http://www.bricobot.ch](http://www.bricobot.ch/)

Snif + RobotAmitiés\
Michel Vonlanthen

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
