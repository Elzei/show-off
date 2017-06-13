from Tkinter import *
class MySlider(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		Label(self, text='Skalowanie').pack()
		self.wartosc = IntVar()
		Scale(self, label='Jaka wartosc?',
			command=self.onMove, variable=self.wartosc,
			from_=0, to=20, length=150, tickinterval=5,
			showvalue=YES, orient='horizontal',
			resolution=1).pack()
	def onMove(self, wartosc):
		print 'po przesunieciu', wartosc

if __name__ == '__main__': MySlider().mainloop()
