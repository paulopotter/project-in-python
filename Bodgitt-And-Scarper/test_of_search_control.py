import unittest
import search_control
from my_exceptions import RecordNotFoundException


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search_class = search_control.SearchControl()

    def test_name_of_search_with_upper_letter(self):
        name = self.search_class.search_for('B', 'name')
        self.assertIn('Buon', name[0].get('name'))

    def test_location_of_search_with_lower_letter(self):
        location = self.search_class.search_for('s', 'location')
        self.assertIn('Smallville', location[0].get('location'))

    def test_search_for_id_number(self):
        id_number = self.search_class.search_for(0, 'id')
        self.assertEqual(0, id_number[0]['id'])

    def test_amount_of_search_all(self):
        self.assertEqual(len(self.search_class.search_for('*', 'name')), 29)

    def test_find_of_criteria(self):
        self.assertEqual(self.search_class.find({'Name': 'Buo'}), [0, 5, 18, 25])

    def test_read_a_record(self):
        dicto = {'byte_flag': 0,
                 'name': 'Swanders & Flaughn              ',
                 'rate': '$55.00  ',
                 'specialties': 'Painting, Air Conditioning                                      ',
                 'location': 'Smallville                                                      ',
                 'owner': '        ',
                 'id': 1,
                 'size': '7     '
                 }
        self.assertEqual(self.search_class.read(1), dicto)

    def test_read_exception(self):
        self.assertRaises(RecordNotFoundException, self.search_class.read, 30)

    def test_duplicate_data_in_find_method(self):
        self.assertEqual(self.search_class.find({'name': 's', 'location': 's'}), [0, 1, 12, 22])


if __name__ == '__main__':
    unittest.main()
