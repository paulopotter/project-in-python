import struct


class DbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb+')

    def length_of_file(self):
        return len(self.open_file.read())

    def read_bytes(self,open_file,number_of_bytes):
        return open_file.read(number_of_bytes)

    def unpack_file(self,number_of_bytes,format_character,open_file):
        return struct.unpack(str(number_of_bytes) + format_character, self.read_bytes(open_file, number_of_bytes))

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
        for x in range(start_of_file["number_of_fields"]):

            bytes_of_field_name = self.unpack_file(2, "B", open_file)
            bytes_of_field_name = bytes_of_field_name[-1]

            field_name = self.unpack_file(bytes_of_field_name, 's', open_file)
            field_name = field_name[0]

            end_of_repeating_block = self.unpack_file(2, 'B', open_file)
            end_of_repeating_block = end_of_repeating_block[-1]

            meta_dados.append((field_name, end_of_repeating_block))

        return meta_dados

