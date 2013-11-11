# 'db-2x1.db'
#Tutorial (base de estudos tirado de: http://www.ibm.com/developerworks/br/library/l-parse-memory-dumps/)
import sys 
import struct

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

# #Bytes of Field Name
bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
numBytesOfFieldName = int(bytesOfFieldName[1])

# #Nome do Campo
fieldName = struct.unpack(str(numBytesOfFieldName)+'s',ReadBytes(fd,numBytesOfFieldName))
strFieldName = fieldName[0]

# End of Repeating Block
endOfRepeatingBlock = struct.unpack('2B',ReadBytes(fd,2))
numEndOfRepeatingBlock = int(endOfRepeatingBlock[1])


print totalOverallLength
print numberOfFields
print bytesOfFieldName
print fieldName
print endOfRepeatingBlock


# for x in range(0, 5):
# 	for y in range(0, numNumberOfFields):

# 		# #Bytes of Field Name
# 		bytesOfFieldName = struct.unpack('2B',ReadBytes(fd,2))
# 		numBytesOfFieldName = int(bytesOfFieldName[1])

# 		# #Nome do Campo
# 		fieldName = struct.unpack(str(numBytesOfFieldName)+'s',ReadBytes(fd,numBytesOfFieldName))
# 		# strFieldName = fieldName[0]
# 		print fieldName

# 		# print "Bytes of Field Name [%i]\n Field Name[%s]"%(bytesOfFieldName[1] , fieldName[0])
# 		# print endOfRepeatingBlock



# dicionario = {}
# for i in range(0,numNumberOfFields):
# 	print i
# 	dicionario[strFieldName] = None

# print dicionario