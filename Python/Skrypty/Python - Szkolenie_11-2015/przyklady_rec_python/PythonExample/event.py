from Tkinter import *

def showPosition(event):
	print 'Pozycja x=%s, y=%s' % ( event.x, event.y)

def showEvent(eventType, ev):
	print eventType, ev

def showPosition(eventType, ev):
	print eventType, 'X= ', ev.x, 'Y=', ev.y

def showChar(eventType, ev):
	print eventType, 'Char=', ev.char

root = Tk()
myLabel = Label(root, text=u'Witam')
myLabel.pack()
myLabel.bind('<Button-1>', lambda ev : showEvent('onLeftClick', ev))
myLabel.bind('<Button-3>', lambda ev : showEvent('onRightClick', ev))
myLabel.bind('<Button-2>', lambda ev : showEvent('onMiddleClick', ev))
myLabel.bind('<Double-1>', lambda ev : showEvent('onDoubleLeftClick', ev))
myLabel.bind('<B1-Motion>', lambda ev : showPosition('onLeftDrag', ev))
myLabel.bind('<KeyPress>', lambda ev : showChar('onKeyPress', ev))
myLabel.bind('<Up>', lambda ev : showEvent('onArrowKey', ev))
myLabel.bind('<Return>', lambda ev : showEvent('onReturnClick', ev))
myLabel.focus()
root.mainloop()


