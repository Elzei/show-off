#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import functools

def my_loger(file_name):
    log = open(file_name, "wb")
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            answer = function(*args, **kwargs)
            message = function.__name__+": ("+str(args)+str(kwargs)+") :"+str(answer)
            log.write(bytes(message, "UTF-8"))
            return answer
        return wrapper
    return decorator


@my_loger('D:\REC_Global_-_workplace\Python\PyCharm\Poligon\Szkolenie_11-2015_decorator_loger-log_function.txt')
def calculate(a,b,c):
    return a+b+c

if __name__ == "__main__":
    calculate(10,20,30)