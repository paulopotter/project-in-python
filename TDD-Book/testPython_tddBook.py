from WasRun import WasRun
from TestCase import TestCase

class TestResult:
	def __init__(self):
		self.runCount = 0
	def testStarted(self):
		self.runCount = self.runCount + 1
	def summary(self):
		return "%d  run, 0 failed" % self.runCount




class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown" == self.test.log)

	def testResult(self):
		test = WasRun("testMethod")
		result = test.run
		assert("1 run, 0 failed" == result.summary())

TestCaseTest("testSetUp").run()
# print test.wasRun
# test.run()
# print test.wasRun