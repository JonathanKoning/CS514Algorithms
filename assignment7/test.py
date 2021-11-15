import random

if __name__ == "__main__":
	p = []
	# d = []
	for i in range(15):
		# p.append((random.randint(1, 10), i+1))
		p.append((i+1, i+1))
		# d.append(i+1)

	k = 4
	print("k = 4")
	print("p: ", p)
	p.sort(key=lambda y:y[0])
	print("p: ", p)
	greed = []
	greed.append(p[0])
	m = 0
	for i in range(len(p)-1, -1, -1):
		valid = 0
		# print(p[i])
		for j in range(len(greed)):
			print("max(p[%d][1]-greed[%d][1], greed[%d][1]-p[%d][1]): %d"%(i,j,j,i, max((p[i][1]-greed[j][1]), (greed[j][1]-p[i][1]))))
			print(p[i][1]-greed[j][1])
			if(max(p[i][1]-greed[j][1], greed[j][1]-p[i][1]) < k):
				valid = 1
				break
		if(valid == 0):
			print(p[i])
			m += p[i][0]
			greed.append(p[i])

	
	greed.sort(key=lambda y:y[1])
	print("mv: ", greed)
	print("m: ", m)
	# print("d: ", d)

	dp = []
	p.sort(key=lambda y:y[1])
	k=0
	m = 0
	while k < len(p):
		m1 = p[k:k+4]
		print(m1)
		m1.sort(key=lambda y:y[0])
		
		# m5 = max(m1,m2,m3,m4)
		dp.append(m1[-1])
		k=m1[0][1]
		k+=4
		m+=m1[-1][0]
	print("dp: ", dp)
	print("m:", m)