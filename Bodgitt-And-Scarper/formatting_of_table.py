# coding:utf-8
import search_control


class FormattingOfTable(object):

    def __init__(self):
        self.search_class = search_control.SearchControl()

    def formatted_table(self, dictionary_values):
        table_column_widths = "| {0:2} | {1:32} | {2:64} | {3:64} | {4:6} | {5:8} | {6:8} |"
        table_header = table_column_widths.format(
            "ID", "Name", "Location", "Specialties", "Size", "Rate", "Owner")
        table_header += "\n+" + "=" * 204 + "+"

        table_line = ''

        for dict_key, dict_value in dictionary_values.items():
            if dict_value != '':
                table_line += self.line_of_table(
                    table_column_widths, self.search_class.search_for(dict_value, dict_key))

        if table_line != '':
            return table_header + '\n' + table_line
        else:
            return 'ERROR: Não existe registro com o(s) parametros passados.'

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
