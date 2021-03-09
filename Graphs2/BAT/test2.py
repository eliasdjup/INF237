def find(v):
    r = v
    p = parent.get(r,r)

    while (r != p):
        pp = parent.get(p,p)
        parent[r] = pp
        r = parent[r]
    return r
    
def union(a,b):
    a = find(a)
    b = find(b)

    ra = rank.get(a,1)
    rb = rank.get(b,1)

    if ra > rb:
        parent[b] = a
        rank[a] = ra + rb
        print(rank[a])
    
    elif rb > ra:
        parent[a] = b
        rank[b] = rb + ra
        print(rank[b])
        
    else:
        parent[b] = a
        rank[a] = ra + rb
        print(rank[a])

n = int(input())

if n == 0:
    print(0)
    exit()

parent = {}
rank = {}
for i in range(n):
    a,b = input().split(" ")
    union(a,b)