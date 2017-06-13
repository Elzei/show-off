#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def piramida(size):
    for i in xrange(1, size + 1, 2):
        print " " * ((size - i) / 2) + "*" * i

def ramka(napis):
    belka = "*" * (len(napis) + 4)
    puste = "* " + " " * len(napis) + " *"
    print belka
    print puste
    print "* " + napis + " *"
    print puste
    print belka

def ascii_tabela():
    for i in xrange(32, 127):
        #print "%d : %c" % (i, chr(i))
        print i, ":", chr(i) 

def numerologia(napis):
    # W stylu C :-)
    """
    sum = 0
    for i in napis:
        sum += ord(i)
    return sum
    """
    # Bardziej w stylu Python :-)
    return reduce(lambda x, y: ord(x) + ord(y), napis)
    

if __name__ == '__main__':
    piramida(7)
    ramka("Ala ma kota i chomika")
    ascii_tabela()
    print "Z napisu: |%s| suma to: %i" % ("  ", numerologia("  "))
