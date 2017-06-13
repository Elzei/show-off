#!/usr/bin/env python2.7

import pickle

class MyContainer(object):
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data
       
#p1 = object()

with open('/tmp/pickle_data.dat', 'rb') as f:
    p = pickle.Unpickler(f)
    p1 = p.load()

print p1.get_data()
