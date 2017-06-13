#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from threading import Thread
import time

class CountDownTask(Thread):
    def __init__(self, n):
        super(CountDownTask,self).__init__()
        self._running = True
        self._n = n

    def terminate(self):
        self._running = False

    # To powinno nazywać się run bo po start() z Thread startowane jest run()
    def run(self):
        while self._running and self._n > 0:
            print "t - minus", self._n
            self._n -= 1
            time.sleep(1)


c = CountDownTask(10)
c.start()
# ....
time.sleep(5)
print "Before terminate"
c.terminate()
print "After terminate"
c.join()


