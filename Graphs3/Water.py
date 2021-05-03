

def printGraph(graph):
    for row in graph:
        print(row)


# n = stations, p = initial pipes, k = improvements
n, p, k = map(int, input().split())
graph = [[0] * n for i in range(n)]

for i in range(p):
    a, b, c = map(int, input().split())
    graph[b-1][a-1] += c


for i in range(k):
    # Capacity between a, b increased by c.
    a, b, c = map(int, input().split())
    graph[b-1][a-1] += c

printGraph(graph)
# Ford fulkerson for each new connection

# Python program for implementation
# of Ford Fulkerson algorithm
