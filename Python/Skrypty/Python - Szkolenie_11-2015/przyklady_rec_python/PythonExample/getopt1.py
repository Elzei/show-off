#!/usr/bin/python3

import getopt
import sys

opts, arg = getopt.getopt(sys.argv[1:], 'ao:v')

print("Opcje")
for opt in opts:
	print(opt)

print("Arg")
for a in arg:
	print(a)
