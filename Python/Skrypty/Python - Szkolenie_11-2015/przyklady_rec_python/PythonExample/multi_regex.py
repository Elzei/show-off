#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

regexp = 'ab'

text = 'abrakadabra'

print('W tekście |%s|' % text)

for regex in re.findall(regexp, text):
	print('Znalazłem |%s|!' % regex)
print("-" * 72)

print('W tekście |%s|' % text)

for regex in re.finditer(regexp, text):
	print("-" * 72)
	print(text[0:regex.start()] + ">" + text[regex.start():regex.end()] + \
		"<" + text[regex.end():])
	print("-" * 72)


text = """
Jakieś długie napisy, teksty i takie tam..
bez składu sensu i jedynie dla testu.
Literki i oraz I
"""
regexp = re.compile("""


	# Bardzo rozbudowany regexp wraz z komentarzem...
	ś.*ł 		# Od literki "ś" do "ł" ,,zachłannie bardzo"



""", re.DOTALL | re.UNICODE | re.IGNORECASE | re.VERBOSE | re.MULTILINE)


for regex in re.finditer(regexp, text):
	print("-" * 72)
	print(text[0:regex.start()] + ">" + text[regex.start():regex.end()] + \
		"<" + text[regex.end():])
	print("-" * 72)

