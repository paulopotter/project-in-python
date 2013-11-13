import unittest
import dbSchema

class TestFile(unittest.TestCase):

	def test_totalLarguraLinha(self):
		# total overall length in bytes of each record
		self.assertEqual(dbSchema.numTotalOverallLength,sum(dbSchema.tuplaMetaFieldLength))

if __name__ == '__main__':
	unittest.main()