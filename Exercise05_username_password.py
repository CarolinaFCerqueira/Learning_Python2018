#Exercise 5
#Carolina 
# Time spent: 50minutes
# -*- coding: Latin-1 -*
""" 
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 """
import re
p= raw_input("Input your password: ")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
		print("Should have at least 1 letter in [a-z]")
		break
    elif not re.search("[0-9]",p):
		print("Should have at least 1 letter in [0-9]")
		break
    elif not re.search("[A-Z]",p):
		print("Should have at least 1 letter in [A-Z]")
		break
    elif not re.search("[$#@]",p):
		print("Should have at least 1 char in [$#@]")
		break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")