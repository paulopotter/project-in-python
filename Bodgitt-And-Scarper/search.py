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

    def formatted_table(self, dictionary_val):
        table_column_widths = "| {0:2} | {1:32} | {2:64} | {3:64} | {4:6} | {5:8} | {6:8} |"
        table_header = table_column_widths.format("#", "Name", "Location", "Specialties", "Size", "Rate", "Owner")
        table_header += "\n+" + "="*204 + "+"

        table_line = ''
        number_of_line = 0

        for dict_key, dict_value in dictionary_val.items():
            if dict_value != '':
                table_line += self.line_of_table(table_column_widths, self.search_for(dict_value, dict_key), number_of_line)
            number_of_line += len(dict_key)

        if number_of_line >= 1:
            return table_header + '\n'+ table_line
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
