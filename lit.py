import streamlit as st
from application import movie_recommender_engine, user_matrix, cf_knn_model, movies_df
from streamlit_option_menu import option_menu

# Définition de la barre latérale avec le menu principal
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Simuler", "Performance"],
    )

# Logique pour traiter la sélection de l'utilisateur
if selected == "Simuler":
    # Paramètres pour la recommandation
    film_name = st.text_input("Entrez le nom du film:", "Batman")
    n_recs = st.slider("Nombre de recommandations:", min_value=1, max_value=20, value=10)

    # Obtenir les recommandations de films
    movie_recs = movie_recommender_engine(film_name, user_matrix, cf_knn_model, n_recs, movies_df)

    # Affichage des résultats sous forme de tableau
    st.write("Recommandations de films:")
    st.table(movie_recs[['Title', 'Distance']])
   

    # Affichage de la distance en tant que graphique et histogramme
    st.write("Distance entre les films recommandés et le film d'entrée:")
    st.line_chart(movie_recs['Distance'], use_container_width=True)
    st.bar_chart(movie_recs['Distance'], use_container_width=True)


# n_recs = 10 
# movie_recs = movie_recommender_engine('Batman', user_matrix, cf_knn_model, n_recs, movies_df)