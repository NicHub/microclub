---
title: "TV connectée"
date: "2015-05-06T20:59:46"
lastmod: "2016-02-02T20:06:52"
author: "Rolf Ziegler"
categories: ["Articles", "Microclub"]
tags: ["4k", "dlna", "gadgets", "hdmi", "m4v", "musique", "nas", "nfc", "photos", "reseau", "samsung", "scart", "tv", "usb", "vhs", "video", "web", "wifi", "yuv"]
url: "/2015/05/06/tv-connectee/"
wordpress_id: 1898
comment_count: 5
---
# Choisir

Comment bien choisir sa TV aujourd’hui ? Les prix sont en baisse régulière, les options et les performances en hausse constante. Au début de ma carrière, une TV couleur 66 cm (pas d’autre choix) multinormes, n’acceptant que la HF coûtait entre 3500.- et 4500.-, Et un vidéo recorder, le même prix… le salaire du technicien débutant, en fin des années 1970 était de 2200.- brut. Donc, grosse maille, 2 salaires pour une TV. Aujourd’hui, pour un écran de 100 cm, on trouve des offres à 600.-, alors que le salaire médian est de 6000.-. Donc 1/10 de salaire pour un écran.\
Lequel choisir ? Quelles performances en attendre ? N’attendez pas de cet article une réponse limpide, d’autant plus que… je n’ai pas la TV ; j’utilise seulement l’écran pour passer des films. Les nouvelles TV sont **connectables**.

C’est-à-dire, via un câble Ethernet ou le WiFi, du contenu peut transiter. On trouvait encore il y a 10 ans, des écrans avec entrées RGB par BNC ; puis il y a 5 ans, l’entrée VGA. Maintenant, c’est HDMI. L’USB peut non seulement proposer des fichiers, mais sert maintenant à l’enregistrement d’émission – souvent dans un format propriétaire.\
Jeux vidéo obligent, il y a toujours l’entrée RCA vidéo composite (YUV) et le son. Et plus qu’une PERITEL pour un ancien – forcément – enregistreur à cassette VHS.\
Mais quel écran prendre ? Les plus petits, soit moins de 80 cm / 32 pouces, n’ont pas/plus toute la connectivité. Un 4K, autrement dit une définition d’au moins 4000 points en largeur pour miser sur l’avenir ? Actuellement, une telle résolution est confidentielle. La plupart sont en 1920 x 1080 ; à noter que les codecs vidéo actuels ne vont pas au-delà.

![](http://media.webcollage.net/rwvfp/wc/live/17264335/module/samsungus/resized/www.samsung.com/us/system/features/hw-h450_anynet.jpg.w960.jpg)\
Un semi circulaire ? Ça ne favorise pas une large vision de l’écran. Refresh à 200, 400, 800 Hz ? Si l’image classique TV est à 50 Hz (50 demi-images), c’est du remplissage, au mieux du lissage ; on ne verra pas forcément la différence. Une TV 3D ? Le nombre de film 3D est confidentiel ; mettre des lunettes assombrit l’image… Commande par geste ? Pourquoi pas…\
On peut aussi juger selon l’indice de consommation ; mais les indications sont pour le moins abstraites avec une indication d’énergie moyenne par an ; mieux vaut se fier au A+++ et à la puissance indiquée, notamment pour le stand-by.\
Pour que ça soit compatible avec le meuble bibliothèque, j’opte pour un 40’ – 100 cm de diagonale. Pour avoir un bon son, je vérifie les épaisseurs ; mais le vendeur m’affranchit : le son n’est de toute façon pas bon, il faut une barre de son. C’est un dispositif longiligne pour les aigues – médium, avec un caisson pour les basses. Les plus chères sont quasi le prix d’une TV, environ 700.-. J’opte pour une de milieu de gamme Samsung HW-H450; malheureusement avant d’avoir vu l’émission A bon entendeur. Rappelez-vous : je n’ai pas la TV ! On peut cependant voir l’émission sur le site de la RTS (<http://www.rts.ch/emissions/abe/6260414-television-quand-le-son-se-barre-la-barre-de-son.html> ) qui préconise, pour le même prix, de s’acheter une petit HiFi…\
Le jargon est étendu, en voici un exemple dont en gras, ce dont le présent article parle. **4K** ; UHD ; **1000Hz**; 3D ; Dimming; TWIN DVB-T/C/S2/Cl+/EPG; **WiFi** ; **DLNA** ; **USB recording** ; Time shift ; PIP ; EPG ; NFS ; Viera Link ; Master surround 2.1 ; **HDMI** ; **SCART** ; DisplayPort ; **YUV**\
Au final, j’hésitais entre deux modèles : Panasonic ou Samsung ? Un essai avec des fichiers sur une clef USB me montre que les photos sont bien rendues sur les deux ; par contre le Samsung ne passait pas un film au format Apple m4v. Ce qui n’a aucune importance, il suffit de renommer les fichiers en mp4 ! Par contre, mon mobile Note 3 de la même marque peut être connecté en mode copie d’écran : sympa pour passer des photos. Il semble qu’entre marque différentes c’est possible via la connexion NFC, mais il faut trouver les bons pilotes. J’opte pour le modèle UE40H6410. Les explications qui suivent sont basées sur ce modèle.

# Télécommandes

Me voici avec 3 télécommandes, 4 avec celle du VHS. Une pour la barre son, elle heureusement inutile sauf pour la configurer; puis deux pour la TV. La 2ème est la « touchpad », soit disant intuitive ; et configurable. Elle agit un peu comme une souris ; un capteur de mouvement permet de déplacer un pointeur sur l’écran et naviguer dans des menus. Qui ne sont guère intuitifs, à mon avis. En matière de commande, cerise sur le gâteau, le PC peut servir aussi de commande : mieux vaut qu’il soit portable.

# WiFi

Je n’ai pas testé le câble Ethernet, car le Wifi de la TV reconnait mon réseau. Elle peut aussi fonctionner en hostpoint. Pour se connecter au routeur, il faut juste être patient et précis pour entrer le password, avec la télécommande et le clavier présenté à l’écran. On pourrait en connecteur un physique sur une entrée USB (mais avec quel jeu de caractères ?).\
Puis on est connecté. Et que dit un poste ainsi connecté ? Mais oui : *voulez-vous mettre à jour le firmware maintenant ?* Puis ce message : *il n’y a pas de signal TV pour scanner les postes possibles*. La TV a donc pris une adresse sur mon routeur. Bien entendu, via le setup paramètres, il est possible de le configurer en manuel, ceci en IPV4 seulement : c’est donc clairement destiné à un sous-réseau et non pas à un accès « full » sur Internet.\
Afin de vérifier ce qu’on peut faire de cet écran, j’ai essayé :\
Ping – OK ; répond, même avec des paquets de 65’500 bytes !\
Telnet – pas de port 22 ; il se ferme tout de suite\
http – pas de réponse ; erreur 404\
D’autres outils réseau de la série Nirsoft ne montrent rien d’utilisable : pas de nom réseau, pas de constructeur de l’interface, rien. Pour aller plus loin, il faudrait hacker le poste : <http://www.numerama.com/f/117008-t-le-hacking-des-televisions.html> Ceci se fait via une clef USB, en « upgradant » le firmware (pour l’instant, je me retiens).

# Vu depuis la TV sur le LAN

Depuis la TV, on voit les PC avec leur nom réseau symbolique. Par exemple, mon portable est affiché avec un joli drapeau Windows, et indiqué « VOSTRO :Yves ». Il montre donc les noms des comptes utilisateurs ; pour chacun s’il y en a plus d’un, une nouvelle instance du PC est affichée. Bien… Si on cherche un fichier multimédia, on ne trouve… rien.[![04 SmV-folders1](/media/2015/05/04-SmV-folders1-1024x681.jpg)](/media/2015/05/04-SmV-folders1.jpg) Malgré tous les droits ouverts sur certains répertoires ; pas moyen de s’y promener. Il manque quelque chose. Une boite de dialogue affiche « impossible… », et c’est tout.

# Programmes pour l’Internet

Une série de programmes sont livrés avec l’appareil ; variable selon le pays. Une partie d’entre eux donne sur des sites payants ; il faut sortir sa carte de crédit. Souvent, les options ou l’activation passent par l’ouverture d’un compte Samsung, que l’on peut activer par… Facebook (au secours !) De retour sur le PC, j’ouvre le compte en question, mais certes hors de FB. Ceci n’est même pas nécessaire pour utiliser les applications suivantes : Youtube, Skype, Zattoo, Netflix, déjà prêtes à l’utilisation.

# Latence

Mon fils Jonathan, qui possède des consoles Nitendo d’un autre âge, les a testées sur la bête. Réaction : « C’est horrible ! Quelle latence !». Comme je lui en demande la démonstration, il me montre que l’appui sur le bouton de tir (je le suppose) réagit 100 ms plus tard… En réglant le filtrage de l’image moins fortement, la latence diminue. Il semble que le moyennage des pixels introduit du retard sur l’image. On peut heureusement faire ces réglages par type de sources vidéo.

# Smart view 2.0

Selon Samsung, c’est l’utilitaire de PC ou pour device Android qui fait tout. [![01 smartview-start](/media/2015/05/01-smartview-start-300x158.jpg)](/media/2015/05/01-smartview-start.jpg)\
Voyons cela. Il propose de faire deux choses : passer des images, des films, de la musique sur la TV; ou de la servir comme écran secondaire et de la télécommander. Un bouton permet de rechercher la TV sur le réseau…[![02 Smartview-connect](/media/2015/05/02-Smartview-connect-300x158.jpg)](/media/2015/05/02-Smartview-connect.jpg)

Après quelques secondes, on voit apparaître le nom qu’on a configuré ; on valide la connexion. Le programme présente alors 3 volets, surmontés de menus sobres.\
[![03 Smartview-connect](/media/2015/05/03-Smartview-connect-300x158.jpg)](/media/2015/05/03-Smartview-connect.jpg)

À partir d’ici, il faut découvrir. Et on découvre que si Samsung est fort pour hard ; concernant le soft, ce n’est pas si évident. Leurs ingénieurs n’ont pas pris des cours d’ergonomie. Ou c’est l’effet W8.\
On découvre deux modes : soit on lance un fichier depuis le PC sur la TV ; soit on cherche un fichier de la TV sur le PC.

## Depuis la TV, vue du contenu du PC

Si Smart View est démarré, mon PC est vu une deuxième fois : « multimédia VOSTRO », et présente 3 répertoires : RootImageFolder, RootVideoFolder, RootMusicFolder, avec les fichiers que l’on a partagé par DragDrop dans Smartview.\
Pour tester les limites de la solution, j’y ai mis tout mon dossier photo ; il pèse 31 Go. L’application a mis un temps important, entre 1H et 2H (je suis allé manger entre deux…). Mais visiblement, hormis le temps d’insertion, pas de duplication du contenu, car l’espace pris sur le HDD n’a pas gonflé entre deux. [![06 smartview add photos](/media/2015/05/06-smartview-add-photos-1024x542.jpg)](/media/2015/05/06-smartview-add-photos.jpg)\
Mais… vu de la TV, c’est la galère concernant la disposition. En effet, je stocke mes photos par répertoires année, puis par mois : 02, 02, 03… Cette organisation n’apparaît pas ainsi sur la TV. Le tri est fait de telle façon à ce que tous les répertoires sont mis « à plat ». Il y a donc une série de quinze icônes 01 (janvier !), puis de 02… sur deux lignes. Et des flèches pour aller un cran plus loin. Insupportable et inutilisable. Il faut donc partager seulement un nombre restreint de répertoires pour s’y retrouver. Et si possible, nommer ses photos. Une fois la séquence démarrée, on peut les faire suivre à l’écran comme un diaporama.\
Quant à la musique – sans compter le peu d’intérêt qu’il y a à passer de la musique sur une TV, la problématique est semblable, si ce n’est que les morceaux sont affichés dans une liste verticale. Ça ne fonctionne pas en parallèle avec le diaporama… Dommage.\
Pour les films partagés, je n’en ai que peu, ça fonctionne correctement. Attention toutefois à ce que le PC ne se mette pas en veille au bout d’une heure d’inactivité! Les fonctions pause, avance et recul rapide sont fonctionnelles. À signaler aussi, l’incroyable délai qu’il faut entre le moment du partage et sa visibilité. Et le fait que Smartview prend 25% du CPU, sans moindre transmission de fichier.

## Played on TV

Depuis la 3ème colonne de Smart View, j’essaie est de passer un film au format mp4 en glissant le fichier sur « Drag content here » de Smartview. Rien ne se passe. Car c’est seulement le contenu déjà mis dans Smart View que l’on peut cliquer-glisser là ! Après quelques secondes de mise en cache, ça marche et il apparait à l’écran ; mais je constate que le format cinémascope original n’est pas respecté (pas de bandes noires horizontales).\
De plus, impossible avec la télécommande de pause ou d’avance rapide. C’est le PC qui pilote, via Smart View.\
Le même principe vaut pour les photos et la musique ; fort heureusement ni les photos ni la musique ne sont déformés !

# DLNA – la norme qui fait… tout ?

Parmi les acronymes associés aux TV connectées, on trouve DLNA. C’est une norme permettant l’échange de contenu image/vidéo entre devices tels que PC, NAS ou smartphone. Explications ici : <http://www.clubic.com/article-314912-5-dlna-reseau-multimedia-maison.html> et Wiki là: <http://fr.wikipedia.org/wiki/Digital_Living_Network_Alliance>

# NAS et service multimédia

Parmi mes NAS (nom : NAS2 sur le LAN) celui qui convient le mieux est un Synology assez récent pour lui ajouter les services DLNA et UPnP. Je dois commencer par mettre Android à jour, en deux fois, car il passe de la version 4.x à 5.0 ; puis tout de suite après, encore à 5.0X… À la fin, je peux enfin activer le DLNA et le UPnP, par un programme « Service multimédia ».

[![20 NAS paquets](/media/2015/05/20-NAS-paquets.jpg)](/media/2015/05/20-NAS-paquets.jpg)\
Une fois installé et démarré, celui-ci ajoute trois répertoires à la racine du serveur : video, photos, music.\
Il me faut mapper des disques réseaux supplémentaires sur mon PC et déplacer ces monceaux de fichiers pour parvenir à mes fins.

[![22 NAS repertoires](/media/2015/05/22-NAS-repertoires.jpg)](/media/2015/05/22-NAS-repertoires.jpg)

Ouf, c’est fait. Et sur la TV, que vois-t-on ? « NAS2 » et trois propositions : Photos, Vidéos, et Musique.\
Si la vision de films ou l’écoute de morceaux de musique ne posent pas de problèmes ; les photos ne sont pas visibles. Le fichier est bien montré dans le folder, mais avec une taille de 0 octet. Alors qu’avec le PC elles sont parfaitement lisibles.

# Conclusion

Une TV connectée permet bien de visionner des émissions sur l’Internet, la bande passante est maintenant suffisante pour assurer une belle qualité. On peut également en profiter pour visionner des photos de son smartphone ; de son PC ou de son NAS. Il faut toutefois chercher la meilleure technique, ce qui demande des essais et de trouver sa voie parmi les techniques mises à disposition et plus ou moins bien implémentées.\
Yves Masur (5/2015)

## Commentaires

### Michel Vonlanthen — 6 mai 2015 à 23:42

Je ne résiste pas à l’envie de parler de l’actualité en relation avec ton téléviseur: la nouvelle méthode de perception de la taxe radio-TV que notre gouvernement veut nous imposer. Avec l’excuse de simplifier la procédure de perception, il veut facturer automatiquement cette taxe à tous les citoyens de ce pays, y compris à ceux qui n’ont ni radio ni TV.

C’est comme si on faisait payer la taxe autoroutière à ceux qui n’empruntent jamais l’autoroute (pour faire des économies) ou à ceux qui n’ont pas de voiture.

C’est une injustice insupportable non?

L’excuse donnée c’est qu’il y a très peu de gens qui n’écoutent ni radio ni TV. C’est exact mais c’est une raison de plus d’accepter de la retirer à ceux qui répondront à la facture par un « non, je n’ai pas de radio-TV ». Ce n’est pas plus compliqué que ça!

En plus il faut aussi pouvoir annuler une concession uniquement radio ou uniquement TV, pourquoi vouloir faire un paquet des deux? Les sourds, par exemple, devraient aussi payer la concession d’un média qu’ils ne peuvent pas écouter? Injustice!

Oui je sais, c’est l’aide sociale qui paiera pour eux, de même que pour les 30% de citoyens qui ne paient pas l’impôt fédéral direct parce que trop pauvres. Mais est-ce la raison d’être de l’aide sociale de financer les loisirs des citoyens? Il me semble qu’on devrait la garder pour les cas sociaux vitaux, sinon on court le risque d’augmenter massivement la facture des aides sociales, ce qui plombera nos impôts…

Au début de ma carrière de jeune papa, chaque été je résiliais ma concession TV car je ne la regardais pas. Et je la reprenais au début de l’hiver. Ca n’a jamais posé problème. Maintenant j’aurais de la peine à ne plus écouter la radio ou regarder la TV mais je résilierais sans hésiter ma concession si de la publicité devait faire son apparition sur nos chaîne radio RTS.

Car voici une raison de plus de refuser ce nouveau système: si la politique de programmes (et de la pub) de la RTS ne vous plaît pas, vous n’auriez même plus la possibilité de la refuser en résiliant votre concession. (Oui je sais, on pourra le faire pendant 5 ans, mais pourquoi 5 ans et pas indéfiniment? On nous prend vraiment pour des pommes!)

Pour terminer, forcer la main aux citoyens en abaissant la taxe de quelques dizaines de Francs pour les faire voter oui est vraiment prendre ces derniers pour des couillons. Car pourquoi le Conseil Fédéral veut-il changer de système de perception? Parce qu’il veut plus de pognon, sinon pourquoi le ferait-il?

En imposant à tous cette taxe de 400 Fr par année (dans un premier temps), il ne sera plus possible d’être pauvre en Suisse. N’oublions pas qu’une taxe est socialement injuste puisqu’elle touche proportionnellement plus les pauvre que les riches. 400Fr pour un pauvre c’est sa nourriture d’un mois entier (ça correspond à 20% de sa rente AVS) alors que pour un riche c’est sont argent de poche d’un jour. Si encore l’Etat la percevait avec les impôts, au moins serait-elle socialement juste puisque proportionnelle aux revenus des contribuables. Mais après la taxe poubelle, voici maintenant la taxe radio-TV!

Il faudra refuser massivement cette insulte à la Justice le 16 juin ! Voter NON !

Encore une chose: Pour en revenir à ton téléviseur, à l’heure où notre TV suisse est polluée massivement par de la publicité (plus d’une heure par jour), n’est-il pas le moment de rediscuter de notre service public? Et de faire choisir notre brave RTS entre redevance et publicité? Je suis d’accord qu’il faut bien financer l’infrastructure des émetteurs radio et TV, ça je suis d’accord de le payer car les ondes radio sont la dernière possibilité de transmettre des informations sans passer par des entreprises privées et donc sans censure. Mais pour les studios, les programmes et les salaires des directeurs, la pub peut largement les financer. Elle le fait bien pour les TV privées.

### ↳ Réponse — Yves Masur — 9 mai 2015 à 20:14

Hello Von, tu sors du sujet; mais je suis 100% d’accord avec toi. D’ailleurs, si tu as bien lu mon article, je n’ai pas la TV. Seulement la concession radio. Et je n’ai pas envie de sponsoriser des matchs et des courses de voitures…

### ↳ Réponse — Michel Vonlanthen — 19 mai 2015 à 11:22

C’est bien ce qui m’étonne dans cette votation. Je n’ai vu personne refuser l’amalgame concession radio et TV. C’est bien que le Conseil fédéral pense à faire des économies en introduisant un nouveau système de perception, mais tout de même pas au détriment de la justice la plus élémentaire (faire payer ceux qui ne veulent pas écouter la radio ou regarder la TV)! Si on continue comme ça, après la taxe au sac et la taxe radio-TV, on fera payer la vignette autoroutière à ceux qui n’ont pas de voiture « par mesure de simplification »…

### Goulu — 7 mai 2015 à 07:32

Ayant une « vieille » TV pas connectée, j’ai récemment fait l’acquisition d’un ChromeCast, vu son prix dérisoire ( <https://www.google.fr/chrome/devices/chromecast/> )\
Ce bidule rend votre TV « connectée » à très peu de frais, mais en demandant un peu de bidouille. Il faut installer du soft sur votre smartphone (Android ou iPhone) pour l’utiliser comme télécommande, puis installer <https://chrome.google.com/webstore/detail/videostream-for-google-ch/cnciopoikihiagdjbjpnocolokfelagl?hl=fr> pour le navigateur Chrome pour pouvoir voir les films stockés sur un PC en réseau ou un NAS.

### RenéS — 7 mai 2015 à 16:14

Je viens d’acheter une TV Samsung 40UE6470, donc aussi une 40 pouces. Je l’ai connectée en Wifi sur mon routeur sans problèmes. J’ai pu me connecter sur mon NAS WD MyCloud 3Gb (récent, DNLA) sans problèmes. J’ai aussi les 3 options Musique/Photos/Vidéo. Tout passe sans problèmes.\
Une spécificité (indiqué dans le mode d’emploi de la TV) : si je choisis « Vidéo », je vois les fichiers Photos, mais je ne peux les lire.\
Bon, c’est vrai que j’ai aussi dû ouvrir un compte Samsung et Zattoo.\
Tout va presque pour le mieux dans le meilleur des mondes.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
