from moviedatabase import MovieDatabase

# Movie sınıfı
class Movie:
    def __init__(self, name, genre, director, lead_actors, imdb_rating, personal_rating, notes):
        self.name = name
        self.genre = genre
        self.director = director
        self.lead_actors = lead_actors
        self.imdb_rating = imdb_rating
        self.personal_rating = personal_rating
        self.notes = notes

    def __repr__(self):
        return f"Movie(name='{self.name}', genre='{self.genre}', director='{self.director}', imdb_rating={self.imdb_rating}, personal_rating={self.personal_rating})"

# Veritabanı nesnesini oluşturma
db = MovieDatabase()  # MovieDatabase sınıfını bir kez oluşturun

# Filmleri oluştur ve ekle
movie_1 = Movie(
    name="Inception", genre="Sci-Fi", director="Christopher Nolan",
    lead_actors="Leonardo DiCaprio, Joseph Gordon-Levitt", imdb_rating=8.8,
    personal_rating=9.5, notes="A mind-bending thriller."
)

movie_2 = Movie(
    name="The Matrix", genre="Action, Sci-Fi", director="The Wachowskis",
    lead_actors="Keanu Reeves, Laurence Fishburne", imdb_rating=8.7,
    personal_rating=9.0, notes="A revolutionary action film with groundbreaking effects."
)

movie_3 = Movie(
    name="Interstellar", genre="Adventure, Drama, Sci-Fi", director="Christopher Nolan",
    lead_actors="Matthew McConaughey, Anne Hathaway", imdb_rating=8.6,
    personal_rating=9.5, notes="A visually stunning film with deep emotional themes."
)

movie_4 = Movie(
    name="The Dark Knight", genre="Action, Crime, Drama", director="Christopher Nolan",
    lead_actors="Christian Bale, Heath Ledger", imdb_rating=9.0,
    personal_rating=9.7, notes="Heath Ledger's Joker is legendary."
)

movie_5 = Movie(
    name="Pulp Fiction", genre="Crime, Drama", director="Quentin Tarantino",
    lead_actors="John Travolta, Uma Thurman", imdb_rating=8.9,
    personal_rating=9.2, notes="Non-linear storytelling at its finest."
)

movie_6 = Movie(
    name="Fight Club", genre="Drama", director="David Fincher",
    lead_actors="Brad Pitt, Edward Norton", imdb_rating=8.8,
    personal_rating=9.3, notes="An introspective film on modern life and identity."
)

movie_7 = Movie(
    name="The Shawshank Redemption", genre="Drama", director="Frank Darabont",
    lead_actors="Tim Robbins, Morgan Freeman", imdb_rating=9.3,
    personal_rating=9.8, notes="A powerful story about hope and friendship."
)

movie_8 = Movie(
    name="Forrest Gump", genre="Drama, Romance", director="Robert Zemeckis",
    lead_actors="Tom Hanks, Robin Wright", imdb_rating=8.8,
    personal_rating=9.1, notes="A heartwarming and iconic American story."
)

movie_9 = Movie(
    name="The Godfather", genre="Crime, Drama", director="Francis Ford Coppola",
    lead_actors="Marlon Brando, Al Pacino", imdb_rating=9.2,
    personal_rating=9.5, notes="A masterpiece of American cinema."
)

movie_10 = Movie(
    name="Gladiator", genre="Action, Adventure, Drama", director="Ridley Scott",
    lead_actors="Russell Crowe, Joaquin Phoenix", imdb_rating=8.5,
    personal_rating=9.0, notes="An epic tale of revenge and honor."
)

# Filmleri veritabanına ekleme
movies_to_add = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6, movie_7, movie_8, movie_9, movie_10]

for movie in movies_to_add:
    db.add_movie(movie)  # Filmleri ekle

# Veritabanındaki tüm filmleri yazdırma
movies = db.get_movies()
for movie in movies:
    print(movie)
