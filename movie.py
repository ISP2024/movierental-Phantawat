from pricing import *


class Movie:
    """A movie that can be rented."""
    
    REGULAR = 0
    CHILDRENS = 2
    NEW_RELEASE = 1

    def __init__(self, title: str, price_code: str):
        self.title = title
        self.price_code = price_code
        self.price_strategy = self._set_price_strategy()

    def _set_price_strategy(self):
        if self.price_code == self.REGULAR:
            return RegularPrice()
        elif self.price_code == self.CHILDRENS:
            return ChildrensPrice()
        elif self.price_code == self.NEW_RELEASE:
            return NewReleasePrice()
        else:
            raise ValueError(f"Unknown price code: {self.price_code}")

    def get_title(self):
        return self.title

    def get_price_strategy(self):
        return self.price_strategy
