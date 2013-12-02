# import argparse
import dbSchema


class Search(object):

    def __init__(self):
        self.db_schema = dbSchema.DbSchema()

    def search_for_name(self, value = ''):
        match_values = []
        formatted_records = self.db_schema.formatted_records()
        for number_of_lines in range(self.db_schema.number_of_records()):
            if value != '*' and value in formatted_records[number_of_lines]['name']:
                match_values.append(formatted_records[number_of_lines])
            elif value == '*':
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def search_for_location(self, value = ''):
        match_values = []
        formatted_records = self.db_schema.formatted_records()
        for number_of_lines in range(self.db_schema.number_of_records()):
            if value != '*' and value in formatted_records[number_of_lines]['location']:
                match_values.append(formatted_records[number_of_lines])
            elif value == '*':
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def search_in_table(self, dictionary):
        table_column_widths = "| {0:32} | {1:64} | {2:64} | {3:6} | {4:8} | {5:8} |"
        table_header = table_column_widths.format("Name", "Location", "specialties", "size", "rate", "owner") + "\n+" + "="*180 + "+"
        table_data = ""

        for values in dictionary:
            table_data += table_column_widths.format(values["name"], values["location"], values["specialties"], values["size"], values["rate"], values["owner"]) + "\n+" + "-"*180 + "+"

        if len(dictionary) < 0:
            return table_header + '\n'+ table_data
        else:
            return 'ERROR'






# # --------- parametros por linha de comando------- #
#     def searching():
#         parser = argparse.ArgumentParser(description = 'DESCRIPTION: Arquivo de busca para o dbSchema')

#         parser.add_argument('--name, --n', action = 'store', dest = 'name', default = '*', required = False, help = 'Name of data')
#         parser.add_argument('--location, --loc', action = 'store', dest = 'location', default = '*', required = False, help = 'Location of data')

#         arguments = parser.parse_args()
#         return arguments.name

# # print searching()
