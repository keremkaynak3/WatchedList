# moviedatabase.py
import sqlite3

class MovieDatabase:
    def __init__(self, db_name='movies.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            genre TEXT,
                            director TEXT,
                            lead_actors TEXT,
                            imdb_rating REAL,
                            personal_rating REAL,
                            notes TEXT)''')
        self.conn.commit()

    def add_movie(self, movie):
        cursor = self.conn.cursor()
        # Aynı isimde bir film olup olmadığını kontrol ediyoruz
        cursor.execute('SELECT * FROM movies WHERE name = ?', (movie.name,))
        result = cursor.fetchone()

        if result:
            print(f"{movie.name} is already in the database.")
        else:
            cursor.execute('''
                INSERT INTO movies (name, genre, director, lead_actors, imdb_rating, personal_rating, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (movie.name, movie.genre, movie.director, movie.lead_actors, movie.imdb_rating, movie.personal_rating,
                  movie.notes))
            self.conn.commit()
            print(f"{movie.name} has been added to the database.")

    def get_movies(self):
        self.cursor.execute('SELECT * FROM movies')
        return self.cursor.fetchall()

    def get_movie_by_name(self, name):
        self.cursor.execute('SELECT * FROM movies WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def update_movie(self, movie_name, personal_rating=None, notes=None):
        with self.conn:
            if personal_rating:
                self.cursor.execute('UPDATE movies SET personal_rating = ? WHERE name = ?', (personal_rating, movie_name))
            if notes:
                self.cursor.execute('UPDATE movies SET notes = ? WHERE name = ?', (notes, movie_name))

    def delete_movie(self, movie_name):
        with self.conn:
            self.cursor.execute('DELETE FROM movies WHERE name = ?', (movie_name,))
