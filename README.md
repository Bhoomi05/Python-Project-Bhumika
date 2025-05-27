#  Movie Picker Bot (Python Project - Bhumika)

This project scrapes top-rated movies by genre from IMDb and suggests a movie to the user based on their chosen genre.

##  Features

-  Web scraping using BeautifulSoup
-  Uses `pandas` to filter and pick movies
-  Simple terminal-based user interaction
-  CSV file output with all movie data
-  Clear error handling if something goes wrong

##  Files Included

- `scrape_movies.py` – Scrapes IMDb for movie data by genre.
- `suggestor.py` – Lets user select a genre and suggests a movie.
- `movies.csv` – CSV file with scraped data.
- `requirements.txt` – List of python libraries used.

##  How to Run This Project

Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Run the Scraper to Get Movie Data
python scrape_movies.py

Step 3: Run the Suggestor Bot
python suggestor.py

##  Sample Output

Welcome to Movie Picker Bot!
Enter a genre (action, comedy, drama, romance, thriller): comedy

 We suggest you watch: '9. Suttaa Thale Enakku'
 IMDb Rating: 9.8
