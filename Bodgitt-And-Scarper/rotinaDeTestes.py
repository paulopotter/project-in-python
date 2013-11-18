import unittest
import dbSchema

db_schema = dbSchema.dbSchema()

class TestDBSchema(unittest.TestCase):

    def test_file_not_empty(self):
        self.assertNotEqual(db_schema.length_of_file(),0)

    def test_unpack_file(self):
        self.assertFalse(db_schema.unpack_file("4B"))





if __name__ == '__main__':
	unittest.main()