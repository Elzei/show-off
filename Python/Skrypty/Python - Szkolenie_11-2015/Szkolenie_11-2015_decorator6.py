#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#Dekoratoryt

import functools

def bounduary(min_val, max_val):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            answer = function(*args, **kwargs)
            if answer < min_val:
                return min_val
            elif answer > max_val:
                return max_val
            return answer
        return wrapper
    return decorator

@bounduary (-10,10)
def calculate(a,b,c):
	return ((a*2) + (b*3) + c)

if __name__ == '__main__':
	print(calculate(2,3,4))
