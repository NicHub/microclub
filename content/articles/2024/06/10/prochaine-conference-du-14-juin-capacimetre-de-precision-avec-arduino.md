---
title: "Prochaine conférence du 14 juin : Capacimètre de précision avec Arduino par Jean-Pierre Broillet"
date: "2024-06-10T20:08:32"
lastmod: "2024-06-10T20:09:40"
author: "franic"
categories: ["Microclub"]
tags: ["arduino", "hardware"]
url: "/2024/06/10/prochaine-conference-du-14-juin-capacimetre-de-precision-avec-arduino/"
wordpress_id: 5396
comment_count: 0
---
# Mesure de capacité avec la méthode de la constante de temps

La méthode de la constante de temps est une technique courante pour mesurer la capacité d’un

condensateur. Elle repose sur le principe de charge et de décharge du condensateur dans un

circuit RC (résistance-condensateur).

## Principe de la méthode

1. Charger le condensateur: On connecte le condensateur à une source de tension constante U0 pendant un temps suffisamment long pour qu’il se charge complètement. La tension à ses bornes atteint alors U0.
2. Décharger le condensateur: On déconnecte la source de tension et on relie le condensateur à une résistance R. Le condensateur se décharge alors graduellement à travers la résistance.
3. Mesure de la tension: On mesure la tension aux bornes du condensateur en fonction du temps pendant la décharge.

La tension aux bornes du condensateur suit une loi exponentielle décroissante décrite

par la formule:

U(t) = U0 \* exp(-t / RC)

où:

- U(t) est la tension aux bornes du condensateur au temps t
- U0 est la tension initiale du condensateur (tension de charge)
- R est la résistance du circuit
- C est la capacité du condensateur
- τ = RC est la constante de temps du circuit

## Avantages de la méthode

- La méthode de la constante de temps est une technique simple et peu coûteuse à mettre en œuvre.
- Elle permet de mesurer une large gamme de valeurs de capacité.
- Elle est relativement précise si les mesures de tension et de temps sont effectuées avec soin.

## Inconvénients de la méthode

- La méthode de la constante de temps n’est pas très précise pour les faibles valeurs de capacité.
- La mesure de la constante de temps peut être affectée par les parasites du circuit.
- La méthode ne permet pas de mesurer directement la capacité d’un condensateur polarisé.

La méthode de la constante de temps est une méthode utile pour mesurer la capacité d’un condensateur. Elle est simple, peu coûteuse et relativement précise. Cependant, il est

# Mesure de capacité avec la méthode de la charge à courant constant

La méthode de la charge à courant constant est une autre technique courante pour mesurer la capacité d’un condensateur. Elle repose sur le principe de la mesure du temps nécessaire pour charger un condensateur à une tension donnée à l’aide d’un courant constant.

## Principe de la méthode

1. Charger le condensateur: On connecte le condensateur à une source de courant constant I et on mesure la tension à ses bornes en fonction du temps.
2. Calcul de la capacité: La capacité du condensateur C est calculée à l’aide de la formule suivante:

C = I \* t / U

où:

- I est le courant de charge constant
- t est le temps nécessaire pour que la tension aux bornes du condensateur atteigne une valeur U donnée
- U est la tension finale aux bornes du condensateur

## Avantages de la méthode

- La méthode de la charge à courant constant est une technique simple et directe à mettre en œuvre.
- Elle permet de mesurer une large gamme de valeurs de capacité.
- Elle est relativement précise si les mesures de courant, de tension et de temps sont effectuées avec soin.

## Inconvénients de la méthode

- La méthode de la charge à courant constant nécessite une source de courant constant stable.
- La mesure de la tension peut être affectée par les parasites du circuit.
- La méthode ne permet pas de mesurer directement la capacité d’un condensateur polarisé.

C = I \* t / U = 1 mA \* 2 s / 10 V = 0,2 μF

## Conclusion

La méthode de la charge à courant constant est une méthode efficace pour mesurer la capacité

d’un condensateur. Elle est simple, directe et relativement précise. Cependant, il est important

de disposer d’une source de courant constant stable et de prendre en compte les parasites du

circuit lors de la mesure de la tension.

# Mesure d’une capacité avec un détecteur de phase

La mesure d’une capacité avec un détecteur de phase est une méthode indirecte qui repose sur la comparaison du déphasage entre un signal de référence et un signal mesuré. Le principe est le suivant :

1. Un signal de référence sinusoïdal de fréquence f est appliqué à une résistance R et à la capacité C à mesurer.
2. Le courant dans le circuit est mesuré et un signal proportionnel est créé. Ce signal est déphasé par rapport au signal de référence d’un angle φ qui dépend de la valeur de C et de R.
3. Le déphasage φ est mesuré à l’aide d’un détecteur de phase. Ce détecteur compare le signal de référence et le signal mesuré et produit un signal de sortie proportionnel à leur différence de phase.
4. La valeur de la capacité C peut être calculée à partir du déphasage φ mesuré, de la fréquence f et de la résistance R en utilisant la formule suivante :

C = 1 / (2πfRZ tan(φ))

## Avantages de la méthode du détecteur de phase

- Haute précision: Cette méthode permet de mesurer des capacités avec une grande précision, même pour les valeurs de capacité très faibles.
- Large plage de mesure: La méthode peut être utilisée pour mesurer une large gamme de valeurs de capacité, de quelques picofarads à plusieurs microfarads.
- Bonne immunité au bruit: La méthode est relativement peu sensible au bruit ambiant, ce qui la rend adaptée aux mesures en environnements bruyants.

## Inconvénients de la méthode du détecteur de phase

- Complexité: La mise en œuvre d’un circuit de mesure basé sur un détecteur de phase peut être plus complexe que d’autres méthodes de mesure de capacité.
- Coût: Les détecteurs de phase peuvent être des composants électroniques relativement coûteux.

## Commentaires <!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
