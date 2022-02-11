#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
import statistics

genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])

coverage = []
for x in range(genome_size):
	coverage.append(0)

for read in range(read_number): 
	position = random.randint(0, genome_size - read_length)
	for i in range(read_length):
		coverage[position + i] = coverage[position + i] + 1

print(min(coverage[read_length:-read_length]), max(coverage[read_length:-read_length]), statistics.mean(coverage[read_length:-read_length]))

'''
python3 32xcoverage.py 1000 100 100
5 20 10.82375
'''
