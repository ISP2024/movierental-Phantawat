import unittest
from datetime import datetime
from movie import Movie, price_code_for_movie, NEW_RELEASE, CHILDRENS, REGULAR

class TestPriceCodeForMovie:
    def setup_method(self):
        """Setup method to create common test data."""
        self.current_year = datetime.now().year
        self.new_release_movie = Movie("Brand New Blockbuster", self.current_year, ["Action", "Adventure"])
        self.children_movie = Movie("Classic Animated Film", 1995, ["Children", "Fantasy"])
        self.childrens_movie = Movie("Modern Kids Movie", 2020, ["Childrens", "Comedy"])
        self.regular_movie = Movie("Drama Masterpiece", 2015, ["Drama", "Romance"])
        self.sci_fi_movie = Movie("Sci-fi Classic", 1982, ["Science Fiction"])
        self.case_insensitive_child_movie = Movie("Another Kid's Movie", 1998, ["children"])

    def test_price_code_for_new_release(self):
        assert price_code_for_movie(self.new_release_movie) == NEW_RELEASE

    def test_price_code_for_childrens_movie(self):
        assert price_code_for_movie(self.children_movie) == CHILDRENS
        assert price_code_for_movie(self.childrens_movie) == CHILDRENS

    def test_price_code_for_regular_movie(self):
        assert price_code_for_movie(self.regular_movie) == REGULAR
        assert price_code_for_movie(self.sci_fi_movie) == REGULAR

    def test_case_insensitive_genre_check(self):
        assert price_code_for_movie(self.case_insensitive_child_movie) == CHILDRENS
