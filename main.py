from crypt import methods
from flask import Flask,render_template
import requests
import json
import urllib.request,json 


app = Flask(__name__)

class Movie:

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count



base_url = 'https://api.themoviedb.org/3/movie/{}?api_key=69e983e707fb12394c364e81aad843ff'
api_key = '69e983e707fb12394c364e81aad843ff'

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

@app.route('/')
def home_page():
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=69e983e707fb12394c364e81aad843ff'
    data = requests.get(BASE_URL).json()['results']
    return render_template('index.html', movies= data)

@app.route('/movie/<int:id>')
def movie_page(id):
    movie = get_movie(id)
    title = f'movie.title'
    return render_template('movie.html',title=title,movie=movie)



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

