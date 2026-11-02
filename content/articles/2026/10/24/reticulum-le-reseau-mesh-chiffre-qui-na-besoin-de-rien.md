---
title: "Reticulum… Le réseau mesh chiffré qui n’a besoin de rien"
date: "2026-10-24T19:01:41"
lastmod: "2026-10-24T19:01:41"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2026/10/24/reticulum-le-reseau-mesh-chiffre-qui-na-besoin-de-rien/"
wordpress_id: 5907
comment_count: 0
---

Un réseau chiffré de bout en bout, indépendant du support et de toute infrastructure

> Topo technique : principes, architecture, outils et cas d’usage

Octobre 2026 Jean-Pierre Broillet Microclub

Vous avez aimé, vous aimez Meshtastic. alors cous aimerez peut-être RETICULUM…

## 1. En bref

**Reticulum** (souvent abrégé RNS, pour « Reticulum Network Stack ») est une pile réseau complète, conçue pour construire des réseaux maillés résilients et chiffrés au-dessus de n’importe quel support physique capable de transporter quelques octets : une radio LoRa, un lien WiFi, un câble Ethernet, une liaison série, un modem de radio amateur ou même un tunnel à travers Internet. Elle ne remplace pas une application, elle remplace la couche réseau : là où l’on utiliserait habituellement IP, TCP et TLS, Reticulum fournit l’adressage, le routage, le chiffrement et le transport fiable en un seul ensemble cohérent.

Le projet est créé et maintenu par **Mark Qvist**. L’implémentation de référence est écrite en Python et s’installe en une commande (`pip install rns`). Après une longue phase bêta, la version 1.0.0 est sortie en juillet 2025, suivie de versions de maintenance de la série 1.x qui ont notamment ajouté la prise en charge des RNodes LoRa haute puissance et la connexion des RNodes en WiFi ou Ethernet.

### L’idée centrale

{{< alert icon="lightbulb" >}}
Reticulum part du principe qu’on ne peut pas compter sur une infrastructure centralisée (opérateurs, DNS, autorités de certification, adresses IP attribuées).
Chaque participant génère lui-même son identité cryptographique, et le réseau s’organise sans coordination, même sur des liens extrêmement lents et intermittents.
{{< /alert >}}

### Ce que Reticulum rend possible, concrètement

-   de la **messagerie** asynchrone avec stockage et retransmission (protocole LXMF) ;
-   des **transferts de fichiers** de taille arbitraire, avec compression, découpage et vérification d’intégrité ;
-   des **appels vocaux** en temps réel (protocole LXST) ;
-   du **shell distant** et de l’exécution de commandes à distance (rnsh, rnx) ;
-   des « sites » et forums consultables hors Internet (Nomad Network) ;
-   de la télémétrie et du partage de position (Sideband).

## 2. Philosophie et principes de conception

### 2.1 Aucune infrastructure requise

Il n’existe pas de « réseau Reticulum » unique au sens où il existe un Internet unique. Reticulum est un protocole : n’importe qui peut monter son propre réseau, isolé ou interconnecté avec d’autres. Deux ordinateurs portables reliés par un câble, trois radios LoRa dans une vallée ou une communauté de nœuds connectés par TCP à travers le monde sont tous des réseaux Reticulum valides, et ils peuvent fusionner dès qu’un lien les relie.

### 2.2 Chiffrement obligatoire et identités auto-générées

Tout trafic vers une destination est chiffré par défaut ; il n’y a pas de mode « en clair » pour les communications privées. Chaque entité possède une **identité** composée de deux paires de clés sur courbes elliptiques : une clé X25519 pour l’échange de clés (chiffrement) et une clé Ed25519 pour les signatures, soit un ensemble de 512 bits. Aucune autorité ne délivre ces identités : chacun les génère localement.

### 2.3 Pas d’adresse source

Les paquets Reticulum ne contiennent **pas d’adresse source**. Un observateur qui capte un paquet peut voir vers quelle destination il va, mais pas qui l’a émis. C’est une propriété forte pour la vie privée, très différente d’IP où l’adresse d’origine figure dans chaque en-tête.

### 2.4 Fonctionner sur des liens très lents

Reticulum est conçu pour rester utilisable avec des débits extrêmement faibles (de l’ordre de quelques centaines de bits par seconde, voire moins) et des latences élevées. La MTU par défaut est de 500 octets, l’établissement d’un lien chiffré ne demande que trois paquets (quelques centaines d’octets au total), et le maintien d’un lien ouvert ne coûte qu’une fraction de bit par seconde. C’est ce qui rend la pile pertinente sur LoRa ou sur radio HF, là où TCP/IP serait inutilisable.

### 2.5 Indépendance vis-à-vis du support

Les applications ne savent pas, et n’ont pas besoin de savoir, par quel support passent leurs données. Un message peut quitter un téléphone en Bluetooth, traverser un lien LoRa de plusieurs kilomètres, passer par Internet en TCP puis finir sur un réseau local en WiFi, sans que l’application n’ait à s’en soucier.

## 3. Architecture technique

### 3.1 Destinations et adressage

Dans Reticulum, on ne s’adresse pas à une machine mais à une **destination** : un point de terminaison identifié par un hachage tronqué de 128 bits (16 octets), dérivé de l’identité et d’un nom d’aspect (par exemple lxmf.delivery pour une boîte de réception de messagerie). Un même appareil peut exposer plusieurs destinations, et une destination peut changer d’appareil ou de réseau physique tout en gardant la même adresse : l’adresse est liée à la clé, pas à la topologie.

Il existe plusieurs types de destinations : **single** (chiffrée vers une identité unique, le cas courant), **group** (clé symétrique partagée), **plain** (non chiffrée, pour la diffusion publique) et **link** (canal établi entre deux pairs).

### 3.2 Annonces et découverte de chemins

Pour être joignable, une destination émet une **annonce** : un paquet signé contenant sa clé publique et éventuellement des données applicatives. Les nœuds de transport propagent ces annonces et mémorisent, pour chaque destination, par quelle interface et quel voisin elle est atteignable. Personne ne connaît la topologie complète : chaque nœud sait seulement quel est le prochain saut. La propagation des annonces est plafonnée (par défaut à environ 2 % de la bande passante d’une interface) pour éviter qu’elles ne saturent les liens lents.

Si un nœud ne connaît pas encore de chemin vers une destination, il peut émettre une **requête de chemin** ; un nœud qui connaît la réponse renvoie l’annonce correspondante.

### 3.3 Nœuds de transport

Tous les nœuds ne routent pas. Par défaut, une instance Reticulum est un simple point d’extrémité. Une instance configurée avec `enable_transport = Yes` devient un **nœud de transport** : elle relaie les paquets et les annonces pour les autres. On active typiquement ce mode sur des machines fixes et bien connectées (un Raspberry Pi avec une RNode sur un toit, un serveur passerelle entre LoRa et Internet), pas sur un téléphone mobile.

### 3.4 Liens et ressources

Un **link** est un canal virtuel chiffré et vérifié entre deux destinations, établi par un échange Diffie-Hellman éphémère : chaque lien a ses propres clés, ce qui assure la **confidentialité persistante** (forward secrecy). Une fois le lien ouvert, on peut y envoyer des paquets, faire des requêtes de type requête/réponse, ou transférer des **ressources**.

Une **ressource** est un bloc de données de taille quelconque (fichier, image, page) que Reticulum se charge de compresser, découper, séquencer, acheminer, réassembler et vérifier. C’est la brique sur laquelle reposent les transferts de fichiers.

### 3.5 Cryptographie

| **Fonction**                  | **Mécanisme**                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Échange de clés               | ECDH sur Curve25519 (X25519), clés éphémères par lien                                                                                |
| Signature                     | Ed25519                                                                                                                              |
| Chiffrement symétrique        | AES-256 en mode CBC avec padding PKCS7 (AES-256 par défaut depuis la 0.9.6 ; les modes AES-128 historiques ont été retirés en 1.0.0) |
| Authentification des messages | HMAC-SHA256 (format de jeton inspiré de Fernet)                                                                                      |
| Dérivation de clés            | HKDF                                                                                                                                 |
| Hachage / adressage           | SHA-256, tronqué à 128 bits pour les adresses                                                                                        |
| Paquets isolés                | Ratchets : rotation périodique de clés pour apporter de la forward secrecy même hors lien établi                                     |

Ces primitives sont classiques et éprouvées ; l’originalité de Reticulum tient à leur assemblage et à leur sobriété en octets, pas à de la cryptographie nouvelle. À notre connaissance, le protocole n’a pas fait l’objet d’un audit de sécurité indépendant publié, ce qui est un point à garder en tête pour des usages sensibles.

## 4. Interfaces et supports physiques

Reticulum se branche sur les supports via des **interfaces**, déclarées dans le fichier de configuration `~/.reticulum/config`. Une même instance peut utiliser plusieurs interfaces simultanément et router entre elles.

| **Interface**            | **Usage**                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| AutoInterface            | Découverte automatique des pairs sur le réseau local (WiFi, Ethernet) via multicast IPv6, sans configuration |
| TCPClient / TCPServer    | Relier des instances à travers Internet ou un réseau IP existant, ou rejoindre un nœud public                |
| UDPInterface             | Diffusion sur un segment IP                                                                                  |
| I2PInterface             | Transport anonyme à travers le réseau I2P                                                                    |
| RNodeInterface           | Radio LoRa via une RNode (matériel ouvert, connecté en USB, Bluetooth, et désormais WiFi ou Ethernet)        |
| RNodeMultiInterface      | RNode à plusieurs radios / sous-interfaces                                                                   |
| SerialInterface          | Liaison série brute (modems, câbles, radios data)                                                            |
| KISSInterface / AX25KISS | Modems et TNC de radio amateur (packet radio)                                                                |
| PipeInterface            | N’importe quel programme externe via stdin/stdout : permet d’inventer ses propres transports                 |
| BLE (Android)            | Bluetooth Low Energy, notamment pour relier un téléphone à une RNode                                         |

### 4.1 Les RNodes

Une **RNode** est un émetteur-récepteur LoRa générique, ouvert, qui fonctionne avec un micrologiciel dédié. On peut en fabriquer une à partir de cartes de développement courantes et bon marché (familles LilyGO T-Beam, T3S3, Heltec, etc.) en flashant le firmware avec l’utilitaire rnodeconf. LoRa offre des portées de plusieurs kilomètres en terrain dégagé (bien davantage avec des antennes en hauteur) au prix de débits faibles, de quelques centaines de bits à quelques dizaines de kilobits par seconde selon les paramètres.

### 4.2 Modes d’interface

Chaque interface peut recevoir un **mode** qui influence la façon dont les annonces et les chemins sont gérés : full (par défaut), gateway (une passerelle qui résout les chemins pour ses clients), access_point (point d’accès pour clients mobiles, avec des chemins à durée de vie courte), roaming (interface physiquement mobile) et boundary (frontière entre deux segments de réseau très différents, par exemple entre Internet et un réseau LoRa local).

## 5. Les outils en ligne de commande

Le paquet rns fournit un ensemble d’utilitaires qui couvrent l’administration du réseau et plusieurs usages directs :

| **Outil** | **Rôle**                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------ |
| rnsd      | Démon Reticulum, à lancer comme service système ; les applications locales se partagent cette instance |
| rnstatus  | État des interfaces, trafic, voisins                                                                   |
| rnpath    | Consulter et demander des chemins vers des destinations                                                |
| rnprobe   | Tester l’accessibilité d’une destination (l’équivalent d’un ping)                                      |
| rncp      | Copier des fichiers vers ou depuis une autre machine                                                   |
| rnx       | Exécuter des commandes à distance                                                                      |
| rnid      | Gérer les identités ; chiffrer, déchiffrer et signer des fichiers                                      |
| rnodeconf | Flasher, configurer et mettre à jour des RNodes                                                        |

Le **shell distant interactif** est fourni par un projet séparé, rnsh, qui offre une session de terminal complète (à la manière de SSH) à travers Reticulum, utilisable même sur un lien LoRa.

## 6. L’écosystème applicatif

### 6.1 LXMF : la messagerie

**LXMF** (Lightweight Extensible Message Format) est le protocole de messagerie de l’écosystème. Il gère la livraison directe quand le destinataire est joignable, et la **livraison différée** via des « propagation nodes » : des nœuds qui stockent les messages chiffrés et les remettent quand le destinataire réapparaît, à la manière d’un serveur de courrier mais sans pouvoir lire le contenu. LXMF permet même des « messages papier » encodés en QR code ou en lien, transportables physiquement.

### 6.2 LXST : la voix en temps réel

**LXST** est le protocole et le framework de transport audio et de signaux en temps réel au-dessus de Reticulum. Il alimente les appels vocaux de Sideband et inclut rnphone, un utilitaire de téléphonie en ligne de commande capable aussi de piloter de vrais combinés téléphoniques matériels. Les codecs utilisés s’adaptent à la bande passante disponible, mais une conversation fluide demande évidemment plus de débit qu’un message texte : sur LoRa, il faut des réglages radio rapides et des liaisons courtes.

### 6.3 Les applications utilisateur

| **Application**        | **Description**                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `Sideband`             | Client graphique de référence (Android, Linux, macOS, Windows) : messagerie, fichiers, messages vocaux, appels, télémétrie, cartes, plugins |
| `Nomad Network`        | Client en mode terminal : messagerie et pages hébergées sur des nœuds (langage de balisage Micron), une sorte de « web » hors Internet      |
| `MeshChat / MeshChatX` | Client LXMF avec interface web, messages vocaux et fichiers ; MeshChatX est un fork qui vise à tout réunir (Reticulum, LXMF, LXST)          |
| `Columba`              | Client Android natif récent, avec messages vocaux et historique d’appels                                                                    |
| `rnsh`                 | Shell distant interactif                                                                                                                    |

### 6.4 Implémentations alternatives

L’implémentation Python reste la référence, mais plusieurs réimplémentations compatibles au niveau protocole sont apparues, souvent pour gagner en performance ou viser l’embarqué : **Reticulum-Go** (Go, avec une cible WebAssembly pour le navigateur), des implémentations en **Rust** (par exemple Leviculum, compatible avec les outils Python et visant aussi les microcontrôleurs nRF), et une pile Kotlin expérimentale utilisée en option par Columba. Leur maturité varie ; pour un premier déploiement, la version Python reste le choix le plus sûr.

## 7. Démarrer en pratique

### 7.1 Installation

```shell
pip install rns # ou : pipx install rns
rnsd # premier lancement : crée ~/.reticulum/config
rnstatus # vérifier les interfaces actives
```

Au premier lancement, la configuration par défaut active l’**AutoInterface** : deux machines sur le même réseau local se trouvent donc automatiquement, sans rien régler.

### 7.2 Exemple de configuration

Extrait de `~/.reticulum/config` combinant le réseau local, un lien Internet vers un nœud distant et une radio LoRa :

```ini
[reticulum]
enable_transport = Yes

[interfaces]

[[Reseau local]]
type = AutoInterface
enabled = yes

[[Lien Internet]]
type = TCPClientInterface
enabled = yes
target_host = noeud.exemple.org
target_port = 4242

[[Radio LoRa]]
type = RNodeInterface
enabled = yes
port = /dev/ttyUSB0
frequency = 868000000
bandwidth = 125000
txpower = 14
spreadingfactor = 8
codingrate = 5
```

### 7.3 Premiers usages

Dans les commandes suivantes, remplace `<hash_destination>` et `<hash>` par les valeurs correspondantes, sans les chevrons.

```shell
rnid -g ~/.reticulum/mon_id # générer une identité
rncp -l # écouter pour recevoir des fichiers
rncp rapport.pdf <hash_destination> # envoyer un fichier
rnx <hash_destination> "uptime" # exécuter une commande à distance
rnprobe rnstransport.probe <hash> # tester l’accessibilité
```

Pour la messagerie, le plus simple est d’installer **Sideband** ou **MeshChat** sur deux appareils et d’échanger les adresses LXMF (affichées sous forme de hachage ou de QR code).

## 8. Comparaison avec d’autres approches

| **Critère**           | **Reticulum**                       | **Meshtastic**                       | **Yggdrasil / cjdns**       |
| --------------------- | ----------------------------------- | ------------------------------------ | --------------------------- |
| Nature                | Pile réseau complète, multi-support | Messagerie LoRa intégrée au firmware | Réseau maillé IPv6 chiffré  |
| Supports              | Tout (LoRa, IP, série, radio, I2P…) | Principalement LoRa (+ MQTT/IP)      | IP uniquement               |
| Débits très bas       | Conçu pour                          | Conçu pour                           | Non adapté                  |
| Fichiers, voix, shell | Oui                                 | Très limité                          | Oui (via IP classique)      |
| Identité / adressage  | Clés, sans adresse source           | Identifiant de nœud                  | Adresse IPv6 dérivée de clé |
| Prise en main         | Moyenne                             | Très simple                          | Moyenne                     |

Meshtastic et Reticulum sont souvent comparés parce qu’ils utilisent le même type de matériel LoRa, mais ils ne jouent pas dans la même catégorie : Meshtastic est un produit de messagerie simple et populaire, Reticulum une fondation réseau généraliste sur laquelle on construit des applications. Les deux ne sont pas interopérables nativement.

## 9. Limites et points de vigilance

-   **Réglementation radio** : le chiffrement est interdit sur les bandes radioamateur dans la plupart des pays, ce qui limite l’usage de Reticulum chiffré sur ces fréquences. Sur les bandes ISM LoRa en Europe (863-870 MHz), les règles de rapport cyclique (souvent 1 %, parfois 10 % selon la sous-bande) et de puissance maximale s’appliquent et limitent fortement le trafic utile.
-   **Débit** : la voix et les gros fichiers fonctionnent bien sur WiFi ou Ethernet, mais sur LoRa il faut rester réaliste. Envoyer une photo peut prendre plusieurs minutes, et une conversation vocale suppose des paramètres radio rapides et des liaisons courtes.
-   **Performance de l’implémentation** : écrite en Python, la référence est moins performante qu’une pile native sur du matériel modeste ou pour des nœuds à fort trafic, d’où l’intérêt des réimplémentations Go et Rust.
-   **Sécurité** : primitives solides et conception soignée, mais pas d’audit indépendant publié à notre connaissance, et une base d’utilisateurs encore modeste.
-   **Licence** : l’implémentation de référence est publiée sous la « Reticulum License », dérivée d’une licence permissive mais avec des restrictions d’usage (par exemple pour les systèmes conçus pour nuire à des personnes). Ce n’est donc pas une licence open source au sens strict de l’OSI ; à vérifier avant tout usage commercial ou institutionnel.
-   **Communauté et documentation** : la documentation officielle est très complète, mais l’écosystème reste porté par un nombre restreint de contributeurs, avec un rythme de développement qui dépend fortement de son créateur.

## 10. Cas d’usage typiques

-   **Communications de secours** lors de catastrophes ou de coupures d’Internet et du réseau mobile.
-   **Zones isolées** : refuges, exploitations agricoles, expéditions, bateaux, chantiers, où l’on veut relier quelques sites sans abonnement.
-   **Résistance à la censure et vie privée** : réseaux communautaires indépendants des opérateurs, absence d’adresses source, transport possible via I2P.
-   **Télémétrie et IoT** : remontée de capteurs sur de longues distances avec des liens très sobres.
-   **Administration à distance** de machines hors réseau via rnsh ou rnx à travers une liaison radio.
-   **Expérimentation** pour radioamateurs, hackers et chercheurs en réseaux, grâce à l’interface Pipe qui permet d’inventer de nouveaux transports.

## 11. Pour aller plus loin

Le **manuel officiel** (markqvist.github.io/Reticulum/manual) est la référence : il détaille le protocole, la configuration de toutes les interfaces et l’API Python. Le dépôt GitHub markqvist/Reticulum héberge le code, le journal des versions et les discussions de la communauté. Les dépôts markqvist/LXMF, markqvist/LXST, markqvist/Sideband et markqvist/NomadNet couvrent les principales applications, et markqvist/RNode_Firmware le micrologiciel radio.

### En résumé

{{< alert icon="lightbulb" >}}
Reticulum est une pile réseau sobre, chiffrée par conception et indifférente au support physique.
Sa force est de rendre possibles fichiers, voix, messagerie et shell distant sur des réseaux que l’on peut monter soi-même, sans Internet ni opérateur. Ses limites sont surtout physiques (débit des radios, réglementation) et liées à la jeunesse relative de son écosystème.
{{< /alert >}}
