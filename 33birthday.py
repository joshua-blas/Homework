#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

people = 25
overlap = 0
overlaptotal = 0
for i in range(1000):  #trials
	calendar = [0] * 365 #reset calendar and overlap
	overlap = 0
	for x in range(people):      #assigning birthdays to each person
		bday = random.randint(0,len(calendar) - 1)
		calendar[bday] = calendar[bday] + 1
		if calendar[bday] > 1:
			overlap = 1
			break
	overlaptotal += overlap
			
			
probability = overlaptotal / 1000

print(probability)
	
			
	

	
	

"""
python3 33birthday.py
0.571
"""

