from flask import Blueprint, render_template
from cinemate_app.service import movie_service
from cinemate_app.models import Movie

movies = Blueprint('movies', __name__)


@movies.route('/')
def movies_page():
    movie_list = movie_service.get_all_movies()
    return render_template('movies.html', title="List of Movies", movie_list=movie_list)


@movies.route('/movie/<int:movie_id>')
def movie(movie_id):
    current_movie = movie_service.get_movie_by_id(movie_id)
    return render_template('movie.html', movie=current_movie)


@movies.route('/add_movie')
def add_movie():
    return render_template('add_movie.html', title="Add Movie")


@movies.route('/update_movie')
def update_movie():
    return render_template('update_movie.html', title="Update Movie")
