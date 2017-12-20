from flask import render_template
from app import app
from .request import get_movies, get_movie

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
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie = movie)