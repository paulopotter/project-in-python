import unittest
import dbSchema

db_schema = dbSchema.dbSchema()

class TestDBSchema(unittest.TestCase):

    def test_file_not_empty(self):
        self.assertNotEqual(db_schema.length_of_file(),0)




if __name__ == '__main__':
	unittest.main()