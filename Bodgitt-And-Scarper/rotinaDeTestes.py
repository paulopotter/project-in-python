import unittest
import dbSchema

class TestDBSchema(unittest.TestCase):

	# def test_IndentifiesDataFile(self):
	# 	self.assertEqual(dbSchema.magicCookieValue, (0,0,2,1))

	def test_total_overall_length(self):
		# total overall length in bytes of each record 
		self.assertEqual(dbSchema.number_total_overall_length, sum(dbSchema.tuple_meta_field_length))

	def test_length_for_fields_name(self):
		# number of fields in each record
		j = -3
		for x in range(len(dbSchema.tuple_meta_field_length)):
			j += 3
			self.assertEqual(len(dbSchema.bytes_of_field_name[j]) + 2, dbSchema.tuple_meta_field_length[x])


if __name__ == '__main__':
	unittest.main()