#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#Dekorator

print("Before decorator definition.")
def decorator(function):
	"""Decorator"""
	print("Before decoration.")
	def wrapper(*args, **kwargs):
		"""Wrapper"""
		print("In wrapper.")
		answer = function(*args, **kwargs)
		print("After wrapper.")
		return answer
	print("After decoration.")
	return wrapper
print("After decorator definition.")

#Przez uzycie @ wymusza sie aby dekorator wykonal swoj kod
@decorator #syntactic sugar
def calculate(a,b,c):
	return ((a*2) + (b*3) + c)

if __name__ == '__main__':
	#f = decorator(calculate)
	#f(2,3,4)
	calculate(2,3,4)