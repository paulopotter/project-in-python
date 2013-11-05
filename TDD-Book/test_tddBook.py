import unittest
import tddBookMoney 
from tddBookDollar import Dollar
import tddBookFranc 

class testTddBook(unittest.TestCase):
	def testMultiplication(self):
		dollarFive = Dollar(5).times(2)
		self.assertEquals(10,dollarFive)
		dollarFive = Dollar(5).times(3)
		self.assertEquals(15,dollarFive)

	def testEquallity(self):
		self.assertTrue(Dollar(5).equals(Dollar(5).amount))
		self.assertFalse(Dollar(5).equals(Dollar(6).amount))

if __name__ == '__main__':
	unittest.main()