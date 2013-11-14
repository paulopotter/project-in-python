import struct

arquivo = './db-2x1.db'
tuple_meta_dados = []
tuple_meta_field_length = []
tuple_dados =[]
list_dados = []

fd = open(arquivo,'rb+')
def ReadBytes(fd, noBytes):
    data = fd.read(noBytes)
    return data

def tamanhoArquivo(fd1):
    fd = open(fd1,'rb')
    tamanho = len(fd.read())
    fd.close()
    return tamanho

# Magic Cookie
magic_cookie_value = struct.unpack('4B',ReadBytes(fd,4))

# Total Overall Length
total_overall_length = struct.unpack('4B',ReadBytes(fd,4))
number_total_overall_length = int(total_overall_length[-1])

# Number of Fields
number_of_fields = struct.unpack('2B',ReadBytes(fd,2))
number_number_of_fields = int(number_of_fields[-1])
# meta_dado
for x in range(number_number_of_fields):

    # Bytes of Field Name
    bytes_of_field_name = struct.unpack('2B',ReadBytes(fd,2))
    number_bytes_of_field_name = int(bytes_of_field_name[-1])

    # Nome do Campo
    field_name = struct.unpack(str(number_bytes_of_field_name)+'s',ReadBytes(fd,number_bytes_of_field_name))
    string_field_name = field_name[0]

    # End of Repeating Block
    end_of_repeating_block = struct.unpack('2B',ReadBytes(fd,2))
    numend_of_repeating_block = int(end_of_repeating_block[-1])

    tuple_meta_dados.append(string_field_name)
    tuple_meta_field_length.append(numend_of_repeating_block)


total_linhas_registro = int(tamanhoArquivo(arquivo)) / int(number_total_overall_length)

for y in range(total_linhas_registro):

    byte_flag = struct.unpack('B',ReadBytes(fd,1))

    bytes_of_field_name = struct.unpack(str(tuple_meta_field_length[0] - 2) + 's 2B ' + str(tuple_meta_field_length[1] - 2) + 's 2B ' +
                                        str(tuple_meta_field_length[2] - 2) + 's 2B ' + str(tuple_meta_field_length[3] - 2) + 's 2B ' +
                                        str(tuple_meta_field_length[4] - 2) + 's 2B ' + str(tuple_meta_field_length[5] - 2) + 's 2B',
                                        ReadBytes(fd,number_total_overall_length))
    
    tuple_dados.append(bytes_of_field_name)
    
    k = -3
    meta_dado_formatado = {}
    for meta_dado in tuple_meta_dados:
        k += 3
        meta_dado_formatado[meta_dado] = tuple_dados[y][k].strip()

    
    meta_dado_formatado['Byte Flag'] = byte_flag[0]
    list_dados.append(meta_dado_formatado)

fd.close()


#------- Exibindo ------
# print '='*50,'\n'
# print "Primeiro dado da Lista: ",list_dados[0]
# print '\n','-'*21,'\n'
# print "Segundo dado da Lista: ",list_dados[1]
# print '\n','-'*21,'\n'
# print "Lista no formato: ",type(list_dados)
# print '\n','-'*21,'\n'
# print "Todos os dados da lista: ",list_dados
# print '\n','='*50