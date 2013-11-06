from tddBookMoney import *

class Dollar(Money):

	def __init__(self,amount):
		self.amount = amount
		self.simbologia = "USD"

	def currency(self):
		return self.simbologia