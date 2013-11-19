import struct
import pdb

class DbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb')

    def length_of_file(self):
        open_file_position = self.open_file.tell()

        length_of_file = len(self.open_file.read())

        self.open_file.seek(open_file_position)

        return length_of_file

    def number_of_lines(self):
        start_of_file = self.start_of_file()

        return self.length_of_file()/start_of_file["total_overall_length"]

    def read_bytes(self, open_file, number_of_bytes):
        return open_file.read(number_of_bytes)

    def unpack_file(self, number_of_bytes, format_character, open_file):
        if number_of_bytes == 1 :
            unpack_file = struct.unpack(format_character, self.read_bytes(open_file, number_of_bytes))
        else:
            unpack_file = struct.unpack(str(number_of_bytes) + format_character, self.read_bytes(open_file, number_of_bytes))

        return unpack_file

    def start_of_file(self):
        self.open_file.seek(0)

        magic_cookie = self.unpack_file(4, "B", self.open_file)

        total_overall_length = self.unpack_file(4, "B", self.open_file)

        number_of_fields = self.unpack_file(2, "B", self.open_file)

        return {"magic_cookie": magic_cookie, "total_overall_length": total_overall_length[-1], "number_of_fields": number_of_fields[-1]}

    def schema_description(self):
        start_of_file = self.start_of_file()
        open_file = self.open_file
        meta_dados = []
        for number_of_fields in range(start_of_file["number_of_fields"]):

            bytes_of_field_name = self.unpack_file(2, "B", open_file)
            bytes_of_field_name = bytes_of_field_name[-1]

            field_name = self.unpack_file(bytes_of_field_name, 's', open_file)
            field_name = field_name[0]

            end_of_repeating_block = self.unpack_file(2, 'B', open_file)
            end_of_repeating_block = end_of_repeating_block[-1]

            meta_dados.append((field_name, end_of_repeating_block))
        self.open_file.seek(open_file.tell())
        return meta_dados

    def records(self):
        start_of_file = self.start_of_file()
        schema_description = self.schema_description()

        pointer_position = self.open_file.tell()
        number_of_lines = self.number_of_lines()
        self.open_file.seek(pointer_position)

        record = []

        for numbers_of_lines in range(number_of_lines):
            byte_flag = self.unpack_file(1, 'B', self.open_file)

            field_of_record_1 = self.unpack_file(schema_description[0][1], 's ', self.open_file)
            field_of_record_2 = self.unpack_file(schema_description[1][1], 's ', self.open_file)
            field_of_record_3 = self.unpack_file(schema_description[2][1], 's ', self.open_file)
            field_of_record_4 = self.unpack_file(schema_description[3][1], 's ', self.open_file)
            field_of_record_5 = self.unpack_file(schema_description[4][1], 's ', self.open_file)
            field_of_record_6 = self.unpack_file(schema_description[5][1], 's ', self.open_file)

            record.append((field_of_record_1[0], field_of_record_2[0], field_of_record_3[0], field_of_record_4[0], field_of_record_5[0], field_of_record_6[0], byte_flag))

        records = []

        for numbers_of_lines in range(number_of_lines):
            records.append({
                        schema_description[0][0] : record[numbers_of_lines][0],
                        schema_description[1][0] : record[numbers_of_lines][1],
                        schema_description[2][0] : record[numbers_of_lines][2],
                        schema_description[3][0] : record[numbers_of_lines][3],
                        schema_description[4][0] : record[numbers_of_lines][4],
                        schema_description[5][0] : record[numbers_of_lines][5],
                        "byte_flag" : byte_flag})
        return records


    def __del__(self):
        self.open_file.close()


