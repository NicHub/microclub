---
title: "Traitement des boutons"
date: "2020-06-14T21:15:36"
lastmod: "2020-06-15T19:21:32"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["arduino", "bounce", "c-2", "macro", "switch"]
url: "/2020/06/14/traitement-des-boutons/"
wordpress_id: 4773
comment_count: 2
---

Dans les entrés sorties, les boutons, switchs et autres commutateurs doivent être traités en entrée par logiciel. Il y a plusieurs besoins : traiter le sens de la lecture, des rebonds, et de la répétition. Et on peut y ajouter : le rafraichissement de la scrutation (scan) pour maintenir à jour l’état du bouton.

![word-image-3.jpeg](/media/2020/06/word-image-3.jpeg)

Dans cet article, on examine une proposition de définitions étagées, et la création d’un objet simple qui permet d’obtenir un code élégant et performant. Le code présenté est prévu pour Arduino ; mais transposable pour d’autres cibles.

## Le sens de lecture

Voici les deux schémas de connexion possible de bouton, avec une résistance de pull-up ou de pull down. Ici, avec des R de 10 KOhms.

![word-image-4.jpeg](/media/2020/06/word-image-4.jpeg)

Bien entendu, le point « output » va sur l’entrée (input) de votre CPU. Celui de gauche donne la tension d’alimentation lorsque le switch est pressé, alors que pour la même fonction, celui de droite donne un 0V. Dans ce second cas, s’il y a un 0 logique lu par le CPU, le code doit prendre en compte le bouton comme pressé. Ça complique un peu la réflexion. Alors pourquoi ce montage ? Son avantage est d’éviter de promener l’alimentation sur les fils qui vont aux boutons. On évite des courts-circuits en cas de mauvaises manipulation.

Le contrôle avec un multimètre est simple : on a soit V+ (donc 5V ou 3.3V selon le MCU utilisé) soit 0V. Sinon, chercher ce qui cloche… R coupée, pas d’alim. Ou plus vicieux : la connexion de GND à 0V n’est pas bonne. Quelle est la « bonne » valeur de R ? Plus elle est élevée, moins on consomme de courant ; mais plus la ligne entre le bouton et le CPU sera sensible aux parasites induits. Classiquement, 10K à 100K sont un bon choix.

## Rebond

Tout contact mécanique génère une commutation comportant des rebonds. Contacts dorés, argentés, lames au béryllium ou pas : les rebonds sont là. L’ordre de grandeur est de 2 à 40 millisecondes. L’auteur de <https://my.eng.utah.edu/~cs5780/debouncing.pdf>, Jack Ganssle a même trouvé un gros bouton ayant 157 ms de rebond ! La moyenne de son lot se situant dans 6,8 ms.

![word-image-1.png](/media/2020/06/word-image-1.png)

## Traitement software

Afin d’obtenir un bon soft de suivi de l’état des boutons, il s’agit de bien établir les différentes couches de définitions.

### Entrée hardware

L’exemple décrit ci-après comporte 4 boutons, pour régler une horloge sur Arduino Uno. Ce sont : \[Action\], \[+\], \[-\] et \[OK\]. Leurs entrées respectives selon le câblage sont définies dans un fichier .H ainsi :

```c++
#define SW_ACT 4 // Input hard definition
#define SW_PLUS 5
#define SW_MINUS 6
#define SW_OK 7
#define SW_NB 4 // nb of used switches
```

Si le câblage diffère, ou leur nombre change ce sont ces définitions qu’il s’agit d’ajuster.

### Tableau de boutons

Pour un traitement identique, nous allons créer des objets boutons, que nous groupons ensuite dans un tableau. Pour indexer chaque bouton par son nom symbolique dans le tableau, l’élément sera référencé :

```c++
#define B_ACT 0 // define button logical definition
#define B_PLUS 1
#define B_MINUS 2
#define B_OK 3
```

### Période de scrutation

C’est la période à laquelle on va lire les entrées pour définir ensuite l’état des boutons. Dans ce logiciel, on utilise une bibliothèque multitâche coopératif le jm-scheduler (). Bien entendu, c’est aussi possible par un appel régulier de la boucle principale loop(). La période est donc définie :

```c++
#define B_SCAN_PERIOD 20 // in millisecond
```

### Période de répétition

Un bouton pressé continuellement peut créer une répétition bienvenue. Par exemple, dans le cas du réglage d’une horloge, c’est plus simple de tenir le bouton \[+\] appuyé et de voir la valeur augmenter que de presser 50 fois pour obtenir le réglage des minutes ! A cet effet, on définit le rythme de répétition par la macro B_REP(n), avec n le nombre de répétition désiré par seconde :

```c++
// compute the repetition delay for a button continuously pressed
// ex. 4x/sec: 1000/(10*4) = 25 ; gives -> 250 ms
#define B_REP(n) (1000/((B_SCAN_PERIOD) * n))
```

C’est évidemment arrondi à l’entier : avec un scan rapide (10 ms expliqué dans le commentaire) on est plus précis. Si toutefois cela a de l’importance…

Voici encore une macro :

```c++
// compute a waiting time in sec. of a pressed button
#define B_WAIT(n_sec) ((n_sec)*(1000/(B_SCAN_PERIOD)))
```

La macro B_WAIT permet d’attendre de manière non-bloquante un nombre de secondes pour un bouton pressé (ou pas), avec la limite de 30000 scan effectués.

## La classe Sw

Cette classe comporte comme variables, toutes privées : un timer pour suivre l’état du bouton, l’état proprement dit, le nom du bouton, le n° de la pin d’entrée hardware du module. Si l’on est serré avec la taille mémoire vive, on peut abandonner le nom qui ne sert que pour des indications écrites en clair sur la sortie série.

```c++
class Sw
{
private:

volatile unsigned short timer; //0..30000 * 10 ms, 0..300 s
volatile bool state; //true: active; false: inact.
String name;
u8 pin;

public:

Sw(u8 pin_in, const String pin_name)
{
  pin = pin_in;

  pinMode(pin, INPUT_PULLUP); // useful: no external resistor needed
  digitalWrite(pin, HIGH); // ensure the level high trough pull-up
  timer = 0;
  state = false; // true: switch is On
  name = pin_name;
}
```

…

Le constructeur Sw**(**u8 pin_in**,** const String pin_name**)** reçoit le n° de pin à configurer en entrée. Sur Arduino, des pins sont paramétrables avec la résistance de pull-up interne, qui est activée : pas besoin de R extérieure, seul le bouton est à connecter contre 0V !

Comme le code est prévu pour de l’embarqué, il n’est pas nécessaire de prévoir un destructeur : le logiciel s’arrête à la coupure de courant.

### Scrutation du bouton

La fonction scan() doit être appelée régulièrement au rythme de la B_SCAN_PERIOD.

```c++
void scan()
{
if (timer<30000) timer++;
bool in = !digitalRead(pin); // get the reversed value

if (in != state) // Q: pin state changed?
{ // A: yes,
state = in; // Store value & reset counter
timer = 0;
}

}
```

Elle agit ainsi :

-   Incrémente le compteur (limité à max. 30000)
-   Lit l’état du bouton, actif ou non
-   Si l’état a changé :
    -   Met à jour l’état
    -   Remet à zéro le compteur

Et… c’est tout ! Ou presque. Une série de fonction inline, au nom évocateur, permettent ensuite le traitement des situations essentielles.

### Utilisation de la classe Sw

Un tableau sw\[ \] de type Sw permet d’y mettre les instances qui seront déclarées dans le code CPP. L’avantage de cette solution est que l’on parcourt les boutons par une boucle.

Le code suivant sera donc exécuté à l’initialisation, soit dans le setup() Arduino :

```c++
// init an array of button control
sw[0] = new Sw(SW_ACT, "ACT");
sw[1] = new Sw(SW_PLUS, "[+]");
sw[2] = new Sw(SW_MINUS, "[-]");
sw[3] = new Sw(SW_OK, "OK");
```

Un appel régulier de la fonction poll_loop-X-ms\>() dans cet exemple est généré par le jm_scheduler. Il va scanner les boutons, selon le choix de la période en millisecondes. Bien sûr, on peut lancer cet appel par la boucle loop() de Arduino, en la réglant avec la période désirée, avec un wait() ou en utilisant la progression du timer Arduino par exemple.

```c++
/* poll_loop_X_ms()
----------------
Compute the state of switches
Modified var: intern of object Sw.
The polling time must be between 10..50 ms
Return value: -
*/
void poll_loop_X_ms()
{
  // scan all switches
  for(short i=0; i<SW_NB; i++)
  {
    sw[i]->scan();
  }
menu_select();
}
```

Par la même occasion, cette boucle gère les menus, qui dépendent justement des boutons.

## Utilisation des fonctions inline

Si l’utilisation de la plupart des fonctions inline de la classe Sw est auto-explicative, certaines méritent une attention approfondie.

## Gestion des menus par les boutons

Les variables globales menu et smenu permettent la gestion respectivement des menus et des sous-menus affichés sur le display. Dans l’application complète, il y a 3 menus :

-   Relais
-   Commutations
-   Horloge

Le relais permet d’enclencher un dispositif par l’ Arduino; les commutations sont un point d’enclenchement qui activera le relais en fonction du temps ; pour finir, le menu horloge permet de régler la RTC du système.

### Remise à zéro du menu

Il est pratique pour l’utilisateur, lorsqu’on est perdu dans un sous-menu de pouvoir simplement revenir au début. Cela se fait par l’appui du bouton ACT et d’une pression sur OK :

```c++
if ( sw[B_ACT]->getPressed() && sw[B_OK]->getActivated() ) // Q: ACT and OK pressed?
{ menu = smenu = 0; } // A:yes, reset menu
```

### Reset des valeurs de l’EEPROM

Des tables d’enclechements du relais sont enregistrées en EEPROM. L’appel de la fonction de remise à zéro des valeurs enregistrées dans l’EEPROM ne doit pas être accidentelle. L’utilisateur doit presser ACT et OK simultanément pendant au moins 5 secondes.

```c++
if (menu == 0 && smenu == 0 && // Q: ACT and OK pressed ~ 5 seconds?
   sw[B_ACT]->getPressed() && sw[B_ACT]->getTm() > B_WAIT(5) &&
   sw[B_OK]->getPressed() && sw[B_OK]->getTm() > B_WAIT(5) )
{
  EEPROM.read(1); // bidon - compiler warning
  eepromInit(); // A: yes, EEPROM data cleared
  smenu = 1;
}
```

Le temps est contrôlé par lecture du timer du bouton, et il est testé avec la valeur calculée de la macro B_WAIT(5). Celle-ci rendra le nombre de scans correspondant à 5 secondes.

### Valeurs répétées

Dans le traitement des menus de l’horloge, il est souhaitable que les boutons \[+\] et \[-\] vont, maintenus pressés de manière continue, augmenter la valeur touchée de manière répétée. Ou bien la décrémenter pour le bouton \[-\], bien sûr. Lorsque le sous-menu est sur le réglage de l’année, on la gère par ces deux lignes :

```c++
if (sw[B_PLUS]->getRepeted()) yy++;
if (sw[B_MINUS]->getRepeted()) yy--;
```

La fonction de getRepeted() se présente ainsi :

```c++
inline bool getRepeted(){ if (state==true && timer%B_REP(4)==0) return true; return false; }
```

Lors de l’appui continu du bouton, le compteur s’incrémente à chaque période de scan. La macro B_REP(4) calcule le nombre de scan nécessaire pour une répétition de 4 fois pendant une seconde. Lorsque l’on tombe sur le modulo de cette valeur, la fonction renvoie « true ». La répétition fonctionne en pulsant des « true » à ce rythme.

## Montage d’essai

Le montage de test complet, sur une planche a cette allure :

![word-image-5.jpeg](/media/2020/06/word-image-5.jpeg)

1. Horloge RTC, câblée en I2C
2. Relais de commande
3. Affichage LCD, piloté en I2C

Cette planche servait pour mettre au point le soft du montage d’un projet de commande de ventilateur. Je l’ai conservée… pour régler des horloges RTC DS3231. En effet, il suffit de la connecter avec les 4 fils (I2C et l’alimentation), et par les boutons je peux la régler.

## Code source complet

Le code complet est disponible sur <https://github.com/ymasur/ventilo>

## Conclusion

Une définition objet d’une entrée de type switch permet un traitement efficace, et permet de produire un code simple et lisible. Ceci est essentiel pour la maintenance des programmes !

Yves Masur (6/2020)

## Commentaires

### franic — 16 juin 2020 à 20:19

Très bonne explication ! beau code.

Pour ma part je traite l’anti rebond des boutons ou de fin de courses par une fonction qui est appelée régulièrement dans la boucle principale. Cette fonction est composée d’une machine d’état et d’un timer. Il y a 4 états possibles :\
0 on attend un flanc descendant\
1 on attend que l’état bas soit stable, on ajuste un flag si c’est atteint et on passe à l’état 2, si l’état est à nouveau haut, on repasse à l’état 0\
2 on attend le flanc montant\
3 on attend que le signal soit stable haut et on repasse à l’état 0

Voici un exemple de code :

```c++
/** ****************************************************************************
* Function : TraiteToucheP
********************************************************************************
* Description : AntiRebond pour l’input PINx, masque MASK
********************************************************************************
* \param – : aucun
********************************************************************************
* \return Boutons, BTNP
*******************************************************************************/
void TraiteToucheP(void)
{
switch(EtToucheP)
{
/** ****************************************************************************
* Case 0 : attente du flanc descendant -\_
*******************************************************************************/
case 0 :
{
if ((digitalRead(BTNP)) == LOW)
{
TimoP = ANTIRTOUCHE;
EtToucheP = 1;
}
}; break; // case 0

/** ****************************************************************************
* Case 1 : attend signal stable bas
*******************************************************************************/
case 1 :
{
if ((digitalRead(BTNP)) == HIGH)
{
EtToucheP = 0;
}
else
{
if (TimoP == 0)
{
EtToucheP = 2;
Boutons |= FLAGBTNP; // Ok, bouton pressé
}
}
}; break; // case 1

/** ****************************************************************************
* Case 2 : Attend du flanc montant _/-
*******************************************************************************/
case 2 :
{
if ((digitalRead(BTNP)) == HIGH)
{
TimoP = ANTIRTOUCHE;
EtToucheP = 3;
}
}; break; // case 2

/** ****************************************************************************
* Case 3 : Attend signal stable haut
*******************************************************************************/
case 3 :
{
if ((digitalRead(BTNP)) == LOW)
{
EtToucheP = 2;
}
else
{
if (TimoP == 0)
{
EtToucheP = 0;
//Boutons &= ~(FLAGBTNP); // c’est le programme principal qui reset le bit ?
}
}
}; break; // case 3

} // switch(EtToucheP)
}
```

### Yves Masur — 16 juin 2020 à 20:45

Intéressant de comparer les deux approches. Faire le polling dans la boucle principale convient parfaitement. Si j’ai bien compris, c’est le schéma « pull-up » qui est utilisé, suivant le commentaire « attend signal stable bas » et le code, si c’est le cas: Boutons \|= FLAGBTNP; // Ok, bouton pressé

Les états des boutons sont compactés en bits: avec 2 bits pour tenir compte de la machine d’état. L’utilisation de mémoire est très faible. Juste pas facile de savoir où est la variable de machine d’état par bouton.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
