#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

input_numbers = []
for x in sys.argv[1:]:
	integer = int(x)
	input_numbers.append(integer)
print(input_numbers)

genome_size = input_numbers[0]
read_number = input_numbers[1]
read_length = input_numbers[2]

genome = []
coverage = []
for x in range(genome_size):
	coverage.append(0)

for read in range(read_number): 
	position = random.randint(0, genome_size - read_length)
	for i in range(read_length):
		update = coverage[position + i] + 1
		coverage[position + i] = update
	
minimum = coverage[0]
maximum = coverage[0]
for num in coverage:
	if num < minimum:
		minimum = num
	if num > maximum:
		maximum = num
running_sum = 0
for pos in coverage:
	running_sum += pos
	print(running_sum)
	
average_coverage = running_sum / genome_size
print(running_sum)
print(minimum, maximum, average_coverage)
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
