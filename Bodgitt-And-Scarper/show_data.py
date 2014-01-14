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
        parser.add_argument('-d', '--delete', action='store_true', dest='delete', default=False, required=False, help='Apaga registro com o ID passado (use espaços para apagar mais de um registro ao mesmo tempo). Se passado um texto, apaga todas as ocorrências deste texto.')

        parser.add_argument('-u', '--update', action='store_true', dest='update', default=False, required=False, help='Altera o \'owner\' do registro encontrado para o ID do usuario a ser informado.')

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
            if not arguments.name or not arguments.location:
                print 'ERRO: \'name\' e/ou \'location\' necessário'
            else:
                print self.draw_table(self.find)
                if self.find:
                    delete_yes_not = raw_input('\nDeseja deletar todos os registros exibidos? \nDigite SIM para apagar e NAO para cancelar a exclusão. ')

                    if delete_yes_not.lower() == 'sim' or delete_yes_not.lower() == 's':
                            excluded_records = 0
                            for recNo in self.find:
                                self.crud.delete(recNo)
                                excluded_records += 1

                            print 'Registro(s) apagado(s) com sucesso!'

                    elif delete_yes_not.lower() == 'nao' or delete_yes_not.lower() == 'não' or delete_yes_not.lower() == 'n':
                        print 'A exclusão foi cancelada'
                    else:
                        print 'Opcão inválida, a exclusão foi cancelada.'
                else:
                    print 'Registro não encontrado.'

        elif arguments.update:
            if not arguments.name or not arguments.location:
                print 'ERRO: \'name\' e/ou \'location\' necessário'
            else:
                print self.draw_table(self.find)
                if self.find:
                    update_yes_not = raw_input('\nDeseja alterar todos os registros exibidos? \nDigite SIM para alterar e NAO para cancelar a alteração. ')

                    if update_yes_not.lower() == 'sim' or update_yes_not.lower() == 's':
                        owner_number_choice = raw_input('\nDigite o valor para alterar o \'owner\' dos registros exibidos ou digite APAGAR para remover todos os valores de \'owner\' dos registros encontrados. \n.Qualquer valor que não se encaixar nesses parametros irá cancelar a alteraçao. ')
                        try:
                            int(owner_number_choice)
                            for x in self.find:
                                self.crud.update(x, {'owner': owner_number_choice})
                                print 'Registro atualizado com sucesso!'
                        except:
                            if owner_number_choice.lower() == 'apagar':
                                for x in self.find:
                                    self.crud.update(x, {'owner': ' '})
                                print 'Registro atualizado com sucesso!'
                            else:
                                print 'Alteraçao foi Cancelada.'

                    elif update_yes_not.lower() == 'nao' or update_yes_not.lower() == 'não' or update_yes_not.lower() == 'n':
                        print 'A atualizaçao foi cancelada'
                    else:
                        print 'Opcão inválida, a alteraçao foi cancelada.'
                else:
                    print 'Registro não encontrado.'

        else:
            print self.draw_table(self.find)

    def draw_table(self, find):
        if find == []:
            return 'Registro informado não encontrado.'

        else:
            text_table = texttable.Texttable()
            header = ['#', 'Name', 'Location', 'Specialties', 'Size', 'Rate', 'Owner']

            text_table.header(header)
            x = 1
            for line_records in range(len(find)):
                row = self.crud.read(find[line_records])

                if row[-1] != 1:  # Se o byte flag for false, exibe
                    row.pop(-1)  # Remove a exibiçao do byte flag
                    text_table.add_row([x] + row)
                    x += 1

            text_table.set_cols_width([2, 32, 32, 50, 6, 8, 8])
            text_table.set_cols_align(['c', 'l', 'l', 'l', 'c', 'l', 'l'])
            return text_table.draw()


if __name__ == '__main__':
    try:
        CommandTerminal()
    except Exception as e:
        print 'Erro:', e
