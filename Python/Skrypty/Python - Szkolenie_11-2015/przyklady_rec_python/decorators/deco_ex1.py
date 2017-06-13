#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import functools

def no_more_10(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        answer = function(*args, **kwargs)
        if answer > 10:
            answer = 10
        elif answer < - 10:
            answer = -10
        return answer
    return wrapper

@no_more_10
def calculate(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print calculate(-1, -10 , -121)
