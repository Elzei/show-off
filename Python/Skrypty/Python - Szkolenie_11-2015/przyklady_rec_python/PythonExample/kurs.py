from uczestnicy import Uczestnik, Sluchacz, Instruktor
class Sala(object):
	def __init__(self, pojemnosc = 3):
		self._pojemnosc = pojemnosc 
		self._obsada = {}
	def dodajStanowisko(self, komputer, uczestnik):
		if (self._pojemnosc - 1) >= 0:
			self._obsada[komputer] = uczestnik
			self._pojemnosc = self._pojemnosc - 1
			print "Pozostalo %d miejsc na sali." % self._pojemnosc
		else:
			print "Nie ma wolnych miejsc na sali."
	def raport(self):
		for i in self._obsada.keys():
			print "K: %s -> %s" % (i, self._obsada[i]._imie),
			print "%s" % (self._obsada[i]._nazwisko)

class Komputer(object): pass
	
if __name__ == '__main__':
	s1 = Sluchacz("Marian", "Janosik")
	s2 = Sluchacz("Tomasz", "Pac")
	s3 = Sluchacz("Adam", "Ferenc")
	s4 = Sluchacz("Grzegorz", "Tracz")
	k1, k2, k3, k4 = Komputer(), Komputer(), Komputer(), Komputer()
	sala = Sala()
	for i in ((k1, s1), (k2, s2), (k3, s3), (k4, s4)):
		sala.dodajStanowisko(i[0], i[1])
	sala.raport()
