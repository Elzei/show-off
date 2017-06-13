#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#1
import random

randomizer = random.random() * 100

def chaos_add(a,b):
    return a+b+randomizer

def chaos_minus(a,b):
    return a-b-randomizer

def chaos_multi(a,b):
    return a*b*randomizer

def chaos_davide(a,b):
    return randomizer/a/b

def test():
    a,b=44,66
    print("Chaos in add",a,"and",b,":",chaos_add(a,b))
    print("Chaos in minus",a,"and",b,":",chaos_minus(a,b))
    print("Chaos in multi",a,"and",b,":",chaos_multi(a,b))
    print("Chaos in davide",a,"and",b,":",chaos_davide(a,b))

if __name__ == "__main__":
    test()