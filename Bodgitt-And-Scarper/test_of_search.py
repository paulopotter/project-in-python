import unittest
from search import Search
from dbSchema import DbSchema


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search_class = Search()

    def test_name_of_search(self):
        name = self.search_class.search_for('b', 'name')
        self.assertIn('Buon', name[0].get('name'))

    def test_location_of_search(self):
        location = self.search_class.search_for('s', 'location')
        self.assertIn('Smallville', location[0].get('location'))

    def test_amount_of_search_all(self):
        self.assertEqual(len(self.search_class.search_for('*', 'name')), len(DbSchema().records()))

    def test_error_of_null_search(self):
        self.assertIn('ERROR', self.search_class.formatted_table({'name': '', 'location': ''}))

    def test_find_of_criteria(self):
        self.assertEqual(self.search_class.find('Buo'), [0, 5, 18, 25])

    def test_read_a_record(self):
        self.assertEqual(self.search_class.read(1),DbSchema().formatted_records()[1])


if __name__ == '__main__':
    unittest.main()
