import unittest
import dbSchema

db_schema = dbSchema.dbSchema()

class TestDBSchema(unittest.TestCase):

    def test_file_not_empty(self):
        self.assertNotEqual(db_schema.length_of_file(),0)

    def test_start_of_file(self):
        self.assertIsInstance(db_schema.start_of_file(),dict)



if __name__ == '__main__':
	unittest.main()