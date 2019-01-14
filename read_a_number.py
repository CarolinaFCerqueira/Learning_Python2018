# -*- coding: Latin-1 -*

# Read a number
#Carolina FC 14-01-1
# in : num_1
# D : 
# out : nothing
import os
import math
from random import randrange

is_number=True;

num_1 = raw_input("Choisi un numero: ")
try :
	num_1 = int(num_1)
except : 
	print("Erreur lors de la convertion du numero choisi!")
	is_number=False

while not(is_number):
	is_number=True;
	try :
		num_1 = input("Choisi un numero:")
	except : 
		print("Erreur lors de la convertion du numero choisi!")
		is_number=False
