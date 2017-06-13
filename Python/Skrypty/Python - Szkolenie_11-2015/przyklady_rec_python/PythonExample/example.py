#!/usr/bin/python
# -*- encoding: utf-8 -*-
import math

def dzielnik(liczba):
	"""
	Zwraca listę z dzielnikami liczby przekazanej jako argument,
	bez wartości samej liczby. W przypadku liczby pierwszej, zwraca 0.
	"""
	# Sprawdzanie dzielników
	for i in range(2, liczba):
		if (liczba % i) == 0:
			yield i
		if i == (liczba - 1):
			yield 0

for i in range(2, 70):
	print "%s:" % i, 
	for j in dzielnik(i):
		print j,
	print ""
