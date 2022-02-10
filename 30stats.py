#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

data = []
for x in sys.argv[1:]:
	flt = float(x)
	data.append(flt)

count = len(data) 

#max and min
minimum = data[0]
maximum = data[0]
for num in data:
	if num < minimum:
		minimum = num
	if num > maximum:
		maximum = num
# mean
total_sum = 0
for num in data:
	total_sum += num
mean = total_sum / count

#standard deviation
numerator = 0
for num in data:
	distance = (num - mean)**2
	numerator += distance

stdev = math.sqrt(numerator/ count)

#median
data.sort()
#even number inputs
if (count % 2) == 0:
	upper = math.ceil(count/2)
	lower = math.floor(count/2)
	
	median = (data[upper] + data[lower])/2
#odd number inputs
else:
	median = data[count//2]
	


print('Count: ' + str(count), 'Minimum: ' + f'{minimum:.1f}', 'Maximum: ' + f'{maximum:.1f}', 'Mean: ' + f'{mean:.3f}', 'Std. dev: ' + f'{stdev:.3f}','Median: ' + f'{median:.3f}', sep='\n')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
