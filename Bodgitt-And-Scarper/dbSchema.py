import struct


class DbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb')
        self.format_of_data = self.start_of_file()

    def length_of_file(self):
        length_of_file = len(self.open_file.read())

        return length_of_file

    def number_of_lines(self):
        pointer_position = self.open_file.tell()
        self.open_file.seek(0)
        number_of_lines = self.length_of_file() / self.format_of_data["total_overall_length"]
        self.open_file.seek(pointer_position)

        return number_of_lines

    def read_bytes(self, open_file, number_of_bytes):
        return open_file.read(number_of_bytes)

    def unpack_file(self, number_of_bytes, format_character, open_file):
        return struct.unpack(str(number_of_bytes) + format_character, self.read_bytes(open_file, number_of_bytes))

    def start_of_file(self):
        self.open_file.seek(0)

        magic_cookie = self.unpack_file(4, "B", self.open_file)

        total_overall_length = self.unpack_file(4, "B", self.open_file)

        number_of_fields = self.unpack_file(2, "B", self.open_file)

        return {
            "magic_cookie": magic_cookie,
            "total_overall_length": total_overall_length[-1],
            "number_of_fields": number_of_fields[-1]
        }

    def schema_description(self):
        self.start_of_file()
        meta_dados = []
        for number_of_fields in range(self.format_of_data["number_of_fields"]):

            field_length = self.unpack_file(2, "B", self.open_file)
            field_length = field_length[-1]

            field_name = self.unpack_file(field_length, 's', self.open_file)
            field_name = field_name[0]

            field_content_length = self.unpack_file(2, 'B', self.open_file)
            field_content_length = field_content_length[-1]

            meta_dados.append((field_name, field_content_length))

        return meta_dados

    def records(self):
        number_of_lines = self.number_of_lines()
        schema_description = self.schema_description()
        record = []

        for x in range(number_of_lines):
            byte_flag = self.unpack_file(1, 'B', self.open_file)
            name = self.unpack_file(schema_description[0][1], 's ', self.open_file)
            location = self.unpack_file(schema_description[1][1], 's ', self.open_file)
            specialties = self.unpack_file(schema_description[2][1], 's ', self.open_file)
            size = self.unpack_file(schema_description[3][1], 's ', self.open_file)
            rate = self.unpack_file(schema_description[4][1], 's ', self.open_file)
            owner = self.unpack_file(schema_description[5][1], 's ', self.open_file)

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
        number_of_lines = self.number_of_lines()
        schema_description = self.schema_description()
        record  = self.records()
        formatted_record = []

        for number_of_lines in range(number_of_lines):
            formatted_record.append({
                                schema_description[0][0] : record[number_of_lines][0],
                                schema_description[1][0] : record[number_of_lines][1],
                                schema_description[2][0] : record[number_of_lines][2],
                                schema_description[3][0] : record[number_of_lines][3],
                                schema_description[4][0] : record[number_of_lines][4],
                                schema_description[5][0] : record[number_of_lines][5],
                                "byte_flag" : record[number_of_lines][6]
                            })
        return formatted_record

    def __del__(self):
        self.open_file.close()
