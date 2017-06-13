#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#0
"""

"""

class Board(object):
    def __init__(self):
        #self._figures = [[0 for col in range(8)] for row in range(0, 8)]
        self._figures=[None]*8
        for x in range(8):
	        self._figures[x]=[None]*8


        for i in range(0, 8):
            self._figures[0][i] = Figure("O")
            self._figures[1][i] = Figure("O")
            self._figures[6][i] = Figure("X")
            self._figures[7][i] = Figure("X")

    def show(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if isinstance(self._figures, Figure):
                    print(self._figures._colour, end="")
                else:
                    print(" ", end="")
            print("")

class Figure(Board):
    def __init__(self, color):
        self._color = color
        self._damka = False
    def move(self):
        pass

class Player(object):
        def __init__(self, board,name):
            self._name = name
            self._board = board
            self._board.show()
            print("Gracz utworzony")
        def show(self):
            self._board.show()
        def move(self, a, b):
            self._board.move(a, b)
        def beat(self):
            self._board.beat(a, b)

if __name__ == "__main__":
    board1 = Board()
    player1 = Player("Zenek", board1)

"""
#canopy
#0.elementy modululu sys
#z poziomu konsloli zamieniam
class MyClass():
    def __repr__(self):
        return "REC >>"

import sys
sys.ps1 = MyClass()
"""
#0.parser - z fajnym wykorzystaniem takiego czegos jak Counter()

def parser_file(file_name):
    line_list = []
    for line in open(file_name, "rb"):
        line_list.append(line)
    return line_list

from collections import Counter
def word_counter(line_list):
    c = Counter()
    for line in line_list:
        for word in line.split():
            c[word] += 1
    return c

if __name__ == "__main__":
    c = word_counter(parser_file('pan-tadeusz.txt'))
    for word, count in c.most_common(5):
        print(word, ":",count)
