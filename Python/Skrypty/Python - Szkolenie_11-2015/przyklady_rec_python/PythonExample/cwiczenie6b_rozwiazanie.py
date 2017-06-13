#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Magazyn wysy�ki ksi��ek

class Paczka(object):
	def __init__(self, klient):	# inicjalizuje paczk� klienta
		self.__klient = klient		
		self.__content = []
	def __add__(self, ksiazka):	# dodaje ksi��k� do paczki
		self.__content.append(ksiazka)
	def __repr__(self):		# raportuje zawartosc paczki
		suma = 0
		message = "Paczka nale��ca do: %s\nNa adres %s\nZawiera:\n" \
			% self.__klient.dajInfo()+ "-" * 40 + "\n" 
		for i in self.__content:
			message += "Tytu�: %-23s Cena: %3d\n" % i.dajInfo()
			suma = suma + i.dajInfo()[1]
		message += "-" * 40 + "\n"
		message += "%29s Razem: %3d\n" % (" ", suma) + "-" * 40
		return message

class Klient(object):
	def __init__(self, nazwa, adres): # inicjalizuje klienta
		self.__nazwa = nazwa
		self.__adres = adres
	def dajInfo(self):		  # zwraca informacj� o kliencie
		return self.__nazwa, self.__adres

class Sprzedawca(object):
	def dodajKsiazke(self, ksiazka, paczka):# dodaje ksi��k� do paczki
		paczka + ksiazka
	def oddajKsiazke(self, ksiazka, paczka):# usuwa ksi��k� z paczki
		paczka.usun(ksiazka)
	def finalizuj(self, paczka):	# "zamyka" paczk� i j� wysy�a
		print "*" * 40 + "\nWysy�am paczk�"
		print paczka
		print "Paczka wys�ana\n" + "*" * 40

class Ksiazka(object):
	def __init__(self, nazwa, cena):# tworzy ksi��k�
		self.nazwa = nazwa
		self.cena = cena
	def dajInfo(self):		# zwraca informacj� o ksi��ce
		return self.nazwa, self.cena

if __name__ == '__main__': 
	klient = Klient('Adam Zyga', "B�otna 32")
	sprzedawca = Sprzedawca()
	paczka = Paczka(klient)
	ksiazki = { 'W pustyni i w puszczy': 32, 'Ksi��ka kucharska': 31,
		'Python - przed i po': 102}
	for i in ksiazki.keys():
		ksiazka = Ksiazka(i, ksiazki[i])
		sprzedawca.dodajKsiazke(ksiazka, paczka)
	sprzedawca.finalizuj(paczka)
