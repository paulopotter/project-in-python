import unittest
import tddBookMoney 
from tddBookDollar import Dollar
import tddBookFranc 

class testTddBook(unittest.TestCase):
	def testMultiplication(self):
		dollarFive = Dollar(5)
		dollarFive.times(2)
		self.assertEquals(10,dollarFive.amount)

if __name__ == '__main__':
	unittest.main()