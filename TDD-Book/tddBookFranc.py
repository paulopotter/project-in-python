from tddBookMoney import Money

class Franc(Money):

	def __init__(self,amount):
		self.amount = amount
		
	def times(self,multiplier):
		return self.amount*multiplier
		
	# def equals(self, numObject):
	# 	return self.amount == Money(numObject).amount

