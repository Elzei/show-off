#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

import threading

class SharedCounter():
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta = 1):
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()

    def decr(self, delta = 1):
        self.incr()

