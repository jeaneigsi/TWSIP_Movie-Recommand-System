# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

user_ratings_df= pd.read_csv("rating-000.csv")
user_ratings_df=user_ratings_df.drop('timestamp',axis=1)

# user_ratings_df=user_ratings_df.sample(n=2000,random_state=42)

# user_ratings_df=user_ratings_df.iloc[:2000000]
print(user_ratings_df.shape)
user_ratings_df.head()

movies_df=pd.read_csv("movie.csv")
movies_df = movies_df[['title', 'genres','movieId']]
movies_df.head()
# movies_df.shape

movies_data=user_ratings_df.merge(movies_df, on='movieId')
movies_data.head()

"""# [code](https://www.freecodecamp.org/news/how-to-build-a-movie-recommendation-system-based-on-collaborative-filtering/)
**texte en gras**
"""

user_matrix = user_ratings_df.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0)
# Supprimer la colonne en trop
user_matrix = user_matrix.iloc[:10158, :10158]

print(user_matrix.shape)
user_matrix.head()

from sklearn.neighbors import NearestNeighbors

#Modele définition

cf_knn_model=NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)

cf_knn_model.fit(user_matrix)

# !pip install fuzzywuzzy
from fuzzywuzzy import process

# Extract input movie ID
movie_id = process.extractOne('Crossing Guard, The (1995)', movies_df['title'])[2]
print(movie_id+1)

def movie_recommender_engine(movie_name, matrix, cf_model, n_recs, movies_df):
    # Extract input movie ID
    movie_id = process.extractOne(movie_name, movies_df['title'])[2]

    # Remodeler la matrice en 2D
    X_2d = matrix[movie_id].values.reshape(1, -1)


    # Calculate neighbour distances
    distances, indices = cf_model.kneighbors(X_2d, n_neighbors=n_recs)
    movie_rec_ids = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]

    # List to store recommendations
    cf_recs = []
    for i in movie_rec_ids:
        cf_recs.append({'Title':movies_df['title'][i[0]],'Distance':i[1]})

    # Select top number of recommendations needed
    df = pd.DataFrame(cf_recs, index = range(1,n_recs))

    return df

# Appeler la fonction avec le modèle déjà formé
n_recs = 10
movie_recs = movie_recommender_engine('Batman', user_matrix, cf_knn_model, n_recs, movies_df)

movie_recs

# @title Distance

from matplotlib import pyplot as plt
movie_recs['Distance'].plot(kind='line', figsize=(8, 4), title='Distance')
plt.gca().spines[['top', 'right']].set_visible(False)

# @title Distance

from matplotlib import pyplot as plt
movie_recs['Distance'].plot(kind='hist', bins=20, title='Distance')
plt.gca().spines[['top', 'right',]].set_visible(False)

movie_recs