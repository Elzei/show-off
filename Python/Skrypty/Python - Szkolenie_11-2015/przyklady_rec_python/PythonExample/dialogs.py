from Tkinter import *
from tkMessageBox import *

def komunikaty():
	if askyesno('Podaj odpowiedz!', u'Czy wiesz co robisz?'):
		showwarning('Tak', u'Jak widze wiesz co robisz.')
	else:
		showinfo('Nie', 'Nie przejmuj sie, nie ty jeden.')

Button(text=u'Koniec', command=komunikaty).pack(fill=X)
Button(text=u'Blad',
	command=(lambda: showerror('Error', 'I to wielki'))).pack(fill=X)
mainloop()
