#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import functools
import time

def memoize(max_calls):
    memo = {}
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            #zapamiętywanie ostatniego wywołania funkcji
            if max_calls < len(memo.keys()):
                for i in memo.keys():
                    del memo[i]
                    break
            if(args, str(kwargs)) in memo.keys():
                return memo[(args, str(kwargs))]
            answer = function(*args,**kwargs)
            memo[(args, str(kwargs))] = answer
            return answer
        return wrapper
    return decorator

@memoize(2)
def calculate(a,b,c):
    time.sleep(3)
    return a+b+c

if __name__ == "__main__":
    print("Lets start!")
    print(calculate(-1,-10,-121))
    print(calculate(-1,-10,-121))
    print(calculate(10,20,30))
    print(calculate(10,20,30))
    print(calculate(20,20,30))
    print(calculate(20,20,30))
    print(calculate(-1,-10,-121))
    print(calculate(-1,-10,-121))
    print(calculate(10,20,30))
