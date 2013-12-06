# coding:utf-8
import argparse
import search_control
import formatting_of_table

search_class = search_control.SearchControl()
formatting_table_class = formatting_of_table.FormattingData()

def searching():
    parser = argparse.ArgumentParser(description = 'Arquivo de busca para o dbSchema')

    parser.add_argument('--name',
        action = 'store',
        dest = 'name',
        default = '',
        required = False,
        help = 'Name of data'
    )
    parser.add_argument('--location',
        action = 'store',
        dest = 'location',
        default = '',
        required = False,
        help = 'Location of data'
    )
    parser.add_argument('--read',
        action = 'store',
        dest = 'read',
        default = '',
        required = False,
        help = 'Read data'
    )
    parser.add_argument('--find',
        action = 'store',
        dest = 'find',
        default = '',
        required = False,
        help = 'Find data and return Id array'
    )

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

if search.has_key('read'):
    read = search_class.read(int(search['read']))
    print formatting_table_class.formatted_table({'id': read['id']})

elif search.has_key('find'):
    print search_class.find(search['find'])

else:
    print formatting_table_class.formatted_table(searching())
