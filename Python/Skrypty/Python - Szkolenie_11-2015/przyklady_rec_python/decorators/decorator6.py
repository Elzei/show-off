#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import functools

def bonduary(min_val, max_val):
    def decorator(function):
        def wrapper(*args, **kwargs):
            answer = function(*args, **kwargs)
            if answer < min_val:
                return min_val
            elif answer > max_val:
                return max_val
            return answer
        return wrapper
    return decorator

@bonduary(-10, 10)
def calculate(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print calculate(-1, -10 , -121)
