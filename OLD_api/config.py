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


def get_movie_details_from_api(title):
    # séparer les mots par des %20
    title = title.replace(' ', '%20')
    movie_url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
    movie = requests.get(movie_url, headers=headers)
    response = movie.json()
    tv_show_result = response['results'].filter(lambda x: x['original_name'] == title)
    if tv_show_result['results'][0]:
        new_movie = {
            'movie_db_id': tv_show_result[0]['id'],
            'picture' : tv_show_result[0]['poster_path'],
        }
        return new_movie

def get_tv_show_details_from_api(title):
    title = title.replace(' ', '%20')
    tv_show_url = f"https://api.themoviedb.org/3/search/tv?query={title}&include_adult=false&language=en-US&page=1"
    response = requests.get(tv_show_url, headers=headers)
    response = response.json()
    tv_show_result = response['results'].filter(lambda x: x['original_name'] == title)

    if tv_show_result[0]:
        new_tv_show = {
            'Movie_db_id': tv_show_result[0]['id'],
            'Picture' : tv_show_result[0]['poster_path'],
        }
        return new_tv_show

def get_video_from_api(movie_db_id):
    video_url = f"https://api.themoviedb.org/3/movie/{movie_db_id}/videos?language=en-US"
    response = requests.get(video_url, headers=headers)
    response = response.json()
    youtube_keys = list(filter(lambda x: x['site'] == 'YouTube', response['results']))
    if youtube_keys[0]:
        key = youtube_keys[0]['key']
        print(key)
        return key
    
