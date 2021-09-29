# Jonathan Koning
# koningj@oregonstate.edu
# CS 514
# factors.py
# instructions: Write a function named factors  that returns all prime factors of an integer. For example, factors(12) returns [2,2,3].
# If the input is a prime or 1 it returns an empty list. The factors should be listed in increasing order.  

import os
import getopt
import sys
import math

#TODO Change to find factorization not factors
def factors(num):
	print("Num: ", num)
	primes = [2]
	print("finding primes")
	
	if(num == 1):
		return []

	if(num%2 == 0):
		return [2] + factors(int(num/2))
	# find all prime numbers that could be factors
	# Only have to search up to num/2 because any number higher will not be a factor

	# To determine if a number is prime, we only have to have to search
	# until the sqrt of the number because all other numbers will be a multiple
	# of a value already checked
	for i in range(2, math.ceil(num/2) + 1):
		isprime = 0
		check = math.ceil(math.sqrt(i))+1
		for j in range(2, check):
			#Check if i is a multiple of j
			if(i%j == 0):
				isprime = 1
				break
			
		if(isprime == 0):
			primes.append(i)
			if(num%i == 0):
				return [i] + factors(int(num/i))

	fac=[]
	# if(num == 1):
	# 	return fac

	# print("finding prime factors")
	# for prime in primes:
	# 	if(num%prime == 0):
	# 		# fac.append(prime)
	# 		return [prime] + factors(num/prime)

	return [int(num)]

if __name__ == "__main__":
	num = ""
	if(len(sys.argv) > 1): 
		num = sys.argv[1]
		try:
			num = int(num)
		except:
			pass		

	if(isinstance(num,int) == False):
		num = input("please enter a positive integer:" )
		try:
			num = int(num)
		except:
			pass
		while isinstance(num,int) == False or num <= 0:
			print("Error! Invalid input!")
			num = input("please enter a positive integer:" )
			try:
				num = int(num)
			except:
				pass
	
	facts = factors(num)
	if(len(facts) == 1):
		facts = []
	print(facts)