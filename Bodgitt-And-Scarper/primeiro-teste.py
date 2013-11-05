



# 'db-2x1.db'
class leituraArquivo:
	

	def lerArquivo(self, arq , noBytes):
		arquivoDB = open(arq,'rb')
		arquivo = arquivoDB.read(noBytes)
		# arquivoDB.close()
		return arquivoDB
#--------------

# import sys
import struct
import testado

fd = open('./db-2x1.db','rb')

def ReadBytes(self, fd, noBytes):
 '''
 Read file and return the number of bytes as specified
 '''
 data = fd.read(noBytes)
 return data

# print len(fd.read())
# for i in range(0,10):
# 	buffer = ReadBytes('./db-2x1.db',fd, 8)
# 	print buffer
# 	print '-'*20

for element in range (0,10):
#loop 18 since we know the file size and
#the record length: 1024/18 = 56 records
	buffer = ReadBytes('./db-2x1.db',fd, 11)
	sourceAddress = struct.unpack_from('6s', buffer,0),struct.unpack_from('6s', buffer,1),struct.unpack_from('2B', buffer,2),struct.unpack_from('2B', buffer,3)
	print "sourceAddress = " , sourceAddress
	print '-'* 10
	print struct.calcsize('2h')
	print '-'* 10
	"""