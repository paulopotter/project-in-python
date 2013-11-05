class Dollar(object):

	def __init__(self,amount):
		self.amount = amount
		
	def times(self,multiplier):
		self.amount*=multiplier
		return self.amount
		
	def equals(self, numObject):
		return self.amount == numObject

