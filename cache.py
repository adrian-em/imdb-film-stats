import json

CACHE_FILE_PATH = "movie_cache.json"


def load_cache():
    """Load the cache file containing movie data."""
    try:
        with open(CACHE_FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_cache(cache):
    """Save the updated cache back to the file."""
    with open(CACHE_FILE_PATH, "w") as file:
        json.dump(cache, file, indent=4)
