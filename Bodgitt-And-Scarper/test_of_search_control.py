import unittest
import search_control
from my_exceptions import RecordNotFoundException
from formatting_of_data import FormattingOfData


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search_class = search_control.SearchControl()

    def test_name_of_search(self):
        name = self.search_class.search_for('B', 'name')
        self.assertIn('Buon', name[0].get('name'))

    def test_location_of_search(self):
        location = self.search_class.search_for('S', 'location')
        self.assertIn('Smallville', location[0].get('location'))

    def test_amount_of_search_all(self):
        self.assertEqual(len(self.search_class.search_for('*', 'name')), 29)

    def test_find_of_criteria(self):
        self.assertEqual(self.search_class.find('Buo'), [0, 5, 18, 25])

    def test_read_a_record(self):
        self.assertEqual(self.search_class.read(1), FormattingOfData().formatted_records()[1])

    def test_read_exception(self):
        self.assertRaises(RecordNotFoundException, self.search_class.read, 30)


if __name__ == '__main__':
    unittest.main()
