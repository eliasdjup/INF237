


V, E = map(int, input().split())

sites = input() # enumerate
sites = [ 1 if x == 'X' else -1 for x in sites]
print(sites)

graph = {}
for i in range(V):
    graph[i] = []

for i in range(E):
    x,y = map(int, input().split())
    graph[x].append(y)


dp = {}
def lp(v):
    if v in dp:
        return dp[v]

    children = [lp(u) for u in graph[v]]

    val = sites[v] + max(children) if children else 0
    dp[v] = val
    return val

#print(graph)

print(lp(0) + 1)

