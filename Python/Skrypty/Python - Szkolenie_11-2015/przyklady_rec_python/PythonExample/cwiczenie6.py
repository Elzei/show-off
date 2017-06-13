#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Magazyn wysy³ki ksi¹¿ek

class Paczka(object):
	def __init__(self, klient):	# inicjalizuje paczkê klienta
	def dodaj(self, ksiazka):	# dodaje ksi¹¿kê do paczki
	def zawartosc(self):		# raportuje zawartosc paczki

class Klient(object):
	def __init__(self, nazwa, adres): # inicjalizuje klienta
	def dajInfo(self):		  # zwraca informacjê o kliencie

class Sprzedawca(object):
	def dodajKsiazke(self, ksiazka, paczka):# dodaje ksi¹¿kê do paczki
	def oddajKsiazke(self, ksiazka, paczka):# usuwa ksi¹¿kê z paczki
	def finalizuj(self, paczka):	# wysy³a paczkê

class Ksiazka(object):
	def __init__(self, nazwa, cena):# tworzy ksi¹¿kê
	def dajInfo(self):		# zwraca informacjê o ksi¹¿ce

if __name__ == '__main__': 
	pass
