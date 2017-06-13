#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

lista = [0,1,2,3,4]
#print(list[1])
#1.1
#print(list[10]) #out of range

#1.2
#print(list[4:1]) #[]

#1.3
"""
lista[2:4]="x"
print(lista[:]) #zastąpi 2 i 3 znakiem x
"""

#2
"""
lista[1]=0
print(lista)
"""

#3
"""
lista.append(5)
print(lista[:])
"""

#4
"""
mydictionary = {"a":1, "b":2, "c":3}
lista.append(mydictionary)
print(lista[5]["a"])
"""

#5

napis="rower"
"""
#1 rozwiązanie
list_napis = list(napis)
list_napis[2]="b"
list_napis.append("t")
napis_rozwiazanie = "".join(list_napis)
print(napis_rozwiazanie)
#2 rozwiązanie
napis_rozwiazanie2 = napis[:2] + "b" + napis[3:] + "t"
print(napis_rozwiazanie2)
"""
#6
"""
faktura = {"position1":(["stuff1",1],["stuff2",2]), "position2":(["stuff1",1],["stuff2",1])}
print(faktura["position1"][1])
"""

#7
"""
szachy = {"szachownica":[("a", 1), ("b", 2)], "gra":{"pionbialy1":["a",1, "zbity"], "lauferbialy1":["b",2,"w grze"]}}
"""