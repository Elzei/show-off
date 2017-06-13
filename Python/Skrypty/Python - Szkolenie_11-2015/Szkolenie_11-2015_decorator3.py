#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#Dekorator
import functools

def decorator(function):
	"""Decorator"""
	#Eleganckie rozwiazanie problemu name i doc i przebijania sie ich od wrappera a nie funkcji opakowanej
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		"""Wrapper"""
		answer = function(*args, **kwargs)
		return answer
	#Toporne rozwiazanie problemu name i doc i przebijania sie ich od wrappera a nie funkcji opakowanej
	#wrapper.__name__ = function.__name__
	#wrapper.__doc__ = function.__doc__
	return wrapper

@decorator #syntactic sugar
def calculate(a,b,c):
	"""Calculate doc..."""
	return ((a*2) + (b*3) + c)

if __name__ == '__main__':
	calculate(2,3,4)
	print(calculate.__doc__)
	print(calculate.__name__)