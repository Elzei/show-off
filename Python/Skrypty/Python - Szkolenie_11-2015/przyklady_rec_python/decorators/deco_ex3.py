#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import functools
import time

def memoize(max_calls):
    assert max_calls > 0, "max_calls > 0 !"
    def decorator(function):
        memo = {}
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if len(memo.keys()) > max_calls:
                del memo[memo.keys()[0]]
            if (args, str(kwargs)) in memo.keys():
                return memo[(args, str(kwargs))]
            answer = function(*args, **kwargs)
            memo[(args, str(kwargs))] = answer
            return answer
        return wrapper
    return decorator

@memoize(3)
def calculate(a, b, c):
    time.sleep(2)
    return a + b + c

if __name__ == '__main__':
    print "Wow expensive ... "
    print calculate(-1, -10 , -121)
    print "No expensive !!"
    print calculate(-1, -10 , -121)
    print calculate(10, 20 ,30)
    print calculate(20, 20 ,30)
    print calculate(20, 20 ,30)
    print calculate(20, 20 ,30)
    print calculate(20, 50 ,30)
    print calculate(20, 50 ,30)
    print calculate(-1, -10 , -121)
