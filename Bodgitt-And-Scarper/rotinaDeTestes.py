import unittest
import dbSchema


class TestDBSchema(unittest.TestCase):

    def setUp(self):
        self.db_schema = dbSchema.DbSchema()

    def test_file_not_empty(self):
        self.assertNotEqual(self.db_schema.length_of_file(), 0)

    def test_number_of_lines(self):
        self.assertNotEqual(self.db_schema.number_of_lines(), 0)

    def test_start_of_file(self):
        self.assertIsInstance(self.db_schema.start_of_file(), dict)

    def test_schema_description(self):
        self.assertIsInstance(self.db_schema.schema_description(), list)

    def test_number_of_records(self):
        self.assertEqual(len(self.db_schema.records()), self.db_schema.number_of_lines())

    def test_formatted_records(self):
        self.assertIsInstance(self.db_schema.formatted_records(), list)





if __name__ == '__main__':
	unittest.main()
