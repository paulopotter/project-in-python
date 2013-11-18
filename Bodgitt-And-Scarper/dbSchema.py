import struct
class dbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file   = open(self.chosen_file, 'rb')

    def length_of_file(self):
        size_of_file = len(self.open_file.read())
        return size_of_file

    def read_bytes(self,number_of_bytes):
        data = self.open_file.read(number_of_bytes)
        return data

    def unpack_file(self,number_of_bytes,format_character):
        return  struct.unpack(str(number_of_bytes) + format_character, dbSchema().read_bytes(number_of_bytes))