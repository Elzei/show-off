#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

from threading import Thread
import  time

def countdown(n):
    while n >0:
        print("t - minus", n)
        n -= 1
        time.sleep(1)

#To jeszcze nie startuje watkow!
t1 = Thread(target=countdown, args=(5,)) #args MUSI byc krotka
t2 = Thread(target=countdown, args=(8,))

#Poprzez zaniechanie, robie cos "niefajnego". Powrot do main nastapi po zakonczeniu tych watkow.
t1.start()
t2.start()

#Ale ale, mozna to naprawic! Wystarczy zrobic join ktory dba o zamykanie i powroty z watkow. Watek po prostu nie bedzie
#wisial w powietrzu tylko ladnie sie skonczy.
t1.join()
t2.join()