from tddBookMoney import *

class Dollar(Money):

	def __init__(self,amount):
		self.amount = amount
		
	def times(self,multiplier):
		return self.amount*multiplier
		
	# def equals(self, numObject):
	# 	# Money(self.amount).equals(numObject)
	# 	return self.amount == Money(numObject).amount