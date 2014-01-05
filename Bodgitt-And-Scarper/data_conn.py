import struct


class DataConn:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'ab+')
        self.format_of_data = self.start_of_file()
        self.meta_dada = self.schema_description()
        self.pointer_position = self.open_file.tell()

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

    def extract_by_byte(self, number_of_bytes):
        return self.extract_data_by_format(number_of_bytes, 'B')[-1]

    def extract_by_string(self, number_of_bytes):
        return self.extract_data_by_format(number_of_bytes, 's')[0]

    def start_of_file(self):
        self.open_file.seek(0)
        magic_cookie = self.extract_data_by_format(4, 'B')
        length_of_each_record = self.extract_by_byte(4)
        number_of_fields = self.extract_by_byte(2)

        return {
            "magic_cookie": magic_cookie,
            "length_of_each_record": length_of_each_record,
            "number_of_fields": number_of_fields
        }

    def schema_description(self):
        self.start_of_file()
        meta_dados = []
        for number_of_fields in range(self.format_of_data["number_of_fields"]):

            field_length = self.extract_by_byte(2)
            field_name = self.extract_by_string(field_length)
            field_content_length = self.extract_by_byte(2)

            meta_dados.append({
                "field_name": field_name,
                "field_content_length": field_content_length
            })

        return meta_dados

    def records(self):
        number_of_records = self.number_of_records()
        records = []

        for x in range(number_of_records):
            byte_flag = self.extract_by_byte(1)
            new_records = [x]
            for field in self.meta_dada:
                new_records.append(self.extract_by_string(field['field_content_length']))

            new_records.append(byte_flag)

            records.append(new_records)

        return records

    def pack_in_file(self, values):
        self.records()
        pointer_position = self.open_file.tell()
        self.open_file.seek(pointer_position - 1)
        x = -1
        self.open_file.write(struct.pack("x"))  # byte flag
        for value in values:
            x += 1
            if len(value) == self.meta_dada[x]['field_content_length']:
                s = bytes(value)
                self.open_file.write(struct.pack(str(self.meta_dada[x]['field_content_length']) + "s", s))

    def __del__(self):
        self.open_file.close()
