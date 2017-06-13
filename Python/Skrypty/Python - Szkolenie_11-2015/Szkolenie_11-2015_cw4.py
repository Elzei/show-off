#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#0.map
"""
def show(arg):
    print(arg)

if __name__ == '__main__':
    data = [10, 20, 30, 40]
    result = map(show, data)
    print("-"*10)
    print(result)
    print("-"*10)
    result = map(lambda x:x*2+1, data)
    for i in range(0,result)
        print(result[i])
"""

#0.filter
"""
def moreTen(x):
    return x>10
filter(moreTen, [4,7,8,11,123,3])
"""

#0.reduce


#0.generatory
def dividers(goldenNumber):
    half_range = ((goldenNumber//2)+1)
    for i in range(1,half_range):
        if not goldenNumber%i:
            yield i

from functools import reduce
def adder(goldenNumber):
    return reduce(lambda x, y: x + y, dividers(goldenNumber))
"""
def perfect_gen(goldenNumer):
    for i in range(2, goldenNumer + 1):
        if i == reduce(lambda x, y: x + y, dividers(goldenNumber)):
            yield i
"""
def CheckGoldenNumeber(goldenNumber):
    if goldenNumber == 0:
        print("Srsly? 0 (zero)!? Dude...")
    elif goldenNumber == 1:
        print("1 can not be a golden number.")
    else:
        if adder(goldenNumber) == goldenNumber:
            print("%s it is gold number!" %goldenNumber)
        else:
            print("Nope, %s it isn't gold number." %goldenNumber)

#for i in range(0, 9001):
#    CheckGoldenNumeber(i)

#0.generator2
def sum_palindrom(value):
    return value + int(str(value)[::-1])

def is_value_palindrom(value):
    return str(value) == str(value)[::-1]

def count_palindromic_add(value):
    answer = []
    for i in range(1, 100):
        sum = sum_palindrom(value)
        if is_value_palindrom(sum):
            answer.append(i)
            answer.append(sum)
            break
        value = sum
    return answer
"""
if __name__ == "__main__":
    for i in  range (1, 100000):
        print(i, ":", count_palindromic_add(i))
"""
#1
def divider(number):
    for i in range(1,number+1):
        if not number%i:
            yield i

def counter(number):
    count = []
    for i in divider(number):
        count.append(i)
    return count

def printer(number):
    list = counter(number)
    if len(list)<3:
        print(number, end=": ")
        print(0)
    else:
        print(number, end=": ")
        for i in list:
            print(i, end=" ")
        print("")

#for i in range(0, 20):
 #   printer(i)

#2
def raport(objectToSpy):
    print(type(objectToSpy))
    for i in range(objectToSpy):
        print(i)

#raport((20,30))








