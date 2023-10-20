# helena_haffner_books_online_P2_06102023
Environnement Virtuel utilisé : Poetry

Installation: curl -sSL https://install.python-poetry.org | python3 -

Activer l'environnement virtuel : poetry shell

Installer les dépendances : poetry install  (les fichiers pyproject.toml ou poetry.lock doivent être présents dans le dossier et qui sont l'équivalent de requirements.txt)

Script servant à récupérer les informations de chaque livres présents sur le site https://books.toscrape.com/index.html afin de les ajouter à un csv en fonction de la catégorie à laquelle appartient le livre.
Ce ou ces exports sont créés dans le dossier ouptuts/csv/catégorie/.
En plus des informations textuelles, les couvertures sont également téléchargées dans le dossier outputs/img/catégorie/.
Le script est capable de déterminer si l'url donnée est celle de l'accueil, d'une catégorie spécifique ou encore celle d'un livre en particulier et s'adaptera donc en fonction.

Ainsi, avec l'URL de la page d'accueil, le script va parcourir chaque catégorie et, pour chacune d'elle, extraire les informations demandées pour chaque livre.
Si l'URL utilisé est celle d'une catégorie, le script récupérera uniquement les informations des livres de cette catégorie précise.
ENfin, si l'URL renvoit sur la page d'un livre particulier, seules les informations de ce livre seront récupérées exportées.

Pour lancer le programme, allez dans le dossier du projet puis, dans un terminal, utilisez la commande python3 main.py.
Pour l'heure, aucune interface ne permet de donner directement au script une URL, il faudra donc aller sur la page main.py et changer l'url des variables ou en l'ajoutant directement comme argument de la fonction scrap_datas(argument).

L'environnement virtuel utilisé pour ce projet est Poetry.

Ce projet s'inscrit dans le cadre d'une formation Python et vise un site destiné à apprendre la récupération d'informations sur internet.



