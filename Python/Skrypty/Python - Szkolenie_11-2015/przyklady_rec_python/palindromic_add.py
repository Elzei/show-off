#!/usr/bin/env python2.7
# -*- conding: utf-8 -*-

def sum_palindromic(value):                                                                                           
    return value + long(str(value)[::-1])

def is_value_palindrom(value):
    return str(value) == str(value)[::-1]

def count_palindromic_add(value):
    answer = ()

    for i in xrange(1, 5000):
        sum = sum_palindromic(value)
        if is_value_palindrom(sum):
            answer = (i, sum)
            break
        value = sum

    return answer

if __name__ == '__main__':
    print sum_palindromic(98)
    print is_value_palindrom(89198)
    for i in xrange(1000000000, 10000000000000000):
        print i, ": ", count_palindromic_add(i)
