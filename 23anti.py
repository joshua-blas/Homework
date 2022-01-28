#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
anti = ''

for nt in dna[::-1]:
	if nt == 'A': anti += 'T'
	elif nt == 'T': anti += 'A'
	elif nt == 'C': anti += 'G'
	else: anti += 'C'
	
print(anti)
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
