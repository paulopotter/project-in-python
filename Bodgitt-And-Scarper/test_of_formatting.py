import unittest
import formatting


class TestFormatting(unittest.TestCase):

    def setUp(self):
        self.formatting = formatting.Formatting()

    def test_formatting_records(self):
      self.assertEqual(type(self.formatting.formatted_records()), list)


if __name__ == '__main__':
    unittest.main()