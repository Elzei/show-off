#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#Dekorator

#pierwsze podejscie
def decorate(function, *args, **kwargs):
	print("Decorator")
	print(function(*args,**kwargs))
	print("After decorator")

def calculate(a,b,c):
	return ((a*2) + (b*3) + c)

if __name__ == '__main__':
	decorate(calculate, 3, 4, 5)