# coding:utf-8
import struct


class DataConn:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file = open(self.chosen_file, 'rb+')
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
            new_records = []
            for field in self.meta_dada:
                new_records.append(self.extract_by_string(field['field_content_length']))

            new_records.append(byte_flag)

            records.append(new_records)

        return records

    def pack_in_file(self, values):
        pointer_position = self.open_file.tell()
        open_file = open(self.chosen_file, 'ab')
        open_file.seek(pointer_position)
        open_file.write(struct.pack('?', False))  # byte flag
        for line, value in enumerate(values):
            if len(value) == self.meta_dada[line]['field_content_length']:
                s = bytes(value)
                open_file.write(struct.pack(str(self.meta_dada[line]['field_content_length']) + "s", s))

        return self.number_of_records()

    def set_byte_flag_true_and_clear_values(self, name, location):
        records = self.records()
        file_header = open(self.chosen_file, 'rb').read(self.pointer_position)
        open_file_to_write = open(self.chosen_file, 'wb')
        open_file_to_write.write(file_header)
        for line in records:
            if line[0] == name and line[1] == location:
                open_file_to_write.write(struct.pack('?', True))  # byte flag
                line.pop(-1)
                for line_number, value in enumerate(line):
                    s = bytes(' ' * (self.meta_dada[line_number]['field_content_length']))
                    open_file_to_write.write(struct.pack(str(self.meta_dada[line_number]['field_content_length']) + "s", s))
            else:
                open_file_to_write.write(struct.pack('?', line[-1]))  # byte flag
                line.pop(-1)
                for line_number, value in enumerate(line):
                    s = bytes(value)
                    open_file_to_write.write(struct.pack(str(self.meta_dada[line_number]['field_content_length']) + "s", s))

        open_file_to_write.close()

    def update_record(self, recNo, field_name, changed_value):
        records = self.records()
        file_header = open(self.chosen_file, 'rb').read(self.pointer_position)
        open_file_to_write = open(self.chosen_file, 'wb')
        open_file_to_write.write(file_header)

        for line_number, line in enumerate(records):
            if line_number != recNo:
                open_file_to_write.write(struct.pack('?', line[-1]))  # byte flag
                line.pop(-1)
                for y, value in enumerate(line):
                    value = str(value)
                    if len(value) == self.meta_dada[y]['field_content_length']:
                        s = bytes(value)
                        open_file_to_write.write(struct.pack(str(self.meta_dada[y]['field_content_length']) + "s", s))
            else:
                open_file_to_write.write(struct.pack('?', False))  # byte flag
                line.pop(-1)
                for y, value in enumerate(line):
                    value = str(value)
                    if len(value) == self.meta_dada[y]['field_content_length']:
                        if self.meta_dada[y]['field_name'] == field_name:
                            s = bytes(changed_value)
                        else:
                            s = bytes(value)
                        open_file_to_write.write(struct.pack(str(self.meta_dada[y]['field_content_length']) + "s", s))

        open_file_to_write.close()

    def __del__(self):
        self.open_file.close()
