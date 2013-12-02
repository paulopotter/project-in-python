import dbSchema


class Search(object):

    def search_for_name(self, value = ''):
        db_schema = dbSchema.DbSchema()
        match_values = []
        formatted_records = db_schema.formatted_records()

        for number_of_lines in range(db_schema.number_of_records()):
            formatted_records_lower = formatted_records[number_of_lines]['name'].lower()

            if value != '*' and value.lower() == formatted_records_lower[:len(value)]:
                match_values.append(formatted_records[number_of_lines])

            elif value == '*':
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def search_for_location(self, value = ''):
        match_values = []
        db_schema = dbSchema.DbSchema()
        formatted_records = db_schema.formatted_records()

        for number_of_lines in range(db_schema.number_of_records()):
            formatted_records_lower = formatted_records[number_of_lines]['location'].lower()

            if value != '*' and  value.lower() == formatted_records_lower[:len(value)]:
                match_values.append(formatted_records[number_of_lines])

            elif value == '*':
                match_values.append(formatted_records[number_of_lines])

        return match_values

    def formatted_table(self, dictionary_name, dictionary_location):
        table_column_widths = "| {0:32} | {1:64} | {2:64} | {3:6} | {4:8} | {5:8} |"
        table_header = table_column_widths.format("Name", "Location", "specialties", "size", "rate", "owner") + "\n+" + "="*180 + "+"
        table_data = ""

        for values in dictionary_name:
            table_data += table_column_widths.format(values["name"], values["location"], values["specialties"], values["size"], values["rate"], values["owner"]) + "\n+" + "-"*180 + "+"

        for values in dictionary_location:
            table_data += table_column_widths.format(values["name"], values["location"], values["specialties"], values["size"], values["rate"], values["owner"]) + "\n+" + "-"*180 + "+"

        if len(dictionary_name) + len(dictionary_location) >= 1:
            return table_header + '\n'+ table_data
        else:
            return 'ERROR'
