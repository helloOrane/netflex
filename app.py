from flask import Flask, render_template

app = Flask(__name__)

movies = [
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

@app.route("/")
@app.route("/index")
def index():
	return render_template("components/slider_movie_card.html", movies=movies, horror_movies=movies)



if __name__ == '__main__':
	app.run(debug=True)