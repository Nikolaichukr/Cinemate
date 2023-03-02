from cinemate_app import db
from ..models import Movie


def get_all_movies():
    movies = Movie.query.all()
    return movies


def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    return movie
