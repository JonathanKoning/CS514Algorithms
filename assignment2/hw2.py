import sys
import getopt
import math




def getinput():
	array = []
	try:
		array = list(map(int, sys.argv[1:]))
	except:
		pass
		
	while(len(array) < 1):
		arr = input("please enter a list of numbers: ")
		array = list(map(int, arr.split(' ')))

	return array

def merge(AL, AR):
	A = []

	i = 0
	j = 0
	while (i < len(AL) and j < len(AR)):
		if(AL[i] <= AR[j]):
			A.append(AL[i])
			i+=1
		else:
			A.append(AR[j])
			j+=1
	
	if(i < len(AL)):
		while i < len(AL):
			A.append(AL[i])
			i+=1
	else:
		while j < len(AR):
			A.append(AR[j])
			j+=1

	return A


def mergeSort(A):
	if(len(A) == 1):
		return A

	half = int(len(A)/2)
	AL = A[:half]
	# print(AL)
	AR = A[half:]
	# print(AR)
	AL = mergeSort(AL)
	AR = mergeSort(AR)
	sorted = merge(AL, AR)

	return sorted

if __name__ == "__main__":
	A = getinput()
	print(A)

	sorted = mergeSort(A)
	print(sorted)