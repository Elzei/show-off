# Klient glupiego komunikatu
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('adres.serwera.com', 12345))
tbuf = s.recv(1024)
s.close()
print "Odebrany komunikat to: %s" % tbuf
