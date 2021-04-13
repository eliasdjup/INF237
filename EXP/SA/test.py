import numpy as np
# Spatial Resource Allocation
# Minimal dominating set of undirected graph

def MDS(matrix, start):
	s = set()

	'''
	while ( not_dominated )
		big_span = vert with the most white neighbors
		state [ big_span ] = Black
		for ( neighbor of big_span )
			if states [neighbor] is white
				states [ neighbor ] = Green
	'''

	return


cases = int(input())

for c in range(cases):
	v = int(input())
	matrix = np.zeros((v,v))
	unconnected = 0

	for x in range(v):
		lst = [int(i) for i in input().split()]
		if lst[0] == 0:
			unconnected += 1
			continue
		for y in lst[1:]:
			matrix[x,y-1] = 1
	
	print(matrix)
	print(unconnected)

	vert
	for i in range(v):
		r = sum(matrix[:,i])
		if 


	print("-----------------------")
	print()
