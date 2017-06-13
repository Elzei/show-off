#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

class MyClass(object):
    def __init__(self, name):
        self._name = name

    def obj_method(self):
        print("Object method in Class",self._name,"in class",MyClass.__name__)

    #Metoda statyczna, wolana _na_rzecz_klasy_
    @staticmethod
    def static_method():
        print("Static method in Class",MyClass.__name__)

    #Metoda klasowa przekazuje klase a nie "self'
    @classmethod
    def class_method(cls):
        print("Class method in class", cls.__name__)

if __name__ == "__main__":
    o1 = MyClass("Klasa")
    o1.obj_method()
    #Tak wywołam metodę statyczną
    MyClass.static_method()
    #A tak nie
    #o1.static_method()
    MyClass.class_method()