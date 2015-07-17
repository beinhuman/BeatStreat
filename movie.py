import webbrowser

class Movie():
    def __init__(self,title,storyline,poster,trailer):
        self.movie_title=title
        self.movie_storyline=storyline
        self.movie_poster=poster
        self.movie_trailer=trailer
    def show_trailer(self):
        webbrowser.open(self.movie_trailer)
        
        
