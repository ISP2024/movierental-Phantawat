import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)
		
	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass

	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_total_charge(self):
        
        # Create rentals with different prices
		regular_rental = Rental(self.regular_movie, days_rented=3)  # $3.50
		children_rental = Rental(self.childrens_movie, days_rented=4)  # $3.00
		new_release_rental = Rental(self.new_movie, days_rented=2)  # $6.00
		
		# Add rentals to customer
		self.c.add_rental(regular_rental)
		self.c.add_rental(children_rental)
		self.c.add_rental(new_release_rental)

		# Calculate total charge
		expected_total = 3.50 + 3.00 + 6.00  # $12.50
		actual_total = self.c.total_charge()
		
		self.assertEqual(actual_total, expected_total)

	def test_total_rental_points(self):
        
        # Create rentals with different prices and points
		regular_rental = Rental(self.regular_movie, days_rented=3)  # Should earn 1 point
		children_rental = Rental(self.childrens_movie, days_rented=4)  # Should earn 1 point
		new_release_rental = Rental(self.new_movie, days_rented=2)  # Should earn 2 points
		
		# Add rentals to customer
		self.c.add_rental(regular_rental)
		self.c.add_rental(children_rental)
		self.c.add_rental(new_release_rental)

		# Calculate total rental points
		expected_points = 1 + 1 + 2  # Total should be 4 points
		actual_points = self.c.total_rental_points()
		
		self.assertEqual(actual_points, expected_points)
