from Tkinter import *

radioButton = ( 'ja', 'ty', 'on, ona, ono', 'my', 'wy', 'oni' )

class MyRadioButton(Frame):
	def __init__(self, parent=None, **args):
		Frame.__init__(self, parent, args)
		self.pack()
		Label(self, text='Demo przycikow radiobutton').pack(side=TOP)
		self.wartosci = StringVar()
		for wartosc in radioButton:
			Radiobutton(self, text=wartosc,
				variable=self.wartosci,
				command=(lambda: 0),
				value=wartosc).pack(side=LEFT)
		self.wartosci.set(radioButton[0])
		Button(self, text='Stan', command=self.raport).pack(fill=X)
	def raport(self):
		print self.wartosci.get(),
		print

if __name__ == '__main__': MyRadioButton().mainloop()
