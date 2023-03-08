"""This module is used to work with review-related views"""

from flask import Blueprint, render_template, redirect, url_for, flash
from cinemate_app.service import review_service, movie_service
from cinemate_app.forms import ReviewForm

reviews = Blueprint('reviews', __name__)


@reviews.route('/')
def reviews_page():
    """
    This function represents the page that provides
    the list of all the reviews that exist in the database.

    :return: rendered `reviews.html` template.
    """
    reviews_list = review_service.get_all_reviews()
    return render_template('reviews.html', title="List of Reviews", reviews_list=reviews_list)


@reviews.route('/review/<int:review_id>')
def review(review_id):
    """
    This function represent the review page for the particular movie.
    It contains links to update/delete forms and the movie page itself.

    :param int review_id: id of the review.
    :return: rendered `review.html` template or redirect to reviews page.
    """
    current_review = review_service.get_review_by_id(review_id)
    if current_review is None:
        flash("The review page you requested does not exist.", "error")
        return redirect(url_for("reviews.reviews_page"))
    return render_template('review.html', review=current_review)


@reviews.route('/add_review/<int:movie_id>', methods=["GET", "POST"])
def add_review(movie_id):
    """
    This function enables user to add new reviews to the movie.
    It renders add review form and adds movie if the data is valid.

    :param int movie_id: id of the movie to add a review to.
    :return: rendered `add_review.html` or redirect to movie(s) page.
    """
    movie = movie_service.get_movie_by_id(movie_id)
    if movie is not None:
        form = ReviewForm()
        if form.validate_on_submit():
            review_service.add_review(movie=movie, nickname=form.nickname.data,
                                      score=form.score.data, comment=form.comment.data)
            flash(f'A new review for "{movie.title}" was published successfully!', "success")
            return redirect(url_for("movies.movie", movie_id=movie_id))
    else:
        flash("The movie you are trying to add a review to does not exist.", "error")
        return redirect(url_for("movies.movies_page"))
    return render_template('add_review.html', title="Add Review", movie=movie, form=form)


@reviews.route('/update_review/<int:review_id>', methods=["GET", "POST"])
def update_review(review_id):
    """
    This function allows to update review.
    It provides user with from that contains prepopulated field
    with the information of the current review based on id.

    :param int review_id: id of the review to update.
    :return: rendered `update.html` template or redirect to review/main page.
    """
    current_review = review_service.get_review_by_id(review_id)
    if current_review is not None:
        form = ReviewForm(obj=current_review)
        if form.validate_on_submit():
            review_service.update_review(current_review=current_review, nickname=form.nickname.data,
                                         score=form.score.data, comment=form.comment.data)
            flash(f'A review for "{current_review.movie.title}" '
                  f'was updated successfully!', "success")

            return redirect(url_for('reviews.review', review_id=review_id))
    else:
        flash("The review you are trying to update does not exist!", "error")
        return redirect(url_for("movies.movies_page"))
    return render_template('update_review.html', title="Update Review",
                           form=form, review=current_review)


@reviews.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    """
    This function represents the logic for delete review page.

    :param int review_id: id of the review to delete.
    :return: redirect to reviews page.
    """
    review_to_delete = review_service.get_review_by_id(review_id)
    if review_to_delete is not None:
        review_service.delete_review(review_to_delete)
        flash(f"Review by {review_to_delete.nickname} was deleted successfully!", "success")
    else:
        flash("Requested review does not exist, so can't be deleted!", "error")
    return redirect(url_for("reviews.reviews_page"))
