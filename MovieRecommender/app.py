import streamlit as st


st.title('Movie recommender')
st.image('app_data/movie_collage.jpg')

if st.button("Build my profile"):
    with st.form(key='form1'):
        movie_name = st.text_input("movie name")

        