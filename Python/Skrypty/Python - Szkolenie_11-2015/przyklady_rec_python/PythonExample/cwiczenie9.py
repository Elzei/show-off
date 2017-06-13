#!/usr/bin/env python
# -*- coding: utf-8 -*-
from questions import questions
from Tkinter import *

"""
for i in questions:
	print "treÄ‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ˘â‚¬ĹľÄ‚ËĂ˘â€šÂ¬Ă‚Â¦Ä‚â€žĂ˘â‚¬ĹˇÄ‚â€ąĂ‚ÂĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬ÄąË‡Ä‚â€šĂ‚Â¬Ä‚â€žĂ„â€¦Ă„Ä…ÄąĹşĂ„â€šĂ˘â‚¬ĹľÄ‚ËĂ˘â€šÂ¬ÄąË‡Ă„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ă„Ä…Ă„ÄľÄ‚â€žĂ˘â‚¬ĹˇÄ‚â€ąĂ‚ÂĂ„â€šĂ‹ÂÄ‚ËĂ˘â€šÂ¬ÄąË‡Ä‚â€šĂ‚Â¬Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ:"
	print i[0]
	print "typ:"
	print i[1]
	print "odpowiedzi:"
	print i[2:-1]
	print "poprawna:"
	print i[-1]
"""

class MyWindow(Frame):
	def __init__(self, parent=None, **config):
		Frame.__init__(self, parent, config)
		self.config(width=640, height=480, relief=RIDGE)
		Label(self, text="Pytanie:").pack()
		self.questionMessage = Message(self, text=u"Treść pytania").pack()
		self.nextButton = Button(self, text=u"Następne").pack()
		self.prevButton = Button(self, text=u"Poprzednie").pack()
		self.pack()

if __name__ == '__main__':
	mw = MyWindow()
	mw.mainloop()
