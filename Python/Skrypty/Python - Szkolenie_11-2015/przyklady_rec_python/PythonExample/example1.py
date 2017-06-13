class Klasa1(object):
	def __init__(self, repr_str = "REPR" , str_str = "STR"):
		self._repr_str = repr_str
		self._str_str = str_str
	def __repr__(self):
		return self._repr_str
	def __str__(self):
		return self._str_str
	def __del__(self):
		print("Ojoj DeSCTRUCTION\n")

