import pandas as pd
from api import get_movie_data
from cache import CACHE_FILE_PATH
import json

class DataHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        df = pd.read_csv(self.filename)
        print("Loading movie data...")
        for index, row in df.iterrows():
            const = row["Const"]
            your_rating = row["Your Rating"]
            get_movie_data(const, your_rating)
        print("Movie data loaded.")

        with open(CACHE_FILE_PATH, "r") as file:
            movie_data = json.load(file)
        movies_list = [details.update({'imdbID': imdb_id}) or details for imdb_id, details in movie_data.items()]
        df_movies = pd.DataFrame(movies_list)
        return df_movies
