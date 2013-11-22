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

    def start_of_file(self):
        self.open_file.seek(0)
        magic_cookie = self.extract_data_by_format(4, "B")
        length_of_each_record = self.extract_data_by_format(4, "B")
        number_of_fields = self.extract_data_by_format(2, "B")

        return {
            "magic_cookie": magic_cookie,
            "length_of_each_record": length_of_each_record[-1],
            "number_of_fields": number_of_fields[-1]
        }

    def schema_description(self):
        self.start_of_file()
        meta_dados = []
        for number_of_fields in range(self.format_of_data["number_of_fields"]):

            field_length = self.extract_data_by_format(2, "B")
            field_length = field_length[-1]

            field_name = self.extract_data_by_format(field_length, 's')
            field_name = field_name[0]

            field_content_length = self.extract_data_by_format(2, 'B')
            field_content_length = field_content_length[-1]

            meta_dados.append({
                "field_name": field_name,
                "field_content_length": field_content_length
            })

        return meta_dados

    def records(self):
        number_of_records = self.number_of_records()
        schema_description = self.schema_description()
        record = []

        for x in range(number_of_records):
            byte_flag = self.extract_data_by_format(1, 'B')
            name = self.extract_data_by_format(schema_description[0]['field_content_length'], 's')
            location = self.extract_data_by_format(schema_description[1]['field_content_length'], 's')
            specialties = self.extract_data_by_format(schema_description[2]['field_content_length'], 's')
            size = self.extract_data_by_format(schema_description[3]['field_content_length'], 's')
            rate = self.extract_data_by_format(schema_description[4]['field_content_length'], 's')
            owner = self.extract_data_by_format(schema_description[5]['field_content_length'], 's')

            record.append((
                name[0],
                location[0],
                specialties[0],
                size[0],
                rate[0],
                owner[0],
                byte_flag[0]
            ))

        return record

    def formatted_records(self):
        schema_description = self.schema_description()
        record  = self.records()
        formatted_record = []

        for number_of_records in range(self.number_of_records()):
            formatted_record.append({
                schema_description[0]['field_name'] : record[number_of_records][0],
                schema_description[1]['field_name'] : record[number_of_records][1],
                schema_description[2]['field_name'] : record[number_of_records][2],
                schema_description[3]['field_name'] : record[number_of_records][3],
                schema_description[4]['field_name'] : record[number_of_records][4],
                schema_description[5]['field_name'] : record[number_of_records][5],
                "byte_flag" : record[number_of_records][6]
            })
        return formatted_record

    def __del__(self):
        self.open_file.close()
