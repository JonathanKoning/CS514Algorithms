import sys 
import math
from graph_gen import generate_seq
import heapdict


def Max_Flow_Fat(s, t, graph):
	print("Fat")
	globalFlow = 0
	flow = {}
	paths = []
	V = []
	C = {}
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
	X = []

	#Find s-t path
	# path = []
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
			x = [edge for edge in graph if edge[0] == m[0]]
			# print("x: ", x)
			for u,v,l in x:
				# print(v)
				if(flow[v] < min(flow[u], C[str((u,v))])):
					flow[v] = min(flow[u], C[str((u,v))])
					H[v] = flow[v]
					parent[v] = u
		
		#increase the flow as much as possible
		parent["total"] = flow[t]
		globalFlow += flow[t]
		
		paths.append(parent)
		
		
		#form residual network
		#capacity - flow along s-t path
		for key in parent:
			if key != "total":
				C[str((parent[key], key))] = C[str((parent[key], key))] - parent["total"]
		# for u,v,l in graph:
		# 	flow[v] = l - flow[v]

		#Remove edge from graph if capacity == 0
		for u,v,l in graph:
			if C[str((u,v))] == 0:
				graph.remove((u,v,l))
		
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
	print()

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
		graph = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
		s = 0
		t = 3
		Max_Flow_Fat(s, t, graph)