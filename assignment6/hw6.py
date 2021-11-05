

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


if __name__ == "__main__":
	X = MST_Kruskel(([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
	print(X)

	X = MST_Kruskel(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
	print(X)

