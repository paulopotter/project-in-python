# coding:utf-8
from data_conn import DataConn
from my_exceptions import RecordNotFoundException
from my_exceptions import DuplicateKeyException


class CRUD(object):

    def find(self, **criteria):
        records = DataConn().records()
        positions = []

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
        if value == ():
            return 'Erro'
        else:
            number_of_fields = len(DataConn().meta_dada)
            x = 0
            new_value = []
            while x < number_of_fields:
                new_value.append(self.deixa_no_tamanho_necessario(value[x], DataConn().meta_dada[x]['field_content_length']))
                x += 1
        DataConn().pack_in_file(new_value)
    
    def deixa_no_tamanho_necessario(self, value, size):
        if len(value) < size:
            difference = size - len(value)
            return value + (' ' * difference)
        else:
            return value
