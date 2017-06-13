# -*- encoding: utf-8 -*-
import readline
import rlcompleter
import atexit
import os
# Uzupe�nianie przez tab
readline.parse_and_bind('tab: complete')
# Historia polece�
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
	readline.read_history_file(histfile)
except IOError:
	pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter
