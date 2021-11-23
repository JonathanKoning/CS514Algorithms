import sys 
import math
from graph_gen import generate_seq
import heapdict



def psuedoCode(s,t,graph):
	print("psuedoCode")
	globalFlow = 0
	flow = {}
	paths = []
	E = []
	#Capacity
	C = {}
	#Residual Network
	Cf = {}
	print("graph:\t", graph)
	#Set value of each node to 0
	for u,v,l in graph:
		C[str((u,v))] = l
		if u not in flow:
			flow[u] = 0
		if v not in flow:
			flow[v] = 0
	flow[s] = math.inf
	H = heapdict.heapdict(flow)
	#Repeat until Stuck
	
	#### Find s-t path##################################################
	#		Start from s and keep adding new edges of highest capacity until
	#		you reach t.
	#		Similar to Dijkstra's except choose nodes with highest additional
	#		flow updated by:
	#		Flow(v) <- Maxu[Min(flow(u), C(u,v))]
	stuck = 0
	while stuck < 5:
		f = {}
		parent = {}
		while t in H:
			u = H.popitem()
			# print(u)
			#find all neighbors v of u in E
			E = [edge for edge in graph if edge[0] == u[0] and C[str((u[0],edge[1]))] > 0]
			print(E)
			if len(E) == 0 and u[0] != t:
				stuck = 1
			for _,v,l in E:
				if flow[v] < min(flow[u[0]], C[str((u[0],v))]):
					flow[v] = min(flow[u[0]], C[str((u[0],v))])
					H[v] = flow[v]
					f[str((u[0],v))] = flow[v]
					parent[v] = u[0]
		#### Increase its flow as much as possible
		stuck +=1
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
		print(bottleneck)
		print("C: ", C)
		while c != s:
			print("p: ", p)
			print("c: ", c)
			print("C[str((p,c))]: ", C[str((p,c))] )
			C[str((p,c))] = C[str((p,c))] - bottleneck
			print("Adjusted for bottleneck")
			print("C[str((p,c))]: ", C[str((p,c))] )
			# flow[c] = C[str((p,c))]
			c = p
			p = parent[c]

		print("C: ", C)
		for key in flow:
			flow[key] = 0

		flow[s] = math.inf
		# for key in f:
		# 	if f[key] <= C[key]:
		# 		Cf[key] = C[key] - f[key]
		# 		flow[v] = Cf[key]
		print("flow:\t",flow)
		
		H = heapdict.heapdict(flow)


def Max_Flow_Fat(s, t, graph):
	print("Fat")
	globalFlow = 0
	flow = {}
	paths = []
	V = []
	#Capacity
	C = {}
	#Residual Network
	CF = {}
	for u,v,l in graph:
		C[str((u,v))] = l
		if u not in flow:
			flow[u] = 0
			V.append(u)
		if v not in flow:
			flow[v] = 0
			V.append(v)
	
	flow[s] = math.inf
	H = heapdict.heapdict(flow)
	print(H[s])
	X = []
	print(C)
	#Find s-t path##################################################
	# Start from s and keep adding new edges f highest capacity until
	# you reach t.
	# Similar to Dijkstra's except choose nodes with highest additional
	# flow updated by:
	# Flow(v) <- Maxu[Min(flow(u), C(u,v))]
	# path = []
	i = 0
	while True:
		parent = {}
		if(t not in H):
			break

		while t in H:
			m = H.popitem()
			# path.append(m[0])
			print("m: ", m)
			# print(graph)
			#for all neighbors of m
			x = [edge for edge in graph if edge[0] == m[0] and C[str((edge[0], edge[1]))]>0]
			print("x: ", x)
			# if(len(x) == 0):
			# 	i = 1
			# 	break
			# print("x: ", x)
			for u,v,l in x:
				# print(v)
				if(flow[v] < min(flow[u], C[str((u,v))])):
					flow[v] = min(flow[u], C[str((u,v))])
					H[v] = flow[v]
					parent[v] = u
		print("t was in H")
		# if(i != 0):
		#increase the flow as much as possible##########################
		parent["total"] = flow[t]
		globalFlow += flow[t]
		print(parent)
		print(globalFlow)
		# break
		
		paths.append(parent)
		
		
		#form residual network##########################################
		#Given a flow f and a Flow network G=(V,E,C,s,t), define a
		#residual network with capacities:
		#Cf(u,v) = C(u,v) - f(u,v) if f(u,v) <= C(u,v) and (u,v) within E
		#		 = f(u,v) if (u,v) within E and f(v,u)>u [reverse flow]
		#Select a new flow in the residual netowrk and and it to previous flows

		#capacity - flow along s-t path
		for key in parent:
			if key != "total":
				C[str((parent[key], key))] = C[str((parent[key], key))] - parent["total"]
		# for u,v,l in graph:
		# 	flow[v] = l - flow[v]
		print(C)
		#Remove edge from graph if capacity == 0
		# for u,v,l in graph:
		# 	if C[str((u,v))] == 0:
		# 		graph.remove((u,v,l))
		
		#reset flow chart
		for key in flow:
			flow[key] = 0
		
		flow[s] = math.inf
		#TODO how to reform heap with disjointed graph?
		H = heapdict.heapdict(flow)
	# for i in range(len(H)):
	# 	print(H.popitem())
	# print(flow[t])
	# print(flow)
	print(globalFlow)

def Max_Flow_Short(s, t, graph):
	print("Short")


if __name__ == "__main__":

	rand_test = 0
	graph = []
	if len(sys.argv) != 1:
		if(sys.argv[1] == '-r'):
			rand_test = 1

	if rand_test !=0:
		graph = generate_seq(5,5,5)

	else:
		# graph = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
		graph = [(0,1,10), (0,2,10), (1,2,2), (1,3,4), (1,4,8), (2,4,9), (3,5,10), (4,3,6), (4,5,10)]
		s = 0
		t = 5
		# Max_Flow_Fat(s, t, graph)
		psuedoCode(s, t, graph)