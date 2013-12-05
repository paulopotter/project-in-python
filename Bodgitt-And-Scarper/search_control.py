# coding:utf-8
import data_conn
import formatting_of_data
from my_exceptions import RecordNotFoundException

class SearchControl(object):

    def search_for(self, value, field_to_search):
        db_schema = data_conn.DataConn()
        formatted_of_data = formatting_of_data.FormattingOfData()
        match_values = []
        formatted_records = formatted_of_data.formatted_records()

        for number_of_lines in range(db_schema.number_of_records()):
            formatted_record = formatted_records[number_of_lines][field_to_search]

            if value == '*' or \
            (type(value) == str and value.lower() == formatted_record.lower()[:len(value)]) or \
            (type(value) == int and value == formatted_record) :
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def line_of_table(self, table_column_widths, dictionary_for_lines):
        table_data = ""

        for values in dictionary_for_lines:
            table_data += table_column_widths.format(
                values['id'],
                values["name"],
                values["location"],
                values["specialties"],
                values["size"],
                values["rate"],
                values["owner"]
            )
            table_data += "\n+" + "-" * 204 + "+\n"

        return table_data

    def find(self, criteria):
        find_value = self.search_for(criteria, 'name')
        positions = []
        for line in range(len(find_value)):
            positions.append(find_value[line]['id'])

        return positions

    def read(self, recNo):
        try:
            return self.search_for(recNo, 'id')[0]
        except IndexError:
            raise RecordNotFoundException('Record with this position not found.')

