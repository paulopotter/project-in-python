# 'db-2x1.db'
#Tutorial (base de estudos tirado de: http://www.ibm.com/developerworks/br/library/l-parse-memory-dumps/)
import sys 
import struct

fd = open('./db-2x1.db','rb')

def ReadBytes(fd, noBytes):
 data = fd.read(noBytes)
 return data

magicCookieValue = struct.unpack('4B',ReadBytes(fd,4))

totalOverallLength = struct.unpack('4B',ReadBytes(fd,4))
totalOverallLength = totalOverallLength[3]

numberOfFields = struct.unpack('2B',ReadBytes(fd,2))
numberOfFields = numberOfFields[1]

print magicCookieValue
print totalOverallLength
print numberOfFields


# for element in range (0,10):
# #loop 18 since we know the file size and
# #the record length: 1024/18 = 56 records
# 	buffer = ReadBytes('./db-2x1.db',fd, 11)
# 	sourceAddress = struct.unpack_from('6s', buffer,0),struct.unpack_from('6s', buffer,1),struct.unpack_from('2B', buffer,2),struct.unpack_from('2B', buffer,3)
# 	print "sourceAddress = " , sourceAddress
# 	print '-'* 10
# 	print struct.calcsize('2h')
# 	print '-'* 10