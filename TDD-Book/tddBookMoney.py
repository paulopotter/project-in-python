class Money(object):

	def __init__(self,amount):
		self.amount = amount
		
	def times(self,multiplier):
		return self.amount*multiplier
		
	def equals(self, dinheiro):
		return self.amount == dinheiro.amount and self.__class__ == dinheiro.__class__

	def dollar(self,amount):
		return amount