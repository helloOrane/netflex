import requests
from dotenv import load_dotenv
import os

from models.init import Movie



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


# movies = get_latest_movies()
# for movie in movies['results']:
#     new_movie_db = Movie(
#         name=movie['title'],
#         release_year=movie['release_date'],
#         picture=movie['poster_path'],
#         genre_id=1,
#         video=movie['video'],
#         director=movie['director'],
#         resume=movie['overview']
#     )
# print(movies)
