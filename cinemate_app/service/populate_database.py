from cinemate_app import app, db
from cinemate_app.models.movies import Movie
from cinemate_app.models.reviews import Review


def populate_with_dummy_data():
    with app.app_context():
        inception = Movie('Inception', 2010, 'Christopher Nolan', 'Sci-Fi')
        pulp_fiction = Movie('Pulp Fiction', 1994, 'Quentin Tarantino', 'Crime')
        the_dark_knight = Movie('The Dark Knight', 2008, 'Christopher Nolan', 'Action')
        shawshank_redemption = Movie('The Shawshank Redemption', 1994, 'Frank Darabont', 'Drama')
        the_godfather = Movie('The Godfather', 1972, 'Francis Ford Coppola', 'Crime')

        Review('MovieFan36', 8, 'Great movie, loved the concept and the execution', inception)
        Review('SciFiGeek90', 9, 'One of the best sci-fi movies I have seen', inception)
        Review('DreamCrafter', 6, 'A bit too complex for my taste, but still a decent movie', inception)
        Review('MindBlown22', 10, 'Absolutely mind-blowing, loved every minute of it', inception)
        Review('FilmBuff42', 7, 'Interesting plot, but could have been executed better', pulp_fiction)
        Review('Cinephile101', 9, 'One of the best movies I have seen, amazing dialogue and performances', pulp_fiction)
        Review('MovieLover88', 8, 'Great acting and cinematography, but a bit too violent for me', pulp_fiction)
        Review('DarkKnightFan', 10, 'One of the best superhero movies ever made, Heath Ledger was phenomenal',
               the_dark_knight)
        Review('ComicBookNerd', 9, 'Great plot, amazing performances, a must-watch for any superhero fan',
               the_dark_knight)
        Review('JokerFan123', 7, 'A bit too dark and intense for my taste, but still a great movie', the_dark_knight)
        Review('BookWorm22', 9, 'One of the most inspiring and uplifting movies I have seen, amazing performances',
               shawshank_redemption)
        Review('DramaQueen', 8, 'Great plot, but a bit slow at times', shawshank_redemption)
        Review('MovieGuru55', 9, 'A masterpiece, one of the best movies ever made', the_godfather)
        Review('CorleoneFan', 10, 'Absolutely loved it, amazing performances and storytelling', the_godfather)
        Review('ClassicFilmFan', 8, 'Great movie, but a bit too long for my taste', the_godfather)

        # Add the movies and reviews to the database
        db.session.add_all([inception, pulp_fiction, the_dark_knight, shawshank_redemption, the_godfather])
        db.session.commit()


if __name__ == "__main__":
    print("Populating the database with dummy data...")
    populate_with_dummy_data()
    print("Database populated successfully!")
