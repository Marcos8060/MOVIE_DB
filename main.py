from crypt import methods
from flask import Flask,render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def home_page():
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=69e983e707fb12394c364e81aad843ff'
    data = requests.get(BASE_URL).json()['results']
    return render_template('index.html', movies= data)

@app.route('/movie/<int:id>')
def movie_page(id):
    movie = get_movie(id)
    title = f'movie.title'
    return render_template('movie.html', title= title, movie =movie)


@app.route('/trending', methods= ['GET'])
def trending_page():
    trending_movies = 'https://api.themoviedb.org/3/trending/movie/week?api_key=69e983e707fb12394c364e81aad843ff'
    data = requests.get(trending_movies).json()['results']
    return render_template('trending.html',trendings = data)

@app.route('/upcoming')
def coming_soon():
    upcoming = 'https://api.themoviedb.org/3/movie/upcoming?api_key=69e983e707fb12394c364e81aad843ff'
    data = requests.get(upcoming).json()['results']
    return render_template('coming.html', upcoming = data)

@app.route('/popular')
def popular_movies():
    popular = 'https://api.themoviedb.org/3/movie/popular?api_key=69e983e707fb12394c364e81aad843ff'
    data = requests.get(popular).json()['results']
    return render_template('popular.html', popular = data)


if __name__ == '__main__':
    app.run(debug=True)

