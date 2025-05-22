import pickle
import streamlit as st

# Load your saved data
new_df = pickle.load(open('movies.pkl', 'rb'))
cos_sim = pickle.load(open('similarity.pkl', 'rb'))  # if you saved similarity also

import streamlit as st

st.title('Hello Streamlit!')

st.write('This is working.')

# Recommend function
def recommend(movie):
    if movie not in new_df['title'].values:
        return ["Sorry, movie not found."]
    index = new_df[new_df['title'] == movie].index[0]
    similarity_scores = cos_sim[index]
    similar_movies = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)[1:6]
    return [new_df.iloc[i[0]].title for i in similar_movies]

# Streamlit UI
st.title("Movie Recommendation System")

movie_name = st.text_input("Enter a movie name")

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    for i in recommendations:
        st.write(i)
