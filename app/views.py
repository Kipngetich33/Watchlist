from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies, get_movie, search_movie
from models import review
from .forms import ReviewForm 
ReviewForm = review.Review

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

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name= search_movie))
    else:
        return render_template('index.html' ,title = title , popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def user(movie_id):
    '''
    View root function that returns a user page and data
    '''
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie_id)
    return render_template('movie.html', title = title, movie = movie, reviews = reviews)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)

@app.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)


    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review (movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))   