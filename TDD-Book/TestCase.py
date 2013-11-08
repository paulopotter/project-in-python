from TestResult import TestResult
from TestSuite import TestSuite

class TestCase:
	def __init__(self,name):
		self.name = name
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def run(self):
		result = TestResult()
		result.testStarted()
		self.setUp()
		try:
			exec "self." + self.name + "()"
		except:
			result.testFailed()
		self.tearDown()
		return result