import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Obtain stats from IMDB csv file.")
parser.add_argument("filename", type=str, help="Name of the CSV file")

args = parser.parse_args()

# Load the data
df = pd.read_csv(args.filename)

# Summary statistics for numerical columns
summary_stats = df.describe()

# Print summary statistics for numerical columns
print("Summary Statistics for Numerical Columns:")
print(summary_stats)
print("\n")

# Most and least frequent genres
genres_series = df["Genres"].str.split(", ").explode()
most_frequent_genres = genres_series.value_counts().head(5)
least_frequent_genres = genres_series.value_counts().tail(5)

# Print most and least frequent genres
print(f"Most Frequent Genres: {most_frequent_genres}")
print(f"Least Frequent Genres: {least_frequent_genres}")
print("\n")

# Correlation between 'Your Rating' and 'IMDb Rating'
correlation = df[["Your Rating", "IMDb Rating"]].corr()

# Print correlation between 'Your Rating' and 'IMDb Rating'
print(f"Correlation between Your Rating and IMDb Rating: {correlation}")
print("\n")

# Yearly trends in movies rated
yearly_trends = df.groupby("Year")["Your Rating"].mean()

# Print Yearly trends in movies rated
print(f"Yearly Trends in Movies Rated: {yearly_trends}")
print("\n")

# Distribution of 'Your Rating' and 'IMDb Rating'
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df["Your Rating"], bins=10, kde=True)
plt.title("Distribution of Your Ratings")
plt.xlabel("Your Rating")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.histplot(df["IMDb Rating"], bins=10, kde=True)
plt.title("Distribution of IMDb Ratings")
plt.xlabel("IMDb Rating")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Genre Combinations
genre_combinations = df["Genres"].value_counts().head(5)

# Print most common genre combinations
print(f"Most Common Genre Combinations: {genre_combinations}")
print("\n")

# Correlation with Other Numerical Features
correlation_with_other_features = df[
    ["Your Rating", "IMDb Rating", "Runtime (mins)", "Num Votes"]
].corr()

# Print correlation with other numerical features
print(f"Correlation with Other Numerical Features: {correlation_with_other_features}")
print("\n")

# Number of Movies Rated Each Year
movies_rated_each_year = df["Year"].value_counts().sort_index()

# Print number of movies rated each year
print(f"Number of Movies Rated Each Year: {movies_rated_each_year}")
print("\n")

# Aggregated Data of Genres
genre_counts = genres_series.value_counts()

# Print aggregated data of genres
print(f"Aggregated Data of Genres: {genre_counts}")
print("\n")

# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_trends.index, y=yearly_trends.values)
plt.title("Yearly Trends in Movies Rated by You")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.show()

plt.figure(figsize=(8, 6))
sns.kdeplot(df["Your Rating"], label="Your Rating", shade=True)
sns.kdeplot(df["IMDb Rating"], label="IMDb Rating", shade=True)
plt.title("Distribution of Your Ratings vs IMDb Ratings")
plt.xlabel("Rating")
plt.ylabel("Density")
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=movies_rated_each_year.index, y=movies_rated_each_year.values)
plt.title("Number of Movies Rated Each Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies Rated")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(15, 8))
sns.barplot(y=genre_counts.index, x=genre_counts.values, orient="h")
plt.title("Aggregated Data of Genres")
plt.xlabel("Number of Occurrences")
plt.ylabel("Genres")
plt.show()

# Most and least frequent directors
directors_series = df["Directors"].str.split(", ").explode()
most_frequent_directors = directors_series.value_counts().head(5)
least_frequent_directors = directors_series.value_counts().tail(5)

# Print most and least frequent directors
print(f"Most Frequent Directors: {most_frequent_directors}")
print(f"Least Frequent Directors: {least_frequent_directors}")
print("\n")

# Plotting most frequent directors
plt.figure(figsize=(12, 6))
sns.barplot(
    y=most_frequent_directors.index, x=most_frequent_directors.values, orient="h"
)
plt.title("Most Frequent Directors")
plt.xlabel("Number of Occurrences")
plt.ylabel("Directors")
plt.show()
