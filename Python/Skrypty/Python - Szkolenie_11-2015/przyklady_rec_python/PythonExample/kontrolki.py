from Tkinter import Tk, Button, Label
import sys

widgets = {
	'Okno 1': [ { 'side': 'top'}, {'side': 'left'}, {'side': 'right'} ],
	'Okno 2': [ { 'side': 'left'}, {'side': 'top'}, {'side': 'right'} ],
	'Okno 3': [ { 'side': 'left', 'fill': 'y'}, {'side': 'top'},
		{'side': 'right', 'expand': 'yes', 'fill': 'x' } ],
	'Okno 4': [ { 'side': 'left', 'anchor': 'n'}, {'side': 'top'},
		{ 'side': 'right'}]
}

for i in widgets.keys():
	win = Tk()
	win.title(i)
	Button(win, text='Przycisk', command=sys.exit).pack(widgets[i][0])
	Label(win, text='Jakas bardzo dluga nazwa...').pack(widgets[i][1])
	Button(win, text='Wyjscie', command=sys.exit).pack(widgets[i][2])

win.mainloop()

