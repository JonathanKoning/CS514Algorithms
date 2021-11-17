import random
import math

def dynamic(p, k):
	# max = 0
	# for value, dist in p:
	# graph={}
	# print("len(p): ",len(p))
	dist = {}
	prev = {}
	# rank = {}
	# dist = {}
	for value, d in p:
		dist[d] = value
		prev[d] = -1

	#For each starting node (there will be k of them)
	#i is the root node
	#j is the next node
	# for level in range(1, int(math.floor((len(p)-1)/k))+1):
	h = []
	for i in range(k):
		h.append(i)

	while len(h) != 0:
		parent = h.pop(0)
		for i in range(k):
			child = parent + k + i
			if child < len(p):
				# print("Parent: ", parent)
				# print("child: ",child)
				if (( p[child][0] + dist[p[parent][1]] ) > dist[p[child][1]]):
					# print(dist)
					prev[p[child][1]] = p[parent][1]
					dist[p[child][1]] = p[child][0] + dist[p[parent][1]]
					# print(dist)
					h.append(child)



	# for i in range(k):
	# 	print("\ni:", i)
	# 	for level in range(1, int(math.floor((len(p)-1)/k))+1):
	# 		print("Level: ", level)
	# 		for j in range(k):
	# 			print("j: ", j)
	# 			child = int(i+((level*k)+j))
	# 			parent = int(child-(j+k))
				
	# 			if child < len(p):
	# 				print("Parent: ", parent)
	# 				print("child: ",child)
	# 				if (( p[child][0] + dist[p[parent][1]] ) > dist[p[child][1]]):
	# 					print(dist)
	# 					prev[p[child][1]] = p[parent][1]
	# 					dist[p[child][1]] = p[child][0] + dist[p[parent][1]]
	# 					print(dist)
	
	# print("dist: ",dist)
	# print(prev)
	# print(max(dist.values()))
	n = max(dist, key=dist.get)
	best = []
	while n != -1:
		best = [p[n]] + best
		# best.append(n)
		n = prev[n]
	print("k = ",k)
	print("p:\t", p)
	print("best\t", best)
	print(max(dist.values()))
				

	
def rodcut(X, n):
	
	ropes = [[0,n]]
	sequence = []
	cost = 0
	while len(sequence) < len(X):
		# print("ropes: ", ropes)
		for i in range(len(ropes)):
			# print("rope: ", ropes)
			cut = -1
			dist = n+1
			cuts = [x for x in X if x>ropes[i][0] and x < ropes[i][1]]
			# print("cuts: ", cuts)
			for x in cuts:
				# print(x)
				mid = ropes[i][0] + ((ropes[i][1] - ropes[i][0])/2)
				if(abs(mid-x) < dist):
					cut = x
					dist = abs(mid - x)
			if(cut > 0):
				cost += (ropes[i][1] - ropes[i][0])
				sequence.append(cut)
				newrope = [ropes[i][0], cut]
				# print("cut: ", cut)
				ropes[i][0] = cut
				ropes.append(newrope)


	# print(sequence)
	# print(cost)
	

	



if __name__ == "__main__":
	# p = [(10,0),(1, 1), (9, 2), (4, 3), (2, 4), (7, 5), (5, 6), (9, 7), (1, 8), (2, 9), (9, 10), (9, 11), (6, 12), (3, 13), (7, 14)]
	# d = []
	# p = [(10, 0), (7, 1), (1, 2), (5, 3), (1, 4), (2, 5), (8, 6), (1, 7), (9, 8), (10, 9)]
	p = []
	for i in range(10):
		p.append((random.randint(1, 10), i))
		# p.append((i+1, i+1))
		# d.append(i+1)

	k = 2
	# print("k = ",k)
	# print("p: ", p)
	dynamic(p,k)

	# print("k = ",k)
	# print("p: ", p)
	p.sort(key=lambda y:y[0])
	# print("p: ", p)
	greed = []
	greed.append(p[-1])
	m = 0
	m+=p[-1][0]
	for i in range(len(p)-1, -1, -1):
		valid = 0
		# print(p[i])
		for j in range(len(greed)):
			# print("max(p[%d][1]-greed[%d][1], greed[%d][1]-p[%d][1]): %d"%(i,j,j,i, max((p[i][1]-greed[j][1]), (greed[j][1]-p[i][1]))))
			# print(p[i][1]-greed[j][1])
			if(max(p[i][1]-greed[j][1], greed[j][1]-p[i][1]) < k):
				valid = 1
				break
		if(valid == 0):
			# print(p[i])
			m += p[i][0]
			greed.append(p[i])

	
	greed.sort(key=lambda y:y[1])
	print("greedy:\t",greed)
	print("m: ", m)
	# print("d: ", d)

	

	dp = []
	p.sort(key=lambda y:y[1])
	d=0
	m = 0
	while d < len(p):
		# print("k=",k)
		m1 = p[d:d+k]
		# print(m1)
		m1.sort(key=lambda y:y[0])
		# print(m1)
		# m5 = max(m1,m2,m3,m4)
		dp.append(m1[-1])
		d=m1[-1][1]
		d+=k
		m+=m1[-1][0]
	print("dp:\t", dp)
	print("m:", m)



	rodcut([1,2,3,4,5], 8)

	rodcut([1,3,4,5], 7)