#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Magazyn wysy�ki ksi��ek

class Paczka(object):
	def __init__(self, klient):	# inicjalizuje paczk� klienta
	def dodaj(self, ksiazka):	# dodaje ksi��k� do paczki
	def zawartosc(self):		# raportuje zawartosc paczki

class Klient(object):
	def __init__(self, nazwa, adres): # inicjalizuje klienta
	def dajInfo(self):		  # zwraca informacj� o kliencie

class Sprzedawca(object):
	def dodajKsiazke(self, ksiazka, paczka):# dodaje ksi��k� do paczki
	def oddajKsiazke(self, ksiazka, paczka):# usuwa ksi��k� z paczki
	def finalizuj(self, paczka):	# wysy�a paczk�

class Ksiazka(object):
	def __init__(self, nazwa, cena):# tworzy ksi��k�
	def dajInfo(self):		# zwraca informacj� o ksi��ce

if __name__ == '__main__': 
	pass
