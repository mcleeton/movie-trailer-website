#5/27/15     Michael Cleeton     cleeton.m@gmail.com
#Generated from Udacity's Programming Fundamentals with Python Course and modified by me

#imports built-in python library webbrowser
import webbrowser

class Movie():

    """ This class provides a way to store movie related infomation"""


    def __init__(self, movie_title, movie_rating, movie_info_page, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.rating = movie_rating
        self.info_page = movie_info_page
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """Provides class Movie with a function to open a web browser window and show its trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
