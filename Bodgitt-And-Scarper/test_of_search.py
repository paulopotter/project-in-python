import unittest
import search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search_class = search.Search()

    def test_name_of_seach(self):
        self.assertEqual(self.search_class.search_for_name('Bu'), ['Buonarotti & Company'] * 4)

    def test_location_of_seach(self):
        self.assertEqual(self.search_class.search_for_location('Sm'), ['Smallville'] * 2)

if __name__ == '__main__':
    unittest.main()