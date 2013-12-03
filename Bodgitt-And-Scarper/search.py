import dbSchema


class Search(object):

    def search_for(self, value, field_to_search):
        db_schema = dbSchema.DbSchema()
        match_values = []
        formatted_records = db_schema.formatted_records()

        for number_of_lines in range(db_schema.number_of_records()):
            formatted_records_lower = formatted_records[number_of_lines][field_to_search].lower()

            if value != '*' and value.lower() == formatted_records_lower[:len(value)]:
                match_values.append(formatted_records[number_of_lines])

            elif value == '*':
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def search_for_name(self, value = ''):
        return self.search_for(value,'name')

    def search_for_location(self, value = ''):
        return self.search_for(value,'location')

    def formatted_table(self, dictionary_name, dictionary_location):
        table_column_widths = "| {0:2} | {1:32} | {2:64} | {3:64} | {4:6} | {5:8} | {6:8} |"
        table_header = table_column_widths.format("#", "Name", "Location", "Specialties", "Size", "Rate", "Owner")
        table_header += "\n+" + "="*204 + "+"

        name = self.line_of_table(table_column_widths, dictionary_name)
        location = self.line_of_table(table_column_widths, dictionary_location, len(dictionary_name))

        if len(dictionary_name) + len(dictionary_location) >= 1:
            return table_header + '\n'+ name + '\n'+ location
        else:
            return 'ERROR'

    def line_of_table(self, table_column_widths, dictionary_for_lines, number_of_line = 0):
        table_data = ""

        for values in dictionary_for_lines:
            number_of_line += 1
            table_data += table_column_widths.format(
                number_of_line,
                values["name"],
                values["location"],
                values["specialties"],
                values["size"],
                values["rate"],
                values["owner"]
            )
            table_data += "\n+" + "-"*204 + "+\n"

        return table_data
