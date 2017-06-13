#!/usr/bin/python

def introspection(obj):
	names = dir(obj)
	for i in names:
		print i, type(obj.i)

introspection(12)
