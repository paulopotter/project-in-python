# coding:utf-8
import argparse
import search_control

search_class = search_control.SearchControl()

def searching():
    parser = argparse.ArgumentParser(description = 'DESCRIPTION: Arquivo de busca para o dbSchema')

    parser.add_argument('--name','-n',
        action = 'store',
        dest = 'name',
        default = '',
        required = False,
        help = 'Name of data'
    )
    parser.add_argument('--location','-l',
        action = 'store',
        dest = 'location',
        default = '',
        required = False,
        help = 'Location of data'
    )

    arguments = parser.parse_args()

    return {'name' : arguments.name, 'location' : arguments.location}

def formatted_table(dictionary_values):
    table_column_widths = "| {0:2} | {1:32} | {2:64} | {3:64} | {4:6} | {5:8} | {6:8} |"
    table_header = table_column_widths.format(
        "ID", "Name", "Location",
        "Specialties", "Size", "Rate", "Owner"
    )
    table_header += "\n+" + "=" * 204 + "+"

    table_line = ''

    for dict_key, dict_value in dictionary_values.items():
        if dict_value != '':
            table_line += line_of_table(
                table_column_widths, search_class.search_for(dict_value, dict_key))

    if table_line != '':
        return table_header + '\n' + table_line
    else:
        return 'ERROR: Não existe registro com o(s) parametros passados'


def line_of_table(table_column_widths, dictionary_for_lines):
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


if searching()['name'] == '' and searching()['location'] == '':
    print formatted_table({'name': '*'})
else:
    print formatted_table(searching())

