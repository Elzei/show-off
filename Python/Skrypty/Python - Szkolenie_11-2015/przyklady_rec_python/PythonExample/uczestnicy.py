class Uczestnik(object):
	def __init__(self, imie = '', nazwisko = ''):
		self._imie = imie
		self._nazwisko = nazwisko
	def przedstawienie(self):
		print "Witam, nazywam sie %s %s" % (self._imie, self._nazwisko),

class Sluchacz(Uczestnik):
	def przedstawienie(self):
		super(Sluchacz, self).przedstawienie()
		print "i jestem sluchaczem na szkoleniu."

class Instruktor(Uczestnik):
	def przedstawienie(self):
		super(Instruktor, self).przedstawienie()
		print "i jestem instruktorem na szkoleniu."

if __name__ == '__main__':
	s1 = Sluchacz("Adam", "Makowiec")
	s2 = Sluchacz("Maciek", "Kulka")
	in1 = Instruktor("Zenon", "Igrekowski")
	for i in (s1, s2, in1):
		i.przedstawienie()
