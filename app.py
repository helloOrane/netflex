from flask import Flask, render_template

app = Flask(__name__)

movies_datas = [
	{
		"title": "Alien Romulus",
		"year": 2024,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Fede Álvarez",
		"genre": "Drama",
		"picture": "./static/img/alien-romulus.webp",

	},
	{
		"title": "The Godfather",
		"year": 1972,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Francis Ford Coppola",
		"genre": "Crime",
		"picture": "./static/img/godfather.png",

	},
	{
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
		"title": "The Conjuring",
		"year": 2013,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "James Wan",
		"genre": "Horror",
		"picture": "./static/img/conjuring.jpg",
	},
	{
		"title": "The Exorcist",
		"year": 1973,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "William Friedkin",
		"genre": "Horror",
		"picture": "./static/img/exorcist.jpg",
	},
	{
		"title": "The Shining",
		"year": 1980,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Stanley Kubrick",
		"genre": "Horror",
		"picture": "./static/img/shining.jpg"
	},
	{
		"title": "Psycho",
		"year": 1960,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Alfred Hitchcock",
		"genre": "Horror",
		"picture": "./static/img/psycho.jpg"
	},
	{
		"title": "The Texas Chainsaw Massacre",
		"year": 1974,
		"resume": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tempor sapien quis aliquam dignissim. Nullam pulvinar mi libero, in porttitor est feugiat sit amet. Curabitur quis lacus odio.",
		"director": "Tobe Hooper",
		"genre": "Horror",
		"picture": "./static/img/texas_chainsaw_massacre.jpg"
	},
	{
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
			"movies": horror_movies
		},
		{
			"category_title": "Horror Movies",
			"movies": horror_movies
		},
		{
			"category_title": "Sci-Fi Movies",
			"movies": horror_movies
		},
		{
			"category_title": "Action Movies",
			"movies": horror_movies
		}
	]

@app.route("/")
@app.route("/index")
def index():
	print(type(movies))

	

	print(type(datas))
	return render_template("pages/home/index.html", datas=datas)

@app.route("/movies")
def movies():
	return render_template('pages/movies/index.html', movies=datas)





if __name__ == '__main__':
	app.run(debug=True)