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
<div><div>
<p>Dans les entrés sorties, les boutons, switchs et autres commutateurs doivent être traités en entrée par logiciel. Il y a plusieurs besoins : traiter le sens de la lecture, des rebonds, et de la répétition. Et on peut y ajouter : le rafraichissement de la scrutation (scan) pour maintenir à jour l’état du bouton.</p>
<p><img height="393" src="/media/2020/06/word-image-3.jpeg" width="518"/></p>
<p>Dans cet article, on examine une proposition de définitions étagées, et la création d’un objet simple qui permet d’obtenir un code élégant et performant. Le code présenté est prévu pour Arduino ; mais transposable pour d’autres cibles.</p>
<h1>Le sens de lecture</h1>
<p>Voici les deux schémas de connexion possible de bouton, avec une résistance de pull-up ou de pull down. Ici, avec des R de 10 KOhms.</p>
<p><img height="196" src="/media/2020/06/word-image-4.jpeg" width="257"/></p>
<p>Bien entendu, le point « output » va sur l’entrée (input) de votre CPU. Celui de gauche donne la tension d’alimentation lorsque le switch est pressé, alors que pour la même fonction, celui de droite donne un 0V. Dans ce second cas, s’il y a un 0 logique lu par le CPU, le code doit prendre en compte le bouton comme pressé. Ça complique un peu la réflexion. Alors pourquoi ce montage ? Son avantage est d’éviter de promener l’alimentation sur les fils qui vont aux boutons. On évite des courts-circuits en cas de mauvaises manipulation.</p>
<p>Le contrôle avec un multimètre est simple : on a soit V+ (donc 5V ou 3.3V selon le MCU utilisé) soit 0V. Sinon, chercher ce qui cloche… R coupée, pas d’alim. Ou plus vicieux : la connexion de GND à 0V n’est pas bonne. Quelle est la « bonne » valeur de R ? Plus elle est élevée, moins on consomme de courant ; mais plus la ligne entre le bouton et le CPU sera sensible aux parasites induits. Classiquement, 10K à 100K sont un bon choix.</p>
<h1>Rebond</h1>
<p>Tout contact mécanique génère une commutation comportant des rebonds. Contacts dorés, argentés, lames au béryllium ou pas : les rebonds sont là. L’ordre de grandeur est de 2 à 40 millisecondes. L’auteur de <a href="https://my.eng.utah.edu/~cs5780/debouncing.pdf">https://my.eng.utah.edu/~cs5780/debouncing.pdf</a>, Jack Ganssle a même trouvé un gros bouton ayant 157 ms de rebond ! La moyenne de son lot se situant dans 6,8 ms.</p>
<p><img height="280" src="/media/2020/06/word-image-1.png" width="512"/></p>
<h1>Traitement software</h1>
<p>Afin d’obtenir un bon soft de suivi de l’état des boutons, il s’agit de bien établir les différentes couches de définitions.</p>
<h2>Entrée hardware</h2>
<p>L’exemple décrit ci-après comporte 4 boutons, pour régler une horloge sur Arduino Uno. Ce sont : [Action], [+], [-] et [OK]. Leurs entrées respectives selon le câblage sont définies dans un fichier .H ainsi :</p>
<pre>#define SW_ACT 4 // Input hard definition<br/>#define SW_PLUS 5<br/>#define SW_MINUS 6<br/>#define SW_OK 7<br/>#define SW_NB 4 // nb of used switches</pre>
<p>Si le câblage diffère, ou leur nombre change ce sont ces définitions qu’il s’agit d’ajuster.</p>
<h2>Tableau de boutons</h2>
<p>Pour un traitement identique, nous allons créer des objets boutons, que nous groupons ensuite dans un tableau. Pour indexer chaque bouton par son nom symbolique dans le tableau, l’élément sera référencé :</p>
<pre>#define B_ACT 0 // define button logical definition<br/>#define B_PLUS 1<br/>#define B_MINUS 2<br/>#define B_OK 3</pre>
<h2>Période de scrutation</h2>
<p>C’est la période à laquelle on va lire les entrées pour définir ensuite l’état des boutons. Dans ce logiciel, on utilise une bibliothèque multitâche coopératif le jm-scheduler (). Bien entendu, c’est aussi possible par un appel régulier de la boucle principale loop(). La période est donc définie :</p>
<pre>#define B_SCAN_PERIOD 20 // in millisecond</pre>
<h2>Période de répétition</h2>
<p>Un bouton pressé continuellement peut créer une répétition bienvenue. Par exemple, dans le cas du réglage d’une horloge, c’est plus simple de tenir le bouton [+] appuyé et de voir la valeur augmenter que de presser 50 fois pour obtenir le réglage des minutes ! A cet effet, on définit le rythme de répétition par la macro B_REP(n), avec n le nombre de répétition désiré par seconde :</p>
<pre>// compute the repetition delay for a button continuously pressed<br/>// ex. 4x/sec: 1000/(10*4) = 25 ; gives -&gt; 250 ms<br/>#define B_REP(n) (1000/((B_SCAN_PERIOD) * n))</pre>
<p>C’est évidemment arrondi à l’entier : avec un scan rapide (10 ms expliqué dans le commentaire) on est plus précis. Si toutefois cela a de l’importance…</p>
<p>Voici encore une macro :</p>
<pre>// compute a waiting time in sec. of a pressed button<br/>#define B_WAIT(n_sec) ((n_sec)*(1000/(B_SCAN_PERIOD)))</pre>
<p>La macro B_WAIT permet d’attendre de manière non-bloquante un nombre de secondes pour un bouton pressé (ou pas), avec la limite de 30000 scan effectués.</p>
<h1>La classe Sw</h1>
<p>Cette classe comporte comme variables, toutes privées : un timer pour suivre l’état du bouton, l’état proprement dit, le nom du bouton, le n° de la pin d’entrée hardware du module. Si l’on est serré avec la taille mémoire vive, on peut abandonner le nom qui ne sert que pour des indications écrites en clair sur la sortie série.</p>
<pre>class Sw<br/><strong>{</strong><br/>private<strong>:<br/></strong><br/>volatile unsigned short timer<strong>;</strong> //0..30000 * 10 ms, 0..300 s<br/>volatile bool state<strong>;</strong> //true: active; false: inact.<br/>String name<strong>;</strong><br/>u8 pin<strong>;</strong><br/><br/>public<strong>:<br/></strong><br/>Sw<strong>(</strong>u8 pin_in<strong>,</strong> const String pin_name<strong>)</strong><br/><strong>{</strong><br/>  pin <strong>=</strong> pin_in<strong>;<br/></strong><br/>  pinMode<strong>(</strong>pin<strong>,</strong> INPUT_PULLUP<strong>);</strong> // useful: no external resistor needed<br/>  digitalWrite<strong>(</strong>pin<strong>,</strong> HIGH<strong>);</strong> // ensure the level high trough pull-up<br/>  timer <strong>=</strong> 0<strong>;</strong><br/>  state <strong>=</strong> <strong>false;</strong> // true: switch is On<br/>  name <strong>=</strong> pin_name<strong>;</strong><br/><strong>}</strong></pre>
<p><strong>…</strong></p>
<p>Le constructeur Sw<strong>(</strong>u8 pin_in<strong>,</strong> const String pin_name<strong>) </strong>reçoit le n° de pin à configurer en entrée. Sur Arduino, des pins sont paramétrables avec la résistance de pull-up interne, qui est activée : pas besoin de R extérieure, seul le bouton est à connecter contre 0V !</p>
<p>Comme le code est prévu pour de l’embarqué, il n’est pas nécessaire de prévoir un destructeur : le logiciel s’arrête à la coupure de courant.</p>
<h2>Scrutation du bouton</h2>
<p>La fonction scan() doit être appelée régulièrement au rythme de la B_SCAN_PERIOD.</p>
<pre>void scan<strong>()</strong><br/><strong>{</strong><br/><strong>if</strong> <strong>(</strong>timer<strong>&lt;</strong>30000<strong>)</strong> timer<strong>++;</strong><br/>bool in <strong>=</strong> <strong>!</strong>digitalRead<strong>(</strong>pin<strong>);</strong> // get the reversed value<br/><br/><strong>if</strong> <strong>(</strong>in <strong>!=</strong> state<strong>)</strong> // Q: pin state changed?<br/><strong>{</strong> // A: yes,<br/>state <strong>=</strong> in<strong>;</strong> // Store value &amp; reset counter<br/>timer <strong>=</strong> 0<strong>;</strong><br/><strong>}</strong><br/><br/><strong>}</strong></pre>
<p>Elle agit ainsi :</p>
<ul>
<li>Incrémente le compteur (limité à max. 30000)</li>
<li>Lit l’état du bouton, actif ou non</li>
<li>Si l’état a changé :
<ul>
<li>Met à jour l’état</li>
<li>Remet à zéro le compteur</li>
</ul>
</li>
</ul>
<p>Et… c’est tout ! Ou presque. Une série de fonction inline, au nom évocateur, permettent ensuite le traitement des situations essentielles.</p>
<h2>Utilisation de la classe Sw</h2>
<p>Un tableau sw[ ] de type Sw permet d’y mettre les instances qui seront déclarées dans le code CPP. L’avantage de cette solution est que l’on parcourt les boutons par une boucle.</p>
<p>Le code suivant sera donc exécuté à l’initialisation, soit dans le setup() Arduino :</p>
<pre>// init an array of button control<br/>sw<strong>[</strong>0<strong>]</strong> <strong>=</strong> <strong>new</strong> Sw<strong>(</strong>SW_ACT<strong>,</strong> "ACT"<strong>);</strong><br/>sw<strong>[</strong>1<strong>]</strong> <strong>=</strong> <strong>new</strong> Sw<strong>(</strong>SW_PLUS<strong>,</strong> "[+]"<strong>);</strong><br/>sw<strong>[</strong>2<strong>]</strong> <strong>=</strong> <strong>new</strong> Sw<strong>(</strong>SW_MINUS<strong>,</strong> "[-]"<strong>);</strong><br/>sw<strong>[</strong>3<strong>]</strong> <strong>=</strong> <strong>new</strong> Sw<strong>(</strong>SW_OK<strong>,</strong> "OK"<strong>);</strong></pre>
<p>Un appel régulier de la fonction poll_loop-X-ms&gt;() dans cet exemple est généré par le jm_scheduler. Il va scanner les boutons, selon le choix de la période en millisecondes. Bien sûr, on peut lancer cet appel par la boucle loop() de Arduino, en la réglant avec la période désirée, avec un wait() ou en utilisant la progression du timer Arduino par exemple.</p>
<pre>/* poll_loop_X_ms()<br/>----------------<br/>Compute the state of switches<br/>Modified var: intern of object Sw.<br/>The polling time must be between 10..50 ms<br/>Return value: -<br/>*/<br/>void poll_loop_X_ms<strong>()</strong><br/><strong>{</strong><br/>  // scan all switches<br/><strong>  for(</strong>short i<strong>=</strong>0<strong>;</strong> i<strong>&lt;</strong>SW_NB<strong>;</strong> i<strong>++)</strong><br/><strong>  {</strong><br/>    sw<strong>[</strong>i<strong>]-&gt;</strong>scan<strong>();</strong><br/><strong>  }</strong><br/>menu_select<strong>();</strong><br/><strong>}</strong></pre>
<p>Par la même occasion, cette boucle gère les menus, qui dépendent justement des boutons.</p>
<h1>Utilisation des fonctions inline</h1>
<p>Si l’utilisation de la plupart des fonctions inline de la classe Sw est auto-explicative, certaines méritent une attention approfondie.</p>
<h1>Gestion des menus par les boutons</h1>
<p>Les variables globales menu et smenu permettent la gestion respectivement des menus et des sous-menus affichés sur le display. Dans l’application complète, il y a 3 menus :</p>
<ul>
<li>Relais</li>
<li>Commutations</li>
<li>Horloge</li>
</ul>
<p>Le relais permet d’enclencher un dispositif par l’ Arduino; les commutations sont un point d’enclenchement qui activera le relais en fonction du temps ; pour finir, le menu horloge permet de régler la RTC du système.</p>
<h2>Remise à zéro du menu</h2>
<p>Il est pratique pour l’utilisateur, lorsqu’on est perdu dans un sous-menu de pouvoir simplement revenir au début. Cela se fait par l’appui du bouton ACT et d’une pression sur OK :</p>
<pre><strong>if</strong> <strong>(</strong> sw<strong>[</strong>B_ACT<strong>]-&gt;</strong>getPressed<strong>()</strong> <strong>&amp;&amp;</strong> sw<strong>[</strong>B_OK<strong>]-&gt;</strong>getActivated<strong>()</strong> <strong>)</strong> // Q: ACT and OK pressed?<br/><strong>{</strong> menu <strong>=</strong> smenu <strong>=</strong> 0<strong>;</strong> <strong>}</strong> // A:yes, reset menu</pre>
<h2>Reset des valeurs de l’EEPROM</h2>
<p>Des tables d’enclechements du relais sont enregistrées en EEPROM. L’appel de la fonction de remise à zéro des valeurs enregistrées dans l’EEPROM ne doit pas être accidentelle. L’utilisateur doit presser ACT et OK simultanément pendant au moins 5 secondes.</p>
<pre><strong>if</strong> <strong>(</strong>menu <strong>==</strong> 0 <strong>&amp;&amp;</strong> smenu <strong>==</strong> 0 <strong>&amp;&amp;</strong> // Q: ACT and OK pressed ~ 5 seconds?<br/>   sw<strong>[</strong>B_ACT<strong>]-&gt;</strong>getPressed<strong>()</strong> <strong>&amp;&amp;</strong> sw<strong>[</strong>B_ACT<strong>]-&gt;</strong>getTm<strong>()</strong> <strong>&gt;</strong> B_WAIT<strong>(</strong>5<strong>)</strong> <strong>&amp;&amp;</strong><br/>   sw<strong>[</strong>B_OK<strong>]-&gt;</strong>getPressed<strong>()</strong> <strong>&amp;&amp;</strong> sw<strong>[</strong>B_OK<strong>]-&gt;</strong>getTm<strong>()</strong> <strong>&gt;</strong> B_WAIT<strong>(</strong>5<strong>)</strong> <strong>)<br/>{ <br/>  EEPROM.read(1); // bidon - compiler warning<br/>  eepromInit(); // A: yes, EEPROM data cleared<br/>  smenu = 1; <br/>} <br/></strong></pre>
<p>Le temps est contrôlé par lecture du timer du bouton, et il est testé avec la valeur calculée de la macro B_WAIT(5). Celle-ci rendra le nombre de scans correspondant à 5 secondes.</p>
<h2>Valeurs répétées</h2>
<p>Dans le traitement des menus de l’horloge, il est souhaitable que les boutons [+] et [-] vont, maintenus pressés de manière continue, augmenter la valeur touchée de manière répétée. Ou bien la décrémenter pour le bouton [-], bien sûr. Lorsque le sous-menu est sur le réglage de l’année, on la gère par ces deux lignes :</p>
<pre><strong>if</strong> <strong>(</strong>sw<strong>[</strong>B_PLUS<strong>]-&gt;</strong>getRepeted<strong>())</strong> yy<strong>++;</strong><br/><strong>if</strong> <strong>(</strong>sw<strong>[</strong>B_MINUS<strong>]-&gt;</strong>getRepeted<strong>())</strong> yy<strong>--;</strong></pre>
<p>La fonction de getRepeted() se présente ainsi :</p>
<pre><br/>inline bool getRepeted<strong>(){</strong> <strong>if</strong> <strong>(</strong>state<strong>==true</strong> <strong>&amp;&amp;</strong> timer<strong>%</strong>B_REP<strong>(</strong>4<strong>)==</strong>0<strong>)</strong> <strong>return</strong> <strong>true;</strong> <strong>return</strong> <strong>false;</strong> <strong>}</strong></pre>
<p>Lors de l’appui continu du bouton, le compteur s’incrémente à chaque période de scan. La macro B_REP(4) calcule le nombre de scan nécessaire pour une répétition de 4 fois pendant une seconde. Lorsque l’on tombe sur le modulo de cette valeur, la fonction renvoie « true ». La répétition fonctionne en pulsant des « true » à ce rythme.</p>
<h1>Montage d’essai</h1>
<p>Le montage de test complet, sur une planche a cette allure :</p>
<p><img height="604" src="/media/2020/06/word-image-5.jpeg" width="640"/></p>
<ol>
<li>Horloge RTC, câblée en I2C</li>
<li>Relais de commande</li>
<li>Affichage LCD, piloté en I2C</li>
</ol>
<p>Cette planche servait pour mettre au point le soft du montage d’un projet de commande de ventilateur. Je l’ai conservée… pour régler des horloges RTC DS3231. En effet, il suffit de la connecter avec les 4 fils (I2C et l’alimentation), et par les boutons je peux la régler.</p>
<h1>Code source complet</h1>
<p>Le code complet est disponible sur <a href="https://github.com/ymasur/ventilo">https://github.com/ymasur/ventilo</a></p>
<h1>Conclusion</h1>
<p>Une définition objet d’une entrée de type switch permet un traitement efficace, et permet de produire un code simple et lisible. Ceci est essentiel pour la maintenance des programmes !</p>
<p>Yves Masur (6/2020)</p>
</div></div>

## Commentaires

### franic — 16 juin 2020 à 20:19

<section class="comment-content comment">
<p>Très bonne explication ! beau code.</p>
<p>Pour ma part je traite l’anti rebond des boutons ou de fin de courses par une fonction qui est appelée régulièrement dans la boucle principale. Cette fonction est composée d’une machine d’état et d’un timer. Il y a 4 états possibles :<br/>
0 on attend un flanc descendant<br/>
1 on attend que l’état bas soit stable, on ajuste un flag si c’est atteint et on passe à l’état 2, si l’état est à nouveau haut, on repasse à l’état 0<br/>
2 on attend le flanc montant<br/>
3 on attend que le signal soit stable haut et on repasse à l’état 0</p>
<p>Voici un exemple de code :<br/>
/** ****************************************************************************<br/>
* Function    : TraiteToucheP<br/>
********************************************************************************<br/>
* Description : AntiRebond pour l’input PINx, masque MASK<br/>
********************************************************************************<br/>
* \param      – : aucun<br/>
********************************************************************************<br/>
* \return     Boutons, BTNP<br/>
*******************************************************************************/<br/>
void TraiteToucheP(void)<br/>
{<br/>
	switch(EtToucheP)<br/>
	{<br/>
	  /** ****************************************************************************<br/>
	  * Case 0 :  attente du flanc descendant -\_<br/>
	  *******************************************************************************/<br/>
		case 0 :<br/>
		{<br/>
			if ((digitalRead(BTNP)) == LOW)<br/>
			{<br/>
			 TimoP = ANTIRTOUCHE;<br/>
			 EtToucheP = 1;<br/>
			}<br/>
		}; break;       // case 0</p>
<p>	  /** ****************************************************************************<br/>
	  * Case 1 : attend signal stable bas<br/>
	  *******************************************************************************/<br/>
		case 1 :<br/>
		{<br/>
			if ((digitalRead(BTNP)) == HIGH)<br/>
			{<br/>
				EtToucheP = 0;<br/>
			}<br/>
			else<br/>
			{<br/>
				if (TimoP == 0)<br/>
				{<br/>
					EtToucheP = 2;<br/>
					Boutons |= FLAGBTNP;            // Ok, bouton pressé<br/>
				}<br/>
			}<br/>
		}; break;       // case 1</p>
<p>	  /** ****************************************************************************<br/>
	  * Case 2 : Attend du flanc montant _/-<br/>
	  *******************************************************************************/<br/>
	  case 2 :<br/>
	  {<br/>
			if ((digitalRead(BTNP)) == HIGH)<br/>
			{<br/>
				TimoP = ANTIRTOUCHE;<br/>
				EtToucheP = 3;<br/>
			}<br/>
	  }; break;       // case 2</p>
<p>	  /** ****************************************************************************<br/>
	  * Case 3 : Attend signal stable haut<br/>
	  *******************************************************************************/<br/>
	  case 3 :<br/>
	  {<br/>
			if ((digitalRead(BTNP)) == LOW)<br/>
			{<br/>
				EtToucheP = 2;<br/>
			}<br/>
			else<br/>
			{<br/>
				if (TimoP == 0)<br/>
				{<br/>
					EtToucheP = 0;<br/>
					//Boutons &amp;= ~(FLAGBTNP);          // c’est le programme principal qui reset le bit	?<br/>
				}<br/>
			}<br/>
	  }; break;       // case 3</p>
<p>	}        // switch(EtToucheP)<br/>
}</p>
 </section>

### Yves Masur — 16 juin 2020 à 20:45

<section class="comment-content comment">
<p>Intéressant de comparer les deux approches. Faire le polling dans la boucle principale convient parfaitement. Si j’ai bien compris, c’est le schéma « pull-up » qui est utilisé, suivant le commentaire « attend signal stable bas » et le code, si c’est le cas: Boutons |= FLAGBTNP; // Ok, bouton pressé</p>
<p>Les états des boutons sont compactés en bits: avec 2 bits pour tenir compte de la machine d’état. L’utilisation de mémoire est très faible. Juste pas facile de savoir où est la variable de machine d’état par bouton.</p>
 </section>

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
