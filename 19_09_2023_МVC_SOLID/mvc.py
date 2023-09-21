# class TaskModel:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
#     def get_tasks(self):
#         return self.tasks
#
#
# class TaskView:
#     def show_tasks(self, tasks):
#         for task in tasks:
#             print(task)
#
#     def prompt_new_task(self):
#         return input("Введіть нове завдання: ")
#
#
# class TaskController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def add_task(self, task):
#         self.model.add_task(task)
#
#     def show_tasks(self):
#         tasks = self.model.get_tasks()
#         self.view.show_tasks(tasks)
#
#     def run(self):
#         while True:
#             choice = input("Оберіть опцію: \n"
#                            "1 - Додати завдання\n"
#                            "2 - Показати завдання\n"
#                            "q - Вийти\n:")
#             if choice == '1':
#                 task = self.view.prompt_new_task()
#                 self.add_task(task)
#             elif choice == '2':
#                 self.show_tasks()
#             elif choice == 'q':
#                 break
#
#
# if __name__ == '__main__':
#     view = TaskView()
#     model = TaskModel()
#     controller = TaskController(model, view)
#     controller.run()


# PRACTICE
# class Movie:
#     name
#     genre
#     producer
#     year
#     actors : list[str]

# MovieModel:
#   ...
#   def add_movie(name, genre, producer, year, actors)
#   def remove_movie(name)
#   def get_movies()
#   ...


class Movie:
    def __init__(self, name, genre, producer, year, duration, actor):
        self.name = name
        self.genre = genre
        self.producer = producer
        self.year = year
        self.duration = duration
        self.actor = actor

    def __str__(self):
        return f"{self.name}: Name, {self.genre}: Genre, {self.producer}: Producer, {self.year}: Year, {self.duration}: Duration, {self.actor}: Actor"


class MovieModel:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)

    def get_movies(self):
        return self.movies


class MovieViev:

    def show_movies(self, movies):
        for movie in movies:
            print(movie)

    def prompt_new_movie(self):
        name = input("Name -> ")
        genre = input("Genre ->  ")
        producer = input("Producer -> ")
        year = input("Year -> ")
        duration = input("Duration -> ")
        actors = input("Actors -> ")

        movie = {
            "name": name,
            "genre": genre,
            "producer": producer,
            "year": year,
            "duration": duration,
            "actors": actors
        }

        return movie


class MovieController:

    def __init__(self, movie, view):
        self.movie = movie
        self.view = view

    def add_movie(self, movie_dict):
        film = Movie(
            movie_dict["name"],
            movie_dict["genre"],
            movie_dict["producer"],
            movie_dict["year"],
            movie_dict["duration"],
            movie_dict["actors"]
        )
        self.movie.add_movie(film)

    def show_movies(self):
        movies = self.movie.get_movies()
        self.view.show_movies(movies)

    def run(self):
        while True:
            choice = input("Оберіть опцію: \n"
                           "1 - Додати фільм\n"
                           "2 - Показати фільм\n"
                           "q - Вийти\n:")
            if choice == '1':
                movie = self.view.prompt_new_movie()
                self.add_movie(movie)
            elif choice == '2':
                self.show_movies()
            elif choice == 'q':
                break


HR1 = Movie("HR1", "fantasy", "Maykle Kow", 2011, "3.03", "John Nim")
model = MovieModel()
view = MovieViev()
controller = MovieController(model, view)
controller.run()
