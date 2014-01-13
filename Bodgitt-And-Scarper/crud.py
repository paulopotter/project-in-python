# coding:utf-8
from data_conn import DataConn
from my_exceptions import RecordNotFoundException


class CRUD(object):

    def find(self, criteria):
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

    def create(self, values):
        if values[0] == ' ' or len(values) == 1 or values[1] == ' ':
            return 'ERRO: Campo \'name\' ou \'location\' OBRIGATÓRIOS!'

        elif len(values) > 6:
            return 'ERRO: A quantidade total de campos são 6, você informou %i' % len(values)

        else:
            records = DataConn().records()
            empty_fields = []
            meta_dada = DataConn().meta_dada
            if len(values) < len(meta_dada):
                for x in range(len(meta_dada) - len(values)):
                    values.append(' ')

            for row in records:
                if row[-1] == 1:
                    empty_fields.append(row[0])

            if not empty_fields:
                formatted_records = []
                for x in range(len(values)):
                    formatted_records.append(self.format_for_necessary_size(values[x], meta_dada[x]['field_content_length']))

                field_number_created = DataConn().pack_in_file(formatted_records) + 1

            else:
                formatted_records = {}
                for x in range(len(values)):
                    formatted_records[meta_dada[x]['field_name']] = self.format_for_necessary_size(values[x], meta_dada[x]['field_content_length'])

                self.update_record(empty_fields[0], formatted_records)

                field_number_created = empty_fields[0]

            return field_number_created

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
            if self.read(recNo)[-1] == 0:
                DataConn().set_byte_flag_true(records[recNo][0])
                return 'Registro [%i] apagado com sucesso!' % recNo
            else:
                raise RecordNotFoundException

        except IndexError:
            raise RecordNotFoundException

    def update(self, recNo, data):
        if self.read(recNo)[-1] == 0:
            self.update_record(recNo, data)
            return 'Registro [%i] atualizado com sucesso!' % recNo
        else:
            raise RecordNotFoundException

    def update_record(self, recNo, data):
        meta_dada = DataConn().meta_dada

        for field_name in data.keys():
            x = -1
            for item in meta_dada:
                x += 1
                if field_name in item.values():
                    DataConn().update_record(recNo, field_name, self.format_for_necessary_size(data[field_name], meta_dada[x]['field_content_length']))

    def verify_entry_type(self, values):
        only_numbers = ['size', 'owner', 'rate']
        size_field = DataConn().meta_dada
        entry_type = 0

        for x in range(len(values)):
            if size_field[x]['field_name'] in only_numbers:
                try:
                    int(values[x])
                    if len(values[x]) <= size_field[x]['field_content_length']:
                        entry_type += 1
                    else:
                        return 'ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])}
                except:
                    return 'ERRO: Campo \'%s\' suporta apenas numeros' % size_field[x]['field_name']
            else:
                if len(values[x]) <= size_field[x]['field_content_length']:
                    entry_type += 1
                else:
                    return 'ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])}

        return False
