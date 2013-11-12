import struct
import pdb


print '\n'

fd = open('./db-2x1.db','rb')

def ReadBytes(fd, noBytes):
 data = fd.read(noBytes)
 return data

magicCookieValue = struct.unpack('4B',ReadBytes(fd,4))

#Total Overall Length
totalOverallLength = struct.unpack('4B',ReadBytes(fd,4))
numTotalOverallLength = int(totalOverallLength[3])

# Number of Fields
numberOfFields = struct.unpack('2B',ReadBytes(fd,2))
numNumberOfFields = int(numberOfFields[1])

tupla = []
pdb.set_trace()

for x in range(0, numNumberOfFields):

	# #Bytes of Field Name
	bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
	numBytesOfFieldName = int(bytesOfFieldName[1])

	#Nome do Campo
	fieldName = struct.unpack(str(numBytesOfFieldName)+'s',ReadBytes(fd,numBytesOfFieldName))
	strFieldName = fieldName[0]

	# End of Repeating Block
	endOfRepeatingBlock = struct.unpack('2B',ReadBytes(fd,2))
	numEndOfRepeatingBlock = int(endOfRepeatingBlock[1])

	# print totalOverallLength
	print "Field Length: ",numBytesOfFieldName
	print "Field Name:",strFieldName
	print "end of Repeating Block:",numEndOfRepeatingBlock
	print '-'*20
	tupla.append(strFieldName)

print tupla
print '\n'
print '-'*21


tupla2 =[]
for y in range(0,3):
# for y in range(0,numTotalOverallLength - numNumberOfFields):
	
	# #Bytes of Field Name
	bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
	numBytesOfFieldName = int(bytesOfFieldName[1])

	#Nome do Campo
	fieldName = struct.unpack('32s',ReadBytes(fd,32))
	strFieldName = fieldName[0]

	# End of Repeating Block
	endOfRepeatingBlock = struct.unpack('2B',ReadBytes(fd,2))
	numEndOfRepeatingBlock = int(endOfRepeatingBlock[1])


	# print totalOverallLength
	print "Field Length: ",numBytesOfFieldName
	print "Field Name:",strFieldName
	print "end of Repeating Block:",numEndOfRepeatingBlock
	print '-'*20
	tupla2.append(strFieldName)

print tupla2


print '\n'
print "magic Cookie Value : ",magicCookieValue
print "num Total Overall Length :",numTotalOverallLength
print "num Number Of Fields :",numNumberOfFields



