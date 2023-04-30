from movie_scraper import scrape_movies_data
import csv
def write_movies_to_csv( filename,fields):
        # Downloading imdb top 250 movie's data
        url = 'http://www.imdb.com/chart/top'

        movies = scrape_movies_data(url)
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in movies:
                writer.writerow({
                "preference_key": movie['preference_key'],
                "movie_title": movie['movie_title'],
                "star_cast": movie['star_cast'],
                "rating": movie['rating'],
                "year": movie['year'],
                "place": movie['place'],
                "vote": movie['vote'],
                "link": movie['link']
                })