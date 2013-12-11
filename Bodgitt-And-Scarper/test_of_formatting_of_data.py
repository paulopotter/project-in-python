import unittest
import formatting_of_data


class TestFormattingOfData(unittest.TestCase):

    def setUp(self):
        self.formatting_of_data = formatting_of_data.FormattingOfData()

    def test_type_of_formatted_records(self):
        self.assertEqual(type(self.formatting_of_data.formatted_records()[0]), dict)

    def test_model_of_dictionary_in_formatted_records(self):
        formatted_records = self.formatting_of_data.formatted_records()[0]
        self.assertEqual(formatted_records.keys(), ['byte_flag', 'name', 'rate', 'specialties', 'location', 'owner', 'id', 'size'])

    def test_model_of_data_in_formatted_recods(self):
        formatted_records = self.formatting_of_data.formatted_records()[0]
        self.assertEqual(formatted_records.values(), [
            0,
            'Buonarotti & Company            ',
            '$40.00  ',
            'Air Conditioning, Painting, Painting                            ',
            'Smallville                                                      ',
            '        ',
            0,
            '10    '
        ])

if __name__ == '__main__':
    unittest.main()
