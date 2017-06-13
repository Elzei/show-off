#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Rodzaje pytañ:
# 'tak/nie' - pytania na które mo¿na odpowiedzieæ jedynie tak i nie
# 'radio' - pytania na które jest jedna dobra odpowiedŸ
# 'check' - pytania na które jest wiele dobrych odpowiedzi
# 'answer' - pytania na które nale¿y podaæ odpwiedŸ tekstow¹

questions = [
	["Na jakim swietle przekraczasz jezdnie.", "radio",
		"czerwone", "zielone", "pomarañczowe", "zielone" ],
	["Czy liczba 7 to liczba pierwsza?", "tak/nie", "tak" ],
	["Jakie znasz kolekcje wspierane przez jêzyk Python?", "check",
		"krotka", "s³ownik", "lista jednokierunkowa", "drzewo", "01"],
	["Jaka nazywa siê funkcja zamieniaj¹ca ci¹g znaków na wielkie litery?",
		"answer", "upper"],
	["Jak nazywa siê jêzyk w którym implementujesz tê aplikacjê?",
		"answer", "python"],
	["Wybierz odpowiedzi które w wyniku daj¹ 8.", "check",
		"3+5", "4+1+3", "11+11", "12-5", "10+3+2-7", "12-13", "0134" ],
	["Czy prawd¹ jest ¿e: True and True daje w wyniku True?", "tak/nie",
		"tak" ]
]
	
