class TestSuite:
	def __init__(self):
		self.tests = []
	def add (self, test):
		self.tests.append(test)
	def run(self):
		for test in tests:
			test.run(result)
		return result