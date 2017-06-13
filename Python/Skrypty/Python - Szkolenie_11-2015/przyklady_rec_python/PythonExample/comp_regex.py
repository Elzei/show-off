#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

regexpy = [ re.compile(x) for x in [ 'Asia', 'Zosia', 'Tosia?' ]]
text = 'Asia powiedziała że Zosia zabrała Tosi jakieś zabawki.'

print("-" * 72)
print("Oto tekst do dopasowania:\n%s" % text)
print("-" * 72)

for regex in regexpy:
	print('Szukanie "%s" -> ' % regex.pattern, end='')
	
	if regex.search(text):
		print('Znalazłem!');
	else:
		print('Nie ma :(');
