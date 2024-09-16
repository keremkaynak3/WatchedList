# gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from moviedatabase import MovieDatabase
from movie import Movie


class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie App")
        self.root.geometry("800x600")  # Increased window size for table
        self.db = MovieDatabase()  # Database object
        self.current_user = None  # Currently logged-in user

        # Start with the login screen
        self.login_screen()

    def login_screen(self):
        # Login Screen UI
        self.clear_screen()

        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Register", command=self.register_screen)
        self.register_button.pack(pady=10)

        self.forgot_password_button = tk.Button(self.root, text="Forgot Password", command=self.forgot_password)
        self.forgot_password_button.pack(pady=10)

    def register_screen(self):
        # Registration screen
        self.clear_screen()

        self.label_new_username = tk.Label(self.root, text="New Username:")
        self.label_new_username.pack(pady=10)
        self.entry_new_username = tk.Entry(self.root)
        self.entry_new_username.pack(pady=10)

        self.label_new_password = tk.Label(self.root, text="New Password:")
        self.label_new_password.pack(pady=10)
        self.entry_new_password = tk.Entry(self.root, show="*")
        self.entry_new_password.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Save", command=self.register_user)
        self.register_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.login_screen)
        self.back_button.pack(pady=10)

    def register_user(self):
        username = self.entry_new_username.get()
        password = self.entry_new_password.get()

        # Add user to database
        self.db.add_user(username, password)
        messagebox.showinfo("Success", "Registration completed!")
        self.login_screen()

    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "A password reset link has been sent!")

    def login(self):
        # User login
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.db.authenticate_user(username, password):  # User authentication
            self.current_user = username
            self.show_user_movies()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def show_user_movies(self):
        # Show movies of the current user
        self.clear_screen()

        tk.Label(self.root, text=f"Movies for user: {self.current_user}", font=('Helvetica', 16, 'bold')).pack(pady=10)

        # Create table to display movies
        self.table = ttk.Treeview(self.root, columns=(
        "Name", "Genre", "Director", "Lead Actors", "IMDb Rating", "Personal Rating", "Notes"), show='headings')
        self.table.heading("Name", text="Movie Name")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Director", text="Director")
        self.table.heading("Lead Actors", text="Lead Actors")
        self.table.heading("IMDb Rating", text="IMDb Rating")
        self.table.heading("Personal Rating", text="Personal Rating")
        self.table.heading("Notes", text="Notes")
        self.table.pack(fill=tk.BOTH, expand=True)

        # Add movies to the table
        movies = self.db.get_movies_by_user(self.current_user)
        for movie in movies:
            self.table.insert("", tk.END, values=(
            movie.name, movie.genre, movie.director, movie.lead_actors, movie.imdb_rating, movie.personal_rating,
            movie.notes))

        self.add_movie_button = tk.Button(self.root, text="Add Movie", command=self.add_movie_screen)
        self.add_movie_button.pack(pady=10)

        self.switch_user_button = tk.Button(self.root, text="Switch User", command=self.login_screen)
        self.switch_user_button.pack(pady=10)

        self.edit_movie_button = tk.Button(self.root, text="Edit Movie", command=self.edit_movie_screen)
        self.edit_movie_button.pack(pady=10)

    def add_movie_screen(self):
        # New screen to add a movie
        self.clear_screen()

        tk.Label(self.root, text="Add New Movie", font=('Helvetica', 14, 'bold')).pack(pady=10)

        self.entry_name = self.create_entry_with_label("Movie Name:")
        self.entry_genre = self.create_entry_with_label("Genre:")
        self.entry_director = self.create_entry_with_label("Director:")
        self.entry_lead_actors = self.create_entry_with_label("Lead Actors:")
        self.entry_imdb_rating = self.create_entry_with_label("IMDb Rating:")
        self.entry_personal_rating = self.create_entry_with_label("Personal Rating:")
        self.entry_notes = self.create_entry_with_label("Notes:")

        save_button = tk.Button(self.root, text="Save", command=self.save_movie)
        save_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.show_user_movies)
        back_button.pack(pady=10)

    def create_entry_with_label(self, text):
        # Helper function to create entry fields with labels
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=50)
        entry.pack(side=tk.RIGHT, padx=10)
        return entry

    def save_movie(self):
        # Save new movie to the database
        name = self.entry_name.get()
        genre = self.entry_genre.get()
        director = self.entry_director.get()
        lead_actors = self.entry_lead_actors.get()
        imdb_rating = float(self.entry_imdb_rating.get())
        personal_rating = float(self.entry_personal_rating.get())
        notes = self.entry_notes.get()

        # Create new movie object and save it to the database
        new_movie = Movie(name=name, genre=genre, director=director, lead_actors=lead_actors,
                          imdb_rating=imdb_rating, personal_rating=personal_rating, notes=notes,
                          user=self.current_user)
        self.db.add_movie(new_movie, self.current_user)

        messagebox.showinfo("Success", "Movie has been added!")
        self.show_user_movies()

    def edit_movie_screen(self):
        # Edit existing movie details
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a movie to edit!")
            return

        movie_values = self.table.item(selected_item)['values']
        movie_name = movie_values[0]

        self.clear_screen()
        tk.Label(self.root, text="Edit Movie", font=('Helvetica', 14, 'bold')).pack(pady=10)

        self.edit_entry_name = self.create_entry_with_label("Movie Name:")
        self.edit_entry_name.insert(0, movie_name)
        self.edit_entry_genre = self.create_entry_with_label("Genre:")
        self.edit_entry_genre.insert(0, movie_values[1])
        self.edit_entry_director = self.create_entry_with_label("Director:")
        self.edit_entry_director.insert(0, movie_values[2])
        self.edit_entry_lead_actors = self.create_entry_with_label("Lead Actors:")
        self.edit_entry_lead_actors.insert(0, movie_values[3])
        self.edit_entry_imdb_rating = self.create_entry_with_label("IMDb Rating:")
        self.edit_entry_imdb_rating.insert(0, movie_values[4])
        self.edit_entry_personal_rating = self.create_entry_with_label("Personal Rating:")
        self.edit_entry_personal_rating.insert(0, movie_values[5])
        self.edit_entry_notes = self.create_entry_with_label("Notes:")
        self.edit_entry_notes.insert(0, movie_values[6])

        save_button = tk.Button(self.root, text="Save", command=lambda: self.save_edited_movie(movie_name))
        save_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.show_user_movies)
        back_button.pack(pady=10)

    def save_edited_movie(self, old_name):
        # Save edited movie details to the database
        name = self.edit_entry_name.get()
        genre = self.edit_entry_genre.get()
        director = self.edit_entry_director.get()
        lead_actors = self.edit_entry_lead_actors.get()
        imdb_rating = float(self.edit_entry_imdb_rating.get())
        personal_rating = float(self.edit_entry_personal_rating.get())
        notes = self.edit_entry_notes.get()

        # Create new movie object and update it in the database
        updated_movie = Movie(name=name, genre=genre, director=director, lead_actors=lead_actors,
                              imdb_rating=imdb_rating, personal_rating=personal_rating, notes=notes,
                              user=self.current_user)
        self.db.update_movie(old_name, updated_movie, self.current_user)

        messagebox.showinfo("Success", "Movie has been updated!")
        self.show_user_movies()

    def clear_screen(self):
        # Clears all widgets from the screen
        for widget in self.root.winfo_children():
            widget.destroy()


# Function to start the GUI
def start_gui():
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
