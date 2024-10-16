class Movie:
    """A movie that can be rented."""
    
    def __init__(self, title: str):
        self.title = title

    def get_title(self):
        return self.title
