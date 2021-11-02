# You will be implementing breadth first search to solve a sliding tile puzzle called 8-puzzle (smaller version of 15-puzzle). 
# 
# 8-puzzle has 8 square tiles, numbered from 1 to 8, arranged in a 3 X 3 square area with one of the 9 cells left vacant. Any tile which is adjacent to the empty cell may be moved into the empty cell. The problem is to take one configuration of the puzzle -- the initial state -- to another configuration -- the goal state -- with a sequence of moves. There is an underlying ``state space graph,''  where each vertex corresponds to a configuration of the puzzle and there is an edge from u to v if there is a move that can take the configuration from u to v. Each edge also has a label associated with it - D for down move, U for up move, L for left and R for right. The sequence of labels in the path from the initial state to the goal state is called a solution.   

# For example, the following problem can be solved in 8 moves: D, R, R, U, L, L, D, R.

# start             goal
# 1 2 3             1 2 3
# 4 5 6  ==>    	8   4	
# 8 7               7 6 5

# Your function should be called "ShortestPath", which takes a single goal state and a list of initial states as inputs, then return the list of lengths of the shortest paths from  the initial states to the goal (one per each initial state). Please note that the initial states may be ordered arbitrarily by the testing program. 
# Your program uses single breadth first search to solve all problems by searching backwards from the goal and collects the solution lengths for all the initial states. Use hashing to check if a node has been already visited.
# Input-output format:

# Both initial and goal state is a 3x3 matrix represented by a Python list, from left to right, and from top to bottom, where the empty cell is represented by 0. For example, the start and goal states above would be represented as [1,2,3,4,5,6,8,7,0] and [1,2,3,8,0,4,7,6,5] respectively.
# There might be multiple solutions (i.e. shortest path) for each problem, thus we ask you to return the length of the shortest path.

# To run:
# python -c 'from hw5 import ShortestPath; print( ShortestPath([1,2,3,8,0,4,7,6,5], [[1,2,3,4,5,6,8,7,0], [8, 3, 4, 0, 7, 1, 6, 2, 5]]))'

def ShortestPath(goal, states):
	# print("ShortestPath")
	
	inits = {}
	for i in range(len(states)):
		inits[str(states[i])] = 1000
	# print(inits)
	dist = {}
	level = 0
	dist[str(goal)] = level
	Q = [goal]
	i = 0
	while len(Q) != 0 and i != len(states):
		u = Q.pop(0)
		stru = str(u)
		level = dist[stru] + 1
		#find all neighbors of u
		#up, down, left, right
		empty = u.index(0)
		#check if empty can move up
		# if(empty != 0 and empty != 1 and empty != 2):
		if(empty > 2):
			# print("Move empty up")
			check = u[:]
			check[empty], check[empty-3] = check[empty-3], check[empty]
			strcheck = str(check)
			# if str(check) not in dist:
			if strcheck not in dist:
				dist[strcheck] = level
				if strcheck in inits:
					inits[strcheck] = level
					i+=1
				Q.append(check)
		#check if empty can move down
		# if(empty != 6 and empty != 7 and empty != 8):
		if(empty < 6):
			check = u[:]
			check[empty], check[empty+3] = check[empty+3], check[empty]
			strcheck = str(check)
			# if str(check) not in dist:
			if str(check) not in dist:
				dist[strcheck] = level
				if strcheck in inits:
					inits[strcheck] = level
					i+=1
				Q.append(check)
		#check if empty can move left
		if(empty != 0 and empty != 3 and empty != 6):
			check = u[:]
			check[empty], check[empty-1] = check[empty-1], check[empty]
			strcheck = str(check)
			if strcheck not in dist:
				dist[strcheck] = level
				if strcheck in inits:
					inits[strcheck] = level
					i+=1
				Q.append(check)
		#Check if empty can move right
		if(empty != 2 and empty != 5 and empty != 8):
			check = u[:]
			check[empty], check[empty+1] = check[empty+1], check[empty]
			strcheck = str(check)
			if strcheck not in dist:
				dist[strcheck] = level
				if strcheck in inits:
					inits[strcheck] = level
					i+=1
				Q.append(check)

	
	return list(inits.values())
		