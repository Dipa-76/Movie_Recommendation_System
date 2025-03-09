import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import load_and_clean_data

# Load cleaned data
movies = load_and_clean_data()

# Vectorize text data
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Movie title mapping to indices
indices = pd.Series(movies.index, index=movies['title_x']).drop_duplicates()

def get_movie_recommendations(movie_title, num_recommendations=5):
    """Returns movie recommendations based on the input title."""
    if movie_title not in indices:
        return ["Movie not found! Please enter a valid movie name."]

    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]

    return movies['title_x'].iloc[movie_indices].tolist()

def get_movie_suggestions(query):
    """Returns a list of movie names that match the query."""
    return movies['title_x'][movies['title_x'].str.contains(query, case=False, na=False)].tolist()








