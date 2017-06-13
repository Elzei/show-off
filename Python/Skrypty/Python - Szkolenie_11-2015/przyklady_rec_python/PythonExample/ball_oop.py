#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Animacja piłki poruszającej się po ekranie.

Program napisany w stylu obiektowym. 
"""

import random, os, time, sys

VERSION = "0.0.1"

class Board(object):
	"""Klasa planszy. Obsługuje całą symulację"""

	def __init__(self, width = 30, height = 25, sleeptime = 0.1):
		"""Inicjalizacja planszy, oraz jej szerokości i  wysokości.

		Board(width = 30, height = 25) -> board
		"""
		random.seed()
		self.width = width
		self.height = height
		self.sleeptime = sleeptime
		self.clear_command = 'cls' if ((sys.platform in
			('win32', 'cygwin'))) else 'clear'

	def show_board(self, ball, empty_char = '.', ball_char = '*'):
		"""Funkcja drukująca planszę z piłką.
	
		ball.show_board(ball, empty_char = '.', ball_char = '*')
	
		Puste pole reprezentowane jako '.' a pole z piłką jako '*'.
		"""

		# Pętla drukująca
		for i in range(0, self.height):
			for j in range(0, self.width):
				char = ball_char if ((j == ball.x)
					and (i == ball.y)) else empty_char
				print(char, end = '')
			print("")

	def add_ball(self, ball):
		"""Dodanie piłki do planszy"""

		self.ball = ball

	def run_ball(self):
		"""Uruchomienie animacji.

		board.run_ball()

		Animacja wymaga przerwania z klawiatury.
		"""

		while True:
			self.show_board(ball)
			self.ball.animate_ball()
			time.sleep(self.sleeptime)
			os.system(self.clear_command)

class Ball(object):
	"""Klasa piłki."""

	def __init__(self, board):
		"""Inicjalizowanie piłki, jej pozycji i wektorów.

		Ball(board) -> ball
		"""
		# Ustawienie pozycji i wektorów
		self.board = board
		self.x = random.randrange(1, board.width - 1)
		self.y = random.randrange(1, board.height - 1)
		self.dx = random.randrange(0,2) * 2 - 1
		self.dy = random.randrange(0,2) * 2 - 1

	def animate_ball(self):
		"""Animacja piłki poruszającej się po ekranie.

		animate_ball()
		"""
	
		# Uderzenie w prawy lub lewy brzeg planszy
		if ( self.x == 0 ) or ( self.x == (self.board.width - 1)):
			self.dx *= -1
		# Uderzenie w górę lub dół planszy
		if ( self.y == 0 ) or ( self.y == (self.board.height - 1)):
			self.dy *= -1
		# Uaktualnienie pozycji
		self.x += self.dx
		self.y += self.dy


if __name__ == '__main__':
	try:
		board = Board(30, 25, 0.1)
		ball = Ball(board)
		board.add_ball(ball)
		board.run_ball()
	except KeyboardInterrupt as e:
		print("Koniec programu.")
