#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pickle

class MyContainer(object):
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data

d1 = MyContainer([2, 5, 4, 3, [ 12, 3, 5 ], 32, { 'a': 12, 'b': 43}])

with open('/tmp/pickle_data.dat', "wb") as f:
    p = pickle.Pickler(f, 2)
    p.dump(d1)




