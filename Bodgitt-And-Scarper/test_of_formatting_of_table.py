# coding:utf-8
import unittest
import formatting_of_table


class TestFormattingData(unittest.TestCase):

    def setUp(self):
        self.formatting_of_table_class = formatting_of_table.FormattingOfTable()

    def test_line_of_table(self):
        table_column_widths = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} |"
        self.assertEqual(
            self.formatting_of_table_class.line_of_table(table_column_widths,
                                                         [{
                                                          'id': 12,
                                                          'name': 'strName',
                                                          'location': 'strLocation',
                                                          'specialties': 'strSpecialties',
                                                          'size': 12,
                                                          'rate': 'strRate',
                                                          'owner': 'strOwner'
                                                          }]),
            '| 12 | strName | strLocation | strSpecialties | 12 | strRate | strOwner |\n+' + '-'*204 + '+\n'
        )

    def test_formatted_table_error(self):
        self.assertEqual(self.formatting_of_table_class.formatted_table(
            {}), 'ERROR: Não existe registro com o(s) parametros passados.')

    def test_formatted_table(self):
        self.assertIs(
            type(self.formatting_of_table_class.formatted_table({'name': 'b'})), str)

if __name__ == '__main__':
    unittest.main()
