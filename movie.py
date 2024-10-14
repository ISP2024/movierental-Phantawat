class PriceStrategy:
    """Base class for price strategies."""
    def get_price(self, days_rented):
        raise NotImplementedError("This method should be overridden.")

    def get_rental_points(self, days_rented):
        raise NotImplementedError("This method should be overridden.")

class RegularPrice(PriceStrategy):
    """Price strategy for regular movies."""
    def get_price(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount

    def get_rental_points(self, days_rented):
        return 1

class ChildrensPrice(PriceStrategy):
    """Price strategy for children's movies."""
    def get_price(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount

    def get_rental_points(self, days_rented):
        return 1

class NewReleasePrice(PriceStrategy):
    """Price strategy for new release movies."""
    def get_price(self, days_rented):
        return 3 * days_rented

    def get_rental_points(self, days_rented):
        return days_rented

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

    def get_price_code(self):
        return self.price_code

    def get_price(self, days_rented):
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        return self.price_strategy.get_rental_points(days_rented)