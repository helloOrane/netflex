import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_BEARER_TOKEN = os.getenv('API_BEARER_TOKEN')

url = "https://api.themoviedb.org/3/configuration"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_BEARER_TOKEN}"
}

response = requests.get(url, headers=headers)


def get_latest_movies():
    url = "https://api.themoviedb.org/3/movie/now_playing"
    response = requests.get(url, headers=headers)
    return response.json()


movies = get_latest_movies()
print(movies)
