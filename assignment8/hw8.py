import sys 
import math
from graph_gen import generate_seq
import heapdict



def Max_Flow_Fat(s,t,graph):
	# print("Max_Flow_Fat")
	globalFlow = 0
	flow = {}
	paths = []
	E = []
	#Capacity
	C = {}
	#Residual Network
	Cf = {}
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
	while stuck == 0:
		f = {}
		parent = {}
		while t in H:
			u = H.popitem()
			# print(u)
			#find all neighbors v of u in E
			E = [edge for edge in graph if edge[0] == u[0] and C[str((u[0],edge[1]))] > 0]
			# print("E: ",E)
			if len(E) == 0 and u[0] != t and H.peekitem()[1]==0:
				stuck = 1
			for _,v,l in E:
				if flow[v] < min(flow[u[0]], C[str((u[0],v))]):
					flow[v] = min(flow[u[0]], C[str((u[0],v))])
					H[v] = flow[v]
					f[str((u[0],v))] = flow[v]
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
		globalFlow += flow[t]
		p = parent[t]
		c = t
		bottleneck = flow[t]
		parent[s] = -1
		while c != s:
			C[str((p,c))] = C[str((p,c))] - bottleneck
			if(str((p,c)) in Cf):
				Cf[str((p,c))] = Cf[str((p,c))] + bottleneck
			else:
				Cf[str((p,c))] = bottleneck
			c = p
			p = parent[c]

		#reset flow to 0		
		for key in flow:
			flow[key] = 0
		flow[s] = math.inf
		H = heapdict.heapdict(flow)

	#Put flow into proper format	
	f = []
	for key in Cf:
		e = tuple(map(int, key[1:-1].split(', ')))
		f.append((e[0], e[1], Cf[key]))
	f.sort(key=lambda y:y[0])
	finalflow = (globalFlow, f)

	return finalflow


def Max_Flow_Short(s, t, graph):
	print("Short")
	globalFlow = 0
	flow = {}
	paths = []
	E = []
	#Capacity
	C = {}
	#Residual Network
	Cf = {}
	#Set value of each node to 0
	for u,v,l in graph:
		C[str((u,v))] = l
		if u not in flow:
			flow[u] = 0
		if v not in flow:
			flow[v] = 0
	flow[s] = math.inf

	H = []
	H.append[s]
	stuck = 0
	while stuck == 0:
		parent = {}
		#Breadth first search
		while len(H) != 0:
			u = H.pop()
			E = [edge for edge in graph if edge[0] == u[0] and C[str((u[0],edge[1]))] > 0]
			for _,v,l in E:
				


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