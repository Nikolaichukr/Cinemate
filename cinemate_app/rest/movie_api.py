from flask_restful import Resource
from cinemate_app.service import movie_service, review_service
from .utils import INVALID_MOVIE_MESSAGE, INVALID_REVIEW_MESSAGE, NO_MOVIE
from .utils import movie_validator, review_validator, movie_parser, review_parser


class MovieList(Resource):

    @staticmethod
    def get():
        movies = movie_service.get_all_movies()
        if movies:
            return {'movies': [movie.as_dict() for movie in movies]}
        return {'Message': 'No movies in DB'}

    @staticmethod
    def post():
        args = movie_parser.parse_args()
        if not movie_validator(args):
            return {'Message': INVALID_MOVIE_MESSAGE}, 400  # Bad request
        movie_service.add_movie(title=args['title'], year=args['year'], director=args['director'], genre=args['genre'])
        return {'Message': 'Movie added successfully!'}


class Movie(Resource):

    @staticmethod
    def get(movie_id):
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'Message': NO_MOVIE}, 404
        result = movie.as_dict()
        result.update({'score': movie.calculate_score()})
        return result

    @staticmethod
    def put(movie_id):
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'Message': NO_MOVIE}, 404
        args = movie_parser.parse_args()
        if not movie_validator(args):
            return {'Message': INVALID_MOVIE_MESSAGE}, 400
        movie_service.update_movie(movie, title=args['title'], year=args['year'], director=args['director'],
                                   genre=args['genre'])
        return {'Message': 'Movie updated successfully.'}

    @staticmethod
    def post(movie_id):
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'Message': NO_MOVIE}, 404
        args = review_parser.parse_args()
        if not review_validator(args):
            return {'Message': INVALID_REVIEW_MESSAGE}, 400
        review_service.add_review(movie=movie, nickname=args['nickname'], score=args['score'], comment=args['comment'])
        return {'Message': f'New review to {movie.title} was added successfully.'}

    @staticmethod
    def delete(movie_id):
        movie = movie_service.get_movie_by_id(movie_id)
        if movie is None:
            return {'Message': NO_MOVIE}, 404
        movie_service.delete_movie(movie)
        return {'Message': 'This movie was successfully deleted.'}
