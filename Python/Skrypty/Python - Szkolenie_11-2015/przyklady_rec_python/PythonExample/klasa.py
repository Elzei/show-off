class Moja(object):
	def __init__(self, *t, **di):
		print("To jest tupla: ", t)
		print("To jest dict: ", di)

o = Moja(10, 100, 200, 300, zuza = 12, ania = 213)
