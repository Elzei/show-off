#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

class MyClass(object):
    def __init__(self, name):
        self._name = name

    def obj_method(self):
        print "Object method in Class", MyClass.__name__, " name ", self._name

    # Metoda statyczna, wołana _na_rzecz_klasy_
    @staticmethod 
    def static_method():
        print "Static method in Class", MyClass.__name__

    # Metoda klasowa przekazuje klasę a nie "self"
    @classmethod
    def class_method(cls):
        print "Class method in class", cls.__name__


if __name__ == '__main__':
    o1 = MyClass("Klasa") 
    o1.obj_method()
    # Tak nie wywołam!
    # o1.static_method()
    MyClass.static_method()
    MyClass.class_method()
