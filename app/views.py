from flask import render_template
from app import app
from .request import get_movies, get_movie, search_movie


#
@app.route('/')
def index():
    '''
    View root page function that returns the index and its data
    '''
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Movie Website'
    return render_template('index.html' ,title = title , popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def user(movie_id):
    '''
    View root function that returns a user page and data
    '''
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies = searched_movies)