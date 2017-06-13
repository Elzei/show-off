#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def get_number():
    while True:
        print "Podaj liczbę:",
        try:
            value = raw_input()  # Tu może polecieć wyjątek KeyboardInterrupt
            liczba = long(value) # Tu może polecieć wyjątek ValueError jeśli konwersja się nie powiedzie
        except ValueError as e:
            print "Powiedziałem _liczba_ a nie ... jakieś .. coś!"
        except KeyboardInterrupt as e:
            print "\nNie kombinuj misiu z magicznymi klawiszami!"
        else:
            break
    return liczba

if __name__ == '__main__':
    liczba = get_number()
    print "Wprowadzono liczbę: %d" % liczba
