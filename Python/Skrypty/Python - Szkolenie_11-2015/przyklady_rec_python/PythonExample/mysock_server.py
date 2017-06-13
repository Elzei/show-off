# Serwer glupiego komunikatu
from socket import *

s = socket(AF_INET, SOCK_STREAM)    # utworzenie gniazda TCP
s.bind(('', 12345))                 # dowiazanie do portu 12345
s.listen(5)                         # oczekiwanie z kolejka max 5 klientow

while True:
    client, addr = s.accept()       # odebranie polaczenia
    print "Puk, polaczenie z", addr 
    client.send('Ale glupi komunikat')  # wyslanie
    client.close()                  # zamkniecie polaczenia
