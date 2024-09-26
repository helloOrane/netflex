from flask import Flask, render_template, request
from repo.Tv_show import get_all_tv_show_paginated,  get_categories_tv_show


app = Flask(__name__)

movies_datas = [
	{
		"id":1,
		"Title": "Alien Romulus",
		"Release_year": 2024,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Fede Álvarez",
		"genre": "Drama",
		"picture": "./static/img/alien-romulus.webp",
		"video": "x0XDEhP4MQs?si=MQou6bAzHhbgbRx7"
	},
	{
		"id":2,
		"Title": "The Godfather",
		"Release_year": 1972,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Francis Ford Coppola",
		"genre": "Crime",
		"picture": "./static/img/godfather.png",
		"video": "UaVTIH8mujA?si=ITrrqUJT7LE3X-sa"

	},
	{
		"id":3,
		"Title": "The Dark Knight",
		"Release_year": 2008,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Christopher Nolan",
		"genre": "Action",
		"picture": "./static/img/dark_knight.jpg",

	},
]

horror_movies = [
	{
		"id": 4,
		"Title": "The Conjuring",
		"Release_year": 2013,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "James Wan",
		"genre": "Horror",
		"picture": "./static/img/conjuring.jpg",
	},
	{
		"id": 5,
		"Title": "The Exorcist",
		"Release_year": 1973,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "William Friedkin",
		"genre": "Horror",
		"picture": "./static/img/exorcist.jpg",
	},
	{
		"id": 6,
		"Title": "The Shining",
		"Release_year": 1980,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Stanley Kubrick",
		"genre": "Horror",
		"picture": "./static/img/shining.jpg"
	},
	{
		"id": 7,
		"Title": "Psycho",
		"Release_year": 1960,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Alfred Hitchcock",
		"genre": "Horror",
		"picture": "./static/img/psycho.jpg"
	},
	{
		"id": 8,
		"Title": "The Texas Chainsaw Massacre",
		"Release_year": 1974,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "Tobe Hooper",
		"genre": "Horror",
		"picture": "./static/img/texas_chainsaw_massacre.jpg"
	},
	{
		"id": 9,
		"Title": "Halloween",
		"Release_year": 1978,
		"Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"Director": "John Carpenter",
		"genre": "Horror",
		"picture": "./static/img/halloween.jpg"
	}
]

datas = [
				{
			"category_title": "Recently added",
			"movies": movies_datas
		},
		{
			"category_title": "Humans In Space",
			"movies": horror_movies
		},
		{
			"category_title": "Earth & Climate",
			"movies": movies_datas
		},
		{
			"category_title": "Solar System",
			"movies": horror_movies
		},
		{
			"category_title": "The Universe",
			"movies": movies_datas
		},
		{
			"category_title": "Aeronautics",
			"movies": movies_datas
		},
		{
			"category_title": "Technology",
			"movies": horror_movies
		},
		{
			"category_title": "News & Events",
			"movies": movies_datas
		},
		{
			"category_title": "Kids",
			"movies": horror_movies
		},
		{
			"category_title": "Originals",
			"movies": movies_datas
		},
		{
			"category_title": "Documentaries",
			"movies": horror_movies
		},
		{
			"category_title": "History",
			"movies": movies_datas
		},

	]

@app.route("/")
@app.route("/authentication")
def index():
	

	return render_template('pages/home/index.html', datas=datas)
	# return render_template('pages/authentication/index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		print('request.form:', request.form)
	
	return render_template('pages/login/index.html')

@app.route("/movies")
def movies():
	return render_template('pages/movies/index.html', datas=datas)

@app.route("/movies/<int:movie_id>")
def movie_detail(movie_id):
	print('movie_id:', movie_id)
	data = list(filter(lambda movie: movie['id'] == movie_id, movies_datas))[0]
	print('data:', data)
	return render_template('pages/movie_detail/index.html', data=data)

@app.route("/movies/<int:movie_id>/watch")
def watch_movie(movie_id):
	data = list(filter(lambda movie: movie['id'] == movie_id, movies_datas))[0]
	return render_template('pages/watch_movie/index.html', data=data)


@app.route("/tv-shows")
def tv_shows():
	# TODO: create error page
	categories =  get_categories_tv_show()
	category_tv_show_list = []
	if categories:
		for category in categories:
			tv_show_list = get_all_tv_show_paginated(category)
			if tv_show_list:
				category_tv_show_list.append({"category": category, "tv_shows": tv_show_list})
	return render_template('pages/tv_shows/index.html', datas=[])

@app.route('/tv-shows/<int:tv_show_id>')
def tv_show_detail(tv_show_id):
	data = list(filter(lambda movie: movie['id'] == tv_show_id, movies_datas))[0]
	return render_template('pages/tv_show_detail/index.html', data=data)


if __name__ == '__main__':
	app.run(debug=True)