#!/usr/bin/env python2.7

def calculate(a, b, c):
    return a * 2 + b * 3 + c

def decorate(function, *args, **kwargs):
    print "Befor decorate"
    print function(*args, **kwargs)
    print "After decorate"

if __name__ == '__main__':
    decorate(calculate, 3, 4, 5)
