"""This module is used to work with movie-related views"""
from flask import Blueprint, render_template, redirect, url_for, flash
from cinemate_app.service import movie_service
from cinemate_app.forms import MovieForm, FilterMovieByYearForm

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['POST', 'GET'])
def movies_page():
    """
    This function is used to render main page.
    This page contains a list of all movies.
    It also gives an ability to filter them by year
    and a link to add form.

    :return: rendered `movies.html` template.
    """
    movie_list = movie_service.get_all_movies()
    filter_form = FilterMovieByYearForm()
    empty_message = "There are no movies in database right now, but you can always add one."
    from_year, to_year = 1900, 2025
    if filter_form.validate_on_submit():
        from_year, to_year = filter_form.from_year.data, filter_form.to_year.data
        movie_list = movie_service.get_movies_by_year_range(from_year, to_year)
        if not movie_list:
            empty_message = f"There are no movies between the {from_year} " \
                            f"and the {to_year} in our database."

    return render_template('movies.html', title="List of Movies",
                           movie_list=movie_list, filter_form=filter_form,
                           empty_message=empty_message, from_year=from_year, to_year=to_year)


@movies.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
    This function represents movie-view.
    It contains all the information about particular movie
    and hyperlink to update/delete functionality.
    There is also an option to go to the add review form.

    :param int movie_id: id of the movie.
    :return: rendered `movie.html` template or redirect to main page.
    """
    current_movie = movie_service.get_movie_by_id(movie_id)
    if current_movie is None:
        flash("The movie page you requested is missing.", "error")
        return redirect(url_for("movies.movies_page"))
    return render_template('movie.html', movie=current_movie)


@movies.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    """
    This function is designed to add movies into the database.

    :return: rendered `add_movie.html` template or redirect to main page.
    """
    form = MovieForm()
    if form.validate_on_submit():
        movie_service.add_movie(title=form.title.data, year=form.year.data,
                                director=form.director.data, genre=form.genre.data)
        flash(f'"{form.title.data}" was added successfully!', "success")
        return redirect(url_for("movies.movies_page"))
    return render_template('add_movie.html', title="Add Movie", form=form)


@movies.route('/update_movie/<int:movie_id>', methods=['POST', 'GET'])
def update_movie(movie_id):
    """
    This function represent a view which is used to update existing movie info.

    :param int movie_id: id of the movie to update.
    :return: rendered `update movie.html` template or redirect to main/movie page.
    """
    current_movie = movie_service.get_movie_by_id(movie_id)
    if current_movie is not None:
        form = MovieForm(obj=current_movie)
        if form.validate_on_submit():
            movie_service.update_movie(current_movie=current_movie, title=form.title.data,
                                       year=form.year.data, director=form.director.data,
                                       genre=form.genre.data)
            flash(f'"{form.title.data}" was updated successfully!', "success")
            return redirect(url_for("movies.movie", movie_id=movie_id))
    else:
        flash("The movie you requested to update does not exist.", "error")
        return redirect(url_for("movies.movies_page"))

    return render_template('update_movie.html', title="Update Movie Info",
                           form=form, movie=current_movie)


@movies.route('/delete_movie/<int:movie_id>')
def delete_movie(movie_id):
    """
    This function is used to delete movies from the database by their id.

    :param int movie_id: id of the movie to delete.
    :return: redirect to main page.
    """
    current_movie = movie_service.get_movie_by_id(movie_id)
    if current_movie is not None:
        movie_service.delete_movie(movie=current_movie)
        flash(f'"{current_movie.title}" was deleted successfully!', "success")
    else:
        flash("The movie you requested to delete does not exist.", "error")
    return redirect(url_for("movies.movies_page"))
