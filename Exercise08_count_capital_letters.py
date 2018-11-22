#Exercise 8
#Carolina  
# Time spent: 30 minutes 
# -*- coding: Latin-1 -*

""" Write a function to count capital letters in a text file text.txt
"""
def countUpLetters (textFile):
	qtyUp=0
	for line in textFile:
		for char in line:
			if char.isupper():
				qtyUp += 1
	return qtyUp

file = open("text.txt", "r")
print ("The file has %i capital letters"%(countUpLetters(file)))
file.close()