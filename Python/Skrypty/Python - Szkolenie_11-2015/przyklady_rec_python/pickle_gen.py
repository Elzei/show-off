#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pickle
import generator

def my_gen(iterations):
    for i in xrange(iterations):
        yield i

g = my_gen(10)

g.next()
g.next()


with open('/tmp/pickle_gen.dat', "wb") as f:
    p = pickle.Pickler(f, 2)
    p.dump(g)




