class Money(object):

	def __init__(self,amount):
		self.amount = amount
		self.currency = None
		
	def times(self,multiplier):
		return self.amount*multiplier
		
	def equals(self, dinheiro):
# Verifica se o valor eh igual ao da classe Money eh igual ao da Classe passada
# e Verifica se a classe passada eh a mesma que esta sendo chamada.
		return self.amount == dinheiro.amount and self.__class__ == dinheiro.__class__


	def plus(self,adicao):
		return self.amount + adicao