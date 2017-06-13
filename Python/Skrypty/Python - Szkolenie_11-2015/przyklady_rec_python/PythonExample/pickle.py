import cPickle

class People(object):
    """Klasa do piklowania."""
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def __str__(self):
        return "%s %s" % (self.imie, self.nazwisko)

p1 = People('Adam', 'Zazol')

print "Przed piklowaniem: %s" % p1

f = open("dane.dat", "wb")      # z trybem binarnym dla windows
p = cPickle.Pickler(f, 2)    # "piklowanie" w trybie binarnym
p.dump(p1)                      # "zapiklowanie" do pliku
f.close()                       # zamkniecie pliku

del p1                          # to dla niedowiarkow...

f = open("dane.dat", "rb")      # znow uklon w strone windows
u = cPickle.Unpickler(f)        # sam rozpozna ze tryb binarny
p1 = u.load()                   # tu ladujemy obiekt

print "Po odtworzeniu z pikla: %s" % p1

f.close()                       # dobre maniery mowia o zamykaniu...
