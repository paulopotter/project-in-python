# coding:utf-8
from data_conn import DataConn
from my_exceptions import RecordNotFoundException
from my_exceptions import DuplicateKeyException
from log import LOG


class CRUD(object):

    def __init__(self):
        self.meta_data = DataConn().meta_dada
        self.only_log = 'info'

    def find(self, criteria):
        if criteria['search_and']:
            and_or = 'e'
        else:
            and_or = 'ou'

        records = DataConn().records()
        positions = []
        positions_name = []
        positions_location = []

        if criteria['name'] == '' and criteria['location'] == '':
            for line in range(len(records)):
                positions.append(line)
            return positions

        LOG('info', self.only_log).message('Busca feita por: "' + criteria['name'] + '" ' + and_or + ' "' + criteria['location'] + '"')
        if criteria['name']:
            for line in range(len(records)):
                if records[line][0].lower().find(criteria['name'].lower()) == 0:
                    positions_name.append(line)
        if criteria['location']:
            for line in range(len(records)):
                if records[line][1].lower().find(criteria['location'].lower()) == 0:
                    positions_location.append(line)

        if criteria['search_and']:
            line_records = list(set(positions_name).intersection(set(positions_location)))
        else:
            positions_name.extend(positions_location)
            line_records = list(set(positions_name))

        line_records.sort()

        return line_records

    def read(self, recNo):
        try:
            records = DataConn().records()
            line_value = records[recNo]
            return line_value
        except IndexError:
            LOG('debug', self.only_log).message('IndexError no read. recNo = ' + str(recNo))
            raise RecordNotFoundException

    def create(self, values):
        matches = self.find({'name': values[0], 'location': values[1], 'search_and': True})
        if not matches:
            self.verify_entry_type(values)
            records = DataConn().records()
            meta_dada = DataConn().meta_dada

            formatted_records = {}
            for line, row in enumerate(records):
                if row[-1] == 1:
                    for x in range(len(values)):
                        formatted_records[meta_dada[x]['field_name']] = self.format_for_necessary_size(values[x], meta_dada[x]['field_name'])

                    self.update_any_record(line, formatted_records)
                    field_number_created = line
                    break

            else:
                formatted_records = []
                for x in range(len(values)):
                    formatted_records.append(self.format_for_necessary_size(values[x], meta_dada[x]['field_name']))
                formatted_records.append(self.format_for_necessary_size('', 'owner'))
                field_number_created = DataConn().pack_in_file(formatted_records)
            LOG('info', self.only_log).message('Criado registro. %i. valores: %s' % (field_number_created, str(values)))
            return field_number_created
        else:
            LOG('debug', self.only_log).message('DuplicateKeyException no create. valores: ' + str(values))
            raise DuplicateKeyException

    def format_for_necessary_size(self, value, field_name):
        meta_dada = DataConn().meta_dada
        for field in meta_dada:
            if field_name in field.values():
                size = field['field_content_length']

                if field_name == 'rate':
                    if value != '' and value[0] != '$':
                        value = '$' + str(value)

                if len(value) < size or value == '':
                    difference = size - len(value)
                    value = value + (' ' * difference)
                elif len(value) > size:
                    raise Exception("ERRO: o campo %s contem %i caracters e o campo suporta até %i" % (field_name, len(value), size))

                return value

    def delete(self, recNo):
        try:
            records = DataConn().records()
            if self.read(int(recNo))[-1] == 0:
                DataConn().set_byte_flag_true_and_clear_values(records[int(recNo)][0], records[int(recNo)][1])
                LOG('info', self.only_log).message('Registro %i deletado.' % recNo)
            else:
                LOG('debug', self.only_log).message('Tentativa de exclusão de registro ja deletado. recNo: ' + str(recNo))
                raise RecordNotFoundException
        except IndexError:
            LOG('debug', self.only_log).message('RecordNotFoundException no delete. recNo: ' + str(recNo))
            raise RecordNotFoundException

    def update(self, recNo, data):
        try:
            recNo = int(recNo)
            if self.read(recNo)[-1] == 0:
                self.update_any_record(recNo, data)
                LOG('info', self.only_log).message('Registro %i alterado para: %s' % (recNo, str(data)))
            else:
                LOG('debug', self.only_log).message('Tentativa de update do registro %i que não pode ser alterado.' % recNo)
                raise RecordNotFoundException
        except:
            LOG('debug', self.only_log).message('RecordNotFoundException em update. Registro numero: %i' % recNo)
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
                            raise Exception('ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'] - 1, 'len_value': len(values[x])})
                    else:
                        entry_type += 1

                except:
                    raise Exception('ERRO: Campo \'%s\' suporta apenas numeros' % size_field[x]['field_name'])
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
                            raise Exception('O campo rate aceita apenas numero, ponto e $.')

                    else:
                        raise Exception('ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])})
                else:
                    entry_type += 1
            else:
                if len(values[x]) <= size_field[x]['field_content_length']:
                    entry_type += 1
                else:
                    raise Exception('ERRO: Campo \'%(field)s\' suporta até \'%(size_field)s\' caracters, você usou \'%(len_value)s\'.' % {'field': size_field[x]['field_name'], 'size_field': size_field[x]['field_content_length'], 'len_value': len(values[x])})

        return True
