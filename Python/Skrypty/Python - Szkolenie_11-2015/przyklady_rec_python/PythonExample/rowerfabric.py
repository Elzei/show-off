class FabRowerow(object):
	def getRower(self, rodzaj):
		choice = { 'torowy': (1, 0),
			'trekkingowy': (12, 1),
			'turystyczny': (24, 2),
			'miejski': (4, 2)}
		return Rower(rodzaj, choice[rodzaj][0], choice[rodzaj][1])

class Rower(object):
	def __init__(self, rodzaj = '', biegi = 0, bagaznik = 0):
		self._biegi = biegi
		self._bagaznik = bagaznik
		self._rodzaj = rodzaj
	def getInfo(self):
		return "Rower: %-12s\tBiegow: %d\tIlosc bagaznikow: %d"\
			 % (self._rodzaj, self._biegi, self._bagaznik)

if __name__ == '__main__':
	fabryka = FabRowerow()
	flotaRowerow = []
	for i in ('torowy', 'trekkingowy', 'turystyczny', 'miejski'):
		flotaRowerow.append( fabryka.getRower(i) )
	for i in flotaRowerow:
		print i.getInfo()
