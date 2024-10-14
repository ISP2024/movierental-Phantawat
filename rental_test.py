import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
		self.regular_movie = Movie("Air", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", Movie.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	@unittest.skip("add this test when you refactor rental price")
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		self.fail("TODO add more tests for other movie categories")

	@unittest.skip("add this test of rental points when you add it to Rental")
	def test_rental_points(self):
		self.fail("add this test of frequent renter points")

	def test_get_price_regular(self):
		rental = Rental(self.regular_movie, days_rented=3)
		amount = rental.get_price()
		
		# Regular pricing for 3 days should be $3.50 ($2 for first two days + $1.50 for third day)
		self.assertEqual(amount, 3.50)

	def test_get_price_children(self):
		rental = Rental(self.childrens_movie, days_rented=4)
		amount = rental.get_price()
		
		# Children's pricing for 4 days should be $3.00 ($1.50 for first three days + $1.50 for fourth day)
		self.assertEqual(amount, 3.00)

	def test_get_price_new_release(self):
		rental = Rental(self.new_movie, days_rented=2)
		amount = rental.get_price()
		
		# New release pricing should be $6.00 ($3 per day)
		self.assertEqual(amount, 6.00)

	def test_rental_points_regular(self):
		rental = Rental(self.regular_movie, days_rented=3)
		points = rental.get_rental_points()
		
		# Regular movies should earn only 1 point regardless of days rented
		self.assertEqual(points, 1)

	def test_rental_points_children(self):
		rental = Rental(self.childrens_movie, days_rented=4)
		points = rental.get_rental_points()
		
		# Children's movies should earn only 1 point regardless of days rented
		self.assertEqual(points, 1)

	def test_rental_points_new_release(self):
		rental = Rental(self.new_movie, days_rented=2)
		points = rental.get_rental_points()
		
		# New release earns points equal to days rented
		self.assertEqual(points, 2)
