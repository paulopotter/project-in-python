# coding:utf-8
from data_conn import DataConn
from my_exceptions import RecordNotFoundException


class CRUD(object):

    def find(self, **criteria):
        records = DataConn().records()
        positions = []

        if criteria['search_and']:
            for line in range(len(records)):
                if records[line][2].lower().find(criteria['location'].lower()) == 0 and records[line][1].lower().find(criteria['name'].lower()) == 0:
                    positions.append(line)
        else:
            if criteria['name'] is None and criteria['location'] is None:
                for line in range(len(records)):
                    positions.append(line)

            if criteria['name'] is not None:
                for line in range(len(records)):
                    if records[line][1].lower().find(criteria['name'].lower()) == 0:
                        positions.append(line)

            if criteria['location'] is not None:
                for line in range(len(records)):
                    if records[line][2].lower().find(criteria['location'].lower()) == 0:
                        positions.append(line)

        line_records = list(set(positions))
        line_records.sort()

        return line_records

    def read(self, recNo):
        try:
            records = DataConn().records()
            line_value = records[recNo]
            return line_value
        except IndexError:
            raise RecordNotFoundException

    def create(self, *value):
        if value == () or value[0] == '' or value[1] == '':
            raise Exception
        else:
            number_of_fields = len(DataConn().meta_dada)
            x = 0
            new_value = []
            while x < number_of_fields:
                new_value.append(self.format_for_necessary_size(value[x], DataConn().meta_dada[x]['field_content_length']))
                x += 1
        return DataConn().pack_in_file(new_value)

    def format_for_necessary_size(self, value, size):
        if len(value) < size:
            difference = size - len(value)
            return value + (' ' * difference)
        else:
            return value

    def delete(self, recNo):
        try:
            records = DataConn().records()
            DataConn().set_byte_flag_true(records[recNo][0])
        except IndexError:
            raise RecordNotFoundException

    def update(self, recNo, **data):

        meta_dada = DataConn().meta_dada

        for field_name in data.keys():
            x = -1
            for item in meta_dada:
                x += 1
                if field_name in item.values():
                    DataConn().update_record(recNo, field_name, self.format_for_necessary_size(data[field_name], meta_dada[x]['field_content_length']))
