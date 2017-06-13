#!/usr/bin/python
# -*- coding: utf-8 -*-
def slownie(liczba):
	"""Zmienia liczbe na nazwy"""
	liczby = { 0: "zero",
		   1: "jeden",
		   2: "dwa", 
		   3: "trzy",
		   4: "cztery",
		   5: "pięć",
		   6: "sześć",
		   7: "siedem",
		   8: "osiem",
		   9: "dziewięć",
		   10: "dziesięć",
		   11: "jedenaście",
		   12: "dwanaście",
		   13: "trzynaście",
		   14: "czternaście",
		   15: "piętnaście",
		   16: "szesnaście",
		   17: "siedemnaście",
		   18: "osiemnaście",
		   19: "dziewiętnaście",
		   20: "dwadzieścia",
		   30: "trzydzieści",
		   40: "czterdzieści",
		   50: "pięćdziesiąt",
		   60: "sześćdziesiąt",
		   70: "siedemdziesiąt",
		   80: "osiemdziesiąt",
		   90: "dziewięćdziesiąt",
		   100: "sto",
		   200: "dwieście",
		   300: "trzysta",
		   400: "czterysta",
		   500: "pięćset",
		   600: "sześćset",
		   700: "siedemset",
		   800: "osiemset",
		   900: "dziewięćset",
		   1000: "tysiąc"
		}

	assert liczba < 1001 and liczba >= 0

	if liczba < 20:
		return liczby[liczba]
	elif (liczba % 100) == 0:
		return liczby[((liczba / 100) * 100)]
	elif (liczba % 10) == 0:
		return liczby[liczba] + " " + liczby[liczba % 10]
	elif (liczba > 100) and (liczba % 10 > 0):
		return liczby[(liczba / 100) * 100] + " " + slownie(liczba % 100)
	elif liczba == 1000:
		return liczby[liczba]
	else:
		return "poza zakresem"


testy = [ 0, 3, 5, 12, 25, 77, 98, 100, 234 ]

for i in testy:
	slowa = slownie(i)
	print "liczba %d to: %s" % \
		( i , slownie(i))
