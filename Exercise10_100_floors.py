# -*- coding: Latin-1 -*
#Exercise 10
#Carolina  
#   

""" A building has 100 floors. One of the floors is the highest floor an egg can be
dropped from without breaking. If an egg is dropped from above that floor, it will
break. If it is dropped from that floor or below, it will be completely undamaged and
you can drop the egg again.
Given two eggs, give a method to find the highest floor an egg can be dropped from
without breaking, with as few drops as possible.
"""
from random import randrange

def maxFirstScan (hFloor):
	"""Egg1: This function scan with step 10 and return the last step scanned.
	Like that you have used your first egg and"""
	for floor in range(1, 100, 10):
		if floor >= hFloor:   #break egg?
			return floor
	else: #is in [92,100]
		return 100

highestFloor = randrange(1,100)
print("%i Random Highest Floor."%(highestFloor))
		
maxFirst =	maxFirstScan(highestFloor)
"""Egg2 scan in a range of maximun 10
"""
for floor in range (maxFirst-9, maxFirst+1):
	if floor == highestFloor:
		print("%i was the Found Floor." %floor)
