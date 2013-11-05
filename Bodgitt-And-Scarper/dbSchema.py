# 'db-2x1.db'
import sys 
#Tutorial (base de estudos tirado de: http://www.ibm.com/developerworks/br/library/l-parse-memory-dumps/)

import struct
import testado


# Le o arquivo
def ReadBytes( arquivo, noBytes):
	fd = open(arquivo,'rb')
	data = fd.read(noBytes)
	return data





for element in range (0,19):
	buffer = ReadBytes('./db-2x1.db',20)

	sourceAddress = struct.unpack_from('B', buffer,element),struct.unpack_from('s', buffer,element+1)
	print '-'*element
	print "sourceAddress = " , sourceAddress
	
	print '%s%s'%(sourceAddress[0][0],sourceAddress[1][0])

