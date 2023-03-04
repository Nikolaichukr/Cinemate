from flask import Blueprint, render_template, redirect, url_for, flash
from cinemate_app.service import review_service, movie_service
from cinemate_app.forms import ReviewForm

reviews = Blueprint('reviews', __name__)


@reviews.route('/')
def reviews_page():
    reviews_list = review_service.get_all_reviews()
    return render_template('reviews.html', title="List of Reviews", reviews_list=reviews_list)


@reviews.route('/review/<int:review_id>')
def review(review_id):
    current_review = review_service.get_review_by_id(review_id)
    if current_review is None:
        flash("The review page you requested does not exist.", "error")
        return redirect(url_for("reviews.reviews_page"))
    return render_template('review.html', review=current_review)


@reviews.route('/add_review/<int:movie_id>', methods=["GET", "POST"])
def add_review(movie_id):
    movie = movie_service.get_movie_by_id(movie_id)
    if movie is not None:
        form = ReviewForm()
        if form.validate_on_submit():
            review_service.add_review(movie=movie, nickname=form.nickname.data, score=form.score.data,
                                      comment=form.comment.data)
            flash(f'A new review for "{movie.title}" was published successfully!', "success")
            return redirect(url_for("movies.movie", movie_id=movie_id))
    else:
        flash("The movie you are trying to add a review to does not exist.", "error")
        return redirect(url_for("movies.movies_page"))
    return render_template('add_review.html', title="Add Review", movie=movie, form=form)


@reviews.route('/update_review/<int:review_id>', methods=["GET", "POST"])
def update_review(review_id):
    current_review = review_service.get_review_by_id(review_id)
    if current_review is not None:
        form = ReviewForm(obj=current_review)
        if form.validate_on_submit():
            review_service.update_review(current_review=current_review, nickname=form.nickname.data,
                                         score=form.score.data, comment=form.comment.data)
            flash(f'A review for "{current_review.movie.title}" was updated successfully!', "success")
            return redirect(url_for('reviews.review', review_id=review_id))
    else:
        flash("The review you are trying to update does not exist!", "error")
        return redirect(url_for("movies.movies_page"))
    return render_template('update_review.html', title="Update Review", form=form, review=current_review)


@reviews.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    review_to_delete = review_service.get_review_by_id(review_id)
    if review_to_delete is not None:
        review_service.delete_review(review_to_delete)
        flash(f"Review by {review_to_delete.nickname} was deleted successfully!", "success")
    else:
        flash(f"Requested review does not exist, so can't be deleted!", "error")
    return redirect(url_for("reviews.reviews_page"))
