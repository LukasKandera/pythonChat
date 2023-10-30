class Movie:
    def __init__(self, title, year, genre, duration, director):
        self._title = title
        self._year = year
        self._genre = genre
        self._duration = duration
        self._director = director

    def print(self):
        print("| {:20} | {:4} | {:6} | {:3}m | {:10}".format(
            self._title,
            self._year,
            self._genre,
            self._duration,
            self._director
        ))


class Library:
    def __init__(self):
        self._movie_library = list()

    def seed(self):
        movie = Movie("Matrix", 1999, "scifi", 136, "Wachowski")
        self._movie_library.append(movie)
        movie = Movie("Jurrasic Park", 1993, "action", 127, "Spielberg")
        self._movie_library.append(movie)
        movie = Movie("Stargate", 1994, "scifi", 128, "Oneil")
        self._movie_library.append(movie)

    def print(self):
        print("| {:20} | {:4} | {:6} | {:3}m | {:10}".format(
            "Title",
            "Year",
            "Genre",
            "Time",
            "Director"
        ))
        for i in self._movie_library:
            i.print()

    def add_movie(self):
        title = input("Write movie title(and press Enter):")
        while True:
            try:
                year = int(input("Write movie title(and press Enter):"))
            except ValueError:
                print("Please enter a valid year in range 1900-2023")
                continue
            if year >= 1900 and year <= 2023:
                print("The entered year of movie {0} has been accepted".format(year))
                break
            else:
                print("Please enter a valid year in range 1900-2023")

            while True:
                try:
                    genre = str(input("Write movie genre(and press Enter):"))
                except ValueError:
                    print("Please enter a valid genre containing 2-20 characters")
                    continue
                if genre.isnumeric() == False and len(genre) >= 2 and len(genre) <= 20:
                    print("The entered genre of movie {0} has been accepted".format(genre))
                    break
                else:
                    print("Please enter a valid genre containing 2-20 characters")

            while True:
                try:
                    duration = int(input("Write movie duration in minutes(and press Enter):"))
                except ValueError:
                    print("Please enter a valid duration in minutes in range 10-600")
                    continue
                if duration >= 10 and duration <= 600:
                    print("The entered duration of movie {0}m has been accepted".format(duration))
                    break
                else:
                    print("Please enter a valid duration in minutes in range 10-600")

            while True:
                try:
                    director = str(input("Write movie director(and press Enter):"))
                except ValueError:
                    print("Please enter a valid director's surname containing 2-20 characters")
                    continue
                if director.isnumeric() == False and len(director) >= 2 and len(director) <= 20:
                    print("The entered director of movie {0} has been accepted".format(director))
                    break
                else:
                    print("Please enter a valid director's surname containing 2-20 characters")

        self._movie_library.append(Movie(title, year, genre, duration, director))

    def find_movie(self, title):
        for i in self._movie_library:
            if i._title == title:
                return i
        return None

    def delete_movie(self):
        self.print()
        print()
        title = input("Enter the title to be removed: ")
        movie = self.find_movie(title)
        if movie == None:
            print("Movie with title {} wasn't found.".format(title))
            return
        self._movie_library.remove(movie)

    def menu(self):
        print("0 -> Add movie")
        print("1 -> Remove movie")
        print("2 -> Print movies lib")
        print("3 -> Save movies lib")
        print("q -> Exit")
        print()
        choice = input("Select an option (0-3, q): ")
        if choice == "0":
            self.add_movie()
        elif choice == "1":
            self.delete_movie()
        elif choice == "2":
            self.print()
        elif choice == "3":
            self.save_movie_library()
        else:
            exit()

    def banner(self):
        print("Movie library, version 0.1a1")
        print()

    def save_movie_library(self):
        subor = open('movie_library.txt','w')
        subor.write("| {:20} | {:4} | {:6} | {:3}m | {:10}".format(
            "Title",
            "Year",
            "Genre",
            "Time",
            "Director"
        ))
        for i in self._movie_library:
            subor.write("\n| {:20} | {:4} | {:6} | {:3}m | {:10}".format(
                i._title,
                str(i._year),
                i._genre,
                str(i._duration),
                i._director
            ))
        subor.close


if __name__ == '__main__':
    lib = Library()
    lib.seed()

    lib.banner()
    while True:
        lib.menu()
