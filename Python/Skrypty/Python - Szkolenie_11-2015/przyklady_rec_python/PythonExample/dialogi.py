from tkFileDialog   import askopenfilename
from tkColorChooser import askcolor
from tkMessageBox   import askquestion, showerror
from tkSimpleDialog import askfloat
dialogs = { 
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda: askquestion('Uwaga', 'Potwierdzasz?'),
	'Error': lambda: showerror('Blad!', 'Paskudztwo!'),
	'Input': lambda: askfloat('Podaj', 'Podaj ile zarabiasz:)')
}

from Tkinter import *

class Dialogi(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		Label(self, text='Dialogi').pack()
		for (klucz, wartosc) in dialogs.items():
			wrap = (lambda klucz=klucz: self.drukuj(klucz))
			Button(self, text=klucz, command=wrap).pack(side=TOP,
				fill=BOTH)
	def drukuj(self, klucz):
		value = dialogs[klucz]()
		print klucz, 'zwraca =>' , value, 'typu =>', type(value)

if __name__ == '__main__': Dialogi().mainloop()
