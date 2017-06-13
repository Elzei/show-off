#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import threading 
import time

class Marynarz(object):

    def __init__(self, szer_drogi= 9, czas = 0.1):
        self._pozycja = szer_drogi / 2
        self._szer_drogi = szer_drogi
        self._blokada = threading.Lock()
        self._czas = czas
        self._uruchomione = False

    def pokaz_droge(self):
        droga = "|"
        for i in range(self._szer_drogi + 1):
            if self._pozycja == i:
                droga += "*"
            else:
                droga += "-"
        droga += "|"
        print droga

    def sciagaj(self, delta = 1):
        while self._uruchomione and self._blokada.acquire():
            self._pozycja += delta
            self.pokaz_droge()
            if self._pozycja == 0 or self._pozycja == self._szer_drogi:
                self._uruchomione = False
            self._blokada.release()

            # Dla testów tendencji "do prawej" i "do lewej"
            time.sleep(self._czas - float(delta) / 100)
            time.sleep(self._czas)

    def run(self):
        lewy = threading.Thread(target=self.sciagaj, args=(-1,))
        prawy = threading.Thread(target=self.sciagaj, args=(1,))
        self._uruchomione = True
        lewy.start()
        prawy.start()
        lewy.join()
        prawy.join()

if __name__ == '__main__':
    m = Marynarz()
    m.run()

