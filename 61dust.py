#!/usr/bin/env python3
# 61dust.py

import argparse
import math
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

import mcb185 as mcb

parser = argparse.ArgumentParser(description='Open file and returns a new fasta file w/ masked low entropy sequences.')

parser.add_argument('--file', type=str, metavar='<file>', required= True, help='required file argument')

parser.add_argument('--window', type=int, metavar='<int>',required= True, help='required int argument')

parser.add_argument('--threshold', type=float, metavar='<float>',required= True, help='required int argument for entropy')

parser.add_argument('--masking', type=str, metavar='<str>',required=True, help='enter type of masking preferred')


args= parser.parse_args()
for entry in mcb.read_fasta(args.file):
	name = entry[0]
	seq = entry[1].upper()


window = args.window
threshold = args.threshold
masking = args.masking

new_seq = ''

for i in range(0, len(seq), window):
	entropy = mcb.entropy_calc(seq[i:i+window],window)
	if entropy >= threshold:
		new_seq += seq[i:i+window].upper()
	else:
		if masking.upper() == 'N':
			new_seq += 'N' * window
		else:
			new_seq += seq[i:i+window].lower()


with open('newfasta.fa','w') as fp:
	fp.write(name)
	fp.write('\n')
	for i in range(0,len(new_seq), 50):
		fp.write(new_seq[i:i+50])
		fp.write('\n')

