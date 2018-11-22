#Exercise 9
#Carolina
# Time spent: 40 minutes 
# -*- coding: Latin-1 -*
""" Write a function to test if a number x is prime
"""
import math
def prime(num):
	for fac in range (2, int(math.sqrt(num))):
		if num % fac == 0:
			print "Not prime."
			break
	else:
		print ("Is prime!")
		return True
	return False
#	for fac in range(sqrt(num)

prime(int(raw_input("Write a number:")))