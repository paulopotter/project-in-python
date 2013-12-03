import argparse
import search


search_class = search.Search()




def searching():
    parser = argparse.ArgumentParser(description = 'DESCRIPTION: Arquivo de busca para o dbSchema')

    parser.add_argument('--name','-n', action = 'store', dest = 'name', default = '', required = False, help = 'Name of data')
    parser.add_argument('--location','-l', action = 'store', dest = 'location', default = '', required = False, help = 'Location of data')

    arguments = parser.parse_args()
    return {'name' : arguments.name,'location' : arguments.location}


if searching()['name'] != '' :
    if searching()['location'] == '':
        print search_class.formatted_table(search_class.search_for_name(searching()['name']), {})
    else:
        print search_class.formatted_table(search_class.search_for_name(searching()['name']), search_class.search_for_location(searching()['location'])
            )
else:
    if searching()['location'] != '':
        print search_class.formatted_table({}, search_class.search_for_location(searching()['location']))

    else:
        print search_class.formatted_table(search_class.search_for_name('*'), {})
