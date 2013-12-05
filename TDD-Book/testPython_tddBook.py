from WasRun import WasRun
from TestCase import TestCase
from TestSuite import TestSuite

from TestResult import testResult

class TestCaseTest(TestCase):

	def setUp(self):
		self.result = TestResult()

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run(self.result)
		assert("setUp testMethod tearDown" == self.test.log)

	def testResult(self):
		test = WasRun("testMethod")
		test.run(self.result)
		assert("1 run, 0 failed" == result.summary())
		
	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		test.run(self.result)
		assert("1 run, 1 failed" == result.summary())

	def testFailedResultFormatting(self):
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())

	def testSuite(self):
		suite = TestSuite()
		suite.add(WasRun("testMethod")) 
		suite.add(WasRun("testBrokenMethod"))
		suite.run(self.result)
		assert("2 run, 1 failed" == self.result.summary()) 

print TestCaseTest("testTemplateMethod").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testFailedResultFormatting").run().summary()
print TestCaseTest("testFailedResult").run().summary()

# TestCaseTest("testSetUp").run()
# print test.wasRun
# test.run()
# print test.wasRun