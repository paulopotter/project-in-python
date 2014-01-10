# coding:utf-8
import argparse
import crud
import texttable


class CommandTerminal(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='File search for dbSchema')
        parser.add_argument('-n', '--name', action='store', dest='name', default=None, required=False, help='Procura e lista todos os registros com o \'name\' informada.')
        parser.add_argument('-l', '--location', action='store', dest='location', default=None, required=False, help='Procura e lista todos os registros com a \'location\' informada.')
        parser.add_argument('-a', '--and', action='store_true', dest='search_and', default=False, required=False, help='Se utilizado será feito a busca no \'name\' E \'location\'( \'name\' e \'location\' obrigatórios).')
        parser.add_argument('-c', '--create', action='store', nargs='+', dest='create', default=None, required=False, help='Cria um novo registro. Espaços serão considerados novos campos (para digitar um texto com espaço use aspas). \'name\' e \'location\' obrigatórios.')
        parser.add_argument('-d', '--delete', action='store', dest='delete', nargs='+', default=None, required=False, help='Apaga registro com o ID passado.')

        arguments = parser.parse_args()

        self.crud = crud.CRUD()
        self.find = self.crud.find({'name': arguments.name, 'location': arguments.location, 'search_and': arguments.search_and})

        if arguments.create:
            print self.crud.create(arguments.create)

        elif arguments.delete:
            print self.crud.delete(int(arguments.delete))

        else:
            if self.find == []:
                print 'Registro informado não encontrado.'

            else:
                text_table = texttable.Texttable()
                header = ['#', 'Name', 'Location', 'Specialties', 'Size', 'Rate', 'Owner']

                text_table.header(header)

                for line_records in range(len(self.find)):
                    row = self.crud.read(self.find[line_records])

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
    except Exception as e:
        print 'Exception:', e
