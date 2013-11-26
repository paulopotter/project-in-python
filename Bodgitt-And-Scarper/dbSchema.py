import struct


class DbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb')
        self.format_of_data = self.start_of_file()

    def length_of_file(self):
        return len(self.open_file.read())

    def number_of_records(self):
        pointer_position = self.open_file.tell()
        self.open_file.seek(0)
        number_of_records = self.length_of_file() / self.format_of_data["length_of_each_record"]
        self.open_file.seek(pointer_position)

        return number_of_records

    def read_chars(self, quantity):
        return self.open_file.read(quantity)

    def extract_data_by_format(self, number_of_bytes, format_character):
        return struct.unpack(str(number_of_bytes) + format_character, self.read_chars(number_of_bytes))

    def extract_data_by_byte(self, number_of_bytes):
        return self.extract_data_by_format(number_of_bytes, 'B')[-1]

    def extract_data_by_string(self, number_of_bytes):
        return self.extract_data_by_format(number_of_bytes, 's')[0]

    def start_of_file(self):
        self.open_file.seek(0)
        magic_cookie = self.extract_data_by_format(4, 'B')
        length_of_each_record = self.extract_data_by_byte(4)
        number_of_fields = self.extract_data_by_byte(2)

        return {
            "magic_cookie": magic_cookie,
            "length_of_each_record": length_of_each_record,
            "number_of_fields": number_of_fields
        }

    def schema_description(self):
        self.start_of_file()
        meta_dados = []
        for number_of_fields in range(self.format_of_data["number_of_fields"]):

            field_length = self.extract_data_by_byte(2)
            field_name = self.extract_data_by_string(field_length)
            field_content_length = self.extract_data_by_byte(2)

            meta_dados.append({
                "field_name": field_name,
                "field_content_length": field_content_length
            })

        return meta_dados

    def records(self):
        number_of_records = self.number_of_records()
        schema_description = self.schema_description()
        records = []

        for x in range(number_of_records):
            byte_flag = self.extract_data_by_byte(1)
            the_record = []
            for field in schema_description:
                the_record.append(self.extract_data_by_string(field['field_content_length']))

            the_record.append(byte_flag)

            records.append(the_record)

        return records

    def formatted_records(self):
        schema_description = self.schema_description()
        record  = self.records()
        formatted_record = []

        for number_of_records in range(self.number_of_records()):
            dicionario = {}

            for number_of_fields in range(self.start_of_file()["number_of_fields"]):
                dicionario[schema_description[number_of_fields]['field_name']] = record[number_of_records][number_of_fields]

            dicionario["byte_flag"] =  record[number_of_records][6]
            formatted_record.append(dicionario)

        return formatted_record

    def __del__(self):
        self.open_file.close()
