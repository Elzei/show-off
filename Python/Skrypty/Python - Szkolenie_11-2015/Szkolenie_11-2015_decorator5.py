#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import functools
import time

def memoize(function):
    memo = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        #zapamiętywanie ostatniego wywołania funkcji
        if(args, str(kwargs)) in memo.keys():
            return memo[(args, str(kwargs))]
        answer = function(*args,**kwargs)
        memo[(args, str(kwargs))] = answer
        return answer
    return wrapper

@memoize
def calculate(a,b,c):
    time.sleep(2)
    return a+b+c

if __name__ == "__main__":
    print("Wow expensive...")
    print(calculate(-1,-10,-121))
    print("No expensive!")
    print(calculate(-1,-10,-121))
    print("Still expensive!")
    print(calculate(5,55,555))
    print("And expensive one more time.")
    print(calculate(5,55,555))
    print("And how about now?")
    print(calculate(-1,-10,-121))
    print("Yeah it's work!")