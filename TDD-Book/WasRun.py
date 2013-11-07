from TestCase import TestCase

class WasRun(TestCase):
	def __init__(self,name):
		self.wasRun = None
		TestCase.__init__(self,name)
	def testMethod(self):
		self.wasRun = 1
	def run(self):
		exec "self." + self.name +"()"