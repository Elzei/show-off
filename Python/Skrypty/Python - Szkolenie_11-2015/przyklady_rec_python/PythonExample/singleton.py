class Singleton(object):
	def __new__(self):
		if not '_instance' in self.__dict__:
			self._instance = object.__new__(self)
		return self._instance

if __name__ == '__main__':
	o1 = Singleton()
	o2 = Singleton()
	o3 = Singleton()
	print o1, o2, o3

