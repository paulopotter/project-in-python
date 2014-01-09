# coding:utf-8
import argparse
import crud
import texttable


class CommandTerminal(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='File search for dbSchema')
        parser.add_argument('-n', '--name', action='store', dest='name', default=None, required=False, help='Search and list all names according to specified criteria.')
        parser.add_argument('-l', '--location', action='store', dest='location', default=None, required=False, help='Search and list all locations according to specified criteria.')
        parser.add_argument('-a', '--and', action='store_true', dest='search_and', default=False, required=False, help='Se utilizado será feito a busca no nome E location( name e location obrigatorios).')
        parser.add_argument('-c', '--create', action='store', dest='create', default=None, required=False, help='Cria um novo registro.')
        parser.add_argument('-d', '--delete', action='store', dest='delete', default=None, required=False, help='Apaga um registro.')

        arguments = parser.parse_args()

        self.name = arguments.name
        self.location = arguments.location
        self.search_and = arguments.search_and

        self.crud = crud.CRUD()
        self.find = self.crud.find(**{'name': self.name, 'location': self.location, 'search_and': self.search_and})

        if self.find == []:
            print 'Sorry, we could not find the value of the search.'

        else:
            text_table = texttable.Texttable()
            header = ['#', 'Name', 'Location', 'Specialties', 'Size', 'Rate', 'Owner']

            text_table.header(header)
            bla = 0

            for line_records in range(len(self.find)):
                row = self.crud.read(self.find[line_records])
                bla = bla + row[0]

                if row[-1] != 1:  # Se o byte flag for false, exibe
                    row.pop(-1)  # Remove a exibiçao do byte flag
                    text_table.add_row(row)
                else:
                    row.pop(-1)  # Remove a exibiçao do byte flag

            text_table.set_cols_width([2, 25, 15, 50, 5, 10, 5])
            text_table.set_cols_align(['c', 'l', 'l', 'l', 'c', 'l', 'l'])
            print text_table.draw()


if __name__ == '__main__':
    try:
        CommandTerminal()
    except:
        print 'erro: no show data'
