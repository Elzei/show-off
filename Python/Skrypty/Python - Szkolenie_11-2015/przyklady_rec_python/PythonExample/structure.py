from struct import pack, unpack, calcsize

dane = open('dane.dat', 'w')

toWrite = pack('c5shhl', 'w', 'ala  ',
	2, 4, 12)
dane.write(toWrite)
dane.close()

dane = open('dane.dat', 'r')
toRead = unpack('c5shhl', dane.read())
print toRead

