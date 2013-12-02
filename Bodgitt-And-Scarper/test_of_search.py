import unittest
import search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search_class = search.Search()

    def test_name_of_seach(self):
        name = self.search_class.search_for_name('b')
        self.assertIn('Buon', name[0].get('name'))

    def test_location_of_seach(self):
        location = self.search_class.search_for_location('s')
        self.assertIn('Smallville', location[0].get('location'))


if __name__ == '__main__':
    unittest.main()
