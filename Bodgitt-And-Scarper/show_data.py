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
        parser.add_argument('-d', '--delete', action='store', dest='delete', nargs='+', default=None, required=False, help='Apaga registro com o ID passado (use espaços para apagar mais de um registro ao mesmo tempo). Se passado um texto, apaga todas as ocorrências deste texto.')

        parser.add_argument('-u', '--update', action='store', dest='update', nargs='*', default=None, required=False, help='Adiciona o Id do usuario no registro informado, o primeiro valor é o campo a ser editado e o segundo o ID do usuario.(Ex.: 00 11)')

        arguments = parser.parse_args()

        self.crud = crud.CRUD()
        self.find = self.crud.find({'name': arguments.name, 'location': arguments.location, 'search_and': arguments.search_and})

        if arguments.create:

            verify_entry_type = self.crud.verify_entry_type(arguments.create)
            if not verify_entry_type:
                create = self.crud.create(arguments.create)
                if type(create) == int:
                    message = 'Registro [%i] criado com sucesso!' % create
                else:
                    message = create
                print message
            else:
                print verify_entry_type

        elif arguments.delete:
            try:
                int(arguments.delete[0])
                for recNo in arguments.delete:
                    self.crud.delete(recNo)
                    print 'Registro [%s] apagado com sucesso!' % recNo

            except:
                value = ' '.join(str(x) for x in arguments.delete)
                records = self.crud.find({'name': str(value), 'location': None, 'search_and': False})
                if records:
                    for recNo in records:
                        self.crud.delete(int(recNo))
                        print 'Registro [%s] apagado com sucesso!' % recNo
                else:
                    print 'ERRO: Registro não encontrado'

        elif arguments.update:
            if len(arguments.update) != 2:
                print 'ERRO: São necessario 2 valores, você digitou %i. \nLembrando: o primeiro valor é o NUMERO do registro a ser editado e o segundo o ID do usuario' % len(arguments.update)
            else:
                self.crud.update(arguments.update[0], {'owner': arguments.update[1]})
                print 'Registro [%s] atualizado com sucesso!' % arguments.update[0]

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

                text_table.set_cols_width([2, 32, 32, 50, 6, 8, 8])
                text_table.set_cols_align(['c', 'l', 'l', 'l', 'c', 'l', 'l'])
                print text_table.draw()


if __name__ == '__main__':
    try:
        CommandTerminal()
    except Exception as e:
        print 'Erro:', e
