# Projet de Système de Recommandation de Films

## Description

Ce projet consiste en un système de recommandation de films basé sur la similarité des évaluations d'utilisateurs. Le système utilise une approche de filtrage collaboratif pour recommander des films similaires à ceux que l'utilisateur a déjà évalués positivement.

## Dataset

Le dataset utilisé dans ce projet est le MovieLens 100K Dataset, qui contient 100 000 évaluations de films effectuées par 943 utilisateurs sur 1682 films. Vous pouvez télécharger le dataset à partir du lien suivant :

[MovieLens 100K Dataset](http://files.grouplens.org/datasets/movielens/ml-100k.zip)

## Simulation Streamlit

Le projet dispose d'une interface utilisateur créée avec Streamlit, qui permet à l'utilisateur de sélectionner un film et de recevoir des recommandations de films similaires. Vous pouvez accéder à la simulation Streamlit à partir du lien suivant :

[Simulation Streamlit](https://share.streamlit.io/your_username/your_app)

## Méthodologie

Le système de recommandation utilise une approche de filtrage collaboratif basée sur la similarité des évaluations d'utilisateurs. Les étapes de la méthodologie sont les suivantes :

1. Préparation des données : le dataset est nettoyé et transformé en une matrice d'évaluations d'utilisateurs.
2. Calcul de la similarité : la similarité entre les utilisateurs est calculée en utilisant la distance cosinus entre leurs vecteurs d'évaluation.
3. Recommandation de films : pour un utilisateur donné, le système recommande les films les plus similaires à ceux qu'il a déjà évalués positivement, en utilisant les k plus proches voisins.

## Évaluation

Pour évaluer les performances du système de recommandation, nous avons utilisé les métriques suivantes :

* Précision : pourcentage de films recommandés qui sont pertinents pour l'utilisateur.
* Rappel : pourcentage de films pertinents pour l'utilisateur qui ont été recommandés.
* F1-score : moyenne harmonique de la précision et du rappel.

Nous avons également utilisé des graphiques pour visualiser les performances du système de recommandation en fonction du nombre de voisins et du seuil de similarité.

## Conclusion

Dans l'ensemble, le système de recommandation de films a montré de bonnes performances dans la recommandation de films similaires à ceux que l'utilisateur a déjà évalués positivement. Cependant, il y a encore place à l'amélioration, en particulier dans la recommandation de films qui sortent des préférences habituelles de l'utilisateur.

## Références

* [Filtrage collaboratif](https://en.wikipedia.org/wiki/Collaborative_filtering)
* [Distance cosinus](https://en.wikipedia.org/wiki/Cosine_similarity)
* [MovieLens 100K Dataset](http://files.grouplens.org/datasets/movielens/ml-100k.zip)
* [Streamlit](https://streamlit.io/)
