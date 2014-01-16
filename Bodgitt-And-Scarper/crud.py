from data_conn import DataConn
# coding:utf-8
from my_exceptions import RecordNotFoundException
from my_exceptions import DuplicateKeyException


class CRUD(object):

    def find(self, criteria):
        records = DataConn().records()
        positions = []

        if criteria['search_and']:
            for line in range(len(records)):
                if records[line][1].lower().find(criteria['location'].lower()) == 0 and records[line][0].lower().find(criteria['name'].lower()) == 0:
                    positions.append(line)
        else:
            if criteria['name'] == '' and criteria['location'] == '':
                for line in range(len(records)):
                    positions.append(line)

            if criteria['name'] != '':
                for line in range(len(records)):
                    if records[line][0].lower().find(criteria['name'].lower()) == 0:
                        positions.append(line)

            if criteria['location'] != '':
                for line in range(len(records)):
                    if records[line][1].lower().find(criteria['location'].lower()) == 0:
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

    def create(self, values):
        find = self.find({'name': values[0], 'location': values[1], 'search_and': True})

        if not find:
            records = DataConn().records()
            empty_fields = []
            meta_dada = DataConn().meta_dada
            if len(values) < len(meta_dada):
                for x in range(len(meta_dada) - len(values)):
                    values.append(' ')

            for line, row in enumerate(records):
                if row[-1] == 1:
                    empty_fields.append(line)

            if not empty_fields:
                formatted_records = []
                for x in range(len(values)):
                    if meta_dada[x]['field_name'] == 'rate':
                        if values[x][0] != '$':
                            values[x] = '$' + str(values[x])
                    formatted_records.append(self.format_for_necessary_size(values[x], meta_dada[x]['field_content_length']))

                field_number_created = DataConn().pack_in_file(formatted_records)

            else:
                formatted_records = {}
                for x in range(len(values)):
                    formatted_records[meta_dada[x]['field_name']] = self.format_for_necessary_size(values[x], meta_dada[x]['field_content_length'])

                self.update_any_record(empty_fields[0], formatted_records)

                field_number_created = empty_fields[0]

            return field_number_created
        else:
            raise DuplicateKeyException

    def format_for_necessary_size(self, value, size):
        if len(value) < size or value == '':
            difference = size - len(value)
            return value + (' ' * difference)
        elif len(value) > size:
            difference = len(value) - size
            return value[:-difference]
        else:
            return value

    def delete(self, recNo):
        try:
            records = DataConn().records()
            if self.read(int(recNo))[-1] == 0:
                DataConn().set_byte_flag_true_and_clear_values(records[int(recNo)][0], records[int(recNo)][1])
            else:
                raise RecordNotFoundException
        except IndexError:
            raise RecordNotFoundException

    def update(self, recNo, data):
        try:
            recNo = int(recNo)
            if self.read(recNo)[-1] == 0:
                self.update_any_record(recNo, data)
            else:
                raise RecordNotFoundException
        except:
            raise RecordNotFoundException

    def update_any_record(self, recNo, data):
        meta_dada = DataConn().meta_dada

        for field_name in data.keys():
            for line, item in enumerate(meta_dada):
                if field_name in item.values():
                    DataConn().update_record(recNo, field_name, self.format_for_necessary_size(data[field_name], meta_dada[line]['field_content_length']))

    def verify_entry_type(self, values):
        only_numbers = ['size', 'owner']
        size_field = DataConn().meta_dada
        entry_type = 0

        for x in range(len(values)):
            if size_field[x]['field_name'] in only_numbers:
                try:
                    if values[x] != '':
                        int(values[x])
                        if len(values[x]) <= size_field[x]['field_content_length']:
                            entry_type += 1
                        else:
                            return 'ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'] - 1, 'len_value': len(values[x])}
                    else:
                        entry_type += 1

                except:
                    return 'ERRO: Campo \'%s\' suporta apenas numeros' % size_field[x]['field_name']
            elif size_field[x]['field_name'] == 'rate':
                if values[x] != '':
                    if len(values[x]) <= size_field[x]['field_content_length']:
                        try:
                            if values[x][0] == '$':
                                float(values[x][1:])
                                entry_type += 1
                            else:
                                float(values[x])
                                entry_type += 1
                        except:
                            return 'O campo rate aceita apenas numero, ponto e $.'

                    else:
                        return 'ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])}
                else:
                    entry_type += 1
            else:
                if len(values[x]) <= size_field[x]['field_content_length']:
                    entry_type += 1
                else:
                    return 'ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])}

        return False
