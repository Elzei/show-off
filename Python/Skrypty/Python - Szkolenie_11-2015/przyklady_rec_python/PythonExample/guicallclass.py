from Tkinter import *

class Witaj(object):
	def __init__(self, msg=u'Witaj', imie=u'nieznajomy'):
		self._msg = msg
		self._imie = imie
	def quit(self):
		import sys; sys.exit()

Witaj()
mainloop()
