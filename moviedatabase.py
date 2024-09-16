# moviedatabase.py
class MovieDatabase:
    def __init__(self):
        self.movies = []
        self.users = []  # Yeni kullanıcı listesi

    def add_user(self, username, password):
        self.users.append({'username': username, 'password': password})

    def authenticate_user(self, username, password):
        # Kullanıcı adı ve şifreyi kontrol et
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def add_movie(self, movie, user):
        # Filme kullanıcı adını ekle
        movie.user = user
        self.movies.append(movie)

    def get_movies_by_user(self, user):
        # Kullanıcıya göre filmleri getir
        return [movie for movie in self.movies if movie.user == user]
