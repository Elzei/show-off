#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#0
def get_number():
    while True:
        print("Podaj liczbę:")
        try:
            value = input() #To może polecieć wyjątek KeyboardInterrput
            liczba = value
        except ValueError:
            print("Miała być LICZBA!")
        except KeyboardInterrupt:
            print("Nie dziwne klawisze, a LICZBA!")
        finally:
            print("Uff, koniec.")
"""
#1,2,3
class MyException(Exception):
    def __init__(self, args, message):
        self._args = args
        self._message = message
    def __str__(self):
        return (self._args, self._message)

def trash():
    #raise ArithmeticError("!")
    #raise ZeroDivisionError("!")
    raise MyException(1, "Ojojoj!")\

def safeException(function, *args, **kwarq):
    apply()

def f():
    try:
        trash()
    except ArithmeticError:
        print("Przechwycono blad arytmetyczny!")
    except MyException as e:
        print(e._args,":",e._message)
    finally:
        print("Funkcja zostala wykonana.")

f()
"""