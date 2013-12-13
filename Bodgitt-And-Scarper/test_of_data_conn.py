import unittest
import data_conn


class TestDataConn(unittest.TestCase):

    def setUp(self):
        self.data_conn = data_conn.DataConn()

    def test_start_of_file_should_return_magic_cookie_total_overall_length_and_number_of_fields(self):
        format_of_data = self.data_conn.start_of_file()
        self.assertEqual(format_of_data["magic_cookie"], (0, 0, 2, 1))
        self.assertEqual(format_of_data["length_of_each_record"], 182)
        self.assertEqual(format_of_data["number_of_fields"], 6)

    def test_bytes_sum_of_each_field_should_be_equal_to_length_of_each_record(self):
        total = 0
        schema_description = self.data_conn.schema_description()

        for number_of_fields in range(self.data_conn.format_of_data["number_of_fields"]):
            total += schema_description[number_of_fields]['field_content_length']

        self.assertEqual(total, self.data_conn.format_of_data["length_of_each_record"])

    def test_length_of_file_should_be_5307(self):
        self.assertEqual(self.data_conn.length_of_file(), 5307)

    def test_file_should_have_29_records(self):
        self.assertEqual(self.data_conn.number_of_records(), 29)

    def test_should_return_x_chars(self):
        self.assertEqual(self.data_conn.read_chars(5), '\x00Buon')

    def test_extract_data_from_file_by_format(self):
        byte_char = self.data_conn.extract_data_by_format(2, "B")
        string_char = self.data_conn.extract_data_by_format(4, "s")

        self.assertEqual(byte_char, (0, 66))
        self.assertEqual(string_char, ("uona",))

    def test_extract_data_from_file_by_byte(self):
        self.assertEqual(self.data_conn.extract_by_byte(2), 66)

    def test_extract_data_from_file_by_string(self):
        self.assertEqual(self.data_conn.extract_by_string(5), '\x00Buon')

    def test_size_of_each_field_record(self):
        schema_description = self.data_conn.schema_description()

        self.assertEqual(schema_description[0]['field_content_length'], 32)
        self.assertEqual(schema_description[1]['field_content_length'], 64)
        self.assertEqual(schema_description[2]['field_content_length'], 64)
        self.assertEqual(schema_description[3]['field_content_length'], 6)
        self.assertEqual(schema_description[4]['field_content_length'], 8)
        self.assertEqual(schema_description[5]['field_content_length'], 8)

    def test_values_of_field_name(self):
        schema_description = self.data_conn.schema_description()

        self.assertEqual(schema_description[0]['field_name'], "name")
        self.assertEqual(schema_description[1]['field_name'], "location")
        self.assertEqual(schema_description[2]['field_name'], "specialties")
        self.assertEqual(schema_description[3]['field_name'], "size")
        self.assertEqual(schema_description[4]['field_name'], "rate")
        self.assertEqual(schema_description[5]['field_name'], "owner")

    def test_records_is_valid_with_byte_flag(self):
        records = self.data_conn.records()

        for number_of_records in range(self.data_conn.number_of_records()):
            self.assertEqual(records[number_of_records][-1], 0)


if __name__ == '__main__':
    unittest.main()
