# 🎬 Movie Picker Bot (Python Project - Bhumika)

This project scrapes top-rated movies by genre from IMDb and suggests a movie to the user based on their chosen genre.

## 📌 Features

- Web scraping using BeautifulSoup
- Data storage in CSV
- User input-driven suggestion system
- Robust error handling
- Modular design with separate scraper and suggestor scripts

## 📁 Files Included

- `scrape_movies.py` – Scrapes IMDb for movie data by genre.
- `suggestor.py` – Lets user select a genre and suggests a movie.
- `movies.csv` – CSV file with scraped data.
- `requirements.txt` – List of libraries used.

## 🧪 Sample Output

```bash
Welcome to Movie Picker Bot!
Enter a genre (action, comedy, drama, romance, thriller): comedy

🎥 We suggest you watch: '9. Suttaa Thale Enakku'
⭐ IMDb Rating: 9.8
