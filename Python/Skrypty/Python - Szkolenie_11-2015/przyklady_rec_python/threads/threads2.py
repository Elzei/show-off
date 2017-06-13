#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from threading import Thread
import time

class CountDownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print "t - minus", n
            n -= 1
            time.sleep(1)


c = CountDownTask()
t = Thread(target=c.run, args=(10,))
t.start()
# ....
time.sleep(5)
print "Before terminate"
c.terminate()
t.join()


