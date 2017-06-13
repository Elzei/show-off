class PointXY(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y
	def __call__(self):
		return self._x, self._y

class PointRGB(object):
	def __init__(self, r, g, b):
		self._r = r
		self._g = g
		self._b = b
	def __call__(self):
		return self._r, self._g, self._b

class Proxy(object):
	def __init__(self, orginal):
		self._orginal = orginal
	def __getattr__(self, name):
		print "Dostep do atrybutu %s" % (name)
		return getattr(self._orginal, name)
	def __call__(self, *arg, **args):
		print "Dostep do wywolania:", arg, args
		return self._orginal(*arg, **args)

if __name__ == '__main__':
	p1 = Proxy(PointXY(10, 12))
	r1 = Proxy(PointRGB(12,13,14))
	print p1(), "\n", r1()
