#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc_count = 0

for i in range(len(dna)):
	if dna[i] == 'G' or dna[i] == 'C': gc_count += 1
fraction = gc_count/len(dna)

print(f'{fraction:.2f}') 
print('%.2f' % (fraction)) 
print('{:.2f}'.format(fraction)) 

#use 3 different ways of frac rounding

"""
python3 21gc.py
0.42
0.42
0.42
"""
