import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=7185c8d9e3929cb21cfe0cfdd02616c3&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = moviesList[moviesList['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = moviesList.iloc[i[0]].movie_id

        recommended_movies.append(moviesList.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
moviesList = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.subheader('Search for a movie')
selected_movie_name = st.selectbox(
    "",
   moviesList['title'].values,
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    st.write("")
    st.write("")
   
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        full_name = (names[0].split('(')[0][:14]) + '...' if len(names[0]) > 14 else names[0]
        st.text(full_name)
        st.image(posters[0])

    with col2:
        full_name = (names[1].split('(')[0][:14]) + '...' if len(names[1]) > 14 else names[1]
        st.text(full_name)
        st.image(posters[1])

    with col3:
        full_name = (names[2].split('(')[0][:14]) + '...' if len(names[2]) > 14 else names[2]
        st.text(full_name)
        st.image(posters[2])

    with col4:
        full_name = (names[3].split('(')[0][:14]) + '...' if len(names[3]) > 14 else names[3]
        st.text(full_name)
        st.image(posters[3])

    with col5:
        full_name = (names[4].split('(')[0][:14]) + '...' if len(names[4]) > 14 else names[4]
        st.text(full_name)
        st.image(posters[4])