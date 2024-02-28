import streamlit as st
from application import movie_recommender_engine, user_matrix, cf_knn_model, movies_df
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

# Définition de la barre latérale avec le menu principal
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Simuler"],
    )

# Logique pour traiter la sélection de l'utilisateur
if selected == "Simuler":
    # Paramètres pour la recommandation
    st.title("Système de recommandation de films")
    st.subheader("Entrez le nom du film et le nombre de recommandations souhaité :movie_camera:")

    st.markdown(""" 
                <style>
                .st-emotion-cache-6qob1r{
                    background: #F5A21F!important;
                    color: #ffffff!important;              
                }
                </style>""", unsafe_allow_html=True)

    movie_options=movies_df['title'].tolist()
    movie_option_filtre=[film for film in movie_options if film!="Toy Story (1995)"]
    film_name = st.selectbox("Nom du film:", movie_option_filtre)
    n_recs = st.slider("Nombre de recommandations:", min_value=1, max_value=20, value=5)

    # Obtenir les recommandations de films
    movie_recs = movie_recommender_engine(film_name, user_matrix, cf_knn_model, n_recs, movies_df)

    # Affichage des résultats sous forme de tableau
    st.write("Recommandations de films:")
    st.table(movie_recs[['Title', 'Distance']])

    # Affichage de la distance en tant que graphique et histogramme
    st.write("Distance entre les films recommandés et le film d'entrée:")
    fig1, ax1 = plt.subplots()
    ax1.plot(movie_recs['Distance'])
    st.pyplot(fig1)

    st.write("Performances du système de recommandation:")
    fig2, ax2 = plt.subplots()
    ax2.bar(movie_recs.index, movie_recs['Distance'])
    st.pyplot(fig2)
