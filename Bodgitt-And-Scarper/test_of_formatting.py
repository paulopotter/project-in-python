import unittest
import formatting


class TestFormatting(unittest.TestCase):

    def setUp(self):
        self.formatting = formatting.Formatting()

    def test_type_of_formatted_records(self):
        self.assertEqual(type(self.formatting.formatted_records()[0]), dict)

    def test_model_of_dictionary_in_formatted_records(self):
        formatted_records = self.formatting.formatted_records()[0]
        self.assertEqual(formatted_records.keys(), ['byte_flag', 'name', 'rate', 'specialties', 'location', 'owner', 'id', 'size'])

    def test_model_of_data_in_formatted_recods(self):
        formatted_records = self.formatting.formatted_records()[0]
        self.assertEqual(formatted_records.values(), [0, 'Buonarotti & Company            ',
                '$40.00  ', 'Air Conditioning, Painting, Painting                            ',
                'Smallville                                                      ',
                '        ', 0, '10    '
            ]
        )

if __name__ == '__main__':
    unittest.main()