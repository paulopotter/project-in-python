#! /usr/bin/env python
# coding:utf-8
import argparse
import crud
import texttable


class CommandTerminal(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='File search for dbSchema')
        parser.add_argument('-n', '--name', action='store', nargs='+', dest='name', default='', required=False, help='Procura e lista todos os registros com o \'name\' informada.')
        parser.add_argument('-l', '--location', action='store', nargs='+', dest='location', default='', required=False, help='Procura e lista todos os registros com a \'location\' informada.')
        parser.add_argument('-a', '--and', action='store_true', dest='search_and', default=False, required=False, help='Se utilizado será feito a busca no \'name\' E \'location\'( \'name\' e \'location\' obrigatórios).')

        parser.add_argument('-c', '--create', action='store_true', dest='create', default=None, required=False, help='Cria um novo registro.  \'name\' e \'location\' obrigatórios.')

        parser.add_argument('-d', '--delete', action='store_true', dest='delete', default=False, required=False, help='Apaga registro com o \'name\' e \'location\' passado.(\'name\' e \'location\' obrigatórios.)')

        parser.add_argument('-u', '--update', action='store', dest='update', default=None, required=False, help='Altera o \'owner\' do registro encontrado para o  do usuario informado. Se passar APAGAR o \'owner\' do registro encontrado será limpo. (\'name\' e \'location\' obrigatórios.)')

        parser.add_argument('-p', '--specialties', action='store', nargs='+', dest='specialties', default='', required=False, help='Cria a informaçao passada na posiçao specialties. Utilizado somente quando for criar um registro novo.')
        parser.add_argument('-s', '--size', action='store', dest='size', default='', required=False, help='Cria a informaçao passada na posiçao size. Utilizado somente quando for criar um registro novo.')
        parser.add_argument('-r', '--rate', action='store', dest='rate', default='', required=False, help='Cria a informaçao passada na posiçao rate. Utilizado somente quando for criar um registro novo.')

        arguments = parser.parse_args()

        self.name = ' '.join(arguments.name)
        self.location = ' '.join(arguments.location)
        self.specialties = ' '.join(arguments.specialties)
        self.size = arguments.size
        self.rate = arguments.rate

        self.crud = crud.CRUD()
        self.matches = self.crud.find({'name': self.name, 'location': self.location, 'search_and': arguments.search_and})

        if arguments.create:
            self.check_required_parameters
            # verify_entry_type = self.crud.verify_entry_type([self.name, self.location, self.specialties, self.size, self.rate])
            # if not verify_entry_type:
            self.crud.create([self.name, self.location, self.specialties, self.size, self.rate])
            print 'Registro criado com sucesso!'
            # else:
            #     print verify_entry_type

        elif arguments.delete:
            print self.draw_table(self.matches)

            if self.matches:
                delete_yes_not = raw_input('\nDeseja deletar todos os registros exibidos? \nDigite SIM para apagar e NAO para cancelar a exclusão. ')

                if delete_yes_not.lower() in ['sim', 's']:
                    for recNo in self.matches:
                        self.crud.delete(recNo)

                    print 'Registro(s) apagado(s) com sucesso!'

                elif delete_yes_not.lower() in ['nao', 'não', 'n']:
                    print 'A exclusão foi cancelada'

                else:
                    print 'Opcão inválida, a exclusão foi cancelada.'

        elif arguments.update:
            self.check_required_parameters(self.name, self.location)

            print self.draw_table(self.matches)

            if self.matches:
                update_yes_not = raw_input('\nDeseja alterar todos os registros exibidos? \nDigite SIM para alterar e NAO para cancelar a alteração. ')

                if update_yes_not.lower() in ['sim', 's']:
                    try:
                        int(arguments.update)
                        for x in self.matches:
                            self.crud.update(x, {'owner': arguments.update})
                            mensage = 'Registro atualizado com sucesso!'
                    except:
                        if arguments.update.lower() == 'apagar':
                            for x in self.matches:
                                self.crud.update(x, {'owner': ' '})
                            mensage = 'Registro atualizado com sucesso!'
                        else:
                            mensage = 'Alteraçao foi Cancelada. Digite apenas numeros ou apagar.'
                else:
                    mensage = 'Alteraçao foi Cancelada'

                print '\n' + mensage

        else:
            print self.draw_table(self.matches)

    def draw_table(self, matches):
        if not matches:
            return 'Registro informado não encontrado.'

        else:
            text_table = texttable.Texttable()
            header = ['#', 'Name', 'Location', 'Specialties', 'Size', 'Rate', 'Owner']

            text_table.header(header)
            x = 1
            for line_records in range(len(matches)):
                row = self.crud.read(matches[line_records])

                if row[-1] != 1:  # Se o byte flag for false, exibe
                    row.pop(-1)  # Remove a exibiçao do byte flag
                    text_table.add_row([x] + row)
                    x += 1

            text_table.set_cols_width([2, 32, 32, 50, 6, 8, 8])
            text_table.set_cols_align(['c', 'l', 'l', 'l', 'c', 'l', 'l'])
            return text_table.draw()

    def check_required_parameters(self, *parameters):
        for parameter in parameters:
            if not parameter:
                raise Exception('ERRO: \'name\' e/ou \'location\' necessário')

        return True


if __name__ == '__main__':
    try:
        CommandTerminal()
    except Exception as e:
        print e
