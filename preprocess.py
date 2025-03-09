import pandas as pd
import ast

def load_and_clean_data():
    """Loads and cleans the movie dataset."""
    # Load datasets
    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    # Merge datasets
    movies = movies.merge(credits, left_on="id", right_on="movie_id", how="left")

    # Check for necessary columns
    if 'title_x' not in movies.columns:
        raise ValueError("Column 'title_x' not found in the dataset")

    # Select relevant columns
    movies = movies[['title_x', 'overview', 'genres', 'cast', 'crew']].fillna("")

    # Function to parse JSON-like data
    def parse_json(data):
        try:
            return [item['name'] for item in ast.literal_eval(data)]
        except:
            return []

    # Apply parsing function
    movies['genres'] = movies['genres'].apply(parse_json)
    movies['cast'] = movies['cast'].apply(parse_json)
    movies['crew'] = movies['crew'].apply(parse_json)

    # Combine relevant text fields
    movies['combined_features'] = (
        movies['overview'] + ' ' +
        movies['genres'].apply(lambda x: ' '.join(x)) + ' ' +
        movies['cast'].apply(lambda x: ' '.join(x)) + ' ' +
        movies['crew'].apply(lambda x: ' '.join(x))
    )

    return movies






