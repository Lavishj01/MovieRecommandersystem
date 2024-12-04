
import streamlit as st
import pickle
import pandas as pd
import requests


# def fetch_poster(movie_id):
#     response = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey=2b6ebfcfb563e04e6180153073ef6751")
#     data = response.json()
#     return data.get('Poster', "No Poster Available")


st.title('Movie Recommender')


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movies_posters = []

    for i in movies_list:
        movie_data = movies.iloc[i[0]]
        recommended_movies.append(movie_data.title)
        # recommended_movies_posters.append(fetch_poster(movie_data))

    return recommended_movies


# Load similarity matrix and movie data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Select movie
selected_movie_name = st.selectbox("Select a Movie to Recommend", movies['title'].values)

# Recommendation button
if st.button("Recommend"):
    names = recommend(selected_movie_name)

    for name in names:

            st.write(name)
