import requests
from bs4 import BeautifulSoup
import pandas as pd
import re  


def scrape_movies(genres, movies_per_genre=10):
    all_movies = []

    for genre in genres:
        print(f"🎬 Scraping top {movies_per_genre} movies for genre: {genre}")
        url = f"https://www.imdb.com/search/title/?genres={genre}&sort=user_rating,desc&title_type=feature"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            print(f"🔎 HTTP Status Code for {genre}: {response.status_code}")
            print(f"📄 Response length: {len(response.text)} characters")
            with open(f"{genre}_page.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Error fetching data for {genre}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        movie_blocks = soup.select('li.ipc-metadata-list-summary-item')
        print(f"🔍 Found {len(movie_blocks)} movie blocks for {genre}")

        for movie in movie_blocks[:movies_per_genre]:
            try:
                title = movie.find('h3').text.strip()
                rating_tag = movie.find('span', class_='ipc-rating-star')  # or inspect if it's different
                rating_text = rating_tag.text.strip() if rating_tag else None
                rating_match = re.match(r"(\d+(\.\d+)?)", rating_text)
                rating = float(rating_match.group(1)) if rating_match else None

                all_movies.append({
                'Title': title,
                'Genre': genre,
                'Rating': rating
                })
            except Exception as e:
                print(f"⚠️ Error parsing a movie: {e}")
                continue


            all_movies.append({
                'Title': title,
                'Genre': genre,
                'Rating': rating
            })

    return pd.DataFrame(all_movies)

if __name__ == "__main__":
    print("🚀 Starting scraper...")
    genres = ['action', 'comedy', 'drama', 'romance', 'thriller']
    df_movies = scrape_movies(genres)

    if df_movies.empty:
        print("❌ Failed to scrape any movies. Check your selectors or site structure.")
    else:
        df_movies.to_csv('movies.csv', index=False)
        print("✅ movies.csv created successfully!")
