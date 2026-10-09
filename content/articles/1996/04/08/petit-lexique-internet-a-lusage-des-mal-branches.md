---
title: "Petit Lexique INTERNET à l'usage des mal branchés."
date: "1996-04-08T15:44:14"
lastmod: "2015-04-24T23:20:25"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: []
url: "/1996/04/08/petit-lexique-internet-a-lusage-des-mal-branches/"
wordpress_id: 49
comment_count: 0
---
*(documents publiés dans le Mi-Chronique No 51 à 53 d’Avril 1996 à Février 1997 et retrouvés en mai 2008 )*

Dans un dico normal, les mots sont rangés par ordre alphabétique. Comme de plus en plus de gens ne savent pas l’alphabet, y compris les américains pour lesquels le « æ » est compris entre le « å » et le « ç », ce qui ne facilite pas la recherche de ma copine Lætitia sur INTERNET, je n’insiste pas et vous propose quelques notions d’internautes en commençant par les notions les plus « bas niveau » sur lesquelles INTERNET est basé et dont vous n’avez tellement rien à faire que vous pouvez les oublier à peine lues, et en terminant par les derniers développements disponibles en bêta version pour les initiés, c’est-à-dire complètement démodés l’année prochaine. Bref, les tuyaux utiles sont au milieu de l’article, le reste c’est du remplissage.

### Paquet

Toutes les informations circulant sur INTERNET sont groupées en paquets de taille variant entre quelques octets et quelques Ko maximum. Un paquet contient de l’information venant d’un expéditeur vers un destinataire, le protocole [TCP](#TCPIP) étant responsable de son acheminement. TCP utilise pour ceci uniquement l’adresse [IP](#TCPIP) du destinataire qui figure en entête du message. Si une grosse information est divisée en multiples paquets, les paquets sont numérotés et le message est recomposé par TCP à la fin de son périple, qui peut être rendu mouvementé par les aléas du [**routage**](#routage).

### Routage

INTERNET est un réseau « maillé » comme son ancêtre [ARPANET](#arpanet). Ceci signifie qu’il existe en principe plusieurs chemins possibles pour les paquets entre deux points quelconques du réseau. Les [noeuds](#noeud) de la toile d’araignée sont chargés de décider par quel chemin un paquet doit passer en fonction de l’état de charge des liaisons utilisées entre noeuds. On ne sait donc pas à l’avance par où passera un paquet entre deux points, c’est décidé dynamiquement.

### Noeud

Les noeuds sont les points ou les liaisons INTERNET se connectent et où le [routage](#routage) s’effectue. Comme les objectifs stratégiques d’[ARPANET](#arpanet) ne sont pas cruciaux pour INTERNET, la structure du réseau n’est vraiment maillée qu’au niveau international et intercontinental. Les noeuds locaux, par exemple votre [fournisseur de service](#fournisseur) ne fait que router que le trafic de quelques [modems](#modem) vers un noeud régional qui envoie tout ça au national et là ça devient assez maillé, bien que presque tout le trafic international passe par le noeud continental d’Amsterdam. En principe, un noeud devrait être connecté en permanence aux diverses liaisons pour garantir le routage. S’il tombe en panne, pour autant que le réseau soit suffisamment maillé dans le coin, aucune information ne sera perdue. Ca sera peut-être un peu plus lent, c’est tout.

### ARPANET

Ancètre d’INTERNET, ARPANET est le réseau de communications militaires des USA, spécialement conçu pour résister à une destruction massive (nucléaire) de certains de ses constituants. C’est un réseau totalement décentralisé et fortement maillé, contrairement aux réseaux locaux genre [ETHERNET](#ethernet) qui reposent sur un seul câble.

### Modem

C’est le bidule qui permet à ton ordinateur de téléphoner, eh!. Si t’en as pas u qui crache à 14’400 bauds, t’oublie INTERNET, mec!. Si tu veux être dans le coup, tu peux toujours la jouer [ISDN](#isdn).

### ISDN

Avec le « integrated services digital network » « réseau numérique à intégration de services » (RNIS), les PTT du monde civilisé ont entrebaillé la porte du numérique aux privés : sur une ligne téléphonique normale on peut désormais brancher des tas d’appareils numériques comme des [modems](#modem) crachant à 64’000 bauds, des fax incroyablement rapides et même des téléphones qui vous affichent le numéro de votre belle-mère avant même que vous ne décrochiez pas. En Suisse, les PTT appellent ça « SWISSNET » et ça coûte comme deux lignes téléphoniques. Ce genre de connexion est beaucoup utilisée par les petits [fournisseurs de service](#fournisseur) locaux car elle leur permet de servir une dizaine de [modems](#modem) très facilement.

### ETHERNET

Y’en a toujours qui confondent avec INTERNET. Ca n’a rien à voir. Ethernet est un système de réseau local actuellement très utilisé et consistant à mettre plusieurs ordinateurs en vrac sur un câble. Ils se causent quand ils veulent et si deux parlent en même temps (collision), ils s’interrompent et recommencent au bout d’un temps aléatoire. En fait tout ça a commencé aux îles Hawaï où l’université a fait un réseau baptisé ALOHA pour communiquer entre les îles. On utilisait des ondes radio, d’où ETHER-net. Maintenant, c’est bien sur des réseaux ETHERNET que le protocole [TCP-IP](#TCPIP) a pris son essor.

### TCP-IP

« Transfer Control Protocol » et « Internet Protocol » sont les piliers du système postal d’INTERNET permettant le [routage](#routage) des [paquets](#paquet) jusqu’à leur destinataire. Chaque heureux participant à INTERNET, vous, moi, le [fournisseur de services](#fournisseur), [AltaVista](#altavista) et les autres est identifié par une adresse IP qui n’avait que 32 bits jusqu’à récemment, maintenant je sais plus. Comme c’est pas facile d’identifier les gens par un nombre entre 0 et 4’294’967’295, on a pris d’abord la convention de le découper en 4 octets notés en décimal séparés par des points, style 128.178.4.56. L’astuce c’est que les adresses sont pas distribuées au hasard mais selon des zones géographiques, ce qui facilite vachement le [routage](#routage) dans les [noeuds](#noeud). En effet, le premier octet correspond vaguement aux continents, le second au pays, le troisième et le quatrième au réseau local. Bien sur, tout ça n’est toujours pas très pratique, alors on a introduit les serveurs [DNS](#dns) qui permettent d’utiliser des adresses sous forme de texte.

### DNS

Les « Domain Name Servers » sont des sortes d’annuaires donnant l’adresse [IP](#TCPIP) numérique correspondant à une adresse sous forme texte. Comme leur nom l’indiquent, les DNS ne connaissent qu’un « domaine » limité d’Internet, mais ils connaissent aussi d’autres DNS à qui demander un coup de main si on cherche une adresse distante. Exemple : si je cherche l’adresse de <www.microsoft.com> (pour dire vraiment n’importe quoi) et que je demande à mon pauvre serveur DNS romand, il va lire l’adresse à l’envers : « .com » c’est aux USA, donc il connaît pas, donc il demande un coup de main au DNS suisse, qui demande à Amsterdam, qui demande aux USA qui demande à Seattle, lequel me renvoie gentiment l’adresse IP.

### Fournisseur de services

Petits [noeuds](#noeud) locaux qui offrent un accès par [modem](#modem) aux particuliers. En fait, ces noeuds sont les plus petits qui soient : ils n’ont souvent qu’une à une dizaine de lignes téléphoniques en entrée et routent le trafic sur une ou deux lignes [ISDN](#isdn) à destination d’un noeud un tout petit peu plus grand qu’eux. A part les modems et les lignes, un tel noeud ne requiert en fait qu’un « petit » ordinateur tournant de préférence sous UNIX (les outils sont les plus sophistiqués et les moins chers : domaine public!). En fait, les privés n’ont besoin que d’un compte sur cette machine, ce qui signifie un accès très similaire à celui qu’on peut avoir sur un BBS. Après connexion en mode texte, on démarre une connexion [**SLIP**](#slip) ou [PPP](#ppp) qui nous branche vraiment à INTERNET. Pour le prix d’un abonnement mensuel (actuellement env. 30.- / mois) on obtient aussi une adresse [e-mail](#email) et certains fournisseurs vous permettent même de créer vos pages [WWW](#www) sur leur machine. Le meilleur deal à Genève, c’est d’acheter un PC chez Infomaniak : on a deux ans d’accès à INTERNET gratuits par chez eux…

### SLIP

A ne pas confondre avec TANGA ou STRING. « Serial Link Internet Protocol », une manière de passer des [paquets](#paquet) sur une ligne série, donc par [**modem**](#modem).

### PPP

« Point to Point Protocol ». Il faut bien réaliser qu’un vrai « branché » à INTERNET doit y rester connecté tout le temps : si on essaie de lui envoyer un [**paquet**](#paquet) pendant qu’il est pas là, l’info se perd. Avec un modem, on n’est pas vraiment branché, on est utilisateur d’une machine appartenant au [fournisseur de services](#fournisseur), mais il nous faut quand même une adresse [**IP**](#TCPIP), sinon comment un expéditeur pourra-t-il faire la différence entre les 1548 abonnés au même [fournisseur de services](#fournisseur), hein ? Mais on peut pas non plus réserver 1548 adresses IP pour tous ces gens, y’en a que 10 au max. Qui seront branchés en même temps. Alors PPP attribue dynamiquement les 10 adresses aux gars connectés. Autrement dit, à chaque fois qu’on se connecte, onreçoit une adresse valable pour la durée de la connexion. La prochaine fois qu’on se connecte, on en reçoit une autre.

### e-mail

La plus belle invention depuis le timbre poste. E-mail permet de s’envoyer des messages entre utilisateurs d’INTERNET. L’adresse du destinataire est de la forme « <pgugliel@infomaniak.ch> » où l’arrobase (at…) signifie « … utilisateur de la machine … ». Si vous vous connectez par [modem](#modem), c’est la machine de votre [fournisseur de services](#fournisseur). Chaque machine a une adresse [IP](#TCPIP) propre à son entrée e-mail, gérée par un serveur SMTP (Simple Mail Transfer Protocol) qui, lorsqu’il reçoit un paquet qui a l’air d’un e-mail, ellle regarde le nom de l’utilisateur et dépose le message dans sa boîte, en attendant qu’il veuille bien se connecter pour lire ses messages. Certains gourous d’INTERNET n’utilisent que le e-mail. En effet, certaines astuces permettent de transférer des fichiers par [FTP](#ftp) et même de lire des pages [WWW](#www) par e-mail uniquement. De plus l’accès à de nombreux groupes de [news usenet](#usenet) est possible via les [mailing-lists](#mailing). Pour faire tout ça, on commence à avoir besoin de logiciels un peu musclés. Sur PC, outre le très bon Exchange livré avec Windows 95, on trouve aussi Eudora dans le domaine public. De plus, des [browsers](#browser) comme [Netscape](#Netscape) gèrent aussi e-mail.

### Mailing-lists

Les mailing lists sont des listes de destinataires de messages [**e-mail**](#email). Elles permettent d’envoyer un message à plein de destinataires. Des petits futés ont bricolé un système qui permet d’ajouter automatiquement l’adresse de quelqu’un à une liste, puis d’envoyer tous les messages qu’ils reçoivent aux inscrits, voire de les collecter en un seul message envoyé tous les jours. Il existe ainsi des centaines de listes de distribution associées à des tas de thèmes plus ou moins intéressants. Pour s’inscrire, il suffit pour la plupart d’envoyer un message e-mail à une adresse ‘<majordomo@la.machine.qui.soccupe.de.la.mailing.list>’ et de mettre soit dans le titre du message soit dans le texte du message (je le mets dans les deux…) le mot « subscribe ». Et voilà!. Ensuite, chacun peut poster des messages à la machine en question, répondre à d’autres messages etc. en utilisant une autre adresse e-mail. L’avantage de ce système sur les [news usenet](#usenet) c’est qu’il y a moins de bordel, de pub car seules les personnes intéressées « subscribent » et on peut les retrouver facilement. L’inconvénient, c’est qu’il faut pas faire le con : le mec qui a une fois inclus un fichier binaire de 2Megas à son mail à la mailing list sur LabView se souvient encore de la bordée qu’il s’est pris de centaines d’utilisateurs qui ont reçu ça, qui ont planté leur e-mail et compagnie…

### News Usenet

Il existe des milliers de groupes plus ou moins d’intérêt sur tous les sujets possibles et imaginables sur cette planète et les autres. Chacun peu librement, sans aucune restriction d’accès lire les millions de messages « postés » et en écrire sans aucun contrôle. C’est en train de devenir le bordel complet, inutilisable, à moins de ne s’intéresser qu’à une branche particulière de la physique théorique. Ce système est géré par un système complexe de serveurs NNTP fonctionnant par un système d’abonnement : chaque serveur offre au reste du monde quelques newsgroups locaux et s’abonne à ceux du reste du monde qui peuvent intéresser les utilisateurs locaux. Le serveur NNTP maintient les textes des messages locaux et n’en transmet que les titres à ses abonnés. Il reçoit donc les titres des groupes auxquels il est abonné et offre donc instantanément à ses utilisateurs la liste de ces titres. Une fois un message potentiellement intéressant repéré, il faut le demander au serveur qui va le downloader du serveur propriétaire du groupe. Il existe des tas de logiciels pour lire les news. Pour les utilisateurs se connectant par [modem](#modem), le meilleur est « Free Agent » qui comme son nom l’indique est shareware. Il est le seul actuellement qui permette de downloader automatiquement les messages de newsgroups choisis pour pouvoir les lire et y répondre off-line. Pour l’utilisateur occasionnel, les [browsers](#browser) comme [Netscape](#Netscape) vont très bien.

### FTP

Le « File Transfer Protocol » permet de transférer des fichiers à travers le réseau. Là vous sentez que ça commence à devenir intéressant en même temps que dangereux… En fait, pour « pomper » un fichier sur une autre machine il faut:

1. Que vous ayez le droit de vous connecter à ce serveur, avec nom d’utilisateur et password.
2. Que la machine de destination ait un « serveur FTP » qui soit capable de répondre à vos commandes (du genre DIR, COPY etc.)
3. Que vous soyez l’heureux possesseur d’un logiciel « client FTP » qui envoie au serveur les commandes ad-hoc pour transférer les fichiers. A noter que les bons [browsers](#browser) comme [Netscape](#Netscape) font en général aussi office de clients FTP.

En pratique donc, 3 ne pose pas de problème, 2 non plus parce que toutes les machines plus ou moins sérieusement connectées à INTERNET sont munies de serveurs FTP, reste plus que 1.

Là y’a ce qu’on appelle le « loguine anonymousse » (anonymous login in English). Beaucoup de machines offrent un accès très limité (en général lecture seule sur certains répertoires) à tout utilisateur dont le nom est « anonymous » et qui a la [netiquette](#netiquette) de donner son adresse [e-mail](#email) comme password. Cette astuce permet de donner en accès public des fichiers, donc de faire une sorte de BBS sur le réseau. Bien sur, z’allez me dire que c’est la Mecque du parfait pirate. Je répondrais que (hélas) non parce que c’est très facile d’une part de localiser géographiquement un serveur qui violerait la loi (reste à savoir laquelle) et d’autre part de tracer le petit malin qui s’y connecterait soit pour downloader soit pour uploader des cochonneries, parce que, n’est-ce pas, le piratage du soft c’est ringard, maintenant ce qu’il fait c’est de la pornographie, du sexe, de la violence. (Voilà, c’est fait, ya ces mots sur la page Web du Microclub donc tous ceux qui vont cherche « sex » ou « porn » sur [AltaVista](#altavista) vont trouver cette page! Youpie!)

Bon alors FTP ça sert à quoi en pratique ? Ben:

1. A pomper du shareware, et yen a des gigatriffouillées de terabytes un peu partout, a tel point qu’un truc comme [Archie](#archie) c’est vraiment utile.
2. A uploader vos belles pages [WWW](#www) chez votre [fournisseur de services](#fournisseur).
3. A servir de base au protocole [HTTP](#http).

### Archie

Un gros problème d’INTERNET qui n’est pas prêt de se résoudre est celui de la bande passante, autrement dit de l’utilisation rationnelle des lignes de communication. Un des plus anciens efforts pour optimiser quelque peu les transferts est le projet Archie. L’idée est que les (gros) serveurs qui offrent des fichiers publics par [FTP](#ftp) transmettent une liste de ces fichiers à des serveurs « Archie » (comme archives) qui sont capables de communiquer entre eux. Lorsqu’un utilisateur a besoin d’un fichier donné, il se connecte à un serveur Archie proche de chez lui et fait une recherche. Le serveur lui renvoie les adresses complètes (machine+path+filename) des serveurs qui ont ce fichier et il choisit le plus proche de chez lui.

Il existe des « clients Archie » très bien interfacés avec des « clients FTP » : Sous Windows95 on fait une sorte de recherche de fichier comme s’il était sur la machine locale, puis on drague-droppe ou double-clique pour le copier en local par [FTP](#ftp).

### WWW

Faut vraiment que je vous explique ce qu’est le « World Wide Web » ? Aujourd’hui quand le pékin te parle INTERNET il te parle du <WWW>. Il sait pas la différence. Un peu comme un gars qui t’expliquerait que la télé, c’est une antenne avec une télécomande.

« World Wide Web » ça veut dire « toile d’araignée mondiale » et ça décrit de façon assez réaliste la situation de l’information disponible sur Internet depuis que le CERN a publié sur Internet des documents écits en [HTML](#html) et diffusé partout le premier [browser](#browser), Mosaic. Avec cet outil, il est devenu possible de surfer l’information et c’est sans aucun doute ce qui a permis de lancer INTERNET dans le marché public.

### Surfer

Naviguer sur le [WWW](#www) en suivant les liens sans se soucier de la localisation géographique, ni même de l’identité des serveurs sur laquelle elle se trouve.

Comme le surf aquatique, ç’est une passion dévorante et qui donne soif. Par contre, cette activité est coûteuse, mais peu dangereuse et n’attirera absolument pas du tout les nanas avant que j’aie enfin trouvé un fabriquant pour mon idée de tubes cathodiques renforcés dans l’ultraviolet.

### HTML

L' »HyperText Markup Language » est le format des documents [WWW](#www). C’est simplement du texte avec des « tags » permettant de définir le formattage (titres, listes, etc) d’inclure des images etc. mais surtout des liens vers d’autres documents. En fait, il suffit de taper le nom d’un serveur HTTP à l’autre bout de la planète suivi du nom du fichier auquel on veut se référer et l’utilisateur y aura accès rien que d’un click sur un mot ou une image.

Le format HTML devrait être standard, mais avec le boum du [WWW](#www) et la compétition acharnée entre les [browser](#browser)s, chacun y va de sa petite extension et de sa petite variante. Actuellement, la tendance est résolument « interactive » et « multimédia ». On peut maintenant insérer des sons, animations, voire des mondes virtuels en 3D au beau milieu de pages qu’on peut découper en « frames » etc. . Il va falloir faire de l’ordre dans tout ça mais ça sera pas facile.

### HTTP

Là mes petits amis, je dois avouer mon incapacité à vous dire exactement en quoi HTTP diffère de [FTP](#ftp). HTTP c’est « Hyper-text transfer protocol » et ça sert à naviguer sur le [WWW](#www). Comme le [WWW](#www) marche en copiant les pages (et les fichiers auxiliaires) sur la machine du client, en fait c’est exactement comme une sorte de couche par dessus [FTP](#ftp).

Je suspecte que HTTP est un peu plus malin en ce sens qu’il regarde le code [HTML](#html) des pages auxquelles on accède et voit qu’il faut transmettre avec des fichiers annexes comme les images, les sons etc. Ce qui est sur, c’est qu’il doit supporter les « [scripts CGI](#CGI) »

### CGI Scripts

Il existe des serveurs [HTTP](#http) extrêmement malins qui « fabriquent » des documents au moment où on les demande. Une application commune est le compteur du nombre d’accès que vous trouvez dans bon nombre de pages [WWW](#www). Si vous les regardez bien, vous verrez que c’est des images. En fait, un script CGI fabrique l’image (en concaténant des images de digits) au moment où il y en a besoin.

Beaucoup plus complexes sont les [Search Engines](#Search) comme [AltaVista](#altavista) qui n’ont pratiquement aucune page WWW fixe, prédéfine, mais qui les génèrent entièreemnt au rythme des mesoins. On peut donc tout faire en CGI, mais il faut que le serveur soit d’accord qu’on fasse tourner du code chez lui… Avec [Java, JavaScript](#java) et les autres, c’est le client qui va trinquer…

### Browser

Le browser est le logiciel « client » que vous utilisez en ce moment pour admirer cette belle page sur le web. Si vous êtes devant un papier jaune, vous trouverez un browser sur n’importe quel CD-ROM fourni avec n’importe quelle autre revue d’informatique au kiosque du coin.

Actuellement, la bagarre est terrible entre le Netscape Navigator et le Microsoft Internet Explorer. Alors que Bill ne croyaint tellement pas à Internet qu’il n’a introduit le protocole [TCP-IP](#TCPIP)

### Search Engines

qui sont en fait des énormes bases de données et qui interprètent une requête en générant le [HTML](#html) qui produit la page [WWW](#www) avec les résultats.

### AltaVista

### Java, JavaScript, ActiveX

### Netiquette

*Goulu le câblé*

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
