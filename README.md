# IMDB Statistics Extractor

## Overview
This Python script allows users to analyze IMDB movie data from a CSV file. It provides summary statistics for numerical columns, identifies the most and least frequent genres and directors, examines the correlation between user ratings and IMDb ratings, and illustrates yearly trends in movies. Additionally, it generates various visualizations to better understand the distribution of ratings, genres, and other factors.

## Installation

Before running this script, ensure you have Python installed on your machine. Additionally, the following Python packages are required:
- matplotlib
- seaborn
- pandas

You can install these packages using pip:

```bash
pip install matplotlib seaborn pandas
```

## Usage

To use this script, you need to have a CSV file containing IMDB data. The CSV file should have columns like 'Genres', 'Your Rating', 'IMDb Rating', 'Year', 'Directors', etc.

Run the script from the command line, providing the path to your CSV file as an argument:

```bash
python imdb_stats.py path_to_your_file.csv
```

The script will print out various statistics and display multiple plots based on the data in your CSV file.

## Features

The script provides the following features:
- Summary statistics for numerical columns in the data.
- Identification of the most and least frequent genres.
- Correlation analysis between 'Your Rating' and 'IMDb Rating'.
- Yearly trends in movies rated.
- Distribution plots for 'Your Rating' and 'IMDb Rating'.
- Most common genre combinations.
- Correlation analysis with other numerical features.
- Annual count of movies rated.
- Aggregated data visualization for genres.
- Identification of the most and least frequent directors.

## Visualizations

The script generates the following visualizations:
- Histograms for the distribution of 'Your Rating' and 'IMDb Rating'.
- Line plot showing yearly trends in movies rated.
- KDE plots comparing the distribution of 'Your Rating' vs 'IMDb Rating'.
- Bar plots showing the number of movies rated each year and the aggregated data of genres.
- Bar plot highlighting the most frequent directors.

## Contributing

Feel free to fork the repository and submit pull requests.
