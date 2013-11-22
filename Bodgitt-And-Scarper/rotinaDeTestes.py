import unittest
import dbSchema
import pdb

class TestDBSchema(unittest.TestCase):

    def setUp(self):
        self.db_schema = dbSchema.DbSchema()

    def test_start_of_file_should_return_magic_cookie_total_overall_length_and_number_of_fields(self):
        format_of_data = self.db_schema.start_of_file()
        self.assertEqual(format_of_data["magic_cookie"], (0, 0, 2, 1))
        self.assertEqual(format_of_data["length_of_each_record"], 182)
        self.assertEqual(format_of_data["number_of_fields"], 6)

    def test_bytes_sum_of_each_field_should_be_equal_to_length_of_each_record(self):
        total = 0
        schema_description = self.db_schema.schema_description()

        for number_of_fields in range(self.db_schema.format_of_data["number_of_fields"]):
            total += schema_description[number_of_fields]['field_content_length']

        self.assertEqual(total, self.db_schema.format_of_data["length_of_each_record"])

    def test_record_should_have_byte_flag_key(self):
        formatted_records = self.db_schema.formatted_records()

        for number_of_record in range(self.db_schema.number_of_records()):
            self.assertIn("byte_flag", formatted_records[number_of_record].keys())

    def test_length_of_file_should_be_5367(self):
        self.assertEqual(self.db_schema.length_of_file(), 5367)

    def test_file_should_have_29_records(self):
        self.assertEqual(self.db_schema.number_of_records(), 29)

    def test_should_return_x_chars(self):
        self.assertEqual(self.db_schema.read_chars(5), '\x00\x04nam')

    def test_extract_data_from_file_by_format(self):
        byte_char = self.db_schema.extract_data_by_format(2, "B")
        string_char = self.db_schema.extract_data_by_format(4, "s")

        self.assertEqual(byte_char, (0, 4))
        self.assertEqual(string_char, ("name",))

    def test_size_of_each_field_record(self):
        schema_description = self.db_schema.schema_description()

        self.assertEqual(schema_description[0]['field_content_length'], 32)
        self.assertEqual(schema_description[1]['field_content_length'], 64)
        self.assertEqual(schema_description[2]['field_content_length'], 64)
        self.assertEqual(schema_description[3]['field_content_length'], 6)
        self.assertEqual(schema_description[4]['field_content_length'], 8)
        self.assertEqual(schema_description[5]['field_content_length'], 8)


    def test_values_of_field_name(self):
        schema_description = self.db_schema.schema_description()

        self.assertEqual(schema_description[0]['field_name'], "name")
        self.assertEqual(schema_description[1]['field_name'], "location")
        self.assertEqual(schema_description[2]['field_name'], "specialties")
        self.assertEqual(schema_description[3]['field_name'], "size")
        self.assertEqual(schema_description[4]['field_name'], "rate")
        self.assertEqual(schema_description[5]['field_name'], "owner")

    def test_records_is_valid_with_byte_flag(self):
        records = self.db_schema.records()

        for number_of_records in range(self.db_schema.number_of_records()):
            self.assertEqual(records[number_of_records][6], 0)

    def test_tamanho_de_cada_data(self):
        records = self.db_schema.records()

        for number_of_records in range(self.db_schema.number_of_records()):
            self.assertEqual(len(records[number_of_records][0]),32)
            self.assertEqual(len(records[number_of_records][1]),64)
            self.assertEqual(len(records[number_of_records][2]),64)
            self.assertEqual(len(records[number_of_records][3]),6)
            self.assertEqual(len(records[number_of_records][4]),8)
            self.assertEqual(len(records[number_of_records][5]),8)



if __name__ == '__main__':
	unittest.main()
