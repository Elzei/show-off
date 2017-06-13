import shelve

class People(object):
    """Klasa do odlozenia na polke."""
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def __str__(self):
        return "%s %s" % (self.imie, self.nazwisko)

p1 = People('Adam', 'Zazol')
p2 = People('Zbigniew', 'Kuczko')

print "Przed odkladaniem shelve: %s" % p1
print "Przed odkladaniem shelve: %s" % p2

d = shelve.open("dane_shelve")  # nazwa pliku bez przyrostkow
d['pierwszy'] = p1
d['drugi'] = p2
d.sync()        # jest: sync, keys, has_key. Prawie jak dict :)
d.close()                       # to chyba zrozumiale

del d, p1, p2                   # dla niedowiarkow 

d = shelve.open("dane_shelve")
print "Po odkladaniu shelve: %s" % d['pierwszy']
print "Po odkladaniu shelve: %s" % d['drugi']

d.close()                       # dobre maniery mowia o zamykaniu...
