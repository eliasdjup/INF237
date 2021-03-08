import sys

n, m, p = map(int, input().split())
insecure = list(map(int, input().split()))
secures = list(range(1, n+1))
[secures.remove(x) for x in insecure]


comp = {}
rank = {}
mst = []
inputs = []
cost = 0


for _ in range(m):
    b1, b2, c = map(int, input().split())
    inputs.append((c, b1, b2))

if n-1 > m:
    if n == 1:
        print(cost)
    else:
        print("impossible")
    sys.exit()

def find(u):
    if u not in comp.keys():
        rank[u] = 1
        comp[u] = u
        return u
    if comp[u] == u:
        return u
    else:
        parent = find(comp[u])
        comp[u] = parent # update
        return parent


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    if rank[r1] < rank[r2]:
        comp[r1] = r2
    elif rank[r2] < rank[r1]:
        comp[r2] = r1
    else:
        comp[r1] = r2
        rank[r2] += 1 

queue = []
edges = sorted(inputs)
for (w, u, v) in edges:
    if (u in insecure or v in insecure):
        queue.append((w,u,v))
        continue
    if find(u) != find(v):
        mst.append((u, v)) # Kan hende dette er dumt, må kanskje bruke comp istedenfor
        cost += w
        union(u, v)

# Sjekker at alle secure bygninger er i samme komponent
if secures:
    for i in secures:
        if find(secures[0]) != find(i):
            print("impossible")
            sys.exit()

#mst is now secure, must connect insecure as leafs
for (w, u, v) in queue:
    if find(u) != find(v) and (not (u in insecure and v in insecure)):
        mst.append((u, v))
        cost += w
        union(u, v)

if (len(mst) != n-1):
    print("impossible")
else:
    print(cost)


'''
3 2 2
1 3
1 2 1
2 3 1

5 4 2
1 2
3 4 1
4 5 1
1 5 1
2 1 1

2 1 0

1 2 10



3 1 0

1 2 10



3 2 0

1 2 10
2 3 10

3 2 1
1
1 2 10
2 3 10


4 3 1
1 4
1 2 10
2 3 10
3 4 10


4 3 1
1 2
1 2 10
2 3 10
3 4 10

2 1 2
1 2
1 2 1

10 9 3
1 3 8
2 4 1
4 5 1
5 6 1
6 7 1
7 9 1
9 10 1
1 2 10
3 8 4
8 10 10


4 2 2
1 4
1 2 1
3 4 1

4 3 2
1 4
1 2 1
3 4 1
2 3 1


4 3 2
1 4
1 2 1
3 4 1
1 4 1

3 2 1
2 3
1 2 3
2 3 1

3 2 3
1 2 3
1 2 1
2 3 1


5 7 2
1 2
1 2 1
2 3 1 
3 4 1
4 5 1
1 5 1
2 5 1
3 5 1


5 5 2
1 2
1 2 1
2 3 1 
3 4 1
4 5 1
3 5 1

10 10 2
1 10
1 2 1
2 3 1
3 4 1
4 5 1
2 7 1
6 7 1
7 8 1
8 9 1
9 10 1
10 6 1


5 6 1
1 2 4 5
1 3 1
2 3 1 
3 4 1
3 5 1
1 5 1
2 4 1

5 5 1
1 2 4 5
2 3 1 
3 4 1
3 5 1
1 5 1
2 4 1

3 2 3
1 2 3
1 2 1 
1 3 1

3 2 1
2
1 2 1 
1 3 1

'''
#print(secures)

