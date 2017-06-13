#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

class MyClass(object):
    def __init__(self, val):
        self._val = val

    @property
    def value(self):
        return self._val + 10

    @value.setter
    def value(self, val):
        self._val = val

    @value.deleter
    def value(self):
        print("Wow... i'm gone :< (delete)!")

if __name__ == '__main__':
    o = MyClass(100)
    #print(o.get_value())
    print(o.value)
    o.value=5000
    print(o.value)
    del o.value
