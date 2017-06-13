class X(object):
	def _moja(self, arg):
		print("_moja wita: ", arg)
	def __getattr__(self, name):
		print("__getattr__ dostep do ", name)
		return self._moja
	def __getitem__(self, index):
		print("Dostep przez indeks:", index)

o = X()
print("Dostep do atrybutu cos")
o.cos
print("Dostep do funkcji cos(123)")
o.cos(123)
print("Dostep do indeksu cos[212]")
o[212]
