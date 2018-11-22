#Exercise 4
#Carolina 
#Time spent: 10 minutes
# -*- coding: Latin-1 -*
""" Write a program to check a computer is connected to the internet. """
import requests
def check_internet():

    url='http://www.google.com/'

    timeout=5

    try:

        _ = requests.get(url, timeout=timeout)

        return True

    except requests.ConnectionError:

        print("Internet is OFF.")

    return False

if check_internet():
	print "Internet is ON"