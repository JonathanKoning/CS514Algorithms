import math

def makeset(u, parent, rank):
	# print("makeset")
	parent[u] = u
	rank[u] = 0
	return parent, rank

def find(x, parent):
	# print("find")
	while(x != parent[x]):
		x = parent[x]
	return x

def union(x, y, parent, rank):
	Rx = find(x, parent)
	Ry = find(y, parent)
	if(Rx == Ry):
		return
	if(rank[Rx] > rank[Ry]):
		parent[Ry] = Rx
	else:
		parent[Rx] = Ry
		if(rank[Rx] == rank[Ry]):
			rank[Ry] = rank[Ry] + 1

	return parent, rank

def MST_Kruskel(graph):
	# print("Kruskel")
	parent = {}
	rank = {} 
	#Key problem is to check if cycles are going to be formed by adding an edge.
	#Represent each tree as a set of vertices
	#Never add and edge (u,v) if u and v are in the same tree (same set).
	V = []
	for edge in graph:
		# print("edge")
		# print(edge)
		if edge[0] not in V:
			V.append(edge[0])
		if edge[1] not in V:
			V.append(edge[1])
	
	for u in V:
		parent, rank = makeset(u, parent, rank)
	# print("V")
	# print(V)
	# print("parent")
	# print(parent)
	# print("rank")
	# print(rank)
	X=[]
	count = 0
	#Sort the edges in E by weight
	graph.sort(key=lambda y: y[2])
	# print(graph)
	for edge in graph:
		u = edge[0]
		v = edge[1]
		if(find(u, parent) != find(v, parent)):
			# X.append((u, v))
			parent, rank = union(u, v, parent, rank)
			# X[0] += edge[2]
			count += edge[2]
			X.append((u,v))
	mst = (count, X)
	return mst




def MST_Prim(graph):
	# print("Prim")
	# Ensure that the selected edges X form a single tree at every stage
	# In every step, select the lightest (least weight) edge that connects to the tree 
	# Add it to the tree and repeat
	# Similar to Dijkstra’s algorithm except the priority queue is maintained by the weight of the edge that connects a node to the tree. 
	# Justified by the cut property where 
	# S = nodes in X
	# V-S = nodes not in X
	# cost = {}
	# prev = {}
	# w = {}
	# E = []
	X = []
	S = []
	# V = []
	H = []
	count = 0
	#Create list of vertices and weights
	#List of weights is ordered by smallest vertex to largest vertex
	# for edge in graph:
	# 	# print("edge")
	# 	# print(edge)
	# 	u = edge[0]
	# 	v = edge[1]
	# 	if u not in V:
	# 		V.append(u)
	# 		cost[u] = math.inf
	# 		prev[u] = -1	
	# 	if v not in V:
	# 		V.append(v)
	# 		cost[v] = math.inf
	# 		prev[v] = -1
		# if v < u:
		# 	u, v = v, u
		
		# w[(u,v)] = edge[2]
		# E.append((u,v))
		
	# for u in V:
	# 	cost[u] = math.inf
	# 	prev[u] = -1

	# print(V)
	# V.sort()
	# print(V)
	# cost[V[0]] = 0
	# print(H)
	graph.sort(key=lambda y: y[2])
	
	H.append(graph[0])
	X.append((H[0][0], H[0][1]))
	count += H[0][2]
	# H = [V[0]]
	S.append(H[0][0])
	S.append(H[0][1])
	while len(H) != 0 and len(S) != len(V):
		# print("H: ",H)
		n = H.pop(0)
		# print("n: ", n)
		edge = [e for e in graph if(((e[0] in S and e[1] not in S) or (e[0] not in S and e[1] in S)))]
		# print("edge: ", edge)
		edge.sort(key=lambda y: y[2])
		
		if(len(edge) > 0):
			if(edge[0][0] not in S):
				S.append(edge[0][0])
			elif(edge[0][1] not in S):
				S.append(edge[0][1])
			
			H.append(edge[0])
			X.append((edge[0][0], edge[0][1]))
			count+=edge[0][2]
	
	mst = (count, X)
	return mst
	
	
	# while len(H) != 0:
	# 	n = H.pop(0)
	# 	print(n)
	# 	e = [(u,v) for (u,v) in E if((u==n or v==n) and ((u in S and v not in S) or (u not in S and v in S)))] 
	# 	print(e)
	# 	minw = math.inf
	# 	mine=[0]
	# 	for (u, v) in e:
			
	# 		if(n == u):
	# 			if cost[v] > w[(u,v)] and v not in S:
	# 				cost[v] = w[(u,v)]
	# 				if(w[u,v] < minw):
	# 					minw = w[(u,v)]
	# 					mine[0] = (u,v)
	# 				# prev[v] = u
	# 		# 		S.append(v)
	# 		# 		H.append(v)
	# 		if(n == v):
	# 			if cost[u] > w[(u, v)] and u not in S:
	# 				cost[u] = w[(u,v)]
	# 				if(w[(u,v)] < minw):
	# 					minw=w[(u,v)]
	# 					mine[0] = (u,v)
	# 		# 		prev[u] = v
	# 		# 		S.append(u)
	# 		# 		H.append(u)
	# 	if(u not in S):
	# 		S.append(mine[0][0])
	# 		prev[u] = v
	# 		H.append(u)
	# 	if(v not in S):
	# 		S.append(mine[0][1])
	# 		prev[v] = u
	# 		H.append(v)
	# for key in prev:
	# 	print(prev)
	# 	# print(prev[key])
	# 	# if(not prev[key]):
	# 		# print(prev[key])
	# 	if (prev[key] != -1):
	# 		if ((prev[key], key) in E):
	# 			X[0] += w[(prev[key], key)]
	# 			X.append((prev[key], key))
	# 		if ((key, prev[key]) in E):
	# 			X[0] += w[(key, prev[key])]
	# 			X.append((key, prev[key]))

	# return X
	# H.sort(key=lambda y: y[2])

	# while(len(H) != 0):
	# 	u = H.pop(0)
	# 	u = u[]
		

	#Sort the edges in E by weight
	# graph.sort(key=lambda y: y[2])
	# H = [graph[0]]
	# while(len(V) != 0):
	# 	u = H[0][0]
	# 	v = H[0][1]
	# 	X[0] = H[0][2]
	# 	X.append((u, v))
	# 	if(u in V):
	# 		V.pop(V.index())
	# 	if(v in V):
	# 		V.pop(V.index(v))


		
		# S.append(H[0][0])
		# S.append(H[0][1])




	


if __name__ == "__main__":
	# X = MST_Kruskel(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	# print(X)

	# X = MST_Kruskel(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	# print(X)

	# X = MST_Prim(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	# print(X)

	# X = MST_Prim(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	# print(X)

	X = MST_Prim(([(1,0,1), (0,2,6), (1,2,2), (1,3,3), (2,3,5), (3,4,2), (3,5,4), (4,5,3)]))
	print(X)