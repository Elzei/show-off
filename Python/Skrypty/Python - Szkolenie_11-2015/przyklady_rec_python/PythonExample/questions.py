#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Rodzaje pyta�:
# 'tak/nie' - pytania na kt�re mo�na odpowiedzie� jedynie tak i nie
# 'radio' - pytania na kt�re jest jedna dobra odpowied�
# 'check' - pytania na kt�re jest wiele dobrych odpowiedzi
# 'answer' - pytania na kt�re nale�y poda� odpwied� tekstow�

questions = [
	["Na jakim swietle przekraczasz jezdnie.", "radio",
		"czerwone", "zielone", "pomara�czowe", "zielone" ],
	["Czy liczba 7 to liczba pierwsza?", "tak/nie", "tak" ],
	["Jakie znasz kolekcje wspierane przez j�zyk Python?", "check",
		"krotka", "s�ownik", "lista jednokierunkowa", "drzewo", "01"],
	["Jaka nazywa si� funkcja zamieniaj�ca ci�g znak�w na wielkie litery?",
		"answer", "upper"],
	["Jak nazywa si� j�zyk w kt�rym implementujesz t� aplikacj�?",
		"answer", "python"],
	["Wybierz odpowiedzi kt�re w wyniku daj� 8.", "check",
		"3+5", "4+1+3", "11+11", "12-5", "10+3+2-7", "12-13", "0134" ],
	["Czy prawd� jest �e: True and True daje w wyniku True?", "tak/nie",
		"tak" ]
]
	
