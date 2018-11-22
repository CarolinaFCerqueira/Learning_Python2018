#Exercise 7
#Carolina
# Time spent: 1h30 minutes 
# -*- coding: Latin-1 -*
""" Consider the following class:
class Coordinate(object): def __init__(self, x, y):
self.x = x
self.y = y
def getX(self): return self.x
def getY(self): return self.y
def __str__(self): return '<' + str(self.getX()) + ',' +
str(self.getY()) + '>'
Write a class method to check if two Coordinate instances are equal.
"""
class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getX(self): return self.x
	def getY(self): return self.y
	def __str__(self): return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
	def __eq__(self, second):
		"""test if second is equal to self"""
		return self.x == other.x and self.y == other.y
