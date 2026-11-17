# SÉNARIO DE DÉMO

Lis les instructions de AGENTS.md.

Affiche l’heure actuelle et mémorise-la sous le nom T1 pour que je puisse te la redemander plus tard dans cette conversation.

Dans le navigateur intégré, affiche la page P1 :
https://microclub.ch/2026/11/17/amelioration-du-simulateur-de-radiosonde-rs41-a-laide-de-antigravity-et-gemini/

Démarre le serveur Hugo avec la commande suivante et récupère l’URL de prévisualisation affichée par le script.
scripts/preview-mac.command --openBrowser=false

Affiche le rendu du serveur Hugo dans le navigateur interne.

À partir de P1, convertis l’article en une page Hugo, sans me poser de questions.

Affiche l’article sur le serveur Hugo local dans le navigateur intégré.

À la fin, indique le chemin du fichier créé, le résultat du build et l’URL locale affichée.

Arrête le serveur Hugo local.

Crée un commit Git décrivant clairement la modification, puis pousse-le vers le dépôt distant avec git push.

Dans le navigateur intégré, affiche :
https://github.com/NicHub/microclub/actions

Attends et vérifie régulièrement que le workflow correspondant au commit vient de se terminer. Ne considère pas le build comme terminé uniquement parce que la page est chargée. Si le build échoue, arrête la procédure et signale l’échec.

Lorsque le build est terminé avec succès, affiche dans le navigateur intégré l’article publié sur :
https://nichub.github.io/microclub/

Affiche l’heure actuelle, l’heure T1 et la différence entre les deux.