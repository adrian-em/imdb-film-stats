import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self, df_movies, analyzer):
        self.df_movies = df_movies
        self.analyzer = analyzer

    def distribution_your_rating_imdb_rating(self):
        # Distribution of 'Your Rating' and 'imdbRating'
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        sns.histplot(self.df_movies["Your Rating"], bins=10, kde=True)
        plt.title("Distribution of Your Ratings")
        plt.xlabel("Your Rating")
        plt.ylabel("Frequency")

        plt.subplot(1, 2, 2)
        sns.histplot(self.df_movies["imdbRating"], bins=10, kde=True)
        plt.title("Distribution of imdbRatings")
        plt.xlabel("imdbRating")
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.show()

    def yearly_trends_movies_rated(self):
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            x=self.analyzer.yearly_trends.index, y=self.analyzer.yearly_trends.values
        )
        plt.title("Yearly Trends in Movies Rated by You")
        plt.xlabel("Year")
        plt.ylabel("Average Rating")
        plt.show()

    def distribution_your_rating_vs_imdb_rating(self):
        plt.figure(figsize=(8, 6))
        sns.kdeplot(self.df_movies["Your Rating"], label="Your Rating", fill=True)
        sns.kdeplot(self.df_movies["imdbRating"], label="imdbRating", fill=True)
        plt.title("Distribution of Your Ratings vs imdbRatings")
        plt.xlabel("Rating")
        plt.ylabel("Density")
        plt.legend()
        plt.show()

    def movies_rated_each_year(self):
        plt.figure(figsize=(12, 6))
        sns.barplot(x=self.analyzer.movies_rated_each_year.index, y=self.analyzer.movies_rated_each_year.values)
        plt.title("Number of Movies Rated Each Year")
        plt.xlabel("Year")
        plt.ylabel("Number of Movies Rated")
        plt.xticks(rotation=45)
        plt.show()

    def aggregated_count_genres(self):
        plt.figure(figsize=(15, 8))
        sns.barplot(y=self.analyzer.genre_counts.index, x=self.analyzer.genre_counts.values, orient="h")
        plt.title("Aggregated Data of Genres")
        plt.xlabel("Number of Occurrences")
        plt.ylabel("Genres")
        plt.show()

    def analyze_directors(self):
        plt.figure(figsize=(12, 6))
        sns.barplot(
            y=self.analyzer.most_frequent_directors.index, x=self.analyzer.most_frequent_directors.values, orient="h"
        )
        plt.title("Most Frequent Directors")
        plt.xlabel("Number of Occurrences")
        plt.ylabel("Directors")
        plt.show()

    def analyze_time_series(self):
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=self.df_movies, x="Year", y="imdbRating", label="imdbRating", estimator=np.mean
        )
        sns.lineplot(
            data=self.df_movies, x="Year", y="Your Rating", label="Your Rating", estimator=np.mean
        )
        plt.title("Average Movie Ratings Over Time")
        plt.xlabel("Year")
        plt.ylabel("Average Rating")
        plt.legend()
        plt.show()

    def ratings_distribution_by_genre(self):
        genres = self.df_movies["Genre"].str.split(", ").explode().unique()
        for genre in genres:
            plt.figure(figsize=(12, 6))
            sns.histplot(
                self.df_movies[self.df_movies["Genre"].str.contains(genre, na=False)]["Your Rating"],
                kde=True,
                label=genre,
            )
            plt.title(f"Ratings Distribution for {genre}")
            plt.xlabel("Your Rating")
            plt.ylabel("Frequency")
            plt.legend()
            plt.show()

    def visualize_all(self):
        self.distribution_your_rating_imdb_rating()
        self.yearly_trends_movies_rated()
        self.distribution_your_rating_vs_imdb_rating()
        self.movies_rated_each_year()
        self.aggregated_count_genres()
        self.analyze_time_series()
        # too much graphs
        # self.ratings_distribution_by_genre()
