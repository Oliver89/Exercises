# Little Python 3 script for calculating the places of PI

import math

def factorial(n):
	# Computers the factorial of n
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def estimate_pi():
	'''Computes an estimation of the value of PI according to the
	algorithm by Srinivasa Ramanujan.'''
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		term = factor * num/den
		total += term
		
		if abs(term) < 1e-15: break
		k += 1
		print(total)
		
		
	return 1 / total
	
print(estimate_pi())
