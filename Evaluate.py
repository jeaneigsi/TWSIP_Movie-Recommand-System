import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, accuracy_score, recall_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Charger les données d'évaluation
user_ratings_df = pd.read_csv("rating-000.csv")
user_ratings_df = user_ratings_df.drop('timestamp', axis=1)

# Diviser les données en un ensemble d'entraînement et un ensemble de test
train_df, test_df = train_test_split(user_ratings_df, test_size=0.2, random_state=42)

# Créer la matrice d'utilisateurs à partir de l'ensemble d'entraînement
user_matrix = train_df.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0)

# Définir le modèle
cf_knn_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)
cf_knn_model.fit(user_matrix)

# Prédire les évaluations de films pour l'ensemble de test
test_predictions = []
for index, row in test_df.iterrows():
    userId = row['userId']
    movieId = row['movieId']
    true_rating = row['rating']

    # Trouver les k plus proches voisins de l'utilisateur
    distances, indices = cf_knn_model.kneighbors(user_matrix.loc[[userId]].values, n_neighbors=11)

    # Trouver l'évaluation prédite pour le film
    prediction = np.mean(user_matrix.iloc[indices[0][1:], indices[1][0]]))

    test_predictions.append((true_rating, prediction))

# Calculer les métriques d'évaluation
true_ratings = [x[0] for x in test_predictions]
pred_ratings = [x[1] for x in test_predictions]

f1 = f1_score(true_ratings, pred_ratings)
accuracy = accuracy_score(true_ratings, pred_ratings)
recall = recall_score(true_ratings, pred_ratings)
rmse = np.sqrt(mean_squared_error(true_ratings, pred_ratings))

print("F1-score :", f1)
print("Précision :", accuracy)
print("Rappel :", recall)
print("RMSE :", rmse)
