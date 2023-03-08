"""
This module contains classes to work with movies via RESTful API.
"""
from flask_restful import Resource
from cinemate_app.service import movie_service, review_service
from .utils import INVALID_MOVIE_MESSAGE, INVALID_REVIEW_MESSAGE, NO_MOVIE
from .utils import movie_validator, review_validator, movie_parser, review_parser


class MovieList(Resource):
    """
    This class contains methods for /api/movies route.
    It manages operations with movies - allows to read them and add new ones.
    """

    @staticmethod
    def get():
        """
        This method is called when GET request is received.
        It allows to fetch all the movies from db.

        :return: a list of all movies in JSON format or an error message.
        """
        movies = movie_service.get_all_movies()
        if movies:
            return {'movies': [movie.as_dict() for movie in movies]}
        return {'message': 'No movies in DB'}

    @staticmethod
    def post():
        """
        This method is called when POST request is received.
        It allows to add new movies to db.

        :return: information message (success or error).
        """
        args = movie_parser.parse_args()
        if not movie_validator(args):
            return {'message': INVALID_MOVIE_MESSAGE}, 400  # Bad request
        movie_service.add_movie(title=args['title'], year=args['year'],
                                director=args['director'], genre=args['genre'])
        return {'message': 'Movie added successfully!'}


class Movie(Resource):
    """
    This class contains methods for /api/movie/<int:movie_id> route.
    It allows to perform CRUD operations (fetch info about movie,
    update info about existing movie, add reviews to a movie, delete movies).
    """

    @staticmethod
    def get(movie_id):
        """
        This method is called when GET request is received.
        It allows to fetch a movie from DB by id.

        :param movie_id: id of the movie.
        :return: movie info as JSON or error message.
        """
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'message': NO_MOVIE}, 404
        result = movie.as_dict()
        result.update({'score': movie.calculate_score()})
        return result

    @staticmethod
    def put(movie_id):
        """
        This method is called when PUT request is received.
        It allows to update info movie info in DB.

        :param movie_id: id of the movie.
        :return: information message (error / success).
        """
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'message': NO_MOVIE}, 404
        args = movie_parser.parse_args()
        if not movie_validator(args):
            return {'message': INVALID_MOVIE_MESSAGE}, 400
        movie_service.update_movie(movie, title=args['title'], year=args['year'],
                                   director=args['director'], genre=args['genre'])
        return {'message': 'Movie updated successfully.'}

    @staticmethod
    def post(movie_id):
        """
        This method is called when POST request is received.
        It allows to add a new review for movie.

        :param movie_id: id of the movie.
        :return: information message (success or error).
        """
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'message': NO_MOVIE}, 404
        args = review_parser.parse_args()
        if not review_validator(args):
            return {'message': INVALID_REVIEW_MESSAGE}, 400
        review_service.add_review(movie=movie, nickname=args['nickname'],
                                  score=args['score'], comment=args['comment'])
        return {'message': f'New review to {movie.title} was added successfully.'}

    @staticmethod
    def delete(movie_id):
        """
        This method is called when DELETE request is received.
        It allows to delete movies from DB.

        :param movie_id: id of the movie.
        :return: information message (success or error).
        """
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'message': NO_MOVIE}, 404
        movie_service.delete_movie(movie)
        return {'message': 'This movie was successfully deleted.'}
