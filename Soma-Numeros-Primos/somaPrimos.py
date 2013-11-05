# -*- coding: utf-8 -*-

print '\n ----- Começa aqui ----\n'
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def ePrimo( numero ):
	if (numero == 1) or (numero == 2):
		return True

	elif (numero % 2 != 0):
		z = 0
		
		for x in range(1, numero + 1):
			if numero % x == 0: 
				z += 1
			else: 
				z += 0
		if z > 2: 
			return False
		else: 
			return True
	else:
		return False

	
z = 0
for x in range(2,2000000):
	if ePrimo(x):
		z +=x

print z













print '\n ------Termina aqui -----'