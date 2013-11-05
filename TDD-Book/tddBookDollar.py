class Dollar(object):

	def __init__(self,amount):
		self.amount = amount
		
	def times(self,multiplier):
		return self.amount*multiplier
		
	def equals(self, numObject):
		return self.amount == numObject

