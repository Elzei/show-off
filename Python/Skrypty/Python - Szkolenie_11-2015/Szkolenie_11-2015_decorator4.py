#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#Dekoratoryt
import functools

def decorator(function):
	"""Decorator"""
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		answer = function(*args, **kwargs)
		if answer > 10:
			answer=10
		elif answer<-10:
			answer=-10
		return answer
	return wrapper

@decorator #syntactic sugar
def calculate(a,b,c):
	"""Calculate"""
	return ((a*2) + (b*3) + c)

if __name__ == '__main__':
	print(calculate(2,3,4))
