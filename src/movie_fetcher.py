
from csv_writer import write_movies_to_csv


def main():
    
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    write_movies_to_csv("/data/movie_results.csv",fields)


if __name__ == '__main__':
    main()