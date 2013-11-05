import unittest
import tddBookMoney 
from tddBookDollar import Dollar
from tddBookFranc import Franc

class testTddBook(unittest.TestCase):
	def testMultiplication(self):
		dollarFive = Dollar(5).times(2)
		self.assertEquals(10,dollarFive)
		dollarFive = Dollar(5).times(3)
		self.assertEquals(15,dollarFive)

		francFive = Franc(5).times(2)
		self.assertEquals(10,francFive)
		francFive = Franc(5).times(3)
		self.assertEquals(15,francFive)

	def testEquallity(self):
		self.assertTrue(Dollar(5).equals(Dollar(5).amount))
		self.assertFalse(Dollar(5).equals(Dollar(6).amount))
		self.assertTrue(Franc(5).equals(Franc(5).amount))
		self.assertFalse(Franc(5).equals(Franc(6).amount))

if __name__ == '__main__':
	unittest.main()