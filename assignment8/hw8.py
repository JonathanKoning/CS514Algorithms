import sys 
import math
from graph_gen import generate_seq
import heapdict
import time


def Max_Flow_Fat(s,t,graph):
	# graph.sort(key=lambda y:y[2], reverse=True)
	globalFlow = 0
	#Flow at each node
	flow = {}

	#Capacity at each edge
	Capacity = {}
	
	#Residual Network
	Cf = {}
	
	neighbors = {}
	#Set value of each node to 0
	for u,v,l in graph:
		Capacity[(u,v)] = l # Original graph
		Capacity[(v,u)] = 0 # Residual graph
		if u not in neighbors:
			neighbors[u] = [v]
		else:
			neighbors[u] += [v]
		if v not in neighbors:
			neighbors[v] = [u]
		else:
			neighbors[v] += [u]
		# if u not in flow:
		flow[u] = 0
		# if v not in flow:
		flow[v] = 0
	flow[s] = 1<<30

	#Repeat until Stuck
	
	#### Find s-t path##################################################
	#		Start from s and keep adding new edges of highest capacity until
	#		you reach t.
	#		Similar to Dijkstra's except choose nodes with highest additional
	#		flow updated by:
	#		Flow(v) <- Maxu[Min(flow(u), C(u,v))]
	stuck = 0
	# H = []
	# H = heapdict.heapdict()
	while True:
		H = []
		H = heapdict.heapdict()
		H[s] = flow[s]
		parent = {}
		foundt = 0
		while len(H) != 0:
			try:
				u = H.popitem()
			except:
				stuck = 1
				break
			# print(u)
			# Find all neighbors v of u in E with a positive capacity
			# E = [edge for edge in graph if edge[0] == u[0] and Capacity[(u[0],edge[1])] > 0]
			# E = [key for key in Capacity if(key[0] == u[0] and Capacity[key] > 0)]
			
			# If the current flow is zero, we have gotten stuck
			# if u[1] == 0 and H.peekitem()[1] == 0:
			# 	stuck = 1
			# 	break

			for v in neighbors[u[0]]:
				# If current flow at v is < the min(parent node, capacity of edge u,v) then we have found a better path
				if(Capacity[(u[0], v)] > 0):
					if flow[v] < min(flow[u[0]], Capacity[(u[0],v)]):
						# Update flow of v
						# Increase it's position in H
						flow[v] = min(flow[u[0]], Capacity[(u[0],v)])
						H[v] = flow[v]
						
						# Keep track of the parent of current node to follow path later
						parent[v] = u[0]
						if(v == t):
							foundt = 1
							break
			if(foundt != 0):
				break

		globalFlow += flow[t]
		if(stuck != 0):
			# f = []
			# for key in Cf:
			# 	f.append((key[0],key[1], Cf[key]))
			# f.sort(key=lambda y:y[0])
			finalflow = (globalFlow, flow)
			return finalflow

		#### Increase its flow as much as possible
		# globalFlow += flow[t]

		if(flow[t] == 0):
			return (globalFlow, flow)
		#### Construct residual network#####################################
		#		Given a flow f and a Flow network G=(V,E,C,s,t), define a
		#		residual network with capacities:
		#		Cf(u,v) = C(u,v) - f(u,v) if f(u,v) <= C(u,v) and (u,v) within E
		#				= f(v,u) if (v,u) within E and f(v,u)>u [reverse flow]
		#		Select a new flow in the residual netowrk and and it to previous flows
		
		# try:
		# 	p = parent[t]
		# except:
		# 	print(flow[t])
		# 	print("globalFlow: ", globalFlow)
		# 	graph.sort(key=lambda y:y[2])
		# 	print("Min edge in graph: ", graph[0][2])
		# 	exit()

		#Follow path starting at t
		# print("parent: ", parent)
		p = parent[t]
		c = t
		bottleneck = flow[t]
		parent[s] = -1
		while c != s:
			Capacity[(p,c)] = Capacity[(p,c)] - bottleneck
			Capacity[(c,p)] += bottleneck

			# if((p,c) in Cf):
			# 	Cf[(p,c)] = Cf[(p,c)] + bottleneck
			# else:
			# 	Cf[(p,c)] = bottleneck
			c = p
			p = parent[c]

		#reset flow to 0		
		for key in flow:
			flow[key] = 0
		flow[s] = 1<<30

	#Put flow into proper format
	#This does not seem to affect the time	
	f = []
	# for key in Cf:
	# 	f.append((key[0],key[1], Cf[key]))
	# f.sort(key=lambda y:y[0])
	finalflow = (globalFlow, f)
	print(Capacity)
	return finalflow


def Max_Flow_Short(s, t, graph):
	globalFlow = 0
	# Flow at each node
	flow = {}
	
	# Capacity of each edge
	C = {}
	
	# Residual Network
	Cf = {}
	
	neighbors = {}
	# Set value of each node to 0
	for u,v,l in graph:
		C[(u,v)] = l
		C[(v,u)] = 0
		if u not in neighbors:
			neighbors[u] = [v]
		else:
			neighbors[u] += [v]
		if v not in neighbors:
			neighbors[v] = [u]
		else:
			neighbors[v] += [u]
		# if u not in flow:
		flow[u] = 0
		# if v not in flow:
		flow[v] = 0
	flow[s] = 10000

	stuck = 0
	# graph.sort(key=lambda y:y[2], reverse=True)
	while stuck == 0:
		parent = {}
		stuck = 1
		H = []
		H.append(s)
		#### Find s-t path##################################################
		#Breadth first search
		foundt = 0
		while len(H) != 0:
			u = H.pop()
			# Find all neighbors v of u in E with a positive capacity
			# E = [edge for edge in graph if (edge[0] == u and C[(u,edge[1])] > 0)]
			# E = [key for key in C if(key[0] == u and C[key] > 0)]
			for v in neighbors[u]:
				if(C[(u,v)] > 0):
					if flow[v] < min(flow[u], C[(u,v)]):
						flow[v] = min(flow[u], C[(u,v)])
						parent[v] = u
						H.append(v)
						#If t has been found, the shortest s-t path has been found
						if(v == t):
							stuck = 0
							foundt = 1
							break
			if(foundt != 0):
				break				

		globalFlow += flow[t]
		if(stuck != 0):
			# f = []
			# for key in Cf:
			# 	f.append((key[0], key[1], Cf[key]))
			# f.sort(key=lambda y:y[0])
			finalflow = (globalFlow, flow)

			return finalflow

		#### Construct residual network#####################################
		#		Given a flow f and a Flow network G=(V,E,C,s,t), define a
		#		residual network with capacities:
		#		Cf(u,v) = C(u,v) - f(u,v) if f(u,v) <= C(u,v) and (u,v) within E
		#				= f(v,u) if (v,u) within E and f(v,u)>u [reverse flow]
		#		Select a new flow in the residual netowrk and and it to previous flows
		
		p = parent[t]
		c = t
		bottleneck = flow[t]
		parent[s] = -1
		while c != s:
			C[(p,c)] = C[(p,c)] - bottleneck
			C[(c,p)] += bottleneck
			# if((p,c) in Cf):
			# 	Cf[(p,c)] = Cf[(p,c)] + bottleneck
			# else:
			# 	Cf[(p,c)] = bottleneck
			c = p
			p = parent[c]

		#reset flow to 0		
		for key in flow:
			flow[key] = 0
		flow[s] = 10000

	f = []
	
	finalflow = (globalFlow, f)

	return finalflow

if __name__ == "__main__":

	rand_test = 0
	graph = []
	if len(sys.argv) != 1:
		if(sys.argv[1] == '-r'):
			rand_test = 1

	if rand_test !=0:
		graph = generate_seq(5,5,5)

	else:
		graph = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
		# graph = [(0,1,10), (0,2,20), (1,2,2), (1,3,4), (1,4,8), (2,4,9), (3,5,10), (4,3,6), (4,5,10)]
		# graph = [(0,1,10),(0,2,10), (1,2,10),(1,3,10), (2,3,10)]
		s = 0
		t = 3
		# Max_Flow_Fat(s, t, graph)
		flow = Max_Flow_Fat(s, t, graph)
		print(flow)

		flow = Max_Flow_Short(s, t, graph)
		print(flow)

		# graph = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
		# graph = [(0,1,10), (0,2,20), (1,2,2), (1,3,4), (1,4,8), (2,4,9), (3,5,10), (4,3,6), (4,5,10)]
		# graph = [(0,1,10),(0,2,10), (1,2,10),(1,3,10), (2,3,10)]
		graph = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
		s = 0
		t = 4
		# Max_Flow_Fat(s, t, graph)
		flow = Max_Flow_Fat(s, t, graph)
		print(flow)

		flow = Max_Flow_Short(s, t, graph)
		print(flow)


		#Large Test case, This should have a max flow of 440
		#Must complete in under 4 seconds
		dense_tuples1 = generate_seq(100, 5000, 1)
		
		def maxG(G): return max([max(x[0], x[1]) for x in G])
		start = time.perf_counter()
		flow = Max_Flow_Fat(0, maxG(dense_tuples1), dense_tuples1)
		stop = time.perf_counter()
		print("Time: ", stop-start)
		print("max flow: ", flow[0])


		start = time.perf_counter()
		flow = Max_Flow_Short(0, maxG(dense_tuples1), dense_tuples1)
		stop = time.perf_counter()
		print("Time: ", stop-start)
		print("max flow: ", flow[0])