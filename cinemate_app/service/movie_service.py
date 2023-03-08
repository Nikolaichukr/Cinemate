"""
This module contains functions to perform CRUD operations on `Movie` table.
"""
from cinemate_app import db
from ..models import Movie


def get_all_movies():
    """
    This function selects all movies from the database.

    :return: a list of movies (or empty list of no movies).
    """
    return Movie.query.all()


def get_movie_by_id(movie_id):
    """
    This function selects a movie from the movies table by id.

    :param int movie_id: id of the movie.
    :return: Movie or None.
    """
    return Movie.query.get(movie_id)


def delete_movie(movie):
    """
    This function deletes movie from the database.

    :param Movie movie: Movie object.
    :return: None.
    """
    db.session.delete(movie)
    db.session.commit()


def add_movie(title, year, director, genre):
    """
    This function adds a new movie to the movies tables.

    :param str title: movie title.
    :param int year: year the movie was released.
    :param str director: name of the person who directed the movie.
    :param str genre: genre(s).
    :return: None.
    """
    new_movie = Movie(title, year, director, genre)
    db.session.add(new_movie)
    db.session.commit()


def update_movie(current_movie, title, year, director, genre):
    """
    This function updates information about movie in movie table.

    :param Movie current_movie: movie that should be updated.
    :param str title: new movie title.
    :param int year: new release year.
    :param str director: new director name.
    :param genre: new genre(s).
    :return: None.
    """
    current_movie.title = title
    current_movie.year = year
    current_movie.director = director
    current_movie.genre = genre
    db.session.commit()


def get_movies_by_year_range(from_year, to_year):
    """
    This movie selects all movies,
    that were released in a range of [from_year; to_year].

    :param int from_year: year the oldest movie was released.
    :param int to_year: year the newest movie was released.
    :return: Movie list or None.
    """
    return Movie.query.filter(Movie.year >= from_year, Movie.year <= to_year).all()
