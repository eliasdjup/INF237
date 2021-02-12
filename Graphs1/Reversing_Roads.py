# ctrl-z enter = EOF
# cat .\Graphs1\sample.in | python .\Graphs1\Reversing_Roads.py  
from sys import stdin
import itertools

def dfs(current_node, visited, graph):
    if current_node not in visited:
        visited.add(current_node)
        for neighbour in graph[current_node]:
            dfs(neighbour, visited, graph)
    return visited


iterator = iter(stdin.readlines())
graphs = {}
locations_by_case = []
case = 0
while True:
    try:
        m, n = map(int, next(iterator).split())
        locations_by_case.append(m)
        graph = {}
        for inp in range(n):
            a,b =  map(int, next(iterator).split())
            connections = graph.get(a, [])
            connections.append(b)
            graph[a] = connections

            connections = graph.get(b, [])
            connections.append(a)
            graph[b] = connections
        
        graphs[case] = graph
        case += 1

    except StopIteration:
        break
    except EOFError: # Trengs nok ikke da iteratoren sender stopiteration exception
        break

for index, locations_in_case in enumerate(locations_by_case):
    location_set = set()
    for i in range(locations_in_case):
        
        [location_set.add(x) for x in dfs(0, location_set, graphs[index])]
        #location_set.add(dfs(0, location_set, graphs[0]))
        #print(location_set)
    
    #if any in locations_by_case not visited...
    #invalid


print(graphs[0])

print(locations_by_case)
print(dfs(0, set(), graphs[0]))
