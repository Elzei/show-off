from Tkinter import *

checkButton = ( 'ja', 'ty', 'on, ona, ono', 'my', 'wy', 'oni' )

class MyCheckButton(Frame):
	def __init__(self, parent=None, **args):
		Frame.__init__(self, parent, args)
		self.pack()
		frameButton = Frame(self)
		frameButton.pack(side=RIGHT)
		Button(frameButton, text='Stan', command=self.raport).pack(fill=X)
		Label(self, text='Demo przycikow checkbutton').pack()
		self.wartosci = []
		for wartosc in checkButton:
			a = IntVar()
			Checkbutton(self, text=wartosc, variable=a,
				command=(lambda: 0)).pack(side=LEFT)
			self.wartosci.append(a)
	def raport(self):
		for i in self.wartosci:
			print i.get(),
		print

if __name__ == '__main__': MyCheckButton().mainloop()
