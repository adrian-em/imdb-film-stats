from cache import load_cache, save_cache
import requests

API_KEY = "your_api_key"  # Replace 'your_api_key' with your actual OMDB API key


def get_movie_data(const, your_rating):
    """Fetch movie data using the OMDB API, utilizing cache to save API calls."""
    cache = load_cache()

    if const in cache:
        # print(f"Data for {const} fetched from cache.")
        cache_data = cache[const]
        # cache_data['Your Rating'] = your_rating
        return cache_data
    else:
        print(f"Fetching data for {const} from OMDB API.")
        base_url = "http://www.omdbapi.com/"
        params = {"i": const, "apikey": API_KEY}
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and "Error" not in data:
            data["Your Rating"] = your_rating
            cache[const] = data
            save_cache(cache)
        else:
            data = None
            print(f"Error fetching data for {const}: {data}")
        return data
