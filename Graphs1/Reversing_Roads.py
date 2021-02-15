# ctrl-z enter = EOF
# cat .\Graphs1\sample.in | python .\Graphs1\Reversing_Roads.py  
from sys import stdin
import itertools

def dfs(current_node, visited, graph):
    if current_node not in visited:
        visited.append(current_node)
        for neighbour in graph[current_node]:
            dfs(neighbour, visited, graph)
    return visited


iterator = iter(stdin.readlines())
graphs = {}
locations_by_case = []
history = []
case = 0


while True:
    try:
        local_history = []
        m, n = map(int, next(iterator).split())
        locations_by_case.append(m)
        local_history.append((m,n))
        graph = {}
        for i in range(m):
            graph[i] = []
        for inp in range(n):
            a,b =  map(int, next(iterator).split())
            local_history.append((a,b))

            connections = graph.get(a, [])
            connections.append(b)
            graph[a] = connections
        
        history.append(local_history)
        graphs[case] = graph
        case += 1

    except StopIteration:
        break


def checkValidity(graph, locations):
        all_routes = [dfs(x, list(), graph) for x in range(locations)]
        success = True
        for route in all_routes:
            if len(route) != locations: # Are all locations reachable?
                success = False
        return success


#print(graphs[2])
def calc(graphs, locations_by_case):
    for case in range(len(locations_by_case)):

        graph = graphs[case]
        locations = locations_by_case[case]

        success = checkValidity(graph, locations)
        if success:
            print(f"Case {case+1}: valid")
            continue
        else:
            m, n = history[case][0]
            
            valid = False
            for idx, (a,b) in enumerate(history[case][1:]):
                alt_history = history[case].copy()
                alt_history[idx+1] = (b,a)
                valid = checkValidity(toGraph(alt_history), m)
                if valid:
                    break
                
            if valid:
                print(f"Case {case+1}: {a} {b}")
            else:
                print(f"Case {case+1}: invalid")

    
def toGraph(graph_list):
    graph = {}
    m,n = graph_list[0]
    for i in range(m):
        graph[i] = []
    for (a,b) in graph_list[1:]:
        lst = graph[a]
        lst.append(b)
        graph[a] = lst
    return graph
        

calc(graphs, locations_by_case)
        






















#for x in range(locations_in_case):
    #routes.append(dfs(x,set(),graph))
    #dfs(x,set(),graph)
    #print()
    #location_set.add(dfs(0, location_set, graphs[0]))
    #print(location_set)

#if any in locations_by_case not visited...
#invalid


#print(graphs[0])

#print(locations_by_case)
#print(dfs(0, set(), graphs[0]))
