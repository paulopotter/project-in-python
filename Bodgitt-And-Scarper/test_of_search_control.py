import unittest
import search_control
from my_exceptions import RecordNotFoundException


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search = search_control.SearchControl()

    def test_find_return_type(self):
        self.assertEqual(type(self.search.find(**{'name': None, 'location': 'Smallville'})), list)

    def test_find_location(self):
        self.assertEqual(self.search.find(**{'name': None, 'location': 'X'}), [19, 20, 21])

    def test_find_name(self):
        self.assertEqual(self.search.find(**{'name': 'Buon', 'location': None}), [0, 5, 18, 25])

    def test_find_all(self):
        self.assertEqual(self.search.find(**{'name': None, 'location': None}), range(29))

    def test_read_return_type(self):
        self.assertEqual(type(self.search.read(0)), list)

    def test_read(self):
        self.assertEqual(self.search.read(0), [0, 'Buonarotti & Company            ', 'Smallville                                                      ', 'Air Conditioning, Painting, Painting                            ', '10    ', '$40.00  ', '        ', 0])

    def test_read_error(self):
        self.assertRaises(RecordNotFoundException, self.search.read, 300)

if __name__ == '__main__':
    unittest.main()
