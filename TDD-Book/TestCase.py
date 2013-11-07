#Perguntar sobre teste que depende de outro, por exemplo, se o que eu for fazer necessita de algo que o outro teste passou, o que fazer...
# parei na pagina 81

class TestCase:
	def __init__(self,name):
		self.name = name
	def run(self):
		exec "self." + self.name + "()"