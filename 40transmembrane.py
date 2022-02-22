#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

def score(code): #made a separate function for attributing value to AA to make neater
		if code == 'I': return 4.5
		elif code == 'V': return 4.2
		elif code == 'L': return 3.8
		elif code == 'F': return 2.8
		elif code == 'C': return 2.5
		elif code == 'M': return 1.9
		elif code == 'A': return 1.8
		elif code == 'G': return -0.4
		elif code == 'T': return -0.7
		elif code == 'S': return -0.8
		elif code == 'W': return -0.9
		elif code == 'Y': return -1.3
		elif code == 'P': return -1.6
		elif code == 'H': return -3.2
		elif code == 'E': return -3.5
		elif code == 'Q': return -3.5
		elif code == 'D': return -3.5
		elif code == 'N': return -3.5
		elif code == 'K': return -3.9
		elif code == 'R': return -4.5
		return 0 #if none of the above put 0
	
def check_proline(seq): #check if P in the alpha helix
	if 'P' in seq:
		return True
	else:
		return False

def KD(seq, window=0, threshold=0, check_alpha = False): #KD calculation. check_alpha is a varaible that dictates whether the proline check function will be executed
	total = 0
	for i in range(window): 
		total += score(seq[i]) #check score for each value in first window
	for pos in range(len(seq) - (window - 1)): #moving window
		if pos > 0:
			total += score(seq[pos + window - 1]) - score(seq[pos-1]) #add one more value on the end, subtract off the other end
		avg = total / window
		if avg > threshold and (check_alpha == False or check_proline(seq[pos:pos+window]) == False): #If threshold is surpassed, and either proline check is being skipped/returned that no P was present, print true
			return True

	return False #if the none of the windows fulfill the criteria, print false


fp = open(sys.argv[1])
assert(len(sys.argv) == 2)
line = fp.readline()

while line: #loop through while there are still lines in the file to go through
	if line[0] == '>':
		name = line.split(' | ') #split each informational segment in the first line into a new list since each segment is separated by two spaces and a |
		protein = name[0] #first segment
		protein = protein[1:] #take off the '>'

		data = ''
		line = fp.readline() #move to next line
		while line:
			data += line[0:len(line) - 1] #add each line to a string of data that will actually be analyzed (minus the \n at the end)
			if data[len(data) - 1] == '*': #if the asterisk is encountered, take off the asterisk and stop the loop
				data = data[0:len(data)-1]
				break
			line = fp.readline() #move to the next line if there is no asterisk

		condition1 = KD(data[0:30], 8, 2.5, False)  
		condition2 = KD(data[30:], 11, 2.0, True)
		if condition1 == True and condition2 == True:
			print(protein)

	line = fp.readline()
		


fp.close()




"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
