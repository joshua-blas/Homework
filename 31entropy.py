#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys


prob = []
tolerance = 0.00001
total_prob = 0

for number in sys.argv[1:]:
	flt = float(number)
	prob.append(flt)
	total_prob += flt
	
if abs(total_prob-1) > tolerance:
	print('Sum of probabilities does not add up to 1')
	sys.exit()

prob_product = 0
prob_sum = 0 

for x in prob:
	prob_product = x * math.log2(x)
	prob_sum += prob_product
	

if abs(total_prob-1) > tolerance:
	sys.exit()
	
entropy = -1 * prob_sum
	
print(f'{entropy:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
