#!/usr/bin/python3

import re

pattern = 'c.*s'
text = 'Oto jakies cos i jeszcze dalej...'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Znaleziono "%s" w "%s" od indeksu "%d" do indeksu "%d" ("%s")' % \
	(match.re.pattern, match.string, s, e, text[s:e]))
