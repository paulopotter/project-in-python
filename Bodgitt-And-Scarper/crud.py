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
            DataConn().pack_in_file(value)