import sys
from Tkinter import Toplevel, Button, Label
windows1 = Toplevel()
windows2 = Toplevel()
Button(windows1, text=u'Okno 1',
	command=sys.exit).pack()
Button(windows2, text=u'Okno 2',
	command=sys.exit).pack()
Label(text=u'Wyskakujace').pack()
	# domyslnie dla okna "root"
windows1.mainloop() # wtarczy mainloop()
	# dla ktoregokolwiek z okien
