#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from threading import Thread
import time

def countdown(n):
    while n > 0:
        print "t - minus", n
        n -= 1
        time.sleep(1)

# To jeszcze nie startuje wątków!
t1 = Thread(target=countdown, args=(5,))
t2 = Thread(target=countdown, args=(8,))
t1.start()
t2.start()

t1.join()
t2.join()

