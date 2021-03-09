# Union find
comp = {}
rank = {}

def get_rank(u):
    if u in rank.keys():
        return rank[u]
    return 1

def find(u):
    if u not in comp.keys():
        rank[u] = 1
        comp[u] = u
        return u
    elif comp[u] == u:
        return u
    else:
        parent = find(comp[u])
        comp[u] = parent
        return parent


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    if r1 == r2:
        return rank[r1]
    if rank[r1] <= rank[r2]:
        comp[r1] = r2
        rank[r2] += rank[r1]
    elif rank[r2] < rank[r1]:
        comp[r2] = r1
        rank[r1] += rank[r2]


num_edges = int(input())
for i in range(num_edges):
    u, v = input().split()
    union(u, v)
    print(rank[find(u)])