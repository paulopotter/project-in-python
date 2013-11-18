import struct


class DbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb')

    def length_of_file(self):
        return len(self.open_file.read())

    def read_bytes(self,open_file,number_of_bytes):
        return open_file.read(number_of_bytes)

    def unpack_file(self,number_of_bytes,format_character,open_file):
        return struct.unpack(str(number_of_bytes) + format_character, self.read_bytes(open_file,number_of_bytes))

    def start_of_file(self):
        magic_cookie = self.unpack_file(4,"B", self.open_file)

        total_overall_length = self.unpack_file(4,"B", self.open_file)

        number_of_fields = self.unpack_file(2, "B", self.open_file)

        return {"magic_cookie": magic_cookie[-1], "total_overall_length": total_overall_length[-1], "number_of_fields": number_of_fields[-1]}
