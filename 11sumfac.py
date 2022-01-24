#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# I worked with Jan Wignall

# your code goes here
sum_n = n
factorial = n
for i in range(1,n):
	sum_n += i
	factorial *= i
print(n, sum_n, factorial)
"""
python3 11sumfac.py
5 15 120
"""
