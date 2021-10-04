import sys
import getopt
import math
import datetime
import random
import csv
import time

def randomData(num):
	array = []
	# for i in range(num):
	# 	array.append(random.randint(0, 1000000))
	i = 0
	while i < num:
		array.append(i)
		i+=1

	return array


def getinput():
	array = []

	if(len(sys.argv) == 1):
		while(len(array) < 1):
			arr = input("please enter a list of numbers: ")
			array = list(map(int, arr.split(' ')))

		return array

	if(sys.argv[1] == "-r"):
		num = ""
		num = sys.argv[2]
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
		
		# for i in range(num):
			# array.append(random.randint(0, 1000000))
		
		return randomData(num)

	elif(sys.argv[1] == "-d"):
		dataMode()
		return "datamode"

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
	AR = A[half:]
	AL = mergeSort(AL)
	AR = mergeSort(AR)
	sorted = merge(AL, AR)

	return sorted


def quickSort(A):
	if A == []:
		return []
	else:
		pivot = A[0]
		left = [x for x in A if x < pivot]
		right = [x for x in A[1:] if x >= pivot]
		return quickSort(left) + [pivot] + quickSort(right)


def dataMode():
	points = 1000
	# points = [1, 10, 50, 100, 500, 1000, 1500, 2000, 2500, 5000, 10000, 15000]
	with open("results_1000s.csv", 'w', newline='') as f:
		row = ["n", "mergeSort", "quickSort"]
		writer = csv.writer(f)
		writer.writerow(row)


	for i in range(1,points):
	# for i,x in enumerate(points):
		# print(i)
		A = randomData(i)
		# print(A)
		# start = datetime.datetime.now()
		start = time.perf_counter()
		sorted = mergeSort(A)
		# stop = datetime.datetime.now()
		stop = time.perf_counter()
		mergeSortduration = stop-start
	
		# start = datetime.datetime.now()
		start = time.perf_counter()
		sorted = quickSort(A)
		# stop = datetime.datetime.now()
		stop = time.perf_counter()
		quickSotduration = stop-start
		# print("quickSort: ", sorted)
		row = [str(i), str(mergeSortduration), str(quickSotduration)]
		with open("results_1000s.csv", 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(row)



if __name__ == "__main__":
	A = getinput()
	# print(A)
	if(A == "datamode"):
		exit()

	start = datetime.datetime.now()
	sorted = mergeSort(A)
	stop = datetime.datetime.now()
	duration = stop-start
	#print("mergeSort: ", sorted)
	print("mergeSort Duration: ", duration)
	
	start = datetime.datetime.now()
	sorted = quickSort(A)
	stop = datetime.datetime.now()
	duration = stop-start
	# print("quickSort: ", sorted)
	print("quickSort Duration: ", duration)