import logging

class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """
   
   def __init__(self, movie, days_rented): 
      """Initialize a new movie rental object for
         a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented

   def get_movie(self):
        return self.movie

   def get_days_rented(self):
      return self.days_rented

   def get_price(self):
      """Calculate movie price for statement."""
      price_strategy = self.movie.get_price_strategy()
      return price_strategy.get_price(self.days_rented)

   def get_rental_points(self):
      """Calculate frequent renter points for this rental."""
      price_strategy = self.movie.get_price_strategy()
      return price_strategy.get_rental_points(self.days_rented)
