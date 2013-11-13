import unittest
import dbSchema

class TestFile(unittest.TestCase):

	# def test_IndentifiesDataFile(self):
	# 	self.assertEqual(dbSchema.magicCookieValue, (0,0,2,1))

	def test_TotalOverallLength(self):
		# total overall length in bytes of each record 
		self.assertEqual(dbSchema.numTotalOverallLength,sum(dbSchema.tuplaMetaFieldLength))

	def test_LengthForFieldsName(self):
		# number of fields in each record
		j = -3
		for i in range(len(dbSchema.tuplaMetaFieldLength)):
			j += 3
			self.assertEqual(len(dbSchema.bytesOfFieldName[j])+2, dbSchema.tuplaMetaFieldLength[i])




if __name__ == '__main__':
	unittest.main()