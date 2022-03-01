#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

filename = sys.argv[1]		
def readfile(filename):
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip().lstrip()
			if len(line) == 0: continue
			if 'ORIGIN' in line:
				seq = ''
			else:
				line = line.split()
				bases = line[1:]
				for fragment in bases:
					seq += fragment
	return seq
	
seq = readfile(filename)
rsite = sys.argv[2]
start = None
for match in re.finditer(rsite, seq):
	if start == None:
		start = match.start()
		print(start)
	else:
		length = match.start() - start
		print(length)
		start = match.start()


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
