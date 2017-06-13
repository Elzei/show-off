#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Animacja piłki poruszającej się po ekranie.

Program napisany w stylu proceduralnym. Zaimplementowano tylko 
pojedynczą piłkę.
"""

import random, os, time, sys

VERSION = "0.0.1"

def init_board(width = 30, height = 25):
	"""Inicjalizacja planszy, oraz jej szerokości i  wysokości.

	init_board(width, height) -> {}
	"""
	board = { 'width': width, 'height': height }
	return board

def show_board(board, ball, empty_char = '.', ball_char = '*'):
	"""Funkcja drukująca planszę z piłką.
	
	show_board(board, ball, empty_char = '.', ball_char = '*')
	
	Puste pole reprezentowane jako '.' a pole z piłką jako '*'.
	"""
	# Pętla drukująca
	for i in range(0, board['height']):
		for j in range(0, board['width']):
			char = ball_char if ((j == ball['x'])
				and (i == ball['y'])) else empty_char
			print(char, end = '')
		print("")

def init_ball(board):
	"""Inicjalizowanie piłki, jej pozycji i wektorów.

	init_ball(board) -> ball
	"""
	random.seed()
	# Ustawienie pozycji i wektorów
	ball = {	'x': random.randrange(1, board['width'] - 1),
			'y': random.randrange(1, board['height'] - 1),
			'dx': random.randrange(0,2) * 2 - 1,
			'dy': random.randrange(0,2) * 2 - 1
	}
	return ball

def animate_ball(board, ball):
	"""Animacja piłki poruszającej się po ekranie.

	animate_ball(board, ball)
	"""
	
	# Uderzenie w prawy lub lewy brzeg planszy
	if ( ball['x'] == 0 ) or ( ball['x'] == (board['width'] - 1) ):
		ball['dx'] *= -1
	# Uderzenie w górę lub dół planszy
	if ( ball['y'] == 0 ) or ( ball['y'] == (board['height'] - 1) ):
		ball['dy'] *= -1
	# Uaktualnienie pozycji
	ball['x'] = ball['x'] + ball['dx']
	ball['y'] = ball['y'] + ball['dy']

def run_ball(width, height, sleeptime = 0.1):
	"""Uruchomienie animacji.

	run_ball(width, height, sleeptime = 0.1)

	Animacja nigdy nie kończy się i wymaga przerwania z klawiatury.
	"""

	board = init_board(width, height)
	ball = init_ball(board)

	while True:
		show_board(board, ball)
		animate_ball(board, ball)
		time.sleep(sleeptime)
		if sys.platform == 'linux':
			os.system("clear")
		elif sys.platform in ('win32', 'cygwin'):
			os.system("cls")

if __name__ == '__main__':
	try:
		run_ball(30, 25, 0.01)
	except KeyboardInterrupt as e:
		print("Koniec programu.")
