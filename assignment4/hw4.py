import sys 
import math
import random
import csv
import time

solutions = 0
#Backtrace search
def B_Queens(board, row, n, solutions, total):
	if(row == n):
		return solutions, total
	
	#Check if board[row][j] is valid place for queen 
	for j in range(n):
		total+=1
		
		attack = 0
		for k in range(row+1):
			left_diag = j-k
			right_diag = j+k
			up = row-k
			if(left_diag >=0):
				if(board[up][left_diag] == 1):
					attack = 1
					break
			if(board[row-k][j] == 1):
				attack = 1
				break
			if(right_diag < n):
				if(board[up][right_diag] == 1):
					attack = 1
					break
		
		#If valid, recurse
		if(attack == 0):
			board[row][j] = 1
			#If last row, increment solution
			if(row == n-1):
				solutions+=1
				# print("Solution")
				# for i in range(n):
				# 	print(board[i])
				# print(board[row-1][j])
			solutions, total = B_Queens(board,row+1, n, solutions, total)

		board[row][j] = 0

	return solutions, total


#Exhaustive search
def E_Queens(board, row, n, solutions, total):
	# print("B_Queens")
	# for l in range(n):
		# print(board[l])
	attack = 0
	if(row == n):
		total+=1
		#Starting from the bottom so we only have to check in one direction
		for i in range(row-1, -1, -1):
			for j in range(n):
				if(board[i][j] == 1):
					for k in range(1, i+1):
						left_diag = j-k
						right_diag = j+k
						up = i-k
						#upper left diagnal
						if(left_diag >=0):
							if(board[up][left_diag] == 1):
								attack = 1
								break
						#above
						if(board[up][j] == 1):
							attack = 1
							break
						#upper right diagnal
						if(right_diag < n):
							if(board[up][right_diag] == 1):
								attack = 1
								break
						
					if(attack == 1):
						return solutions, total	
		solutions +=1
		return solutions, total			

	for i in range(n):
		board[row][i]=1
		solutions, total = E_Queens(board, row+1, n, solutions, total)
		board[row][i]=0

	return solutions, total

def createBoard(n):
	board = []
	for i in range(n):
		a = []
		for j in range(n):
			a.append(0)
		board.append(a)

	return board

def dataMode():
	points = 8
	with open("results_8.csv", 'w', newline='') as f:
		row = ["n","backtrace", "exhaustive", "Solutions"]
		writer = csv.writer(f)
		writer.writerow(row)

	

	for i in range(4,points):
		# print(i)
		board = createBoard(i)
		
		bstart = time.perf_counter()
		bsolutions, btotal = B_Queens(board, 0, i, 0, 0)
		bstop = time.perf_counter()
		bactraceTime = bstop-bstart

		estart = time.perf_counter()
		esolutions, etotal = E_Queens(board, 0, i, 0, 0)
		estop = time.perf_counter()
		exhaustiveTime = estop-estart

		with open("results_8.csv", 'a', newline='') as f:
			row = [str(i), str(bactraceTime), str(exhaustiveTime), str(btotal)]
			writer = csv.writer(f)
			writer.writerow(row)

		

def getinput():
	board = []
	n = 0

	if(len(sys.argv) == 1):
		n = input("please enter the size of the board: ")
		try:
			n = int(n)
		except:
			pass
		while isinstance(n,int) == False or n <= 0:
			print("Error! Invalid input!")
			n = input("please enter the size of the board: ")
			try:
				n = int(n)
			except:
				pass
			n = input("please enter the size of the board: ")
			try:
				n = int(n)
			except:
				pass

		for i in range(n):
			row = []
			for j in range(n):
				row.append(0)
			board.append(row)

		return board, n

	
	elif(sys.argv[1] == "-d"):
		dataMode()
		return "datamode", 0

	try:
		n = int(sys.argv[1])
	except:
		pass

	while isinstance(n,int) == False or n <= 0:
		print("Error! Invalid input!")
		n = input("please enter the size of the board: ")
		try:
			n = int(n)
		except:
			pass
		n = input("please enter the size of the board: ")
		try:
			n = int(n)
		except:
			pass

	for i in range(n):
		row = []
		for j in range(n):
			row.append(0)
		board.append(row)

	return board, n


if __name__ == "__main__":
	board, n = getinput()
	# print(A)
	if(board == "datamode"):
		exit()

	solutions, total = E_Queens(board, 0, n, 0, 0)
	print("E_Queens: ", solutions)
	# print(solutions)
	# print(total)

	solutions, total = B_Queens(board, 0, n, 0, 0)
	print("B_Queens: ", solutions)
	# print(solutions)
	# print(total)