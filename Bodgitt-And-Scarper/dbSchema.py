import struct
import pdb


print '\n'

fd = open('./db-2x1.db','rb')

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

tupla = []
# pdb.set_trace()

# MetaDado
for x in range(0, numNumberOfFields):

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
	tupla.append(strFieldName)
	# tupla.append(numEndOfRepeatingBlock)

print "MetaDados :",tupla
print '-'*21
tupla2 =[]
dicionario = {}
estrutura1 = []
estrutura2 = []
estrutura3 = []
estrutura4 = []
estrutura5 = []
estrutura6 = []
# Dados
for y in range(0,3):
# for y in range(0,numTotalOverallLength - numNumberOfFields):
	
	#Bytes of Field Name
	bytesOfFieldName = struct.unpack('B 30s 2B 62s 2B 62s 2B 4s 2B 6s 2B 6s B',ReadBytes(fd,numTotalOverallLength))
	byteFlag = struct.unpack('B',ReadBytes(fd,1))

	# print "Field Length: ",bytesOfFieldName
	# print '-'*20
	tupla2.append(bytesOfFieldName)
	estrutura1.append(tupla2[y][1].strip())
	estrutura2.append(tupla2[y][4].strip())
	estrutura3.append(tupla2[y][7].strip())
	estrutura4.append(tupla2[y][10].strip())
	estrutura5.append(tupla2[y][13].strip())
	estrutura6.append(tupla2[y][16].strip())

# print tupla2 
dicionario[tupla[0]] = estrutura1
dicionario[tupla[1]] = estrutura2
dicionario[tupla[2]] = estrutura3
dicionario[tupla[3]] = estrutura4
dicionario[tupla[4]] = estrutura5
dicionario[tupla[5]] = estrutura6


print '\n'
print "Data: ",dicionario

print '\n'
print "magic Cookie Value : ",magicCookieValue
print "num Total Overall Length :",numTotalOverallLength
print "num Number Of Fields :",numNumberOfFields



