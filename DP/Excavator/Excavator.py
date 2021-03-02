V,E = [int(x) for x in input().split()]


mapping = {}
seq = input().split()[0]
for i in range(V):
    if seq[i] == 'X':
         mapping[i] = 1
    else:
        mapping[i] = -1
mapping[0] = 0
mapping[V-1] = 0

print(mapping)

graph = {}
for i in range(E):
    F,T = [int(x) for x in input().split()]


    if F in graph:
        graph[F] = graph[F]+[T]
    else:
        graph[F] = [T]

print(graph)