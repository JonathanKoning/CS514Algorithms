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
	X=[0]
	#Sort the edges in E by weight
	graph.sort(key=lambda y: y[2])
	# print(graph)
	for edge in graph:
		u = edge[0]
		v = edge[1]
		if(find(u, parent) != find(v, parent)):
			# X.append((u, v))
			parent, rank = union(u, v, parent, rank)
			X[0] += edge[2]
			X.append((u,v))

	return X




def MST_Prim(graph):
	print("Prim")
	# Ensure that the selected edges X form a single tree at every stage
	# In every step, select the lightest (least weight) edge that connects to the tree 
	# Add it to the tree and repeat
	# Similar to Dijkstra’s algorithm except the priority queue is maintained by the weight of the edge that connects a node to the tree. 
	# Justified by the cut property where 
	# S = nodes in X
	# V-S = nodes not in X
	cost = {}
	prev = {}
	w = {}
	E = []
	X = [0]
	S = []
	V = []
	#Create list of vertices and weights
	#List of weights is ordered by smallest vertex to largest vertex
	for edge in graph:
		# print("edge")
		# print(edge)
		u = edge[0]
		v = edge[1]
		if u not in V:
			V.append(u)
		if v not in V:
			V.append(v)
		
		if v < u:
			u, v = v, u
		
		w[(u,v)] = edge[2]
		E.append((u,v))
		
	for u in V:
		cost[u] = math.inf
		prev[u] = -1

	# print(V)
	V.sort()
	# print(V)
	cost[V[0]] = 0
	# print(H)
	H = [V[0]]
	while len(H) != 0:
		u = H.pop(0)
		for (u, v) in E:
			if cost[v] > w[(u,v)]:
				cost[v] = w[(u,v)]
				prev[v] = u
				# X[0] += cost[v]
				# X.append((u,v))
				H.append(v)

	for key in prev:
		# print(prev[key])
		# if(not prev[key]):
			# print(prev[key])
		if (prev[key] != -1):
			X[0] += w[(prev[key], key)]
			X.append((prev[key], key))

	return X
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
	X = MST_Kruskel(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(X)

	X = MST_Kruskel(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	print(X)

	X = MST_Prim(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	print(X)

	X = MST_Prim(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(X)