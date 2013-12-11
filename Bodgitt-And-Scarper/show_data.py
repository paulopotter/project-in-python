# coding:utf-8
import argparse
import search_control
import formatting_of_table

search_class = search_control.SearchControl()
formatting_table_class = formatting_of_table.FormattingOfTable()


def searching():

    parser = argparse.ArgumentParser(description='Arquivo de busca para o dbSchema')

    parser.add_argument('--name', action='store', dest='name', default='', required=False, help='Search and list all names according to specified criteria.')
    parser.add_argument('--location', action='store', dest='location', default='', required=False, help='Search and list all locations according to specified criteria.')
    parser.add_argument('--read', action='store', dest='read', default='', required=False, help='Read a single data')
    parser.add_argument('--find', action='store', dest='find', default='', required=False, help='Find data and return Id array')

    arguments = parser.parse_args()

    if arguments.read != '':
        return {'read': arguments.read}
    elif arguments.find != '':
        return {'find': arguments.find}
    else:
        if arguments.name == '' and arguments.location == '':
            return {'name': '*', 'location': arguments.location}
        else:
            return {'name': arguments.name, 'location': arguments.location}


search = searching()

if 'read' in search:
    read = search_class.read(int(search['read']))
    print formatting_table_class.formatted_table({'id': read['id']})

elif 'find' in search:
    print search_class.find(search['find'])

else:
    print formatting_table_class.formatted_table(searching())
