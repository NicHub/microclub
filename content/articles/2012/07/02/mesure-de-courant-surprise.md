---
title: "Mesure de courant – surprise"
date: "2012-07-02T20:49:28"
lastmod: "2015-04-24T23:21:11"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["electronique", "energie", "initiation", "mesure"]
url: "/2012/07/02/mesure-de-courant-surprise/"
wordpress_id: 803
comment_count: 0
---
<h1>Conversion I -&gt; U</h1>
<p>Comme j’ai souvent besoin de conversion I-&gt;U, je me suis mis à construire un module ayant comme caractéristiques:</p>
<ul>
<li>Mesure du courant AC sur le 230 VAC, 0..1 A</li>
<li>Galvaniquement isolé</li>
<li>Fonctionne avec une alimentation 5VDC</li>
</ul>
<p>Ceux qui ont lu le projet « barrette » savent que j’en ai déjà fait un. Mais peu précis, et demandant une résistance « shunt » de 1 ohm. C’est plus professionnel d’utiliser une bobine de mesure, tel qu’on trouve par exemple chez Boxtec: <a href="http://shop.boxtec.ch/product_info.php/cPath/39_75/products_id/40267http://" target="_blank" title="sonde 30A">http://shop.boxtec.ch/product_info.php/cPath/39_75/products_id/40267</a></p>
<p><a href="/media/2012/07/bobine_de_mesure_I.jpg"><img alt="" height="225" src="/media/2012/07/bobine_de_mesure_I-300x225.jpg" title="bobine_de_mesure_I" width="300"/></a></p>
<p>Mais comment la connecter à une carte CPU pourvue d’un A/D, afin d’en faire la conversion? La méthode la plus expéditive est de connecter la bobine de mesure à un point milieu, soit 2,5V et de tout faire par soft en mesurant divers points rapprochés pour connaître la tension, image du courant. Cependant, cette méthode (super-flemmarde) a des inconvénient rédhibitoires:</p>
<ul>
<li>Faible sensibilité</li>
<li>Danger de casse du CPU en cas d’impulsion (dépasse +5V ou 0V)</li>
<li>Mange plein de ressource en T réel</li>
</ul>
<p>En effet, il faut échantillonner à 1 milliseconde, voir plus rapidement et chercher le min et le max de la sinusoïde – si c’en est une!</p>
<p>L’autre solution, c’est avec un montage ampli + redresseur. On peut ajuster la sensibilité parfaitement à nos besoins, et filtrer par un simple RC pour procéder à la mesure au besoin. Encore faut-il un bon schéma. Il y en a de bonne qualité ici: <a href="http://sound.westhost.com/appnotes/an001.htm" target="_blank" title="precision rectifier">http://sound.westhost.com/appnotes/an001.htm</a>. Je m’en suis inspiré pour faire le mien, le schéma est mis à la fin de l’article, ainsi qu’une discussion des améliorations possibles.</p>
<p>A la sortie, on doit retrouver des arches de sinusoïdes à filtrer. Par rapport à la tension de crête, on aura la tension moyenne, soit un facteur de 2/∏, au lieu de √2/2. Le rapport entre les deux est de : 0.9003. Voici leur allure, avec une charge de 70W, vu sur un oscilloscope analogique Tektronix T922; sensibilité Y: 200 mV/division, vitesse X: 2 ms/division.</p>
<p><a href="/media/2012/06/70W.jpg"><img alt="" height="150" src="/media/2012/06/70W-150x150.jpg" title="70W" width="150"/></a> Maintenant, si le filtre passe-bas est constitué d’un condensateur pas trop chargé résistivement, ici par 1KΩ R7 (voir  le schéma ci après), on peut obtenir la tension de crête. Cette solution n’est pas adéquate, lorsque la consommation n’a pas une forme sinusoidale! En effet, la plupart (et de plus en plus) des consommateurs font du hachage électronique qui sont fort loin de la gentille consommation résistive.</p>
<p>Mais tout d’abord, voyons ce qui se passe à plus faible puissance, avec une ampoule de 25W. C’est cette grandeur d’amplitude qui m’intéresse, afin de pouvoir déclencher des consommateurs en stand-by.</p>
<p><a href="/media/2012/06/25W.jpg"><img alt="" height="150" src="/media/2012/06/25W-150x150.jpg" title="25W" width="150"/></a> Certes, le signal (mesuré toujours avec la même sensibilité de 200 mV/div. sur l’axe Y) est plus petit, mais on y voit aussi un peu de déformation. C’est grave? ça dépend de l’utilité du montage. Normalement, il ne devrait pas y avoir de « plat » vers le 0V.</p>
<p>Dans le montage proposé ci-dessous, l’un des AOPs est en amplification, l’autre en saturation, sa sortie à 0V pour une demi-alternance. Il met malheureusement environ 1 milliseconde pour désaturer et « coller » à l’arche du sinus. C’est un petit retard, mais sur un signal de 10 ms (soit une demi période de 20 ms, 50Hz du réseau…), ça se voit. Et les mesures le reflètent.</p>
<p>Le plat inférieur peut également provenir du filtrage, mal adapté. Voici l’ampoule de 70W avec une sortie peu chargée (la résistance R7 – 1 KΩ est retirée), le DC monte à approximativement à 400 mV de la tension de crête. Valeur nécessaire à la conduction de la diode.<a href="/media/2012/06/70W-pic.jpg"><img alt="" height="150" src="/media/2012/06/70W-pic-150x150.jpg" title="70W-pic" width="150"/></a></p>
<p>Et voici l’image de courant d’une lampe économique à tube fluorescent de 15W:</p>
<p><a href="/media/2012/06/15W-tube.jpg"><img alt="" height="150" src="/media/2012/06/15W-tube-150x150.jpg" title="15W-tube" width="150"/></a>Les pics de courant n’ont rien à voir avec une sinusoïde. En en prenant la valeur moyenne, on ne sera pas trop loin de la valeur efficace consommée sur le secteur. A titre indicatif, un module LED de puissance est encore pire: c’est quasiment une sorte de parasite qui est présenté.</p>
<p>Pour bien suivre le courant, il faut que la bobine aie une bande passante large et que la sortie du redresseur (que je n’ose qualifier de parfait) au point B soit chargée par une résistance faible par rapport à la charge présentée par le filtrage (ici 22 KΩ R8) et l’entrée de lecture de tension du CPU, qui est heureusement classiquement d’impédance élevée.</p>
<p><a href="/media/2012/06/osc-HF.jpg"><img alt="" height="150" src="/media/2012/06/osc-HF-150x150.jpg" title="osc-HF" width="150"/></a>L’AOP, sur le montage d’essai, n’est pas stable. On voit ci-dessous, que sans une capacité dans la contre réaction, il oscille joyeusement. Je l’ai enlevée sur un des demi-montages, c’est pourquoi une seule arche montre une trace épaisse, signe d’oscillation HF. Par contre, ça n’affecte que peu les mesures. Ce n’est pas étonnant, vu que la tension est moyennée. Mais comme dans tout montage, on n’aime pas laisser de l’incertitude, le stabiliser est une bonne chose. Il est probable aussi, que sur un un circuit imprimé le comportement serait meilleur que sur la plaque d’essai « breadboard ».</p>
<h2>Tableau de mesure</h2>
<p>Le tableau complet est ici: <a href="/media/2012/06/mesure_I.pdf">mesure_I</a></p>
<p><a href="/media/2012/07/lin_I-U.jpg"><img alt="" height="300" src="/media/2012/07/lin_I-U-300x300.jpg" title="lin_I-U" width="300"/></a>Les mesures effectuées avec les charges suivants:</p>
<ul>
<li>A vide</li>
<li>ampoule « économique » 15W Osram</li>
<li>ampoule de 25 W Philips</li>
<li>ampoule de 40W Philips</li>
<li>ampoule de 70W Elec – Leuci, modèle utilisé pour la signalisation</li>
</ul>
<h2>Schéma</h2>
<p>Ce schéma est utilisé pour les mesures ci-dessus. L’impédance d’entrée Ze calculée est de 561Ω, le gain théorique GU est de 103.2. Les oscillogrammes sont pris au point B, la mesure de tension au point S1, avec un multimètre Metex 4 1/2 digits.</p>
<p><a href="/media/2012/06/schema_I-U.jpg"><img alt="" height="489" src="/media/2012/06/schema_I-U-1024x543.jpg" title="schema_I-U" width="922"/></a></p>
<h2>Description</h2>
<p>La bobine de mesure de courant L <em>mes</em> attaque une entrée symétrique, chargée par 390Ω. Des AOPs, en montage inverseur, redressent chacun une demi-alternance par les diodes  d1, d2. R7 sert de charge, les R8 et C4 filtrent le signal pour présenter la composante moyenne aux bornes S1, S2. Les condensateurs C1, C2 préservent la stabilité des AOPs. Le tout fonctionne en 5 VDC. Pour ce faire, l’AOP TS922 choisi travaille avec les entrées à la valeur de 0V, c’est un « rail-to-rail », soit capable de fonctionner avec sa sortie de -V alim jusqu’à +V alim, les entrées en mode commun idem. A titre indicatif, j’ai également testé l’AOP TLC972 de Texas Instrument, avec des résultats très proches; il sature en positif un peu plus rapidement que le TS922.</p>
<h2>Améliorations</h2>
<p>Puisque la sortie saturée ne semble pas être très appréciée de l’AOP, essayons de le faire fonctionner sans saturation. Une tentative d’amélioration de la linéarité a été faite en portant le point A (soit le commun de l’entrée et les références [+] des AOPs) à 0.74V par un diviseur 2.7KΩ et 470Ω; et l’ajout de deux diodes dans la contre réaction, soit entre les pattes 1; 2 et 7;6 de l’IC, la cathode connectée à la sortie. Ainsi, si la sortie s’approche de la saturation, la diode ajoutée tire l’entrée [-] contre 0V et empêche l’AOP de saturer. La tension en B qui devrait être au repos de 0.741V est mesurée à 0.675V, soit -66 mV d’écart. Avec 1 mV d’offset et un gain GU de 220, on peut avoir 220 mV d’erreur; c’est beaucoup! Mais cet IC est donné à 0.9 mV max pour sa déclinaison TS922A.</p>
<p>L’utilisation de diodes au germanium sont à proscrire! en effet, l’important courant de fuite en mode blocage de tension ruine tout espoir de précision. Pour D1 et D2, ça peut convenir et augmenter la plage de tension. Mieux vaudrai utiliser des diodes Schottky (pas testé).</p>
<p>La linéarité est un peu meilleure; visible dans ce tableau de résultats: <a href="/media/2012/07/mesure_I2.pdf">mesure_I2</a>.</p>
<p>L’offset de 0.675V est <strong>déjà soustrait</strong>. Le problème du retard à la dé-saturation de ~1ms est diminué, mais toujours présent. Le filtre passe-haut constitué par 220 K et 470 pF a une constante de 0.1 ms qui ne nous aide pas… Par contre, on peut tenir compte de l’offset de l’AOP dans une certaine mesure, en prenant comme valeur 0, la tension affichée avec un courant de mesure nul: dans notre cas, 0.675V</p>
<p>On remarquera que le gain de conversion en tension a varié, par rapport au montage en mode commun à 0V: 895 mV au lieu de 614 mV pour 0.295 A, charge de 70W!</p>
<p>Une analyse théorique primaire ne permet pas de prédire ce résultat: les AOPs ayant un gain important, seul le rapport de contre-réaction est déterminant. Par contre, par une analyse plus poussée, on voit que le schéma  d’origine souffre un peu de son impédance d’entrée <em>variable</em>. Admettons un signal en phase positive sur E1, négatif sur E2. En effet, lorsque l’AOP sature l’entrée [-] reçoit un signal positif; la résistance de 1K R3 est flottante et n’est plus en parallèle avec 390Ω R1. L’impédance augmente et le gain diminue.</p>
<p>Une autre piste d’amélioration: passer 10 fois le fil dont le courant I est mesuré dans la bobine, prévue on le rappelle pour 30A. La tension disponible supérieure permet de poser des résistances R3; R4 de 10KΩ au lieu de 1KΩ. On y gagne sur tous les tableaux: moins d’offset, moins de rupture d’impédance. En outre, le circuit s’avère plus stable, et les capacités C1, C2 peuvent être retirées!</p>
<p><a href="/media/2012/07/lin_I-U_10x.jpg"><img alt="" height="300" src="/media/2012/07/lin_I-U_10x-294x300.jpg" title="lin_I-U_10x" width="294"/></a> La linéarité du montage grimpe sérieusement; les résultats sont donnés ici: <a href="/media/2012/07/mesure_I_10x.pdf">mesure_I_10x</a>.</p>
<p>Par curiosité, j’ai ajouté la mesure avec une charge de 56 KΩ, ce qui en l’espèce représente une puissance de 1W, qui est raisonnablement mesurable. Avec un A/D de 10 bits, basé sur une référence de 5.000V pleine échelle, les pas sont de 4.88 mV. Or, la puissance de 1W dans ces conditions présente une tension de 13 mV. Il s’agit alors de soustraire l’offset qui est de même grandeur. On considèrera que c’est la résolution de ce montage.</p>
<h2>Conclusion</h2>
<p>Par un montage relativement simple, il est possible d’obtenir une bonne conversion AC/DC permettant la mesure de courants sur le secteur, tout en étant galvaniquement isolé, et en travaillant avec une seule alimentation de 5VDC. La précision dépend fortement de la configuration du montage et du bon choix de la sensibilité du domaine de travail. Si la possibilité existe, il vaut mieux obtenir une bonne sensibilité au départ plutôt que de recourir à de l’amplification démesurée, qui apporte de l’instabilité au montage et amplifie des défauts d’offset inhérents aux AOPs. Ceci parfaitement compatible avec un montage à microprocesseur. Je compte le coupler avec un Arduino.</p>
<p>Y. Masur (7/2012)</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
