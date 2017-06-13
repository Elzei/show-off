#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import pickle

class MyClass(object):
    def __init__(self, value):
        self._value = value
        self._list = [self._value, self._value+1]

    def get_data(self):
        print(self._list[0])
        print(self._list[1])

if __name__ == "__main__":
    path="D:\REC_Global_-_workplace\Python\PyCharm\Poligon\Szkolenie_11-2015_pickle-pickle.txt"
    lista = MyClass(15)
    file = open(path, "wb")
    pickla = pickle._Pickler(file, 0)
    pickla.dump(lista)
    file.close()

    del lista

    obj = object()
    with open(path, "rb") as f:
        p = pickle.Unpickler(f)
        obj = p.load()

    obj.get_data()
