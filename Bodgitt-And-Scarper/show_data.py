# coding:utf-8
import argparse
import search_control
import texttable


class CommandTerminal(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='Arquivo de busca para o dbSchema')
        parser.add_argument('-n, --name', action='store', dest='name', default=None, required=False, help='Search and list all names according to specified criteria.')
        parser.add_argument('-l, --location', action='store', dest='location', default=None, required=False, help='Search and list all locations according to specified criteria.')

        arguments = parser.parse_args()

        self.name = arguments.name
        self.location = arguments.location


if __name__ == '__main__':
    CommandTerminal()


search = search_control.SearchControl()
find = search.find(**{'name': CommandTerminal().name, 'location': CommandTerminal().location})


if find == []:
    print 'Sorry, we could not find the value of the search.'

else:
    text_table = texttable.Texttable()
    header = ['#', 'Name', 'Location', 'Specialties', 'Size', 'Rate', 'Owner']

    text_table.header(header)

    for line_records in range(len(find)):
        row = search.read(find[line_records])
        row.pop(-1)  # Remove a exibiçao do byte flag
        text_table.add_row(row)

    text_table.set_cols_width([2, 25, 15, 50, 5, 10, 5])
    text_table.set_cols_align(['c', 'l', 'l', 'l', 'c', 'l', 'l'])
    print text_table.draw()
