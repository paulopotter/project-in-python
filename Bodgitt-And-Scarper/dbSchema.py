import struct
class dbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file   = open(self.chosen_file, 'rb')

    def length_of_file(self):
        size_of_file = len(self.open_file.read())
        return size_of_file

    def read_bytes(self,open_file,number_of_bytes):
        data = open_file.read(number_of_bytes)
        return data

    def unpack_file(self,number_of_bytes,format_character,open_file):
        return struct.unpack(str(number_of_bytes) + format_character, dbSchema().read_bytes(open_file,number_of_bytes))

    def start_of_file(self):
        open_file = dbSchema().open_file

        magic_cookie = dbSchema().unpack_file(4,"B",open_file)

        total_overall_length = dbSchema().unpack_file(4,"B",open_file)

        number_of_fields = dbSchema().unpack_file(2, "B", open_file)

        return {"magic_cookie":magic_cookie[-1], "total_overall_length":total_overall_length[-1], "number_of_fields":number_of_fields[-1] }