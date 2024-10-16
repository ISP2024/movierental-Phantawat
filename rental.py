import logging
from pricing import *
from movie import Movie

class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """
   
   def __init__(self, movie, days_rented, price_code): 
      """Initialize a new movie rental object for
         a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented
      self.price_code = price_code
      self.price_strategy = self._set_price_strategy()

   def _set_price_strategy(self):
        if self.price_code == Movie.REGULAR:
            return RegularPrice()
        elif self.price_code == Movie.CHILDRENS:
            return ChildrensPrice()
        elif self.price_code == Movie.NEW_RELEASE:
            return NewReleasePrice()
        else:
            raise ValueError(f"Unknown price code: {self.price_code}")

   def get_movie(self):
        return self.movie

   def get_days_rented(self):
      return self.days_rented

   def get_price_code(self):
      return self.price_code

   def get_price(self):
      """Calculate movie price for statement."""
      return self.price_strategy.get_price(self.days_rented)

   def get_rental_points(self):
      """Calculate frequent renter points for this rental."""
      return self.price_strategy.get_rental_points(self.days_rented)
