import argparse
from data_handler import DataHandler
from movie_analyzer import MovieAnalyzer
from visualizer import Visualizer

def main():
    parser = argparse.ArgumentParser(description="Obtain stats from IMDB csv file.")
    parser.add_argument("filename", type=str, help="Name of the CSV file")
    args = parser.parse_args()

    data_handler = DataHandler(args.filename)
    df_movies = data_handler.load_data()

    analyzer = MovieAnalyzer(df_movies)
    analyzer.perform_all_analyses()

    visualizer = Visualizer(df_movies, analyzer)
    visualizer.visualize_all()

if __name__ == "__main__":
    main()
