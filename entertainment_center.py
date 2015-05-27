# 5/27/15   Michael Cleeton   cleeton.m@gmail.com
#Generated from Udacity's Programming Fundamentals with Python Course and modified by me


# imports the functions from built-in library media and the file
# fresh_tomatoes.py
import media
import fresh_tomatoes


""" Entertainment Center holds all instances of class media,
    similar to a shelf of dvds or media library """

fantastic_mr_fox = media.Movie("Fantastic Mr Fox", "PG", "http://www.imdb.com/title/tt0432283",
                               "A cunning fox outwits three farmers and saves his family.",
                               "http://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg",
                               "https://www.youtube.com/watch?v=n2igjYFojUo")

batman_begins = media.Movie("Batman Begins", "PG-13", "http://www.imdb.com/title/tt0372784",
                            "A wealthy orphan grows into a hero to save his city from a great evil",
                            "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                            "www.youtube.com/watch?v=vak9ZLfhGnQ")

big_trouble = media.Movie("Big Trouble in Little China", "PG-13", "http://www.imdb.com/title/tt0090728",
                          "A trucker gets lost in china town",
                          "http://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                          "www.youtube.com/watch?v=592EiTD2Hgo")

train_dragon = media.Movie("How to Train Your Dragon", "PG", "http://www.imdb.com/title/tt0892769",
                           "A young man eschews the tradition of his viking family and befriends a dragon",
                           "http://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                           "www.youtube.com/watch?v=oKiYuIsPxYk")

ratatouille = media.Movie("Ratatouille", "G", "http://www.imdb.com/title/tt0382932",
                          "A Rat in Paris becomes a chef",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "http://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "PG-13", "http://www.imdb.com/title/tt1605783",
                                "While traveling in Paris, a nostalgic screenwriter experiences the 1920s every evening",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")


# List of all movies in our library
movies = [fantastic_mr_fox, batman_begins, big_trouble,
          train_dragon, ratatouille, midnight_in_paris]


"""Calls the function from fresh_tomatoes.py to create the
    movie webpage """
fresh_tomatoes.open_movies_page(movies)
