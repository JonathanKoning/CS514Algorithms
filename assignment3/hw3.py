import sys 
import math
import random


#Maxheapify(A, i) assumes left and right subtrees of i already satisfy the heap property.
#Guarantees all nodes rooted at i satisfy the heap property.
#if i violates the heap property, i.e., smaller than one of its children:
# exchange A[i] with Max(A[Left[i], A[Right[i]]).
# recusrsively call Maxheapify on A,j where A[j] and A[i] have just been exchanged
def Maxheapify(A, i): 
	left = int(2*i+1)
	right = int(2*i+2)
	#print("len(A): ", len(A))
	#print("left: ", left)
	#print("right: ", right)

	if(left >= len(A)):
		return A

	elif(right >= len(A)):
		if(A[i] < A[left]):
			A[i], A[left] = A[left], A[i]
			A = Maxheapify(A, left)

	elif((A[i] < A[left]) and (A[left] >= A[right])):
		A[i], A[left] = A[left], A[i]
		A = Maxheapify(A, left)
	elif((A[i] < A[right]) and (A[right] > A[left])):
		A[i], A[right] = A[right], A[i]
		A = Maxheapify(A, right)

	return A

def BuildMaxHeap(A):
	N = len(A)

	i = int(math.floor((N-1)/2))
	while(i >= 0): 
		A = Maxheapify(A, i)
		i-=1

	return A



def HeapSort(A):
	A = BuildMaxHeap(A)
	# print(A)
	s = len(A)
	n = len(A)-1
	while(s > 1): 
		A[0], A[n] = A[n], A[0]
		# print(A)
		s-=1
		n-=1
		A = Maxheapify(A[:s], 0) + A[s:]
		# print(A)

	# print("Sorted HeapSort")
	# print(A)
	return A



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




def randomData(num):
	array = []
	for i in range(num):
		array.append(random.randint(0, 10000))

	return array

def sortedData(num):
	i = 0
	while i < num:
		array.append(i)
		i+=1

def dataMode():
	points = 1000
	with open("results_1000r.csv", 'w', newline='') as f:
		row = ["n", "HeapSort", "mergeSort", "quickSort"]
		writer = csv.writer(f)
		writer.writerow(row)

	with open("results_1000s.csv", 'w', newline='') as f:
		row = ["n", "HeapSort". "mergeSort", "quickSort"]
		writer = csv.writer(f)
		writer.writerow(row)


	for i in range(1,points):
		###################Random############################
		#Form array of random values
		A = randomData(i)

		#Sort using HeapSort
		start = time.perf_counter()
		sorted = HeapSort(A)
		stop = time.perf_counter()
		HeapSortduration = stop-start


		#Sort using mergeSort
		start = time.perf_counter()
		sorted = mergeSort(A)
		stop = time.perf_counter()
		mergeSortduration = stop-start
	
		#Sort using quickSort
		start = time.perf_counter()
		sorted = quickSort(A)
		stop = time.perf_counter()
		quickSotduration = stop-start
		row = [str(i), str(HeapSortduration), str(mergeSortduration), str(quickSotduration)]
		with open("results_1000r.csv", 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(row)

		###################Sorted############################
		#Form array of sorted values
		A = sortedData(i)

		#Sort using HeapSort
		start = time.perf_counter()
		sorted = HeapSort(A)
		stop = time.perf_counter()
		HeapSortduration = stop-start


		#Sort using mergeSort
		start = time.perf_counter()
		sorted = mergeSort(A)
		stop = time.perf_counter()
		mergeSortduration = stop-start
	
		#Sort using quickSort
		start = time.perf_counter()
		sorted = quickSort(A)
		stop = time.perf_counter()
		quickSotduration = stop-start
		row = [str(i), str(HeapSortduration), str(mergeSortduration), str(quickSotduration)]
		with open("results_1000s.csv", 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(row)

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

		return randomData(num)

	if(sys.argv[1] == "-s"):
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

		return sortedData(num)

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



if __name__ == "__main__":
	A = getinput()
	# print(A)
	if(A == "datamode"):
		exit()

	Hsorted = HeapSort(A)
	# print("Sorted")
	print(Hsorted)
