---
title: "Le chiffre de Kaprekar"
date: "2025-03-20T18:47:16"
lastmod: "2025-03-20T19:41:45"
author: "Jean-Pierre Broillet"
categories: ["Microclub"]
tags: []
url: "/2025/03/20/le-chiffrede-kaprekar/"
wordpress_id: 5472
comment_count: 0
---
<figure><img alt="" height="417" src="/media/2025/03/word-image-5472-1.jpeg" width="597"/></figure>
<p></p>
<p><strong>Pour aller plus loin avec les microcontrôleurs tels que, Arduino et AVR connexes, il est indispensable de posséder de bonnes bases du langage C++.</strong>
</p>
<p><strong>Ainsi, une fois n’est pas coutume, je vous propose le petit programme ci-joint, qui est la traduction en C++ d’une curiosité mathématique découverte lors d’un voyage dans le labyrinthe de la toile …</strong>
</p>
<p><strong>L’algorithme de Kaprekar</strong>
</p>
<p>
  En préambule, quelques mots sur ce monsieur Kaprekar.
</p>
<p>
  Dattatreya Ramachandra Kaprekar est un mathématicien indien connu pour ses recherches sur la notion de nombre de Kaprekar ainsi que l’algorithme de Kaprekar. Boudé par ses contemporains, ses travaux seraient passés inaperçus s’ils n’avaient pas été relayés par Martin Gardner, spécialiste de mathématiques récréatives.
</p>
<p>
  L’algorithme de Kaprekar est un processus qui transforme un nombre entier en un autre nombre entier.
</p>
<p>
  Il fonctionne de la façon suivante : soit N (ici 4 chiffres) un nombre entier. Soit Nd le nombre obtenu en rangeant les chiffres de N dans l’ordre décroissant, et Nc le nombre obtenu en les rangeant dans l’ordre croissant. L’Algorithme de Kaprekar retourne alors le nombre Nd – Nc. On réitère le processus plusieurs fois jusqu’à obtenir toujours le même nombre…Soit <strong>6174</strong>
</p>
<p>
  Combien d’itérations sont-elles nécessaires, si on part d’un nombre à quatre chiffres ? Quels sont les résultats intermédiaires ?
</p>
<p>
  C’est ce que je vous propose avec ce petit programme, très documenté, écrit en C++ d’après un canevas trouvé sur le net.
</p>
<p>Attention, tous les nombres divisibles par 1111 ne fonctionnent pas, évidemment. </p>
<p>
  J’apprécierais beaucoup si quelqu’un pouvait coder cet algorithme en Python ou en un autre langage.
</p>
<pre><code>/* Programme C++ pour trouver le nombre d'itérations de la routine pour atteindre 6174 (constante de Kaprekar). 

  Ce programme retourne une erreur pour les entrées non valides (par exemple les nombres divisibles par 1111*/

#include &lt;bits/stdc++.h&gt;

using namespace std;

int cnt = 0; //compteur d'itérations

// Test de la validité du nombre entré

bool estValide(string &amp; nombre, int &amp; n)

{

  // Stocke chaque chiffre dans un ensemble

  unordered_set &lt; char &gt; freq;
  for (int i = 0; i &lt; n; i++) freq.insert(nombre[i]);

  // Return false si tous les chiffres sont les mêmes sinon true

  return freq.size() &gt;= 2 ? 1 : 0;

}

int Kaprekar_Cste(string nombre, int n)

{

  // Lorsque le longeur du nombre est supérieure à 4, ou que le nombre possède 4 chiffres, mais identiques

  if ((!estValide(nombre, n) || n &gt; 4) &amp;&amp; cnt == 0)

  {

    cout &lt;&lt; "Le nombre choisi est invalide" &lt;&lt; endl;

    return -1;

  } else

  {

    if (stoi(nombre) == 6174) //convertit le string en un entier

    {

      return cnt; //retourne le nombre d'itérations

    }

  }

  // Compte le nombre d'itérations cnt++;

  // Si le nombre entré possède moins de 4 caractères, on insère un 0 tout à gauche

  while (n++ &lt; 4) nombre.insert(0, "0");
  string nombre2 = nombre;

  // Fabrication du plus petit nombre (ascendant 1 2 3 4 5) et du plus grand nombre(descendant 5 4 3 2 1)

  sort(nombre.begin(), nombre.end()); //ordre ascendant

  sort(nombre2.begin(), nombre2.end(), greater &lt; int &gt; ()); //ordre descendant

  // Conversion string en integer

  int increasing = stoi(nombre); //difficile de trouver un terme simple en français

  int decreasing = stoi(nombre2);

  // Soustraction du plus grand nombre moins le plus petit 
  string res_soust = to_string(abs(increasing - decreasing)); cout&lt;&lt;"ressoust = "&lt;&lt;res_soust&lt;&lt;endl;

  // Si la valeur 6174 n'est pas atteinte on réitère le processus, sinon on stoppe le processus

  return Kaprekar_Cste(res_soust, res_soust.length());

}

// Nombre à traiter

int main()

{

  string nombre;

  cout &lt;&lt; "Choisissez un nombre de 4 chiffres" &lt;&lt; endl;

  cin &gt;&gt; nombre;

  cout &lt;&lt; "le nombre choisi est " &lt;&lt; nombre &lt;&lt; endl;

  int n = nombre.length();

  // Appel de la fonction Kaprekar_Cste Kaprekar_Cste(nombre, n);

  cout &lt;&lt; "le nombre d'iterations necessaires pour atteindre 6174 est de " &lt;&lt; cnt &lt;&lt; endl;

  return 0;

}</code></pre>
<figure><img alt="" height="247" src="/media/2025/03/word-image-5472-2.png" width="580"/></figure>
<p></p>
<p>
  Jean-Pierre Broillet Microclub 2024
</p>

## Commentaires

<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->
