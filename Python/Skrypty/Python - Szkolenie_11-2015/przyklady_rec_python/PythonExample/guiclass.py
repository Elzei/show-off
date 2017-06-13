from Tkinter import *
import sys

class Witaj(object):
	def __init__(self):
		self._msg = u'Witaj'
		self._imie = u'Adamie'
	def __call__(self):
		print self._msg, self._imie
		import sys; sys.exit()

myButton = Button(Tk(), text=u'Przywitaj', command=sys.exit)
myButton.pack()
myButton.mainloop()
