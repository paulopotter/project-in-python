from tddBookMoney import Money

class Franc(Money):

	def __init__(self,amount):
		self.amount = amount
		self.simbologia = "CHF"

	def currency(self):
		return self.simbologia