from flask_restful import reqparse

INVALID_REVIEW_MESSAGE = "Invalid data provided! All fields should contain at least one symbol. " \
                         "Nickname should be less then 70 symbols, score should be in range from 1 to 10," \
                         "comment should be less then 2048 symbols."

INVALID_MOVIE_MESSAGE = 'Invalid data provided! The title and genre length should be from 1 to 150 symbols long, ' \
                        'director length should be from 1 to 100 symbols long, ' \
                        'the year should be between 1900 and 2025'

NO_MOVIE = 'Movie with this ID does not exist.'
NO_REVIEW = 'Review with this ID does not exist.'

review_parser = reqparse.RequestParser()
review_parser.add_argument('nickname', type=str, required=True, help='Nickname is required (string)')
review_parser.add_argument('score', type=int, required=True, help='Score is required (integer)')
review_parser.add_argument('comment', type=str, required=True, help='Comment is required (string)')

movie_parser = reqparse.RequestParser()
movie_parser.add_argument('title', type=str, required=True, help='Title key is required (string)')
movie_parser.add_argument('year', type=int, required=True, help='Year key is required (integer)')
movie_parser.add_argument('director', type=str, required=True, help='Director key is required (string)')
movie_parser.add_argument('genre', type=str, required=True, help='Genre key is required (string)')


def review_validator(args):
    return all([1 <= len(args['nickname']) <= 70, 1 <= args['score'] <= 10, 1 <= len(args['comment']) <= 2048])


def movie_validator(args):
    return all([1 <= len(args['title']) <= 150, 1900 <= args['year'] <= 2025, 1 <= len(args['director']) <= 100,
                1 <= len(args['genre']) <= 150])
