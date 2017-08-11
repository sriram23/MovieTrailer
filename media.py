import webbrowser

class Movie():
    
    """The function __init__ will initialise the instances.
    The function show_trailer, when called will open a browser
    and runs the trailer"""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
    
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        print self.trailer_youtube_url
