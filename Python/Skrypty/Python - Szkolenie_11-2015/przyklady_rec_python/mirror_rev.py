#!/usr/bin/env python2.7
# -*- conding: utf-8 -*-

def sum_rev(value):
    return value + long(str(value)[::-1])

def is_palindrom(value):
    return str(value) == str(value)[::-1]

def calc_add_palindromic(value):
    i = 1;
    result = value

    while(i < 100):
        result = sum_rev(result)
        if is_palindrom(result):
            break
        i += 1
    else:
        i, result = 0, 0

    return (i, result)


if __name__ == '__main__':
    for i in xrange(200):
        count, number = calc_add_palindromic(i)
        print "%d: %d %d" % (i, count, number)
