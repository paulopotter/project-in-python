from WasRun import WasRun
import TestCase
class TestCaseTest(TestCase):
	test = WasRun("testMethod")
	assert(not test.wasRun)
	test.run()
	assert(test.wasRun)

TestCaseTest("testRunning").run()
# print test.wasRun
# test.run()
# print test.wasRun