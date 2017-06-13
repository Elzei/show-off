class WrapObject(object):
	def __init__(self, obj):
		self._obj = obj
	def __getattr__(self, attrname):
		print 'Dostep:', attrname
		return getattr(self._obj, attrname)	
	def __getitem__(self, keyname):
		print 'Dostep do klucza:', keyname
		return self._obj[keyname]

if __name__ == '__main__':
	x = WrapObject({'a': 1, 'b': 2, 'c': 3})
	print x.keys()
	print x.values()
	print x['b']
