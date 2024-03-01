import pandas as pd
from itertools import combinations
import pprint


class MovieAnalyzer:
    def __init__(self, df_movies):
        df_movies.columns = [col.strip() for col in df_movies.columns]
        df_movies["imdbRating"] = pd.to_numeric(
            df_movies["imdbRating"], errors="coerce"
        )
        df_movies["Your Rating"] = pd.to_numeric(
            df_movies["Your Rating"], errors="coerce"
        )
        df_movies["Year"] = df_movies["Year"].str.split("–").str[0].str.strip()
        df_movies["Year"] = pd.to_numeric(df_movies["Year"], errors="coerce")

        self.df_movies = df_movies

    def calculate_summary_statistics(self):
        summary_stats = self.df_movies.describe()
        print("Summary Statistics for Numerical Columns:")
        print(summary_stats)
        print("\n")

    def analyze_genres(self):
        self.genres_series = self.df_movies["Genre"].str.split(", ").explode()
        most_frequent_genres = self.genres_series.value_counts().head(5)
        least_frequent_genres = self.genres_series.value_counts().tail(5)

        print(f"Most Frequent Genres: {most_frequent_genres}")
        print(f"Least Frequent Genres: {least_frequent_genres}")
        print("\n")

    def calculate_correlation(self):
        correlation_matrix = self.df_movies[["Your Rating", "imdbRating"]].corr()
        print("Correlation between 'Your Rating' and 'imdbRating':")
        print(correlation_matrix)
        print("\n")

    def analyze_actors(self):
        actors_series = self.df_movies["Actors"].str.split(", ").explode()
        actors_series = actors_series[actors_series != "N/A"]
        actor_counts = actors_series.value_counts()

        print("Most Common Actors:")
        print(actor_counts.head(10))
        print("\n")

        expanded_actors = self.df_movies.explode("Actors")
        average_ratings_by_actor = (
            expanded_actors.groupby("Actors")["imdbRating"]
            .mean()
            .sort_values(ascending=False)
        )

        print("Average IMDb Ratings by Actor:")
        print(average_ratings_by_actor.head(10))
        print("\n")

    def analyze_actor_pairs(self):
        self.df_movies["Pairs"] = (
            self.df_movies["Actors"]
            .dropna()
            .apply(lambda x: [pair for pair in combinations(x.split(", "), 2)])
        )
        pairs_series = self.df_movies.explode("Pairs")
        pair_counts = pairs_series["Pairs"].value_counts()

        print("Most Common Actor Pairs:")
        print(pair_counts.head(10))
        print("\n")

    def yearly_trends_movies_rated(self):
        self.yearly_trends = self.df_movies.groupby("Year")["Your Rating"].mean()

        print(f"Yearly Trends in Movies Rated: {self.yearly_trends}")
        print("\n")

    def genre_combinations(self):
        # Genre Combinations
        genre_combinations = self.df_movies["Genre"].value_counts().head(5)
        print(f"Most Common Genre Combinations: {genre_combinations}")
        print("\n")

    def aggregated_count_genres(self):
        # Aggregated Data of Genres
        self.genre_counts = self.genres_series.value_counts()

        # Print aggregated data of genres
        print(f"Aggregated Data of Genres: {self.genre_counts}")
        print("\n")

    def number_movies_rated_each_year(self):
        self.movies_rated_each_year = self.df_movies["Year"].value_counts().sort_index()
        print(f"Number of Movies Rated Each Year: {self.movies_rated_each_year}")
        print("\n")

    def analyze_directors(self):
        directors_series = self.df_movies["Director"].str.split(", ").explode()
        directors_series = directors_series[directors_series != "N/A"]
        self.most_frequent_directors = directors_series.value_counts().head(5)
        least_frequent_directors = directors_series.value_counts().tail(5)

        print(f"Most Frequent Directors: {self.most_frequent_directors}")
        print(f"Least Frequent Directors: {least_frequent_directors}")
        print("\n")

    def top_rated_movies_by_genre(self):
        genres = self.df_movies["Genre"].str.split(", ").explode().unique()
        top_movies = {}
        for genre in genres:
            top_movie = (
                self.df_movies[self.df_movies["Genre"].str.contains(genre, na=False)]
                .sort_values(by="Your Rating", ascending=False)
                .head(1)[["Title", "Your Rating"]]
            )
            top_movies[genre] = (
                top_movie.to_dict("records")[0]
                if not top_movie.empty
                else "No movies found"
            )

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(top_movies)

    def perform_all_analyses(self):
        self.calculate_summary_statistics()
        self.analyze_genres()
        self.calculate_correlation()
        self.analyze_actors()
        self.analyze_actor_pairs()
        self.yearly_trends_movies_rated()
        self.genre_combinations()
        self.aggregated_count_genres()
        self.number_movies_rated_each_year()
        self.analyze_directors()
        self.top_rated_movies_by_genre()
