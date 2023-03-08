"""
This module contains functions to perform CRUD operations on `Review` table.
"""
from cinemate_app import db
from ..models import Review


def get_all_reviews():
    """
    Selects all reviews from the review table.

    :return: a list of reviews (or empty list if no reviews)
    """
    return Review.query.all()


def get_review_by_id(review_id):
    """
    Selects infromation about review with the specified id.

    :param int review_id: id of the review.
    :return: Review or None.
    """
    return Review.query.get(review_id)


def delete_review(review):
    """
    Deletes review from the reviews table.

    :param Review review: Review object that represent a record to delete.
    :return: None
    """
    db.session.delete(review)
    db.session.commit()


def add_review(movie, nickname, score, comment):
    """
    Adds a new review to reviews table.

    :param Movie movie: Movie object that represent a movie to add a review to.
    :param str nickname: Nickname of the user that left the review.
    :param int score: Score given to the movie by the user.
    :param str comment: A few words about movie itself.
    :return: None.
    """
    new_review = Review(nickname=nickname, score=score, comment=comment, movie=movie)
    db.session.add(new_review)
    db.session.commit()


def update_review(current_review, nickname, score, comment):
    """
    Updates a review record in the reviews table.

    :param Review current_review: an object that represent review to update.
    :param str nickname: new nickname of the user.
    :param int score: new score given to a movie.
    :param str comment: new comment.
    :return: None.
    """
    current_review.nickname = nickname
    current_review.score = score
    current_review.comment = comment
    db.session.commit()
