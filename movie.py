# movie.py
class Movie:
    def __init__(self, name, genre, director, lead_actors, imdb_rating, personal_rating, notes, user=None):
        self.name = name
        self.genre = genre
        self.director = director
        self.lead_actors = lead_actors
        self.imdb_rating = imdb_rating
        self.personal_rating = personal_rating
        self.notes = notes
        self.user = user  # Kullanıcıyı ekledik

    def __repr__(self):
        return f"Movie(name='{self.name}', genre='{self.genre}', director='{self.director}', imdb_rating={self.imdb_rating}, personal_rating={self.personal_rating})"
