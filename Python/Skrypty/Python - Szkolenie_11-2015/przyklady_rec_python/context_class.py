#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

class MyClass(object):
    def __enter__(self):
        print "Zajęcie zasobu"

    def __exit__(self, type, value, traceback):
        print "Zwolnienie zasobu"

if __name__ == '__main__':
    with MyClass() as o:
        pass


