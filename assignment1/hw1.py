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

def factorsTest(num, num2):
	# print("Num: ", num)
	# primes = [2]
	# print("finding primes")
	
	if(num == 1):
		return ([], num2)

	if(num%2 == 0):
		l,n = factorsTest(int(num/2), 0)
		return ([2] + l, num2+n)
	# find all prime numbers that could be factors
	# Only have to search up to num/2 because any number higher will not be a factor

	# To determine if a number is prime, we only have to have to search
	# until the sqrt of the number because all other numbers will be a multiple
	# of a value already checked
	# for i in range(2, math.ceil(num/2) + 1):	#n/2 times
	i = 2
	while(i*i < num):
		num2 = num2 + 1
		isprime = 0								#n/2 times
		# check = math.ceil(math.sqrt(i))+1
		check = math.ceil(i/2)+1				#n/2 times
		# for j in range(2, check):			 	#n/4 * n/2; 
		j=2
		while(j*j < i):
			num2 = num2 + 1
			#Check if i is a multiple of j
			if(i%j == 0):						#j * n/2 
				isprime = 1						#j * n/2
				#breaks when i is not prime
				break
			j+=1
			
		if(isprime == 0):						#n/2
			if(num%i == 0):
				l,n = factorsTest(int(num/i), 0)
				return ([i] + l, num2+n)
		i+=1

	return ([int(num)], num2)


def factors(num):
	if(num == 1):
		return []

	if(num%2 == 0):
		return [2] + factors(int(num/2))

	# find all prime numbers that could be factors
	# Only have to search up to sqrt(num) because any number higher will not be a factor
	# for i in range(2, math.ceil(num/2) + 1):	#n/2 times worst case
	i = 2
	while(i*i <= num):							#sqrt(num) times
		isprime = 0								
		#check if i is prime
		# To determine if a number is prime, we only have to have to search
		# until the sqrt of the number because all other numbers will be a multiple
		# of a value already checked
		# check = math.ceil(i/2)+1				#sqrt(num) times
		j = 2
		while (j*j <= i): 						#sqrt(sqrt(n)) * sqrt(n) times
			#Check if i is a multiple of j
			if(i%j == 0):						#sqrt(sqrt(n)) * sqrt(n) times
				isprime = 1						
				#breaks when i is not prime
				break
			j+=1
		#if i is prime, check if it is a factor of num	
		if(isprime == 0):						
			if(num%i == 0):						#sqrt(num) times
				return [i] + factors(int(num/i))
		i+=1

	#if num is prime, return
	return [int(num)]


def getinput():
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
	return int(num)

if __name__ == "__main__":
	num = getinput()
	
	facts = factors(num)
	
	#if facts only contains 1 number, then num was prime
	if(len(facts) == 1):
		facts = []
	print(facts)


	# facts = factorsTest(num, 0)
	# runtime = (math.sqrt(num) + math.sqrt(math.sqrt(num)) * math.sqrt(num)) * math.log(num,2)
	# print("sqrt(sqrt(n)) * sqrt(n) * 1/pow(2,log(num,2) ", facts[1]/runtime)