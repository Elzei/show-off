#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

class MyClass(object):
    def __enter__(self):
        print("Zajęto zasób...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Zwolniono zasób!")

if __name__ == "__main__":
    with MyClass() as o:
        pass