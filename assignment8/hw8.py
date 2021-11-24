import sys 
import math
from graph_gen import generate_seq
import heapdict
import time


def Max_Flow_Fat(s,t,graph):
	# graph.sort(key=lambda y:y[2])
	# print("Min edge in graph: ", graph[0][2])
	# print("Max_Flow_Fat")
	globalFlow = 0
	flow = {}
	# paths = []
	# E = []
	#Capacity
	C = {}
	#Residual Network
	Cf = {}
	#Set value of each node to 0
	for u,v,l in graph:
		C[(u,v)] = l
		if u not in flow:
			flow[u] = 0
		if v not in flow:
			flow[v] = 0
	flow[s] = 10000
	# H = heapdict.heapdict(flow)
	#Repeat until Stuck
	
	#### Find s-t path##################################################
	#		Start from s and keep adding new edges of highest capacity until
	#		you reach t.
	#		Similar to Dijkstra's except choose nodes with highest additional
	#		flow updated by:
	#		Flow(v) <- Maxu[Min(flow(u), C(u,v))]
	stuck = 0
	while stuck == 0:
		# f = {}
		H = heapdict.heapdict(flow)
		parent = {}
		# print("##### New s-t path ################")
		while t in H:
			
			u = H.popitem()
			if(u[0] == t):
				break
			# Find all neighbors v of u in E with a positive capacity
			E = [edge for edge in graph if edge[0] == u[0] and C[(u[0],edge[1])] > 0]
			# if(u[1] == 0):
			# 	print(E)
			# If there are no neighbors, the current node is not t, and the flow of the next node is 0
			# There is no path to t and so we are stuck 
			# if len(E) == 0 and u[0] != t and H.peekitem()[1]==0:
			if u[1] == 0 and H.peekitem()[1] == 0:
				# print("stuck")
				stuck = 1
				break
			for _,v,l in E:
				# if(v == t):
				# 	print("flow at t: ", flow[v])
				# 	print("flow at u: ", flow[u[0]])
				# 	print("Capacity at u-t: ", C[(u[0],v)])
				# parent[v] = u[0]
				# If current flow at v is < the min(parent node, capacity of edge u,v) then we have found a better path
				if flow[v] < min(flow[u[0]], C[(u[0],v)]):
					flow[v] = min(flow[u[0]], C[(u[0],v)])
					# if(v == t):
					# 	print("New flow at t: ", flow[v])
					# 	print("parent of t is: ", u[0])
					# if(flow[v] == 0):
					# 	print("New flow at: ", v, " is 0")
					H[v] = flow[v]
					# f[str((u[0],v))] = flow[v]
					parent[v] = u[0]
		#### Increase its flow as much as possible
		if(stuck != 0):
			break
		#### Construct residual network#####################################
		#		Given a flow f and a Flow network G=(V,E,C,s,t), define a
		#		residual network with capacities:
		#		Cf(u,v) = C(u,v) - f(u,v) if f(u,v) <= C(u,v) and (u,v) within E
		#				= f(v,u) if (v,u) within E and f(v,u)>u [reverse flow]
		#		Select a new flow in the residual netowrk and and it to previous flows
		# print(parent)
		globalFlow += flow[t]
		# try:
		# 	p = parent[t]
		# except:
		# 	print(flow[t])
		# 	print("globalFlow: ", globalFlow)
		# 	graph.sort(key=lambda y:y[2])
		# 	print("Min edge in graph: ", graph[0][2])
		# 	exit()
		p = parent[t]
		c = t
		bottleneck = flow[t]
		parent[s] = -1
		while c != s:
			C[(p,c)] = C[(p,c)] - bottleneck
			if((p,c) in Cf):
				Cf[(p,c)] = Cf[(p,c)] + bottleneck
			else:
				Cf[(p,c)] = bottleneck
			c = p
			p = parent[c]

		#reset flow to 0		
		for key in flow:
			flow[key] = 0
		flow[s] = 1000000
		# H = heapdict.heapdict(flow)

	#Put flow into proper format
	#This does not seem to affect the time	
	f = []
	for key in Cf:
		# e = tuple(map(int, key[1:-1].split(', ')))
		f.append((key[0],key[1], Cf[key]))
	f.sort(key=lambda y:y[0])
	finalflow = (globalFlow, f)

	return finalflow


def Max_Flow_Short(s, t, graph):
	# print("Short")
	globalFlow = 0
	flow = {}
	# paths = []
	# E = []
	#Capacity
	C = {}
	#Residual Network
	Cf = {}
	#Set value of each node to 0
	for u,v,l in graph:
		C[(u,v)] = l
		if u not in flow:
			flow[u] = 0
		if v not in flow:
			flow[v] = 0
	flow[s] = 10000

	H = []
	H.append(s)
	stuck = 0
	while stuck == 0:
		parent = {}
		stuck = 1
		#### Find s-t path##################################################
		#Breadth first search
		foundt = 0
		while len(H) != 0:
			u = H.pop()
			if(u == t):
				stuck = 0
				break
			E = [edge for edge in graph if edge[0] == u ]
			for _,v,l in E:
				if flow[v] < min(flow[u], C[(u,v)]):
					flow[v] = min(flow[u], C[(u,v)])
					# H[v] = flow[v]
					parent[v] = u
					H.append(v)
					if(v == t):
						foundt = 1
						break
			# if(foundt != 0):
			# 	break				
	
		if(stuck != 0):
			break

		#### Construct residual network#####################################
		#		Given a flow f and a Flow network G=(V,E,C,s,t), define a
		#		residual network with capacities:
		#		Cf(u,v) = C(u,v) - f(u,v) if f(u,v) <= C(u,v) and (u,v) within E
		#				= f(v,u) if (v,u) within E and f(v,u)>u [reverse flow]
		#		Select a new flow in the residual netowrk and and it to previous flows
		globalFlow += flow[t]
		p = parent[t]
		c = t
		bottleneck = flow[t]
		parent[s] = -1
		while c != s:
			C[(p,c)] = C[(p,c)] - bottleneck
			if((p,c) in Cf):
				Cf[(p,c)] = Cf[(p,c)] + bottleneck
			else:
				Cf[(p,c)] = bottleneck
			c = p
			p = parent[c]

		#reset flow to 0		
		for key in flow:
			flow[key] = 0
		flow[s] = 100000
		H.append(s)

	f = []
	for key in Cf:
		# e = tuple(map(int, key[1:-1].split(', ')))
		f.append((key[0], key[1], Cf[key]))
	f.sort(key=lambda y:y[0])
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