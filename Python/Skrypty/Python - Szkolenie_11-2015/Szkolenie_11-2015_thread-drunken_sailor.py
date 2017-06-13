#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import threading
from threading import Thread
import time


class DrunkenSailor(object):

    def __init__(self, road_width=5, position=3):
        self._running = True
        self._road_width = road_width
        self._position = position
        self._value_lock = threading.Lock()

    def terminate(self):
        self._running = False

    def show_road(self):
        road = "|"
        for i in range(self._road_width + 1):
            time.sleep(0.2)
            if self._position == i:
                road += "*"
            else:
                road += "-"
        road += "|"
        print(road)

    def wind_right(self, delta=1):
        while (self._position > 0) and (self._position < self._road_width):
            self._value_lock.acquire()
            self._position += delta
            self._value_lock.release()
            self.show_road()

    def wind_left(self, delta=1):
        self.wind_right(-1)

    def wind(self):
        pass

sailor = DrunkenSailor()

t1 = Thread(target=sailor.wind_right())
t2 = Thread(target=sailor.wind_left())

t1.start()
t2.start()

t1.join()
t2.join()
