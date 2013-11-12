import struct #pack e unpack
import pdb #Debug
import sys #exit()

tuplaMetaDados = []
tuplaDados =[]
dicionario = {}
fd = open('./db-2x1.db','rb+')

def tamanhoArquivo(fd1 ='./db-2x1.db'):
	fda = open(fd1,'rb')
	tamanho = len(fda.read())
	fda.close()
	return tamanho


def ReadBytes(fd, noBytes):
 data = fd.read(noBytes)
 return data




# Magic Cookie
magicCookieValue = struct.unpack('4B',ReadBytes(fd,4))

#Total Overall Length
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

	# print totalOverallLength
	# print "Field Length: ",numBytesOfFieldName
	# print "Field Name:",strFieldName
	# print "end of Repeating Block:",numEndOfRepeatingBlock
	# print '-'*20
	tuplaMetaDados.append(strFieldName)
	# tuplaMetaDados.append(numEndOfRepeatingBlock)


# Cria as variaveis metaDado(x) dinamicamente
for i in range(numNumberOfFields):
	locals()['metaDado%d'%i] = []
tuplaByteFlag = []

print numberOfFields
# Dados
for y in range(int(tamanhoArquivo())/int(numTotalOverallLength)):
	# Byte flag
	byteFlag = struct.unpack('B',ReadBytes(fd,1))
	#Bytes of Field Name
	bytesOfFieldName = struct.unpack('30s 2B 62s 2B 62s 2B 4s 2B 6s 2B 6s 2B',ReadBytes(fd,numTotalOverallLength))

	tuplaDados.append(bytesOfFieldName)
	metaDado0.append(tuplaDados[y][0].strip())
	metaDado1.append(tuplaDados[y][3].strip())
	metaDado2.append(tuplaDados[y][6].strip())
	metaDado3.append(tuplaDados[y][9].strip())
	metaDado4.append(tuplaDados[y][12].strip())
	metaDado5.append(tuplaDados[y][15].strip())
	tuplaByteFlag.append(byteFlag[0])


fd.close()

# Adicionando todos os campos metadado(x) no dicionario
for i in range(numNumberOfFields):
	dicionario[tuplaMetaDados[i]] = locals()['metaDado%d'%i]
dicionario["byteFlag"] = tuplaByteFlag




#-------------

print "MetaDados :",tuplaMetaDados
print '-'*21
print '\n'
print "Data: ",dicionario
print '\n'
print "magic Cookie Value : ",magicCookieValue
print "num Total Overall Length :",numTotalOverallLength
print "num Number Of Fields :",numNumberOfFields



