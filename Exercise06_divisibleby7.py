#Exercise 6
#Carolina
# Time spent: 8 minutes
# -*- coding: Latin-1 -*
""" Write a program which will find all such numbers which are divisible by 7 but are not
a multiple of 5, between 77 and 777 (both included).
"""

for num in range(77, 778):
	if (num % 7 == 0) and not(num % 5 == 0):
		print num,