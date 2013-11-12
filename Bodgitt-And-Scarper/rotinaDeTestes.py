import unittest
import dbSchema

class TestFile(unittest.TestCase):
	def testMagicCoookie(self):
		self.assertIsInstance(dbSchema.magicCookieValue,tuple)



if __name__ == '__main__':
	unittest.main()