#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Magazyn wysy³ki ksi¹¿ek

class Paczka(object):
	def __init__(self, klient):	# inicjalizuje paczkê klienta
		self.__klient = klient		
		self.__content = []
	def dodaj(self, ksiazka):	# dodaje ksi¹¿kê do paczki
		self.__content.append(ksiazka)
	def zawartosc(self):		# raportuje zawartosc paczki
		suma = 0
		print "Paczka nale¿¹ca do: %s\nNa adres %s\nZawiera:" \
			% self.__klient.dajInfo()
		print "-" * 40
		for i in self.__content:
			print "Tytu³: %-23s Cena: %3d" % i.dajInfo()
			suma = suma + i.dajInfo()[1]
		print "-" * 40
		print "%29s Razem: %3d" % (" ", suma)
		print "-" * 40

class Klient(object):
	def __init__(self, nazwa, adres): # inicjalizuje klienta
		self.__nazwa = nazwa
		self.__adres = adres
	def dajInfo(self):		  # zwraca informacjê o kliencie
		return self.__nazwa, self.__adres

class Sprzedawca(object):
	def dodajKsiazke(self, ksiazka, paczka):# dodaje ksi¹¿kê do paczki
		paczka.dodaj(ksiazka)
	def oddajKsiazke(self, ksiazka, paczka):# usuwa ksi¹¿kê z paczki
		paczka.usun(ksiazka)
	def finalizuj(self, paczka):	# "zamyka" paczkê i j¹ wysy³a
		print "*" * 40 + "\nWysy³am paczkê"
		paczka.zawartosc()
		print "Paczka wys³ana\n" + "*" * 40
		

class Ksiazka(object):
	def __init__(self, nazwa, cena):# tworzy ksi¹¿kê
		self.nazwa = nazwa
		self.cena = cena
	def dajInfo(self):		# zwraca informacjê o ksi¹¿ce
		return self.nazwa, self.cena

if __name__ == '__main__': 
	klient = Klient('Adam Zyga', "B³otna 32")
	sprzedawca = Sprzedawca()
	paczka = Paczka(klient)
	ksiazki = { 'W pustyni i w puszczy': 32, 'Ksi¹¿ka kucharska': 31,
		'Python - przed i po': 102}
	for i in ksiazki.keys():
		ksiazka = Ksiazka(i, ksiazki[i])
		sprzedawca.dodajKsiazke(ksiazka, paczka)
	sprzedawca.finalizuj(paczka)
