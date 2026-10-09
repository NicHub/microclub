---
title: "Python et les objets statiques"
date: "2014-01-26T16:38:23"
lastmod: "2015-04-24T23:21:10"
author: "Rolf Ziegler"
categories: ["Microclub"]
tags: ["embarque", "initiation", "programmation", "python"]
url: "/2014/01/26/python-et-les-objets-statiques/"
wordpress_id: 1408
comment_count: 1
---

## Les variables statiques

En C/C++, il est l’usage d’avoir des variables statiques, c’est-à-dire non-dynamiques, pour le comptage d’objets ou pour des flags en code embarqué, ou l’on évite comme la peste les new et delete. C’est intégré au langage, avec le mot clef ‘static’, au cas où la définition globale – hors des accolades – n’y suffit pas. Une variable statique est aussi privée au module, afin de réduire sa visibilité.

Déclarer une variable static revient à lui donner une adresse mémoire définitive. Au niveau du module, on le comprend aisément. C’est plus surprenant dans une fonction : on la retrouve inchangée depuis le dernier appel – a moins bien sûr que la fonction en question ne la modifie ! Cette persistance est valable même si elle est déclarée à l’intérieur d’un objet alloué dynamiquement. Mais en Python, comment reproduire ce comportement ?

Petite digression : dans ce texte, j’utilise souvent le mot fonction par habitude, alors que la terminologie Python est : method.

A priori, « static » va l’encontre de la programmation orientée objet… Mais parfois, on aimerait un objet unique, a dispo de manière globale, déclaré et initialisé au niveau du module. Il serait ‘objet’ pour la beauté de la pensée, donc de la programmation, plutôt qu’un fatras de variables globales ; même si elles sont utilisées au niveau du module. Cet objet serai statique parce que l’instancier ne fait que de compliquer le code, voire de prendre le risque de dédoubler l’objet par mégarde alors qu’il doit être unique.

C’est un peu tordu : si un objet n’est pas instancié… il doit être un peu instancié quand même, puisque par définition, une variable statique doit exister au moment où le programme tourne. Les exemples de codes sont entrés au niveau de la console Python ; ici en version 2.7.2, dans l’environnement (gratuit) PyCharm Community : <http://www.jetbrains.com/pycharm/>

## Variable de classe statique

Bien. Mais comment, en Python,  reproduire ce qu’on sait si bien faire en C/C++ ?

Python permet la définition de variables statiques tout court si, hors d’une classe, définie au niveau du module; et dans un objet, si défini  hors des fonctions de la classe. On s’intéresse à cette possibilité. Dans un tel cas, elle est accédée par le nom de la classe.

[![1-con-Static](/media/2014/01/1-con-Static.jpg)](/media/2014/01/1-con-Static.jpg)

A priori, ça fonctionne fort bien ! En utilisant la classe de base, soit Toto – avec la majuscule qui symbolise la déclaration de classe – l’attribut ‘a’ de classe est accessible et modifiable. C’est pratique, et on peut toujours instancier la classe normalement, p. exemple dans la variable x :

[![1-con-Static-instance](/media/2014/01/1-con-Static-instance.jpg)](/media/2014/01/1-con-Static-instance.jpg)

Ha. Hem… Ça donne 4, on attendait un 6. L’attribut ‘a’ de la classe reste donc inchangé ; de plus c’est cette valeur (donc : 4) qui serait utilisée à la prochaine instanciation (par exemple : y = Toto() ). On peut donc compter des objets, par exemple. Par contre, dès qu’on touche à la variable (de même nom) d’une instance, celle-ci devient indépendante et suit la dynamique de l’instance.

En prime, (c’est Python tout craché, ça!) on peut toujours ajouter une variable au vol à la classe de base :

[![1-con-Static-add_var](/media/2014/01/1-con-Static-add_var.jpg)](/media/2014/01/1-con-Static-add_var.jpg)

On la retrouve dans les objets précédemment instanciés, qui se rabattent sur la classe de base pour l’afficher. Bien entendu, on peut modifier l’instance x ou y, sans que cela touche la classe de base, pour à nouveau, avoir une variable d’instance propre et indépendante.

## Les fonctions et le statique (@staticmethod)

Mais pour les fonctions ? Ça ne marche pas si bien :

[![20-fonction](/media/2014/01/20-fonction.jpg)](/media/2014/01/20-fonction.jpg)

Python pas content… On beau essayer de passer la classe de base par Toto.prn(Toto), seule une version **instanciée** de Toto() fonctionne, comme le montre l’essai avec x. Sinon, on obtient l’erreur « unbound method prn() … »

Donc, on doit avoir une **instance** pour que la fonction… fonctionne. On peut toutefois forcer Python à intégrer la fonction dans la classe de base. L’astuce est de la précéder de la ligne : @classmethod. La fonction reçoit en paramètre classiquement sa propre self-référence. Et là :

[![2-fonction_staticmethod](/media/2014/01/2-fonction_staticmethod.jpg)](/media/2014/01/2-fonction_staticmethod.jpg)

On y arrive ! OK pour le statique. Avec une instance, ça se gâte :

[![22-fonction_staticmethod_x](/media/2014/01/22-fonction_staticmethod_x.jpg)](/media/2014/01/22-fonction_staticmethod_x.jpg)

On doit donner comme paramètre d’appel de fontion le nom de l’instance, alors qu’avec une classe « classique », si j’ose dire, c’est implicite. Pas terrible comme écriture de code, un peu verbeux à mon goût. Autre solution, c’est de virer l’argument, et de coder :

```py
def prn() :
    print Toto.a
```

On en revient à une méthode de module, écrite hors de la définition de classe…

## Fonction de classe de base (@classmethod)

Un autre décorateur, @classmethod, permet de lier la fonction à la classe:

[![2-fonction_classmethod_x](/media/2014/01/2-fonction_classmethod_x.jpg)](/media/2014/01/2-fonction_classmethod_x.jpg)

Elle reçoit comme 1\<sup\>er\</sup\> paramètre non pas l’instance, mais la classe de base. Elle convient parfaitement pour compter les objets. L’écriture du code est plus claire.

Cependant, une variable instanciée ne sera pas à sa portée, et peut pousser à la faute… On ne peut pas tout avoir.

## En résumé

Pour obtenir un objet statique en Python, il faut :

-   mettre les variables après la déclaration de la classe, avant les méthodes.
-   les méthodes doivent être précédées du décorateur @classmethod

Précaution : ne pas instancier cet objet dynamiquement. On peut carrément afficher un message d’erreur avec la fonction \_\_init\_\_(), pour en informer l’utilisateur.

Yves Masur (1/2014)

## Références

<http://fr.wikibooks.org/wiki/Programmation_C/Classe_de_stockage>

<http://stackoverflow.com/questions/68645/static-class-variables-in-python>

<http://stackoverflow.com/questions/735975/static-methods-in-python>

<http://docs.python.org/2/library/functions.html?highlight=decorator>

## Commentaires

### Yves Masur — 9 février 2014 à 21:42

Un lecteur me signale : « J’ai relevé une confusion, paragraphe Variable de classe statique\
Dans cet exemple, ce n’est pas une variable d’instance justement mais un attribut de classe. »

Dans le livre « Apprenez à programmer en Python » de Vincent Legoff, p. 175, on parle d’attributs. Dans le livre « Rapid Gui programming with Python and QT », page 75, il est dit: Variable that belong to a specific instance are called ‘attributes’ or ‘instance variable . Dans celui de Tarek Ziadé, « Python – petit guide à l’usage du développeur agile », p 53, il est dit: »… \[le constructeur\] se charge ensuite d’initialiser les variables de l’objet, ou attribut ». Pour finir, dans l’ouvrage « Python – fondamentaux du langage » de Mathieu Bruchez, p. 56 et 57 parle autant d’attribut que de variable de classe et variable d’instance.\
Visiblement, les deux terminologies existent côte à côte.On peut donc admettre que les deux sont correctes; ou du moins utilisées comme telles dans la littérature.\
Ce qui serait plus clair serait: **attribut** si définit dans la classe de base; **variable** pour les objets instanciés.

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
