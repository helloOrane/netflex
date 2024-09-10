from flask import Flask, render_template
from api import config

app = Flask(__name__)

movies_datas = [
	{
		"id":1,
		"title": "Alien Romulus",
		"year": 2024,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Fede Álvarez",
		"genre": "Drama",
		"picture": "./static/img/alien-romulus.webp",
		"video": "x0XDEhP4MQs?si=MQou6bAzHhbgbRx7"
	},
	{
		"id":2,
		"title": "The Godfather",
		"year": 1972,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Francis Ford Coppola",
		"genre": "Crime",
		"picture": "./static/img/godfather.png",
		"video": "UaVTIH8mujA?si=ITrrqUJT7LE3X-sa"

	},
	{
		"id":3,
		"title": "The Dark Knight",
		"year": 2008,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Christopher Nolan",
		"genre": "Action",
		"picture": "./static/img/dark_knight.jpg",

	},
]

horror_movies = [
	{
		"id": 4,
		"title": "The Conjuring",
		"year": 2013,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "James Wan",
		"genre": "Horror",
		"picture": "./static/img/conjuring.jpg",
	},
	{
		"id": 5,
		"title": "The Exorcist",
		"year": 1973,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "William Friedkin",
		"genre": "Horror",
		"picture": "./static/img/exorcist.jpg",
	},
	{
		"id": 6,
		"title": "The Shining",
		"year": 1980,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Stanley Kubrick",
		"genre": "Horror",
		"picture": "./static/img/shining.jpg"
	},
	{
		"id": 7,
		"title": "Psycho",
		"year": 1960,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Alfred Hitchcock",
		"genre": "Horror",
		"picture": "./static/img/psycho.jpg"
	},
	{
		"id": 8,
		"title": "The Texas Chainsaw Massacre",
		"year": 1974,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Tobe Hooper",
		"genre": "Horror",
		"picture": "./static/img/texas_chainsaw_massacre.jpg"
	},
	{
		"id": 9,
		"title": "Halloween",
		"year": 1978,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "John Carpenter",
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
	

	# return render_template('pages/home/index.html', datas=datas)
	return render_template('pages/authentication/index.html')

@app.route("/movies")
def movies():
	return render_template('pages/movies/index.html', datas=datas)

@app.route("/movies/<int:movie_id>")
def movie_detail(movie_id):
	print('movie_id:', movie_id)
	data = list(filter(lambda movie: movie['id'] == movie_id, movies_datas))[0]
	print('data:', data)
	return render_template('pages/movie_detail/index.html', data=data)


@app.route("/tv-shows")
def tv_shows():
	return render_template('pages/tv_shows/index.html', datas=datas)

@app.route('/tv-shows/<int:tv_show_id>')
def tv_show_detail(tv_show_id):
	data = list(filter(lambda movie: movie['id'] == tv_show_id, movies_datas))[0]
	return render_template('pages/tv_show_detail/index.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)