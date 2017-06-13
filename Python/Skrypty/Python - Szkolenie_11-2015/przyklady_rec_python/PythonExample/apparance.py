from Tkinter import *

root = Tk()
myFont = ('halvetica', 15, 'bold italic')
myLabel = Label(root, text=u'Oto etykieta!')
myLabel.config(bg='yellow', fg='black', font=myFont)
myLabel.config(height=5, width=30)
myLabel.pack(expand=YES, fill=BOTH)

myButton = Button(root, text=u'Oto przycisk!', padx=10, pady=10)
myButton.pack(padx=20, pady=20)
myButton.config(cursor='hand2', bd=5, relief=RAISED, bg='grey')
myButton.config(fg='white')
myButton.config(font=('helvetica', 15, 'underline italic'))

root.mainloop()
