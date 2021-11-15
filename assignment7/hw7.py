import string
import random
import time
import csv

def editDistance(str1, str2):
	print("editDistance")
	D = []
	C_ins = C_del = C_Rep = 1
	for i in range(len(str1)+1):
		arr = []
		arr.append(i)
		# if i == len(str1):
		# 	arr[0] = 0
		for j in range(1,len(str2)):
			if(i==0):
				arr.append(j)
			else:
				arr.append(0)
		arr.append(0)
		D.append(arr)
	
	for i in range(len(str1)):
		for j in range(len(str2)):
			if(str1[i] == str2[j]):
				D[i+1][j+1] = min(D[i][j+1]+C_ins, D[i+1][j]+C_del, D[i][j])
			else:
				D[i+1][j+1] = min(D[i][j+1]+C_ins, D[i+1][j]+C_del, D[i][j]+C_Rep)

	return D[len(str1)][len(str2)]

def strgen(n):
	newstr = ""
	for i in range(n):
		newstr += random.choice('atcg')

	return newstr


def longsub(str1, str2):
	longstr = ""

	i = 0
	k = 0
	while i <len(str1):
		idxs = [idx for idx, value in enumerate(str2) if value==str1[i]]
		for idx in idxs:
			k=0
			tempstr = ""
			while i+k < len(str1) and k+idx < len(str2):
				if(str1[i+k] == str2[k+idx]):
					tempstr+= str1[i+k]
					k+=1
				else:
					break
			if(len(tempstr) > len(longstr)):
				longstr = tempstr
		i+=k
	
	print(longstr)


if __name__ == "__main__":

	longsub("ATCAT", "ATTATC")

	longsub("CGCAATTCTGAAGCGCTGGGGAAGACGGGT", "TATCCCATCGAACGCCTATTCTAGGAT")
	# dist = editDistance("BABBLE", "APPLE")
	# print(dist)

	# dist = editDistance("ATCAT", "ATTATC")
	# print(dist)

	# dist = editDistance("taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat", "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat")
	# print(dist)

	# dist = editDistance("CGCAATTCTGAAGCGCTGGGGAAGACGGGT", "TATCCCATCGAACGCCTATTCTAGGAT")
	# print(dist)

	# dist = editDistance("tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa", "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt")
	# print(dist)

	# with open("results.csv", 'w', newline='') as f:
	# 	row = ["n","time"]
	# 	writer = csv.writer(f)
	# 	writer.writerow(row)
	# n = 100
	# for i in range(1, 31):
	# 	# print("rand")
	# 	print(n*i)
	# 	str1 = strgen(int(n*i))
	# 	str2 = strgen(int(n*i))
	# 	start = time.perf_counter()
	# 	dist = editDistance(str1, str2)
	# 	stop = time.perf_counter()
	# 	# print(stop - start)
	# 	with open("results.csv", 'a', newline='') as f:
	# 		row = [str(n*i), str(stop-start)]
	# 		writer = csv.writer(f)
	# 		writer.writerow(row)
		
		# print(dist)