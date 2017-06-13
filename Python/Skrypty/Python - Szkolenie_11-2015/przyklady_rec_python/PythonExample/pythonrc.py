# -*- encoding: utf-8 -*-
import readline
import rlcompleter
import atexit
import os
# Uzupe³nianie przez tab
readline.parse_and_bind('tab: complete')
# Historia poleceñ
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
	readline.read_history_file(histfile)
except IOError:
	pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter
