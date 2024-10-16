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
