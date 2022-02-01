#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

#worked with Jan Wignall

dna = ''
at = 0
for i in range(30):
	r = random.random()
	if r < 0.3: 
		dna += 'A'
		at += 1
	elif r < 0.6: 
		dna += 'T'
		at += 1
	elif r < 0.8: dna += 'G'
	else: dna += 'C'
	
at_frac = at / len(dna)

print(len(dna) , at_frac, dna)

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
