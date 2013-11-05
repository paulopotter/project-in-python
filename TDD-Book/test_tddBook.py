import unittest
import tddBookMoney 
import tddBookDollar
import tddBookFranc 

class testTddBook(unittest.TestCase):
	def testMultiplication(self):
		dollarFive = Dollar(5)
		dollarFive.times(2)
		self.assertEquals(10,five.amount)

if __name__ == '__main__':
	unittest.main()