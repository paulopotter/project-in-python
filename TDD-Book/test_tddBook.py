import unittest
from tddBookMoney import Money
from tddBookDollar import Dollar
from tddBookFranc import Franc

class testTddBook(unittest.TestCase):
	def testMultiplication(self):
		five = Money(5)
		self.assertEquals(Dollar(10).amount,five.times(2))
		self.assertEquals(Dollar(15).amount,five.times(3))

		francFive = Franc(5)
		self.assertEquals(10,francFive.times(2))
		self.assertEquals(15,francFive.times(3))

	def testEquallity(self):
		self.assertTrue(Dollar(5).equals(Dollar(5)))
		self.assertFalse(Dollar(5).equals(Dollar(6)))

		self.assertTrue(Franc(5).equals(Franc(5)))
		self.assertFalse(Franc(5).equals(Franc(6)))
		
		self.assertFalse(Dollar(5).equals(Franc(5)))

	def testCurrency(self):
		self.assertEquals("USD",Dollar(1).currency())
		self.assertEquals("CHF",Franc(1).currency())

if __name__ == '__main__':
	unittest.main()


