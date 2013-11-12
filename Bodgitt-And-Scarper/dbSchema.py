import struct #pack e unpack

arquivo = './db-2x1.db'
tuplaMetaDados = []
tuplaMetaFieldLength = []
tuplaDados =[]
listDados = []

fd = open(arquivo,'rb+')

def tamanhoArquivo(fd1 = arquivo):
	fda = open(fd1,'rb')
	tamanho = len(fda.read())
	fda.close()
	return tamanho

def ReadBytes(fd, noBytes):
	data = fd.read(noBytes)
	return data

# Magic Cookie
magicCookieValue = struct.unpack('4B',ReadBytes(fd,4))

# Total Overall Length
totalOverallLength = struct.unpack('4B',ReadBytes(fd,4))
numTotalOverallLength = int(totalOverallLength[-1])

# Number of Fields
numberOfFields = struct.unpack('2B',ReadBytes(fd,2))
numNumberOfFields = int(numberOfFields[-1])

# MetaDado
for x in range(numNumberOfFields):

	# Bytes of Field Name
	bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
	numBytesOfFieldName = int(bytesOfFieldName[-1])

	# Nome do Campo
	fieldName = struct.unpack(str(numBytesOfFieldName)+'s',ReadBytes(fd,numBytesOfFieldName))
	strFieldName = fieldName[0]

	# End of Repeating Block
	endOfRepeatingBlock = struct.unpack('2B',ReadBytes(fd,2))
	numEndOfRepeatingBlock = int(endOfRepeatingBlock[-1])

	tuplaMetaDados.append(strFieldName)
	tuplaMetaFieldLength.append(numEndOfRepeatingBlock)

totalLinhasRegistro = int(tamanhoArquivo())/int(numTotalOverallLength)
# Dados
for y in range(totalLinhasRegistro):
	# Byte flag
	byteFlag = struct.unpack('B',ReadBytes(fd,1))

	#Bytes of Field Name
	bytesOfFieldName = struct.unpack(str(tuplaMetaFieldLength[0]-2)+'s 2B '+str(tuplaMetaFieldLength[1]-2)+'s 2B '+str(tuplaMetaFieldLength[2]-2)+'s 2B '+str(tuplaMetaFieldLength[3]-2)+'s 2B '+str(tuplaMetaFieldLength[4]-2)+'s 2B '+str(tuplaMetaFieldLength[5]-2)+'s 2B',ReadBytes(fd,numTotalOverallLength))
	
	tuplaDados.append(bytesOfFieldName)
	
	i = -3
	metaDadoFormatado = {}
	for metaDado in tuplaMetaDados:
		i += 3
		metaDadoFormatado[metaDado] = tuplaDados[y][i].strip()
	
	metaDadoFormatado['Byte Flag'] = byteFlag[0]
	listDados.append(metaDadoFormatado)

#fechando o arquivo aberto
fd.close()


#------- Exibindo ------
# print '='*50,'\n'
# print "Primeiro dado da Lista: ",listDados[0]
# print '\n','-'*21,'\n'
# print "Segundo dado da Lista: ",listDados[1]
# print '\n','-'*21,'\n'
# print "Lista no formato: ",type(listDados)
# print '\n','-'*21,'\n'
# print "Todos os dados da lista: ",type(listDados)
# print '\n','='*50