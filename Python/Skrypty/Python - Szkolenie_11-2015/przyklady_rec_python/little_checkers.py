#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Implementacja gry w warcaby."""

class Board(object):
    """Klasa obsługująca szachownicę."""

    def __init__(self):
        """Konstruktor inicjujący szachownicę i rozstawiający piony na pozycjach wyjściowych"""
        self._fields = {}
        for i in "aceg":
            line = [None, None, None, None, None, None, None, None]
            line[0] = Pawn("black")
            line[2] = Pawn("black")
            line[6] = Pawn("white")

            self._fields[i] = line

        for i in "bdfh":
            line = [None, None, None, None, None, None, None, None]
            line[7] = Pawn("white")
            line[5] = Pawn("white")
            line[1] = Pawn("black")

            self._fields[i] = line

    def show(self):
        """Pokazuje szachownicę"""

        print "    a b c d e f g h"
        print "  +" + "-" * 17 + "+"
        for i in xrange(7, -1, -1):
            print i + 1, "|",
            for l in "abcdefgh":
                if self._fields[l][i] is None:
                    print "_",
                else:
                    print self._fields[l][i], 
            print "|", i + 1

        print "  +" + "-" * 17 + "+"
        print "    a b c d e f g h"

    def move(self, src_let, src_num, dst_let, dst_num):
        """Przesuwa lub bije pion, w przypadku niepowodzenia zwraca False"""

        # Obiekty źródła, celu
        src_obj = self._fields[src_let][src_num - 1]
        dst_obj = self._fields[dst_let][dst_num - 1]

        # Współrzędne piona do ew. bicia
        beat_let = chr((ord(src_let) + ord(dst_let)) // 2)
        beat_num = (src_num + dst_num ) // 2

        # Obiekt pionu do ew. bicia
        beat_obj = self._fields[beat_let][beat_num - 1]

        # W źródle jest pion a w celu jest pusto
        if (dst_obj is None) and (src_obj is not None):
            if (abs(src_num - dst_num) == 1) and (abs(ord(src_let) - ord(dst_let)) == 1):
                # Wykonanie ruchu
                # TODO: Brak sprawdzania "ruch tylko do przodu"
                self.__move_from_to(src_obj, src_let, src_num, dst_let, dst_num)
                return True
            elif (abs(src_num - dst_num) == 2) and (abs(ord(src_let) - ord(dst_let)) == 2):
                # Współrzędne wskazują na możliwe bicie..
                # TODO: Brak sprawdzania "bicie tylko do przodu"
                # Nie ma piona do bicia lub piony o tych samych kolorach!
                if (beat_obj is None) or (beat_obj.get_color() == src_obj.get_color()):
                    return False
                else:
                    self._fields[beat_let][beat_num - 1] = None
                    self.__move_from_to(src_obj, src_let, src_num, dst_let, dst_num)
                return True
        else:
            # Problem ze źródłem lub celem
            return False

    def __move_from_to(self, src_obj, src_let, src_num, dst_let, dst_num):
        """Metoda pomocnicza przesuwania piona"""

        pawn = src_obj
        self._fields[src_let][src_num - 1] = None
        self._fields[dst_let][dst_num - 1] = pawn


class Player(object):
    """Reprezntacja gracza"""

    def __init__(self, board, name):
        """Inicjalizuje gracza, przyjmuje szachownicę oraz nazwę gracza"""
        self._board = board
        self._name = name

    def __str__(self):
        return self._name

    def move(self):
        """Przesunięcie piona na szachownicy"""

        # a7 -> b6 z błędem... 
        print "Ruch gracza z a7 -> b6 udany?: ", self._board.move('a', 7, 'b', 6)
        # b6 -> c5 bez błędu ... 
        print "Ruch gracza z b6 -> c5 udany?: ", self._board.move('b', 6, 'c', 5)
        # a5 -> b4 z błędem....
        print "Ruch gracza z a5 -> b4 udany?: ", self._board.move('a', 5, 'b', 4)
        # a3 -> b4 bez błędu...
        print "Ruch gracza z a3 -> b4 udany?: ", self._board.move('a', 3, 'b', 4)

    def beat(self):
        """Bicie piona na szachownicy"""

        # c3 -> e5 z błędem...
        print "Bicie gracza z c3 -> e5 udany?: ", self._board.move('c', 3, 'e', 5)
        # c5 -> a3 bez błędu...
        print "Bicie gracza z c5 -> a3 udany?: ", self._board.move('c', 5, 'a', 3)
        # b2 -> d4 z błędem...
        print "Bicie gracza z b2 -> d4 udany?: ", self._board.move('b', 2, 'd', 4)

    def show_board(self):
        """Prezentacja szachownicy"""

        self._board.show()

class Pawn(object):
    """Reprezentacja piona"""

    def __init__(self, color = "white", is_lady = False):
        """Inicjalizuje pion."""

        self._color = color
        self._is_lady = is_lady

    def lady_promotion(self):
        """Promocja do damy"""

        self._is_lady = True

    def is_lady(self):
        """Sprawdzenie czy dama"""

        return self._is_lady

    def get_color(self):
        """ Zwraca kolor piona"""

        return self._color

    def __str__(self):
        """Reprezentacja piona w postaci ciągu znaków"""

        if self._color == "white":
            return "o"
        elif self._color == "black":
            return "*"
        else:
            # TODO: Obsługa damy... 
            return " "

if __name__ == '__main__':
    b1 = Board()
    p1 = Player(b1, "Bill")
    b1.show()
    p1.move()
    b1.show()
    p1.beat()
    b1.show()
