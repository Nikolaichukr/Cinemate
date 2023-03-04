from cinemate_app import db
from ..models import Movie


def get_all_movies():
    return Movie.query.all()


def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)


def delete_movie(movie):
    db.session.delete(movie)
    db.session.commit()


def add_movie(title, year, director, genre):
    new_movie = Movie(title, year, director, genre)
    db.session.add(new_movie)
    db.session.commit()


def update_movie(current_movie, title, year, director, genre):
    current_movie.title = title
    current_movie.year = year
    current_movie.director = director
    current_movie.genre = genre
    db.session.commit()


def get_movies_by_year_range(from_year, to_year):
    return Movie.query.filter(Movie.year >= from_year, Movie.year <= to_year).all()
