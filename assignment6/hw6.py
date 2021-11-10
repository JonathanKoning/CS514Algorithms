from collections import deque
import math
import time 

parent = {}
rank = {}
adder = [0]
def makeset(u):
	# print("makeset")
	parent[u] = u
	rank[u] = 0
	# return parent, rank

def find(x):
	# start = time.perf_counter()
	# print("find")
	u =x
	while(u != parent[u]):
		u = parent[u]
	# end = time.perf_counter()
	# adder[0] += (end-start)
	 
	return u

def union(Rx, Ry):
	# start = time.perf_counter()
	# Rx = find(x, parent)
	# Ry = find(y, parent)
	if(Rx == Ry):
		return
	if(rank[Rx] > rank[Ry]):
		parent[Ry] = Rx
	else:
		parent[Rx] = Ry
		if(rank[Rx] == rank[Ry]):
			rank[Ry] = rank[Ry] + 1

	# end = time.perf_counter()
	# adder[0] += (end-start)
	# return parent, rank

def MST_Kruskel(graph):
	# print("Kruskel")
	# parent = {}
	# rank = {} 
	#Key problem is to check if cycles are going to be formed by adding an edge.
	#Represent each tree as a set of vertices
	#Never add and edge (u,v) if u and v are in the same tree (same set).
	V = []
	X=[]
	count = 0
	#Sort the edges in E by weight
	# start = time.perf_counter()
	sgraph = sorted(graph, key=lambda y: y[2])					#O(e log n)
	# end = time.perf_counter()
	# print(end - start)
	# start = time.perf_counter()
	for edge in sgraph:								#O(e)
		# e+=1
		u = edge[0]
		v = edge[1]
		if u not in V:
			V.append(u)
			makeset(u)
		if v not in V:
			V.append(v)
			makeset(v)
	# print(graph)
	# e = 0
	# end = time.perf_counter()
	# print(end - start)
	# start = time.perf_counter()
	for edge in sgraph:									#O(e)
		# e+=1
		u = edge[0]
		v = edge[1]
		# if u not in V:
		# 	V.append(u)
		# 	makeset(u)
		# if v not in V:
		# 	V.append(v)
		# 	makeset(v)
		#X are the edges within the MST
		if(len(X) == len(V)-1):
			break
			
		pu = find(u)								#O(log(n))
		pv = find(v)							#O(log(n))
		if(pu != pv):
			# X.append((u, v))
			union(pu, pv) #O(1)
			# X[0] += edge[2]
			count += edge[2]
			X.append((u,v))
	# end = time.perf_counter()
	# print(end - start)
	# print(e)
	mst = (count, X)
	return mst




def MST_Prim(graph):
	# print("Prim")
	# Ensure that the selected edges X form a single tree at every stage
	# In every step, select the lightest (least weight) edge that connects to the tree 
	# Add it to the tree and repeat
	# Similar to Dijkstra's algorithm except the priority queue is maintained by the weight of the edge that connects a node to the tree. 
	# Justified by the cut property where 
	# S = nodes in X
	# V-S = nodes not in X
	X = []
	S = []
	# H = []
	count = 0
	#Create list of vertices and weights
	#List of weights is ordered by smallest vertex to largest vertex
	# start = time.perf_counter()
	graph.sort(key=lambda y: y[2])
	# end = time.perf_counter()
	# print(end - start)
	# H.append(graph[0])
	X.append((graph[0][0], graph[0][1]))
	count += graph[0][2]
	# print(count)
	# H = [V[0]]
	S.append(graph[0][0])
	S.append(graph[0][1])
	H = [e for e in graph if(((e[0] in S and e[1] not in S) or (e[0] not in S and e[1] in S)))][0]
	# for edge in H:
	# 	graph.remove(edge)
	while len(H) != 0:
		
		if(H[0] not in S):
			S.append(H[0])
			
		elif(H[1] not in S):
			S.append(H[1])
			
		# H.append(edge)
		X.append((H[0], H[1]))
		# graph.remove(edge)
		count+=H[2]
		try:
			H = [e for e in graph if(((e[0] in S and e[1] not in S) or (e[0] not in S and e[1] in S)))][0]
		except:
			break
		# for edge in J:
		# 	graph.remove(edge)
		
		# H+=J
		# H.sort(key=lambda y: y[2])
		# try:
		# 	#edge = next(filter(lambda e: ((e[0] in S and e[1] not in S) or (e[0] not in S and e[1] in S)), graph))
		# 	# start = time.perf_counter()
		# 	edge = [e for e in graph if(((e[0] in S and e[1] not in S) or (e[0] not in S and e[1] in S)))][0]
		# 	# end = time.perf_counter()
		# 	# print(end-start)
		# except:
		# 	break
		#print("edge: ", edge)
		# print("edge2: ", edge2)
		
		# if(len(edge) > 0):
		# 	if(edge[0] not in S):
		# 		S.append(edge[0])
		# 	elif(edge[1] not in S):
		# 		S.append(edge[1])
			
		# 	# H.append(edge)
		# 	X.append((edge[0], edge[1]))
		# 	# graph.remove(edge)
		# 	count+=edge[2]
	
	mst = (count, X)
	#print(mst)
	return mst

	
	
testarr = []	
for i in range(0, 100):
	for j in range(0, 100):
		for k in range(0, 5):
			testarr.append((i,j,k))
		
			

if __name__ == "__main__":
	# print(len(testarr))
	# start = time.perf_counter()
	# MST_Kruskel(testarr)
	# end = time.perf_counter()
	# print(end - start)

	# print("end testarr")
	
	X = MST_Kruskel(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(X)

	X = MST_Kruskel(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	print(X)

	X = MST_Prim(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(X)

	X = MST_Prim(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	print(X)

	X = MST_Prim(([(1,0,1), (0,2,6), (1,2,2), (1,3,3), (2,3,5), (3,4,2), (3,5,4), (4,5,3)]))
	print(X)

	# start = time.perf_counter()
	# MST_Prim(testarr)
	# end = time.perf_counter()
	# print(end - start)

	X = MST_Prim(([(0,1,2), (2,0,5), (4,1,7), (0,3,3), (3,4,4), (1,3,1)]))
	print(X)
