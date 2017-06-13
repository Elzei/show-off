#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#0.rozszerzenie turtle biblioteki tkinter
"""
import turtle
def turtlesy():
    colors=["red","purple","blue","green","yellow","orange"]

    tur =turtle.Pen()
    turtle.bgcolor("black")

    turtle.speed("fastest")

    for x in range(360):
        #tur.pencolor("#fbfbfb")
        tur.pencolor(colors[x%len(colors)])
        tur.width(x//100 + 1)
        tur.forward(x)
        tur.left(59)
"""
#0.przeliczanie stopni celsjusza na Fahrenheita


#należy zrobić jeszcze tak by niezaleznie czy wprowadze farenhaita czy celsjusza to mi ładnie to przeliczy



from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(celsius.get())
        print(value)
        fahrenheit.set((value*1.8)+32)
    except ValueError as e:
        print(e.__format__())

root = Tk()
root.title(u"Swap from \260C to \260F")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

celsius = StringVar()
fahrenheit = StringVar()

celsius_entry = ttk.Entry(mainframe, width=7, textvariable=celsius)
celsius_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=fahrenheit).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Degree in Celsius: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="\260C").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Degree in Fahrenheit : ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="\260F").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

celsius_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
