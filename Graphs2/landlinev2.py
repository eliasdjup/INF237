import sys
comp = {}
rank = {}

inputs = []

network_cost = 0

def find(u):
    if u not in comp.keys():
        rank[u] = 1
        comp[u] = u
        return u
    if comp[u] == u:
        return u
    else:
        parent = find(comp[u])
        comp[u] = parent
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
        rank[r2] += rank[r1]

n, m, p = map(int, input().split())

if n == 0:
    sys.exit()
elif n-1 > m:
    print("impossible")
    sys.exit()

insecure = []
if p > 0:
    insecure = list(map(int, input().split()))

for i in range(m):
    b1, b2, c = map(int, input().split())
    inputs.append((b1, b2, c))

inputs.sort(key = lambda x: x[2])

insecure_edges = []

for i in inputs:
    b1, b2, c = i
    u = find(b1)
    v = find(b2)
    if u in insecure or v in insecure:
        insecure_edges.append((b1,b2,c))
        continue
    if u != v: # Different components
        union(u, v)
        network_cost += c


for (b1, b2, c) in insecure_edges:
    if find(b1) != find(b2) and (not (b1 in insecure and b2 in insecure)):
        union(b1, b2)
        network_cost += c

if len(insecure) == n: # all nodes are insecure
    for (b1, b2, c) in inputs:
        if find(b1) != find(b2):
            union(b1, b2)
            network_cost += c

for i in range(1, n+1):
    if find(1) != find(i): # Not all buildings included in network
        print("impossible")
        sys.exit()

print(network_cost)

# Det er kun kommunikasjon som går fra en sikker node til en
# annen node gjennom en usikker node som ikke er lov. Det vil
# si at 2 1 2 -> 1 2 -> 1 2 1 er lov!

# Må kanskje sjekke at det finnes en trygg, deretter sjekket at alle
# andre trygge er i samme komponent


#2 1 2
#1 2
#1 2 1
#1 <- return

#print(comp)
#print(network_cost)
#print(insecure_edges)
