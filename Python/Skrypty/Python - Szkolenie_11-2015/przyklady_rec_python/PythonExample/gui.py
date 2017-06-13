from Tkinter import *
import sys

class Witacz(object):
	def __init__(self, name = u'Adam', msg = u'Witaj'):
		self._name = name
		self._msg = msg
	def __call__(self):
		print self._msg, self._name
		sys.exit()

myWitacz = Witacz('Franek', 'Spadaj')
myButton = Button(None, text=u'Przycisk', command=myWitacz)

myButton.pack()
myButton.mainloop()
