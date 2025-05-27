import pandas as pd

def suggest_movie(genre, df):
    if genre not in df['Genre'].unique():
        print(f" Sorry, no movies found for genre '{genre}'. Please try another.")
        return
    
    movies = df[df['Genre'] == genre]
    movie = movies.sample(1).iloc[0]
    
    print(f"\n We suggest you watch: '{movie['Title']}'")
    if pd.notnull(movie['Rating']):
        print(f" IMDb Rating: {movie['Rating']}")
    else:
        print(" Rating not available")

if __name__ == "__main__":
    print(" Looking for file: movies.csv")
    try:
        df = pd.read_csv('movies.csv')
    except FileNotFoundError:
        print(" 'movies.csv' not found. Please run the scraper first (scrape_movies.py).")
        exit(1)

    print("Welcome to Movie Picker Bot!")
    user_genre = input("Enter a genre (action, comedy, drama, romance, thriller): ").strip().lower()

    suggest_movie(user_genre, df)
