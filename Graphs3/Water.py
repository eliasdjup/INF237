
from collections import deque

class Graph():
    def __init__(self, graph):
        self.R = graph
        self.V = [i for i in range(len(graph))]

    def addEdge(self, a, b, c):
        self.R[a-1][b-1] += c
        self.R[b-1][a-1] += c
    
    
edges = lambda p: zip(p, p[1:])

def create_path(parents, start, target):
    path = [target]
    while target != start:
        target = parents[target]
        path.append(target)
    return tuple(reversed(path))

def bfs(graph, start, target):
    q = deque([start])
    parents = dict()
    while q:
        v = q.popleft()
        for u in graph.V:
            if u in parents:
                continue
            if graph.R[v][u] <= 0:
                continue
            parents[u] = v
            q.append(u)
            if u == target:
                return create_path(parents, start, target)

def maxflow(graph, start, target):
    flow = 0
    P = bfs(graph, start, target)
    while P != None:
        F = min(graph.R[v][u] for (v, u) in edges(P))
        flow += F
        for i in range(1, len(P)):
            v, u = P[i - 1], P[i]
            graph.R[v][u] -= F
            graph.R[u][v] += F
        P = bfs(graph, start, target)
    return flow


def main():  
    n, p, k = map(int, input().split())
    g = Graph([[0] * n for _ in range(n)])

    for _ in range(p):
        a, b, c = map(int, input().split())
        g.addEdge(a,b,c)

    curr_flow = maxflow(g, 0, 1)
    print(curr_flow)

    for _ in range(k):
        a, b, c = map(int, input().split())

        filter_ = g.R[a-1][b-1] == 0 or g.R[b-1][a-1] == 0
        g.addEdge(a,b,c)

        if filter_:
            curr_flow += maxflow(g, 0, 1)
        print(curr_flow)


if __name__ == '__main__':  
    main()