import struct #pack e unpack
import pdb #Debug
import sys #exit()
arquivo = './db-2x1.db'
tuplaMetaDados = []
tuplaMetaFieldLength = []
tuplaDados =[]
dicionario = {}
tuplaByteFlag = []
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
numTotalOverallLength = int(totalOverallLength[3])

# Number of Fields
numberOfFields = struct.unpack('2B',ReadBytes(fd,2))
numNumberOfFields = int(numberOfFields[1])

# MetaDado
for x in range(numNumberOfFields):

	# Bytes of Field Name
	bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
	numBytesOfFieldName = int(bytesOfFieldName[1])

	# Nome do Campo
	fieldName = struct.unpack(str(numBytesOfFieldName)+'s',ReadBytes(fd,numBytesOfFieldName))
	strFieldName = fieldName[0]

	# End of Repeating Block
	endOfRepeatingBlock = struct.unpack('2B',ReadBytes(fd,2))
	numEndOfRepeatingBlock = int(endOfRepeatingBlock[1])

	tuplaMetaDados.append(strFieldName)
	tuplaMetaFieldLength.append(numEndOfRepeatingBlock)


# Cria as variaveis metaDado(x) dinamicamente
for i in range(numNumberOfFields):
	locals()['metaDado%d'%i] = []

# Dados
# for y in range(3):
for y in range(int(tamanhoArquivo())/int(numTotalOverallLength)):
	# Byte flag
	byteFlag = struct.unpack('B',ReadBytes(fd,1))
	#Bytes of Field Name
	bytesOfFieldName = struct.unpack(str(tuplaMetaFieldLength[0]-2)+'s 2B '+str(tuplaMetaFieldLength[1]-2)+'s 2B '+str(tuplaMetaFieldLength[2]-2)+'s 2B '+str(tuplaMetaFieldLength[3]-2)+'s 2B '+str(tuplaMetaFieldLength[4]-2)+'s 2B '+str(tuplaMetaFieldLength[5]-2)+'s 2B',ReadBytes(fd,numTotalOverallLength))

	tuplaDados.append(bytesOfFieldName)
	listDados.append({
					tuplaMetaDados[0]:tuplaDados[y][0].strip(),
					tuplaMetaDados[1]:tuplaDados[y][3].strip(),
					tuplaMetaDados[2]:tuplaDados[y][6].strip(),
					tuplaMetaDados[3]:tuplaDados[y][9].strip(),
					tuplaMetaDados[4]:tuplaDados[y][12].strip(),
					tuplaMetaDados[5]:tuplaDados[y][15].strip(),
				   'Byte Flag':      byteFlag[0]
				   })

#fechando o arquivo aberto
fd.close()

# Adicionando todos os campos metadado(x) no dicionario
for i in range(numNumberOfFields):
	dicionario[tuplaMetaDados[i]] = locals()['metaDado%d'%i]
dicionario["byteFlag"] = tuplaByteFlag


#------- Exibindo ------
print '='*50,'\n'
print listDados[0]
print '\n','-'*21,'\n'
print listDados[1]
print '\n','-'*21,'\n'
print listDados
# print "MetaDados :",tuplaMetaDados
# print "Data: ",dicionario
# print '\n','-'*21,'\n'
print '\n','='*50